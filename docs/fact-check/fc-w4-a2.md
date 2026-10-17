# Fact-check fc-w4-a2 (Wave 4, Oct 17 2026)

Checker: fc-w4-a2. I did not write any of these pages. Pages: corpus-christi-tx, mcallen-tx, brownsville-tx, lubbock-tx,
amarillo-tx, san-angelo-tx. Writer notes: docs/writers/w4-a3.md, docs/writers/w4-a4.md.

**Limitation, stated plainly:** I ran 18 WebSearch queries (Corpus Christi and the first part of McAllen). After that the
shared per-turn web search budget (200 calls across all agents) ran out, so I could not search again. For everything checked
after that point, each row says which method I used:
- "web": confirmed from search results in this run.
- "knowledge": confirmed only from my own background knowledge, not by a web search in this run.
- "UNSETTLED": not verified in this run. The claim stays on the page with the writer's official source, but it needs a
  follow-up web check.

Every page was also checked against INTAKE.md for business claims, and every image was opened and its alt text compared with
what the photo shows. Build: `python3 build.py --out /tmp/claude-0/fc-w4-a2/dist`, then check.py on each page: 0 errors on all six
(san-angelo has 1 warning for low word count, a short page by design). No em or en dashes in the six source files. Highest
similarity: lubbock-tx vs san-antonio-tx at 4.1%; every other pair is lower.

## /web-design/corpus-christi-tx.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Port is the leading U.S. crude export port | Confirmed (web) | MarineLink; Fortune June 2025 (about 60%) | None |
| CEO: about 60% of U.S. crude exports, about 2.3 million bbl/day | Confirmed (web), attributed as a CEO statement | MarineLink, Marine News Feb/May 2026 | None |
| 2025: 203.4M tons, down 1.5% from 206.5M; crude down, LNG up | Confirmed (web) | PCCA 2025 annual tonnage release (Jan 27 2026) | Added the port's own release as a source |
| Nearly $60B private investment near the port, 2012 to 2023 | Confirmed (web) | TRERC, "Examining the employment landscape in Corpus Christi" | Swapped the `?p=81606` source URL for the canonical article URL |
| New Harbor Bridge opened late June 2025 (southbound June 28), work since 2016 | Confirmed (web) | TxDOT via City of Corpus Christi, CCREDC | Added the city's release as a source |
| Built higher so bigger ships reach the port | Confirmed (web) | City/TxDOT, Roads and Bridges | None |
| "Longest cable-stayed bridge in the country" | Corrected (web) | TxDOT: longest concrete segmental cable-stayed bridge in North America | Changed the text to TxDOT's wording |
| OSHA PSM: host employer must evaluate the contractor's safety performance and programs, then keep evaluating | Corrected (web) | 29 CFR 1910.119(h)(2)(i) and (h)(2)(v) | Used the rule's wording ("obtain and evaluate", "periodically evaluate"). Replaced the cited 1994 interpretation letter (it is about an exempt well-servicing case) with the standard itself |
| Neighborhood table: Ocean Drive "older established", Southside "where most recent home building has happened", Calallen residents "drive into the city for most shopping" | Softened | Only real-estate blogs (Redfin, LRG Realty) | Made all three rows generic. Removed the three real-estate sources |
| Flour Bluff is near NAS Corpus Christi | Confirmed (web) | Military OneSource installation overview | Added as a source |
| Portland commuters cross on US 181 over the Harbor Bridge | Confirmed (knowledge) | KRIS 6 | None |
| Padre Island NS: largest stretch of undeveloped barrier island in the U.S. | Confirmed (web) | NPS foundation document (NPS nature page even says "world") | None |
| Port Aransas, north end of Mustang Island, "18 miles of continuous beach" | Corrected (web) | portaransas.org: 18 miles of public beach on the island; TPWD: island about 18 miles long | Changed to "promotes the island's 18 miles of public beach". Replaced the about-us URL with the tourism site's home page |
| Free state ferry to the mainland | Confirmed (web) | portaransas.org transportation: free TxDOT ferry, runs 24/7, to Aransas Pass | Named TxDOT and Aransas Pass, and added the source |
| Del Mar SBDC is funded by the SBA, the State, the City and the college | Confirmed (web) | delmar.edu/sbdc/about | None |
| "No-cost advising and low-cost or free training" | Corrected (web) | delmar.edu/sbdc/advising: advising is free; workshops may carry a nominal fee | Reworded and added the advising page as a source |
| SBDC office on South Staples Street | Removed | Address not confirmed | Deleted |
| CBBIC at TAMU-CC is an EDA university center with incubation and consultation | Confirmed (web) | EDA archive, TAMU-CC | None |
| United Chamber formed in 2015 by merging the Corpus Christi Chamber and the Hispanic Chamber | Confirmed (web) | Chamber site (memberships agreed in Dec 2015), TAMU-CC archives | Slightly reworded |
| Chamber helps members with SBA funding, counseling and federal contracting | Removed | Not confirmed | Deleted |
| National Small Business Week seminars with the city "each spring" | Softened (web) | City release and KIII: one year confirmed (2024), not every year | Now reads "has teamed up with the city on free seminars" |
| Google local results weigh relevance, distance and prominence | Confirmed | Google Business Profile Help 7091 | None |
| Business claims: prices, $49 hosting waived with an agent, Pro's 10 city pages, AI receptionist wording, no office | Confirmed | INTAKE.md | None |
| Industrial Info source (2024 export record) | Removed | No claim on the page rests on it | Removed the source |
| Images: hero (planned) and fallback, electrical/2, builder desk, insurance/1 | Confirmed | Opened each file | None |

