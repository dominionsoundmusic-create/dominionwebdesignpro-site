# Fact-check report: fc-w4-c1 (Wave 4, Oct 17 2026)

Independent checker. I wrote none of these pages. Pages: /web-design/denver-co.html, colorado-springs-co.html,
fort-collins-co.html, seattle-wa.html, spokane-wa.html. Writer notes: docs/writers/w4-c1.md, w4-c2.md.

Method: I read each page, the writer notes and INTAKE.md. I verified claims with WebSearch, at most 6 searches per
page and 30 in all. WebFetch is blocked, so I checked against search results from the cited or official source.
"PK" means I confirmed it from my own knowledge (well-known geography, time zones, place names) with no search.
I opened every image (contact sheets of all 20 files in src/static) and checked each alt text against the photo.
I checked pricing and FAQ text against INTAKE.md. I built into /tmp/claude-0/fc-w4-c1/dist, ran check.py
--only on each page (0 errors, 0 warnings), ran similarity.py (highest area pair in the whole site is 6.1%, so all
five pages are under 15%), and found no em or en dashes and no banned phrases.

## /web-design/denver-co.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| C2ER index puts Denver at 110.2 vs 100, about 10% above average, housing the main driver | Confirmed, but the data is dated | KDVR digital-release (cites 2022 to 2023 pricing) | Added "using 2023 price data" |
| Median household income $94,718, 2020 to 2024 | Confirmed | Census QuickFacts, Denver County | None |
| Colorado has 730,887 small businesses, 99.5% of businesses | Confirmed | SBA Advocacy 2025 Colorado profile | None |
| RiNo historically part of Five Points; industrial area | Confirmed | Source Hotel, 5280, Beacon | None |
| "foundries and pattern shops" | Softened | Sources say factories, warehouses, foundries | Changed to "factories, warehouses and foundries" |
| Artists moved into empty warehouses for low rents | Confirmed | Search results (Source Hotel, Beacon) | None |
| District formally founded 2005 | Confirmed | Multiple sources (Hadley-Hooper and Weil, 2005) | None |
| Creative businesses (architects, furniture makers, photographers) | Confirmed per writer source | Source Hotel (writer) | None |
| "apartment towers along Brighton Boulevard" | Softened | Not checked in detail | Changed to "newer apartment buildings" |
| DEDO business development team offers free one-on-one advising | Not searched; writer source on denvergov.org; low risk | denvergov.org | Kept |
| Denver Metro SBDC now hosted by Red Rocks CC, no-cost advising, moved to Lakewood campus fall 2025 | Confirmed | ColoradoBiz, RRCC, sbdc.colorado.gov | None |
| SCORE Denver and Wyoming, free mentoring, covers Metro Denver, Northern Colorado, SE Wyoming | Not searched (budget); writer source score.org; chapter name matches | score.org | Kept |
| Chamber VP said Dec 2025 small businesses are 85% of members | Confirmed | Colorado Politics; chamber site also says 85% | None |
| Google local ranking: relevance, distance, prominence | Confirmed (PK, well-documented Google help page) | support.google.com | None |
| Neighborhood and suburb names (LoHi, Highlands, South Broadway, Capitol Hill, Cherry Creek, Aurora, Lakewood, Englewood, Arvada) | Confirmed | PK | None |
| Pricing, three-year totals ($2,261 / $2,761 / $3,761), trials, $297, $49 | Confirmed | INTAKE.md (arithmetic checked: 497+1764, 997+1764, 1997+1764) | None |
| FAQ: $49 or included with AI agent ($297/mo after trial) | Confirmed | INTAKE.md | None |
| Image alts (insurance/4, hire-domain-ownership, auto-repair/1, contact-hero fallback) | 3 accurate, 1 fixed | Opened files | Fallback alt: "with a notepad in hand" changed to "writing in a notepad" |

Summary: 18 checked, 12 confirmed, 1 corrected (fallback alt), 3 softened, 0 removed. Searches 6, PK 2, writer source kept 2.

