# Fact-check report: fc-w4-c2 (Wave 4, Oct 17 2026)

Independent checker. I did not write any of these pages. I checked them against INTAKE.md, the writer notes
(docs/writers/w4-c2.md, w4-c3.md, w4-c4.md) and web searches. WebFetch is blocked, so claims were checked against
search results from the official or credible source. Search budget: 6 searches per page, 30 in total, all used.
"PK" means the claim is well-known geography or a basic fact I confirmed from my own knowledge without a search.

Built into /tmp/claude-0/fc-w4-c2/dist. check.py --only on each page: 0 errors, 0 warnings. Similarity: area max
6.1% across all area pairs (under 15%). No em or en dashes. 3 to 6 FAQs on each page. `m.no_office` appears once per page.
Every alt text was checked against its photo (contact sheets of all 17 images). All 17 alt texts match their photos.
Real city photos are used only for Boise (images/cities/boise-id.jpg) and Reno (images/cities/reno-nv.jpg).

## /web-design/boise-id.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| COMPASS April 2026: Ada + Canyon 876,760 | Confirmed (search) | COMPASS 2026 news release | none |
| Boise 256,450, Meridian 152,070 (COMPASS 2026) | Confirmed (cited table; total confirmed in search) | COMPASS population table | none |
| Meridian 3.1% vs Boise 1.4% a year earlier (BoiseDev) | Softened | COMPASS 2026 release: Caldwell +5,160, Kuna +4,810, Meridian +4,730 | Replaced with "Meridian, Caldwell and Kuna each added more than 4,500 people in the year to April 2026"; BoiseDev source removed |
| Census 2021: Meridian, Nampa, Caldwell in top 15 fastest-growing cities of 50,000+ | Confirmed (search) | Census press release May 26 2022 (ranked 13, 14, 15) | Added the Census release as a primary source |
| Micron HQ in Boise; about $15B fab announced 2022; about 2,000 direct jobs | Confirmed (PK plus Idaho Commerce citation) | Idaho Commerce | none |
| Micron targets first wafer output mid-2027, second Boise fab late 2028 | Confirmed (search) | Idaho News, FY2026 results | none |
| Hyde Park, North End, 13th and Eastman, first suburban commercial center, historic district | Confirmed (cited city page plus PK) | City of Boise historic district page | none |
| Basque Block = 600 block of Grove St; museum founded 1985 | Confirmed (search) | Basque Museum (601 and 607 Grove) | none |
| City "formally inaugurated the block in 2000" | Softened | ACHP; AP: major city streetscape work in the early 2000s, no inauguration year found | Now says "city-funded streetscape work in the early 2000s"; weak Euskal Kazeta source replaced with ACHP |
| Bown Crossing "anchors one of the area's popular neighborhoods" (WorldAtlas) | Softened | PK (Southeast Boise shopping village) | Reworded to a plain place description; WorldAtlas source removed (weak) |
| Idaho SBDC lead center at Boise State since Jan 1986, six regional centers, free confidential consulting | Confirmed (search) | Idaho SBDC 40-year page | none |
| Boise Metro Chamber 2026 small business awards, June 23, Boise Centre | Confirmed (search) | Idaho Business Review | none |
| City of Boise small business guide; economic development office | Confirmed (cited city pages, PK) | cityofboise.org | none |
| Google local results: relevance, distance, prominence | Confirmed (PK) | Google Business Profile Help | none |
| Boise is one hour behind Big Sandy | Confirmed (PK: Mountain vs Central) | none needed | none |
| Prices, trials, hosting, $297 agents (FAQ and body) | Confirmed against INTAKE.md | INTAKE.md | none |

Summary: 16 checked, 13 confirmed, 0 corrected, 3 softened, 0 removed (plus 3 weak sources removed or replaced, Census release added). 6 searches, 10 PK or cited-source checks.

