# Fact-check fc-w4-a4 (Wave 4, Oct 17 2026)

Independent checker; I wrote none of these pages. Pages: the-woodlands-tx, beaumont-tx, round-rock-tx,
nacogdoches-tx, texarkana-tx. Writer notes: docs/writers/w4-a7.md, docs/writers/w4-a8.md.

**Method note, stated honestly.** I ran 19 WebSearch queries (the SBDC question, every Nacogdoches claim, and
the Texarkana medical, depot and university claims). Then the shared per-turn WebSearch budget (200 calls across
all agents) ran out, and WebFetch cannot resolve hosts here. For the claims I could not search, I used two rules.
"Confirmed (knowledge)" means a well-documented fact I know independently: dates of famous events, known landmarks,
the 2020 census counts. For a specific figure or program detail I could neither search nor confirm from
knowledge, I softened or removed it instead of trusting the writer's source. Those claims are marked "not
re-verified". A later checker with search budget could restore some of them (list at the end).

Build: `python3 build.py --out /tmp/claude-0/fc-w4-a4/dist`; check.py --only on each page: 0 errors (word-count
warnings only, on The Woodlands and Round Rock). Similarity after edits: the highest pair involving my pages is
below the site maximum of 5.3% (abilene/new-orleans). The highest pair for any of my pages is under 4%. No
dashes, FAQ counts unchanged (4, 4, 3, 5, 5), `m.no_office` once on each page. Alt text: I opened all 5 heroes
and 15 in-body images, and every alt describes what the photo shows. None claims to show the city.

## Open question: which SBDC serves Nacogdoches County?
**Both do.** The UH Texas Gulf Coast SBDC network lists Angelina College SBDC (Lufkin) with a six-county area:
Angelina, Polk, Houston, Tyler, Nacogdoches and Trinity (app.sbdc.uh.edu/app/Angelina_College_SBDC.asp). The
North Texas SBDC network's county search, the TJC catalogs (2021-22, 2023-24) and atcog.org list the Tyler SBDC
at Tyler Junior College with Cherokee, Nacogdoches, Sabine, San Augustine, Shelby, Smith and Wood. So
east-texas.html is correct and was **not edited**. On nacogdoches-tx.html I kept Angelina College and added a
bullet saying the Tyler SBDC also lists the county, with the ntsbdc.org county search as the source.

## /web-design/nacogdoches-tx.html
| Claim | Verdict | Source | Action |
|---|---|---|---|
| Population about 32,000 (V2023 32,156) | Confirmed | census.gov QuickFacts | none |
| SFA fall 2025: 2,800 first-time undergrads, record, +31%; total +7%, first rise since fall 2018 | Confirmed | sfasu.edu release; KLTV | none |
| SFA is part of the UT System | Confirmed | sfasu.edu (joined 2023) | none |
| "Oldest town in Texas" claim, 1779 founding, 1716 mission, title disputed (Ysleta, Presidio) | Confirmed | Travel Texas; WorldAtlas; barrypopik | none |
| Red brick streets laid "in the early 1920s" | Softened | Travel Texas ("laid in the 1920s"); KLTV March 2026 (TxDOT found 1920s brick) | now "laid in the 1920s" |
| Texas Main Street Program since 1998; Main Street is a city department | Confirmed | THC Dec 2014 newsletter; visitnacogdoches.org | none |
| Facade grant listed among incentives | Not re-verified (low stakes, attributed to state listing) | downtowntx.org | kept as attributed |
| Blueberry Festival second Saturday in June; 36th on June 13 2026; about 20,000; free | Confirmed | Texas Co-op Power; tbf.nacogdoches.org | none |
| 5K and 10K run | Confirmed | tbf.nacogdoches.org race page | source added |
| Music stages, car show | Confirmed | festival listings | none |
| Chamber produces festival; proceeds fund chamber community and business programs | Confirmed | Texas Co-op Power; KETK | none |
| HR 156 (80th Leg.): lumber, ranching, poultry | Confirmed | capitol.texas.gov | none |
| Pilgrim's 2020: 1,500+ employees, 280 growers, $36M+ a year | Confirmed | jbssa.com 2020 release | none |
| Angelina College SBDC, no-cost advising, Nacogdoches County in its area | Confirmed | app.sbdc.uh.edu | none |
| SBDC helped a downtown cafe that opened Aug 2025 | Confirmed | sbdc.uh.edu case study (opened Aug 23 2025) | none |
| Tyler SBDC also serves Nacogdoches County | Added (Confirmed) | ntsbdc.org; TJC catalogs | bullet and source added |
| Big Sandy about 73 miles straight-line | Softened | weak source (thecitiesnow.com); my own coordinate calculation gives about 73 mi | now "roughly 70 miles"; weak source removed |
| Google local ranking: relevance, distance, prominence | Confirmed | support.google.com | none |
| Prices, AI receptionist, Starter contents | Confirmed | INTAKE.md | none |

