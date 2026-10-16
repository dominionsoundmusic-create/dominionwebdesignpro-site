# Writer brief: Wave 2 national city pages (Oct 16 2026)

Read first, in full: `CLAUDE.md`, `CITY-PAGES-WAVE2.md`, `INTAKE.md`, `docs/WRITING-GUIDE.md` (every
rule there applies), then the two model pages `src/pages/web-design/atlanta-ga.html` and
`src/pages/web-design/lawrenceville-ga.html`. Your pages use the same front matter shape, templates,
macros and image handling. INTAKE.md wins over everything.

## Your files
- `src/pages/web-design/<slug>.html` for each assigned city (flat URL: `url: "/web-design/<slug>.html"`,
  `type: area`, `city_name`, `state_name`, `crumb: "City, ST"`, `summary:` max 160 chars, `schema_service`).
- `docs/writers/w2-<your-batch>.md`: per page, the main and supporting keywords used, every fact
  stated with its source URL, and what you left out because you could not verify it.
- Do NOT edit shared files (build.py, templates, static, site.json, scripts, SERVICES.md,
  docs/keyword-plan.md, other writers' pages). The 13 cities are already in site.json, group
  `other-us`, so `m.area_pills(group='other-us', exclude='<slug>')` and `area:<slug>` links work.

## Keyword rules
The main target goes in the title (50 to 65 characters), the H1, the first paragraph and one H2.
Supporting terms go in naturally (an H2 or H3, body copy, the description); the Question-type
rows become FAQ questions where they read like real questions. Never stuff. Never use another
agency's brand name (for example "spinx", "duogeeks", "sacramento web design group" reads like a
company name, do not use it).

## Honesty rules (repeat of the hard rules that matter most here)
- Dominion Web Design Pro is Maurice Johnson in Big Sandy, East Texas, building remotely. No office,
  no team, no clients in the city. Use `{{ m.no_office('City') }}` exactly once. Never say Maurice
  has built for any business there. No reviews, ratings, awards, job counts, years, guarantees,
  ranking promises. Never "certified", "top-rated", "#1", "unlimited", "guarantee" in any form.
- Prices exactly: Starter $497, Pro $997, Agency $1,997, one time. Starter is live in 7 to 14 days;
  Agency pages arrive in waves, the first live inside two weeks. Pro chat widget free 14 days then
  $297/mo. Agency AI phone agent SETUP; the agent is free for 7 days then $297/mo for up to 750
  minutes, cancel any time, not part of the one-time price. Hosting, maintenance and updates included
  while the client keeps the AI agent, otherwise $49/mo. Use `{{ m.pricing_cards() }}` if you show
  the packages at all (optional on a city page).
- Phone: (903) 636-7511 is answered by an AI receptionist any hour that can transfer callers to
  Maurice. Never say a person always answers.
- No em dashes or en dashes anywhere. No eyebrow labels. American spelling. No banned phrases.
- Mark: the template adds `dwdp:handwritten`; do not add it yourself.

## Make every page different (the similarity limit is 15% on 5-word shingles, all city pages)
Each city has an assigned ANGLE below. Build the outline around it. Do not copy any section shape
from another city page: no "Four reasons a X business would hire..." grid copied from Dallas, no
"questions worth asking" table copied from Atlanta, no "Free help for X small businesses" panel
heading reused verbatim. The remote / East Texas disclosure is `m.no_office('City')` plus at most
one or two fresh sentences of your own. "Getting started" is at most one short line plus
`m.demo_box('a fresh sentence')`. Write every heading and paragraph fresh; vary your own phrasing
between your two or three cities too. Aim for 1,300 to 1,900 words of your own copy per page.

## Research and sources
Research each city with WebSearch before writing (WebFetch may be blocked; verify from search results
of the official or credible source). Budget about 8 to 10 searches per city. State only facts you
verified, and cite each one in `m.sources([...])` with a real URL that supports it. Cover: the
city's small business makeup (kinds of owner-run businesses common there), real neighborhoods,
corridors or suburbs a resident would recognize, its chamber of commerce and small business
resources (SBDC, SCORE chapter, city small business office), and why local search matters there.
When citing Google on local ranking use
https://support.google.com/business/answer/7091?hl=en (relevance, distance, prominence). Keep
numbers to ones you can source (Census QuickFacts, SBA Office of Advocacy state profiles, city or
chamber pages). If you cannot verify it, leave it out.

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
- In-body: use the three assigned existing photos (at least two) with `{{ img("path", "alt", w, h) }}`.
  Open each image with the Read tool first and write alt text that describes what is really in it.
  Never write alt text that claims a photo shows the city. Sizes: demo-images 1344x768,
  images/body 1200x800, images/contractors/contractor-work.jpg and contractor-review.jpg 1200x686.

