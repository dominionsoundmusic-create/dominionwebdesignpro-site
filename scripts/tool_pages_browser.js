// Open the built tool pages and form pages in headless Chromium: page scripts must run without
// JavaScript errors and each Netlify form must be present in the page with its original name.
// Network errors for third-party hosts the sandbox blocks (GA, Google Translate, YouTube, the demo
// backend) are listed separately and do not count as failures.
// Usage: (serve dist on :8766) NODE_PATH=$(npm root -g) node scripts/tool_pages_browser.js [baseUrl]
const { chromium } = require("playwright");
const base = process.argv[2] || "http://127.0.0.1:8766";
const PAGES = [
  ["/site-check/", ["site-check"], "#lead"], ["/demo.html", [], "#demoForm"], ["/demo-generator.html", [], "#claimBtn"],
  ["/intake/", ["client-intake"], "#f"], ["/intake/thanks/", [], "main"], ["/contact/", ["homepage-contact"], "form"],
  ["/contact/thanks/", [], "main"], ["/", ["homepage-contact"], "#contact form"], ["/compare/", [], "#b"], ["/tools/", [], "main"],
];
(async () => {
  const browser = await chromium.launch();
  let bad = 0;
  for (const [u, forms, sel] of PAGES) {
    const page = await browser.newPage();
    const jsErrors = [], netErrors = [];
    page.on("pageerror", (e) => jsErrors.push(String(e)));
    page.on("console", (m) => { if (m.type() === "error") (/net::ERR_|Failed to load resource/.test(m.text()) ? netErrors : jsErrors).push(m.text()); });
    await page.goto(base + u, { waitUntil: "load" });
    await page.waitForTimeout(800);
    const found = await page.evaluate(() => [...document.querySelectorAll("form[name]")].map((f) => f.getAttribute("name")));
    const hasSel = await page.$(sel) !== null;
    const toggle = await page.$(".dlang__btn") !== null;
    const ok = !jsErrors.length && forms.every((f) => found.includes(f)) && hasSel && toggle;
    bad += !ok;
    console.log(`${ok ? "OK  " : "FAIL"} ${u}  forms=${JSON.stringify(found)} key-element=${hasSel} EN/ES=${toggle} js-errors=${jsErrors.length} blocked-third-party=${netErrors.length}`);
    for (const e of jsErrors) console.log("     JS:", e.slice(0, 200));
    await page.close();
  }
  await browser.close();
  process.exit(bad ? 1 : 0);
})();
