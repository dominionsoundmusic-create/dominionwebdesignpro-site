// SEO audit for the Site Check tool (/site-check/).
// Fetches a public web page plus its robots.txt and sitemap, and returns plain-English checks.
// Speed scores come from Google PageSpeed Insights, which the page calls directly.
import { lookup } from "node:dns/promises";
import net from "node:net";

export const config = { path: "/api/seo-audit" };

const UA = "Mozilla/5.0 (compatible; DominionSiteCheck/1.0; +https://dominionwebdesignpro.com/site-check/)";
const TIMEOUT = 12000;
const MAX_BYTES = 3_000_000;

function json(body, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store", "access-control-allow-origin": "*" },
  });
}

function privateIp(ip) {
  if (net.isIPv4(ip)) {
    const [a, b] = ip.split(".").map(Number);
    return a === 10 || a === 127 || a === 0 || (a === 169 && b === 254) || (a === 172 && b >= 16 && b <= 31) ||
      (a === 192 && b === 168) || (a === 100 && b >= 64 && b <= 127) || a >= 224;
  }
  const v = ip.toLowerCase();
  return v === "::1" || v === "::" || v.startsWith("fc") || v.startsWith("fd") || v.startsWith("fe80") || v.startsWith("::ffff:127.") || v.startsWith("::ffff:10.") || v.startsWith("::ffff:192.168.");
}

async function safeHost(u) {
  if (!/^https?:$/.test(u.protocol)) return false;
  if (u.port && !["80", "443"].includes(u.port)) return false;
  const host = u.hostname;
  if (!host.includes(".") || host.endsWith(".local") || host.endsWith(".internal")) return false;
  try {
    const addrs = await lookup(host, { all: true });
    return addrs.length > 0 && addrs.every((a) => !privateIp(a.address));
  } catch { return false; }
}

async function get(url, { redirects = 5 } = {}) {
  let current = new URL(url);
  const chain = [];
  for (let i = 0; i <= redirects; i++) {
    if (!(await safeHost(current))) throw new Error("blocked");
    const ctl = new AbortController();
    const t = setTimeout(() => ctl.abort(), TIMEOUT);
    const started = Date.now();
    let r;
    try {
      r = await fetch(current, { redirect: "manual", signal: ctl.signal, headers: { "user-agent": UA, accept: "text/html,application/xhtml+xml,*/*;q=0.8" } });
    } finally { clearTimeout(t); }
    if (r.status >= 300 && r.status < 400 && r.headers.get("location")) {
      chain.push({ url: current.href, status: r.status });
      current = new URL(r.headers.get("location"), current);
      continue;
    }
    const buf = await r.arrayBuffer();
    const text = new TextDecoder("utf-8", { fatal: false }).decode(buf.slice(0, MAX_BYTES));
    return { url: current.href, status: r.status, headers: r.headers, text, bytes: buf.byteLength, ms: Date.now() - started, chain };
  }
  throw new Error("too many redirects");
}

