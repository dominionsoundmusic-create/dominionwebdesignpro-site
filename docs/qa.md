# QA record (Oct 12 2026, final run on the `build` branch)

## Atlanta add-on run (Oct 12 2026)

| Check | Result |
|---|---|
| Build `python3 build.py` | 60 content pages (6 added or rebuilt in this run: /black-owned-web-design/, Atlanta strengthened, Decatur, McDonough, Conyers, Douglasville); 58 planned photos in docs/image-list.md (10 new: 5 heroes, 5 in-body) |
| Rules and SEO `python3 scripts/check.py` | 68 pages checked, **0 errors, 0 warnings** |
| Old URLs `python3 scripts/check_old_urls.py` | **285 old URLs checked, 0 would 404** |
| Final grep `python3 scripts/grep_check.py` | **0 hits** across 68 pages |
| Tool pages `check_tool_pages.py` and `tool_pages_browser.js` | unchanged byte for byte; 10 of 10 load with 0 JS errors, forms site-check, client-intake, homepage-contact present |
| Duplication `python3 scripts/similarity.py` | area pairs max **4.3%** (new pages: 0.0% to 3.5%, highest Decatur vs Lawrenceville 3.4%), service pairs max **2.5%** (black-owned page at most 1.4%) |
| Keywords `python3 scripts/keyword_plan.py` | Atlanta file: 385 keywords, 154 at 10+: **43 assigned, 111 unused with a reason, 0 unclassified** |
| Responsive `responsive_check.js` | 282 page loads at 1440/1024/768/390 (all pages) and 1920/2560 (sample): **0 problems**; Atlanta and black-owned pages screenshotted at 1440 and 2560, H1 at the left rail (79px and 140px), no horizontal scroll |
| Fact-check | 3 independent sub-agents: 115 claims, 91 confirmed, 7 corrected, 15 softened, 1 removed (docs/fact-check.md) |


All commands run from the repo root against the production build in dist/.

| Check | Command | Result |
|---|---|---|
| Build | `python3 build.py` | 55 content pages built (plus 8 tool pages copied through); 48 planned photos listed in docs/image-list.md, each shown as a brand-color block or an existing photo meanwhile, never a broken image |
| Rules and SEO | `python3 scripts/check.py` | 63 pages checked, **0 errors, 0 warnings** (banned phrases and claims, dashes, eyebrow labels, exact quote bar, John 3:16, GA4 with phone-tap tracking, EN/ES toggle and both social links on every page, AI receptionist note, package-trial facts, handwritten marker in the first 4KB, one H1, unique titles and descriptions, canonical, OG tags, one valid JSON-LD block, 3 to 6 FAQs visible and in FAQPage JSON-LD, hero plus 2 in-body images with lazy loading, alt/width/height, internal links, sitemap, _redirects targets) |
| Old URLs | `python3 scripts/check_old_urls.py` | **285 old URLs checked, 0 would 404** (every file on main in both .html and extensionless forms, every sitemap URL, every _redirects source; table in docs/qa-old-urls.md) |
| Tool pages | `python3 scripts/check_tool_pages.py` | 8 of 8 OK: every script block and every form, input, textarea, select, option and button tag byte for byte as on main; form names site-check, client-intake unchanged; all 88 demo-images photos present; netlify/functions/seo-audit.mjs present and netlify.toml points functions at netlify/functions |
| Final grep | `python3 scripts/grep_check.py` | **0 hits** across 63 pages for em/en dashes (Duplantis credit excepted), the banned phrases, "unlimited pages", "100+", "guarantee", "#1", "testimonial", "5-star", "(832)", "(928)", "(689)" in visible text, titles, meta, alt and aria labels |
| Duplication | `python3 scripts/similarity.py --other ../phoenix-pool-cleaning-pro/dist` | City pairs max **4.5%**, service pairs max **2.5%**, guide pairs max **1.9%** (limit 15%); no page shares an 8-word run with the Phoenix build whose system was copied (two incidental runs found and reworded) |
| Keywords | `python3 scripts/keyword_plan.py` | 1,501 rows; 794 at 10+ searches: **302 assigned** to pages, **492 listed unused with a reason**, 0 unclassified |
| Responsive | `node scripts/responsive_check.js` (dist served locally, Chromium) | 262 page loads: every page at 1440, 1024, 768 and 390 px plus samples at 1920 and 2560: **0 problems** (no horizontal overflow, no JS errors, no broken images, hero edge to edge, hero at most 720px tall with the main button above the fold, headline on the left rail). Screenshots of the home page and the Houston and Tyler pages at 1440, 1920 and 2560 reviewed: hero content starts at the left rail (70px at 1280 scale, `--rail`) |
| Tool pages in a browser | `node scripts/tool_pages_browser.js` | 10 of 10 OK: /site-check/, /demo.html, /demo-generator.html, /intake/, /intake/thanks/, /contact/, /contact/thanks/, /, /compare/, /tools/ load with 0 JavaScript errors, forms present by name (site-check, client-intake, homepage-contact), EN/ES toggle present |
| Fact-check | 9 independent sub-agents | 535 claims checked; 58 corrected, 61 softened, 16 removed (docs/fact-check.md) |

**Not verified here (needs the live site):** third-party scripts (GA4, Google Translate, YouTube, the
demo backend on onrender.com) are blocked in this sandbox, so the EN/ES translation itself, the demo
generator's backend call and the Site Check function were not exercised end to end; Netlify form
delivery (no production form was submitted); Netlify's Pretty URLs, 404 status and redirect behavior
in production.

