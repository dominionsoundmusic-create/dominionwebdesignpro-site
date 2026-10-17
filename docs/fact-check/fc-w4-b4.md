# Fact-check fc-w4-b4 (Wave 4), Oct 17 2026

Independent checker; wrote none of these pages. Pages: st-petersburg-fl, sarasota-fl, fort-myers-fl, new-orleans-la,
baton-rouge-la. Writer notes: docs/writers/w4-b6.md, docs/writers/w4-b7.md (including the follow-up writer sections).
Searches: 29 WebSearch calls (St. Pete 6, Sarasota 5, Fort Myers 6, New Orleans 6, Baton Rouge 6). "PK" = confirmed
from the checker's own knowledge (well-known geography or facts), not searched. "Src" = an official source is cited and
the claim is low risk, but it was not searched again because of the budget.
All photos opened and alt text compared with the image. Business claims compared with INTAKE.md.
Build: `python3 build.py --out /tmp/claude-0/fc-w4-b4/dist`; check.py `--skip-links --only` 0 errors, 0 warnings on all
five pages. Similarity after edits: highest pair 6.1% (st-petersburg-fl vs tallahassee-fl); all under 15%.

## /web-design/st-petersburg-fl.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Keep Saint Petersburg Local, nonprofit tied to AMIBA; runs Localtopia | Confirmed (search shows KSPL organizes Localtopia; AMIBA tie Src) | stpetecatalyst.com, stpeterising.com | Kept |
| Localtopia in Williams Park; 2026 edition Feb 14, 13th, 300+ vendors, one street added | Confirmed (search) | stpeterising.com, Chamber calendar | Kept |
| Population about 263,500 (2023 estimate) | Confirmed (search: QuickFacts V2023 263,553; V2024 shows NA) | census.gov | Kept |
| EDGE District: shopping, dining, nightlife on Central just west of downtown | Confirmed (PK, sources cited) | Visit St. Pete/Clearwater, Partnership | Kept |
| Grand Central: breweries, vintage shops, galleries, wellness studios | Softened (search found no named mix; writer's source was a commercial listing) | PK | Now "locally owned shops, eateries and studios" |
| Warehouse Arts District, former industrial area, rough street bounds | Confirmed (Src, city art districts page) | stpete.org | Kept |
| SHINE: St. Pete Arts Alliance, nearly 170 murals since 2015, 11th year Nov 2025, 19 new | Confirmed (search) | Arts Alliance, Tampa Bay Times | Kept |
| Second Saturday ArtWalk in "seven districts" incl. Deuces Live and the Edge, 5 to 9 p.m. monthly | Softened (search: 5 to 9 confirmed; district count differs, Arts Alliance flyers list six without EDGE) | stpeteartsalliance.org | Count removed; names Grand Central and Warehouse Arts only |
| Downtown parking often metered or time-limited | Confirmed (Src) | St. Pete Catalyst | Kept |
| Google local ranking: relevance, distance, prominence | Confirmed (PK, Google help page) | support.google.com | Kept |
| Greenhouse: City and Chamber partnership since 2013, business assistance center | Confirmed (search, Patch 2013) | stpetegreenhouse.com, Crow's Nest | Kept |
| Greenhouse staff "called Navigators"; runs Storefront Conservation Corridor Program and SBE program | Softened (search could not confirm Navigators; the Storefront Corridor item appears as a plan, status unclear) | | Now "one-on-one guidance and workshops and connects owners with city business programs" |
| FSBDC at Pinellas County through PCED, office at USF St. Petersburg on 7th Ave S | Corrected (search: a satellite office at 140 7th Ave S; main office in Clearwater; "USF region" wording dropped) | pced.org, sbdctampabay.com | Now "satellite office on the USF St. Petersburg campus"; "free, confidential consulting" |
| Hero swap: the city photo shows the historic Pinellas County Courthouse, which is in Clearwater | Confirmed (PK) | | Swap stands; do not reuse that photo as St. Pete |
| Alt text (4 images) | Confirmed | opened each file | Kept |
| Business claims (prices, trials, 7 to 14 days, waves, AI receptionist, no office) | Confirmed against INTAKE.md | | Kept |

Summary: 17 checked, 12 confirmed, 1 corrected, 3 softened, 0 removed (wording only; one fact detail removed inside a softening). By search 8, PK 4, Src 5.

## /web-design/sarasota-fl.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| County 38.8% aged 65+ in 2025 (Census via Sarasota Magazine) | Confirmed (search) | sarasotamagazine.com Sept 2026 | Kept |
| County median age 57.8 in 2025 | Removed (search could not confirm) | | Deleted |
| "First among counties of 250,000+ on both measures"; H2 "oldest large county in the country" | Softened (not confirmed for 2025; older rankings conflict) | | H2 now "...when more than a third of the county is over 65"; ranking sentence deleted |
| City 29.3% aged 65+ "in the 2023 estimate" | Corrected (search: QuickFacts shows 29.3%, an ACS-based value carried across vintages) | census.gov | Now "29.3% in the Census Bureau's QuickFacts figures" |
| Lakewood Ranch top-selling multigenerational MPC 8 straight years (RCLCO) | Confirmed (search) | Sarasota Magazine, Observer | Kept |
| Lakewood Ranch No. 2 overall in 2025 behind The Villages | Confirmed (search, RCLCO 2025 PDF) | Sarasota Magazine Jan 2026 | Kept |
| 1,064 new-home contracts first half 2026; Wellen Park No. 3 with 727 | Confirmed (search; Observer gives 1,035 in a sub-category, overall 1,064 widely cited) | Sarasota Magazine July 2026 | Kept |
| Lakewood Ranch "east of the city" and implied to be a Sarasota County community | Corrected (PK: it straddles the Manatee and Sarasota county line, most of it in Manatee) | | Added "straddling the Manatee and Sarasota county line" |
| "Wellen Park, another Sarasota County community" | Corrected (PK) | | Now "in south Sarasota County near Venice" |
| Florida SBDC at USF: no-cost face-to-face consulting in Sarasota and Manatee | Confirmed (search; sessions at the Greater Sarasota Chamber, Fruitville Rd) | sbdctampabay.com | Kept |
| Place names Main Street, St. Armands Circle, Siesta Key, Gulf Gate, Venice | Confirmed (PK) | | Kept |
| Google local ranking | Confirmed (PK) | Google help | Kept |
| Vet photo alt: "a vet walking one on a leash" | Corrected (photo shows the vet standing among the dogs) | opened file | Alt fixed |
| Other 3 alts | Confirmed | opened files | Kept |
| Business claims; "custom software not in packages" | Confirmed against INTAKE.md | | Kept |
| Sources: county QuickFacts (no claim rests on it now) and South Florida Agent Magazine (weak, duplicated) | Removed | | Deleted from m.sources |

Summary: 16 checked, 9 confirmed, 4 corrected, 1 softened, 2 removed (median age; two unused/weak sources counted as one item). By search 7, PK 5, file/INTAKE 4.

## /web-design/fort-myers-fl.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| SWFL marked 100 years of MLB spring training in 2025 | Confirmed (Src, WINK; search result listed it) | winknews.com | Kept |
| Red Sox at JetBlue Park since 2012, Fenway dimensions, Green Monster, about 11,000 seats | Confirmed (PK) | Visit Fort Myers, Stadium Journey | Kept |
| Hammond Stadium in Lee Health Sports Complex seats 9,900 | Corrected (search: Lee County lists 9,300) | leefl.gov | Now "which Lee County lists at 9,300 seats"; Lee County complex page added |
| Parks "about six miles apart" | Softened (not verified) | | Now "a short drive apart" |
| Schedules and ticket prices released mid-November | Confirmed (Src, Lee County) | leegov.com | Kept |
| 2018 study: $68.9M non-resident spending, $56.7M outside ballparks, 41% baseball sole reason | Confirmed (search: news coverage of the DPA study) | Lee County PDF, Fort Myers Beach Talk (added) | Kept; "last full study" changed to "most recent study" (WINK 2025: still the latest) |
| Cape Coral 400+ miles of navigable waterways | Confirmed (PK, city page) | capecoral.gov | Kept |
| Stormwater manager: 409 miles, 222 salt, 156 fresh | Removed (weak AOL syndication; numbers do not add up) | | Deleted; AOL source removed |
| Cape Coral 233,025 and Fort Myers 99,918 (2024) | Softened (search could not confirm city figures; 2020 Census 194,016 vs 86,395 supports the ratio, PK) | citypopulation.de | Now "well over 200,000 residents ... roughly twice the size of Fort Myers"; USAFacts county source removed |
| Cape Coral largest city in Lee County | Confirmed (PK) | | Kept |
| Art Walk first Friday, hosted by River District Alliance, named streets, First Street closed | Softened (sources old; host and closure not confirmed) | artswfl.com | Now "a free Art Walk opens galleries and shops downtown" on first Friday evenings; Gulfshore Life RDA source removed |
| Edison and Ford Winter Estates, 2350 McGregor, about 20 acres, public since 1947, 200,000+ visitors | Corrected (search: "more than 20 acres"; Mina Edison gave it to the city in 1947 but public opening is given as 1947 or 1950; 200,000+ confirmed) | Wikipedia, Captiva Sanibel (added) | Reworded to the gift in 1947, no opening year |
| Estero village Dec 31, 2014; 36,939 in 2020 | Confirmed (search) | Wikipedia, citypopulation | Kept |
| Hurricane Ian Cat 4 landfall near Cayo Costa Sept 28, 2022 | Confirmed (PK) | Sarasota Magazine, Moody's | Kept |
| Florida SBDC at FGCU: statewide network "which FGCU hosts" | Corrected (search: the Florida SBDC Network is headquartered at the University of West Florida; FGCU campus is the SWFL regional HQ) | sbdc.fgcu.edu (location page added) | Fixed |
| Lee County EDO office "on Second Street downtown" | Softened (only a directory listing as source) | | Street dropped; services and Procurement registration kept (Src) |
| Greater Fort Myers Chamber, Edwards Drive downtown | Confirmed (Src, chamber's own page) | fortmyers.org | Kept |
| SCORE Southwest Florida in Fort Myers, lists SBDC as partner | Confirmed (Src) | score.org | Kept |
| Google local ranking | Confirmed (PK) | Google | Kept |
| Alt text (4 images) | Confirmed | opened files | Kept |
| Business claims | Confirmed against INTAKE.md | | Kept |

Summary: 21 checked, 11 confirmed, 4 corrected, 5 softened, 1 removed. By search 9, PK 6, Src 6.

## /web-design/new-orleans-la.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| City and Orleans Parish share a boundary; about 362,000 July 2025 | Confirmed (search: QuickFacts V2025 362,154) | Data Center; QuickFacts (URL changed to the parish page that shows the number) | Kept |
| Magazine Street about six miles, Canal to Audubon Park, CBD, Garden District, Uptown | Confirmed (PK, tourism site) | neworleans.com | Kept |
| 69,400 leisure and hospitality jobs Dec 2025 (NSA); 58,800 accommodation and food | Confirmed (search) | FRED | Kept |
| About 478,000 nonfarm Dec 2025; "about one job in seven" | Confirmed (search: 478.3k preliminary NSA; 14.5%) | BLS | Kept |
| Annual average 69,000 in 2024, about 53,900 in 2020 | Confirmed (Src, FRED annual series) | FRED | Kept |
| Carnival opens Twelfth Night Jan 6; Mardi Gras Tuesday Feb 9, 2027 | Confirmed (PK; Easter 2027 is March 28) | Hoodline | Kept |
| Jazz Fest 2027 Fair Grounds, April 22 to 25 and April 29 to May 2; lineup usually around December | Confirmed (search, festival FAQ) | neworleans.com, nojazzfest.com (added) | Kept |
| Freret: National Trust Main Street adoption 2001; by 2011 Napoleon to Jefferson called newest restaurant row | Confirmed (search) | Wikipedia, WWNO | Kept |
| Google local ranking | Confirmed (PK) | Google | Kept |
| LSBDC hosted statewide by LSU, ten regional offices | Confirmed (search for LSU host; regional count Src) | lsu.edu | Kept |
| GNO region hosted by Xavier; seven parishes listed | Confirmed (search) | xula.edu, LSU | Kept |
| GNO office on North Causeway in Metairie | Confirmed (Src, Opportunity Louisiana) | opportunitylouisiana.gov | Kept |
| New Orleans Chamber founded 2004; networking, education, advocacy; Women's Business Alliance | Confirmed (PK/Src) | bizneworleans.com | Kept |
| Office of Supplier Diversity, SLDBE, race and gender neutral, online application, public directory | Confirmed (Src, nola.gov) | nola.gov | Kept |
| Propeller 2025 Growth Accelerator for 15 "May to July"; Startup Bootcamp "Sept to Nov"; Financial Wellness Collaborative with Thrive New Orleans and Fund 17 | Softened (search: 15 ventures and the collaborative confirmed; program months conflict, press release says 5 months) | bizneworleans.com, gopropeller.org | Months removed |
| "Most have a website set up once by a cousin" | Softened (unsupported generalization) | | Now "plenty have a website that was set up once and never touched again" |
| Neighborhood names, Metairie in Jefferson, Northshore as St. Tammany | Confirmed (PK) | | Kept |
| Freret kitchen labeled as made-up example | Confirmed | | Kept |
| Alt text (3 in-body, fallback hero; planned hero alt matches its Artistly prompt) | Confirmed | opened files | Kept |
| Business claims | Confirmed against INTAKE.md | | Kept |

Summary: 20 checked, 18 confirmed, 0 corrected, 2 softened, 0 removed. By search 8, PK 6, Src 6.

## /web-design/baton-rouge-la.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Tiger Stadium capacity 102,321 incl. media, game management, concessions | Confirmed (PK) | WAFB | Kept |
| ExxonMobil Baton Rouge refinery about 540,000 bbl/day as of 2020, one of the largest in the US | Confirmed (search: 540,000 input capacity as of Jan 2020; described as fifth largest) | Wikipedia | Kept |
| 2017 House resolution: more than six thousand employees and contractors | Confirmed (Src; search shows about 6,300 workers incl. contractors on Wikipedia, consistent) | legis.la.gov | Kept |
| About 77,000 government jobs, Baton Rouge MSA, 2025 | Confirmed (Src, FRED series) | FRED | Kept |
| EBR Parish about 456,000 July 2025; consolidated city-parish government | Confirmed (search: QuickFacts 456,180; consolidation PK) | census.gov | Kept |
| Bocage and Tara in Mid City South; Southdowns between Perkins Road and Bayou Duplantier; Oak Hills Place on Highland Road south of Mall of Louisiana | Confirmed (PK, Wikipedia) | Wikipedia | Kept |
| Perkins Road Overpass restaurants, nightlife, walkable; Perkins Rowe mixed-use | Confirmed (PK) | | Kept; weak PODS marketing source removed |
| Zachary north, Prairieville in Ascension, Denham Springs in Livingston | Confirmed (PK) | | Kept |
| LSBDC at Southern University, Harding Blvd, no-cost confidential consulting, seven parishes | Confirmed (search: 616 Harding Blvd; parishes match) | louisianasbdc.org (locations page added) | Kept |
| LSU statewide host at Innovation Park; technology-focused LSBDC at LSU | Confirmed (Src, LSU news) | lsu.edu | Kept |
| BRAC regional economic development org since 2006, nine parishes incl. Ascension, Livingston, Pointe Coupee, St. Helena | Confirmed (search) | Entergy | Kept |
| Build EBR Front Door Refresh, July 2026, up to $10,000, Plank Road between N 22nd St and Clayton St | Confirmed (search) | WAFB | Kept |
| SBA 2025: 511,235 small businesses, 99.5%, 54.1% of employees | Softened (search: 511,235 may be the all-business count; 2024 profile says 99.5% and 54.5%; 2025 shares not confirmed) | SBA 2025 and 2024 profiles (2024 added) | Now "more than 99% of the state's businesses ... employ more than half of its workers" |
| "Updates are part of what you pay for, not an extra" | Corrected (INTAKE: hosting, maintenance and updates are $49/mo or included with the AI agent) | INTAKE.md | Now states the $49 plan |
| Hero: real Baton Rouge photo, Spanish Town Rd sign, LA Dept of Public Safety SUV, tower not named; credit line | Confirmed | opened file | Kept |
| Other alt text (3 images) | Confirmed | opened files | Kept |
| Other business claims | Confirmed against INTAKE.md | | Kept |

Summary: 17 checked, 15 confirmed, 1 corrected, 1 softened, 0 removed. By search 7, PK 5, Src 4, file/INTAKE 1.

## Could not settle
- JetBlue Park seat count (about 11,000) and the 2018 study's exact $68.9M were not seen in a primary document; both
  match widely repeated coverage and are kept.
- Greater Fort Myers Chamber address and SCORE chapter details rest on their own pages (not searched).