Summary: 19 checked, 15 confirmed, 0 corrected, 2 softened, 0 removed (plus 1 added fact, 1 weak source removed, 1 low-stakes item not re-verified).

## /web-design/texarkana-tx.html
| Claim | Verdict | Source | Action |
|---|---|---|---|
| Texas side about 36,000 (2024 estimate 35,971) | Softened | 2020 census 36,193 (knowledge); V2024 not re-searched | "about 36,000 people in recent Census Bureau counts" |
| Post office and courthouse in both states on State Line Ave | Confirmed (knowledge) | GSA | Wikipedia source removed (GSA kept) |
| TexAmericas: medical hub of a large rural market | Confirmed (attributed quote) | TAC 2025 overview | none |
| CHRISTUS finalized Wadley purchase Nov 2024 from Steward bankruptcy, kept nearly all staff | Confirmed | KSLA; CHRISTUS; Becker's | none |
| 800,000 sq ft of retail at Richmond Rd and I-30 | Removed | undated trade article, not re-verified | figure cut; Richmond Road retail strip kept; source removed |
| RRAD: WWII, 20,000+ construction workers, 18,000 acres | Confirmed | army.mil (other Army pieces say 22,000; "more than 20,000" holds) | none |
| Major employers: CHRISTUS St. Michael, RRAD, Cooper Tire, TAMUT | Confirmed (attributed) | TAC overview; tamut.edu | none |
| TAMUT "about 3,000 students" fall 2025 | Removed | no source found with the figure | cut |
| TAMUT +40% fall 2023 to fall 2025; 7th record term spring 2026 | Confirmed | tamut.edu Jan 2026 | none |
| Fall 2026 +30% | Corrected | tamut.edu Aug 27 2026 says ninth straight record term | added "ninth straight record" |
| NE Texas SBDC: six named counties, hosted by NTCC and Texarkana College, 220 Texas Blvd | Softened | atcog.org (not re-verified after budget ran out) | now: Bowie County in its service area, Texarkana office, free |
| Chamber Nov 2024 tuition partnership with TAMUT | Removed | not re-verified | cut along with its source |
| Not selling online stores; no patient portals | Consistent | INTAKE.md (no ecommerce listed) | none |
| Prices, hosting, AI receptionist | Confirmed | INTAKE.md | none |

Summary: 14 checked, 8 confirmed, 1 corrected, 2 softened, 3 removed.

## /web-design/beaumont-tx.html
| Claim | Verdict | Source | Action |
|---|---|---|---|
| Lucas gusher Jan 10 1901, 150+ ft, nine days to cap | Confirmed (knowledge) | Lamar Spindletop museum | none |
| Beaumont about 9,000 to about 30,000 by March 1901 | Confirmed (knowledge, matches TSHA account) | Beaumont CVB | none |
| Gulf Oil and Texaco trace to Spindletop | Confirmed (knowledge) | as above | none |
| Golden Triangle = Beaumont, Port Arthur, Orange | Confirmed (knowledge) | Texas Monthly | none |
| ExxonMobil $2B expansion 2023, +250,000 b/d, 630,000+, among largest US refineries | Confirmed (knowledge) | ExxonMobil release Mar 2023 | none |
| 112,200 residents (2023 estimate) | Softened | not re-searched; 2020 census 115,282 | "a little over 110,000 residents in recent Census Bureau counts" |
| Turnaround definition, every 3 to 5 years, staggered | Confirmed (knowledge) | Hydrocarbon Engineering | none |
| Dowlen Road, Parkdale Mall, Calder Ave, Eastex Freeway as landmarks | Confirmed (knowledge) | real place names | Crexi listing source removed (weak) |
| Cajun food everywhere in the region | Confirmed (attributed) | Texas Highways | none |
| Texas Almanac: up to 375,000 Cajuns in Texas | Removed | not re-verified | cut |
| Choates family came "during the oil boom"; "Jolie Blonde" 1946 | Corrected | knowledge: his 1946 recording is titled "Jole Blon" | now "fiddler Harry Choates's among them; he recorded his famous 'Jole Blon' in 1946", oil-boom timing dropped |
| Lamar enrollment topped 18,000 (Nov 2025) | Softened | not re-verified | "brings thousands of students to Beaumont"; source removed |
| Lamar SBDC no-cost confidential advising | Confirmed (knowledge) | app.sbdc.uh.edu | Rolfe Christopher Dr address and "surrounding counties" scope removed |
| Chamber mentoring; Beaumont Business Academy with Lamar SBDC | Softened | not re-verified | generic chamber line; event source removed |
| Package details (Pro chat 14 days then $297; Agency agent 7 days then $297/750 min) | Confirmed | INTAKE.md | none |
| Auto shop "fifteen years" customer | OK, labeled hypothetical ("Picture") | n/a | none |

