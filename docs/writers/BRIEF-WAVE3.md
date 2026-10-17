# Writer brief: Wave 3 national city pages (Oct 17 2026)

Read first, in full: `CLAUDE.md`, `CITY-PAGES-WAVE3.md`, `INTAKE.md`, `docs/WRITING-GUIDE.md` (every
rule there applies), `docs/writers/BRIEF-WAVE2.md` (same rules as Wave 2; only the cities differ),
then the model pages `src/pages/web-design/st-louis-mo.html` and `src/pages/web-design/miami-fl.html`.
Your pages use the same front matter shape, templates, macros and image handling. INTAKE.md wins
over everything.

## Your files
- `src/pages/web-design/<slug>.html` for each assigned city (flat URL: `url: "/web-design/<slug>.html"`,
  `type: area`, `city_name`, `state_name`, `crumb: "City, ST"`, `summary:` max 160 chars, `schema_service`).
- `docs/writers/w3-<your-batch>.md`: per page, the main and supporting keywords used, every fact
  stated with its source URL, and what you left out because you could not verify it.
- Do NOT edit shared files (build.py, templates, static, site.json, scripts, SERVICES.md,
  docs/keyword-plan.md, other writers' pages, any existing city page). The 8 cities are already in
  site.json, group `other-us`, so `m.area_pills(group='other-us', exclude='<slug>')` and
  `area:<slug>` links work.

## Keyword rules
The main target goes in the title (50 to 65 characters), the H1, the first paragraph and one H2.
Supporting terms go in naturally (an H2 or H3, body copy, the description); the Question-type rows
become FAQ questions where they read like real questions. Never stuff. Never use another agency's
brand name (for example "creative813").

## Honesty rules (the ones that matter most here)
- Dominion Web Design Pro is Maurice Johnson in Big Sandy, East Texas, building remotely. No office,
  no team, no clients in the city. Use `{{ m.no_office('City') }}` exactly once. Never say Maurice
  has built for any business there. No reviews, ratings, awards, job counts, years, guarantees,
  ranking promises. Never "certified", "top-rated", "#1", "unlimited", "guarantee" in any form,
  "testimonial", "5-star", "our clients", "happy clients".
- Prices exactly: Starter $497, Pro $997, Agency $1,997, one time. Starter is live in 7 to 14 days;
  Agency pages arrive in waves, the first live inside two weeks. Pro chat widget free 14 days then
  $297/mo. Agency AI phone agent SETUP; the agent is free for 7 days then $297/mo for up to 750
  minutes, cancel any time, not part of the one-time price. Hosting, maintenance and updates included
  while the client keeps the AI agent, otherwise $49/mo. Use `{{ m.pricing_cards() }}` if you show
  the packages as cards (optional on a city page). Keep the "we do not sell page counts" idea if
  you discuss page counts.
- Phone: (903) 636-7511 is answered by an AI receptionist any hour that can transfer callers to
  Maurice. Never say a person always answers.
- No em dashes or en dashes anywhere. No eyebrow labels. American spelling. No banned phrases.
- The template adds the `dwdp:handwritten` mark; do not add it yourself.

## Make every page different (limit 15% Jaccard on 5-word shingles, against ALL 52 city pages)
Each city has an assigned ANGLE below. Build the outline around it. Do not copy any section shape
from another city page: no "Four reasons a X business would hire..." grid, no "questions worth
asking" table, no "Help that already exists for X owners" or "Free help for X small businesses"
heading reused, no "How our packages map to X" list copied from St. Louis. The remote / East Texas
disclosure is `m.no_office('City')` plus at most one or two fresh sentences of your own. "Getting
started" is at most one short line plus `m.demo_box('a fresh sentence')`. Write every heading and
paragraph fresh; vary your phrasing between your two cities too. Aim for 1,300 to 1,900 words of
your own copy per page.

## Research and sources
Research each city with WebSearch before writing (WebFetch may be blocked; verify from search
results of the official or credible source). Budget about 8 to 10 searches per city. State only
facts you verified, and cite each in `m.sources([...])` with a real URL that supports it. Cover: the
city's small business makeup (kinds of owner-run businesses common there), real neighborhoods,
corridors or suburbs a resident would recognize, its chamber of commerce and small business
resources (SBDC, SCORE chapter, city small business office), and why local search matters there.
When citing Google on local ranking use https://support.google.com/business/answer/7091?hl=en
(relevance, distance, prominence). Keep numbers to ones you can source (Census QuickFacts, SBA Office
of Advocacy 2024 or 2025 state profiles, city or chamber pages). If you cannot verify it, leave it out.

## Images (no new in-body images; one new hero per city)
- Hero front matter:
  ```yaml
  hero:
    image: images/heroes/<slug>-hero.jpg
    alt: "<describes the planned photo; never claims a real landmark>"
    desc: "Artistly scene: <bright scene of a real small business owner's setting typical of that city, no readable signs, no text, no logos, no recognizable faces, no real landmarks presented as fact>, wide cinematic landscape shot, subject positioned on right third of frame, well lit"
    fallback: <assigned fallback below>
    fallback_alt: "<accurate alt of the fallback photo; must NOT say it is in the city>"
    position: "65% 50%"
    lead: "One or two short sentences."
  ```
- In-body: use the assigned existing photos (at least two, all three if they fit) with
  `{{ img("path", "alt", w, h) }}`. Open each image with the Read tool first (files are in
  src/static/) and write alt text that describes what is really in it. Never write alt text that
  claims a photo shows the city. Sizes: demo-images 1344x768, images/body 1200x800.

## Check before you report
```
python3 build.py --out /tmp/claude-0/w3-<batch>/dist
python3 scripts/check.py --skip-links --dist /tmp/claude-0/w3-<batch>/dist --only /web-design/<slug>.html
python3 scripts/similarity.py --dist /tmp/claude-0/w3-<batch>/dist
```
Fix every ERROR. In the similarity output look at every pair that involves your pages and keep each
at or under 15% (aim for under 8%; other writers are writing at the same time, re-run at the end).
Do not touch git. Report: pages, word counts, highest similarity pair per page, searches used,
anything unverified.

## The 8 cities

Keyword numbers verified from keywords/Web-Design-Wave3-Cities-Keywords.xlsx (city tabs) and the
ALL tab of keywords/Web-Design-Keywords.xlsx ("original"). Volume is searches a month, SD is SEO difficulty.

### new-york-ny (batch A)
- Main: website design company new york (3,600, SD 12, original). Supporting: new york web design
  company (2,400, SD 47); website design new york (1,900, SD 44); web design new york city (1,900,
  SD 48); web design new york (1,600, SD 40); web design company in new york (260, SD 40); website
  design in new york (2,900); web design new york ny (390); website design company nyc (1,300,
  original); web design nyc (260, original); small business web design new york (20); affordable /
  cheap web design new york (30 / 50); custom web design new york (50); law firm web design new york (10).
- Angle: five boroughs, five markets. Customers search by borough and neighborhood (Astoria,
  Flushing, Jackson Heights, Bushwick, Park Slope, Harlem, Washington Heights, the Bronx's Arthur
  Avenue, Staten Island's North Shore), and the city's storefront corridors are run through a large
  network of Business Improvement Districts and the Department of Small Business Services (NYC SBS,
  Business Solutions Centers). Second thread: New York is where a large share of the country's
  website accessibility (ADA) lawsuits are filed (verify from a credible annual report and cite
  it), so a small New York business site should be built to accessibility basics (alt text,
  contrast, keyboard use, readable forms). Say honestly what Dominion builds in and that it is not
  legal advice. Do not promise lawsuit protection.
- Fallback hero: images/heroes/website-designer-cost-hero.jpg
- Photos: demo-images/restaurant/2.jpg, demo-images/salon/3.jpg, demo-images/legal/3.jpg

### orange-county-ca (batch A)
- Main: orange county website design (1,900, SD 16). Supporting: orange county web design company
  (1,600, SD 16); web design orange county california (1,600, SD 29); web design orange county ca
  (1,300, SD 28); orange county website designers (480, SD 9); web design in orange county (1,600);
  web design orange county (140); orange county website design company (50); responsive web design
  orange county (10); website design companies orange county (1,900, original); web design company in
  orange county (1,600, original). NEVER "orange county ny".
- Angle: a county with 34 cities and no single downtown, where the customer names a city (Irvine,
  Anaheim, Santa Ana, Huntington Beach, Costa Mesa, Fullerton, Mission Viejo), and a home-service
  economy shaped by master-planned communities and HOAs (Irvine's villages, Mission Viejo, Rancho
  Santa Margarita, Ladera Ranch): trades that must explain HOA architectural approval, permits and
  scheduling on their sites. Little Saigon (Westminster and Garden Grove) as one real example of a
  community that searches in another language, briefly (Miami already covers bilingual sites; keep
  it to a paragraph). Resources: the Orange County SBDC network (verify host), SCORE Orange County,
  city chambers. Do NOT reuse the Los Angeles page's "88 cities" framing or wording.
- Fallback hero: images/heroes/pricing-hero.jpg
- Photos: demo-images/dental/1.jpg, demo-images/roofing/1.jpg, demo-images/real-estate/1.jpg

### tampa-fl (batch B)
- Main: web design tampa florida (1,600, SD 28). Supporting: website design company tampa (2,400,
  SD 35, original); web design company in tampa (2,400, SD 38); web design in tampa (2,900, SD 48);
  tampa web design company (210, SD 26); tampa web design agency (170, SD 36); web design company
  tampa (1,600, original); web design tampa (390); web design tampa bay (90); custom web design tampa
  (40); tampa bay web design firm (30); professional / responsive web design tampa (30 / 30). Never
  "creative813".
- Angle: storm season and a region split by the bay. After a hurricane (Helene and Milton in 2024;
  verify dates and local impact), customers check a business's website and Google profile to learn
  if it is open, so a Tampa site needs an easy way to post hours and closures, plus pages for the
  storm-repair trades (roofing, tree, water damage) that customers search urgently. Second thread:
  Tampa Bay is Tampa, St. Petersburg and Clearwater across the bridges, and Hillsborough, Pinellas and
  Pasco counties; customers search by city and neighborhood (Ybor City, Seminole Heights, South
  Tampa, Westshore, Brandon, Riverview, Wesley Chapel). Resources: Florida SBDC at USF, SCORE Tampa
  Bay, the City of Tampa's small business help, the Greater Tampa Chamber (verify names).
- Fallback hero: images/heroes/seo-web-design-hero.jpg
- Photos: demo-images/roofing/4.jpg, demo-images/plumbing/2.jpg, images/body/why-website-google-profile.jpg

### huntsville-al (batch B)
- Main: web design huntsville al (880, SD 29). Supporting: huntsville website design (210, SD 32).
  The other rows in the Huntsville tab are hosting questions; you may answer one as an FAQ if it
  reads naturally ("who is hosting my website" 210, "cheapest web design and hosting" 50), since
  hosting is part of the offer ($49/mo or included with the AI agent).
- Angle: the Rocket City's contractor and supplier economy. Redstone Arsenal, NASA's Marshall Space
  Flight Center and Cummings Research Park (verify its size claim) mean many small Huntsville firms
  sell to prime contractors or the federal government: they need a capability statement page, NAICS
  codes, SAM.gov registration and a clear "who we serve" page, written for a contracting officer who
  checks the website before calling. Explain what those are and how a buyer checks them; NEVER claim
  Dominion is a government contractor or holds any registration. Second thread: rapid growth
  (Huntsville became Alabama's most populous city; verify with Census) and suburbs such as Madison,
  Athens, Decatur, Hampton Cove; neighborhoods like Five Points, MidCity, downtown and Lowe Mill
  (verify). Resources: Alabama SBDC at UAH (and its procurement help, APEX Accelerator, verify),
  Huntsville/Madison County Chamber, SCORE North Alabama. Do not reuse Sacramento's state
  certification framing.
- Fallback hero: images/heroes/how-to-hire-a-web-designer-hero.jpg
- Photos: demo-images/electrical/3.jpg, demo-images/default/2.jpg, demo-images/insurance/2.jpg

### tucson-az (batch C)
- Main: web design company tucson (590, SD 7, original). Supporting: web design tucson az (590,
  SD 38); web design tucson arizona (720, SD 48); tucson website design (720, SD 55); web design in
  tucson (590); web design tucson (90); affordable web design tucson (10). Question row usable as an
  FAQ: web design rates (40).
- Angle: food and the budget-minded owner. Tucson was the first U.S. city named a UNESCO City of
  Gastronomy (verify year), so restaurants, food trucks, tortillerias, caterers and small producers
  are a big part of the owner-run economy; their sites need menus as text (not PDFs), hours, and
  catering pages. Second thread: "affordable web design tucson" is searched and Tucson incomes run
  below the national median (verify from Census QuickFacts), so a printed one-time price and what
  each package really includes matters. Places: Fourth Avenue, downtown, Barrio Viejo, Mercado
  District, Oracle Road, Speedway, Oro Valley, Marana, Sahuarita, Vail; the University of Arizona.
  Resources: Pima County / Tucson SBDC (verify host, likely Pima Community College), SCORE Southern
  Arizona, Tucson Metro Chamber, City of Tucson business help. Do not reuse the Phoenix page's
  service-area-trades angle.
- Fallback hero: images/heroes/website-cost-per-month-hero.jpg
- Photos: demo-images/auto-repair/3.jpg, demo-images/veterinary/3.jpg, demo-images/restaurant/4.jpg

### richmond-va (batch C)
- Main: richmond va web design (480, SD 14). Supporting: web design richmond va (590, SD 26); web
  design in richmond (590, SD 32); richmond website design (720, SD 52); richmond web design (880,
  SD 72); web design company richmond va (720, original); web design company richmond (170,
  original). Never "williamsburg va".
- Angle: makers, breweries and historic districts. Scott's Addition grew into a brewery, cidery and
  maker district (verify), Carytown is a long independent retail strip, Jackson Ward was a center of
  Black business life (Maggie L. Walker, first woman to charter a U.S. bank; verify) and the
  Manchester and Church Hill areas. Small producers need product and "where to buy" pages, event
  calendars and tasting room hours, not a giant online store. Second thread: the city is
  independent of the surrounding counties (Henrico, Chesterfield, Hanover), so customers in Short
  Pump or Midlothian may not say "Richmond"; keep this brief and word it fresh (the St. Louis page
  already leads with a city/county split, so it must NOT be the lead here). Resources: Virginia SBDC
  (Capital Region / Greater Richmond, verify), City of Richmond Office of Community Wealth Building or
  the economic development office (verify the real current name), ChamberRVA, SCORE Richmond.
- Fallback hero: images/heroes/web-design-packages-hero.jpg
- Photos: demo-images/photography/3.jpg, demo-images/default/3.jpg, demo-images/gym/2.jpg

### louisville-ky (batch D)
- Main: web design louisville (480, SD 20). Supporting: louisville web design (590, SD 26);
  louisville website design (880, SD 61); web design louisville ky (480, SD 47); ecommerce web design
  louisville (10); black web design louisville (10: link /black-owned-web-design/ where you mention
  that Dominion is Black-owned, per INTAKE section 7; never claim a certification). Question row
  usable as an FAQ: web design rates (40).
- Angle: a calendar town. The Kentucky Derby and the two-week Kentucky Derby Festival, bourbon
  tourism (the Kentucky Bourbon Trail, Whiskey Row on Main Street; verify), and big events bring
  seasonal surges: a Louisville site has to change with the calendar (spring hours, event specials,
  booking pages that go up and come down). Second thread: neighborhoods and corridors (NuLu on East
  Market, the Highlands along Bardstown Road, Germantown, Butchertown, Old Louisville, the West End,
  St. Matthews, Jeffersontown) and the Southern Indiana side across the Ohio (Jeffersonville, New
  Albany, Clarksville). Resources: Kentucky SBDC (Louisville office, verify host), Louisville Metro
  economic development / Louisville Forward (verify current name), Greater Louisville Inc. (the metro
  chamber), SCORE Louisville. Do not lead with the consolidated metro government (Indianapolis and
  Nashville pages already discuss consolidation).
- Fallback hero: images/heroes/faq-hero.jpg
- Photos: demo-images/hvac/4.jpg, demo-images/chiropractic/6.jpg, demo-images/cleaning/3.jpg

### wilmington-nc (batch D)
- Main: web design wilmington nc (260, SD 30). Supporting: website design wilmington nc (260, SD 34);
  wilmington website design (70, SD 36); web design wilmington (390, SD 62); web design wilmington
  north carolina (10); website development wilmington nc (10); web design nc (170, SD 38). Question
  rows usable as FAQs: how much does web design cost (170); how much web design cost (40).
  Wilmington, North Carolina ONLY: say plainly once that this page is about Wilmington, NC (not
  Wilmington, Delaware), since searchers mix them up.
- Angle: a coastal small city that runs on seasons. Summer beach traffic at Wrightsville Beach,
  Carolina Beach and Kure Beach, short-term rental turnover, charter and surf businesses, then an
  off-season when locals carry the business; plus the film and TV production industry (verify the
  studio and its history) with its freelance crews and vendors, and UNCW. A Wilmington site has to
  speak to both the visitor in June and the local in January. Places: historic downtown and the
  Riverwalk, the Cargo District, Market Street, Oleander Drive, Ogden, Leland, Hampstead, Monkey
  Junction. Resources: SBTDC at UNCW (North Carolina's SBDC is called the Small Business and
  Technology Development Center; verify), Wilmington Chamber of Commerce, SCORE Cape Fear, the UNCW
  CIE (verify). Do NOT lead with hurricanes (the Tampa page covers storms); one sentence at most.
- Fallback hero: images/heroes/website-builder-vs-web-designer-hero.jpg
- Photos: demo-images/cleaning/1.jpg, demo-images/veterinary/4.jpg, demo-images/photography/1.jpg
