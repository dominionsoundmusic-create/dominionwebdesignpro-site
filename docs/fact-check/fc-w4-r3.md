# Fact-check fc-w4-r3 (Wave 4 search recheck, Oct 17 2026)

Independent checker; I wrote none of these pages. This is the search pass for claims that fc-w4-a3 and fc-w4-a4
left "not verified" or confirmed only from prior knowledge after the shared search budget ran out. Pages:
killeen-tx, sugar-land-tx, katy-tx, cypress-tx, beaumont-tx, round-rock-tx, the-woodlands-tx, texarkana-tx.

Method: 31 WebSearch calls (no more than 4 per page; Cypress used 2, Round Rock 3). WebFetch is blocked, so each
check rests on what the search results show from the official or credible source. A claim I could not confirm
was softened or removed rather than kept. I also checked every page's pricing and FAQ text against INTAKE.md. Six
pages had a FAQ saying hosting is "$49 a month, or included while you keep the AI agent" without saying what the
agent costs; all eight pages now state that the AI agent is $297 a month after its free trial. On Beaumont and
Texarkana the hosting line or the agent and widget terms were missing from the package paragraph, and I added them.

Build: `python3 build.py --out /tmp/claude-0/fc-w4-r3/dist`. `check.py --skip-links --only` on all 8 pages:
0 errors (1 word-count warning on Round Rock, which was there before). No em or en dashes. FAQ counts unchanged.
Similarity: area max 6.1% (st-petersburg/tallahassee, neither page is mine), so all are under 15%. Note: build.py
always rewrites docs/image-list.md. My pages add no planned images, so the content of that file does not change
because of me.

