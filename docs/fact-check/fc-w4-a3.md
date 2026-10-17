# Fact-check report: fc-w4-a3 (Wave 4, Oct 17 2026)

Independent checker. I wrote none of these pages. Pages: midland-tx, odessa-tx, killeen-tx, sugar-land-tx,
katy-tx, cypress-tx (source files in src/pages/web-design/). Writer notes: docs/writers/w4-a5.md, w4-a6.md.

**Limitation (read this first).** The shared WebSearch budget for this turn (200 calls across all agents) ran
out after 25 of my searches, partway through Odessa. Midland and Odessa got full search verification. For Killeen,
Sugar Land, Katy and Cypress I did every check that does not need search: business claims against INTAKE.md,
alt text against each photo, removing weak sources (realty blogs, builder blog, apartment blog) and the claims that
rested only on them, and checking claims against what I already knew. Claims marked "Not verified (no search)"
below still rest only on the writer's source and need a follow-up search pass before anyone calls these four pages
fully fact-checked.

Build: `python3 build.py --out /tmp/claude-0/fc-w4-a3/dist`; check.py --only for each page: 0 errors, 0 warnings.
Similarity after edits: area max 5.3% (abilene/new-orleans, neither page is mine). None of my six pages is in the
top 10 pairs, so all are under 5.3%.

## /web-design/midland-tx.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Permian output record 6.2M b/d in Q2 2024 | Confirmed | dallasfed.org pb2402 | none |
| 36 fewer rigs, 310 in June against 346 | Confirmed | dallasfed.org pb2402 | none |
| Nonfarm jobs contracted 1.4% annualized through June | Confirmed | dallasfed.org pb2402 | none |
| 2015: restaurant added Sunday brunch, dealer shifted to repairs/used cars, "Dallas Morning News" | Corrected | Details match a New York Times report (Jan 19 2015, Clifford Krauss) reproduced at sej.org/node/20138. Dallas News URL not found in search | Attributed to NYT, source replaced |
| 2020 price war plus pandemic "double whammy" (CBS News) | Confirmed | cbsnews.com | none |
| Loop 250 Midland Dr to Garfield: restaurants, shopping, Midland Park Mall off Midkiff | Confirmed | Wikipedia Loop 250; simon.com | none |
| Airport owned by City of Midland, inside city limits, about midway between downtowns | Confirmed | flymaf.com; Wikipedia; FAA | none |
| FAA spaceport license 2014, first primary commercial service airport | Confirmed | Wikipedia; Midland Reporter-Telegram via search; flymaf | none |
| Google: relevance, distance, prominence | Confirmed | support.google.com 7091 | none |
| UTPB SBDC in College of Business, serves Midland and Ector | Confirmed | utpb.edu award story; TexVet; UTPB catalog | utpb.edu/directory URL not verifiable, replaced with UTPB catalog page |
| 2024 Excellence and Innovation award, Northwest Texas SBDC network | Confirmed | utpb.edu success story | none |
| Midland Chamber more than 1,000 members | Confirmed | midlandtxchamber.com membership page | none |
| Leadership Midland | Confirmed (since 1978) | midlandtxchamber.com chamber history | Added year and source |
| Founder's Blend monthly, first Wednesday | Softened | Aug 2026 newsletter lists Wed Aug 5, free, 7:30 networking; "monthly first Wednesday" not stated anywhere | Reworded to a Wednesday morning event, Aug 5 listed |
| MDC $200,000 "grant" for UTPB incubator and makerspace | Corrected | NewsWest 9: a $200,000 payment under an incubator and makerspace grant agreement (undated) | Reworded |
| Entrepreneurial Challenge relaunch 2021, up to eight winners, up to $100,000 each | Confirmed | EIN Presswire Aug 2021 release | none |
| Packages, prices, trials, hosting, no office, AI receptionist | Confirmed | INTAKE.md | none |
| Alt text: electrical/4 "gray work shirt" | Corrected | photo shows a light, near-white shirt | "light-colored work shirt" |
| Other alts (restaurant/2, chiropractic/6, fallback hero) | Confirmed | viewed photos | none |

Summary: checked 19, confirmed 14, corrected 4, softened 1, removed 0.