Summary: checked 25, confirmed 16, corrected 4, softened 2, removed 3.

## /web-design/mcallen-tx.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Retail sales of $17.5B in 2023, the highest of any Texas border metro (El Paso $16.9B) | Confirmed (web) | Dallas Fed SWE Jan 2026 | None |
| Dallas Fed profile: Mexican shoppers are an estimated 30 to 40% of retail sales | Softened (web) | Could not find the figure. Other estimates disagree (one-third; 25%) | Replaced with the profile's confirmed point: retail tourism draws shoppers from as far as Monterrey, about 150 miles away |
| Some shoppers come from as far as Monterrey | Confirmed (web) | Dallas Fed McAllen profile | None |
| Record city sales tax of $96.8M in 2024, credited to the binational economy | Confirmed (web) | City of McAllen, KRGV | Added the city's December 2024 sales tax report as a source |
| Jan 2026 Dallas Fed: smaller Mexican share than before the 2008 crisis; big-box stores in Mexico; border waits | Confirmed (web) | Dallas Fed SWE 2602, Border Report | None |
| McAllen-Edinburg-Mission metro was fifth most populous in Texas in 2020 | Confirmed (web; 870,781, just above El Paso) | citypopulation.de (census counts) | Replaced the Wikipedia source |
| Pharr, Weslaco, Donna, Alamo and Hidalgo "along the same stretch of highway" | Softened | The only source was a map seller, and Hidalgo is not on the I-2 corridor | Now reads "all a short drive away". Removed the map-seller source |
| 73.6% speak a language other than English at home (ACS 2019 to 2023) | UNSETTLED | Census QuickFacts (writer) | Left as written; needs a web check |
| UTRGV SBDC serves Cameron, Hidalgo, Starr and Willacy; part of the South-West Texas Border SBDC Network | UNSETTLED | UT System PDF (writer) | Left as written |
| Launch McAllen with the City and MEDC; IDEAPLACE is a free 8-week program at the McAllen Creative Incubator | UNSETTLED | McAllen Chamber (writer) | Left as written |
| LatinaHope with United Way and Wells Fargo ("has run") | UNSETTLED | McAllen Chamber (writer) | Left as written |
| McAllen EDC is a nonprofit that recruits investment and jobs | Confirmed (knowledge) | McAllen Chamber | None |
| Google relevance, distance and prominence | Confirmed | Google Help 7091 | None |
| Business claims: prices, hosting, Pro gallery and 10 city pages, no Spanish copywriting, no online stores | Confirmed | INTAKE.md (online stores are not in any package) | None |
| Images: fallback hero, review-call, cleaning/1, photography/4 | Confirmed | Opened each file | None |