## /web-design/killeen-tx.html
| Claim | Verdict | Source | Action |
|---|---|---|---|
| Chamber added 88 members, total 468 | Confirmed (late 2024 article, president Scott Connell) | kdhnews.com chamber adds 88 members | Dated it "reported in late 2024" |
| 32 ribbon cuttings and groundbreakings in 2024 | Removed | not found in search | Cut, along with the "look back at 2024" source |
| KEDC three-person office funded by city | Confirmed / Corrected | KDH 2024: three employees including Connell; funded by a direct city contract ($885,000) | Now "had three employees in 2024 and is funded mainly through a contract with the city" |
| Harker Heights 57 single-family permits in 2025 | Removed | no source found; the cited KDH URL did not surface | Number and source cut; replaced with a general line that Harker Heights and Copperas Cove keep growing |
| Nolanville hired an economic development director | Confirmed, dated | nolanvilletx.gov article 137; KDH Sept 2022 (Brian O'Connor hired as NEDC director) | Added "in 2022" |
| 2023 estimate 159,643 | Softened (no search budget left for this page) | 2020 count 153,095 kept | Now "Census Bureau estimates show it has kept growing since" |
| TAMUCT "runs a site on the post" | Removed | not verified | Clause cut; founding 1999 as Tarleton branch kept |
| Pricing FAQ | Corrected | INTAKE.md | Added that the AI agents are $297/mo after the trial |

Summary: 8 checked, 2 confirmed, 2 corrected, 1 softened, 3 removed.

## /web-design/sugar-land-tx.html
| Claim | Verdict | Source | Action |
|---|---|---|---|
| Foreign-born 35.3% (2019 to 2023); Asian alone 39.5% | Confirmed | census.gov QuickFacts Sugar Land | none |
| Council approved Imperial purchase Feb 2025, closed June 2025, partner to follow | Confirmed (Feb 18 vote; June 18 2025 closing; partner targeted Q1 2026) | communityimpact.com; connectcre; sugarlandtx.gov | Replaced the Covering Katy source with Community Impact "officially acquires" |
| Fort Bend SBDC serves Fort Bend, Matagorda and Wharton counties | Corrected | sbdc.uh.edu Fort Bend page: no-cost confidential advising for Fort Bend and Southwest Harris County, 1116 Morton St, Richmond | Service area corrected |
| Plug and Play 2024 three-year agreement, SLDC funded, "free programs for startups" | Corrected | Community Impact: $4.5M three-year agreement approved Nov 2024, SLDC funded; two startup cohorts a year with mentorship and events | "free" dropped; now "startup cohorts with mentorship and events", dated Nov 2024 |
| GHP Dec 2025: region's most diverse county | Removed | not searched (budget); Texas Tribune and Kinder claims already carry the point | Clause and source cut |
| Telfair: prison land sold 2002, first homes 2006 | Softened | not searched | "built in the 2000s on former state prison land" |
| US 59 low-rise offices through the 1980s | Softened | not searched | "lined with office buildings and shopping centers" |
| Governor's Small Business Summit, May 2025 | Removed | not searched | Sentence and gov.texas.gov source cut; chamber address kept |
| Pricing FAQ | Corrected | INTAKE.md | Added the $297/mo agent cost |

Summary: 9 checked, 2 confirmed, 3 corrected, 2 softened, 2 removed.

## /web-design/katy-tx.html
| Claim | Verdict | Source | Action |
|---|---|---|---|
| Katy ISD 97,000+ students, 100+ campuses and facilities (2025-26) | Softened | No search result showed the cited district release. Community Impact: growth slower since 2024-25 (+524 projected for 2025-26), and a Nov 2025 demographic study projected a net decrease | Now "more than 90,000 students spread over dozens of campuses"; the katyisd.org source was removed |
| Enrollment gains smaller since 2024-25 | Confirmed and updated | Community Impact (Apr 2025; Nov 2025 study) | Added the late 2025 projected net decrease and its source |
| Cinco Ranch CDP, Fort Bend and Harris, 16,899 (2020) | Confirmed | census.gov QuickFacts; Wikipedia | none |
| Elyson north of I-10, FM 529, Grand Parkway | Confirmed | Community Impact 2014 (Newland, between Cypress and Katy, off Grand Parkway near FM 529) | Sponsored Chron Story Studio source replaced with Community Impact |
| Katy Area EDC private nonprofit; three counties | Confirmed | katyedc.org (private non-profit, 501(c)(6), Harris/Fort Bend/Waller) | Startup help reworded to what the EDC states: planning, site selection, financing |
| EDC lists Fort Bend SBDC and HCC Northwest as partners | Removed | not found in search | Cut. The SBDC panel now cites sbdc.uh.edu directly (free advising, Richmond office, Fort Bend and SW Harris) |
| Pricing FAQ | Corrected | INTAKE.md | Added the $297/mo agent cost |

Summary: 7 checked, 4 confirmed (one updated with a newer fact), 1 corrected, 1 softened, 1 removed.

## /web-design/cypress-tx.html
| Claim | Verdict | Source | Action |
|---|---|---|---|
| Cy-Fair ISD enrollment down 2.7% as of Oct 2025 | Confirmed | Community Impact 2026 | Attributed to Community Impact |
| PASA projection 118,057 to 116,757 by 2034 | Confirmed (April 2025 report, "stabilization" phase) | communityimpact.com demographic shifts article | Dated April 2025 |
| "partly because there is less open land" | Removed | not in search results | Replaced with the report's own "stabilization phase" wording |
| Chamber office on Highway 6 | Removed | not found | Cut |
| Small business category 1 to 9 employees | Confirmed for 2020 | Community Impact 2020 winners | "which in 2020 covered businesses with one to nine employees" |
| UH SBDC "fourteen centers", 32 counties | Corrected | sbdc.uh.edu: 15 locations, 32 counties | "Fifteen locations" |
| Pricing FAQ and package line ("nothing extra while you keep the AI agent") | Corrected | INTAKE.md | Both now state the $297/mo agent cost |

Summary: 7 checked, 3 confirmed, 2 corrected, 0 softened, 2 removed.

## /web-design/beaumont-tx.html
| Claim | Verdict | Source | Action |
|---|---|---|---|
| ExxonMobil $2B expansion 2023, +250,000 b/d, 630,000+, among largest US refineries | Confirmed | corporate.exxonmobil.com release Mar 16 2023 | none |
| Population about 9,000 (Jan 1901) to about 30,000 (Mar 1901) | Confirmed (the CVB figure; Wikipedia's Spindletop article gives 10,000 to 50,000, and both say it roughly tripled) | beaumontcvb.com history | none |
| Cajun families came from Louisiana for work; Choates among them; "Jole Blon" 1946 | Confirmed | Wikipedia Harry Choates; Port Arthur News; oldtimeblues (Gold Star 1946) | Choates source added |
| Lamar enrollment topped 18,000 | Restored (softened by fc-w4-a4) | lamar.edu news Nov 2025 "Fall enrollment tops 18,000" (the body text is ambiguous about the term) | "the university reported enrollment topping 18,000 in late 2025"; source added |
| Pricing FAQ; package paragraph lacked hosting line | Corrected | INTAKE.md | FAQ adds the $297/mo agent cost; the paragraph adds the $49 hosting line |

Summary: 5 checked, 4 confirmed (1 of them restored), 1 corrected (pricing), 0 softened, 0 removed.

## /web-design/round-rock-tx.html
| Claim | Verdict | Source | Action |
|---|---|---|---|
| Dell HQ opened Aug 2 1994; agreement 1993; extended 2024 | Confirmed (restored) | roundrocktexas.gov: agreement extended through 2099 (April 2024); Aug 1993 Chapter 380 agreement; Aug 2 1994 opening | Date, 1993 agreement and 2024 extension restored; city source added |
| Old Settlers Park about 645 acres | Confirmed | roundrocktexas.gov park page | Official source added |
| Multipurpose Complex $27M, 60 acres | Confirmed | Patch; city release (2017 opening rests on the Parkhill source, completed May 2017) | none |
| Commercial Historic District, NRHP 1983, 100 and 200 blocks E. Main | Confirmed (listed June 9 1983, ref 83003170) | NPS NPGallery; THC Atlas | none |
| Pricing FAQ | Corrected | INTAKE.md | Added the $297/mo agent cost |

Summary: 5 checked, 4 confirmed, 1 corrected (pricing). Not rechecked: Express affiliation end year and trademark year (both were already cut or softened, so nothing changed).

## /web-design/the-woodlands-tx.html
| Claim | Verdict | Source | Action |
|---|---|---|---|
| 114,436 residents, 2020 census; QuickFacts link | Confirmed (figure on Wikipedia, English and other languages; the QuickFacts CDP page exists but the snippet did not show the value) | census.gov QuickFacts thewoodlandscdptexas; Wikipedia | none |
| Incorporation rejected Nov 2021, about two thirds no | Confirmed (Prop A 67.44% against, Prop B 66.97%) | communityimpact.com | none |
| Seven-member township board | Not found in search; kept from knowledge (the Township board has seven directors) | thewoodlands.com governance article | kept, flagged |
| ExxonMobil campus "built for up to 10,000 employees and visitors" | Removed | search showed the campus described by size only | Now "its large campus in Spring" |
| HPE HQ at CityPlace 2022 "with room for more than 2,200 Houston-area employees" | Corrected | Houston Chronicle via Quorum Report and Community Impact: about 2,200 employees in the Houston area, not a campus capacity | Reworded to the Houston-area headcount the company gave |
| Chamber founded 1978 as SMCWCC, renamed 2012, 1,300+ employers | Confirmed (restored, self-reported by the chamber) | woodlandschamber.org; thewoodlands.com | Restored with "says it represents" |
| Pricing FAQ | Corrected | INTAKE.md | Added the $297/mo agent cost |

Summary: 7 checked, 3 confirmed, 2 corrected, 0 softened, 1 removed, 1 kept from knowledge and flagged.

## /web-design/texarkana-tx.html
| Claim | Verdict | Source | Action |
|---|---|---|---|
| Texas side 35,971 (2024 estimate) | Confirmed (restored) | census.gov QuickFacts | "about 36,000 people (35,971 in the Census Bureau's 2024 estimate)" |
| NE Texas SBDC: hosted by NTCC and Texarkana College, six counties, Texarkana office | Confirmed (restored) | atcog.org (Bowie, Camp, Cass, Franklin, Morris, Titus; Texarkana satellite); ntcc.edu (hosted by NTCC and TC); no-fee, by appointment | Restored without the street address (two directories give different addresses) |
| Chamber Nov 2024 tuition partnership with TAMUT | Confirmed (restored) | tamut.edu Nov 2024 (MOU signed Nov 4 2024; reduced tuition for chamber and member employees) | Restored with source; chamber name aligned to the university's "Texarkana, USA Chamber of Commerce" |
| TAMUT fall 2026: ninth straight record, about 30% over fall 2025 | Confirmed | tamut.edu Aug 27 2026 | none |
| Pricing: package paragraph lacked the chat widget, phone agent and hosting terms; FAQ lacked the agent cost | Corrected | INTAKE.md | Added the Pro widget (14 days, then $297), the Agency agent (7 days, then $297 for up to 750 minutes, cancel any time) and the $49 hosting line |

Summary: 5 checked, 4 confirmed (3 of them restored), 1 corrected. TAMUT fall 2025 headcount and the Richmond Road retail square footage were not rechecked and stay cut.

## Totals
53 claims checked across 8 pages: 26 confirmed (7 of them restored after earlier softening or removal), 13
corrected (9 of them pricing or FAQ fixes to match INTAKE.md), 4 softened, 9 removed, 1 kept from knowledge and
flagged (The Woodlands board size).