## /web-design/colorado-springs-co.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| USOPC headquartered in Colorado Springs since 1978 | Confirmed | Gazette (Aug 1 1978), KOAA | None |
| USOPC owns and operates the training center | Confirmed | KOAA, KRDO | None |
| City leases HQ on South Tejon Street; deal lets city brand as Olympic City USA | Confirmed | KRDO, KOAA | None |
| Museum 60,000 square feet, Hall of Fame, downtown | Confirmed | Visit COS museum page, olympics.com, CSURA; opened July 30 2020 | Added "opened in 2020"; replaced the sports-itinerary blog source with the Visit COS museum page |
| Training center more than 15,000 athletes and 130,000 visitors a year | Removed | Not found in any search result | Sentence deleted |
| Garden of the Gods given 1909 by Perkins's children, free to the public | Confirmed | coloradosprings.gov/gog | None |
| "city says well over 4 million visitors a year" | Softened | The city page did not show a figure; 4.5 million appears only on travel sites | Changed to "draws millions of visitors a year" |
| Old Colorado City founded 1859 | Confirmed | History Colorado, Wikipedia, markers (exact day varies) | None |
| Briefly territorial capital | Confirmed (sources differ on 1861 vs 1862) | History Colorado, Westside Pioneer | Wording kept general ("briefly") |
| Historic district on National Register since 1982 | Confirmed | NPS NRIS 82001018, listed Nov 2 1982 | Grammar fix ("has had") |
| Colorado Springs MSA 2025 estimate 781,796 | Confirmed | FRED CLRPOP (July 1 2025) | None |
| Pikes Peak SBDC hosted by Colorado Springs Chamber and EDC, Catalyst Campus 559 E. Pikes Peak Ave., El Paso and Teller counties, no-cost | Confirmed | sbdc.colorado.gov Pikes Peak listing | None |
| Chamber and EDC small business resource hub | Confirmed per writer source | coloradospringschamberedc.com | None |
| Place names (Briargate, Monument, Manitou Springs, Broadmoor, Powers Boulevard, Pikes Peak, Colorado Avenue) | Confirmed | PK | None |
| Pricing: FAQ said $49 or included with AI agent but the page never named the $297 charge | Corrected | INTAKE.md | Added "($297 a month after its free trial)" to FAQ; Pro line now names the chat widget (free 14 days, then $297/mo) and the $49 hosting |
| Hero alt "sketching page layouts on paper beside a laptop" | Corrected | Opened file: hands on the laptop, sketches and a pencil beside it | Alt rewritten |
| Plumbing/3 alt "kneeling" | Corrected | Photo shows him leaning at the sink | "leaning" |
| Cleaning/4, roofing/4 alts | Confirmed | Opened files | None |

Summary: 18 checked, 12 confirmed, 4 corrected, 1 softened, 1 removed. Searches 6, PK 1.