## /web-design/portland-or.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Five address sections for decades, South Portland added 2020 east of SW Naito / View Point Terrace, about 6,000 addresses, SW to S, leading zeros dropped, USPS one more year | Confirmed (PK plus cited Portland Mercury, OPB, KATU) | cited sources | none |
| Last Southwest signs scheduled to come down May 2025 | Confirmed by cited PBOT document; already hedged ("scheduled") | portland.gov PBOT document | none |
| Neighborhoods by section (St. Johns and Mississippi N, Alberta NE, Hawthorne, Division, Sellwood SE, Pearl NW) | Confirmed (PK) | Travel Portland | none |
| Last Thursday: about 15 blocks of Alberta closed, summer evenings, 6 to 9 p.m. | Confirmed (search) | Travel Portland, KOIN | The cited portland.gov URL could not be found; replaced with the Travel Portland Last Thursday page |
| Mississippi Street Fair, July, 30,000+ visitors | Confirmed (search; tourism-board figure) | Travel Portland | none |
| Portland Made founded 2012 by Kelley Roy, ADX founder | Confirmed (search) | portlandmade.com | none |
| 2018 Urban Manufacturing Alliance snapshot with PSU and Prosper Portland | Confirmed (cited UMA press release) | urbanmfg.org | none |
| Metro about 2.54 million in 2024 (Portland-Vancouver-Hillsboro) | Confirmed (search: 2,537,904) | FRED PORPOP | none |
| Vancouver WA in the same metro; Beaverton, Gresham, Lake Oswego, Hillsboro | Confirmed (PK; MSA name) | FRED | Wikipedia Portland metropolitan area source removed (weak, nothing rests on it alone) |
| SBA 2024 Oregon: 409,958 small businesses, 99.4%, 53.5% of employees | Confirmed (search) | SBA Advocacy Oregon.pdf | none |
| PCC SBDC free confidential advising plus paid training | Confirmed (cited PCC page, PK) | pcc.edu | none |
| PCC SBDC advises at the Chamber "on Tuesdays by appointment" | Softened | not re-verified | "on Tuesdays" removed; now "by appointment at the Portland Metro Chamber office" |
| Prosper Portland IBRN launched 2017, services | Confirmed (cited Prosper Portland page) | prosperportland.us/ibrn | none |
| PBA took back the Portland Metro Chamber name June 2023; roots in Portland Trade Board 1870 | Confirmed (search) | portlandmetrochamber.com about page | Wikipedia source replaced with the chamber's own About page |
| FAQ "what you pay every month": $49 hosting unless you keep an AI agent | Corrected | INTAKE.md | Now also says the AI agent costs $297 a month after its free trial, so $49 never reads as the only monthly cost |
| Other prices, trials, no online store, AI receptionist wording | Confirmed against INTAKE.md | INTAKE.md | none |

Summary: 16 checked, 14 confirmed, 1 corrected, 1 softened, 0 removed (plus 2 Wikipedia sources and 1 dead portland.gov URL replaced or removed). 6 searches, 10 PK or cited-source checks.