## /web-design/odessa-tx.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| HUD January 2024 profile: economy expands/contracts with oil, largest employers oilfield service | Softened | The cited HMP PDF did not show up in search. HUD's Odessa CHMA (OdessaTX_comp_15.pdf) says the economy has been closely linked to oil and gas since the 1920s and slowed with oil prices | Reworded to the CHMA, employer-list clause cut, source replaced |
| Metro covers all of Ector County | Confirmed | Wikipedia Odessa (MSA = Ector County) | none |
| Andrews Hwy industrial, E 42nd retail/warehouse, N Grandview offices | Removed | Rested only on two commercial property listings (weak source) | Generic sentence, both listing sources removed |
| Population 115,743 (2023 estimate) | Confirmed | census.gov QuickFacts | none |
| Hispanic or Latino 61.2% | Confirmed | census.gov QuickFacts | none |
| OC Truck Driving Academy up to 200 hours, Class A CDL | Confirmed | odessa.edu | none |
| PSP $3.5M to academy, "Transport Topics reported" | Corrected | The TT article is from March 30 2018 (college bringing CDL training in-house) and does NOT report the gift. The $3.5M PSP gift (trucks, instructors, scholarships, Jan 2023, CDL shortage) is confirmed by KOSA and Odessa American | Re-attributed to the Jan 2023 announcement, TT source replaced with KOSA |
| UTPB is in Odessa | Confirmed | common knowledge, utpb.edu | none |
| Workforce Solutions Permian Basin office at JBS Parkway; WorkInTexas; free to employers | Confirmed | pbrpc.org; TWC | none |
| "local arm of the Texas Workforce Commission" | Softened | Local boards are partners of TWC, not its arm | Reworded |
| ODC job creation grants, capital investment grants, incentives | Confirmed | pbrpc.org ODC listing | none |
| Chamber: small business support; economic development department funded by ODC | Softened | odessachamber.com says so; Odessa American reports it is a contract the council has reviewed | "funded through the ODC, according to the chamber" |
| Governor's Small Business Summit in Odessa | Confirmed (co-hosted with ODC, chamber, TWC) | gov.texas.gov | "co-hosted" |
| UTPB SBDC "based in the CEED building" | Removed | Could not confirm the SBDC's location | Replaced with College of Business, confirmed |
| SBDC helps with funding and business plans; director speaks to ODC monthly | Confirmed (wording aligned to "start, expand and grow") | NewsWest 9; utpb.edu | Reworded slightly |
| Spanish copy disclaimer, prices, trials, no office, AI receptionist | Confirmed | INTAKE.md | none |
| Alts (hero, hvac/2, veterinary/2, dental/3) | Confirmed | viewed photos | none |

Summary: checked 17, confirmed 10, corrected 1, softened 4, removed 2.

## /web-design/killeen-tx.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Renamed Fort Cavazos 2023; Army announced June 2025 return to Fort Hood, honoring Col. Robert B. Hood, WWI DSC | Confirmed (prior knowledge, no search) | KXXV; Dallas Morning News | none |
| About 214,000 acres | Confirmed (prior knowledge) | Wikipedia | none |
| Killeen 153,095 (2020 Census) | Confirmed (prior knowledge) | QuickFacts | none |
| 159,643 (2023 estimate) | Not verified (no search) | QuickFacts | kept, flag |
| TAMUCT founded 1999 as Tarleton branch, non-traditional students, site on post | Partly confirmed (founding, prior knowledge); "site on the post" not verified | Wikipedia | kept, flag |
| Central Texas College in Killeen | Confirmed (prior knowledge) | Wikipedia | none |
| SBA pointed spouses to Boots to Business on installations | Confirmed (prior knowledge; past tense) | sba.gov 2017 | none |
| Harker Heights 57 single-family permits in 2025 | Not verified (no search) | KDH | kept, flag |
| Nolanville hired an economic development director | Not verified (no search) | nolanvilletx.gov | kept, flag |
| Chamber added 88 members, total 468; 32 ribbon cuttings in 2024 | Not verified (no search) | KDH | kept, flag |
| KEDC three-person office funded by city | Not verified (no search) | KDH 2024 | kept, flag |
| Google ranking factors | Confirmed | support.google.com | none |
| Prices, trials, hosting, no office, AI receptionist | Confirmed | INTAKE.md | none |
| Alts (contact-hero, therapist-waiting-room, chiropractic/5, salon/3) | Confirmed | viewed photos | none |

Summary: checked 14, confirmed 8, corrected 0, softened 0, removed 0; 6 not verified (search budget).

## /web-design/sugar-land-tx.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Fort Bend long named among most diverse counties | Confirmed (prior knowledge) | Texas Tribune 2011 | none |
| Kinder Institute: near even split Asian, Latino, Black, Anglo | Confirmed (prior knowledge) | Community Impact | none |
| GHP Dec 2025: region's most diverse county | Not verified (no search) | houston.org | kept, flag |
| Foreign-born 35.3% (2019-2023); Asian alone 39.5% (2020) | Not verified (no search) | QuickFacts | kept, flag |
| Town Square opened 2003 with City Hall, hotel, shops, offices | Confirmed (prior knowledge) | Wikipedia; ULI | none |
| First Colony begun 1977, about 10,000 acres; remaining districts annexed 1997 | Confirmed (prior knowledge) | Wikipedia | none |
| Telfair on former prison land sold 2002, first homes 2006 | Not verified (no search) | Wikipedia | kept, flag |
| Char House 1925; production stopped 2003; Imperial Market stalled | Confirmed (prior knowledge) | city report; Community Impact | none |
| City approved purchase Feb 2025, closed June 2025 | Not verified (no search) | ABC13; Covering Katy | kept, flag |
| US 59 low-rise offices in the 1980s | Not verified (no search) | Wikipedia | kept, flag |
| Fort Bend Chamber on Commerce Green Blvd | Confirmed (prior knowledge) | uschamber.com | none |
| Governor's Small Business Summit, Sugar Land, May 2025, with TWC | Not verified (no search) | gov.texas.gov | kept, flag |
| Fort Bend County SBDC: UH network, no-cost advising, Richmond office, three counties | Not verified (no search) | sbdc.uh.edu | kept, flag |
| Plug and Play three-year agreement 2024, funded by SLDC | Not verified (no search) | Community Impact | kept, flag |
| Google ranking factors | Confirmed | support.google.com | none |
| Tutoring owner labeled "Picture an owner" (illustration, not a client) | Confirmed | page text | none |
| Prices, trials, hosting, no office, AI receptionist | Confirmed | INTAKE.md | none |
| Alts (bakery hero, dental/2, restaurant/1, veterinary/1) | Confirmed | viewed photos | none |