Summary: 16 checked, 10 confirmed, 1 corrected, 3 softened, 1 removed (plus 1 weak source removed, 1 hypothetical OK).

## /web-design/round-rock-tx.html
| Claim | Verdict | Source | Action |
|---|---|---|---|
| Dell HQ opened Aug 2 1994; agreement 1993, extended 2024 | Softened | knowledge confirms 1994 and a city agreement; exact date and 2024 extension not re-verified | "in 1994, under an economic development agreement with the city" |
| One Dell Way | Confirmed | Dell 10-K | none |
| 130,406 residents (2023 estimate) | Corrected/Softened | 2020 census 119,468 (knowledge) | now 2020 count; H2 "a city of about 130,000" changed to "a fast-growing city"; source label and URL updated |
| BSW Medical Center Round Rock, 300 University Blvd | Confirmed (knowledge) | AMA FREIDA; Tradeline | none |
| Texas State, ACC Round Rock campuses with health programs; Texas A&M medicine campus | Confirmed (knowledge) | Community Impact; medicine.tamu.edu | none |
| Sports Capital of Texas: 2004 campaign, trademark registered 2018 | Softened | barrypopik; Justia (not re-verified) | "later registered the phrase as a federal trademark" (year dropped; 2004 kept with its source) |
| Old Settlers Park about 645 acres next to Dell Diamond | Confirmed (knowledge) | texaslodging.com | none |
| Multipurpose Complex $27M, 60 acres, opened 2017 | Confirmed (knowledge for 2017 opening) | city release; Parkhill | none |
| Express = Rangers Triple-A | Confirmed (knowledge) | MiLB | none |
| Affiliation deal through 2030 | Removed | not re-verified | cut, and its source |
| Commercial Historic District, NRHP 1983, 100-200 blocks E. Main | Confirmed (knowledge) | City of Round Rock | none |
| Chamber small business guide with plan template | Removed | not re-verified | generic chamber mention; source removed |
| Texas State SBDC "Round Rock office" | Corrected | earlier checker (fc-w2/fc-w3 Austin suburbs): office in Austin, Williamson in its 12 counties | now "from its Austin office" |
| FAQ: tourism staff say sports nearly every weekend | Confirmed (attributed) | texaslodging.com quote of the CVB director | none |
| Prices, hosting | Confirmed | INTAKE.md | none |

Summary: 15 checked, 9 confirmed, 2 corrected, 2 softened, 2 removed.

## /web-design/the-woodlands-tx.html
| Claim | Verdict | Source | Action |
|---|---|---|---|
| 114,436 residents, 2020 census | Confirmed (knowledge) | Census | Wikipedia source replaced with Census QuickFacts URL |
| Township is a special purpose district, 2007 legislation, 7-member board, Montgomery and Harris voters | Confirmed (knowledge) | thewoodlands.com; Township | none |
| Incorporation rejected Nov 2021, about two thirds no | Confirmed (knowledge) | Community Impact; Township | none |
| Village association list; Creekside Park the only village in Harris County | Confirmed (knowledge) | Township; Community Impact | none |
| Address lookup "because even residents are not always sure" | Softened | Township page | now states only that the lookup exists |
| ExxonMobil 2022 HQ move Irving to Spring campus, up to 10,000 | Confirmed (knowledge) | Valve Magazine | none |
| HPE HQ at CityPlace, Spring, 2022, 2,200+ employees | Confirmed (knowledge for 2022 opening; headcount attributed to Business Wire) | Business Wire; Community Impact | none |
| Relocators often weigh The Woodlands | Removed | weak source (relocation blog) | claim and source cut |
| Waterway links Market Street, Waterway Square, Hughes Landing, Mall | Confirmed (knowledge) | Township Town Center | none |
| Chamber founded 1978, renamed 2012, 1,300+ employers | Softened | not re-verified | kept only the former name |
| Lone Star College SBDC, free consulting, covers The Woodlands | Confirmed (knowledge) | Community Impact | none |
| Prices, hosting | Confirmed | INTAKE.md | none |

Summary: 12 checked, 9 confirmed, 0 corrected, 2 softened, 1 removed (plus 1 weak source replaced).

## Could restore with a later search (removed or softened only because of the search limit)
Round Rock 2023 estimate and the Express deal end year; the Sports Capital trademark year; Lamar enrollment;
the Texas Almanac Cajun figure; the Beaumont Business Academy; The Woodlands chamber dates and member count;
TAMUT fall 2025 headcount; the NE Texas SBDC host colleges and street address; the Texarkana Chamber and TAMUT
tuition partnership; the Texarkana retail square footage.
