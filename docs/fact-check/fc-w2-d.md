# Fact-check fc-w2-d: Miami, Orlando, Nashville (Wave 2 batch D, Oct 16 2026)

Checker: fc-w2-d (independent, did not write these pages). Writer notes: docs/writers/w2-d.md.
WebSearch only (WebFetch/curl not used). 25 searches.
Build: `python3 build.py --out /tmp/claude-0/fc-w2d/dist`; `check.py --skip-links --only` on each URL: 0 errors, 0 warnings.
No em/en dashes, "certified" or "guarantee" in any of the three source files.

## /web-design/miami-fl.html
| Claim | Verdict | Source | Action |
|---|---|---|---|
| Miami-Dade: 70.6% Hispanic or Latino | Confirmed | census.gov QuickFacts Miami-Dade (2020 to 2024 ACS / 2025 estimates) | none |
| 75.3% age 5+ speak a language other than English at home | Confirmed | census.gov QuickFacts | none |
| 54.5% foreign born | Confirmed | census.gov QuickFacts | none |
| Little Havana: most businesses still Cuban-owned | Confirmed | Little Havana community background report PDF (giscloud.fiu.edu), "despite increasing diversity, most neighborhood businesses are still Cuban-owned" | source label corrected (it is a community background report hosted by FIU, not an FIU baseline study) |
| "even as Central American families have moved in"; report lists botanicas, music stores, cigar factories | Softened | report says "increasing diversity"; botanicas, cigar shops, music stores on Calle Ocho confirmed by travel and press sources (Pilot Guides, Herald, AAA, VISIT FLORIDA) | rewritten: report credited only for the Cuban-ownership point; Calle Ocho "known for" restaurants, walk-up coffee windows, family cigar shops, botanicas, Latin music stores |
| Viernes Culturales on Calle Ocho, third Friday each month | Softened | miamiandbeaches.com event listing, Time Out (third Friday; some listings dated 2024) | now "usually held on the third Friday of the month" |
| Little Haiti: NE 2nd Avenue main commercial strip | Confirmed | Wikipedia Little Haiti; Local10 2026 ("Northeast Second Avenue corridor"); Hyperallergic (Libreri Mapou on NE 2nd Ave) | none |
| City of Miami designated Little Haiti in 2016 | Confirmed | local10.com 2016/05/27 (commissioners voted unanimously); local10.com 2026/05/26 10-year anniversary (cited URL real) | none |
| Haitian-owned shops, bookstores and restaurants line NE 2nd Ave | Confirmed | Hyperallergic, WLRN (Libreri Mapou), Wikipedia (Chef Creole, shops) | none |
| Wynwood: galleries, retail, antique shops, bars and eateries, one of the largest open-air street art installations in the world | Confirmed | Wynwood BID listing on miamiandbeaches.com (BID language); wynwoodmiami.com | none |
| Wynwood formerly a garment district | Confirmed | Wikipedia Wynwood; BID materials ("home to Miami's Garment District") | none |
| Allapattah: NW 17th Ave nicknamed Little Santo Domingo, Dominican community | Confirmed | Wikipedia Allapattah; savingplaces.org (National Trust); WLRN 2023 | added National Trust source |
| Allapattah: large open-air produce market; textile strip on NW 20th St; auto repair, carpentry, upholstery shops | Softened | sources confirm garment/fabric wholesale around NW 20th St, produce wholesale and bodegas; open-air market and named trades not confirmed | now "long-running garment and fabric wholesale trade around NW 20th Street, alongside produce wholesalers, bodegas and small shops" |
| Google local results: relevance, distance, prominence | Confirmed | support.google.com/business/answer/7091 | none |
| Florida SBDC at FIU, 1101 Brickell Avenue, Miami-Dade and Monroe | Confirmed | business.fiu.edu SBDC contact and FAQ pages (1101 Brickell Ave, South Tower, Suite 300) | none |
| SBDC "free and low-cost consulting on start-up, marketing, financing and government contracting" | Corrected | FIU SBDC FAQ: most services at no cost (export marketing plan is fee-based); services are consulting, workshops, market research, help seeking financing | rewritten to match the FAQ |
| Miami-Dade SBE certification programs free, race and gender neutral; local business tax receipt required | Confirmed | miamidade.gov certification programs and SBE pages | none |
| Greater Miami Chamber traces to the Miami Board of Trade, 1907 | Confirmed | miamichamber.com history; miamidade.gov 2019 chamber PDF | none |
| This site's EN/ES toggle "at the top" runs on Google machine translation | Confirmed | src/static/js/site.js (google.translate.TranslateElement, includedLanguages "es"); src/templates/partials/header.html (toggle in header) | none |
| Maurice does not claim to write fluent Spanish; Spanish (and Creole) written or reviewed by client or a fluent person | Confirmed (honesty) | page text; no place on the page says Maurice writes Spanish | none |
| Prices, trials, hosting, AI receptionist wording, no Miami office, no ranking promise | Confirmed | INTAKE.md sections 1 and 3 | none |
| Doral, Hialeah, Coral Gables are separate cities | Confirmed (general knowledge) | n/a | none |

