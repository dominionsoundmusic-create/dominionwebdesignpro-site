# Fact-check fc-w4-c5 (Wave 4, Oct 17 2026)

Independent checker, did not write these pages. Writer notes: docs/writers/w4-c7.md, w4-c8.md, w4-c10.md.
Search budget: 30 WebSearch calls used in total (6 per page). WebFetch not used. "PK" means confirmed from
the checker's own knowledge (well-known geography or history), not by a search in this pass.
All five pages: alt text checked against the actual image files (all describe what the photo shows; none claims a
city photo). Pricing checked against INTAKE.md. Each pricing FAQ said only "$49 a month, or included while you
keep the AI agent", which could read as if $49 hosting were the only monthly cost, so each now also says the
chat widget (Pro) or phone agent (Agency) costs $297 a month after its free trial. Des Moines' body pricing
paragraph also had no $297 mention and now gives both trials.
Build: `python3 build.py --out /tmp/claude-0/fc-w4-c5/dist`; check.py --only on each page: 0 errors, 0 warnings.
Similarity: area max 6.1% after edits. No em or en dashes. FAQ counts unchanged (5 each).

## /web-design/des-moines-ia.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| More than 80 insurance company HQs in Greater Des Moines | Corrected | dsmpartnership.com insurance page says "nearly 80 of Iowa's insurance companies headquartered here" | Changed to "Nearly 80 of Iowa's insurance companies are headquartered in Greater Des Moines" |
| 2025 State Fair Aug 7 to 17, 1,160,121, third-highest; 2024 record 1,182,682 | Confirmed, but out of date | KTIV/KCRG 2025, iowastatefair.org | The 2026 fair has happened, so the section now uses 2026 figures |
| (new) 2026 fair Aug 13 to 23, 1,218,834, all-time record | Corrected (updated) | iowastatefair.org 2026 release; KCRG/KTIV Aug 2026 | Added; 2025 and 2024 kept as comparison |
| Common Sense Institute: fairgoers spent about $85 million | Removed | Searches show CSI's 2025 figure as $177M to state GDP, not $85M spent | Cut. KIMT source swapped for the fair's 2026 release and KCRG |
| Waukee and Ankeny first and second for population gain (LSA 2025) | Softened | Search: 2025 Census estimates, gain since 2020, Waukee 10,949, Ankeny 9,731 | Now "added more residents since 2020 than any other Iowa city" |
| Ankeny about 77,800 (2025 estimate) | Confirmed | citypopulation.de / Census 77,833 | Kept |
| Metro 758,539 (2025) | Softened | Not confirmed in search | Now "roughly three quarters of a million people" |
| Beaverdale one of the largest of 51 neighborhood associations; Beaver Avenue business district | Confirmed | Search (Wikipedia, beaverdale.org) | Kept |
| Brick homes in Beaverdale | Confirmed (PK) | Writer's source, beaverdale.org | Kept |
| East Village, Ingersoll and Grand, Valley Junction 120+ shops | Confirmed (writer's source, Partnership) | dsmpartnership.com | Kept (not re-searched) |
| Mid Iowa SBDC in Des Moines, serving Polk, Dallas, Warren, Jasper, Marion; free counseling and workshops | Confirmed | iowasbdc.org | Kept |
| SCORE Des Moines free mentoring | Confirmed (PK) | score.org | Kept |
| SBA 2024 Iowa: 282,323, 99.3%, 45.6% | Confirmed (writer's source, official PDF) | advocacy.sba.gov | Kept, not re-searched |
| Google local ranking: relevance, distance, prominence | Confirmed (PK) | support.google.com/business/answer/7091 | Kept |
| Pricing, trials, AI receptionist wording, no office | Confirmed vs INTAKE.md after fix | INTAKE.md | Added $297 after-trial wording in FAQ 1 and body |

Summary: checked 15, confirmed 9, corrected 3, softened 2, removed 1. Search 6 / PK 3.

## /web-design/minneapolis-mn.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| We Love Lake Street: more than $12M, over 80,000 donors, about $7M to roughly 350 businesses when TCB profiled it | Confirmed (dated, attributed) | TCB, Spokesman-Recorder; other outlets give $11M/65,000/500 at other dates | Kept as attributed to the TCB profile |
| Funds mostly for construction repairs, inventory, equipment | Confirmed | Lake Street Council recovery report | Kept |
| $1.4M to 20 entrepreneurs (acquisition and predevelopment fund) | Confirmed (writer's source, Council annual report) | visitlakestreet.com | Kept |
| Five years on, almost all businesses came back (KSTP) | Confirmed (writer's source) | KSTP | Kept |
| LEDC founded 2003, Mercado Central bought its building in 2019 | Confirmed | Bush Foundation, SW Connector | Kept |
| Mercado organizing began 1991; LEDC helped develop Midtown Global Market | Confirmed (writer's sources, PK) | minneapolis.org, community-wealth.org | Kept |
| Karmel Mall 100+ small businesses | Confirmed (writer's source, Fortune 2026) | Fortune | Kept |
| "By 1998 Cedar-Riverside had one of the largest Somali communities in Minnesota" | Softened | Search found refugee arrivals in the 1990s, not the 1998 claim | Now "arriving in large numbers in the 1990s ... became a center of Somali life in Minnesota" |
| About half of roughly 8,000 residents of East African descent | Confirmed | Augsburg Digitours; DMNA | Kept |
| Art-A-Whirl first held 1995; NEMAA 1997; 1,600+ members; district set 2002 | Confirmed (NEMAA's own history; some sources say 1996/2003) | nemaa.org | Kept |
| BTAP up to 50 hours no-cost consulting, 25+ providers, list shows community and languages | Confirmed | minneapolismn.gov | Kept |
| MCCD Open to Business, seven-county metro | Confirmed (writer's source) | GuideStar | Kept |
| Minnesota has 9 SBDCs plus satellites | Confirmed | mn.gov/deed | Kept; added that the Twin Cities metro center is hosted by the University of St. Thomas (DEED/MnSBDC brochure) |
| Google ranking factors | Confirmed (PK) | Google help | Kept |
| Ecommerce and translation not in packages; pricing and trials | Confirmed vs INTAKE.md | INTAKE.md | Added $297 after-trial wording to FAQ 2 |

Summary: checked 15, confirmed 12, corrected 2 (SBDC detail, pricing FAQ), softened 1, removed 0. Search 6 / PK 3.

## /web-design/madison-wi.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Market on the Capitol Square Saturdays April to November, 2026 season April 11 to Nov 14; Wednesday market | Confirmed | visitmadison.com, isthmus.com | Kept |
| Widely described as largest producer-only market in the country; sell-outs | Confirmed | visitmadison.com, travelwisconsin.com | Kept |
| Madison about 286,000 (2025), second largest after Milwaukee; metro about 710,000 | Confirmed | citypopulation.de (286,233), FRED/Wikipedia (709,685) | Kept |
| UW-Madison about 51,800 students fall 2025 | Corrected | news.wisc.edu reports 51,865 | Now "nearly 52,000" |
| Incoming class 8,500 | Confirmed | news.wisc.edu | Kept |
| Epic more than 13,000 employees, 12,500 in Verona | Softened | WPR: "around 13,000"; no current Verona split found | Now "around 13,000 people, most of them at its Verona campus" |
| Willy Street: in 1984 neighbors blocked a fast food chain, land became Willy Street Park | Softened | Search found nothing confirming the year or park | Now "the American Planning Association credits neighbors with pushing back against chain development" |
| Willy Street Co-op opened 1974, Middleton store 2010 | Confirmed (PK) | Isthmus, Daily Cardinal | Kept |
| Atwood Avenue: Craftsman bungalows, Saturday cafe culture | Softened | Only source was a real-estate/relocation blog (weak) | Now plain geography (PK): runs east from Williamson toward Schenk-Atwood with local shops and cafes; Latitude source removed |
| Wisconsin SBDC at UW-Madison: no-cost, confidential, mainly Dane, Sauk, Columbia | Confirmed | sbdc.wisc.edu | Kept |
| City Office of Business Resources, facade grants, KIVA 0% loans, Black Chamber match | Confirmed (writer's sources, city site) | cityofmadison.com | Kept, not re-searched |
| SBA 2025 Wisconsin: 497,370, 99.4%, 48.0% | Confirmed (writer's source, official PDF) | advocacy.sba.gov | Kept, not re-searched |
| Pricing, trials | Confirmed vs INTAKE.md | INTAKE.md | Added $297 after-trial wording to FAQ 2 |

Summary: checked 13, confirmed 8, corrected 2 (enrollment, pricing FAQ), softened 3, removed 0 (one weak source dropped). Search 6 / PK 3.

## /web-design/grand-rapids-mi.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Haldane cabinet shop 1836; awards at the 1876 Centennial; Furniture Manufacturers Association 1881 | Confirmed | Culture Trip, American Heritage, Norma Lewis book | Kept |
| Steelcase founded 1912 as Metal Office Furniture Co., HQ Grand Rapids; Herman Miller Zeeland, Haworth Holland | Confirmed (PK) | Wikipedia, CFN | Kept |
| More than $1.2 billion invested on the Medical Mile | Removed | Only Wikipedia; searches found no current total | Replaced with "hospital, research and medical school buildings now line the corridor" |
| Butterworth 1875 as St. Mark's Home and Hospital, now Corewell Health Butterworth | Confirmed (PK, writer's source) | Wikipedia | Kept |
| Van Andel Institute founded 1996, opened 2000 on Michigan Street | Confirmed (PK) | Wikipedia | Kept |
| Secchia Center opened 2010 as MSU CHM headquarters, with hospital and VAI backing | Confirmed | humanmedicine.msu.edu | Kept |
| Corridor districts "under a 2005 Michigan law" | Softened | PK: PA 280 of 2005 was later recodified into the 2018 Recodified Tax Increment Financing Act | Now "a Michigan law first passed in 2005" |
| Uptown first CID; East Fulton, Wealthy, East Hills, Eastown; West Side district | Confirmed (writer's sources, Rapid Growth) | rapidgrowthmedia.com | Kept |
| Michigan SBDC HQ at GVSU Seidman; West Michigan region at Seidman Center, 13 counties incl. Kent and Ottawa | Confirmed | michigansbdc.org, gvsu.edu | Kept |
| Grand Rapids Chamber about 3,000 members | Confirmed | grandrapids.org ("over 3,000", "nearly 3,000") | Kept, "Roughly" changed to "About" |
| Start Garden 5x5 Night is monthly, $5,000 | Softened | No current monthly Grand Rapids schedule found; 2026 5x5 events still offer $5,000 | "Monthly" dropped: "known for its 5x5 Night pitch events ... compete for a $5,000 prize" |
| SBA 2024 Michigan: 945,788, 99.6%, 47.4% | Confirmed (writer's source, official PDF) | advocacy.sba.gov | Kept, not re-searched |
| Pricing, trials | Confirmed vs INTAKE.md | INTAKE.md | Added $297 after-trial wording to FAQ 3 |

Summary: checked 13, confirmed 9, corrected 1 (pricing FAQ), softened 2, removed 1. Search 6 / PK 4.

## /web-design/pittsburgh-pa.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| 90 official neighborhoods; Neighborhood Planning 1969 under Flaherty; Squirrel Hill and Lawrenceville splits | Confirmed (PK, writer's sources WESA) | WESA | Kept |
| Population 307,632 (July 1, 2025) | Confirmed | citypopulation.de; PA State Data Center | Kept |
| City of Bridges, three rivers; 446 bridges (2006, disputed) | Confirmed (PK) | Heinz History Center, Wikipedia | Kept |
| PennDOT tunnels, 229,000+ drivers a day (2017) | Confirmed (writer's source, dated and attributed) | WESA 2017 | Kept |
| Robotics Row in the Strip and Lower Lawrenceville | Confirmed (PK) | The Incline, GeekWire | Kept |
| NREC "more than 25 years" of robotics work | Corrected | Wikipedia/CMU: in Lawrenceville and renamed NREC in 1996 (roots in 1994) | Now "has been in Lawrenceville since 1996" |
| Butler St, Liberty Ave Bloomfield (Little Italy), East Carson St, Forbes and Murray | Confirmed (PK) | Writer's travel sources | Kept |
| UPMC largest regional employer, largest nongovernmental in PA | Confirmed (writer's source) | WPXI / Pittsburgh Business Times | Attribution clarified ("as reported by WPXI") |
| "Some Pittsburgh firms quote a few hundred dollars" (FAQ 1) | Softened | No local source | Now "Some designers" |
| Duquesne SBDC no-cost, confidential; outreach in Beaver, Butler, Lawrence | Confirmed | sbdc.duq.edu | Kept |
| Pitt SBDC "working with entrepreneurs across Western Pennsylvania" (weak directory source) | Corrected | cec.pitt.edu / entrepreneur.pitt.edu: no-cost, confidential; Allegheny, Beaver, Greene, Indiana, Washington counties | Rewritten; Venturize source replaced with cec.pitt.edu |
| URA with Invest PGH: $5,000 to $500,000, fixed below-market, 5 to 20 years | Confirmed | ura.org access-to-capital | Kept |
| Greater Pittsburgh Chamber, Allegheny Conference affiliate, two dozen chambers | Confirmed (writer's source, Chamber PDF 2026) | Chamber | Kept |
| SBA 2024 PA: 1.1M, 99.6%, 45.4% | Confirmed (writer's source, official PDF) | advocacy.sba.gov | Kept |
| Pricing, trials ("ten city or neighborhood pages") | Confirmed vs INTAKE.md (neighborhood reading OK, a place per page) | INTAKE.md | Added $297 after-trial wording to FAQ 1 |

Summary: checked 15, confirmed 10, corrected 3, softened 1 (plus 1 attribution clarified), removed 0. Search 5 / PK 6.

## Not settled
- Des Moines: the Partnership's 2026 flyer (writer's source) may say "more than 80". The page now uses the
  Partnership web page's "nearly 80", which is the safer figure.
- Madison: the 1984 Willy Street fast food story may well be true (the APA Great Places page is the writer's
  source), but it could not be confirmed in a search, so the page now makes only the general claim.