## Check before you report
```
python3 build.py --out /tmp/claude-0/w2-<batch>/dist
python3 scripts/check.py --skip-links --dist /tmp/claude-0/w2-<batch>/dist --only /web-design/<slug>.html
python3 scripts/similarity.py --dist /tmp/claude-0/w2-<batch>/dist
```
Fix every ERROR. In the similarity output look at every pair that involves your pages and keep each
at or under 15% (other writers are writing at the same time; re-run at the end). Report: pages,
word counts, highest similarity pair per page, searches used, anything unverified.

## The 13 cities

Keyword numbers below are verified from keywords/Web-Design-National-Cities-Keywords.xlsx (city tabs)
and keywords/Web-Design-5-Cities-Recheck.xlsx (Cleveland). Volume is searches a month, SD is SEO difficulty.

### st-louis-mo (batch A)
- Main: website design st louis (2,400, SD 8). Supporting: st louis website design (1,300, SD 29);
  st louis web design company (1,600, SD 61); st louis web development (90, SD 36); web design stl (10, SD 30).
- Angle: a region split between an independent city and St. Louis County with many separate
  municipalities, so "St. Louis" means different places to different customers; neighborhood
  identity (The Hill, Soulard, The Grove, Cherokee Street, South City, North County, West County).
  Customers search by neighborhood or municipality, so pages need to name the real places served.
- Fallback hero: images/heroes/contact-hero.jpg ("Small business owner at a shop counter talking on a phone with a notepad in hand")
- Photos: demo-images/roofing/3.jpg, demo-images/restaurant/1.jpg, images/body/seo-city-pages-planning.jpg

### kansas-city-mo (batch A)
- Main: kansas city website design (390, SD 6). Supporting: kansas city web design (320, SD 25);
  web design kansas city mo (590, SD 46); website design in kansas city (720, SD 60); kansas city web
  design company (70, SD 55); kansas city web design and seo (30, SD 46).
- Angle: a two-state metro split by State Line Road (Kansas City, Missouri and Overland Park, Olathe,
  Lenexa, Kansas City, Kansas): a business that works both sides needs pages that say which side
  and which towns; licensing and city names differ by state. Neighborhoods: Crossroads, Westport,
  River Market, Brookside, Waldo, Northland.
- Fallback hero: images/heroes/pricing-hero.jpg ("Small business owner at a kitchen table comparing options on a laptop with a notepad beside it")
- Photos: demo-images/auto-repair/2.jpg, demo-images/landscaping/2.jpg, images/body/why-website-google-profile.jpg

### indianapolis-in (batch A)
- Main: indianapolis website design (1,900, SD 16). Supporting: indianapolis web design company
  (210, SD 43); indiana web design (210, SD 14); website design indiana (110, SD 39).
- Angle: the business-to-business small firm. Indianapolis sits on interstates and logistics and
  manufacturing; many small firms sell to other businesses (suppliers, contractors, distributors,
  service shops) whose buyers research vendors online before calling. Plus consolidated city-county
  government (Unigov) and cultural districts (Mass Ave, Fountain Square, Broad Ripple).
- Fallback hero: images/heroes/how-to-hire-a-web-designer-hero.jpg ("Business owner on a phone call at a workbench, taking notes while talking to a web designer")
- Photos: demo-images/electrical/2.jpg, demo-images/insurance/3.jpg, images/body/packages-seo-setup.jpg

### phoenix-az (batch B)
- Main: web design company in phoenix (2,900, SD 9). Supporting: web design in phoenix (1,900, SD 7);
  web development company phoenix (30, SD 32); phoenix web design services (10, SD 27).
- Angle: home service trades in a heat-driven, very spread-out metro (HVAC, pool, pest, roofing,
  landscaping) that work as service-area businesses without a storefront, across Phoenix and
  suburbs such as Mesa, Chandler, Gilbert, Glendale, Scottsdale, Peoria. Service-area pages and
  urgent mobile calls are the point.
- Fallback hero: images/contractors/contractor-hero.jpg ("Contractor in a hard hat checking a phone beside a work truck at sunset")
- Photos: demo-images/hvac/1.jpg, demo-images/landscaping/4.jpg, images/contractors/contractor-review.jpg

