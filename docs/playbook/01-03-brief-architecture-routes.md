# Prompts 1 to 3: fact brief, architecture, baseline (Oct 12 2026)

## Prompt 1: client fact brief

Source: INTAKE.md (filled Oct 12 2026 from Maurice Johnson's statements and the live site), CLAUDE.md,
the live site on main (docs/old-site/).

| Item | Value | Status |
|---|---|---|
| Name | Dominion Web Design Pro, a d/b/a of Dominion Digital Group | Confirmed |
| Owner | Maurice Johnson, builds every site himself; may be named | Confirmed |
| Category | Hand-written websites for local businesses, free demo first | Confirmed |
| Services | Websites, city and service-area pages, local SEO setup, AI chat widget and AI phone agent add-ons, free tools | Confirmed |
| Packages | Starter $497, Pro $997 (Most Popular), Agency $1,997, one time; Stripe links; hosting $49/mo without the AI agent | Confirmed (INTAKE wins over the live site, see decisions 18) |
| Base | Big Sandy, Texas; 279 Boyd Road, Big Sandy, TX 75755, shown only on privacy, terms and in schema | Confirmed |
| Phone | (903) 636-7511, tel:+19036367511, AI receptionist 24/7 that transfers to Maurice | Confirmed |
| Email | maurice@dominionwebdesignpro.com | Confirmed |
| Hours | Phone answered any hour by the AI receptionist; no office hours displayed | Confirmed |
| Year established | Not displayed | Confirmed rule |
| CTAs | Primary: free demo (/demo.html). Secondary: packages, phone | Confirmed |
| Brand | Blue #2563EB / #1D4ED8, gold #F5A623, near-black #0A0F1A, images/dominion-logo.svg, favicons | Confirmed |
| Faith | John 3:16 in the top bar; the Jesse Duplantis quote with its credit near the top of every page | Confirmed |
| Social | Facebook and YouTube top and footer; x.com in schema sameAs as on the live site | Confirmed |
| Analytics | GA4 G-3MZXMC1JKS with phone-tap event | Confirmed |
| Forms | Netlify: homepage-contact, client-intake, site-check | Confirmed |
| Reviews, testimonials, portfolio, awards, years, job counts, guarantees | None approved | Confirmed rule |
| Service area | Nationwide remote; East Texas home turf; Texas metros with demand; existing Georgia pages | Confirmed |
| Domain | https://dominionwebdesignpro.com | Confirmed |

Contradictions found: the live site's AI phone agent trial (14 days vs INTAKE 7), "Unlimited pages",
a three-month minimum and a yearly discount on city pages, and "Dominion Solar Pro" in the footer.
Resolved in INTAKE's favor (docs/decisions.md 18, 22). Launch blockers in content: none. Deferred: the
photos listed in docs/image-list.md.

## Prompt 2: architecture

Not an SSR framework project: the live site was hand-written static HTML with no build. This rebuild
uses the same static pre-rendered system as the Phoenix build: Python 3 + Jinja2 build.py, YAML front
matter per page in src/pages/, central src/data/site.json (business, phone, pricing, nav, services,
guides, areas), shared templates (header, footer, hero, FAQ, call band) and macros. Every title,
canonical, heading, body and JSON-LD block is in the raw HTML; nothing is client-rendered. The only
JavaScript is the menu, the EN/ES toggle, GA4 and the copied tool pages' own scripts. Commands:
`python3 build.py`, `python3 scripts/check.py`, `python3 scripts/check_old_urls.py`,
`python3 scripts/check_tool_pages.py`, `python3 scripts/similarity.py`, `python3 scripts/grep_check.py`,
`python3 scripts/keyword_plan.py`, `node scripts/responsive_check.js`. The playbook's AI Studio,
TanStack and form-embed steps do not apply and were mapped to this system. Deployment: Netlify
publishes the committed dist/ (netlify.toml); netlify/functions/seo-audit.mjs deploys as before.

## Prompt 3: baseline and route matrix

Baseline: the live site (main) had no build, typecheck or tests to run. It was saved to docs/old-site/.
Pre-existing issues: dark all-over design, em dashes throughout, emoji icons, claims INTAKE does not
support (decisions 18, 22), thin hub pages (the six "by city" hubs), no /contact/ page.

| Route | Type | Source | Nav | Sitemap | Indexable | Status |
|---|---|---|---|---|---|---|
| / | home | src/pages/index.html | logo | yes | yes | rebuilt |
| /services/, /pricing/, /how-it-works/, /faq/, /contact/ | core | src/pages/*.html | header/footer | yes | yes | new |
| /about.html, /service-areas.html, /how-city-pages-work.html, /web-design/ | core | src/pages (url: flat) | header/footer | yes | yes | rebuilt at the same URL |
| /small-business-website/, /contractor-website-design/, /seo-web-design/ | service | src/pages | Services menu, footer | yes | yes | rebuilt at the same URL |
| /small-business-website-redesign/, /affordable-website-design/, /web-design-for-plumbers/, /roofing-contractor-website-design/, /web-design-for-law-firms/, /web-design-for-therapists/ | service | src/pages | Services menu, footer | yes | yes | new |
| /small-business-website-cost.html | guide | src/pages (url: flat) | Guides menu, footer | yes | yes | rebuilt |
| 6 more guides (/how-much-does-a-website-designer-cost/ etc.) | guide | src/pages | Guides menu, footer | yes | yes | new |
| /web-design/<town>.html x 26 | area | src/pages/web-design/ | Cities menu, footer | yes | yes | 19 rebuilt, 7 new |
| /privacy-policy.html, /terms.html | legal | src/pages (url: flat) | footer | yes | yes | rebuilt |
| /404.html | error | src/pages/404.html | none | no | noindex | new |
| /demo.html, /demo-generator.html, /site-check/, /compare/, /tools/, /intake/ | tool | src/static (copied) | Free Tools menu, footer | yes | yes | copied through |
| /intake/thanks/, /contact/thanks/ | tool | src/static (copied) | none | no | noindex (as live) | copied through |
| 5 retired hubs, /website-design-for-contractors.html, blog and retired URL rules | 301 | src/static/_redirects | none | no | n/a | kept or re-pointed |

Implementation plan: Prompts 4 to 6 (config, brand, navigation) in the shared system; Prompts 7 to 12
written page by page by separate writer sub-agents following docs/WRITING-GUIDE.md; Prompts 13 to 15
(forms, social, media) in the templates and tool-page checks; Prompts 16 to 20 by the scripts above,
a browser run and independent fact-check sub-agents (docs/playbook/04-20-build-qa-handoff.md).