## /web-design/salt-lake-city-ut.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Most people live between Ogden and Provo, about 80 miles along I-15 | Confirmed (PK) | none needed | none |
| Urban area "rarely more than 18 miles wide" | Removed | Wikipedia only | Removed |
| "Around four out of five Utahns live along this corridor" | Corrected | Gardner: Salt Lake + Utah counties about 56%, Weber + Davis 18.7% | Now "About three of every four Utahns live in its four core counties: Salt Lake, Utah, Davis and Weber"; Wikipedia replaced with Gardner fact sheet |
| Utah youngest state, median age 31.3 in the 2020 census | Confirmed (search) | Gardner blog | none |
| 20.4% of households with five or more people, the highest share | Confirmed (search) | Gardner 2020 census households fact sheet | Added the fact sheet as a source (the writer had asked the checker to confirm which page carries it) |
| Median age 32.1 in 2022, up from 30.5 in 2014 (Tribune) | Confirmed (search) | Salt Lake Tribune 2024-09-18 | none |
| Silicon Slopes: Draper, Lehi, Orem, Provo; Lehi at its center; Adobe Lehi campus 2012 | Confirmed (PK plus cited CNBC) | CNBC via NBC LA | none |
| 9th and 9th at 900 South and 900 East; Sugar House southeast with its park | Confirmed (PK) | ABC4 | none |
| SBA 2024 Utah: 352,191, 99.4%, 45.7% | Confirmed (search) | SBA Advocacy Utah.pdf | none |
| Utah SBDC office at SLCC Miller Campus in Sandy, free consulting | Confirmed (PK plus cited Valley Journals) | Valley Journals Apr 2026 | none |
| Salt Lake Chamber, "Utah's largest and longest-serving business association", roots to 1887 | Confirmed (search) | slchamber.com/about | none |
| EDLF: seven loans, about $1.3M approved by the City Council in 2022 | Confirmed (search) | The Enterprise; slc.gov EDLF page | Added the city's EDLF page as a source |
| Builder "more than 1,000 miles away" | Confirmed (calculated: about 1,085 miles straight line) | calculation | none |
| FAQ: $49 hosting "waived while you keep an AI agent" | Corrected | INTAKE.md | Added "which costs $297 a month after its free trial" |
| Other prices, 7 to 14 days, waves, AI receptionist wording | Confirmed against INTAKE.md | INTAKE.md | none |

Summary: 15 checked, 12 confirmed, 2 corrected, 0 softened, 1 removed. 6 searches, 9 PK, cited-source or calculation checks.

## /web-design/reno-nv.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| TRIC in Storey County, more than 100,000 acres | Confirmed (PK plus cited Guardian) | Guardian via AOL | none |
| "Tesla's Gigafactory was its original anchor after Tesla bought land there in 2013" | Corrected | Las Vegas Sun 2015 and others: the park already had many companies before Tesla; the Gigafactory was announced in 2014 | Now "The park already had many tenants when Tesla chose it for its Gigafactory, announced in 2014, which became its best-known tenant"; Manufacturing.net source replaced |
| Switch began building in 2015 | Confirmed (cited This Is Reno, 2015) | This Is Reno | none |
| Google subsidiary bought 1,210 acres in 2017 | Confirmed (search: "more than 1,200 acres", KOLO and KNPR) | 9to5Google | none |
| EDAWN: 501(c)(6) nonprofit founded 1983, focus on primary companies that export | Confirmed (search) | edawn.org/about | none |
| Reno 2020 census count 264,146 | Corrected | Census 2020 count is 264,165 (264,146 is the estimates base) | Changed to 264,165 |
| 274,915 July 2023 estimate; "4.1% rise" | Confirmed / Softened | Census QuickFacts | Now "a rise of about 4%" (recomputed against the census count) |
| Metro about 575,100 in 2024 (USAFacts) | Corrected | HUD Reno-Sparks market profile: about 505,600 on Jan 1 2024; 575,100 has no Census backing | Replaced with the HUD figure and source |
| Midtown along South Virginia St south of downtown: murals, cafes, thrift stores, patio pubs | Confirmed (PK plus cited Reno Historical) | renohistorical.org | none |
| Riverwalk Merchants Association: "about 50 businesses ... between Arlington and Lake streets" | Softened | searches show 20+ wine walk stops and 60+ coalition members; no source for 50 or the street bounds | Now "brings together dozens of nearby restaurants, shops, salons and museums" |
| Wine walk on the third Saturday of every month | Confirmed (search) | renoriver.org event page | Membership kit source replaced with the wine walk page |
| Sparks a separate city; South Meadows, Northwest Reno, Somersett, Damonte Ranch | Confirmed (PK) | none needed | Redfin source removed (weak) |
| Nevada SBDC state office at UNR, Ansari Business Building; free confidential advising | Confirmed (PK plus cited KOLO and nevadasbdc.org) | cited | none |
| Reno + Sparks Chamber advocating since 1919 | Confirmed (search) | Congressional Record 2019 (centennial; 1919 merger) | none |
| Hero alt: Washoe County Courthouse, dome, columns, snow, flag | Confirmed (photo viewed) | image | none |
| Prices, trials, hosting, WordPress FAQ, AI receptionist wording | Confirmed against INTAKE.md | INTAKE.md | none |

