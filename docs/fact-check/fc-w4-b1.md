# Fact-check report: fc-w4-b1 (Wave 4, Oct 17 2026)

Independent checker. I did not write these pages. Pages: charlotte-nc, greensboro-nc, augusta-ga, raleigh-nc, durham-nc.
Method: WebSearch (6 per page, 30 total, none refused); well-known facts confirmed from my own knowledge and marked PK.
Images: every hero and in-body image opened and its alt text compared with the photo.
Build: `python3 build.py --out /tmp/claude-0/fc-w4-b1/dist`; check.py --only on all five pages: 0 errors, 0 warnings.
Similarity after edits: area pages max 6.1% (all pairs under 15%). No em or en dashes on any of the five pages.

## /web-design/charlotte-nc.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Bank of America and Truist corporate HQs in Charlotte | Confirmed (PK) | Wikipedia, Fortune | none |
| Wells Fargo's largest East Coast operation after buying Wachovia in 2008 | Confirmed (PK) | Fortune | none |
| Japanese bank SMBC picked Charlotte for a second U.S. HQ in 2026 | Confirmed (search) | charlottenc.gov, Axios Apr 7 2026, Banking Dive | none |
| Charlotte about 911,000 (2023 estimate) | Confirmed (PK) | Census QuickFacts | none |
| NC about 1.1 million small businesses, 99.6% (SBA 2025 profile) | Confirmed (search) | advocacy.sba.gov PDF | none |
| LYNX Blue Line links South End, NoDa, UNC Charlotte | Confirmed (PK) | was RentCafe (weak) | Source replaced with Wikipedia: LYNX Blue Line; Uptown added |
| Rail Trail runs Uptown into South End past breweries and galleries | Weak source (Greystar listing) | none | Removed (sentence and Greystar source) |
| NoDa historic arts district (Livability 2026) | Confirmed (PK, magazine source) | Livability | none |
| Northwood bought Ballantyne 2017 for $1.2 billion | Confirmed (search) | Urban Land, Simpson Thacher, PERE | Softened to "most of the office park ... about $1.2 billion" |
| About 17,000 workers a day at Ballantyne | Not found | none | Removed |
| Golf course redeveloped around The Bowl with apartments, shops, hotel | Confirmed (search, Ballantyne Reimagined) | Urban Land, Wikipedia | none |
| SBTDC UNC Charlotte in PORTAL; 8 counties incl. southern Iredell | Confirmed (search) | sbtdc.org/offices/uncc, inside.charlotte.edu | none |
| SBTDC "most services free, all confidential" | Confirmed (PK, SBTDC wording) | sbtdc.org | none |
| SCORE Charlotte free mentoring, Lake Norman, SC border | Confirmed (PK) | score.org/charlotte | none |
| CLT Alliance formed 2018 (Chamber + Regional Partnership), 14-county bi-state | Confirmed (search) | charlotteregion.com | businessnc.com source (unverified URL) replaced with charlotteregion.com Jan 2026 release |
| AMP Up: 141 graduates since 2018 (July 2025) | Confirmed (search) | charlottenc.gov | "mid-2025" made "July 2025" |
| AMP Up cohort 10 asked $175,000 revenue and two years | Not confirmed | none | Removed, and the cohort-10 applications source dropped |
| Google local ranking: relevance, distance, prominence | Confirmed (PK) | support.google.com | none |
| Business claims (prices, trials, AI receptionist, one builder, remote) | Match INTAKE.md | INTAKE.md | none |
| Planner case labeled "an illustration, not a client" | OK | | none |
| Fallback hero alt "comparing an old website ... new design on a tablet" | Wrong (both screens are dark) | the photo | Corrected to what the photo shows |
| In-body alts (consult room, landscaping, gym) | Match photos | the photos | none |

Summary: 21 checked, 13 confirmed (6 search, 7 PK), 3 corrected, 2 softened, 3 removed.