Summary: checked 18, confirmed 10, corrected 0, softened 0, removed 0; 8 not verified (search budget).

## /web-design/katy-tx.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| City of Katy 21,894 (2020); in Harris, Fort Bend, Waller counties | Confirmed (prior knowledge) | Wikipedia | none |
| Katy address does not mean inside city; much of area unincorporated or Houston ETJ | Confirmed (prior knowledge) | Wikipedia Greater Katy | none |
| Katy EDC "three counties, one marketplace" | Not verified (no search) | katyedc.org | kept, flag |
| Katy ISD 97,000+ students, 100+ campuses and facilities, 2025-26 | Not verified (no search; official district source) | katyisd.org | kept, flag |
| Enrollment gains smaller since 2024-25 | Not verified (no search) | Community Impact | kept, flag |
| Cinco Ranch CDP, Fort Bend and Harris, 16,899 (2020) | Not verified (no search) | Wikipedia | kept, flag |
| Cross Creek Ranch 3,200 acres, Fulshear address | Confirmed (prior knowledge) | Johnson Development | none |
| Elyson north of I-10 on FM 529 by Grand Parkway | Confirmed (prior knowledge); source is sponsored Chron Story Studio content (weak) | storystudio.chron.com | kept, weak source flagged |
| Rice Harvest Festival each fall for decades; began as "Sellabration" late 1970s/early 1980s; moved downtown | Kept, rests on Texas House resolution and Community Impact | capitol.texas.gov; communityimpact.com | none |
| City of Katy and Rotary present it; proceeds to Rotary scholarships | Removed | Rested on an apartment-complex blog (weak) | Sentence cut, Olympus source removed |
| Katy Area EDC private nonprofit, startup help, SBDC and HCC partners | Not verified (no search) | katyedc.org | kept, flag |
| Katy Area Chamber exists | Confirmed (prior knowledge) | Community Impact | none |
| Prices, trials, hosting, no office, AI receptionist | Confirmed | INTAKE.md | none |
| Alts (pricing hero, seo-city-pages-planning, hvac/1, legal/3) | Confirmed | viewed photos | none |

Summary: checked 14, confirmed 7, corrected 0, softened 0, removed 1; 6 not verified (search budget).

## /web-design/cypress-tx.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Unincorporated, Harris County, Houston ETJ, about 24 mi NW along US 290; 1980s growth | Confirmed (prior knowledge) | Wikipedia Cypress | none |
| US 290 and Grand Parkway "frame much of the growth" | Softened | Taylor Morrison builder blog (weak) | "run through the area", blog removed |
| Bridgeland a Howard Hughes MPC; Towne Lake lake about 300 acres; Fairfield developed from 1988 | Softened | Realtor blogs only (HAR agent blog, Houston Prime Realty) | Kept the four community names only, both sources removed |
| Bridgeland, Towne Lake, Coles Crossing, Fairfield grouped under 77433 | Softened | Realtor blog only | "Cypress has several ZIP codes, 77433 among them"; Harbert source removed |
| Cy-Fair ISD third-largest in Texas, nearly 118,000 | Confirmed (prior knowledge) | Community Impact | none |
| Enrollment down 2.7% Oct 2025; projection 118,057 to 116,757 by 2034 | Not verified (no search) | Community Impact | kept, flag |
| LSC-CyFair on Barker Cypress Road; business courses | Confirmed (prior knowledge) | Wikipedia; lonestar.edu | none |
| Cy-Fair Houston Chamber office on Highway 6; small business award category 1 to 9 employees | Not verified (no search) | Community Impact | kept, flag |
| UH SBDC 14 centers, 32 counties, ZIP finder | Not verified (no search) | sbdc.uh.edu | kept, flag |
| Chiropractor example clearly hypothetical ("Take a chiropractor") | Confirmed | page text | none |
| "Hero photo shows an owner reviewing bills" | Corrected | photo shows laptop and calculator, no bills | Reworded |
| Prices, trials, hosting, no office, AI receptionist | Confirmed | INTAKE.md | none |
| Other alts (hero, real-estate/3, chiropractic/4, dental/1) | Confirmed | viewed photos | none |

Summary: checked 13, confirmed 6, corrected 1, softened 3, removed 0; 3 not verified (search budget).