## Duplication (Jaccard on 5-word shingles, page copy and FAQ answers; shared template parts excluded)

| Group | Pairs | Max | Mean | Min |
|---|---:|---:|---:|---:|
| area | 325 | 4.5% | 0.7% | 0.0% |
| guide | 21 | 1.9% | 0.5% | 0.1% |
| legal | 1 | 3.6% | 3.6% | 3.6% |
| mixed | 1262 | 3.5% | 0.3% | 0.0% |
| page | 66 | 5.6% | 0.8% | 0.0% |
| service | 36 | 2.5% | 0.6% | 0.0% |

Top 15 pairs:

| Jaccard | Page | Page |
|---:|---|---|
| 5.6% | /compare/ | /site-check/ |
| 5.0% | /compare/ | /demo.html |
| 4.5% | /web-design/lawrenceville-ga.html | /web-design/plano-tx.html |
| 3.6% | /privacy-policy.html | /terms.html |
| 3.6% | /compare/ | /tools/ |
| 3.5% | /contact/ | / |
| 3.5% | /site-check/ | /tools/ |
| 3.3% | /demo-generator.html | /demo.html |
| 3.3% | / | /web-design/austin-tx.html |
| 3.3% | /compare/ | /demo-generator.html |
| 3.2% | /demo.html | /site-check/ |
| 3.0% | /about.html | / |
| 2.9% | /web-design/frisco-tx.html | /web-design/lawrenceville-ga.html |
| 2.8% | /web-design/lawrenceville-ga.html | /web-design/mckinney-tx.html |
| 2.6% | /about.html | /faq/ |

## Old URLs

