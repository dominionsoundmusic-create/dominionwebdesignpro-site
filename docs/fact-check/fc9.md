# Fact-check fc9: Austin-area city pages (Oct 12 2026)

Independent checker (did not write these pages). Pages: /web-design/leander-tx.html, pflugerville-tx.html, kyle-tx.html, san-marcos-tx.html, dripping-springs-tx.html, new-braunfels-tx.html (sources in src/pages/web-design/). 22 WebSearch queries; WebFetch blocked, so claims were verified from search-result summaries of the official or credible source. Business claims checked against INTAKE.md on every page: prices $497 / $997 / $1,997 one time, hosting $49/mo or included with the AI agent, AI receptionist wording, `m.no_office()` used once per page, "built remotely from Big Sandy", no clients, reviews, rankings or office implied. All matched.

Build: `python3 build.py --out /tmp/claude-0/fc9/dist` then `scripts/check.py --skip-links --only <url>`: 0 errors on all six pages after fixes (one banned-word hit, "Certified", introduced by my own edit and fixed). No em or en dashes in the six sources.

## Leander
| Claim | Verdict | Source | Action |
|---|---|---|---|
| Census 2010 26,521; 2020 59,202 | Confirmed | census.gov QuickFacts leandercitytexas | none |
| Appears on fastest-growing city lists | Confirmed | en.wikipedia.org/wiki/Leander,_Texas (fastest-growing US city 2018 to 2019) | none |
| 183A north extension opened 2012, RM 1431 to north of FM 2243 | Confirmed (writer source) | communityimpact.com 2012 article | none |
| Hero Way meets 183A; Ronald Reagan Blvd | Confirmed | communityimpact.com Hero Way improvements; KXAN 183A | none |
| Leander is northern end of MetroRail Red Line, "brings commuters through town every weekday" | Corrected | en.wikipedia.org/wiki/Leander_station; leandertx.gov | Reworded to the terminus fact (station off US 183 north of FM 2243); dropped the weekday-schedule claim; added source |
| Northline, about 17 acres along 183A, first official downtown development | Confirmed (writer source) | hoodline.com 2024 | none |
| ACC San Gabriel campus and St. David's drew growth north | Confirmed | communityimpact.com ACC/St. David's; sites.austincc.edu | none |
| Chamber office on North West Drive | Corrected | communityimpact.com Jan 29 2026 (moved Jan 7 2026 from Brushy St to 103 N West Dr) | Added "moved in January 2026" and the source |
| Texas State SBDC "office in nearby Round Rock" | Corrected | sbdc.mccoy.txst.edu (office at 505 E Huntland Dr, Austin; serves 12 counties incl. Williamson, Travis; no Round Rock office listed) | Now "serves Williamson and Travis counties"; source added |
| SCORE Austin free mentoring | Confirmed | score.org/austin | source added to block |

## Pflugerville
| Claim | Verdict | Source | Action |
|---|---|---|---|
| 2025 S.C.R. 4: Trail Capital of Texas, 10 years ending 2035 | Confirmed | capitol.texas.gov SC00004F (enrolled); legiscan (signed May 24 2025); FOX 7 | Source switched from committee version (S) to enrolled text (F) |
| Most trail per capita, 1.49 mi per 2,000 residents | Softened | SC00004F recitals | Now says the resolution cites a city staff analysis |
| Gilleland Creek trails | Confirmed | traillink.com (about 6.5 mi, longest in the city) | Named and sized; source added |
| Lake Pflugerville draws trail users | Confirmed (general) | TrailLink lists it in the city network | none |
| "Population above 65,000" per Governor's release | Corrected | Census 2020 count about 65,191 (QuickFacts / Wikipedia); 2023 estimate 65,301 | Now "the 2020 census counted about 65,000"; QuickFacts source added |
| Chamber "led by CEO Kristen Cepak" | Removed | communityimpact.com Jan 12 2026: Cepak left Jan 7 2026 | Name removed |
| Chamber "part of the city's push" for Tourism Friendly Texas | Softened | gov.texas.gov Apr 9 2025 release | Now states only that the city received the designation in 2025 |
| Community Impact founded 2005 by John and Jennifer Garrett, first edition Round Rock/Pflugerville, Garretts' house; HQ in Pflugerville; offices Houston, Dallas, San Antonio | Confirmed | Wikipedia; communityimpact.com/about | none |
| "Six people" at founding | Softened | Wikipedia says six, company About page says three | Now "a small team" |
| 2012 HQ deal, 130 Commerce Center, Pflugerville CDC | Confirmed (writer source) | communityimpact.com | none |
| Stone Hill Town Center at SH 130 and SH 45 | Confirmed | pfdevelopment.com listing (SWC SH 130 & SH 45) | none |
| SBDC "Round Rock and Austin offices" | Corrected | sbdc.mccoy.txst.edu contact (Austin office; Travis and Williamson served) | Reworded; source added |
| Live-and-work-in-town aim | Confirmed as general statement (no figure) | n/a | none |