### las-vegas-nv (batch B)
- Main: website design las vegas nevada (2,900, SD 9). Supporting: las vegas website design (880,
  SD 10); web design in las vegas (3,600, SD 60); web design vegas (1,900, SD 42); las vegas web
  developers (70, SD 46); las vegas web design agency (50, SD 20).
- Angle: the locals' economy behind the tourist one. The Strip is largely in unincorporated Clark
  County (Paradise, Winchester), and residents live and shop in Henderson, Summerlin, North Las
  Vegas, Spring Valley, Enterprise. Small businesses that serve residents (trades, auto, salons,
  child care) compete for local searches; a 24-hour town where calls come at odd hours.
- Fallback hero: images/heroes/website-cost-per-month-hero.jpg ("Owner of a small shop reviewing monthly bills on a laptop at the back counter")
- Photos: demo-images/auto-repair/4.jpg, demo-images/salon/1.jpg, demo-images/cleaning/4.jpg

### sacramento-ca (batch B)
- Main: website design sacramento (2,400, SD 17). Supporting: sacramento web design (1,600, SD 36);
  web design in sacramento ca (2,400, SD 56); sacramento web design agency (10, SD 5).
- Angle: the state capital economy. Many small firms sell to government or to people who work for
  it; California's state Small Business certification program (explain what it is and how buyers
  check it; NEVER claim Dominion holds it), plus farm-to-fork food businesses. Neighborhoods and
  corridors: Midtown, Oak Park, Land Park, East Sacramento, the R Street corridor, Del Paso Boulevard;
  suburbs Elk Grove, Roseville, Folsom, Rancho Cordova.
- Fallback hero: images/heroes/website-designer-cost-hero.jpg ("Web designer sketching page layouts on paper beside a laptop in a bright home office")
- Photos: images/body/law-office-laptop.jpg, demo-images/landscaping/1.jpg, demo-images/insurance/4.jpg

### los-angeles-ca (batch C)
- Main: los angeles web design companies (1,900, SD 9). Supporting: web design in la (1,000, SD 13);
  web design in los angeles (4,400, SD 37); website design in los angeles (9,900, SD 50); web design
  agency in los angeles (260, SD 46); los angeles web design agency (880, SD 70); web design firms
  los angeles (720, SD 51); best web design los angeles (40, SD 26); los angeles website design
  experts (40, SD 18); top web design companies los angeles (50, SD 58).
- Angle: comparison shopping in the biggest, most crowded market. How to compare Los Angeles web
  design companies when there are hundreds; LA County has 88 cities, so "Los Angeles" covers places
  like Glendale, Pasadena, Long Beach, Santa Monica, Burbank that customers search by name. The city
  requires a Business Tax Registration Certificate; BusinessSource Centers help small owners.
- Fallback hero: images/heroes/web-design-packages-hero.jpg ("Two web design proposals laid out side by side on a desk with a highlighter")
- Photos: images/body/designer-cost-quote-review.jpg, images/body/hire-domain-ownership.jpg, demo-images/photography/1.jpg

### san-diego-ca (batch C)
- Main: web design in san diego (2,900, SD 9). Supporting: san diego website design (2,400, SD 51);
  website design san diego (1,300, SD 37); san diego web design company (320, SD 48); san diego web
  design experts (70, SD 37); best web design company san diego (10, SD 5); web design services in
  san diego (10, SD 5); san diego website developer (20, SD 22). Question rows usable as FAQs:
  how much do web designers charge (210); how much web design cost (40).
- Angle: neighborhood business districts. The city has Business Improvement Districts and
  neighborhood business associations (North Park, Hillcrest, Little Italy, Barrio Logan, Ocean Beach,
  Pacific Beach, City Heights, Kearny Mesa); a large military presence; residents search by
  neighborhood. Plus the high cost of running a business there, which makes a one-time price matter.
- Fallback hero: images/cost-page-hero.jpg ("Small business owner at a laptop working out what a new website will cost")
- Photos: demo-images/veterinary/2.jpg, demo-images/gym/3.jpg, demo-images/chiropractic/5.jpg

### miami-fl (batch D)
- Main: web design in miami (1,900, SD 10). Supporting: web design agency in miami (480, SD 13);
  miami web design companies (210, SD 42); web design company in miami (170, SD 38); website
  development in miami (30, SD 67); web design miami prices (30, SD 31).
- Angle: a bilingual market. Miami-Dade has a Hispanic majority and most residents speak a language
  other than English at home (verify the Census numbers); Haitian Creole too (Little Haiti). A
  Miami site often needs Spanish pages written by a person, not a machine-translated toggle. Be
  honest about what Dominion offers: ask in the demo request; do not claim fluent Spanish writing
  unless INTAKE says so (it does not), so say the client's Spanish copy is reviewed by the client or
  a fluent person. Neighborhoods: Little Havana (Calle Ocho), Wynwood, Little Haiti, Doral, Allapattah.
