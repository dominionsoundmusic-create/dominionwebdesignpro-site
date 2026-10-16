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

## Atlanta add-on (Oct 12 2026)

Three independent sub-agents that did not write the pages checked the six Atlanta add-on pages
against docs/fact-check/BRIEF.md, using web searches of official and credible sources, and fixed
the pages in place. Full tables: docs/fact-check/fc10.md, fc11.md, fc12.md.

| Checker | Pages | Checked | Confirmed | Corrected | Softened | Removed |
|---|---|---:|---:|---:|---:|---:|
| fc10 | /black-owned-web-design/ | 16 | 12 | 1 | 3 | 0 |
| fc10 | /web-design/decatur-ga.html | 21 | 16 | 1 | 3 | 1 |
| fc11 | /web-design/conyers-ga.html | 18 | 17 | 0 | 1 | 0 |
| fc11 | /web-design/mcdonough-ga.html | 15 | 9 | 2 | 4 | 0 |
| fc11 | /web-design/douglasville-ga.html | 17 | 12 | 2 | 3 | 0 |
| fc12 | /web-design/atlanta-ga.html | 28 | 25 | 1 | 1 | 0 |
| | **Total** | **115** | **91** | **7** | **15** | **1** |

**Notable corrections:** the Federal Reserve Small Business Credit Survey figure on the Black-owned
page now gives its fielding date (fall 2020) and scope (non-emergency financing); a Google Maps
"Black-owned filter" was softened to the opt-in Google Business Profile attribute; Decatur's
unconfirmed 2021 Main Street approval removed; Douglasville's county-seat history reworded to the
1875 act that established the town; McDonough's festival years, road-widening timing and SBDC
schedule softened to what current sources confirm; the Atlanta grant window softened to "check with
Invest Atlanta". Business claims: "domain in your name" wording on four pages changed to "the site is
yours outright" (INTAKE says the client owns the site, not whose name the domain is in); schema
described as a Pro feature; the contact form described as INTAKE does; the McDonough FAQ given the AI
receptionist wording. Every page states Black ownership as INTAKE section 7 allows and claims no
certification or membership.

**For Maurice to confirm:** the Atlanta FAQ "Do you do WordPress web design for Atlanta businesses?"
says the packages are sold by what you get, not by a platform name, and asks anyone who needs
WordPress to say so when requesting the demo. INTAKE does not say what platform sites are built on.

## Wave 2 (Oct 16 2026): 13 national city pages

Run by four independent sub-agents that did not write the pages, using docs/fact-check/BRIEF.md and the
writer notes docs/writers/w2-a.md to w2-e.md. Each checked every factual claim and every source URL with
web searches, fixed the source file in place, rebuilt and re-ran check.py. Full tables (Claim | Verdict |
Source | Action): docs/fact-check/fc-w2-a.md, fc-w2-b.md, fc-w2-c.md, fc-w2-d.md.

| Checker | Page | Checked | Confirmed | Corrected | Softened | Removed |
|---|---|---:|---:|---:|---:|---:|
| fc-w2-a | /web-design/st-louis-mo.html | 22 | 18 | 3 | 1 | 0 |
| fc-w2-a | /web-design/kansas-city-mo.html | 19 | 15 | 3 | 1 | 0 |
| fc-w2-a | /web-design/indianapolis-in.html | 16 | 16 | 0 | 0 | 0 |
| fc-w2-b | /web-design/phoenix-az.html | 18 | 12 | 2 | 3 | 1 |
| fc-w2-b | /web-design/las-vegas-nv.html | 17 | 14 | 2 | 0 | 1 |
| fc-w2-b | /web-design/sacramento-ca.html | 25 | 21 | 1 | 1 | 2 |
| fc-w2-c | /web-design/los-angeles-ca.html | 20 | 15 | 3 | 2 | 0 |
| fc-w2-c | /web-design/san-diego-ca.html | 19 (1 not a claim) | 13 | 3 | 1 | 1 |
| fc-w2-c | /web-design/chicago-il.html | 19 (1 not a claim) | 15 | 2 | 1 | 0 |
| fc-w2-c | /web-design/cleveland-oh.html | 17 | 13 | 2 | 2 | 0 |
| fc-w2-d | /web-design/miami-fl.html | 21 | 17 | 1 | 3 | 0 |
| fc-w2-d | /web-design/orlando-fl.html | 17 | 13 | 2 | 2 | 0 |
| fc-w2-d | /web-design/nashville-tn.html | 15 | 12 | 2 | 1 | 0 |
| | **Total** | **245** | **194** | **26** | **18** | **5** |

**Notable corrections:** Phoenix's record heat example moved to Oct 1, 2024 (first 110 degree day in
October) and an unsourced Peoria population removed; SCORE workshops no longer called free everywhere;
Nevada's State Business License wording allows for exemptions and an unsourced chamber member count was
removed; Sacramento's 90,000 state jobs dated to the 2019 study (2017 data), an unconfirmed department list
and a conflicting Metro Chamber/SBDC claim removed; St. Louis populations updated to the newest Census
estimates and the facade program credited to the Community Development Administration; Kansas City,
Missouri now spans Jackson, Clay, Platte and Cass counties and the contractor-exam reciprocity was
corrected to one direction; Los Angeles County population updated, the business tax exemption worded as
the city states it; San Diego's "one-third of the Marine Corps" removed and the SBDC center list replaced
from official sources; Chicago now 58 active SSAs; Cleveland Clinic employer figures updated to the Dec
2022 Ohio Major Employers Report and West Side Market to "more than 70" vendors; Orlando's Main Street
program dated 2008; Nashville's Kurdish Heritage Month proclamation attributed correctly (Mayor John
Cooper, 2022). Business claims on all 13 pages match INTAKE.md (prices, 7 to 14 day Starter launch, 14-day
chat trial, 7-day phone agent trial then $297/mo for up to 750 minutes, $49/mo hosting without the agent,
AI receptionist wording, no office or clients in the city). The Sacramento page states that Dominion does
not hold California's Small Business certification; the Miami page states the site's EN/ES button is
machine translation and does not claim Maurice writes Spanish.
