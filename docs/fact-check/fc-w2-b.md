# Fact-check fc-w2-b: Phoenix, Las Vegas, Sacramento (Wave 2 batch B, Oct 16 2026)

Checker: fc-w2-b (independent, did not write the pages). Writer notes: docs/writers/w2-b.md.
About 35 WebSearch queries (WebFetch blocked: census.gov DNS failure). Build: `python3 build.py --out /tmp/claude-0/fc-w2b/dist`;
check.py --skip-links --only on each page: 0 errors, 0 warnings. No em/en dashes; "certified" appears only inside a DGS source URL.

## /web-design/phoenix-az.html
| Claim | Verdict | Source | Action |
|---|---|---|---|
| Google: service-area business should hide its address, list up to 20 service areas, one profile for the territory | Confirmed | support.google.com/business/answer/9157481, /3038177, /2853879 | none |
| NWS confirmed 2024 hottest year on record, average 78.6 degrees | Confirmed | weather.gov/psr/YearInReview2024; KJZZ 2025-01-01; KTAR recap | added NWS year in review source |
| 70 days at 110+ in 2024 vs a typical 21 | Confirmed | KJZZ 2025-01-01; KTAR; Gigafact | none |
| Sept 25, 2024 hit 113, "the latest 110 degree day in the city's recorded history" | Corrected | azfamily (true on that day) superseded: KTAR and ASU Arizona Climate Summary Oct 2024: Oct 1, 2024 hit 113, first 110+ day ever in October; last 110 day Oct 7 | now "On October 1, 2024 it hit 113, the first 110 degree day in October in the city's recorded history"; azfamily source replaced with KTAR October article |
| Phoenix land area about 518 sq mi | Confirmed | Wikipedia infobox 518.26 land | none |
| Census July 1, 2024: Phoenix 1,673,164; Mesa 517,151; Gilbert 288,790; Chandler 281,231; Glendale 258,143; Scottsdale 246,170 | Confirmed | Census QuickFacts V2024 (search results); abc15 | source URL replaced: old one was a QuickFacts chart for Bullhead City, Sun City and Mesa; now a QuickFacts table for the six cities named |
| Peoria 199,924 (July 2024) | Removed | not found anywhere; QuickFacts showed 2023 198,750; AZ OEO 203,065 | number deleted (Peoria still mentioned as a place) |
| Phoenix has 15 urban villages incl. Maryvale, Alhambra, Central City, South Mountain, North Gateway | Confirmed | phoenix.gov PhxCAN and village data; pdd_pz_pdf_00154 (North Gateway) | none |
| "residents use those names when they describe where they live" | Softened | no source; Central City / North Gateway are planning names | now "some of those names, Maryvale among them, are how residents describe where they live" |
| ROC: license needed when project (labor and materials) is $1,000 or more or needs a permit; "handyman" label does not change it | Confirmed | roc.az.gov/news/contracting-arizona-heres-what-you-need-know; A.R.S. 32-1121 | none |
| ROC search by "six-digit number"; "only a current, active license may legally contract" | Softened | official page layout not confirmed (only third-party descriptions) | now "looks up a license by its number or by name and shows whether that license is currently active" |
| Maricopa SBDC led by Maricopa Community Colleges, no-cost advising, mostly free workshops | Confirmed | maricopa.edu SBDC page; Phoenix Chamber listing (nominal fees for some trainings) | none |
| Greater Phoenix Chamber "runs" BRE visits with ACA, City, County, referring to SBDC | Softened | phoenixchamber.com BRE page describes Phoenix Forward in past tense; latest material 2019 | now "Through its Phoenix Forward effort, the Chamber has made ... visits"; BRE page added as source |
| City of Phoenix Small Business Support Division runs SBE certification for city contracts | Confirmed | phoenix.gov EOD business-relations and small-business-certifications | none |
| Neighborhood Services lists free management and technical assistance | Confirmed | phoenix.gov NSD economic development programs | none |
| SCORE "free mentoring and workshops" | Corrected | score.org/az/greater-phoenix: mentoring free; most webinars now carry a small registration fee | now "free mentoring ... plus workshops and webinars, some free and some with a small registration fee"; source changed from score.org/arizona to score.org/az/greater-phoenix/ |
| Dominion: prices $497/$997/$1,997; Starter contents, live in 7 to 14 days; Pro 10 pages, 10 city pages, GBP, schema, reviews, chat widget free 14 days then $297/mo; Agency research, 30 to 60 pages in waves, first live inside two weeks, phone agent setup, free 7 days then $297/mo up to 750 min, cancel any time, separate from one-time price; hosting $49/mo without agent | Confirmed | INTAKE.md section 3 | none |
| One person, Maurice Johnson, Big Sandy, remote; m.no_office('Phoenix'); not a Phoenix firm | Confirmed | INTAKE.md sections 1, 5 | none |