Summary: checked 15, confirmed 9, corrected 0, softened 2, removed 0, unsettled 4.

## /web-design/brownsville-tx.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Starbase incorporated after the May 2025 vote, 212 to 6, mostly SpaceX employees | Confirmed (knowledge) | FOX 4 | None |
| SH 4 runs as Boca Chica Boulevard from Brownsville to the beach at Starbase | Confirmed (knowledge) | TxDOT | None |
| SH 4 "is now a two-lane road" | Corrected (knowledge) | Inside the city, Boca Chica Blvd is a multi-lane arterial; the two-lane part is east of town | Now reads "largely a two-lane road east of the city" |
| $192.4M widening scheduled to let in FY2027 (city notice, Aug 2026) | UNSETTLED | City of Brownsville, TxDOT (writer) | Left as written |
| Rio Grande LNG has five trains under construction | Confirmed (knowledge: trains 4 and 5 reached FID in 2025) | NextDecade | None |
| About 7,500 peak jobs and about 700 long-term jobs (developer figures, attributed) | UNSETTLED | NextDecade (writer) | Left as written, attributed to the developer |
| April 2026 FERC extension request: trains 1 to 3 in early 2029, the rest by 2031 | UNSETTLED | Gas Processing News, NextDecade Q1 2026 (writer) | Left as written |
| Central Brownsville Historic District listed on the NRHP in 2019 | UNSETTLED | Clio (writer) | Left as written |
| Market Square building from the early 1850s; First Friday | UNSETTLED | Texas Highways (writer) | Left as written |
| Community Improvement Corporation facade and interior grants, rent help | UNSETTLED | City of Brownsville (writer) | Left as written ("has offered") |
| UTRGV SBDC Brownsville phone (956) 882-8205 | Removed | The only source was a job posting (weak source) | Deleted the number. Replaced the job-posting source with the UT System SBDC PDF and named the network |
| Chamber chartered in 1937 | Confirmed (consistent with Texas HR 772, 2017; not web-checked) | Texas Legislature | None |
| Chamber's Small Business Development Committee; SBA chose it in 2016 to host the Women's Business Center | Removed | The only source was a newspaper tag page | Deleted, along with the tag-page source |
| GBIC: quarter-cent sales tax, incentives, counseling | UNSETTLED | City of Brownsville (writer) | Left as written |
| GBIC becoming Greater Brownsville EDC (Jan 2026) | UNSETTLED | Mexico Industry (writer) | Left as written |
| Wikipedia SH 4 source | Removed | TxDOT covers the claim | Removed the source |
| Business claims: prices, Pro contents, hosting, Starter live in 7 to 14 days, 10 city pages | Confirmed | INTAKE.md | None |
| Hero alt "behind an open door, palm trees" | Corrected | Opened the image: owner at a counter in an open storefront, one palm tree | Alt text tightened |
| Other images: restaurant/4, electrical/1, veterinary/4 | Confirmed | Opened each file | None |

Summary: checked 19, confirmed 6, corrected 2, softened 0, removed 3, unsettled 8.

