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

## Wave 3 (Oct 17 2026): 8 national city pages

Run by four independent sub-agents that did not write the pages, using docs/fact-check/BRIEF.md and the
writer notes docs/writers/w3-a.md to w3-d.md (each writer also flagged its weakest claims for them). Each checked
every factual claim and every source URL with web searches, fixed the source file in place, rebuilt and re-ran
check.py. Full tables (Claim | Verdict | Source | Action): docs/fact-check/fc-w3-a.md, fc-w3-b.md, fc-w3-c.md, fc-w3-d.md.

| Checker | Page | Checked | Confirmed | Corrected | Softened | Removed |
|---|---|---:|---:|---:|---:|---:|
| fc-w3-a | /web-design/new-york-ny.html | 25 | 18 | 5 | 2 | 0 |
| fc-w3-a | /web-design/orange-county-ca.html | 23 | 19 | 1 | 2 | 1 |
| fc-w3-b | /web-design/tampa-fl.html | 28 | 26 | 1 | 1 | 0 |
| fc-w3-b | /web-design/huntsville-al.html | 25 | 20 | 3 | 2 | 0 |
| fc-w3-c | /web-design/tucson-az.html | 17 | 13 | 2 | 1 | 0 (1 figure cut inside a corrected row) |
| fc-w3-c | /web-design/richmond-va.html | 27 | 18 | 1 | 7 | 1 |
| fc-w3-d | /web-design/louisville-ky.html | 24 | 19 | 0 | 5 | 0 |
| fc-w3-d | /web-design/wilmington-nc.html | 25 | 20 | 0 | 5 | 0 |
| | **Total** | **194** | **153** | **13** | **25** | **2** |

**Notable corrections:** New York's Business Improvement District numbers updated to the FY25 report (78 BIDs, more
than $216 million, nearly 25,000 storefronts) and Census figures to the July 2025 estimate; an unverified court-rule PDF
link replaced with the court system's Part 1200 page; the Irvine HOA claim (sourced to a remodeler blog) softened and the
blog removed; Orange County SCORE wording corrected. Tampa's storm-surge line now separates surge height (6.3 ft gauge)
from flooding; an unconfirmed Seminole Heights corridor dropped; SAM.gov and UEI facts on the Huntsville page now cite
sam.gov, gsa.gov and sba.gov; Marshall Space Flight Center's workforce replaced with NASA's own figure; Lowe Mill dated to
1901 with "more than 150 studios"; SCORE Alabama described as a virtual chapter. Tucson's income figures updated to
QuickFacts 2020 to 2024 ($57,073 vs $80,734) and Vail's incorporation votes dated (2013 and 2023); Richmond's Scott's
Addition plant dates fixed (the Coca-Cola plant is 1953) and the cidery noted as having moved. Louisville's hotel line
limited to downtown hotels and Whiskey Row history softened to what sources support; Wilmington's Cargo District counts
attributed to the developer as rough figures and "record" dropped from UNCW's total enrollment.

## Wave 4 (Oct 17 2026): 81 city pages

Run by independent sub-agents that wrote none of the pages, using docs/fact-check/BRIEF.md, docs/fact-check/BRIEF-WAVE4.md
and the writer notes docs/writers/w4-*.md. Each checked the claims and cited sources on its pages with web searches, fixed
the source files in place, rebuilt and re-ran check.py. Full tables (Claim | Verdict | Source | Action) are in
docs/fact-check/fc-w4-*.md.

Web searches are capped at 200 per orchestrator turn, shared by every running agent. The first Part A checkers ran out
partway and confirmed some claims from prior knowledge; those pages then got a second, search-only recheck (fc-w4-r1,
r2, r3). Later checkers worked with a fixed budget of about 6 searches per page and marked any claim confirmed without a
search as "PK" (well-known geography and history) in their tables. Where a specific number could not be confirmed it was
softened or removed, never kept on trust. Four pages written with little or no research (Little Rock, Greenville SC,
Memphis, Chattanooga) got a research pass before their fact-check.