## /web-design/greensboro-nc.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Cone opened White Oak in 1905, alongside Proximity and Revolution | Confirmed (PK) | WFMY, O.Henry | none |
| Sit-in Feb 1 1960, four A&T students, Woolworth on South Elm; desegregated that July | Confirmed (PK) | census.gov | none |
| Civil Rights Center and Museum opened on the 50th anniversary, 2010 | Confirmed (PK) | Wikipedia | none |
| White Oak closed end of 2017, about 200 jobs; "described as" last selvedge mill | Confirmed (PK) | Textile World, Apparel News | none |
| Toyota Liberty batteries from Nov 2025, $13.9 billion, up to 5,100 jobs | Confirmed (search) | IndustryWeek, Axios, Plant Services | none |
| Greensboro and High Point share a metro area | Confirmed (PK) | HUD | none |
| High Point Market each April and October | Confirmed (PK) | | none |
| Nearly 75,000 registered visitors, spring 2026 | Not confirmed (only an ad-platform estimate) | none | Softened to "draws tens of thousands"; Spectrum source removed |
| Greensboro about 302,000 (2023 estimate) | Confirmed (PK) | Census QuickFacts | none |
| A&T fall 2025: 15,275 students, first HBCU over 15,000 | Confirmed (search) | ncat.edu | none |
| A&T "largest HBCU for four straight years" | Wrong (the four-year streak is record HBCU enrollment; A&T says largest public HBCU for 12 straight years) | ncat.edu Points of Pride | Corrected to "by its own count ... largest public HBCU for more than a decade" |
| SBTDC at A&T serves Caswell, Guilford, Randolph, Rockingham | Confirmed (search) | sbtdc.org/locations/greensboro | none |
| "Basic counseling on financing, financial performance and leadership is free" | Partly confirmed (listed services: financial performance, capital, market opportunities) | sbtdc.org | Softened to the listed services |
| City M/WBE Office | Source is an old plan document; office now runs as the Office of Business Opportunity | city PDF, WUNC/WFAE | Softened to "has long run a minority and women owned business program" |
| 2026 race and gender neutral SBE program, directory for Guilford, Rockingham, Randolph firms | Confirmed (search) | WFAE / WUNC May 17 2026 | Dated "May 2026" |
| Chamber: networking, advocacy, Launch Greensboro (LaunchCamp, LaunchLab), Small Business Awards | Confirmed (search) | greensboro.org, chamber.greensboro.org | none |
| Google local ranking | Confirmed (PK) | support.google.com | none |
| Business claims (prices, trials, no stores, AI receptionist, remote) | Match INTAKE.md | | none |
| Hero alt "Hands sketching wireframe ..." | Wrong (hands are on the laptop) | the photo | Corrected |
| HVAC alt "walking ... toward" | Slightly off (standing) | the photo | Corrected |
| Electrical and plumbing alts | Match photos | | none |

Summary: 21 checked, 14 confirmed (5 search, 9 PK), 3 corrected, 3 softened, 1 removed (the 75,000 figure, counted under softened text; Spectrum source removed).