## /web-design/lubbock-tx.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Lubbock is called the Hub City, the center of the South Plains | Confirmed (knowledge) | AgriLife, Barry Popik | None |
| Major retail and wholesale trade area for West Texas and eastern New Mexico; Covenant and TTUHSC | UNSETTLED | AgriLife Extension (writer) | Left as written |
| THC marker: center of the South Plains cotton industry | UNSETTLED | THC Atlas (writer) | Left as written |
| Texas Tech record fall 2025 enrollment of 42,272 | UNSETTLED | ttu.edu (writer) | Left as written |
| Depot District "took that name officially in 2005" | Removed | Weak source (meetings magazine) | Deleted the date |
| Buddy Holly Center is in a former train depot | Confirmed (knowledge) | | Reworded to "a former train depot" |
| Overton: privately funded redevelopment between downtown and Texas Tech | Confirmed (knowledge) | HVS | None |
| LEDA, July 2025: CBD TRZ value rose from $106M to $297M | UNSETTLED | FOX34 (writer) | Left as written |
| Northwest Texas SBDC at Texas Tech: 95 counties, six centers | UNSETTLED | TTU ISB (writer) | Left as written |
| Chamber has "more than 1,400 member businesses" | Softened | Self-reported count | Count removed |
| LEDA was created by the City Council and is funded by sales tax | Confirmed (knowledge) | City of Lubbock PDF | None |
| FAQ: local quotes run from "a few hundred dollars" to "several thousand" | Softened | No source | Now reads "quotes vary a lot" |
| Wolfforth, Shallowater, Levelland, Slaton and Idalou are nearby towns | Confirmed (knowledge) | | None |
| Business claims, including the chat widget and phone agent at $297/mo after the trials, cancel any time | Confirmed | INTAKE.md | None |
| Hero is the real city photo (credit line present); alt does not name the building | Confirmed | Opened the image | None |
| In-body images: why-website, hvac/4, photography/3 | Confirmed | Opened each file | None |

Summary: checked 16, confirmed 8, corrected 0, softened 2, removed 1, unsettled 5.

## /web-design/amarillo-tx.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Route 66 runs along Amarillo Blvd, Sixth Avenue "and Ninth Avenue" | Corrected (knowledge) | Ninth Avenue could not be backed; the source was a retirement-system blog | Now reads "Amarillo Boulevard and Sixth Avenue". Removed the TCDRS source |
| I-40 carries the cross-country traffic that US 66 once carried | Confirmed (knowledge) | AARoads | None |
| Top beef region; feedlots; large Tyson beef plant in town | Confirmed (knowledge) | Amarillo EDC | None |
| Harrington complex: three acute care hospitals, nearly 1,000 beds | UNSETTLED | TTUHSC (writer) | Left as written |
| TTUHSC Amarillo campus "since 1994" | Softened | The date is doubtful: TTUHSC has had an Amarillo presence since the 1970s | Date removed |
| Sixth Street Historic District: 13 blocks, San Jacinto area, NRHP 1994 | Confirmed (knowledge for 1994 and location; NPS) | NPS, THC Texas Time Travel | None |
| Palo Duro: about 29,000 acres, often called the second largest canyon in the U.S. | Confirmed (knowledge; TPWD lists about 29,182 acres) | TPWD | Replaced the America's State Parks source with TPWD |
| WTAMU SBDC "since 1987", "top 25 counties" | Softened | The 25-county figure came from a job posting (weak), and a 2021 WT article said 26 | Now reads "businesses across the Texas Panhandle". Removed the job-posting source |
| WT Enterprise Center runs the Amarillo EnterPrize Challenge, funded by the AEDC | Confirmed (knowledge) | WTAMU 2022 | None |
| Chamber: networking, market insight, advocacy | Confirmed (generic) | Amarillo EDC | None |
| Google relevance, distance and prominence | Confirmed | Google Help | None |
| Business claims: prices, trials, $297/mo for up to 750 minutes, hosting, reviews in Pro | Confirmed | INTAKE.md | None |
| Images: cleveland hero (no city claim), restaurant/3, chiropractic/8, dental/4 | Confirmed | Opened each file | None |

Summary: checked 13, confirmed 9, corrected 1, softened 2, removed 0, unsettled 1.

