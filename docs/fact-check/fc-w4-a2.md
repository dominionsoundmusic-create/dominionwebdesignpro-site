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