## /web-design/augusta-ga.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| "Augusta Rule": rent a home up to 14 days a year without reporting the income (federal) | Confirmed (PK, IRC 280A(g)) | IRS Pub 527, SmartAsset | Weaver (accounting firm blog) replaced with IRS Publication 527 |
| Augusta Metro Chamber runs the Masters Housing Bureau | Confirmed (PK); search found only the writer's press digest | The Augusta Press | none |
| Bureau revenue helps pay for chamber work | Single-source, not confirmed | none | Removed; sentence now says what the bureau does |
| Renamed Fort Eisenhower Oct 2023; name Fort Gordon restored 2025, honoring MSG Gary I. Gordon, Mogadishu 1993 | Confirmed (search) | Army history page, WRDW June 11 2025, Georgia Encyclopedia | Army history source added; page keeps "in 2025" (Army: June 2025; Encyclopedia: Sept 2025) |
| Army Cyber Command, Cyber CoE, Signal Corps, Georgia Cryptologic Center | Confirmed (PK) | Georgia Encyclopedia | none |
| Georgia Cyber Center: Hull McKnight July 10 2018, second building Jan 2019, 332,000 sq ft, AU campus, range, incubator | Confirmed (PK) | GTA, Tradeline | none |
| MCG the state's only public medical school; Wellstar took over AU hospitals Aug 2023 | Confirmed (PK) | WABE, Wikipedia | none |
| 478-bed medical center, 154-bed children's hospital | Confirmed (PK, writer's AU fact sheet) | MCG 2026 fact sheet | none |
| Wellstar "plans" a 100-bed Grovetown hospital | Out of date: ribbon cut Aug 4 2026, opened to patients Aug 26 2026 | Becker's, AU Jagwire | Corrected to "in August 2026 Wellstar opened ... the first hospital in Columbia County"; Becker's source added |
| Broad Street work until early 2027; one owner 15 to 20% down | Confirmed (search) | WRDW Aug 1 2026, Sept 2 2026 | none |
| Augusta Market 50% off vendor space between 5th and 15th streets | Confirmed (search) | WRDW Aug 29 2026 | none |
| Richmond County about 206,300 (2024 estimate) | Confirmed (PK) | Census QuickFacts | none |
| Summerville: about 730 acres, NRHP 1980, Walton Way, small AU campus | Confirmed (PK) | NPS, Wikipedia | none |
| Evans and Martinez unincorporated, Columbia County; Martinez borders Augusta | Confirmed (PK) | Wikipedia | none |
| Evans "runs north along the Savannah River" | Not confirmed | none | Softened to "Evans lies just past it" |
| North Augusta: 13th Street and 5th Street bridges, Riverside Village, SRP Park, GreenJackets | Confirmed (PK) | Aiken County | none |
| UGA SBDC Augusta, 2907 Professional Parkway, 13 counties as listed | Confirmed (search) | georgiasbdc.org | none |
| Google local ranking | Confirmed (PK) | | none |
| Business claims; Broad Street gift shop labeled illustration | Match INTAKE.md / labeled | | none |
| Alts (contact hero, insurance/4, hire-domain-ownership) | Match photos | | none |

Summary: 20 checked, 16 confirmed (6 search, 10 PK), 1 corrected, 1 softened, 1 removed, 1 source replaced.

## /web-design/raleigh-nc.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Wake County's 12 municipalities; Durham and Angier extend in | Confirmed (PK) | wake.gov | none |
| Wake County 1,232,444 (July 2024), up 9.1% from April 2020 | Confirmed (search; 9.1% checked against 2020 base) | Census QuickFacts | none |
| Raleigh passed 500,000 in 2024, about 33,000 added since 2020, second only to Charlotte | Confirmed (search) | OSBM Oct 2025 | none |
| Cary 180,010 (2023) | Not searched; PK approximate | Census QuickFacts | Softened to "about 180,000" |
| Fuquay-Varina 46,617 (2024) | Not verified | none | Removed (bullet and town source) |
| Downtown Raleigh Alliance's five districts; Capital District buildings; Glenwood South history | Confirmed (PK) | DRA report, Wikipedia | none |
| Kane Realty bought North Hills Mall 2001, credits it with creating Midtown | Confirmed (PK) | Wikipedia, Kane Realty | none |
| RTP 7,000 acres, 78% Durham / 22% Wake, 385+ companies, about 55,000 employees | Confirmed (search) | Research Triangle Foundation Feb 2026 deck | none |
| SBTDC at NC State: Wake plus 8 counties as listed; 16 offices | Confirmed (search) | sbtdc.org/about and office list | none |
| Building Up-fit Grant: up to 50% of interior costs, 49 or fewer employees, city limits | Confirmed (search) | raleighnc.gov | Shop Local Raleigh replaced with two raleighnc.gov pages |
| Grant "quarterly windows, one grant per three years" | Windows confirmed (four in 2024-25); three-year rule not found | raleighnc.gov | Softened to "set windows during the year and paid after the work is finished" |
| Impact Partner Grant for groups supporting underrepresented entrepreneurs | Confirmed (PK) | raleighnc.gov | none |
| Greater Raleigh Chamber small business department; quarterly roundtable (2023) | Low risk, writer's chamber pages; worded "has hosted" | raleighchamber.org | none |
| Raleigh is the state capital | Confirmed (PK) | | none |
| Business claims; no Shopify or stores; Garner plumber labeled example | Match INTAKE.md / labeled | | none |
| Alts (plumbing/3, insurance/4, auto-repair/1, fallback hero) | Match photos | | none |