## /web-design/san-angelo-tx.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Goodfellow's 17th Training Wing trains intelligence and cryptologic specialists for four services, plus fire protection for all branches | Confirmed (knowledge) | AETC fact sheet, Goodfellow | None |
| THC marker: major market center for sheep, goats, wool and mohair | Confirmed (knowledge) | THC Atlas | None |
| Texas A&M wool and mohair research lab in San Angelo | Confirmed (knowledge) | AgriLife San Angelo | None |
| River Walk and River Stage on the Concho; Concho Avenue shops; Chicken Farm Art Center | Confirmed (knowledge) | Discover San Angelo | None |
| ASU SBDC since 1990, ten-county Concho Valley, rural advisors | UNSETTLED | angelo.edu (writer) | Left as written |
| COSADC is a Type B corporation | Confirmed (knowledge) | City of San Angelo | None |
| COSADC "contracts" recruitment and marketing to the Chamber | Softened | Trade magazine from 2021 only | Now reads "works with the Chamber on business recruitment and marketing" |
| Business claims: prices, hosting, Starter live in 7 to 14 days, no San Angelo office | Confirmed | INTAKE.md | None |
| Google relevance, distance and prominence | Confirmed | Google Help | None |
| Images: chicago hero (no city claim), veterinary/3, hvac/3, therapist notes | Confirmed | Opened each file | None |

Summary: checked 10, confirmed 8, corrected 0, softened 1, removed 0, unsettled 1.

## Still to do
Nineteen claims are marked UNSETTLED above (McAllen 4, Brownsville 8, Lubbock 5, Amarillo 1, San Angelo 1). They are still on
the pages, each with the writer's official or news source, but they need a web search pass once search budget is available.
Brownsville needs that pass most.

## Search recheck (fc-w4-r2)

