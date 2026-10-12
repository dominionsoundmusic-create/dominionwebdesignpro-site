# Fact-check fc2 (independent checker, Oct 12 2026)

Pages: /small-business-website/, /small-business-website-redesign/, /affordable-website-design/, /seo-web-design/.
Method: read CLAUDE.md, INTAKE.md, docs/WRITING-GUIDE.md and docs/writers/w-svc1.md, listed every non-obvious claim, verified with WebSearch (24 searches; WebFetch blocked), restricted to the official domain where possible (developers.google.com, support.google.com, icann.org, sba.gov, wix.com, squarespace.com, support.wix.com, support.squarespace.com). Package and business claims were compared with INTAKE.md. The /compare/ and /site-check/ tool descriptions were checked against src/static/compare/index.html and netlify/functions/seo-audit.mjs.
Build: `python3 build.py --out /tmp/claude-0/fc2/dist`; `scripts/check.py --skip-links --only <url>`: 0 errors on all four pages after the fixes.

## /small-business-website/

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Package facts: Starter 5 pages (home, services, about, contact, service area), $497/$997/$1,997 one time, 7 to 14 days, $49/mo hosting without AI agent, Pro adds gallery, 5 more pages, 10 city pages, Agency keyword research and waves inside two weeks | Confirmed | INTAKE.md | None |
| Starter: mobile, form emails leads, titles/descriptions, sitemap to Google, Maps and hours, Facebook/Instagram links, owned outright | Confirmed | INTAKE.md | None |
| Maurice works from Big Sandy, builds nationwide remotely | Confirmed | INTAKE.md | None |
| "Most of the owners who ask about this already have something online" | Softened | Implied observation about the business's prospects, not verifiable | Changed to "Many owners looking for a small business website already have something online." |
| SBA advises registering a domain name as the first step to an online presence | Confirmed, wording tightened | https://www.sba.gov/business-guide/launch-your-business/choose-your-business-name ("If you want an online presence for your business, start by registering a domain name") | Reworded to match SBA wording |
| SBA advises buying web design, hosting and domains in the company's name | Confirmed | SBA blog "How to build business credit on a shoestring budget" | Source URL changed to the current canonical https://www.sba.gov/blog/how-build-business-credit-shoestring-budget (the /2019/2019-03/ path did not appear in search) |
| Three layout patterns, common problems list | Not factual claims (general advice, no client named) | n/a | None |

## /small-business-website-redesign/

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Google recommends permanent server-side redirects (301/308), map each old URL to its new equivalent | Confirmed | https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes | None |
| Redirecting many URLs to the home page can be treated as a soft 404 | Confirmed | Same | None |
| Avoid redirect chains | Confirmed (Google: Googlebot follows up to 10 hops, redirect to final destination directly) | Same; 301-redirects page | None |
| Keep redirects at least 1 year | Confirmed ("as long as possible, generally at least 1 year") | Same | None |
| 301 redirects do not cause a loss in PageRank | Confirmed for permanent redirects; the wording ("301 and other permanent redirects don't cause a loss in PageRank") is on the site-move page, not shown for 302s | site-move-with-url-changes | Text now says "Google's site move guide says permanent redirects like these do not cause a loss in PageRank." |
| Google follows 301s and moves signals to the new page (FAQ) | Confirmed | Google crawling/indexing FAQ: ranking signals pass across 301 redirects | None |
| ICANN: transfer is the registrant's right; auth code via account or within five calendar days; fee may be charged but transfer cannot be denied for non-payment of it | Confirmed | https://www.icann.org/resources/pages/name-holder-faqs-2017-10-10-en ; ICANN Transfer Policy | None |
| SBA: buy domains and web services in the company's name | Confirmed | SBA blog | Source URL updated to canonical form |
| Siimple: custom build by designer or agency $1,000 to $10,000 | Confirmed | https://getsiimple.com/tools/website-cost-calculator | None |
| G2: small business site under 20 pages $2,000 to $8,000 | Confirmed (assumes under 20 pages, few stock photos, simple functionality) | https://www.g2.com/articles/how-much-does-a-website-cost | None |
| Shopify: hosting $5 to $250 a month | Removed | Range appears on Shopify's AU/NZ/UK editions; the cited US page could not be confirmed to carry it and the US ecommerce post gives $2.49 to $1,000+ | Table row and source deleted |
| FAQ: "most small business sites from freelancers and small studios around $1,000 to $10,000, agencies often quote more" | Corrected | Siimple says designer or agency custom build | Now "a custom small business site from a web designer or agency at roughly $1,000 to $10,000, with larger agency projects costing more" |
| Redesign priced at package price, redirect map included | Consistent with INTAKE.md (no new price or promise) | INTAKE.md | None |
| Before and After tool compares Google PageSpeed scores; Site Check reports titles, headings, search basics | Confirmed | src/static/compare/index.html (PageSpeed Insights API); netlify/functions/seo-audit.mjs | None |

