# Fact-check fc-w4-b5 (Wave 4, Oct 17 2026)

Independent checker (wrote none of these pages). Pages: shreveport-la, birmingham-al, mobile-al, jackson-ms, knoxville-tn.
Method: 30 WebSearch calls (6 per page), spent on numbers, dates, program names and weak sources. Well-known geography and
history confirmed from own knowledge are marked PK. Unverified specific numbers were softened or removed. No WebFetch.
All images opened (contact sheets); every alt matches what the photo shows, and only the real city photos (mobile-al,
knoxville-tn) name the city. Business claims (prices, trials, AI receptionist, no office, no ranking promise) match INTAKE.md
on all five pages.
Build: `python3 build.py --out /tmp/claude-0/fc-w4-b5/dist`; check.py --skip-links --only on each page: 0 errors, 0 warnings.
Similarity after edits: highest pairs 5.7% (knoxville-tn vs memphis-tn; birmingham-al vs jackson-ms), 5.3% (jackson-ms vs mobile-al).
No em or en dashes; m.no_office once per page; FAQ counts unchanged (5 each).

## /web-design/shreveport-la.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Shreveport about 175,900 (July 2025) vs 187,500 (April 2020) | Confirmed (search; KEEL reading of Census) | 710keel.com | Kept |
| Caddo Parish down about 1,100 in 2024 to 2025 | Confirmed by writer source (search shows the Advocate article) | shreveportbossieradvocate.com | Kept |
| Metro about 383,000 | Confirmed (search) | FRED SHPPOP | Kept |
| Barksdale workforce "more than 8,500" | Corrected (search): current fact sheet says nearly 9,000 active duty, reserve and civilians | barksdale.af.mil fact sheet | Text and source updated; Wikipedia source dropped |
| 2nd Bomb Wing flies B-52H | Confirmed (PK, fact sheet) | barksdale.af.mil | Kept |
| Willis-Knighton more than 7,000 employees, largest nongovernmental employer | Confirmed as its own claim (search); page already says "says" | KEEL | Kept |
| Ochsner LSU Health Shreveport is a partnership of Ochsner Health and LSU Health Shreveport | Confirmed (PK) | weak Cause IQ directory removed | Source removed, claim kept |
| Five riverboat casinos reported revenue in late 2024 | Softened: not verified | n/a | Now "riverboat casinos have drawn visitors to both banks since the 1990s" |
| Live! Casino opened Feb 2025, first land-based casino, 550-room hotel | Confirmed (search; opened Feb 13 2025; Cordish says 550 rooms, local reports 549) | cordish.com, Red River Radio | "a hotel of about 550 rooms"; Cordish source added |
| Highland historic neighborhood; Line Avenue shops, dining, antiques | Confirmed (PK, Forum News) | theforumnews.com | Kept; Marriott travel page removed as weak |
| Youree Drive "one of the busiest retail roads" | Softened (only source was a property listing) | listing removed | "a major retail road lined with shopping centers" (PK) |
| Bossier Strip on East Texas Street, 1940s to 1970s, airmen | Confirmed (PK, Wikipedia) | Wikipedia | Kept |
| Strip faded after casinos came "in the early 1990s" | Corrected (PK): Shreveport-Bossier riverboats opened mid-1990s | n/a | "its heyday ended long before riverboat casinos arrived in the 1990s"; "light industry" line cut |
| LSBDC Northwest Louisiana at SUSLA, Hilry Huckaby Ave, parish list incl. Claiborne | Corrected (search): LSBDC and SUSLA pages disagree (Claiborne vs Lincoln) | louisianasbdc.org | Now "across northwest Louisiana, including Caddo, Bossier, De Soto, Red River, Bienville and Webster" |
| Greater Shreveport Chamber founded 1910, Edwards St | Confirmed (search) | shreveportchamber.org/history | History page added as source |
| Chamber over 1,100 members | Softened (search: 2023 figure, other figures exist) | lsus.edu (2023) | "has reported more than 1,100"; LSUS source added |
| Bossier Chamber more than 800 members | Removed (not verified) | n/a | Count cut; Benton Road, diplomats, SkillBridge kept on writer's official source |
| Big Sandy "roughly 85 miles west of the Shreveport airport" | Softened (source was airport.guide, weak) | removed | "roughly an hour and a half west of Shreveport by road" and "an easy drive west along Interstate 20" (PK) |
| Google local ranking: relevance, distance, prominence | Confirmed (PK, Google help page) | support.google.com | Kept |
| Business claims (prices, trials, online store not included) | Confirmed against INTAKE.md | INTAKE.md | Kept |