## Kyle
| Claim | Verdict | Source | Action |
|---|---|---|---|
| Census 2010 28,016; 2020 45,697; July 2023 est. 62,548 | Confirmed | census.gov QuickFacts kylecitytexas | none |
| Dec 2022 ran out of Edwards Aquifer allotment, bought from San Marcos | Confirmed | KUT / TPR May 9 2024 | none |
| 2024 deal up to 500 acre-feet a year through 2026 | Confirmed | FOX 7; University Star | none |
| Lowe's 120,000 sq ft, Kyle Crossing Business Park, one block west of I-35 in Plum Creek | Confirmed | cityofkyle.com/node/12071; Community Impact | none |
| Planned 138-acre Uptown District (retail, office, hotel, convention) | Confirmed as planned | nmrk.com press release | none (page already says "planned") |
| Waterfront at Marketplace | Confirmed (writer source) | communityimpact.com | none |
| Kyle chamber mission | Confirmed | uschamber.com; Hays Free Press | none |
| Chamber members get "no-cost one-on-one counseling, referrals" | Removed | only a circa 2011 Hays Free Press article | Replaced with networking events and member directory |
| GBP tip "turn on messages" | Corrected | Google ended Business Profile chat in July 2024 (known product change) | Bullet replaced with keeping phone and website link current |
| Map results "usually" above web results | Softened | n/a | "often" |
| City of Kyle Small Business Resource Summit | Confirmed (writer source, no date stated) | cityofkyle.com | none |

## San Marcos
| Claim | Verdict | Source | Action |
|---|---|---|---|
| Record fall 2025 enrollment 44,630 | Corrected | news.txst.edu: official count 44,596 (44,630 appears only in a Jan 2026 speech report) | Changed to 44,596; source swapped to the university release |
| I-35 "halfway" between Austin and San Antonio | Softened | geography (about 30 mi from Austin, 50 from San Antonio) | "between" |
| SBDC "hosted right here" in San Marcos | Corrected | sbdc.mccoy.txst.edu (hosted by Texas State, office in Austin, serves 12 counties incl. Hays) | Body and FAQ reworded |
| Texas South-West SBDC Network, SBA cooperative agreement | Confirmed | sbdc.mccoy.txst.edu/about-us; UTSA | none |
| Greater San Marcos Partnership: regional EDO for San Marcos, Hays and Caldwell | Confirmed (writer source) | hillviews.txst.edu | none |
| LBJ Dr, Hopkins St, Aquarena Springs Dr, Wonder World Dr, Craddock Ave, courthouse square, outlets, spring-fed river | Confirmed (well-known local geography) | n/a | none |

## Dripping Springs
| Claim | Verdict | Source | Action |
|---|---|---|---|
| HCR 43 (84th Leg.) Wedding Capital of Texas, signed May 18 2015 | Confirmed | capitol.texas.gov HC00043F; Texas Tribune | none |
| Recitals: more than 1,000 weddings a year, more than 30 venues | Confirmed (as the resolution's own recitals; page attributes them) | capitol.texas.gov HC00043 | none |
| Mercer Street Historic District on National Register; US 290 formerly ran on Mercer | Confirmed (writer sources) | npgallery.nps.gov; drippingspringstx.gov | none |
| Dripping Springs Chamber holds ribbon cuttings | Confirmed (writer source) | haysfreepress.com | none |
| SBDC "in nearby San Marcos" | Corrected | sbdc.mccoy.txst.edu (serves Hays County; office in Austin) | Reworded; source added |

## New Braunfels
| Claim | Verdict | Source | Action |
|---|---|---|---|
| Census 2020 90,403; July 2023 est. 110,958 | Confirmed | census.gov QuickFacts | none |
| Growth since 2010 about 92% vs 24% MSA ("more than three times") | Confirmed | newbraunfels.gov FY 2024 PAFR | none |
| Comal meets Guadalupe; Gruene inside city limits; Gruene Hall oldest continuously operating dance hall (stated as "often described") | Confirmed | Wikipedia | none |
| Wurstfest draws visitors | Confirmed | communityimpact.com 2024 (63rd year) | Source added |
| Creekside along I-35 | Confirmed | Creekside Crossing at I-35 and FM 306 (store listings) | none |
| Main Plaza, SH 46, Canyon Lake, Seguin, Schertz, Garden Ridge | Confirmed (general geography) | n/a | none |
| "Texas plumbers are licensed by the state" | Confirmed and sharpened | 22 TAC 367.10 (ads must state the RMP license number) | Added the ad rule and source |
| NBEDC partners incl. chamber, city, county, GNBEDF, NBU | Confirmed (writer source) | 2021 benchmark book | none |
| 2019 Senate resolution credits chamber with creating and supporting SBDC | Confirmed (writer source) | capitol.texas.gov SR 490 | none |
| Small Business Person of the Year criteria | Confirmed (writer source) | communityimpact.com 2024 | none |
| "Texas State University SBDC network serves the region" | Corrected | Comal County is not among Texas State SBDC's 12 counties; New Braunfels is served by the UTSA SBDC through the city's Spark Small Business Center (utsa.edu 2022) | Replaced with Spark / UTSA SBDC sentence; source added |

## Summary
Checked 63 | Confirmed 43 | Corrected 11 | Softened 6 | Removed 3.
Most important fixes: named Pflugerville chamber CEO who left in January 2026 (removed); SBDC office locations wrong on five pages (Texas State SBDC is in Austin, no Round Rock or San Marcos office; New Braunfels is served by UTSA SBDC via Spark); Texas State enrollment corrected to the official 44,596; Pflugerville population restated as the 2020 census count; Google Business Profile "messages" tip removed (feature discontinued); Kyle chamber benefits trimmed to what is verifiable.