| Old URL | Result | How |
|---|---|---|
| / | 200 | served by a rebuilt page or file at the same path |
| /about | 200 | served by a rebuilt page or file at the same path |
| /about.html | 200 | served by a rebuilt page or file at the same path |
| /affordable-web-design/ | 301 | redirect to /affordable-website-design/ (rule /affordable-web-design/) |
| /ai-website-design/ | 301 | redirect to /small-business-website/ (rule /ai-website-design/) |
| /apple-touch-icon.png | 200 | served by a rebuilt page or file at the same path |
| /blog | 301 | redirect to / (rule /blog) |
| /blog/best-website-design-tips-for-local-businesses-1784554351977 | 301 | redirect to /contractor-website-design/ (rule /blog/best-website-design-tips-for-local-businesses-1784554351977) |
| /blog/best-website-design-tips-for-local-businesses-1784554351977.html | 301 | redirect to /contractor-website-design/ (rule /blog/best-website-design-tips-for-local-businesses-1784554351977.html) |
| /blog/best-website-design-tips-for-local-businesses-1786023539143 | 301 | redirect to /contractor-website-design/ (rule /blog/best-website-design-tips-for-local-businesses-1786023539143) |
| /blog/best-website-design-tips-for-local-businesses-1786023539143.html | 301 | redirect to /contractor-website-design/ (rule /blog/best-website-design-tips-for-local-businesses-1786023539143.html) |
| /blog/best-website-design-tips-for-local-businesses-1786278353341 | 301 | redirect to /contractor-website-design/ (rule /blog/best-website-design-tips-for-local-businesses-1786278353341) |
| /blog/best-website-design-tips-for-local-businesses-1786278353341.html | 301 | redirect to /contractor-website-design/ (rule /blog/best-website-design-tips-for-local-businesses-1786278353341.html) |
| /blog/how-a-website-pays-for-itself-with-one-new-customer-1786191829290 | 301 | redirect to /contractor-website-design/ (rule /blog/how-a-website-pays-for-itself-with-one-new-customer-1786191829290) |
| /blog/how-a-website-pays-for-itself-with-one-new-customer-1786191829290.html | 301 | redirect to /contractor-website-design/ (rule /blog/how-a-website-pays-for-itself-with-one-new-customer-1786191829290.html) |
| /blog/how-much-does-a-website-cost-for-a-small-business-1785766402549 | 301 | redirect to /small-business-website-cost (rule /blog/how-much-does-a-website-cost-for-a-small-business-1785766402549) |
| /blog/how-much-does-a-website-cost-for-a-small-business-1785766402549.html | 301 | redirect to /small-business-website-cost (rule /blog/how-much-does-a-website-cost-for-a-small-business-1785766402549.html) |
| /blog/how-to-get-more-customers-with-local-seo-1785707136206 | 301 | redirect to /seo-web-design/ (rule /blog/how-to-get-more-customers-with-local-seo-1785707136206) |
| /blog/how-to-get-more-customers-with-local-seo-1785707136206.html | 301 | redirect to /seo-web-design/ (rule /blog/how-to-get-more-customers-with-local-seo-1785707136206.html) |
| /blog/how-to-get-more-customers-with-local-seo-1785937210069 | 301 | redirect to /seo-web-design/ (rule /blog/how-to-get-more-customers-with-local-seo-1785937210069) |
| /blog/how-to-get-more-customers-with-local-seo-1785937210069.html | 301 | redirect to /seo-web-design/ (rule /blog/how-to-get-more-customers-with-local-seo-1785937210069.html) |
| /blog/how-to-rank-on-google-in-your-city-1786970130390 | 301 | redirect to /how-city-pages-work (rule /blog/how-to-rank-on-google-in-your-city-1786970130390) |
| /blog/how-to-rank-on-google-in-your-city-1786970130390.html | 301 | redirect to /how-city-pages-work (rule /blog/how-to-rank-on-google-in-your-city-1786970130390.html) |
| /blog/signs-your-website-needs-a-redesign-1785851074882 | 301 | redirect to /contractor-website-design/ (rule /blog/signs-your-website-needs-a-redesign-1785851074882) |
| /blog/signs-your-website-needs-a-redesign-1785851074882.html | 301 | redirect to /contractor-website-design/ (rule /blog/signs-your-website-needs-a-redesign-1785851074882.html) |
| /blog/website-mistakes-small-businesses-make-1786106283756 | 301 | redirect to /small-business-website/ (rule /blog/website-mistakes-small-businesses-make-1786106283756) |
| /blog/website-mistakes-small-businesses-make-1786106283756.html | 301 | redirect to /small-business-website/ (rule /blog/website-mistakes-small-businesses-make-1786106283756.html) |
| /blog/why-mobile-friendly-websites-matter-for-local-business-1784553970896 | 301 | redirect to /small-business-website/ (rule /blog/why-mobile-friendly-websites-matter-for-local-business-1784553970896) |
| /blog/why-mobile-friendly-websites-matter-for-local-business-1784553970896.html | 301 | redirect to /small-business-website/ (rule /blog/why-mobile-friendly-websites-matter-for-local-business-1784553970896.html) |
| /blog/why-small-businesses-need-a-website-in-2026-1786365719381 | 301 | redirect to /small-business-website/ (rule /blog/why-small-businesses-need-a-website-in-2026-1786365719381) |
| /blog/why-small-businesses-need-a-website-in-2026-1786365719381.html | 301 | redirect to /small-business-website/ (rule /blog/why-small-businesses-need-a-website-in-2026-1786365719381.html) |
| /blog/why-your-competitor-is-getting-more-calls-than-you-1786451944655 | 301 | redirect to / (rule /blog/why-your-competitor-is-getting-more-calls-than-you-1786451944655) |
| /blog/why-your-competitor-is-getting-more-calls-than-you-1786451944655.html | 301 | redirect to / (rule /blog/why-your-competitor-is-getting-more-calls-than-you-1786451944655.html) |
| /business-website-design/ | 301 | redirect to /small-business-website/ (rule /business-website-design/) |
| /compare/ | 200 | served by a rebuilt page or file at the same path |
| /compare/index.html | 200 | served by a rebuilt page or file at the same path |
| /contact/thanks/ | 200 | served by a rebuilt page or file at the same path |
| /contact/thanks/index.html | 200 | served by a rebuilt page or file at the same path |
| /contractor-website-design/ | 200 | served by a rebuilt page or file at the same path |
| /contractor-website-design/index.html | 200 | served by a rebuilt page or file at the same path |
| /custom-website-design/ | 301 | redirect to /small-business-website/ (rule /custom-website-design/) |
| /demo | 200 | served by a rebuilt page or file at the same path |
| /demo-generator | 200 | served by a rebuilt page or file at the same path |
| /demo-generator.html | 200 | served by a rebuilt page or file at the same path |
| /demo-images/accounting/1.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/accounting/2.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/accounting/3.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/accounting/4.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/auto-repair/1.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/auto-repair/2.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/auto-repair/3.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/auto-repair/4.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/chiropractic/1.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/chiropractic/2.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/chiropractic/3.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/chiropractic/4.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/chiropractic/5.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/chiropractic/6.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/chiropractic/7.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/chiropractic/8.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/cleaning/1.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/cleaning/2.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/cleaning/3.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/cleaning/4.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/construction/1.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/construction/2.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/construction/3.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/construction/4.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/default/1.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/default/2.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/default/3.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/default/4.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/dental/1.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/dental/2.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/dental/3.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/dental/4.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/electrical/1.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/electrical/2.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/electrical/3.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/electrical/4.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/gym/1.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/gym/2.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/gym/3.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/gym/4.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/hvac/1.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/hvac/2.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/hvac/3.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/hvac/4.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/insurance/1.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/insurance/2.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/insurance/3.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/insurance/4.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/landscaping/1.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/landscaping/2.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/landscaping/3.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/landscaping/4.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/legal/1.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/legal/2.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/legal/3.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/legal/4.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/manifest.json | 200 | served by a rebuilt page or file at the same path |
| /demo-images/pest-control/1.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/pest-control/2.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/pest-control/3.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/pest-control/4.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/photography/1.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/photography/2.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/photography/3.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/photography/4.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/plumbing/1.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/plumbing/2.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/plumbing/3.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/plumbing/4.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/real-estate/1.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/real-estate/2.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/real-estate/3.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/real-estate/4.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/restaurant/1.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/restaurant/2.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/restaurant/3.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/restaurant/4.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/roofing/1.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/roofing/2.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/roofing/3.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/roofing/4.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/salon/1.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/salon/2.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/salon/3.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/salon/4.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/veterinary/1.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/veterinary/2.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/veterinary/3.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo-images/veterinary/4.jpg | 200 | served by a rebuilt page or file at the same path |
| /demo.html | 200 | served by a rebuilt page or file at the same path |
| /ecommerce-website-design/ | 301 | redirect to /small-business-website/ (rule /ecommerce-website-design/) |
| /ecommerce-website-design/index.html | 301 | redirect to /small-business-website/ (rule /ecommerce-website-design/*) |
| /favicon.ico | 200 | served by a rebuilt page or file at the same path |
| /favicon.svg | 200 | served by a rebuilt page or file at the same path |
| /how-city-pages-work | 200 | served by a rebuilt page or file at the same path |
| /how-city-pages-work.html | 200 | served by a rebuilt page or file at the same path |
| /images/cities/anaheim-ca.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/asheville-nc.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/atlanta-food-truck.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/atlanta-small-business.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/atlanta-sole-proprietor.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/austin-skyline.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/baton-rouge-la.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/bellingham-wa.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/boise-id.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/boulder-co.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/castle-rock-co.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/cedar-park-hero.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/chattanooga-tn.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/columbia-sc.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/credits.json | 200 | served by a rebuilt page or file at the same path |
| /images/cities/denton-hero.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/dripping-springs-hero.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/durham-nc.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/et-street-b.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/fayetteville-ar.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/fort-collins-co.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/frisco-hero.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/gilmer-business.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/gilmer-industry.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/gilmer-street.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/gladewater-business.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/greenville-sc.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/gwinnett-international-corridor.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/harrisburg-pa.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/indianapolis-in.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/kilgore-business.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/kilgore-industry.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/knoxville-tn.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/kyle-hero.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/lawrenceville-courthouse-district.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/lawrenceville-storefronts.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/leander-hero.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/longview-business.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/longview-industry.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/longview-tx.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/lubbock-tx.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/marshall-business.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/marshall-industry.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/mckinney-hero.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/mobile-al.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/new-braunfels-hero.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/pflugerville-hero.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/plano-hero.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/reno-nv.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/san-marcos-hero.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/savannah-ga.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/spokane-wa.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/springfield-mo.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/st-petersburg-fl.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/tacoma-wa.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/tyler-tx.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cities/wichita-ks.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/contractors/contractor-hero.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/contractors/contractor-review.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/contractors/contractor-work.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/cost-page-hero.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/dominion-logo.svg | 200 | served by a rebuilt page or file at the same path |
| /images/og-dominion-web-design-pro.jpg | 200 | served by a rebuilt page or file at the same path |
| /index.html | 200 | served by a rebuilt page or file at the same path |
| /intake/ | 200 | served by a rebuilt page or file at the same path |
| /intake/index.html | 200 | served by a rebuilt page or file at the same path |
| /intake/thanks/ | 200 | served by a rebuilt page or file at the same path |
| /intake/thanks/index.html | 200 | served by a rebuilt page or file at the same path |
| /lead-generation-website/ | 301 | redirect to /small-business-website/ (rule /lead-generation-website/) |
| /local-business-website/ | 301 | redirect to /small-business-website/ (rule /local-business-website/) |
| /medical-website-design/ | 301 | redirect to /web-design-for-therapists/ (rule /medical-website-design/) |
| /medical-website-design/index.html | 301 | redirect to /web-design-for-therapists/ (rule /medical-website-design/*) |
| /mobile-website-design/ | 301 | redirect to /small-business-website/ (rule /mobile-website-design/) |
| /onboarding | 301 | redirect to /intake/ (rule /onboarding) |
| /onboarding/ | 301 | redirect to /intake/ (rule /onboarding/) |
| /privacy-policy | 200 | served by a rebuilt page or file at the same path |
| /privacy-policy.html | 200 | served by a rebuilt page or file at the same path |
| /professional-website-design/ | 301 | redirect to /small-business-website/ (rule /professional-website-design/) |
| /professional-website-design/index.html | 301 | redirect to /small-business-website/ (rule /professional-website-design/*) |
| /real-estate-website-design/ | 301 | redirect to /small-business-website/ (rule /real-estate-website-design/) |
| /real-estate-website-design/index.html | 301 | redirect to /small-business-website/ (rule /real-estate-website-design/*) |
| /restaurant-website-design/ | 301 | redirect to /small-business-website/ (rule /restaurant-website-design/) |
| /restaurant-website-design/index.html | 301 | redirect to /small-business-website/ (rule /restaurant-website-design/*) |
| /robots.txt | 200 | served by a rebuilt page or file at the same path |
| /seo-web-design/ | 200 | served by a rebuilt page or file at the same path |
| /seo-web-design/index.html | 200 | served by a rebuilt page or file at the same path |
| /service-areas | 200 | served by a rebuilt page or file at the same path |
| /service-areas.html | 200 | served by a rebuilt page or file at the same path |
| /site-check/ | 200 | served by a rebuilt page or file at the same path |
| /site-check/index.html | 200 | served by a rebuilt page or file at the same path |
| /sitemap.xml | 200 | served by a rebuilt page or file at the same path |
| /small-business-website-cost | 200 | served by a rebuilt page or file at the same path |
| /small-business-website-cost.html | 200 | served by a rebuilt page or file at the same path |
| /small-business-website/ | 200 | served by a rebuilt page or file at the same path |
| /small-business-website/index.html | 200 | served by a rebuilt page or file at the same path |
| /terms | 200 | served by a rebuilt page or file at the same path |
| /terms.html | 200 | served by a rebuilt page or file at the same path |
| /tools/ | 200 | served by a rebuilt page or file at the same path |
| /tools/index.html | 200 | served by a rebuilt page or file at the same path |
| /web-design/ | 200 | served by a rebuilt page or file at the same path |
| /web-design/atlanta-ga | 200 | served by a rebuilt page or file at the same path |
| /web-design/atlanta-ga.html | 200 | served by a rebuilt page or file at the same path |
| /web-design/austin-tx | 200 | served by a rebuilt page or file at the same path |
| /web-design/austin-tx.html | 200 | served by a rebuilt page or file at the same path |
| /web-design/cedar-park-tx | 200 | served by a rebuilt page or file at the same path |
| /web-design/cedar-park-tx.html | 200 | served by a rebuilt page or file at the same path |
| /web-design/denton-tx | 200 | served by a rebuilt page or file at the same path |
| /web-design/denton-tx.html | 200 | served by a rebuilt page or file at the same path |
| /web-design/dripping-springs-tx | 200 | served by a rebuilt page or file at the same path |
| /web-design/dripping-springs-tx.html | 200 | served by a rebuilt page or file at the same path |
| /web-design/frisco-tx | 200 | served by a rebuilt page or file at the same path |
| /web-design/frisco-tx.html | 200 | served by a rebuilt page or file at the same path |
| /web-design/gilmer-tx | 200 | served by a rebuilt page or file at the same path |
| /web-design/gilmer-tx.html | 200 | served by a rebuilt page or file at the same path |
| /web-design/gladewater-tx | 200 | served by a rebuilt page or file at the same path |
| /web-design/gladewater-tx.html | 200 | served by a rebuilt page or file at the same path |
| /web-design/index.html | 200 | served by a rebuilt page or file at the same path |
| /web-design/kilgore-tx | 200 | served by a rebuilt page or file at the same path |
| /web-design/kilgore-tx.html | 200 | served by a rebuilt page or file at the same path |
| /web-design/kyle-tx | 200 | served by a rebuilt page or file at the same path |
| /web-design/kyle-tx.html | 200 | served by a rebuilt page or file at the same path |
| /web-design/lawrenceville-ga | 200 | served by a rebuilt page or file at the same path |
| /web-design/lawrenceville-ga.html | 200 | served by a rebuilt page or file at the same path |
| /web-design/leander-tx | 200 | served by a rebuilt page or file at the same path |
| /web-design/leander-tx.html | 200 | served by a rebuilt page or file at the same path |
| /web-design/longview-tx | 200 | served by a rebuilt page or file at the same path |
| /web-design/longview-tx.html | 200 | served by a rebuilt page or file at the same path |
| /web-design/marshall-tx | 200 | served by a rebuilt page or file at the same path |
| /web-design/marshall-tx.html | 200 | served by a rebuilt page or file at the same path |
| /web-design/mckinney-tx | 200 | served by a rebuilt page or file at the same path |
| /web-design/mckinney-tx.html | 200 | served by a rebuilt page or file at the same path |
| /web-design/new-braunfels-tx | 200 | served by a rebuilt page or file at the same path |
| /web-design/new-braunfels-tx.html | 200 | served by a rebuilt page or file at the same path |
| /web-design/pflugerville-tx | 200 | served by a rebuilt page or file at the same path |
| /web-design/pflugerville-tx.html | 200 | served by a rebuilt page or file at the same path |
| /web-design/plano-tx | 200 | served by a rebuilt page or file at the same path |
| /web-design/plano-tx.html | 200 | served by a rebuilt page or file at the same path |
| /web-design/san-marcos-tx | 200 | served by a rebuilt page or file at the same path |
| /web-design/san-marcos-tx.html | 200 | served by a rebuilt page or file at the same path |
| /website-design-for-contractors | 301 | redirect to /contractor-website-design/ (rule /website-design-for-contractors) |
| /website-design-for-contractors.html | 301 | redirect to /contractor-website-design/ (rule /website-design-for-contractors.html) |
| /website-design/ | 301 | redirect to /small-business-website/ (rule /website-design/) |
| /website-designer/ | 301 | redirect to /small-business-website/ (rule /website-designer/) |
| /website-redesign/ | 301 | redirect to /small-business-website-redesign/ (rule /website-redesign/) |
| /wordpress-web-design/ | 301 | redirect to /small-business-website/ (rule /wordpress-web-design/) |

285 old URLs checked, 0 would 404.

## Wave 2 (Oct 16 2026): 13 national city pages

| Check | How | Result |
|---|---|---|
| Build | `python3 build.py` | 73 pages built, 13 planned hero images listed in docs/image-list.md |
| Page rules | `python3 scripts/check.py` | 81 pages checked, **0 errors, 0 warnings** |
| Old URLs | `python3 scripts/check_old_urls.py` | 285 old URLs checked, **0 would 404** |
| Banned phrases, dashes, numbers | `python3 scripts/grep_check.py` | **0 hits** across 81 pages |
| Keyword 10+ rule | `python3 scripts/keyword_plan.py` (runs keyword_plan_wave2.py) | 150 Wave 2 keywords at 10+: 85 on a page, 65 unused with a reason, 0 unclassified |
| Responsive | `node scripts/responsive_check.js` (dist served locally) | 334 page loads at 1440/1024/768/390 plus 1920/2560 samples: **0 problems** (no overflow, no JS errors, no broken images, hero on the left rail). Miami page screenshot at 1440 reviewed |
| Tool pages and forms | `node scripts/tool_pages_browser.js`, `python3 scripts/check_tool_pages.py` | all OK, forms present with original names, 0 JS errors, scripts byte-for-byte unchanged, seo-audit function present |
| Fact-check | 4 independent sub-agents (docs/fact-check.md, Wave 2) | 245 claims: 194 confirmed, 26 corrected, 18 softened, 5 removed |

### Similarity (Jaccard, 5-word shingles, `python3 scripts/similarity.py`)

All 43 city pages, 903 pairs: min 0.0%, mean 0.9%, max 4.3%.

| New page | Words | Highest pair | Jaccard |
|---|---:|---|---:|
| /web-design/st-louis-mo.html | 1,735 | /web-design/indianapolis-in.html | 4.0% |
| /web-design/kansas-city-mo.html | 1,357 | /web-design/lawrenceville-ga.html | 3.2% |
| /web-design/indianapolis-in.html | 1,429 | /web-design/st-louis-mo.html | 4.0% |
| /web-design/phoenix-az.html | 1,804 | /web-design/sacramento-ca.html | 2.6% |
| /web-design/las-vegas-nv.html | 1,457 | /web-design/indianapolis-in.html | 2.3% |
| /web-design/sacramento-ca.html | 1,667 | /web-design/phoenix-az.html | 2.6% |
| /web-design/los-angeles-ca.html | 1,902 | /web-design/orlando-fl.html | 2.7% |
| /web-design/san-diego-ca.html | 1,447 | /web-design/indianapolis-in.html | 2.0% |
| /web-design/miami-fl.html | 1,932 | /web-design/decatur-ga.html | 2.4% |
| /web-design/orlando-fl.html | 1,538 | /web-design/cleveland-oh.html | 4.0% |
| /web-design/nashville-tn.html | 1,639 | /web-design/los-angeles-ca.html | 2.2% |
| /web-design/chicago-il.html | 1,804 | /web-design/cleveland-oh.html | 2.2% |
| /web-design/cleveland-oh.html | 1,458 | /web-design/orlando-fl.html | 4.0% |

Pairs involving a Wave 2 page: 546 (pairs counted from each side), range 0.0% to 4.0%. Limit 15%: none over.

## Wave 3 (Oct 17 2026): 8 national city pages

| Check | How | Result |
|---|---|---|
| Build | `python3 build.py` | 81 pages built, 8 planned hero images listed in docs/image-list.md |
| Page rules | `python3 scripts/check.py` | 89 pages checked, **0 errors, 0 warnings** |
| Old URLs | `python3 scripts/check_old_urls.py` | 285 old URLs checked, **0 would 404** |
| Banned phrases, dashes, numbers | `python3 scripts/grep_check.py` | **0 hits** across 89 pages |
| Keyword 10+ rule | `python3 scripts/keyword_plan.py` (runs keyword_plan_wave3.py) | 110 Wave 3 keywords at 10+ (per city tab, 8 targets included): 75 on a page (8 targets, 60 supporting, 7 FAQ questions), 35 unused with a reason, 0 unclassified |
| Responsive | `node scripts/responsive_check.js` (dist served locally; New York page added to the 1920/2560 sample) | 368 page loads at 1440/1024/768/390 plus 1920/2560 samples. First run flagged the New York hero at 764px (long H1); H1 shortened, re-run **0 problems** (no overflow, no JS errors, no broken images, hero on the left rail, main button above the fold). New York screenshot at 1440 reviewed |
| Tool pages and forms | `node scripts/tool_pages_browser.js`, `python3 scripts/check_tool_pages.py` | all OK: site-check, client-intake and homepage-contact forms present with original names, 0 JS errors, scripts unchanged, seo-audit function present |
| Fact-check | 4 independent sub-agents (docs/fact-check.md, Wave 3) | 194 claims: 153 confirmed, 13 corrected, 25 softened, 2 removed |

### Similarity (Jaccard, 5-word shingles, `python3 scripts/similarity.py`)

All 51 area pages, 1,275 pairs: min 0.0%, mean 0.9%, max 4.3% (lawrenceville-ga vs plano-tx, unchanged from earlier waves).

| New page | Words | Highest pair | Jaccard |
|---|---:|---|---:|
| /web-design/new-york-ny.html | 2,031 | /web-design/orange-county-ca.html | 3.6% |
| /web-design/orange-county-ca.html | 1,886 | /web-design/new-york-ny.html | 3.6% |
| /web-design/tampa-fl.html | 2,102 | /web-design/st-louis-mo.html | 2.5% |
| /web-design/huntsville-al.html | 1,927 | /web-design/indianapolis-in.html | 3.4% |
| /web-design/tucson-az.html | 1,560 | /web-design/louisville-ky.html | 1.1% |
| /web-design/richmond-va.html | 1,561 | /web-design/indianapolis-in.html | 2.2% |
| /web-design/louisville-ky.html | 1,671 | /web-design/miami-fl.html | 3.7% |
| /web-design/wilmington-nc.html | 1,493 | /web-design/louisville-ky.html | 3.2% |

Pairs involving a Wave 3 page: 400 (counted from each side), range 0.0% to 3.7%. Limit 15%: none over.
(Words = all visible words on the built page, as similarity.py counts them.)

## Wave 4 (Oct 17 2026): 81 more city pages (23 Texas, 29 South and East, 29 West and Midwest)

| Check | How | Result |
|---|---|---|
| Build | `python3 build.py` | 162 pages built; 32 planned hero images listed in docs/image-list.md (24 new Wave 4 heroes plus the 8 Wave 3 heroes still to come) |
| Page rules | `python3 scripts/check.py` | 170 pages checked, **0 errors**, 4 warnings (word count on the short Laredo, Round Rock, San Angelo and Temple pages, short by design per CITY-PAGES-WAVE4.md) |
| Old URLs | `python3 scripts/check_old_urls.py` | 285 old URLs checked, **0 would 404** |
| Banned phrases, dashes, numbers | `python3 scripts/grep_check.py` | **0 hits** across 170 pages |
| Keyword 10+ rule | `python3 scripts/keyword_plan.py` (runs keyword_plan_wave4.py) | Wave 4 tabs: 673 keyword rows at 10+ (per tab): 81 targets, 283 supporting, 22 FAQ questions, 78 assigned to another page, 1 repeat of a target, 208 unused with a reason, **0 unclassified** |
| Responsive | `node scripts/responsive_check.js` (dist served locally; San Antonio and Denver added to the 1920/2560 sample) | 696 page loads at 1440/1024/768/390 plus 1920/2560 samples. First run flagged ten Wave 4 heroes at 729 to 764px (long H1s); H1s shortened, re-run **0 problems** (no overflow, no JS errors, no broken images, hero on the left rail, main button above the fold). San Antonio at 1440 and 2560: H1 left edge at 79px and 140px |
| Tool pages and forms | `node scripts/tool_pages_browser.js`, `python3 scripts/check_tool_pages.py` | 10 of 10 OK: site-check, client-intake and homepage-contact forms present with original names, 0 JS errors, scripts unchanged, seo-audit function present |
| Fact-check | 18 independent fact-check sub-agents plus 3 search rechecks and 3 research passes (docs/fact-check.md, Wave 4) | 1,460 claims: 991 confirmed, 168 corrected, 163 softened, 73 removed (remainder kept on official writer sources) |

### Similarity (Jaccard, 5-word shingles, `python3 scripts/similarity.py`)

All 132 area pages, 8,646 pairs: min 0.0%, mean 1.3%, **max 6.1%** (st-petersburg-fl vs tallahassee-fl). Limit 15%: none over.

| New page | Words | Highest pair | Jaccard |
|---|---:|---|---:|
| /web-design/san-antonio-tx.html | 1,551 | /web-design/lubbock-tx.html | 4.1% |
| /web-design/laredo-tx.html | 905 | /web-design/temple-tx.html | 2.0% |
| /web-design/temple-tx.html | 800 | /web-design/abilene-tx.html | 3.8% |
| /web-design/fort-worth-tx.html | 1,561 | /web-design/st-louis-mo.html | 4.9% |
| /web-design/arlington-tx.html | 1,264 | /web-design/abilene-tx.html | 5.5% |
| /web-design/abilene-tx.html | 1,040 | /web-design/arlington-tx.html | 5.5% |
| /web-design/corpus-christi-tx.html | 1,524 | /web-design/abilene-tx.html | 1.5% |
| /web-design/mcallen-tx.html | 1,195 | /web-design/brownsville-tx.html | 1.7% |
| /web-design/brownsville-tx.html | 1,086 | /web-design/mcallen-tx.html | 1.7% |
| /web-design/lubbock-tx.html | 1,756 | /web-design/san-antonio-tx.html | 4.1% |
| /web-design/amarillo-tx.html | 1,297 | /web-design/sugar-land-tx.html | 3.3% |
| /web-design/san-angelo-tx.html | 814 | /web-design/texarkana-tx.html | 1.9% |
| /web-design/midland-tx.html | 1,313 | /web-design/abilene-tx.html | 2.3% |
| /web-design/odessa-tx.html | 1,153 | /web-design/killeen-tx.html | 3.4% |
| /web-design/killeen-tx.html | 999 | /web-design/texarkana-tx.html | 3.9% |
| /web-design/sugar-land-tx.html | 1,410 | /web-design/katy-tx.html | 3.9% |
| /web-design/katy-tx.html | 1,316 | /web-design/sugar-land-tx.html | 3.9% |
| /web-design/cypress-tx.html | 1,179 | /web-design/beaumont-tx.html | 3.7% |
| /web-design/the-woodlands-tx.html | 921 | /web-design/nacogdoches-tx.html | 2.9% |
| /web-design/beaumont-tx.html | 1,154 | /web-design/texarkana-tx.html | 4.1% |
| /web-design/round-rock-tx.html | 791 | /web-design/the-woodlands-tx.html | 2.3% |
| /web-design/nacogdoches-tx.html | 1,186 | /web-design/abilene-tx.html | 3.2% |
| /web-design/texarkana-tx.html | 1,139 | /web-design/beaumont-tx.html | 4.1% |
| /web-design/charlotte-nc.html | 1,815 | /web-design/montgomery-al.html | 3.5% |
| /web-design/greensboro-nc.html | 1,152 | /web-design/knoxville-tn.html | 4.7% |
| /web-design/augusta-ga.html | 1,565 | /web-design/montgomery-al.html | 4.4% |
| /web-design/raleigh-nc.html | 1,488 | /web-design/shreveport-la.html | 2.2% |
| /web-design/durham-nc.html | 1,370 | /web-design/fort-myers-fl.html | 1.2% |
| /web-design/montgomery-al.html | 1,247 | /web-design/augusta-ga.html | 4.4% |
| /web-design/charleston-sc.html | 1,519 | /web-design/greenville-sc.html | 3.1% |
| /web-design/columbia-sc.html | 1,252 | /web-design/pensacola-fl.html | 3.2% |
| /web-design/greenville-sc.html | 1,423 | /web-design/wilmington-nc.html | 3.3% |
| /web-design/savannah-ga.html | 1,600 | /web-design/shreveport-la.html | 3.3% |
| /web-design/jacksonville-fl.html | 1,376 | /web-design/wilmington-nc.html | 4.2% |
| /web-design/tallahassee-fl.html | 1,479 | /web-design/st-petersburg-fl.html | 6.1% |
| /web-design/fort-lauderdale-fl.html | 1,812 | /web-design/west-palm-beach-fl.html | 5.2% |
| /web-design/west-palm-beach-fl.html | 1,964 | /web-design/fort-lauderdale-fl.html | 5.2% |
| /web-design/pensacola-fl.html | 1,295 | /web-design/wilmington-nc.html | 5.3% |
| /web-design/st-petersburg-fl.html | 1,459 | /web-design/tallahassee-fl.html | 6.1% |
| /web-design/sarasota-fl.html | 1,199 | /web-design/fort-myers-fl.html | 5.5% |
| /web-design/fort-myers-fl.html | 1,436 | /web-design/sarasota-fl.html | 5.5% |
| /web-design/new-orleans-la.html | 1,692 | /web-design/baton-rouge-la.html | 5.5% |
| /web-design/baton-rouge-la.html | 1,519 | /web-design/new-orleans-la.html | 5.5% |
| /web-design/shreveport-la.html | 1,163 | /web-design/baton-rouge-la.html | 5.2% |
| /web-design/birmingham-al.html | 1,733 | /web-design/jackson-ms.html | 5.7% |
| /web-design/mobile-al.html | 1,564 | /web-design/jackson-ms.html | 5.3% |
| /web-design/jackson-ms.html | 1,478 | /web-design/birmingham-al.html | 5.7% |
| /web-design/knoxville-tn.html | 1,677 | /web-design/memphis-tn.html | 5.7% |
| /web-design/chattanooga-tn.html | 1,661 | /web-design/knoxville-tn.html | 4.2% |
| /web-design/memphis-tn.html | 1,725 | /web-design/knoxville-tn.html | 5.7% |
| /web-design/lexington-ky.html | 2,081 | /web-design/louisville-ky.html | 4.1% |
| /web-design/little-rock-ar.html | 1,636 | /web-design/louisville-ky.html | 4.6% |
| /web-design/denver-co.html | 1,680 | /web-design/fort-collins-co.html | 2.4% |
| /web-design/colorado-springs-co.html | 1,154 | /web-design/fort-collins-co.html | 2.3% |
| /web-design/fort-collins-co.html | 1,285 | /web-design/reno-nv.html | 3.7% |
| /web-design/seattle-wa.html | 1,747 | /web-design/boise-id.html | 4.3% |
| /web-design/spokane-wa.html | 1,327 | /web-design/boise-id.html | 5.0% |
| /web-design/boise-id.html | 1,303 | /web-design/spokane-wa.html | 5.0% |
| /web-design/portland-or.html | 1,635 | /web-design/reno-nv.html | 4.4% |
| /web-design/salt-lake-city-ut.html | 1,340 | /web-design/des-moines-ia.html | 2.0% |
| /web-design/reno-nv.html | 1,045 | /web-design/portland-or.html | 4.4% |
| /web-design/san-francisco-ca.html | 1,721 | /web-design/oklahoma-city-ok.html | 3.0% |
| /web-design/san-jose-ca.html | 1,554 | /web-design/long-beach-ca.html | 2.8% |
| /web-design/long-beach-ca.html | 1,344 | /web-design/san-jose-ca.html | 2.8% |
| /web-design/fresno-ca.html | 1,611 | /web-design/albuquerque-nm.html | 5.7% |
| /web-design/bakersfield-ca.html | 1,206 | /web-design/fresno-ca.html | 5.5% |
| /web-design/albuquerque-nm.html | 1,335 | /web-design/fresno-ca.html | 5.7% |
| /web-design/scottsdale-az.html | 1,672 | /web-design/tulsa-ok.html | 4.9% |
| /web-design/mesa-az.html | 1,331 | /web-design/tulsa-ok.html | 4.5% |
| /web-design/tulsa-ok.html | 1,327 | /web-design/scottsdale-az.html | 4.9% |
| /web-design/oklahoma-city-ok.html | 1,612 | /web-design/abilene-tx.html | 4.1% |
| /web-design/omaha-ne.html | 1,421 | /web-design/des-moines-ia.html | 4.4% |
| /web-design/des-moines-ia.html | 1,448 | /web-design/omaha-ne.html | 4.4% |
| /web-design/minneapolis-mn.html | 1,790 | /web-design/madison-wi.html | 4.1% |
| /web-design/madison-wi.html | 1,367 | /web-design/grand-rapids-mi.html | 4.6% |
| /web-design/grand-rapids-mi.html | 1,406 | /web-design/madison-wi.html | 4.6% |
| /web-design/detroit-mi.html | 1,701 | /web-design/columbus-oh.html | 4.2% |
| /web-design/cincinnati-oh.html | 1,571 | /web-design/columbus-oh.html | 3.3% |
| /web-design/columbus-oh.html | 1,681 | /web-design/detroit-mi.html | 4.2% |
| /web-design/pittsburgh-pa.html | 1,933 | /web-design/philadelphia-pa.html | 3.2% |
| /web-design/philadelphia-pa.html | 1,541 | /web-design/fort-worth-tx.html | 3.4% |

Pairs involving a Wave 4 page: 10611 (counted from each side), range 0.0% to 6.1%, mean 1.5%.
(Words = all visible words on the built page, as similarity.py counts them.)