Summary shreveport-la: 20 checked, 10 confirmed, 4 corrected, 5 softened, 1 removed (search 10, PK 10).

## /web-design/birmingham-al.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Sloss Furnaces pig iron 1882 to 1971; saved; National Historic Landmark; museum, metal arts, concerts | Confirmed (PK) | Wikipedia, Bhamwiki | Kept |
| UAB some 28,000 employees across university and hospital | Confirmed (search; UAB toolkit and 2023 UAB news) | uab.edu | Kept |
| UAB 2022 impact $12.1B, 107,600 jobs, 1 in 20 | Confirmed (writer sources UAB News and Business Alabama; PK) | uab.edu | Kept |
| Avondale/Lakeview revitalization; 41st Street early Complete Streets project | Not re-searched; writer sources are local news and REV Birmingham (reputable) | abc3340, revbirmingham.org | Kept |
| Park at Wood Station, first new housing in Woodlawn in more than 50 years | Confirmed (search) | businessalabama.com | Kept |
| Over the Mountain suburbs and their newspaper | Confirmed (PK) | otmj.com | Kept |
| Alabama 449,000 small businesses, 99.4%, 46.7% "from SBA Advocacy's 2025 profiles" | Corrected (search): figures come from the SBA statement in Gov. Ivey's May 2025 proclamation, released before the June 2025 profiles | governor.alabama.gov | Attribution reworded; governor release added; 2025 profiles link removed |
| Innovation Depot opened 2007 in former downtown Sears building, about 140,000 sq ft, works with UAB | Confirmed (search for 2007/Sears/downtown; size PK) | VentureBeat, Business Alabama | Kept |
| Greater Birmingham SBDC at Innovation Depot, 1500 1st Ave N; network hosted by University of Alabama; free confidential advising | Confirmed (search) | asbdc.org | Kept |
| UAB SBDC closed 2008 | Softened (only Bhamwiki) | Bhamwiki | "UAB once ran its own center" |
| BBA "missing middle" 6 to 99 employees | Confirmed (search, BBA page) | businessalabama.com, BBA | Kept |
| 12-week intensive "called Supplier Scale" | Corrected (search): began 2022 as Supplier Scale, now the Small Business Intensive, for Jefferson County firms; not the missing-middle program | Business Alabama, Bham Now | Rewritten; two sources added |
| Match for Impact: 16 businesses, at least $40,000 in services, with Innovate Alabama, 2026 | Confirmed (search; awarded January 2026) | BBA, Bham Now | "In January 2026"; Bham Now source added |
| Small Business Week 2026 ran May 3 to 9 | Removed (search found no 2026 source) | n/a | Panel deleted; grid changed to grid-3 |
| Business claims, AI receptionist, no office | Confirmed against INTAKE.md | INTAKE.md | Kept |

Summary birmingham-al: 15 checked, 10 confirmed, 2 corrected, 1 softened, 1 removed, 1 kept on writer source without re-search (search 8, PK 7).