Miami: 21 checked, 17 confirmed (one with its source label corrected), 1 corrected (SBDC services), 3 softened (Little Havana businesses, Viernes Culturales date, Allapattah trades), 0 removed.

## /web-design/orlando-fl.html
| Claim | Verdict | Source | Action |
|---|---|---|---|
| Record about 76.7 million visitors in 2025 | Confirmed | visitorlando.org press release (cited URL real); ConventionSouth, Travelweek | none |
| 70.3 million domestic, 6.3 million international | Confirmed | Visit Orlando release; Prevue, Travel Industry Today | none |
| Canada top foreign market; Mexico, Colombia, Japan set records | Confirmed | Visit Orlando release (records: U.S., Mexico, Colombia, Japan; Canada 1.1 million, top) | none |
| Orlando Main Streets "since 2007" | Corrected | orlando.gov Main Streets page: created by Mayor Dyer and Council in 2008; 2016 annual report "established in 2008" | changed to 2008 |
| First districts Audubon Park, College Park, Downtown South, Ivanhoe Village, Mills 50 | Confirmed | orlando.gov 2009 annual reports; Wikipedia (Downtown South later SoDo) | added "(now SoDo)" |
| Later Church Street, Thornton Park, Milk District, Gateway Orlando | Confirmed | Spectrum News 13 2018 list; orlando.gov Gateway District (joined 2012) | none |
| Curry Ford West added as a district by the city council in 2018 | Confirmed | mynews13.com 2018/10/08 (approved as 10th district) | none |
| 2024 annual report describes twelve corridors | Softened | orlando.gov 2023 report "twelve unique neighborhood commercial corridors"; Sept 2025 Council highlights "grown to twelve"; 2024 page snippet did not show the count | now "The program now counts twelve neighborhood commercial districts." |
| 34.9% of Orlando residents Hispanic or Latino (2023 ACS, city summary) | Confirmed | orlando.gov ACS 2023 1-year summary report (QuickFacts 5-year shows 35.6%, a different vintage) | none |
| Pew: Orlando metro had more Puerto Ricans than any other Florida metro in 2013, about 314,000 | Confirmed | pewresearch.org 2015/10/30 short read (cited URL real) | none |
| FAQ: "about 35%" Hispanic | Confirmed | as above | none |
| Florida SBDC at UCF: no-cost consulting and seminars, National Entrepreneur Center at Orlando Fashion Square | Confirmed | ucf.edu location page; cflbizlink.com listing; UCF news 2026 | none |
| SBDC at UCF serves "Orange and seven neighboring counties" | Corrected | UCF: eight counties (Brevard, Flagler, Lake, Orange, Osceola, Seminole, Sumter, Volusia); not all border Orange | now "an eight-county area that includes Orange, Osceola and Seminole" |
| Hispanic Chamber of Metro Orlando aims to strengthen Hispanic business in Central Florida | Confirmed | hispanicchamber.com | none |
| Chamber membership "made up largely of small businesses" (72%) | Softened | hispanicchamber.com Who We Are: 80% business owners and professionals, 20% large corporations; 72% figure not found | reworded to "mostly business owners and professionals rather than large corporations"; source replaced with hispanicchamber.com/who-we-are/ |
| Google local results: relevance, distance, prominence | Confirmed | support.google.com/business/answer/7091 | none |
| Prices, trials, hosting, AI receptionist wording, no Orlando office, no ranking promise; EN/ES toggle is Google machine translation | Confirmed | INTAKE.md; src/static/js/site.js | none |

