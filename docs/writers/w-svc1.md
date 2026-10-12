# Writer notes: w-svc1 (service pages, Oct 12 2026)

Four service pages. Package facts on every page come from INTAKE.md (via m.pricing_cards() and prose that repeats only INTAKE wording: $497 / $997 / $1,997 one time, 7 to 14 days, $49/mo hosting unless the AI agent is kept, Pro: schema + Google Business Profile + 10 city pages + reviews shown, Agency: keyword research, 30 to 60 pages typical, custom design). No client, review, ranking or lead claims anywhere. Searches used: 13.

## /small-business-website/ (src/pages/small-business-website.html)
Target: small business website design (2,900/mo). Old hub (docs/old-site/small-business-website/) had no content beyond one sentence; nothing to keep.
Facts stated and sources:
- SBA advises registering a domain name as the first step to an online presence: https://www.sba.gov/business-guide/launch-your-business/choose-your-business-name
- SBA advises buying web design, hosting and domains in the company's name, not the owner's: https://www.sba.gov/blog/2019/2019-03/how-build-business-credit-shoestring-budget/
- "Three ways a site can be laid out" are generic structure patterns (no client or example business named).
Left out: any statistic on how many small businesses have websites (not verified within budget).

## /small-business-website-redesign/ (src/pages/small-business-website-redesign.html)
Target: small business website redesign (2,400/mo); supporting: how much does a website redesign cost.
Facts and sources:
- Google recommends permanent server-side redirects (301/308), mapping each old URL to its new equivalent, avoiding redirecting many URLs to the home page (can be treated as soft 404), avoiding chains, keeping redirects at least 1 year: https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes
- 301/302 redirects do not cause a loss in PageRank: https://developers.google.com/search/docs/crawling-indexing/301-redirects (stated in Google docs per search results; fact-checker please confirm the exact wording is on the redirects page or the site-move page)
- ICANN: transferring between registrars is the registrant's right; registrar must let you get the auth code or provide it within five calendar days; transfer fee may be charged but a transfer cannot be denied for non-payment of that fee: https://www.icann.org/resources/pages/name-holder-faqs-2017-10-10-en and https://www.icann.org/en/contracted-parties/accredited-registrars/resources/domain-name-transfers/policy
- SBA: buy domains/web services in the company's name (link above).
- Cost table: Siimple, custom build by designer or agency typically $1,000 to $10,000 (https://getsiimple.com/tools/website-cost-calculator); G2, small business site under 20 pages $2,000 to $8,000 (https://www.g2.com/articles/how-much-does-a-website-cost); Shopify, hosting $5 to $250 a month (https://www.shopify.com/blog/how-much-does-a-website-cost). These are new-build costs; the page says redesigns are usually priced like a new build (reasoning, not a sourced statistic).
- FAQ answer "around $1,000 to $10,000" summarizes the Siimple and G2 ranges.
Left out: redesign-specific ranges from agency blogs (lowcode.agency, 925studios etc.) because their figures and currencies conflicted between articles; the Clutch "$42,500 average" (secondhand, not verified at source).

## /affordable-website-design/ (src/pages/affordable-website-design.html)
Target: affordable website design for small business (720/mo).
Facts and sources:
- Wix Light about $17/mo billed annually, monthly billing costs more: https://www.websitebuilderexpert.com/website-builders/wix-pricing/ (third-party; Wix's own page not reachable with the tools here)
- Squarespace Basic about $16/mo billed annually, monthly billing higher: https://outfy.com/blog/squarespace-pricing (third-party; several trackers agreed)
- "Over five years either plan adds up to roughly a thousand dollars": arithmetic ($16 to $17 x 60 = $960 to $1,020).
- "Most builders do not let you carry the design to another host": general knowledge, not separately cited; fact-checker may want to confirm or soften.
- The page states honestly that Dominion's $49/mo hosting (without the AI agent) is more than the cheapest builder plan.
Wording kept distinct from /pricing/ and the cost guide: no market cost ranges restated here.

## /seo-web-design/ (src/pages/seo-web-design.html)
Target: seo web design (2,900/mo) plus seo for websites (14,800/mo). Old hub had no content.
Facts and sources (all Google's own documentation):
- Starter Guide: no secrets that automatically rank a site first; best practices make it easier to crawl and understand; headings to break up content; most new pages found through links; descriptive anchor text: https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- Good titles are unique, clear, accurate; Google uses the title element and other sources for title links: https://developers.google.com/search/docs/appearance/title-link
- Mobile version used for indexing: https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing
- Core Web Vitals good thresholds LCP 2.5 s, INP under 200 ms, CLS below 0.1; aligns with what core ranking systems reward: https://developers.google.com/search/docs/appearance/core-web-vitals
- Structured data and rich results eligibility: https://developers.google.com/search/docs/appearance/structured-data/search-gallery
- Do you need an SEO: hiring can help only if you act on it; avoid anyone promising first place, a "special relationship" or "priority submit"; sitemap is one of the direct ways to submit: https://developers.google.com/search/docs/fundamentals/do-i-need-seo
- Helpful content: people-first content: https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- Local results based mainly on relevance, distance, prominence; prominence includes links and reviews; no way to request or pay for better local ranking: https://support.google.com/business/answer/7091?hl=en
- Site speed claims about this build (WebP at several sizes, hero loaded first, width/height on images) describe the build system in CLAUDE.md.

## Images
Existing: images/cities/atlanta-sole-proprietor.jpg (hero), gilmer-business.jpg, demo-images/default/2.jpg, demo-images/salon/1.jpg (small business); marshall-business.jpg, demo-images/default/3.jpg (redesign); atlanta-food-truck.jpg (hero), kilgore-business.jpg, demo-images/cleaning/2.jpg (affordable); longview-business.jpg, demo-images/restaurant/2.jpg (SEO).
Planned (desc given): images/heroes/small-business-website-redesign-hero.jpg, images/heroes/seo-web-design-hero.jpg, images/body/seo-city-pages-planning.jpg.