// ---------- HTML helpers (no dependencies) ----------
const decode = (s) => s.replace(/&amp;/g, "&").replace(/&quot;/g, '"').replace(/&#39;|&apos;/g, "'").replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&nbsp;/g, " ").replace(/&#(\d+);/g, (_, n) => String.fromCharCode(+n));
const strip = (s) => decode(s.replace(/<[^>]+>/g, " ")).replace(/\s+/g, " ").trim();
function attr(tag, name) {
  const m = tag.match(new RegExp(`\\s${name}\\s*=\\s*("([^"]*)"|'([^']*)'|([^\\s>]+))`, "i"));
  return m ? decode(m[2] ?? m[3] ?? m[4] ?? "") : null;
}
const tags = (html, name) => html.match(new RegExp(`<${name}\\b[^>]*>`, "gi")) || [];
function meta(html, key, val) {
  for (const t of tags(html, "meta")) if ((attr(t, key) || "").toLowerCase() === val) return attr(t, "content");
  return null;
}

export function analyze(page, extras = {}) {
  const raw = page.text;
  const html = raw.replace(/<!--[\s\S]*?-->/g, "");
  const body = (html.match(/<body\b[\s\S]*<\/body>/i) || [html])[0];
  const visible = body.replace(/<script\b[\s\S]*?<\/script>/gi, " ").replace(/<style\b[\s\S]*?<\/style>/gi, " ").replace(/<noscript\b[\s\S]*?<\/noscript>/gi, " ").replace(/<svg\b[\s\S]*?<\/svg>/gi, " ");
  const text = strip(visible);
  const words = text ? text.split(" ").filter((w) => /[a-z]/i.test(w)).length : 0;
  const year = new Date().getFullYear();
  const host = new URL(page.url).hostname.replace(/^www\./, "");

  const title = strip((html.match(/<title[^>]*>([\s\S]*?)<\/title>/i) || [, ""])[1]);
  const desc = meta(html, "name", "description");
  const h1s = (html.match(/<h1\b[\s\S]*?<\/h1>/gi) || []).map(strip).filter(Boolean);
  const h2s = (html.match(/<h2\b[\s\S]*?<\/h2>/gi) || []).length;
  const imgs = tags(body, "img");
  const noAlt = imgs.filter((t) => { const a = attr(t, "alt"); return a === null; });
  const viewport = meta(html, "name", "viewport");
  const robotsMeta = (meta(html, "name", "robots") || "").toLowerCase();
  const canonicalTag = tags(html, "link").find((t) => (attr(t, "rel") || "").toLowerCase() === "canonical");
  const canonical = canonicalTag ? attr(canonicalTag, "href") : null;
  const lang = (html.match(/<html\b[^>]*>/i) || [""])[0];
  const hasLang = !!attr(lang, "lang");
  const ogTitle = meta(html, "property", "og:title");
  const ogImage = meta(html, "property", "og:image");
  const favicon = tags(html, "link").some((t) => /icon/i.test(attr(t, "rel") || ""));
  const ld = (html.match(/<script[^>]+application\/ld\+json[^>]*>([\s\S]*?)<\/script>/gi) || []);
  const types = new Set();
  for (const block of ld) {
    const m = block.match(/"@type"\s*:\s*(\[[^\]]*\]|"[^"]+")/g) || [];
    m.forEach((x) => (x.match(/"([A-Za-z]+)"/g) || []).forEach((y) => types.add(y.replace(/"/g, ""))));
  }
  const localTypes = [...types].filter((t) => /LocalBusiness|Organization|Store|Service|Contractor|Plumber|Electrician|Dentist|Attorney|LegalService|Restaurant|HomeAndConstructionBusiness|RoofingContractor|HVACBusiness|AutoRepair|BeautySalon|HairSalon|NailSalon|MedicalBusiness|ProfessionalService|RealEstateAgent/.test(t));
  const phoneText = /(\(\d{3}\)\s?\d{3}[-.\s]\d{4}|\b\d{3}[-.]\d{3}[-.]\d{4}\b)/.test(text);
  const telLink = /href\s*=\s*["']tel:/i.test(body);
  const forms = tags(body, "form").length;
  const links = tags(body, "a").map((t) => attr(t, "href") || "").filter((h) => h && !h.startsWith("#") && !/^(mailto|tel|javascript):/i.test(h));
  let internal = 0, external = 0;
  for (const h of links) {
    try { const u = new URL(h, page.url); (u.hostname.replace(/^www\./, "") === host ? internal++ : external++); } catch {}
  }
  const analytics = /googletagmanager\.com|google-analytics\.com|gtag\(|fbq\(|plausible\.io|clarity\.ms/i.test(raw);
  const years = [...text.matchAll(/(?:©|&copy;|copyright)\s*(?:\d{4}\s*[-–]\s*)?(\d{4})/gi)].map((m) => +m[1]);
  const copyYear = years.length ? Math.max(...years) : null;
  const https = page.url.startsWith("https://");
  const kb = Math.round(page.bytes / 1024);

  const C = [];
  const add = (group, id, label, status, detail, fix, weight = 1) => C.push({ group, id, label, status, detail, fix: status === "pass" ? "" : fix, weight });

  // Basics
  add("Basics", "https", "Secure connection (HTTPS)", https ? "pass" : "fail",
    https ? "The site loads over a secure https:// address." : "The site does not load over https://. Browsers label it Not Secure.",
    "Install an SSL certificate (most hosts include one free) and redirect every http:// address to https://.", 3);
  add("Basics", "status", "Page loads without errors", page.status === 200 ? "pass" : "fail",
    `The server answered with status ${page.status}.`, "The page should answer with status 200. Have the host or developer check why it returns an error.", 3);
  add("Basics", "indexable", "Google is allowed to list this page", /noindex/.test(robotsMeta) ? "fail" : "pass",
    /noindex/.test(robotsMeta) ? "The page has a noindex tag, which tells Google to leave it out of search results." : "Nothing on the page blocks Google from listing it.",
    "Remove the noindex robots tag unless the page is meant to be hidden.", 3);
  add("Basics", "mobile", "Set up for phones", viewport && /width\s*=\s*device-width/i.test(viewport) ? "pass" : "fail",
    viewport ? `Viewport tag found: ${viewport}` : "No mobile viewport tag. On a phone the page will show zoomed out and hard to read.",
    "Add <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"> and make sure the layout adapts to small screens.", 3);
  if (extras.robots !== undefined) add("Basics", "robots", "robots.txt file", extras.robots ? "pass" : "warn",
    extras.robots ? "Found a robots.txt file." : "No robots.txt file found.", "Add a robots.txt file at the root of the site that points Google to the sitemap.", 1);
  if (extras.sitemap !== undefined) add("Basics", "sitemap", "XML sitemap", extras.sitemap ? "pass" : "warn",
    extras.sitemap ? `Found a sitemap${extras.sitemapCount ? ` listing ${extras.sitemapCount} addresses` : ""}.` : "No sitemap found at /sitemap.xml or in robots.txt.",
    "Create a sitemap.xml listing every page and submit it in Google Search Console.", 2);

  // Search listing
  const tl = title.length;
  add("How it shows on Google", "title", "Page title", !title ? "fail" : (tl < 25 || tl > 65) ? "warn" : "pass",
    title ? `"${title}" (${tl} characters)` : "The page has no title.",
    "Write a title of about 30 to 60 characters that names the main service and the city, for example: Roof Repair in Tyler, TX | Company Name.", 3);
  const dl = desc ? desc.length : 0;
  add("How it shows on Google", "description", "Search description", !desc ? "fail" : (dl < 70 || dl > 165) ? "warn" : "pass",
    desc ? `"${desc}" (${dl} characters)` : "No meta description. Google will pull random text from the page instead.",
    "Write a 120 to 160 character description that says what you do, where, and why to call.", 2);
  add("How it shows on Google", "canonical", "Preferred address (canonical)", canonical ? "pass" : "warn",
    canonical ? `Points to ${canonical}` : "No canonical tag.", "Add a canonical tag so Google knows which version of the address to rank.", 1);
  add("How it shows on Google", "social", "Preview when shared on Facebook or text", ogTitle && ogImage ? "pass" : "warn",
    ogTitle && ogImage ? "Has a share title and image." : "Missing a share title or share image, so links look plain when people share them.",
    "Add og:title, og:description and og:image tags.", 1);
  add("How it shows on Google", "favicon", "Browser tab icon", favicon ? "pass" : "warn",
    favicon ? "Has a favicon." : "No favicon. Google also shows this icon next to mobile search results.", "Add a favicon with the business logo.", 1);

  // Content
  add("Content", "h1", "One main headline (H1)", h1s.length === 1 ? "pass" : h1s.length === 0 ? "fail" : "warn",
    h1s.length ? `${h1s.length} found: "${h1s[0].slice(0, 90)}"` : "No H1 headline.",
    "Use exactly one H1 headline that says the main service and the city.", 2);
  add("Content", "h2", "Section headings", h2s >= 2 ? "pass" : "warn", `${h2s} section heading${h2s === 1 ? "" : "s"} (H2) found.`,
    "Break the page into sections with H2 headings, one for each service or question.", 1);
  add("Content", "words", "Enough words for Google to understand the page", words >= 400 ? "pass" : words >= 200 ? "warn" : "fail",
    `About ${words} words of readable text.`, "Pages that rank for local services usually explain the work in 500+ words: services, area served, process, and common questions.", 2);
  add("Content", "alt", "Image descriptions (alt text)", imgs.length === 0 ? "warn" : noAlt.length === 0 ? "pass" : noAlt.length / imgs.length > 0.3 ? "fail" : "warn",
    imgs.length === 0 ? "No images found on the page." : `${imgs.length - noAlt.length} of ${imgs.length} images have alt text.`,
    imgs.length === 0 ? "Add real photos of your work, each with a short description." : "Give every image a short alt description of what it shows.", 1);
  add("Content", "lang", "Language set", hasLang ? "pass" : "warn", hasLang ? "The page declares its language." : "The page does not declare its language.",
    "Add lang=\"en\" to the <html> tag.", 1);
  if (copyYear) add("Content", "copyright", "Site looks up to date", copyYear >= year - 1 ? "pass" : "warn",
    `The footer copyright says ${copyYear}.`, "Update the copyright year. An old year makes customers wonder if the business is still open.", 1);

  // Local business
  add("Local business", "schema", "Business details for Google (schema)", localTypes.length ? "pass" : types.size ? "warn" : "fail",
    localTypes.length ? `Found: ${localTypes.join(", ")}` : types.size ? `Found schema (${[...types].slice(0, 5).join(", ")}) but no LocalBusiness details.` : "No structured data. Google has to guess the business name, address, phone and hours.",
    "Add LocalBusiness schema with the name, address, phone, hours, service area and website.", 2);
  add("Local business", "phone", "Phone number on the page", phoneText ? "pass" : "fail",
    phoneText ? "A phone number is shown on the page." : "No phone number found in the page text.", "Show the phone number at the top of every page.", 2);
  add("Local business", "tel", "Tap to call on phones", telLink ? "pass" : "warn",
    telLink ? "Has a tap-to-call link." : "The phone number is not a tap-to-call link, so mobile visitors have to copy it.", "Make the phone number a tel: link so one tap calls the business.", 2);
  add("Local business", "form", "Contact or quote form", forms ? "pass" : "warn",
    forms ? `${forms} form${forms > 1 ? "s" : ""} on the page.` : "No form on this page.", "Add a short quote or contact form for people who would rather not call.", 1);
  add("Local business", "analytics", "Visitor tracking", analytics ? "pass" : "warn",
    analytics ? "A tracking tool (such as Google Analytics) is installed." : "No visitor tracking found, so there is no record of how many people visit or call.",
    "Install Google Analytics or a similar tool and connect Google Search Console.", 1);
  add("Local business", "links", "Links to other pages on the site", internal >= 5 ? "pass" : "warn",
    `${internal} links to other pages on this site, ${external} to other sites.`, "Link to a page for each service and each town you serve, so Google can find them.", 1);

  // Page weight
  add("Basics", "size", "Page size", kb <= 500 ? "pass" : kb <= 1500 ? "warn" : "fail", `The HTML is about ${kb} KB.`,
    "Trim the page: remove unused code and builder bloat.", 1);
  if (page.chain && page.chain.length > 1) add("Basics", "redirects", "Redirect steps", "warn",
    `It took ${page.chain.length} redirects to reach the page.`, "Point links and the domain straight at the final address to save load time.", 1);

  const max = C.reduce((s, c) => s + c.weight * 2, 0);
  const got = C.reduce((s, c) => s + c.weight * (c.status === "pass" ? 2 : c.status === "warn" ? 1 : 0), 0);
  return {
    url: page.url, status: page.status, title, description: desc, h1: h1s[0] || null, words, kb,
    onpage: Math.round((got / max) * 100), checks: C,
    counts: { pass: C.filter((c) => c.status === "pass").length, warn: C.filter((c) => c.status === "warn").length, fail: C.filter((c) => c.status === "fail").length },
  };
}

const SKIP_EXT = /\.(pdf|jpe?g|png|gif|webp|svg|zip|mp4|mp3|docx?|xlsx?|pptx?|xml|txt|css|js|ico)(\?|$)/i;
const locs = (xml) => [...xml.matchAll(/<loc>\s*([^<\s]+)\s*<\/loc>/gi)].map((m) => decode(m[1]));

async function findSitemap(origin) {
  const [rob, smap] = await Promise.allSettled([get(origin + "/robots.txt", { redirects: 2 }), get(origin + "/sitemap.xml", { redirects: 2 })]);
  const robotsText = rob.status === "fulfilled" && rob.value.status === 200 && !/<html/i.test(rob.value.text) ? rob.value.text : "";
  let smText = smap.status === "fulfilled" && smap.value.status === 200 && /<(urlset|sitemapindex)/i.test(smap.value.text) ? smap.value.text : "";
  const smLine = robotsText.match(/^\s*sitemap:\s*(\S+)/im);
  if (!smText && smLine) {
    try { const s = await get(new URL(smLine[1], origin).href, { redirects: 2 }); if (s.status === 200 && /<(urlset|sitemapindex)/i.test(s.text)) smText = s.text; } catch {}
  }
  return { robotsText, smText };
}

async function loadPage(raw) {
  if (!/^https?:\/\//i.test(raw)) raw = "https://" + raw;
  const start = new URL(raw);
  try { return await get(start.href); }
  catch (e) {
    if (start.protocol === "https:") return await get(start.href.replace(/^https:/, "http:"));
    throw e;
  }
}

// mode=pages: list up to `limit` page addresses on the same site (sitemap first, homepage links as a fallback)
async function listPages(raw, limit) {
  const home = await loadPage(raw);
  const base = new URL(home.url);
  const host = base.hostname.replace(/^www\./, "");
  const same = (u) => { try { const x = new URL(u, base); return x.hostname.replace(/^www\./, "") === host && /^https?:$/.test(x.protocol) && !SKIP_EXT.test(x.pathname); } catch { return false; } };
  const norm = (u) => { const x = new URL(u, base); x.hash = ""; return x.href; };
  const out = new Set([norm(home.url)]);
  let source = "links";
  const { smText } = await findSitemap(base.origin);
  if (smText) {
    source = "sitemap";
    let pageLocs = [];
    if (/<sitemapindex/i.test(smText)) {
      const children = locs(smText).slice(0, 8);
      const got = await Promise.allSettled(children.map((c) => get(c, { redirects: 2 })));
      for (const g of got) if (g.status === "fulfilled" && g.value.status === 200) pageLocs.push(...locs(g.value.text));
    } else pageLocs = locs(smText);
    for (const u of pageLocs) { if (out.size >= limit) break; if (same(u)) out.add(norm(u)); }
  }
  if (out.size < limit) {
    const hrefs = (tags(home.text, "a").map((t) => attr(t, "href") || "")).filter((h) => h && !h.startsWith("#") && !/^(mailto|tel|javascript):/i.test(h));
    for (const h of hrefs) { if (out.size >= limit) break; if (same(h)) out.add(norm(h)); }
  }
  return { home: home.url, source, pages: [...out].slice(0, limit) };
}

export default async (req) => {
  const params = new URL(req.url).searchParams;
  const raw = (params.get("url") || "").trim();
  if (!raw) return json({ error: "Type a web address first." }, 400);
  try { new URL(/^https?:\/\//i.test(raw) ? raw : "https://" + raw); } catch { return json({ error: "That does not look like a web address." }, 400); }

  if (params.get("mode") === "pages") {
    const limit = Math.max(1, Math.min(500, parseInt(params.get("limit") || "30", 10) || 30));
    try { return json(await listPages(raw, limit)); }
    catch { return json({ error: "Could not reach that website. Check the spelling and that the site is public." }, 502); }
  }

  let page;
  try { page = await loadPage(raw); }
  catch { return json({ error: "Could not reach that website. Check the spelling and that the site is public." }, 502); }
  if (!/html/i.test(page.headers.get("content-type") || "html")) return json({ error: "That address is not a web page." }, 400);

  // light=1: per-page check inside a multi-page audit (skip the site-wide robots and sitemap fetches)
  if (params.get("light") === "1") return json(analyze(page, {}));

  const { robotsText, smText } = await findSitemap(new URL(page.url).origin);
  return json(analyze(page, { robots: !!robotsText, sitemap: !!smText, sitemapCount: smText ? (smText.match(/<loc>/gi) || []).length : 0 }));
};