Orlando: 17 checked, 13 confirmed, 2 corrected (program start year 2007 to 2008; SBDC counties), 2 softened (twelve districts wording, chamber membership), 0 removed.

## /web-design/nashville-tn.html
| Claim | Verdict | Source | Action |
|---|---|---|---|
| Metro grew about 86 people a day in 2023 | Confirmed | nashvillechamber.com press release (cited URL real) | none |
| About 66 a day moved in | Confirmed | nashvillechamber.com "66 people a day moved to Nashville in 2023" (24,246 movers) | none |
| Music Industry Report 2020: direct music employment 21,878 jobs in 2019, up 29% since 2012 | Confirmed | nashvillechamber.com Music Industry Report 2020 release | none |
| Region's concentration of music businesses highest in the nation | Confirmed | Nashville Chamber research center | none |
| Metro charter approved June 1962; consolidated government since April 1, 1963 | Confirmed | nashville.gov history of Metro and 60th anniversary pages; Metro Archives | none |
| Nolensville Pike often called the international corridor | Confirmed | Edible Nashville ("most diverse corridor"); Vanderbilt dining guide | none |
| Kurdish, Turkish, Salvadoran restaurants on Nolensville | Confirmed | Edible Nashville (Edessa, Istanbul); El Paraiso at 2209 Nolensville Pike | none |
| Somali, Persian and Southeast Asian restaurants and markets | Softened | not found by name; Vanderbilt: grocers and restaurants from Central and South America, the Indian subcontinent, Africa and the Middle East | replaced with the Vanderbilt list; added Vanderbilt source |
| Edible Nashville cited URL article/42249-2/ | Corrected | could not confirm that URL; confirmed Edible URL eat/best-ethnic-food-nolensville-pike | source URL replaced |
| "A Nashville mayor's proclamation ... pointed to the many Kurdish-owned businesses" | Corrected | NewsChannel 5 and Kurdsat: Mayor John Cooper proclaimed March Kurdish Heritage Month in 2022; the point about Kurdish-owned businesses on Nolensville and Murfreesboro pikes was made by a community leader (Effendi Foundation), not the proclamation | rewritten: "When Mayor John Cooper proclaimed March as Kurdish Heritage Month in 2022, community leaders pointed to..." |
| Tennessee SBDC Nashville office, 315 10th Avenue North, by appointment, run with TSU, free consulting | Confirmed | tsbdc.org/center/nashville (315 10th Ave N, by appointment); tsbdc.org/tsu (TSU host). Other directories list 330 10th Ave N Suite G-400; the office's own page wins | none |
| SCORE Nashville: free mentoring for the life of the business, workshops, Davidson, Williamson, Rutherford, Sumner, Wilson, Montgomery | Confirmed | score.org/nashville; score.org/tn/nashville/contact-us/ | none |
| Google local results: relevance, distance, prominence; prominence from reviews, links, mentions | Confirmed | support.google.com/business/answer/7091 | none |
| Prices, trials, hosting, AI receptionist wording, no Nashville office, no ranking promise | Confirmed | INTAKE.md | none |
| Neighborhood and town names (The Gulch, East Nashville, 12 South, Germantown, Sylvan Park, Antioch, Donelson, Franklin, Murfreesboro, Hendersonville) | Confirmed (place names only) | general knowledge | none |

Nashville: 15 checked, 12 confirmed, 2 corrected (Kurdish proclamation attribution and year; Edible source URL), 1 softened (Nolensville cuisines), 0 removed.

## Totals
53 claims checked: 42 confirmed, 5 corrected, 6 softened, 0 removed. Sources added: National Trust (Allapattah), Vanderbilt (Nolensville), Hispanic Chamber Who We Are (replaces Partner guide).