## /affordable-website-design/

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Wix Light about $17/mo billed annually, monthly billing higher ($24) | Confirmed | Wix blog/plans; Website Builder Expert; Craftybase | Added wix.com/plans as a source; corrected Website Builder Expert URL to /website-builders/wix/wix-pricing/ |
| Squarespace Basic about $16/mo billed annually | Corrected | Squarespace's own pricing page shows Basic $19/mo billed annually ($25 monthly); PetaPixel (July 17, 2026) reports the July 2026 rise from $16 to $19 | Now $19; added note that Squarespace raised prices in July 2026; Outfy source replaced with squarespace.com/pricing and PetaPixel |
| Five-year total "roughly a thousand dollars"; "most businesses move up a tier" | Corrected / Softened | Arithmetic: $17 x 60 = $1,020, $19 x 60 = $1,140; "most businesses move up" unverifiable | Now "roughly $1,000 to $1,150, more if you move up a tier" |
| "Most builders do not let you carry the design to another host" | Softened to what was verified | Wix Help Center: SaaS architecture does not support external hosting; Squarespace Help Center: designs and templates cannot be exported, export is limited content in WordPress XML | Now names Wix and Squarespace specifically, both sources added |
| "Most owners ... have been quoted two extremes" | Softened | Unverifiable observation | Now "often run into two extremes" |
| Starter contents, $49/mo hosting unless AI agent kept, Pro/Agency extras, no store, no retainer, no ranking promises | Confirmed | INTAKE.md | None |
| Dominion's $49/mo is more than the cheapest builder plan | Confirmed ($49 > $17/$19) | Above | None |
| Maurice works from Big Sandy, remote nationwide | Confirmed | INTAKE.md | None |

## /seo-web-design/

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Starter Guide: no secrets that automatically rank a site first; best practices make it easier to crawl and understand | Confirmed (guide intro: "won't tell you any secrets that'll automatically rank your site first ... (sorry!)") | https://developers.google.com/search/docs/fundamentals/seo-starter-guide (wording seen via secondary copy) | None |
| Starter Guide recommends headings | Confirmed | Starter Guide | None |
| Google finds most new pages through links | Confirmed ("the vast majority of the new pages Google finds every day are through links") | Starter Guide | Attributed to the Starter Guide in the table |
| Good titles unique, clear, accurate; title element among sources for title links | Confirmed | https://developers.google.com/search/docs/appearance/title-link | None |
| Sitemap is one of the direct ways to submit to Google | Confirmed ("the only way to submit a site to Google directly is through the URL Inspection Tool, by submitting a Sitemap, or ... the Indexing API") | do-i-need-seo | None |
| Google uses the mobile version for indexing | Confirmed | mobile-first indexing best practices | None |
| CWV good thresholds: LCP 2.5 s or less, INP under 200 ms, CLS below 0.1 | Confirmed | https://developers.google.com/search/docs/appearance/core-web-vitals | None |
| "Google says good scores align with what its ranking systems reward" | Corrected | Google: Core Web Vitals are used by its ranking systems, recommends good scores; good scores do not ensure top rankings | Reworded to match |
| Structured data can make a page eligible for rich results | Confirmed | search-gallery | None |
| Helpful content: made for people vs. mainly to attract search visits | Confirmed | creating-helpful-content | None |
| Local results based mainly on relevance, distance, prominence; prominence includes links and reviews; cannot request or pay for better local ranking | Confirmed | https://support.google.com/business/answer/7091?hl=en | None |
| Do you need an SEO: find someone else if they promise first place; beware "special relationship", "priority submit" | Confirmed | https://developers.google.com/search/docs/fundamentals/do-i-need-seo | None |
| FAQ: hiring help useful "but only if you will act on what you are told" | Softened | Not confirmed as Google wording; Google does say a small local business can probably do much of the work itself | Reworded: small local business can do much itself, hiring can be useful, avoid anyone promising first place ("guarantees" replaced to satisfy banned-word check) |
| Build claims: WebP at several sizes, hero loaded first, width/height on images, few scripts | Confirmed against build system (CLAUDE.md speed rules) | CLAUDE.md | None |
| Pro: schema, GBP setup, 10 city pages, real Google reviews; Agency keyword research | Confirmed | INTAKE.md | None |

## Summary

Checked 56, confirmed 42, corrected 5, softened 8, removed 1.
Most important fixes: Squarespace Basic price was out of date ($16, now $19 after the July 2026 increase); "most builders" lock-in claim replaced with sourced Wix and Squarespace help-center statements; Shopify hosting row removed (unverified on the cited page); Core Web Vitals ranking wording aligned with Google's text; PageRank claim scoped to permanent redirects per the site-move page.