## /web-design/mobile-al.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Austal USA in Mobile since 1999; built LCS USS Independence | Confirmed (PK) | Area Development | Kept |
| Airbus picked Brookley in 2012 for A320 family line; A220 line opened May 2020 | Confirmed (search for 2020 line; 2012 PK) | Wikipedia, Made in Alabama | Kept |
| 100th Mobile-built A220 delivered in 2025 | Confirmed (search: July 15 2025, to Breeze Airways) | madeinalabama.com | "In July 2025" |
| More than 1,600 people on site as of 2023 | Removed (search found no confirmation) | n/a | Cut; 2023 Made in Alabama source removed |
| Port of Mobile $89.1B economic value in 2024, one in seven jobs (Alabama Port Authority) | Confirmed, single secondary source (search) | southalabama.edu | "has estimated", "about one in seven"; Business Alabama link (did not carry the figure) replaced |
| $131M container berth, construction expected 2026 | Confirmed (search; with APM Terminals, work slated to start 2026) | Baird Maritime, Supply Chain 24/7 | Kept, wording tightened; Baird added |
| LoDa walkable district; second Friday Artwalk | Confirmed (PK) | mobile.org | Kept |
| Old Dauphin Way largest historic district, 766 acres | Confirmed (PK, Wikipedia) | Wikipedia | Kept |
| Shoppes at Bel Air (former Bel Air Mall) on Airport Blvd | Confirmed (PK) | AARoads | Kept |
| Mardi Gras "oldest verified organized ... dating to 1703" per city government | Confirmed (PK; attributed claim) | Wikipedia, mobile.org | Kept |
| Eastern Shore Chamber: Daphne, Fairhope, Spanish Fort; Fairhope Ave office; began 1924 as Fairhope Chamber; HR290 2024 centennial | Confirmed (search) | HR290, eschamber.com | Kept |
| Alabama SBDC South Alabama hosted by Univ. of South Alabama, free confidential advising, six-county area | Confirmed (search) | asbdc.org | Kept |
| Mobile Chamber navigator free, membership not required; nine-week Minority Business Accelerator | Confirmed (search) | mobilechamber.com | Kept |
| StatCounter June 2026: phones about 40%, desktops about 60% | Softened (not verified; monthly figure) | StatCounter | Numbers removed; FAQ now says StatCounter shows both with a large share |
| Google mobile-first indexing complete Oct 2023 | Confirmed (PK) | Google Search Central | Kept |
| Business claims, AI receptionist | Confirmed against INTAKE.md | INTAKE.md | Kept |

Summary mobile-al: 16 checked, 12 confirmed, 2 corrected (Port attribution/source, 100th A220 date precision), 1 softened, 1 removed (search 8, PK 8).

## /web-design/jackson-ms.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Boil water notice from July 29 2022; O.B. Curtis on backup pumps; Pearl River flooding late August | Confirmed (PK, writer sources) | Wikipedia, Mississippi Today | Kept |
| Officials announced failure Aug 29; governor declared emergency "the next day" | Corrected (search): Gov. Reeves declared the emergency on the night of Aug 29 | Boston Globe/AP, CNBC | Rewritten; AP source added |
| About 600 National Guard members | Removed number (search did not confirm) | WDAM | "the Mississippi National Guard was called in" |
| Restaurant association: many of about 500 area restaurants had water problems; ice from other towns | Confirmed (search; NPR) | KPBS/NPR | Kept |
| "Thousands of dollars a week" in extra costs | Corrected (search): one manager estimated up to $2,500 a week | Mississippi Today | Rewritten; source added |
| Fondren restaurant cited water when it closed fall 2022 | Confirmed by writer source (WTOK) | wtok.com | Kept |
| Federal judge put interim third-party manager in charge Nov 2022; now JXN Water | Confirmed (PK: Ted Henifin, Nov 29 2022) | Mississippi Free Press, WLBT | Kept |
| Fondren First Thursday, North State Street | Confirmed (PK, Visit Jackson) | visitjackson.com | Kept |
| Belhaven near Fondren and downtown | Confirmed (PK) | belhaven.edu | Kept |
| Farish Street: 1870s/1880s, Black business center, Trumpet Records, NRHP 1980 | Confirmed (PK) | Wikipedia, Ole Miss, Mississippi Today | Kept |
| JSU founded 1877 as Natchez Seminary, moved to Jackson, John R. Lynch St | Confirmed (PK) | Britannica | Kept |
| Ridgeland, Madison in Madison County; Brandon, Flowood in Rankin County | Confirmed (PK) | Niche, Redfin (weak, low-risk geography) | Kept |
| SBA 2025 MS profile: 294,768, 99.4%, 444,113, 47% | Confirmed (search) | advocacy.sba.gov | Kept |
| JSU SBDC, 1400 John R. Lynch St | Confirmed (PK, JSU page) | jsums.edu | Kept |
| MSBDC City of Jackson center, 200 S President St, weekdays | Confirmed, dated (search: opened Dec 2019) | news.olemiss.edu | "opened ... in 2019"; call-ahead kept |
| SBA Mississippi District Office, 210 E Capitol St | Confirmed (PK) | sba.gov | Kept |
| Greater Jackson Chamber Partnership as umbrella of Jackson Chamber and Greater Jackson Alliance, members sole props to largest | Softened (2010 source; current structure unverified; partnership confirmed active in 2026) | WLBT 2026 | Described as the metro's chamber and economic development group; 2010 Jackson Free Press source replaced |
| Business claims, AI receptionist, no office | Confirmed against INTAKE.md | INTAKE.md | Kept |

