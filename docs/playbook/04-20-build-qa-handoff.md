# Prompts 4 to 20: build, QA and handoff (Oct 12 2026)

Every playbook step was mapped to this static build system (docs/playbook/01-03-brief-architecture-routes.md).

| Prompt | What was done | Validation actually performed |
|---|---|---|
| 4 Business data | src/data/site.json holds name, d/b/a, owner, phone (once, display and tel), email, address, AI receptionist wording, CTAs, GA4 id, social links, sister brands, the three plans with Stripe links, hosting note and the page-count note | fc1 compared site.json to INTAKE.md word by word: no mismatch. Old-identity sweep: no Phoenix, pool or other-business text (check.py, similarity.py --other) |
| 5 Brand system | site.css tokens: header blue #1D4ED8, blue #2563EB, gold #F5A623, near-black #0A0F1A; gold buttons with near-black text; white sections, first band blue, second gold, call band and footer near-black; self-hosted Inter; the live EN/ES pill | Screenshots at 390 to 2560 px; contrast choices in docs/decisions.md 28 to 30 |
| 6 Navigation | Header: Services, Pricing, Cities, Guides, Free Tools menus, About, Contact; EN/ES toggle; tap-to-call. Footer: services, tools, 26 cities, guides, company, sister brands, social icons | check.py: 0 broken internal links on 63 pages; keyboard and Escape handling in site.js; menus tested at 1440 and 390 |
| 7 Home | Hero (photo, H1 with "website design company", two CTAs), demo-first story, process band, services, packages (#pricing), free tools band, near-me and city section, homepage-contact form, 6 FAQs | check.py, browser load with 0 JS errors, form present by name |
| 8 Services overview | /services/ built ("web design services", 8,100/mo) from site.json | links checked |
| 9 Service pages | 9 pages, each with its own design treatment (page-plan tables, checklists, comparison tables, insurance wording table, lawyer-rules panel) | check.py, similarity (max 2.5%), fact-check fc2 and fc3 |
| 10 Areas overview | /service-areas.html (Texas coverage, no-office language) and /web-design/ (directory) | check.py, fc1 |
| 11 Area pages | 26 city pages: 19 rebuilt at the same URLs with their research re-verified, 7 new (Houston, Dallas, Tyler, East Texas, Waco, El Paso, Kingwood); each with corridors, chambers, SBDC/SCORE, why local search matters, four reasons, no-office note, FAQs, sources | similarity max 4.5%; fact-check fc6 to fc9 |
| 12 Supporting pages | About, FAQ, How it works, How city pages work, privacy, terms (marked not legal advice), 404 | check.py, fc1 |
| 13 Forms | homepage-contact on / and /contact/ (identical markup to the live form), client-intake and site-check copied through byte for byte, all rendered in static HTML | check_tool_pages.py; tool_pages_browser.js finds every form by name. Lead delivery not verified (no production submission) |
| 14 Social and profiles | Facebook and YouTube icons top and footer with labels; "Review us on Google" link; sameAs in schema. No review widget (no approved reviews) | check.py requires both links on every page |
| 15 Media | Existing photos reused (city photos, contractor photos, demo-images without printed words); 48 planned photos (20 heroes) with Artistly prompts in docs/image-list.md, shown as brand-blue blocks meanwhile; WebP 480 to 1920 srcset; hero preloaded, eager, fetchpriority high; in-body lazy | check.py image rules; browser broken-image check: 0 |
| 16 SEO | Unique title, description, canonical (same as the live URLs), OG and Twitter tags, one JSON-LD graph (ProfessionalService, WebPage, BreadcrumbList, Service, Article, FAQPage), sitemap.xml with every indexable page and the indexable tool pages, robots.txt, 404 noindex | check.py on raw HTML |
| 17 Remnant sweep | Old-client and placeholder sweep (Phoenix text, pool terms, (623), lorem, TODO, UNKNOWN), old live-site claims INTAKE does not support (unlimited pages, three-month minimum, yearly discount, 14-day phone agent trial, Dominion Solar Pro) | check.py, grep_check.py, similarity.py --other: 0 hits |
| 18 Responsive and accessibility | Skip link, focus styles, aria labels on icon links and toggles, details/summary FAQs, reduced-motion CSS, tables stack on phones | responsive_check.js: 262 loads, 0 problems |
| 19 Functional | Menus, toggle, links, CTAs, phone links (tel:+19036367511 only), forms, tool page scripts | tool_pages_browser.js 10/10; third-party calls blocked in this sandbox (not verified) |
| 20 Final QA and handoff | docs/qa.md | All scripted checks pass |

## Route inventory

55 built content pages (13 core, 9 services, 7 guides, 26 cities) plus 8 tool pages copied through.
Every old URL on main resolves (285 checked). Full list: dist/sitemap.xml and docs/qa.md.

## Remaining placeholders and missing assets

48 photos in docs/image-list.md (20 heroes at 1920x1080, 28 in-body at 1200x800).

## Launch blockers and readiness

No content blocker. Not production-verified here: Netlify deploy of dist/ with the new netlify.toml,
Pretty URLs and redirects in production, form delivery, the Site Check function and the demo backend
from the live domain, Google Translate. Readiness decision: ready for Maurice's review on a Netlify
deploy preview of the `build` branch; not merged, not deployed.

## Exact files changed

New: build.py, netlify.toml, .gitignore, SERVICES.md, src/ (pages, templates, data, static), scripts/,
docs/ (decisions, keyword plan, image list, QA, fact-check, writers, playbook, old-site). Moved: the
live site's images/, demo-images/, icons, _redirects, _headers and tool pages into src/static/ at the
same paths. Removed from the repo root: the old hand-written pages (kept in docs/old-site/).