| Checker | Pages | Checked | Confirmed | Corrected | Softened | Removed |
|---|---|---:|---:|---:|---:|---:|
| fc-w4-a1 | San Antonio, Laredo, Temple, Fort Worth, Arlington, Abilene | 88 | 59 | 7 | 15 | 6 |
| fc-w4-a2 | Corpus Christi, McAllen, Brownsville, Lubbock, Amarillo, San Angelo | 98 | 56 | 7 | 9 | 7 |
| fc-w4-a3 | Midland, Odessa, Killeen, Sugar Land, Katy, Cypress | 95 | 55 | 6 | 8 | 3 |
| fc-w4-a4 | Nacogdoches, Texarkana, Beaumont, Round Rock, The Woodlands | 76 | 51 | 4 | 11 | 7 |
| fc-w4-r1 (search recheck) | Temple, Fort Worth, Arlington, Abilene | 43 | 30 | 6 | 2 | 4 |
| fc-w4-r2 (search recheck) | McAllen, Brownsville, Lubbock, Amarillo, San Angelo | 43 | 33 | 7 | 2 | 1 |
| fc-w4-r3 (search recheck) | Killeen, Sugar Land, Katy, Cypress, Beaumont, Round Rock, The Woodlands, Texarkana | 53 | 26 | 13 | 4 | 9 |
| fc-w4-b1 | Charlotte, Greensboro, Augusta, Raleigh, Durham | 95 | 69 | 8 | 9 | 6 |
| fc-w4-b2 | Montgomery, Charleston, Columbia, Greenville, Savannah | 67 | 51 | 3 | 12 | 1 |
| fc-w4-b3 | Jacksonville, Tallahassee, Fort Lauderdale, West Palm Beach, Pensacola | 68 | 51 | 6 | 6 | 3 |
| fc-w4-b4 | St. Petersburg, Sarasota, Fort Myers, New Orleans, Baton Rouge | 91 | 65 | 10 | 12 | 3 |
| fc-w4-b5 | Shreveport, Birmingham, Mobile, Jackson, Knoxville | 85 | 58 | 13 | 8 | 5 |
| fc-w4-b6 | Chattanooga, Memphis, Lexington, Little Rock | 82 | 58 | 10 | 8 | 4 |
| fc-w4-c1 | Denver, Colorado Springs, Fort Collins, Seattle, Spokane | 90 | 56 | 11 | 17 | 3 |
| fc-w4-c2 | Boise, Portland, Salt Lake City, Reno, San Francisco | 80 | 64 | 8 | 7 | 1 |
| fc-w4-c3 | San Jose, Long Beach, Fresno, Bakersfield, Albuquerque | 88 | 58 | 20 | 6 | 4 |
| fc-w4-c4 | Scottsdale, Mesa, Tulsa, Oklahoma City, Omaha | 76 | 54 | 8 | 11 | 3 |
| fc-w4-c5 | Des Moines, Minneapolis, Madison, Grand Rapids, Pittsburgh | 71 | 48 | 11 | 9 | 2 |
| fc-w4-c6 | Philadelphia, Detroit, Cincinnati, Columbus | 71 | 49 | 10 | 7 | 1 |
| | **Total** | **1,460** | **991** | **168** | **163** | **73** |

(Rows can sum to less than "checked": a few claims per page were kept on the writer's official source without a new
search, or left as written with the reason in the table.)

**Business claims.** The most common correction across all three parts: pricing FAQs that gave hosting as "$49 a month,
or included while you keep the AI agent" without saying the agent itself costs $297 a month after its free trial, so the
$49 read as the only monthly cost. Every Wave 4 pricing answer now states both, as INTAKE.md requires (the phone agent
must not read as free). Five more pages (and the existing Cedar Park page) were fixed directly. Other INTAKE fixes: an
Oklahoma City line that said Pro "adds ten more pages" (Pro is a 10-page site); a Philadelphia FAQ with the hosting rule
backward and another that implied Maurice answers the phone (it is the AI receptionist, which can transfer); a Baton Rouge
line implying updates come with the build.

**Notable factual corrections.** Leon County repealed the Tallahassee minority and women business certification thresholds
the page quoted; Wellstar's Grovetown hospital opened in August 2026 (the page said "plans"); NC A&T is the largest public
HBCU, not the largest HBCU; the Pennsylvania SBDC lead office moved to Kutztown in 2018 and Wharton's own center closed in
2019; the Florida SBDC Network is headquartered at UWF, with FGCU as a regional office; the Birmingham SBDC at UAB closed in
2008 (the Greater Birmingham SBDC is at Innovation Depot); Baton Rouge and Shreveport SBDC offices are hosted by Southern
University; Montgomery's 908th Airlift Wing became the 908th Flying Training Wing in 2024; Fort Hood carries its restored
name; the Temple page's Killeen business resource center closed in December 2024; Lubbock's Texas Tech enrollment updated
to more than 45,000 (fall 2026); Columbus uses Ohio State's autumn 2026 figures; the Des Moines State Fair figures use the
2026 record attendance; a Memphis FedEx claim attributed to a report that does not exist was replaced; a Lexington SBA
percentage that was really the women-owned share was removed; San Jose's "Little Saigon designated 2007" became the true
2007 to 2008 naming dispute; Bakersfield's Epoch Times sourced oil figure was cut; Mesa's "more people than Atlanta" was
cut (Atlanta's estimate is higher). The St. Petersburg city photo in images/cities/ shows the 1917 Pinellas County
Courthouse in Clearwater, so it was not used for St. Petersburg.

**Weak sources removed.** Real-estate blogs, moving-company guides, commercial property listings (Crexi), travel
listicles, sponsored newspaper content, GuideStar profiles and Wikipedia pages without a better source behind them were
replaced with official or reputable sources, or the claim was softened or cut.

**Alt text.** Every checker opened every image on its pages; dozens of alt texts were tightened to describe exactly what
the photo shows, and none claims a generic photo shows the city. Photos with readable lettering or brand names were swapped
out by the writers (camera brands, AC unit labels, awning signs, an Apple logo, a car maker emblem).