Summary jackson-ms: 18 checked, 13 confirmed, 3 corrected (emergency date, cost figure, MSBDC date), 1 softened, 1 removed (search 6, PK 12).

## /web-design/knoxville-tn.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| GSMNP about 11.5M visits 2025, most of any national park, more than twice Zion (second) | Confirmed (search; 11,527,939 vs Zion 4,984,525) | National Parks Traveler | Weak sources (More Than Just Parks, PlanetWare) replaced |
| Sevier County 2024 visitor spending about $3.93B, third of 95 counties | Confirmed (search) | WATE, Mountain Press | Kept |
| Tennessee 147M visitors, $31.66B direct spending 2024 | Confirmed (search) | WATE, Mountain Press | Kept |
| Market Square "laid out" 1854 for farmers; NRHP 1984; Chalk Walk in spring | Confirmed (search: land donated 1854; listed Dec 20 1984; Chalk Walk each April) | Wikipedia, APA | "Donated to the city in 1854"; APA source added |
| Immigrant shopkeepers (German, Swiss, Jewish, Greek) | Confirmed (PK, Wikipedia) | Wikipedia | Kept |
| Gay Street main street since 1790s; 1919 viaduct raised the street | Confirmed (PK) | Wikipedia | Kept |
| Old City nightlife and live music | Confirmed (PK) | visitknoxville.com | Kept |
| South Loop "connects more than 60 miles of trails" | Corrected (search): 60+ miles is the wider Urban Wilderness; South Loop system is about 42 miles; City is a partner | knoxvilletn.gov, legacyparks.org | Rewritten; two Legacy Parks sources added |
| ORNL largest science and energy lab in DOE system | Confirmed (PK; ORNL's own description) | Wikipedia | Kept |
| UT and ORNL long partnership | Confirmed (PK) | tennessee.edu | Kept |
| TSBDC Knoxville hosted by Pellissippi State, by appointment, 865-246-2663 | Confirmed (search) | tsbdc.org | Kept |
| SBDC worked with 420 clients in 2024 | Removed (search found no figure) | n/a | Sentence and Knox TN Today source cut |
| Chamber small business page lists TSBDC, KEC, SCORE, Smart Start | Confirmed by writer source (official chamber page) | knoxvillechamber.com | Kept |
| Chamber operates county business parks (Eastbridge, Hardin, Karns Valley, Pellissippi Corporate Center) | Confirmed (search: "maintains and operates existing business parks") | knoxvillechamber.com | Wording aligned |
| Hero: 1886 Knox County Courthouse with Andrew Johnson Building behind | Confirmed (PK; photo opened, matches) | VoiceMap | Kept |
| Business claims, AI receptionist, no office | Confirmed against INTAKE.md | INTAKE.md | Kept |

Summary knoxville-tn: 16 checked, 13 confirmed, 2 corrected (South Loop miles, Market Square wording), 0 softened, 1 removed (search 8, PK 8).

## Not settled
- Bossier Chamber details beyond the address and programs (member count cut), and the exact LSBDC Northwest parish list (two official pages disagree).
- Port of Mobile $89.1B rests on one University of South Alabama page that cites the Port Authority; no Port Authority release found.
- StatCounter monthly split not checked, so the page no longer gives numbers.