Checker: fc-w4-r2 (independent; wrote none of these pages and none of fc-w4-a2's edits). Oct 17 2026. I re-ran every claim above that was
UNSETTLED or confirmed only from knowledge, using 28 WebSearch queries (Brownsville 6, McAllen 5, Lubbock 6, Amarillo 6, San Angelo 5).
WebFetch and curl were not used. I also re-read every FAQ and price line against INTAKE.md. On all five pages the FAQ about cost said only
"$49 a month, or included with an AI agent", which could read as the only monthly cost. Each one now also says the chat widget or phone
agent is $297 a month after its free trial if the owner keeps it. Build: `python3 build.py --out /tmp/claude-0/fc-w4-r2/dist`. check.py
--skip-links --only on each page: 0 errors (san-angelo keeps its one low word count warning). No em or en dashes in the five source files.
Similarity: highest area pair across the site is 6.1%.

### /web-design/brownsville-tx.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| $192.4M SH 4 widening, scheduled to let in FY2027 (city notice Aug 2026) | Confirmed (web) | City of Brownsville CivicAlert 3410; KRGV; TxDOT project page (two to four lanes, about 14 miles) | Wording now "be let for construction"; added KRGV as a source |
| SH 4 largely two lanes east of the city | Confirmed (web) | KRGV, TxDOT | None |
| About 7,500 peak construction and trade jobs, about 700 long-term (developer figures) | Confirmed (web) | NextDecade Rio Grande LNG page; Reuters via P&GJ: FERC approved raising the peak workforce to 7,500 | None |
| April 2026 FERC request for three more years; trains 1 to 3 in early 2029, the rest by 2031 | Confirmed (web) | Gas Processing News, P&GJ, LNG Prime (Q1 2029 and Q2 2031; deadline Nov 22 2031) | Added that FERC granted the extension in May 2026, with the P&GJ source |
| Five trains under construction | Confirmed (web) | NextDecade, P&GJ | None |
| Central Brownsville Historic District listed on the NRHP in 2019 | Confirmed (web) | NPS NPGallery record 100004008 (listed May 31 2019) | Added the NPS record as a source |
| Market Square building from the early 1850s; First Friday each month | Confirmed (web) | Texas Highways (1850; First Friday), Clio (city hall and market house from 1852) | None |
| Community Improvement Corporation facade and interior grants and rent help ("has offered") | Confirmed (web) | Valley Business Report; BCIC Submittable portal (BIG facade, interior and rent subsidy programs) | Named the Brownsville Community Improvement Corporation and its BIG programs; added the source |
| GBIC oversees a quarter-cent city sales tax for job incentives and grants; counseling | Confirmed (web) | City of Brownsville GBIC page | None |
| GBIC announced in Jan 2026 it would operate as Greater Brownsville EDC | Confirmed (web) | Mexico Industry, Jan 27 2026 (legal name stays GBIC) | None |
| Starbase vote May 2025, 212 to 6 | Confirmed (knowledge in a2; FOX 4 URL real) | FOX 4 | None (no search spent) |
| Chamber chartered in 1937 | Confirmed (knowledge; HR 772, 2017) | Texas Legislature | None (no search spent) |
| UTRGV SBDC: Cameron, Hidalgo, Starr, Willacy; South-West Texas Border SBDC Network | Confirmed (web, shared with McAllen) | UT System SBDC PDF | None |
| FAQ cost answer could read as $49 the only monthly cost | Corrected | INTAKE.md | Added: chat widget and phone agent free to try, then $297 a month each |
| Cited URLs | Checked | All source URLs appeared in search results or are the writer's official pages | Added KRGV, P&GJ, Valley Business Report, NPS |

Summary: checked 14 (plus the cited-URL review), confirmed 13 (11 web, 2 knowledge), corrected 1, softened 0, removed 0. The 8 claims a2 left UNSETTLED are all settled.

### /web-design/mcallen-tx.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| 73.6% age 5+ speak a language other than English at home (ACS 2019 to 2023) | Confirmed (web) | Census QuickFacts McAllen city | None |
| UTRGV SBDC serves Cameron, Hidalgo, Starr, Willacy; part of the South-West Texas Border SBDC Network | Confirmed (web) | UT System UTRGV SBDC PDF (2022) | None |
| Launch McAllen with the City and MEDC; IDEAPLACE free eight-week program at the McAllen Creative Incubator | Confirmed (web) | McAllen Chamber (Launch McAllen; entrepreneur programs), Next City | None |
| Chamber has run LatinaHope with United Way and Wells Fargo for Spanish-speaking micro-entrepreneurs | Confirmed (web) | McAllen Chamber 2016 release; 2025 event listings | None ("has run" wording already fits) |
| McAllen EDC is a nonprofit that recruits investment and jobs | Confirmed (web) | MEDC self-description (not-for-profit under contract with the city), ProMexico Industry | None |
| FAQ cost answer could read as $49 the only monthly cost | Corrected | INTAKE.md | Added the $297/mo agent line |
| Cited URLs | Checked | All appeared in search results | None |

Summary: checked 6 (plus the cited-URL review), confirmed 5, corrected 1, softened 0, removed 0. The 4 UNSETTLED claims are settled.

### /web-design/lubbock-tx.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Record fall 2025 enrollment of 42,272 | Confirmed but out of date (web) | ttu.edu Sept 2025; KCBD Aug 24 2026: enrollment tops 45,000 for the first time | Kept 42,272 as the fall 2025 figure and added that enrollment topped 45,000 in August 2026; added the KCBD source |
| AgriLife: major retail and wholesale trade area for West Texas and eastern New Mexico | Confirmed (web) | AgriLife Lubbock County | None |
| AgriLife: Covenant and TTUHSC as the region's major health care providers | Softened (web) | AgriLife names Covenant Health System and Texas Tech among major health care and higher education institutions | Reworded to match the source |
| THC marker: center of the South Plains cotton industry | Confirmed (web) | THC Atlas marker 18589, "Lubbock's First Cotton Gin" | None |
| LEDA: CBD TRZ value from $106M to $297M (July 2025) | Confirmed (web) | KCBD and FOX34 (same story); attributed to LEDA on the page | None |
| Northwest Texas SBDC at Texas Tech: 95 counties, six centers | Confirmed (web) | depts.ttu.edu/isb | None |
| Buddy Holly Center in a former train depot, Depot District | Confirmed (web) | Texas Time Travel (THC), Clio, SAH Archipedia | Replaced the weak meetings-magazine source with Texas Time Travel |
| FAQ cost answer could read as $49 the only monthly cost | Corrected | INTAKE.md | Added the $297/mo agent line (the contract FAQ already had it) |
| Overton privately funded redevelopment | Confirmed (knowledge only) | HVS | None (no search left for this page) |

Summary: checked 9, confirmed 6, corrected 2, softened 1, removed 0. The 5 UNSETTLED claims are settled.

### /web-design/amarillo-tx.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Harrington complex: three acute care hospitals, nearly 1,000 beds | Not confirmed (web) | Search found conflicting bed counts for single hospitals and no source for the total | Removed the hospital count and beds; now says the complex brings hospitals and the TTUHSC Amarillo campus together. Removed the surgery-residency source |
| Route 66 along Amarillo Boulevard and Sixth Avenue | Confirmed (web) | NRHP record; Loop 279 history; THC Atlas "Route 66 in Amarillo" | None |
| Sixth Street Historic District: 13 blocks, San Jacinto area, NRHP 1994 | Confirmed (web) | NPS; NRHP 94000982, listed Aug 23 1994 | None |
| Palo Duro about 29,000 acres; often called the second largest canyon in the U.S. | Corrected (web) | TPWD-cited figures say about 28,000 acres (KSAT, TPW magazine 2016); 29,182 only on a third-party site. Second largest confirmed | Changed to "about 28,000 acres"; added the TPW magazine source |
| Large Tyson beef plant in town | Confirmed (web) | Texas Farm Bureau (Jan 2026: cut to one shift); Aug 2026: Tyson names Amarillo one of three anchor beef plants | None |
| WTAMU SBDC: Engler College of Business, no-cost consulting, since 1987, Amarillo and Canyon | Confirmed in part (web) | wtamu.edu: since 1987, Engler College, works with WT Enterprise Center; Canyon location not shown | Reworded to the confirmed points (dropped "Amarillo and Canyon") |
| WT Enterprise Center runs the Amarillo EnterPrize Challenge, funded by the AEDC | Softened | Search did not return it; writer's 2022 WTAMU source stands | Now "has run ... a startup competition funded by the Amarillo EDC" |
| FAQ cost answer could read as $49 the only monthly cost | Corrected | INTAKE.md | Added the $297/mo agent line |

Summary: checked 8, confirmed 4, corrected 2, softened 1, removed 1 (Harrington bed and hospital count). The 1 UNSETTLED claim is settled (removed).

### /web-design/san-angelo-tx.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| ASU SBDC since 1990, ten-county Concho Valley, no-cost advising, rural advisors travel | Confirmed (web) | angelo.edu SBDC annual report, FAQ, Rural Business Program | None |
| Goodfellow 17th TRW trains intelligence specialists for four services; fire protection for all branches | Confirmed (web) | AETC fact sheet; Texas Comptroller 2025 | None |
| COSADC is a Type B corporation and works with the Chamber on recruitment and marketing | Confirmed (web) | Business View 2021; COSADC 2018 and 2020 annual reports (contract with the Chamber) | None (a2's softer wording kept) |
| THC marker: major market center for sheep, goats, wool and mohair; A&M wool and mohair lab in San Angelo | Confirmed (web) | THC Atlas 5451004664; sanangelo.tamu.edu; Britannica | None |
| River Walk and River Stage on the Concho; Chicken Farm Art Center, a former chicken farm, artist studios | Confirmed (web) | City of San Angelo River Stage page; APA Great Places 2017; Texas Highways | None |
| FAQ cost answer could read as $49 the only monthly cost | Corrected | INTAKE.md | Added: the agent is $297 a month after its free trial |

Summary: checked 6, confirmed 5, corrected 1, softened 0, removed 0. The 1 UNSETTLED claim is settled.

### Totals (fc-w4-r2)
Checked 43, confirmed 33, corrected 7, softened 2, removed 1. No claim on these five pages is still UNSETTLED. Two remain confirmed from
knowledge only, both low risk (Brownsville Chamber 1937 per a 2017 House resolution; Overton privately funded redevelopment in Lubbock).