Summary: 18 claims checked: 12 confirmed, 2 corrected, 3 softened, 1 removed. Sources: 2 replaced, 3 added.

## /web-design/las-vegas-nv.html
| Claim | Verdict | Source | Action |
|---|---|---|---|
| Most of the Strip is in unincorporated Paradise and Winchester, Clark County | Confirmed | Wikipedia Paradise, Winchester, Las Vegas Strip; Las Vegas Advisor | none |
| Paradise created as a town in 1950 after casino operators sought town status to head off annexation | Confirmed | Wikipedia Paradise (Dec 8, 1950; Gus Greenbaum and casino executives vs Mayor Cragin) | none |
| Clark County 2024: Las Vegas about 681,000, Henderson about 355,000, county about 2.42 million | Confirmed | files.clarkcountynv.gov Final_2024_Place_Population.pdf (681,397; 354,961; 2,421,685) | none (Census V2024 county figure is lower, 2,398,871; page cites the county's own file) |
| Spring Valley and Enterprise unincorporated towns, each passed 215,000 in 2020 census | Confirmed | Census QuickFacts Spring Valley CDP 215,597; Wikipedia Enterprise 221,831 | none |
| Summerlin partly in city limits, partly unincorporated county | Confirmed | Las Vegas Advisor; multiple local sources (Charleston Blvd line) | none |
| North Las Vegas is its own city | Confirmed | Clark County licensing FAQ (six jurisdictions) | none |
| Google local results weigh relevance, distance, prominence; relevance = match to search | Confirmed | support.google.com/business/answer/7091 | none |
| "Every Nevada business needs a State Business License" via SilverFlume | Corrected | NV SOS notice; NRS 76.020(2) exemptions require an exemption filing | now "Most Nevada businesses need ... and the few that qualify for an exemption still have to file for it" |
| Clark County: six jurisdictions each with own licensing agency; much of valley has Las Vegas mailing address but is unincorporated; jurisdiction locator; some need more than one license | Confirmed | clarkcountynv.gov general license guide and FAQ; 10-step guide | none |
| SBA Advocacy 2024 Nevada: 333,471 small businesses, 99.3%, 45.3% of employees | Confirmed | advocacy.sba.gov/wp-content/uploads/2024/11/Nevada.pdf | none |
| Vegas Chamber: former Las Vegas Metro Chamber, roots 1911, 2012 merger with North Las Vegas chamber | Confirmed | vegaschamber.com rebrand post; UNLV Special Collections node/1706; VegasInc 2012 | none |
| Vegas Chamber "more than 3,500 members" | Removed | no source found (older figures say 4,000 in 2018, "over 6,000" in UNLV archive) | member count deleted |
| "most of them small businesses" | Corrected (made specific and sourced) | Vegas Chamber CEO testimony, U.S. Senate Commerce subcommittee, Aug 2023: 85% of members are small businesses (50 or fewer employees) | sentence rewritten with the 85% figure; Senate testimony added as source |
| Nevada SBDC statewide program of UNR, offices incl. UNLV, no-cost confidential advising | Confirmed | unlv.edu/sbdc; nevadasbdc.org; unr.edu | none |
| SCORE Las Vegas free mentoring in person, email or video; low or no-cost workshops | Confirmed | score.org/lasvegas/about (in-person availability may be limited) | none |
| Odd-hour customers framed as "if your customers include" shift workers | Not a factual claim | n/a | none |
| Dominion prices, Pro chat widget 14 days then $297/mo, Agency phone agent 7 days then $297/mo up to 750 min, not part of one-time price; hosting $49/mo; 30 to 60 pages; 7 to 14 days | Confirmed | INTAKE.md section 3 | none |
| No Nevada office; built from Big Sandy; not a Las Vegas agency | Confirmed | INTAKE.md | none |

Summary: 17 claims checked: 14 confirmed, 2 corrected, 0 softened, 1 removed (plus 1 non-claim). One source added.

## /web-design/sacramento-ca.html
| Claim | Verdict | Source | Action |
|---|---|---|---|
| City says it has the highest concentration of government jobs per capita in California | Confirmed (as the city's own statement, attributed) | cityofsacramento.org/Living-Here/Jobs; careersingovernment.com | none |
| Almost 90,000 state government jobs in the county (2017 data) | Confirmed, dated | Centers of Excellence 2019 public sector study (ca-ilg.org PDF): Sacramento County almost 90,000 state jobs; region 119,500, over a quarter of CA state jobs | text now states "A 2019 regional workforce study, using 2017 data" and adds the quarter-of-state context; source label corrected |
| Leading departments: Health Care Services, Corrections and Rehabilitation, Transportation, General Services | Removed | not found in any result | deleted |
| DGS SB eligibility: independent, not dominant, CA principal office, owners/officers domiciled in CA, 100 or fewer employees, avg gross receipts $19M or less over 3 years | Confirmed | DGS apply page; DGS 2026 brochure HTDB_Brochure_Web_03-2026.pdf | none |
| Microbusiness at $6M or less, automatic designation | Confirmed | DGS apply page | none |
| DGS adjusts limits every two years | Confirmed | Gov. Code 14837(d)(3) biennial review; DGS SB GARs FAQ | none |
| Each department annual goal at least 25% SB, at least 3% DVBE | Confirmed | DGS SCM TOC 12/12; SCM Vol 1 | none |
| 5% bid preference for SBs against non-SBs | Confirmed | DGS SCM 8.21 to 8.22; DGS assist SB/DVBE PDF | none |
| Applications and public search in Cal eProcure | Confirmed | DGS search page | none |
| Dominion does NOT hold California Small Business certification; cannot count toward a goal | Confirmed and clear | INTAKE.md section 7 (no certification claims); stated in FAQ and band | none |
| Farm-to-Fork Capital declared "October 2012" by Mayor Kevin Johnson | Softened | sources split between Oct 31 and Nov 2012 | now "In 2012" |
| Idea from Josh Nelson (Selland Family Restaurants) to Visit Sacramento; based partly on proximity to farmland; festival events from 2013 | Confirmed | Visit Sacramento; Comstock's; UOP thesis; ABC10 | none |
| Midtown east of downtown; East Sacramento east of Midtown with McKinley Park; Land Park around William Land Park; Oak Park between Midtown and Land Park | Confirmed | visitsacramento.com/plan/neighborhoods | none |
| R Street warehouse district along Sacramento Valley Railroad, Front Street to Folsom, 1856; now restaurants and galleries | Confirmed | City of Sacramento R Street Historic District; CA Historical Landmark 526 (completed Feb 22, 1856) | none |
| City offered up to $240,000 storefront grants to North Sacramento businesses on Del Paso Boulevard | Confirmed ("has offered" wording) | CBS Sacramento; Carmichael Times Jan 2025 (Storefront Retailer tier $100,000 to $240,000, Del Paso Blvd) | none |
| DOF Jan 1, 2024: Sacramento about 520,000; Elk Grove about 179,000; Folsom about 88,000; Rancho Cordova about 82,000 | Confirmed | saccounty.gov Demographics and Facts (520,407; 178,697; 88,023; 82,109) | none |
| Roseville in Placer County | Confirmed (common knowledge) | n/a | none |
| Google local results relevance, distance, prominence | Confirmed | support.google.com/business/answer/7091 | none |
| Sacramento Valley SBDC one-on-one consulting, satellite offices in eight counties | Confirmed | downtownsac.org business assistance; economic.saccounty.gov | added downtownsac source; "no-cost" added (City of Davis, county page) |
| Metro Chamber took over the region's SBDC management in 2014 | Removed | not confirmed: a 2017 Chamber update lists "Capital Region SBDC since Oct 1 2014"; a Comstock's piece says California Capital took over hosting the Sacramento Valley SBDC; which entity runs it is unclear | sentence deleted; Comstock's source removed |
| California Capital APEX Accelerator: part of federal APEX network, no-cost counseling, bid matching, training | Confirmed | sacrt.com resources page; business.defense.gov APEX PDF; DGS event page | SacRT source added |
| DGS Office of Small Business and DVBE Services handles certification and Cal eProcure search | Confirmed | DGS | none |
| Sacramento County Economic Development lists resources incl. SBDC and SCORE | Confirmed | economic.saccounty.gov business resources | none |
| Dominion prices and add-on terms; Starter contents; Pro contents; Agency setup, 7 days then $297/mo up to 750 min, not part of one-time price; hosting $49/mo | Confirmed | INTAKE.md section 3 | none |
| No Sacramento office; built remotely from East Texas | Confirmed | INTAKE.md | none |

Summary: 25 claims checked: 21 confirmed, 1 corrected (90,000 dated and context added), 1 softened, 2 removed (departments list, Metro Chamber 2014). One source label fixed, two sources added, one removed (Comstock's).

## Totals
60 claims checked: 47 confirmed, 5 corrected, 4 softened, 4 removed (Phoenix 1, Las Vegas 1, Sacramento 2).