- Fallback hero: images/heroes/why-small-businesses-need-a-website-hero.jpg ("Bakery owner arranging bread on shelves before opening, with the shop door propped open")
- Photos: demo-images/salon/4.jpg, demo-images/insurance/1.jpg, demo-images/dental/3.jpg

### orlando-fl (batch D)
- Main: web design in orlando (1,600, SD 13). There are no other 10+ Orlando-specific web design terms
  in the file except "duogeeks web design in orlando" (another agency's brand: do NOT use).
  Question rows usable: how much web design cost (40).
- Angle: the visitor economy versus the resident economy, and the city's Main Street districts
  (Orlando has a city Main Street program with several neighborhood districts such as Mills 50,
  Ivanhoe Village, Audubon Park, College Park; verify the list). Businesses that serve visitors
  (vacation rental cleaning, tours, photographers) and those that serve the fast-growing resident
  base; Puerto Rican and broader Hispanic community.
- Fallback hero: images/heroes/website-builder-vs-web-designer-hero.jpg ("Small shop owner at a counter comparing website builder plans on a laptop")
- Photos: demo-images/cleaning/2.jpg, demo-images/photography/4.jpg, demo-images/hvac/3.jpg

### nashville-tn (batch D)
- Main: web design in nashville (880, SD 10). Supporting: website designer in nashville (140, SD 9);
  nashville website design (1,000, SD 50); nashville web design company (140, SD 38); nashville web
  design agency (30, SD 12).
- Angle: a fast-growing metro full of newcomers who do not yet know which local businesses to trust
  and search for everything; plus a large creative and self-employed workforce (music industry side
  businesses, photographers, studios). Neighborhoods: East Nashville, The Gulch, 12 South,
  Germantown, Sylvan Park, Antioch; suburbs Franklin, Murfreesboro, Hendersonville. Metro
  Nashville-Davidson consolidated government.
- Fallback hero: images/heroes/seo-web-design-hero.jpg ("Business owner at a counter looking up a local business on a phone, with a laptop open beside it")
- Photos: demo-images/photography/2.jpg, demo-images/gym/1.jpg, demo-images/real-estate/2.jpg

### chicago-il (batch E)
- Main: web design agency in chicago (880, SD 11). Supporting: web design in chicago (2,900, SD 80);
  web design company in chicago (880, SD 52); web development company chicago (390, SD 41); web
  development in chicago (260, SD 42); web development agency chicago (50, SD 12). Do NOT use the
  "how to cite a website chicago style" rows (citation style, unrelated).
- Angle: agency versus one person, in a city of 77 community areas whose neighborhood commercial
  strips are organized through Special Service Areas (SSAs) and neighborhood chambers. Corridors
  such as Milwaukee Avenue, Devon Avenue, 26th Street in Little Village, Clark Street in Andersonville,
  Chinatown. What an agency gives you versus what a one-person builder gives you, honestly.
- Fallback hero: images/heroes/faq-hero.jpg ("Shop owner leaning on a counter reading on a phone during a quiet moment in a small store")
- Photos: demo-images/salon/2.jpg, demo-images/restaurant/3.jpg, demo-images/default/1.jpg

### cleveland-oh (batch E)
- Main: website design cleveland ohio (880, SD 8). Supporting: cleveland website design (480, SD 23);
  website design cleveland (480, SD 23); cleveland web development (720, SD 41); cleveland web
  designer (210, SD 26); web design cleveland (210, SD 24); cleveland web design company (110, SD 26);
  cleveland web design agency (40, SD 25). "web design cleveland tn" is a different Cleveland: do not use.
- Angle: old houses and the trades that keep them standing (a city whose housing is among the oldest
  in the country: verify the Census median year built), plus a big health care economy. Explain
  plainly the difference between web design and web development, since "cleveland web development"
  is searched. Neighborhoods: Ohio City, Tremont, Gordon Square / Detroit Shoreway, Slavic Village,
  Collinwood; suburbs Lakewood, Parma, Euclid, Shaker Heights.
- Fallback hero: images/heroes/small-business-website-redesign-hero.jpg ("Owner of a small shop comparing an old website on a laptop with a new design on a tablet")
- Photos: images/contractors/contractor-work.jpg, demo-images/plumbing/3.jpg, demo-images/dental/2.jpg