Summary: 16 checked, 12 confirmed (5 search, 7 PK), 0 corrected, 2 softened, 1 removed, 1 source replaced.

## /web-design/durham-nc.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Watts and Yuille warehouses 1904 on West Main; American Tobacco then Liggett and Myers until 1970 | Confirmed (search) | Wikipedia, Open Durham | none |
| Renamed Brightleaf Square, shops from 1981; retail and office today | Confirmed (search) | Wikipedia, Open Durham | none |
| American Tobacco stopped making cigarettes 1987 | Confirmed (search) | NCpedia, DNCR | none |
| Capitol Broadcasting bought the 16-acre site in 2002 | Conflicting (NCpedia: early 1990s; DNCR: interest late 1990s) | | Softened: no purchase year or acreage, step dated 2004 |
| GSK first business to move in, June 2004 | Confirmed (search) | DNCR, Capitol Broadcasting June 24 2004 | none |
| American Underground opened 2010 in the campus basement | Confirmed (search) | Google, LocalWiki | none |
| About 250 companies and "one of eight" Google tech hubs by 2016 | Counts conflict (7, 8 or 10 by source and year) | | Corrected to "In 2013 Google picked it as one of the first sites in its new tech hub network"; WRAL TechWire source replaced with Capitol Broadcasting 2013 release |
| Duke 48,000+ workforce; largest Durham employer; second-largest private employer in NC | Confirmed (search) | Duke Today, community.duke.edu | none |
| NC Mutual to Parrish Street 1906; M&F Bank 1907; known as Black Wall Street | Confirmed (search) | NCpedia | none |
| Hayti, main Black residential district; 1960s urban renewal damage | Confirmed (PK) | NCpedia, DNCR | none |
| Hayti Heritage Center in the former St. Joseph's AME complex | Confirmed (PK) | WRAL | none |
| RTP 7,000 acres, about 78% in Durham County | Confirmed (search, see Raleigh) | RTF deck | none |
| SBTDC 16 offices, free confidential counseling | Confirmed (search) | sbtdc.org/about | none |
| Which SBTDC office serves Durham (left open by the writer) | Found: SBTDC at NC Central University serves Durham County | sbtdc.org office list, nccu.edu | Added, with NCCU source |
| Black-owned, no certification claimed | Matches INTAKE.md section 7 | | none |
| Hero is the real city photo (Durham Auditorium carving, marquee); credit line | Matches photo | the photo | none |
| In-body alts (cleaning/4, roofing/4, electrical/4) | Match photos | | none |

Summary: 17 checked, 14 confirmed (10 search, 4 PK), 1 corrected, 1 softened, 0 removed (two unsupported numbers dropped inside the correction), 1 fact added.

## Could not settle
- Masters Housing Bureau: kept as run by the Augusta Metro Chamber from my own knowledge plus the writer's press source. Search found no official chamber page for it.
- Fort Gordon restoration date: the Army says June 2025 and the Georgia Encyclopedia says Sept 26 2025. The page says only "in 2025".
- Capitol Broadcasting's purchase year for American Tobacco: sources conflict, so the page no longer gives one.
