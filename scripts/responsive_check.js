// Browser QA over the built site: horizontal overflow at 1440/1024/768/390, JS errors, broken images,
// hero height and main button above the fold, hero text on the left rail at 1440/1920/2560.
// Tool pages copied from the live site have their own layout and only get the overflow, image and JS checks.
// Usage: (serve dist on :8765 first) NODE_PATH=$(npm root -g) node scripts/responsive_check.js [baseUrl] [--shots dir]
const { chromium } = require("playwright");
const fs = require("fs");
const path = require("path");
const base = process.argv[2] && !process.argv[2].startsWith("--") ? process.argv[2] : "http://127.0.0.1:8765";
const shotsIdx = process.argv.indexOf("--shots");
const shots = shotsIdx > -1 ? process.argv[shotsIdx + 1] : "";
const dist = process.env.DIST || path.join(__dirname, "..", "dist");

function pages(dir, out = []) {
  for (const f of fs.readdirSync(dir)) {
    const p = path.join(dir, f);
    if (fs.statSync(p).isDirectory()) pages(p, out);
    else if (f.endsWith(".html")) {
      let u = "/" + path.relative(dist, p).split(path.sep).join("/");
      if (u.endsWith("/index.html")) u = u.slice(0, -"index.html".length);
      out.push(u);
    }
  }
  return out;
}

(async () => {
  const urls = pages(dist).sort();
  const browser = await chromium.launch();
  const problems = [];
  let checks = 0;
  for (const width of [1440, 1024, 768, 390, 1920, 2560]) {
    const ctx = await browser.newContext({ viewport: { width, height: width >= 1440 ? 900 : 844 } });
    const page = await ctx.newPage();
    let errs = [];
    page.on("pageerror", (e) => errs.push(String(e)));
    page.on("console", (m) => { if (m.type() === "error") errs.push(m.text()); });
    const SAMPLE = ["/", "/web-design/houston-tx.html", "/web-design/tyler-tx.html", "/pricing/", "/web-design-for-plumbers/", "/web-design/new-york-ny.html", "/web-design/san-antonio-tx.html", "/web-design/denver-co.html"];
    const list = width > 1440 ? urls.filter((u) => SAMPLE.includes(u)) : urls;
    for (const u of list) {
      errs = [];
      await page.goto(base + u, { waitUntil: "load" });
      checks++;
      const r = await page.evaluate(() => {
        const de = document.documentElement;
        const over = de.scrollWidth - de.clientWidth;
        const wide = [];
        if (over > 0) {
          for (const el of document.querySelectorAll("body *")) {
            const b = el.getBoundingClientRect();
            if (b.right > de.clientWidth + 1 && b.width > 0) wide.push(el.tagName + "." + el.className);
            if (wide.length > 4) break;
          }
        }
        const broken = [...document.images].filter((i) => i.complete && i.naturalWidth === 0).map((i) => i.src);
        const hero = document.querySelector(".hero");
        const h1 = document.querySelector(".hero h1");
        const call = document.querySelector(".hero .btn--gold");
        const hb = hero ? hero.getBoundingClientRect() : null;
        return {
          over, wide, broken,
          heroH: hb ? Math.round(hb.height) : null,
          heroW: hb ? Math.round(hb.width) : null,
          h1Left: h1 ? Math.round(h1.getBoundingClientRect().left) : null,
          callBottom: call ? Math.round(call.getBoundingClientRect().bottom) : null,
          vh: window.innerHeight, vw: de.clientWidth,
        };
      });
      if (r.over > 0) problems.push(`${width}px ${u}: horizontal overflow ${r.over}px (${r.wide.join(", ")})`);
      if (r.broken.length) problems.push(`${width}px ${u}: broken images ${r.broken.join(", ")}`);
      // the sandbox blocks third-party hosts (Google Analytics, Translate, YouTube, the demo backend); only same-site errors count
      errs = errs.filter((e) => !/ERR_TUNNEL_CONNECTION_FAILED|ERR_NAME_NOT_RESOLVED|net::ERR_/.test(e));
      if (errs.length) problems.push(`${width}px ${u}: JS errors ${errs.join(" | ")}`);
      const tool = ["/demo.html", "/demo-generator.html", "/site-check/", "/compare/", "/tools/", "/intake/", "/intake/thanks/", "/contact/thanks/"].includes(u);
      if (tool) { r.heroW = null; r.heroH = null; r.callBottom = null; r.h1Left = null; }
      if (r.heroW !== null && r.heroW < r.vw - 1) problems.push(`${width}px ${u}: hero not edge to edge (${r.heroW} of ${r.vw})`);
      if (width >= 1024 && r.heroH !== null && r.heroH > 720) problems.push(`${width}px ${u}: hero ${r.heroH}px tall`);
      if (width >= 1024 && r.callBottom !== null && r.callBottom > r.vh) problems.push(`${width}px ${u}: call button below the fold (${r.callBottom} > ${r.vh})`);
      if (width >= 1440 && r.h1Left !== null && r.h1Left > Math.min(140, width * 0.055) + 2) problems.push(`${width}px ${u}: hero headline not on the left rail (left ${r.h1Left})`);
      if (shots && (u === "/" || u === "/web-design/houston-tx.html" || u === "/web-design/tyler-tx.html")) {
        fs.mkdirSync(shots, { recursive: true });
        await page.screenshot({ path: path.join(shots, `${width}${u.replace(/[\/.]/g, "_")}.png`), fullPage: width <= 1440 });
      }
    }
    await ctx.close();
  }
  await browser.close();
  for (const p of problems) console.log("PROBLEM", p);
  console.log(`\n${checks} page loads checked at 1440/1024/768/390 (all pages) and 1920/2560 (sample), ${problems.length} problems`);
  process.exit(problems.length ? 1 : 0);
})();