Summary: 16 checked, 11 confirmed, 3 corrected, 2 softened, 0 removed (plus 1 weak source removed and 3 replaced). 6 searches, 10 PK or cited-source checks.

## /web-design/san-francisco-ca.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Legacy Business Registry: 30+ years, no break over 2 years, contributed to history or identity | Confirmed (search) | sf.gov step by step | none |
| 20+ years with significant contribution and displacement risk | Confirmed (cited 2022 application form; PK Admin Code 2A.242) | sf.gov form | none |
| HPC recommends, Small Business Commission decides; applying is free | Confirmed (search) | sf.gov | Added the required nomination by a supervisor or the mayor, which the page left out |
| Listing does not entitle a business to grant money | Confirmed (cited form) | sf.gov form | none |
| 2026: 39 small businesses in long-term leases incl. Bayview, Mission, Excelsior | Confirmed (search) | OEWD press release; Local News Matters | Added the sf.gov press release |
| Corridor programs on Mission, Clement, Irving and Third streets | Confirmed (search; historical, page already says "have long been") | Mayor Lee release | none |
| ABAG: nine counties, 101 cities and towns | Confirmed (PK plus cited ABAG) | abag.ca.gov | none |
| Office of Small Business: central point of information, Permit Center at 49 South Van Ness, free counseling | Confirmed (PK plus cited sf.gov) | sf.gov | none |
| SF SBDC "hosted by the Office of Small Business" | Corrected | search: hosted by the city's Office of Economic and Workforce Development | Changed to OEWD |
| SBDC free confidential consulting in English, Spanish, Mandarin, Cantonese; restaurant program | Confirmed (search) | Venturize, sf.gov | none |
| SCORE SF and East Bay: free mentoring by video, in person or email; Oakland office | Confirmed (search: 5627 Telegraph Ave, Oakland) | score.org | none |
| SF Chamber founded 1850 during the Gold Rush; 900+ member companies | Confirmed (search) | sfchamber.com, 2026 benefits PDF | none |
| Micro-business tier "for one to three employees" | Softened | 2026 PDF shows individual and micro-business benefits; the 1 to 3 employee definition was not confirmed | Now "membership options include individuals and micro-businesses" |
| Three-year Pro math: $997 + $1,764 = $2,761 | Confirmed (arithmetic: $49 x 36 = $1,764) | INTAKE.md | none |
| "Two time zones away" | Confirmed (PK: Central to Pacific) | none needed | none |
| FAQ: $49 hosting "or included while you keep the AI agent" | Corrected | INTAKE.md | Added "which is $297 a month after its free trial" |
| Other prices, trials, WordPress FAQ, AI receptionist wording, no ranking promise | Confirmed against INTAKE.md | INTAKE.md | none |

Summary: 17 checked, 14 confirmed, 2 corrected (plus 1 missing fact added), 1 softened, 0 removed. 6 searches, 11 PK, cited-source or arithmetic checks.

## Totals
80 claims checked: 64 confirmed, 8 corrected, 7 softened, 1 removed (plus 2 more removed sources and source swaps as listed above).
30 searches.

Not fully settled (left as written because the cited source supports it and it is low risk): the May 2025 South Portland
sign removal (from a PBOT document), the Boise and Meridian city figures (COMPASS table, not shown in my search,
though the two-county total matched), and the Nevada SBDC's Ansari Building location (PK).
