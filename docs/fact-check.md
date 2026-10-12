# Independent fact-check (Oct 12 2026)

**What was run.** After all 55 content pages were written by nine writer sub-agents, nine separate
fact-check sub-agents (fc1 to fc9) checked every factual claim and cited source. None of them wrote
any page it checked. Each followed docs/fact-check/BRIEF.md: list every non-obvious claim (numbers,
dates, populations, laws and rule numbers, agencies, chambers, SBDC and SCORE offices, corridors,
employers, events, third-party prices, survey statistics, and everything said about Dominion Web
Design Pro), verify it, then confirm, correct, soften or remove it in place, re-run build.py and
check.py on its pages, and log every claim. Claim-by-claim tables: docs/fact-check/fc1.md to fc9.md.
Writer notes with each fact's source: docs/writers/.

**Method limit (read this).** This environment blocks direct page fetches (WebFetch and curl fail for
census.gov, capitol.texas.gov, google.com and nearly every source). Claims were verified against
WebSearch result summaries of the named official or credible source, not by opening the page. The
search budget was shared by all checkers; fc1 and fc3 ran out before their last few searches, and
the handful of low-risk items not searched again are marked "known" or "rests on the writer's source"
in their logs. To re-verify by opening every source, allow those domains in the environment's network
settings and re-run the checkers.

| Checker | Pages | Claims | Confirmed | Corrected | Softened | Removed |
|---|---|---:|---:|---:|---:|---:|
| fc1 | /, /services/, /pricing/, /how-it-works/, /faq/, /about.html, /contact/, /how-city-pages-work.html, privacy, terms, 404, /service-areas.html, /web-design/, plus site.json vs INTAKE.md | 96 | 72 | 7 | 14 | 3 |
| fc2 | /small-business-website/, /small-business-website-redesign/, /affordable-website-design/, /seo-web-design/ | 56 | 42 | 5 | 8 | 1 |
| fc3 | contractor, plumbers, roofing, law firms, therapists | 44 | 32 | 8 | 3 | 1 |
| fc4 | /small-business-website-cost.html, designer cost, cost per month, packages explained | 44 | 33 | 7 | 3 | 1 |
| fc5 | builder vs designer, hiring a web designer, does a small business need a website | 31 | 23 | 3 | 4 | 1 |
| fc6 | Houston, Kingwood, Dallas, Waco, El Paso, Plano, Frisco | 74 | 58 | 5 | 9 | 2 |
| fc7 | McKinney, Denton, Atlanta, Lawrenceville, Tyler, Longview, East Texas | 66 | 48 | 8 | 8 | 2 |
| fc8 | Gilmer, Kilgore, Marshall, Gladewater, Austin, Cedar Park | 61 | 49 | 4 | 6 | 2 |
| fc9 | Leander, Pflugerville, Kyle, San Marcos, Dripping Springs, New Braunfels | 63 | 43 | 11 | 6 | 3 |
| **Total** | **55 pages** | **535** | **400** | **58** | **61** | **16** |

**Notable corrections:** Squarespace prices updated after its July 2026 increase; Upwork project
rates replaced with Upwork's current figures; the ABA Model Rule 7.1 wording separated from its
comments and Rule 7.2(c) applied to certification claims; the Texas plumbing rule (22 TAC 367.10)
cited for invoices and advertising; the McKinney airport updated (terminal opening November 11, 2026,
Avelo); Eastman's Longview plant status updated; SBDC coverage corrected on five Austin-area pages
(New Braunfels is served by the UTSA SBDC); Plano's 12th Street DART station corrected; El Paso
language figure stated as persons, not households; Cedar Park's population ranking softened; the
Pflugerville chamber CEO's name removed (she left in January 2026); a recycled "73% of small
businesses" figure removed. Business claims: every page was checked against INTAKE.md; lines not in
INTAKE ("no contract", the receptionist taking messages, free changes outside upkeep, a general
"cancel any time") were removed or limited to what INTAKE says.

**Still open:** Texas HB 3344 (a 2025 bill for a state reroofing license through TDLR). Searches found
the committee documents but not its final status; the roofing page describes it only as a proposed
2025 bill and tells roofers to check TDLR and their city.