## /web-design/fort-collins-co.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| CSU record enrollment 34,412 in fall 2025 | Confirmed | CSU newsroom, Oct 9 2025 | None |
| $622 million sponsored research, FY2025 | Confirmed (record) | CSU research news, Institutional Profile 2024 to 2025 | Wording: "reported a record $622 million in sponsored research spending" |
| CSU STRATA combined CSU Ventures and CSU Research Foundation | Confirmed | PK (2020 merger), writer source | None |
| Lab to Life, Dept. of Commerce grant, goal of 15 companies in three years | Confirmed, but the goal dates from the 2022 award | CSU SOURCE, EDA Build to Scale | Softened to "started ... with a stated goal of"; no claim that it is still running toward that goal |
| Population estimate 170,376 (July 1 2023) | Confirmed | Census QuickFacts (2024 city value shows NA) | Credited to the Census Bureau in text |
| Disneyland Main Street drew on Old Town per Harper Goff, who grew up there and photographed its buildings | Confirmed | history.fcgov.com (rates it true), Visit Fort Collins | None |
| "local guides count more than 20 breweries" (KMAX radio list) | Softened | Weak source | Changed to "known for its craft breweries" (PK); KMAX source removed |
| Larimer SBDC hosted by Front Range CC, South Shields Street campus, no-cost confidential advising, no- or low-cost training | Confirmed | sbdc.colorado.gov/larimer (4616 S. Shields) | None |
| Economic Health Office Business Connectors, free guidance in English and Spanish | Not searched (budget); writer source fcgov.com; low risk | fcgov.com | Kept |
| Chamber: more than 80% of members have 20 or fewer employees; celebration each September | Softened | Search found nothing to support the 80% figure or the month | Cut the 80% and "September"; now "holds a yearly event celebrating small business" (the chamber's key-events page title) |
| I-25 to Denver, about an hour south; Old Town, Campus West, Midtown, College Ave, Harmony Road, Loveland, Windsor, Timnath | Confirmed | PK | None |
| Google local ranking factors | Confirmed | support.google.com | None |
| Pricing paragraph (Starter, Pro, Agency, trials, $297, $49, "We do not sell page counts") | Confirmed | INTAKE.md | None |
| Hero alt "Five-story red brick office building" | Softened | City photo; storey count unclear (about 4 plus a tower) | Cut "Five-story" |
| Electrical/4, domain-renewal-reminder, insurance/3 alts | Confirmed | Opened files | None |

Summary: 15 checked, 9 confirmed, 0 corrected, 5 softened, 1 removed (the KMAX brewery source). Searches 6, PK 3.

## /web-design/seattle-wa.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| CBRE 2026 Scoring Tech Talent: Seattle No. 2 | Confirmed | CBRE press release, GeekWire | None |
| Tech jobs 10.2% of metro employment vs 5.5% average across 50 markets | Confirmed (GeekWire, citing CBRE) | GeekWire | None |
| Google local ranking factors | Confirmed | support.google.com | None |
| West Seattle Junction: streetcar lines met at California Ave SW and SW Alaska St, April 1907 | Confirmed | HistoryLink 8725, Seattle historic sites | None |
| Displaced Admiral as commercial center by end of decade | Confirmed | HistoryLink | None |
| "one of more than a dozen business improvement associations" | Softened | Count not found | Changed to "work together through the West Seattle Junction Association" |
| Minimum wage $21.30 from Jan 1 2026, up from $20.76; same rate for all employers | Confirmed | Seattle OLS announcement | None |
| Most businesses need a business license tax certificate, renewed yearly | Confirmed | PK, seattle.gov/licenses | None |
| OED ABC program: up to 10 hours free one-on-one help | Corrected | City page: up to 10 hours per category, eligibility rules apply | Now "up to 10 hours ... per topic for eligible ..."; dropped "several languages" (not seen); added the ABC program page as a source |
| OED Small Business Legal Assistance: free counseling and workshops incl. commercial leases | Not searched (budget); writer source seattle.gov | seattle.gov | Kept |
| Washington SBDC: more than 30 advisors, WSU and SBA, no cost | Confirmed (newer pages say 40+; "more than 30" still true) | sbdc.wsu.edu, business.wa.gov | None |
| Seattle Metro Chamber about 2,500 members, 80% small to mid-size (2026 prospectus); Small Business Advisory Group | Confirmed | 2026 Membership Prospectus | None |
| Seattle two hours behind Big Sandy | Confirmed | PK (Pacific vs Central) | None |
| Bellevue, Redmond, Kirkland separate cities east of Lake Washington; neighborhood names | Confirmed | PK | None |
| FAQ "quotes often run high" in Seattle | Softened | Not verifiable | Changed to "that can show up in their quotes" |
| Pricing (FAQ lists $49 hosting AND $297 agent as recurring; package list) | Confirmed | INTAKE.md | None |
| Salon/2 alt "a stylist working with a client in the background" | Softened | Background figures are blurred | "people working in the background" |
| Contractor-review, cleaning/3, faq-hero fallback alts | Confirmed | Opened files | None |

Summary: 18 checked, 13 confirmed, 1 corrected, 3 softened, 0 removed. Searches 6, PK 3.

## /web-design/spokane-wa.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Spokane Valley unincorporated for over a century; voters narrowly approved May 21 2002 after failed 1990s attempts; city began March 31 2003 | Confirmed | HistoryLink 10119, city About Us | None |
| 2020 census 102,976, "largest suburb of Spokane" (Wikipedia only) | Softened | Weak source; city site says more than 107,000 as of 2022 | Now "the city says it is now home to more than 100,000 people"; Wikipedia source removed |
| City calls the region the health care hub of the Inland NW and northern Idaho, largest concentration of medical services in four states | Confirmed as the city's own description | spokanevalleywa.gov/270 | Already attributed to the city; kept |
| Coeur d'Alene and Post Falls in north Idaho | Confirmed | PK | None |
| Browne's Addition: west of downtown, often called oldest neighborhood | Confirmed | PK, Visit Spokane, KREM | None |
| Browne's Addition dates to 1883, National Register 1976 | Softened | Search returned nothing on the dates | Dates cut; kept "has a historic district on the National Register" (PK) |
| Garland District north of downtown, 1940s-era Garland Theater; South Perry cafes, shops, weekly farmers market | Confirmed | PK, Visit Spokane districts page | None |
| Kendall Yards: Union Pacific rail facility 1914 to 1955, just north of downtown, vacant for decades | Confirmed | WA Ecology site page and blog | None |
| "Construction began in 2010"; east end shops/apartments, west end townhouses/houses | Corrected/softened | Ecology: project stalled in recession, revived 2010 | Now "got moving again in 2010 after stalling in the recession, and it now mixes shops, apartments and houses"; Wikipedia West Central source replaced by the Ecology blog |
| Expo '74 ran May to November 1974 | Confirmed | Wikipedia, HistoryLink, BIE | None |
| Expo drew 5.6 million visitors | Softened | Sources differ (5.6M Wikipedia, about 5.2M HistoryLink) | "more than 5 million" |
| Park opened 1978 | Corrected | Spokesman-Review: dedicated May 5 1978 by President Carter | "The site was dedicated as Riverfront Park in 1978"; Wikipedia Expo source replaced by the Spokesman piece |
| Park "hosts" Bloomsday and Hoopfest | Softened | PK: both are downtown events near the park | "big events like Bloomsday and Hoopfest still bring crowds to the area" |
| Fairchild AFB and Gonzaga "appear on lists of largest employers" (TVB source) | Corrected | WSAC and WA ESD profiles name Fairchild as the county's largest employer; Gonzaga only on commercial lists | Now: Fairchild named in state profiles as the largest employer; Gonzaga "sits just north of downtown" (PK). TVB source replaced by WSAC and ESD |
| Washington SBDC (WSU and SBA) lead center and advising offices at The Quarry in Spokane Valley; free, confidential; workshops and market research | Confirmed | WSU research news, Spokane Journal, sbdc.wsu.edu | None |
| Greater Spokane Inc.: chamber and economic development group | Confirmed | Spokane Valley partners page, PK | None |
| GSI is the state-designated economic development organization for Spokane County | Removed | Not confirmed in search | Clause cut |
| Hero alt: Spokane County Courthouse, pale stone, turreted tower, dark roofs, bare trees, snow | Confirmed | Opened file; real city photo from images/cities | None |
| Roofing/3, landscaping/2, designer-cost-quote-review alts | Confirmed | Opened files | None |
| Pricing: FAQ said $49 or included with AI agent | Corrected | INTAKE.md | Added "($297 a month after its free trial)"; body already lists the trials |
| "How often should a website be redesigned" FAQ: small updates part of maintenance | Confirmed | INTAKE.md (maintenance and updates) | None |

Summary: 21 checked, 10 confirmed, 5 corrected, 5 softened, 1 removed. Searches 6, PK 5.

## Totals
92 claims checked: 56 confirmed, 11 corrected, 17 softened, 3 removed (plus 5 sources swapped and 2 removed).
30 searches used. 4 claims were kept on the writer's official source without a search because the budget ran out
(Denver DEDO, SCORE Denver, Fort Collins Business Connectors, Seattle legal assistance). All are low-risk program
descriptions on .gov or .org pages.
