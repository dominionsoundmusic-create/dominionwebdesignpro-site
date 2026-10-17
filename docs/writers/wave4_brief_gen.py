#!/usr/bin/env python3
"""Generates docs/writers/BRIEF-WAVE4.md: per-city keywords, angle, hero and photo assignments for Wave 4.

Photo assignment is deterministic: each city gets three in-body photos from the reusable pool, spread so
every photo is used about evenly across the site, never twice on one page and never shared inside one
writer batch. Run: python3 docs/writers/wave4_brief_gen.py
"""
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
OUT = ROOT / "docs" / "writers" / "BRIEF-WAVE4.md"

POOL = (
    [f"demo-images/auto-repair/{n}.jpg" for n in (1, 2, 3, 4)]
    + [f"demo-images/chiropractic/{n}.jpg" for n in (4, 5, 6, 8)]
    + [f"demo-images/cleaning/{n}.jpg" for n in (1, 2, 3, 4)]
    + [f"demo-images/default/{n}.jpg" for n in (1, 2, 3)]
    + [f"demo-images/dental/{n}.jpg" for n in (1, 2, 3, 4)]
    + [f"demo-images/electrical/{n}.jpg" for n in (1, 2, 3, 4)]
    + [f"demo-images/gym/{n}.jpg" for n in (1, 2, 3, 4)]
    + [f"demo-images/hvac/{n}.jpg" for n in (1, 2, 3, 4)]
    + [f"demo-images/insurance/{n}.jpg" for n in (1, 2, 3, 4)]
    + [f"demo-images/landscaping/{n}.jpg" for n in (1, 2, 4)]
    + ["demo-images/legal/3.jpg"]
    + [f"demo-images/photography/{n}.jpg" for n in (1, 2, 3, 4)]
    + [f"demo-images/plumbing/{n}.jpg" for n in (1, 2, 3, 4)]
    + [f"demo-images/real-estate/{n}.jpg" for n in (1, 2, 3)]
    + [f"demo-images/restaurant/{n}.jpg" for n in (1, 2, 3, 4)]
    + [f"demo-images/roofing/{n}.jpg" for n in (1, 3, 4)]
    + [f"demo-images/salon/{n}.jpg" for n in (1, 2, 3, 4)]
    + [f"demo-images/veterinary/{n}.jpg" for n in (1, 2, 3, 4)]
    + [f"images/body/{f}.jpg" for f in (
        "builder-vs-designer-desk", "designer-cost-quote-review", "domain-renewal-reminder", "hire-domain-ownership",
        "law-firm-consult-room", "law-office-laptop", "packages-seo-setup", "seo-city-pages-planning",
        "therapist-waiting-room", "therapist-writing-notes", "why-website-google-profile",
        "black-owned-web-design-review-call")]
    + ["images/contractors/contractor-work.jpg", "images/contractors/contractor-review.jpg"]
)
SIZES = {"demo-images": "1344x768", "images/body": "1200x800", "images/contractors": "1200x686"}

# Real photos of the city already in the repo (Wikimedia Commons, credits in images/cities/credits.json).
REAL = {
    "lubbock-tx": ("1280x960", "Billy Hathorn", "CC BY-SA 3.0"),
    "knoxville-tn": ("1280x917", "Brian Stansberry", "CC BY 3.0"),
    "chattanooga-tn": ("1280x722", "Brian Stansberry", "CC BY 3.0"),
    "mobile-al": ("1280x720", "Altairisfar", "public domain"),
    "st-petersburg-fl": ("1280x960", "Ebyabe", "CC BY 2.5"),
    "spokane-wa": ("1280x960", "Murderbike", "public domain"),
    "reno-nv": ("1280x960", "Ken Lund", "CC BY-SA 2.0"),
    "boise-id": ("1280x804", "Lordchadwick79", "CC BY-SA 3.0"),
    "fort-collins-co": ("1280x720", "Xnatedawgx", "CC BY-SA 4.0"),
    "durham-nc": ("1280x960", "Warren LeMay", "CC BY-SA 4.0"),
    "greenville-sc": ("1280x852", "P. Hughes", "CC BY-SA 4.0"),
    "columbia-sc": ("1280x960", "Billy Hathorn", "CC BY-SA 3.0"),
    "baton-rouge-la": ("1280x851", "theMinsk", "public domain"),
}

# Generic heroes already in the repo, with an accurate alt for each (none shows or names a real place).
GENERIC = {
    "images/heroes/contact-hero.jpg": "Small business owner at a shop counter talking on a phone with a notepad in hand",
    "images/heroes/faq-hero.jpg": "Shop owner leaning on a counter reading on a phone during a quiet moment in a small store",
    "images/heroes/pricing-hero.jpg": "Small business owner at a kitchen table comparing options on a laptop with a notepad beside it",
    "images/heroes/seo-web-design-hero.jpg": "Business owner at a counter looking up a local business on a phone, with a laptop open beside it",
    "images/heroes/website-designer-cost-hero.jpg": "Web designer sketching page layouts on paper beside a laptop in a bright home office",
    "images/heroes/how-to-hire-a-web-designer-hero.jpg": "Business owner on a phone call at a workbench, taking notes while talking to a web designer",
    "images/heroes/small-business-website-redesign-hero.jpg": "Owner of a small shop comparing an old website on a laptop with a new design on a tablet",
    "images/heroes/website-builder-vs-web-designer-hero.jpg": "Small shop owner at a counter comparing website builder plans on a laptop",
    "images/heroes/website-cost-per-month-hero.jpg": "Owner of a small shop reviewing monthly bills on a laptop at the back counter",
    "images/heroes/why-small-businesses-need-a-website-hero.jpg": "Bakery owner arranging bread on shelves before opening, with the shop door propped open",
    "images/heroes/black-owned-web-design-hero.jpg": "Small business owner's counter with a laptop open to a new website, shelves of products behind it",
    "images/heroes/web-design-packages-hero.jpg": "Two web design proposals laid out side by side on a desk with a highlighter",
    "images/cost-page-hero.jpg": "Small business owner working on a laptop at a sunny desk",
    "images/contractors/contractor-hero.jpg": "Contractor in a hard hat checking a phone beside a work truck at sunset",
    "images/heroes/kansas-city-mo-hero.jpg": "Owner of a small auto repair shop talking with a customer beside a car in an open service bay",
    "images/heroes/indianapolis-in-hero.jpg": "Owner of a small industrial supply business checking an order sheet beside stacked boxes on warehouse shelving",
    "images/heroes/phoenix-az-hero.jpg": "HVAC technician beside a service van in a desert neighborhood driveway in bright afternoon light",
    "images/heroes/cleveland-oh-hero.jpg": "Tradesman measuring a wooden window frame on the porch of an older two-story frame house",
    "images/heroes/miami-fl-hero.jpg": "Owner of a small neighborhood cafe setting out pastries on a bright counter by an open window",
    "images/heroes/san-diego-ca-hero.jpg": "Owner of a small neighborhood shop checking a laptop at a sunny counter by an open door",
    "images/heroes/st-louis-mo-hero.jpg": "Owner of a small neighborhood bakery stacking bread loaves on a wooden rack in a brick-walled shop",
    "images/heroes/chicago-il-hero.jpg": "Owner of a small neighborhood shop sorting stock behind a counter by a big front window",
    "images/heroes/sacramento-ca-hero.jpg": "Small consulting firm owner reviewing a proposal at a desk in a bright converted brick office",
    "images/heroes/los-angeles-ca-hero.jpg": "Owner of a small neighborhood shop comparing two website proposals on a laptop at a sunny front counter",
    "images/heroes/las-vegas-nv-hero.jpg": "Auto shop owner at the counter of a small neighborhood repair shop at dusk, with a car on a lift behind him",
    "images/heroes/orlando-fl-hero.jpg": "Owner of a small cleaning company loading supplies into a van outside a stucco home",
    "images/heroes/el-paso-tx-hero.jpg": "Small business owner standing outside a stucco storefront with desert mountains in the background at golden hour",
    "images/heroes/gladewater-tx-hero.jpg": "Brick storefronts along a small-town East Texas street at sunset",
    "images/heroes/marshall-tx-hero.jpg": "Brick storefronts on a downtown street in East Texas at sunset",
    "images/heroes/decatur-ga-hero.jpg": "Owner arranging books and gifts in a bright independent shop with a brick wall and big front windows",
}

# slug -> (batch, words, main, supporting, angle, hero)
# hero: ("new", fallback) for a planned Artistly hero, ("real",) for a repo photo of the city, ("generic", path)
C = {}


def city(slug, batch, words, main, supporting, angle, hero):
    C[slug] = dict(batch=batch, words=words, main=main, supporting=supporting, angle=angle, hero=hero)


FULL = "1,300 to 1,900"
MID = "1,000 to 1,400"
SHORT = "700 to 1,000"

# ---------------- Part A: Texas ----------------
city("san-antonio-tx", "A1", FULL, "web design san antonio (1,900, SD 18)",
     "web designer san antonio tx (720, Question); san antonio website designers (260, Question); web design san antonio texas (110); "
     "san antonio web design company (110, Question); web design san antonio tx (90); affordable web design san antonio (30); "
     "texas web design san antonio (30); small business web design san antonio (20); wordpress web design san antonio (20). "
     "FAQ-able generic question: how much do web designers charge (210).",
     "Military City USA. Joint Base San Antonio (Fort Sam Houston, Lackland, Randolph) means military families arriving and "
     "leaving every year and many veteran-owned and military-spouse businesses (verify any number you use). Those newcomers "
     "search for everything from scratch, so a site must answer basics fast. Second thread: the city's own corridors and "
     "districts (St. Mary's Strip, Broadway, Southtown, the Pearl, Stone Oak, Alamo Heights, the Medical Center, the West Side). "
     "Resources: City of San Antonio Economic Development Department small business office, the UTSA SBDC network, the San "
     "Antonio Chamber and the San Antonio Hispanic Chamber (verify names). Keep tourism/River Walk to one sentence.",
     ("new", "images/heroes/los-angeles-ca-hero.jpg"))
city("laredo-tx", "A1", SHORT, "web design laredo tx (30, SD 10)", "web design laredo (30). FAQ-able: how much web design cost (40).",
     "The trade city. Laredo is one of the busiest land ports in the country for trade with Mexico (verify the current ranking "
     "and source), so a lot of its small firms are customs brokers, freight forwarders, trucking companies, warehouses and the "
     "shops and restaurants that serve drivers. A short, honest page: what a B2B logistics firm's site needs (services, "
     "languages spoken, bridges and hours, how to request a quote). Resources: Laredo Chamber, the SBDC at Texas A&M "
     "International University (verify). Mention the I-35 and Mines Road corridors only if verified.",
     ("generic", "images/heroes/miami-fl-hero.jpg"))
city("temple-tx", "A1", SHORT, "web design temple tx (10, SD 5)", "temple web design (40, Question).",
     "A medical town on I-35. Baylor Scott & White Medical Center in Temple and the VA hospital (verify) make health care the "
     "biggest employer, so small practices, home health, therapy and the services around hospital staff (child care, food, "
     "apartments) are common. Short honest page. Note that 'temple web design' also gets searches about Temple University, so "
     "say plainly the page is about Temple, Texas in Bell County. Resources: Temple Chamber, Temple EDC, the SBDC that covers "
     "Bell County (verify).",
     ("generic", "images/heroes/how-to-hire-a-web-designer-hero.jpg"))

city("fort-worth-tx", "A2", FULL, "web design fort worth texas (1,900, SD 34)",
     "web design fort worth tx (1,600); fort worth website design (1,600, Question); web design fort worth (1,300); web development "
     "fort worth (260, Question, SD 6); web design company fort worth (40, Question). FAQ-able: how much do web designers charge "
     "for a website (210).",
     "Fort Worth is not Dallas. A city that grew past a million people (verify Census) with its own identity: the Stockyards and "
     "western heritage, the Cultural District, Near Southside and Magnolia Avenue, West 7th, Camp Bowie, the TCU area, and the "
     "fast growth up north around Alliance. Owners want to be found as Fort Worth businesses, not lumped into 'DFW'. Use the "
     "'web development fort worth' search for one short, plain section on design versus development (do not copy the Cleveland "
     "page). Resources: Fort Worth Chamber, the City of Fort Worth Business Assistance Center (verify name), the SBDC for "
     "Tarrant County (verify host), Fort Worth Hispanic Chamber and Fort Worth Metropolitan Black Chamber (verify).",
     ("new", "images/heroes/web-design-packages-hero.jpg"))
city("arlington-tx", "A2", MID, "arlington website design (90, SD 18)",
     "web design arlington tx (70); web design arlington (70, Question); web design company arlington tx (20).",
     "The city in the middle. Arlington sits between Dallas and Fort Worth with the entertainment district (AT&T Stadium, "
     "Globe Life Field, Six Flags Over Texas) and UT Arlington. Game days and concerts bring crowds; most residents and "
     "customers drive (verify what you say about transit, the city has an on-demand rideshare service, not fixed bus routes). "
     "Angle: event-day business versus everyday neighbors, and customers arriving from both sides of the Metroplex. Say "
     "'Arlington, Texas' plainly (Arlington, Virginia exists). Resources: Arlington Chamber, the SBDC serving Tarrant County, "
     "City of Arlington economic development.",
     ("generic", "images/heroes/kansas-city-mo-hero.jpg"))
city("abilene-tx", "A2", MID, "abilene website design (90, SD 11)", "web design abilene tx (90).",
     "Dyess Air Force Base, three private universities (Abilene Christian, Hardin-Simmons, McMurry; verify) and a downtown "
     "that brands itself the Storybook Capital of America (verify the exact title and who granted it). Small businesses here "
     "sell to students and their families, to base households and to ranch country around Taylor County. Resources: Abilene "
     "Chamber, Development Corporation of Abilene, the Abilene SBDC (verify host).",
     ("generic", "images/heroes/st-louis-mo-hero.jpg"))

city("corpus-christi-tx", "A3", FULL, "website design corpus christi (170, SD 19)",
     "web design corpus christi (170); web design corpus christi tx (170). (Ignore 'corpus christi hooks schedule', dress code.)",
     "The port economy. The Port of Corpus Christi is a top U.S. energy export port (verify the exact claim and source), with "
     "refineries and plants along the ship channel that hire local contractors: welders, fabricators, industrial cleaners, "
     "safety trainers, equipment rental. Their buyers check a vendor's site for safety programs, capabilities and coverage area "
     "before calling. Second thread: Padre and Mustang Islands and Port Aransas bring visitors (one paragraph, do not repeat "
     "the Wilmington page's season framing). Places: downtown and the bayfront, Ocean Drive, the Southside, Calallen, "
     "Flour Bluff, Portland across the bay. Resources: the Coastal Bend SBDC (verify host), United Corpus Christi Chamber.",
     ("new", "images/heroes/orlando-fl-hero.jpg"))
city("mcallen-tx", "A3", MID, "web design mcallen texas (90, SD 11)",
     "web design mcallen (90); web developer mcallen tx (10).",
     "The Valley's shopping city. McAllen's retail draws shoppers from Mexico (verify how this is documented, for example sales "
     "tax or retail studies, and leave it out if you cannot source it), and the Rio Grande Valley works as one market: Edinburg, "
     "Mission, Pharr, Weslaco. Many customers search in Spanish or switch languages; be honest that Dominion does not claim "
     "Spanish copywriting and that Spanish pages should be written or reviewed by a fluent speaker (do not repeat the Miami "
     "page's wording). Resources: UTRGV SBDC, McAllen Chamber, McAllen EDC.",
     ("new", "images/heroes/black-owned-web-design-hero.jpg"))
city("brownsville-tx", "A3", MID, "web design brownsville (40, SD 9)", "web design brownsville tx (40).",
     "A border city with new kinds of work: SpaceX's Starbase at Boca Chica (now its own incorporated city, verify), the Port "
     "of Brownsville and its industrial projects (verify current status of any LNG project before naming it). Newcomers and "
     "contractors need food, housing, repairs and services, and long-time family businesses compete for them online. Places: "
     "historic downtown, the Southmost area, Boca Chica Boulevard, Los Fresnos and Port Isabel nearby. Resources: UTRGV SBDC "
     "(Brownsville office), Brownsville Chamber, Greater Brownsville Incentives Corporation (verify).",
     ("generic", "images/heroes/san-diego-ca-hero.jpg"))

city("lubbock-tx", "A4", FULL, "web design lubbock tx (320, SD 43)", "web design lubbock (320).",
     "The Hub City of the South Plains. Customers drive in from towns an hour or more away, so a Lubbock site has to work for "
     "someone planning a trip: hours, what is in stock, whether to call ahead, service area towns (Wolfforth, Shallowater, "
     "Levelland, Slaton). Cotton and farm services, Texas Tech and its medical school, and the Depot District, Broadway, "
     "34th Street and fast-growing south Lubbock (verify). Resources: the Northwest Texas SBDC (headquartered at Texas Tech, "
     "verify), Lubbock Chamber, Lubbock EDA.",
     ("real",))
city("amarillo-tx", "A4", MID, "web design amarillo (140, SD 18)", "web design amarillo tx (140). ('web design az' is Arizona: unused.)",
     "Two audiences on I-40. Travelers crossing the Panhandle search on their phones for food, tires, motels and repairs in "
     "the next exit or two, while the local economy runs on cattle feeding, meat processing and medical care (verify). One "
     "site can serve both if it is fast on a phone and plain about location. Route 66's Sixth Avenue historic district, "
     "Canyon and Palo Duro Canyon nearby, the Medical Center district. Resources: Amarillo Chamber, Amarillo EDC, the SBDC "
     "for the Panhandle (verify host, likely West Texas A&M).",
     ("generic", "images/heroes/cleveland-oh-hero.jpg"))
city("san-angelo-tx", "A4", SHORT, "web design san angelo (20, SD 13)", "none above 10 besides the target.",
     "Short page. Goodfellow Air Force Base (verify its training mission), Angelo State University, ranching and the wool and "
     "mohair trade the city is known for (verify), the Concho River and downtown's River Stage area. Small owners serve students, "
     "base families and ranch country across the Concho Valley. Resources: San Angelo Chamber, the ASU SBDC (verify), COSADC "
     "(San Angelo's development corporation, verify name).",
     ("generic", "images/heroes/chicago-il-hero.jpg"))

city("midland-tx", "A5", MID, "web design midland tx (70, SD 26)", "none above 10 besides the target.",
     "Boom and bust in the Permian Basin. Midland is where oil companies keep their offices; when prices swing, hiring, rents "
     "and restaurant traffic swing with them (verify a recent example). A small business site here should be easy to change "
     "fast: hiring now, slower season, new hours. Places: downtown towers, the Loop 250 corridor, Midland Park Mall area, "
     "the airport between Midland and Odessa. Resources: Midland Chamber, Midland Development Corporation, the UTPB SBDC (verify).",
     ("new", "images/contractors/contractor-hero.jpg"))
city("odessa-tx", "A5", MID, "website design odessa tx (90, SD 5)", "web design odessa tx (40).",
     "The field side of the Permian. Odessa's small companies are hands-on: welding, trucking, oilfield services, equipment "
     "repair, and the restaurants and shops that feed crews (verify). These firms hire as much as they sell, so a site needs a "
     "plain careers or 'now hiring' page as well as services and a coverage map. Also UTPB and Odessa College, and a large "
     "Hispanic community. Do NOT repeat the Midland page's boom-and-bust framing. Resources: Odessa Chamber, Odessa Development "
     "Corporation, UTPB SBDC (verify).",
     ("generic", "images/heroes/phoenix-az-hero.jpg"))
city("killeen-tx", "A5", SHORT, "web design killeen tx (40, SD 20)", "web design killeen (20).",
     "Short page. The post next door: Fort Hood (verify the current name; it was renamed Fort Cavazos in 2023 and the Army "
     "restored the Fort Hood name in 2025, confirm before writing) is one of the largest military installations in the world "
     "(verify). Soldiers and families rotate in and out, military spouses run home-based businesses, and service businesses "
     "near the gates compete hard. Harker Heights, Copperas Cove, Nolanville. Resources: Greater Killeen Chamber, the SBDC "
     "serving Bell County (verify), Killeen EDC.",
     ("generic", "images/heroes/contact-hero.jpg"))

city("sugar-land-tx", "A6", MID, "web design sugar land (40, SD 14)", "web design sugar land tx (30); sugar land web design (30, Question).",
     "Professional and family services in one of the country's most diverse counties (Fort Bend, verify the source). Dentists, "
     "CPAs, tutoring centers, insurance agents, physical therapists: credentials and languages spoken matter on their sites. "
     "Places: Sugar Land Town Square, Telfair, First Colony, Imperial Market on the old sugar refinery site (verify), Highway 6 "
     "and US 59/I-69. Resources: Fort Bend Chamber, City of Sugar Land economic development, the Houston SBDC network (verify "
     "which office serves Fort Bend).",
     ("generic", "images/heroes/why-small-businesses-need-a-website-hero.jpg"))
city("katy-tx", "A6", MID, "katy web design (40, SD 14)", "katy web (50, Question); web design katy tx (30); web design katy (30).",
     "Katy is bigger than the city of Katy. Most people with a Katy address live outside the small city limits, in "
     "master-planned communities in Harris, Fort Bend and Waller counties (Cinco Ranch, Cross Creek Ranch, Elyson; verify). So a "
     "business should name the communities and roads (Grand Parkway, I-10, Fry Road, Mason Road) it serves, not just 'Katy'. "
     "Katy ISD families drive the demand for home services, activities and tutoring. Old Town Katy and the Katy Rice Festival "
     "(verify). Resources: Katy Area Chamber, Katy Area EDC.",
     ("generic", "images/heroes/pricing-hero.jpg"))
city("cypress-tx", "A6", MID, "web design cypress tx (170, SD 9; found in the Temple TX tab of the Texas file)", "none above 10 besides the target.",
     "A large community with no city hall. Cypress is unincorporated Harris County (verify), so there is no city small business "
     "office; customers know it by ZIP code, school (Cy-Fair ISD, one of the largest districts in Texas, verify) and community "
     "name (Towne Lake, Bridgeland, Fairfield, Coles Crossing), and by Highway 290 and the Grand Parkway. A site needs those "
     "names. Resources: Cy-Fair Houston Chamber (verify name), the Houston SBDC network, Lone Star College (verify any small "
     "business center).",
     ("generic", "images/heroes/website-cost-per-month-hero.jpg"))

city("the-woodlands-tx", "A7", SHORT, "web design the woodlands (40, SD 10)", "web design the woodlands tx (20).",
     "Short to mid page. A township, not a city (The Woodlands Township, verify), built as villages (Alden Bridge, Sterling Ridge, "
     "Creekside Park, Panther Creek). Families relocate here for big employers nearby (verify which, for example the ExxonMobil "
     "campus in Spring) and often research local businesses from out of state before they move. Market Street, the Waterway, "
     "Hughes Landing. Resources: The Woodlands Area Chamber, the SBDC serving Montgomery County (verify).",
     ("generic", "images/heroes/seo-web-design-hero.jpg"))
city("beaumont-tx", "A7", MID, "web design beaumont tx (30, SD 15)", "none above 10 besides the target (the Beaumont tab's other rows are other towns).",
     "The Golden Triangle (Beaumont, Port Arthur, Orange). Refineries and plants bring 'turnaround' crews for weeks at a time "
     "(verify), so food, lodging and repair businesses see surges; the Spindletop gusher of 1901 started it all (verify); Cajun "
     "and Creole food crosses over from Louisiana; Lamar University. Storms: one sentence at most. Resources: the Lamar "
     "University SBDC (verify), Greater Beaumont Chamber, City of Beaumont.",
     ("generic", "images/heroes/indianapolis-in-hero.jpg"))
city("round-rock-tx", "A7", SHORT, "web design round rock (30, SD 11)", "web design round rock tx (30).",
     "Short page. Dell's hometown (headquarters, verify) and a city that calls itself the Sports Capital of Texas (verify), with "
     "Dell Diamond, the Round Rock Express and big youth tournaments that bring visiting families on weekends. Old Settlers Park, "
     "downtown Main Street, La Frontera, University Boulevard and the medical campuses (verify). Do NOT repeat the Pflugerville, "
     "Cedar Park or Leander pages (read them first). Resources: Round Rock Chamber, the SBDC serving Williamson County (verify).",
     ("generic", "images/heroes/faq-hero.jpg"))

city("nacogdoches-tx", "A8", SHORT, "web design nacogdoches (10, SD 18)", "none above 10 besides the target.",
     "Short page, East Texas and close to home (Big Sandy is about two hours away, verify the drive before stating it; say it "
     "honestly, no office). Nacogdoches calls itself the oldest town in Texas (verify the wording), with brick streets downtown, "
     "Stephen F. Austin State University, timber and poultry. Students and parents, a historic downtown, rural customers from "
     "the surrounding counties. Resources: Nacogdoches County Chamber, the SBDC that serves Deep East Texas (verify host, likely "
     "Angelina College in Lufkin), City of Nacogdoches economic development.",
     ("generic", "images/heroes/gladewater-tx-hero.jpg"))
city("texarkana-tx", "A8", SHORT, "website design texarkana (10, SD 13)", "web design texarkana (10).",
     "Short page. A medical and shopping center for a four-state corner (Texas, Arkansas, Louisiana, Oklahoma; verify the "
     "framing), with CHRISTUS St. Michael and Wadley hospitals (verify), Texas A&M University-Texarkana and Red River Army Depot "
     "nearby (verify). The state line runs down State Line Avenue: mention it in one sentence only, because the Kansas City page "
     "already leads with a two-state metro. Resources: Texarkana Chamber (verify name), the SBDC serving Bowie County (verify).",
     ("generic", "images/heroes/marshall-tx-hero.jpg"))

# ---------------- Part B: South and East ----------------
city("charlotte-nc", "B1", FULL, "web design in charlotte nc (1,900, SD 65)",
     "web design in charlotte (1,600); web design charlotte (1,000); website design charlotte (1,000); web design charlotte nc "
     "(1,000); charlotte web design company (390); web design charlotte north carolina (90); professional / responsive web design "
     "charlotte (20 / 20); affordable / custom web design charlotte (10 / 10). FAQ-able: how much do web designers charge per hour (50). "
     "Unused: port charlotte (Florida), charlottesville (Virginia), salary.",
     "A banking city full of professionals who go out on their own. Charlotte is a major U.S. banking center (Bank of America "
     "headquarters, verify), and many consultants, advisors, bookkeepers and coaches start firms here; their sites must earn "
     "trust fast. Neighborhoods: South End, NoDa, Plaza Midwood, Dilworth, Ballantyne, University City; towns: Matthews, "
     "Huntersville, Concord, and Fort Mill across the South Carolina line. Resources: SBTDC at UNC Charlotte (verify), Charlotte "
     "Regional Business Alliance, the City of Charlotte's small business programs (verify current names), SCORE Charlotte.",
     ("new", "images/heroes/small-business-website-redesign-hero.jpg"))
city("greensboro-nc", "B1", MID, "web design greensboro (390, SD 28)", "web design greensboro nc (30); from keywords/Web-Design-5-Cities-Recheck.xlsx: website design greensboro (390, Question, SD 25); website designer greensboro nc (20, Question).",
     "Makers of the Piedmont Triad. Textile and furniture history (High Point's furniture market is next door, verify), NC A&T "
     "(verify its HBCU size claim), UNC Greensboro, the 1960 Woolworth sit-ins and the International Civil Rights Center and "
     "Museum, and new manufacturing nearby such as the Toyota battery plant in Liberty (verify). Small suppliers, workshops "
     "and trades need plain capability pages. Places: downtown and Elm Street, Fisher Park, Lindley Park, Friendly Avenue. "
     "Resources: Greensboro Chamber, the SBTDC office serving Greensboro (verify host), City of Greensboro M/WBE office (verify).",
     ("generic", "images/heroes/website-designer-cost-hero.jpg"))
city("augusta-ga", "B1", MID, "web design augusta ga (140, SD 27)", "web design augusta (140, Question); web design ga (40).",
     "One week every April and a cyber town the rest of the year. Masters week brings visitors and a short-term home rental "
     "market (verify how it works and cite it), and Fort Eisenhower (formerly Fort Gordon, verify) is home to Army Cyber "
     "Command (verify), so cybersecurity contractors and IT firms have grown. Augusta University and its medical center. "
     "Places: Broad Street downtown, Summerville, the Hill, Evans and Martinez in Columbia County, North Augusta across the "
     "river. Resources: UGA SBDC Augusta office, Augusta Metro Chamber.",
     ("generic", "images/heroes/contact-hero.jpg"))

city("raleigh-nc", "B2", FULL, "web design raleigh north carolina (590, SD 34)",
     "raleigh web design (720, Question); web design raleigh (590); raleigh web design company (50, Question); custom web design "
     "raleigh nc / raleigh (10 / 10); small business web design raleigh (10); shopify web design raleigh (10: answer honestly, "
     "online stores are not in the INTAKE packages); web design in nc (210, SD 6, statewide, from the Nacogdoches tab).",
     "Wake County's string of towns. Raleigh plus Cary, Apex, Holly Springs, Wake Forest, Garner, Fuquay-Varina, Morrisville: "
     "each has its own identity and many residents are new homeowners (verify growth from Census). Customers search by their "
     "own town, so a business needs a page per town it really serves. Also the state government and Research Triangle Park. "
     "Do NOT reuse the Nashville newcomer framing. Raleigh places: downtown, Glenwood South, North Hills, Five Points, "
     "Warehouse District. Resources: SBTDC at NC State (verify), Greater Raleigh Chamber, City of Raleigh Office of Economic "
     "Development and Innovation (verify name), SCORE.",
     ("new", "images/cost-page-hero.jpg"))
city("durham-nc", "B2", FULL, "web design durham nc (210, SD 23)",
     "website design durham nc (210, Question); durham website design (50, Question). 'webb design durham' rows read like a "
     "company name: unused. 'web design north carolina' (170) may be worked in as supporting.",
     "Old tobacco buildings, new companies. Durham turned its tobacco warehouses into offices and venues (American Tobacco "
     "Campus, Brightleaf Square, verify), Duke University and Duke Health are the biggest employers (verify), and startups "
     "cluster downtown (American Underground, verify). Parrish Street's 'Black Wall Street' history and Hayti (verify) matter "
     "here; you may link /black-owned-web-design/ once in context (INTAKE section 7, no certification claims), but do not make "
     "it the whole page (the Tulsa page uses Greenwood). Resources: SBTDC office serving Durham (verify, NC Central hosts one), "
     "Greater Durham Chamber, City of Durham's small business programs (verify).",
     ("real",))
city("montgomery-al", "B2", MID, "web design montgomery al (90, SD 32)", "none above 10 besides the target.",
     "History visitors and a capital economy. The Legacy Museum and the National Memorial for Peace and Justice (opened 2018, "
     "verify), the Rosa Parks Museum and the Civil Rights Memorial draw visitors from around the world; Maxwell Air Force Base, "
     "state government and the Hyundai plant (verify) anchor jobs. Small restaurants, tour guides, lodging and shops need pages "
     "for visitors, while trades serve residents. Places: downtown and Dexter Avenue, the Alley, Cloverdale, EastChase. Resources: "
     "Montgomery Area Chamber, the Alabama SBDC office serving Montgomery (verify host).",
     ("generic", "images/heroes/website-cost-per-month-hero.jpg"))

city("charleston-sc", "B3", FULL, "charleston website design (1,300, SD 40)",
     "web design charleston sc (1,000); charleston sc web design (880, Question); charleston web designer (320, Question); "
     "web design summerville sc (30, from the Sugar Land tab; Summerville is a Charleston suburb). FAQ-able: how much do web designers charge for a website (210).",
     "Old houses, strict rules, and weddings. On the peninsula, exterior work on historic buildings goes through the city's "
     "Board of Architectural Review (verify scope), so contractors who restore old homes must explain that process; and "
     "Charleston is a big wedding and event market (verify a source), so planners, florists, photographers and venues compete "
     "online. Places: King Street, Upper King, Mount Pleasant, West Ashley, James Island, Johns Island, Summerville, North "
     "Charleston. Do NOT copy the Orange County HOA framing. Resources: SC SBDC Charleston office (verify host), Charleston "
     "Metro Chamber, SCORE.",
     ("new", "images/heroes/why-small-businesses-need-a-website-hero.jpg"))
city("columbia-sc", "B3", MID, "web design columbia (720, SD 55)",
     "web design columbia sc (590); website design columbia sc (480, Question); columbia web design (50, Question); web design lexington sc "
     "(70, from the Lexington KY tab; Lexington, SC is a Columbia suburb). 'web design columbia mo' is Missouri: unused.",
     "Which Columbia? Say plainly this page is Columbia, South Carolina. Fort Jackson is the Army's largest basic training "
     "center (verify), and graduation weeks bring families to town nearly every week (verify how often), filling restaurants "
     "and hotels; plus the state capital and the University of South Carolina. Places: the Vista, Main Street, Five Points, "
     "Devine Street, Forest Acres, Lexington and Irmo. Resources: the SC SBDC (state office at USC, verify), Columbia Chamber, "
     "City of Columbia Office of Business Opportunities (verify).",
     ("real",))
city("greenville-sc", "B3", MID, "web design greenville sc (480, SD 49)",
     "greenville web design (390, Question); site design greenville sc (90); greenville sc web design company (40); web design sc "
     "(90). 'web design greenville nc' rows: different place, unused.",
     "A downtown that came back. Main Street's makeover, Falls Park and the Liberty Bridge (verify the dates), and the Swamp "
     "Rabbit Trail out to Travelers Rest (verify length), with bike shops, cafes and breweries along it. Upstate manufacturing "
     "(Michelin North America headquarters, BMW's plant in nearby Spartanburg County; verify) feeds a supplier economy: keep that "
     "to one paragraph. Resources: SC SBDC Greenville office, Greenville Chamber, City of Greenville economic development.",
     ("real",))

city("savannah-ga", "B4", FULL, "savannah website design (390, SD 31)", "web design savannah (320); web design savannah georgia (320).",
     "A city full of designers. SCAD (Savannah College of Art and Design) puts a lot of design talent in town (verify enrollment), "
     "so be honest: a Savannah owner can hire a local student or graduate; explain what Dominion offers instead (a fixed price, "
     "the demo first, hand-written copy, hosting) without knocking anyone. Second thread: the historic district's squares "
     "(verify count), tourism and the Port of Savannah's growth plus the Hyundai Metaplant in Bryan County (verify). Use "
     "images/cities/savannah-ga.jpg (804x1200, photo by Jrozwado, CC BY-SA 4.0) as one in-body figure with a credit line. "
     "Resources: UGA SBDC Savannah, Savannah Area Chamber, City of Savannah Entrepreneurial Center (verify).",
     ("generic", "images/heroes/sacramento-ca-hero.jpg"))
city("jacksonville-fl", "B4", FULL, "jacksonville website design (1,600, SD 57)",
     "web design jacksonville fl (1,000); jacksonville web design company (40, Question); website design company jacksonville fl "
     "(210, National file); website development jacksonville (70, National file). 'web design jacksonville nc' is a different "
     "place: unused.",
     "One city, an hour across. Jacksonville is the largest city by land area in the lower 48 (verify), so a customer in "
     "Mandarin and one at the Beaches are far apart; businesses must name the parts of town they serve (Riverside, Avondale, "
     "San Marco, Southside, Arlington, Northside, the Beaches, Orange Park in Clay County). Navy bases (NAS Jacksonville, "
     "Mayport; verify) bring rotating families. Do NOT lead with consolidated government. Resources: Florida SBDC at UNF, "
     "JAX Chamber, the City's JSEB program (Jacksonville Small and Emerging Business, verify).",
     ("new", "images/heroes/pricing-hero.jpg"))
city("tallahassee-fl", "B4", MID, "web design tallahassee fl (140, SD 32)",
     "web design tallahassee (140); tallahassee web design (90, Question); tallahassee website design (70, Question).",
     "Two calendars: the legislative session and the school year. FSU, FAMU and Tallahassee Community College bring tens of "
     "thousands of students (verify), and the Legislature's session (verify length and months) fills hotels and restaurants "
     "with lobbyists and staff. Small businesses have to update for both. Places: College Town, Midtown, Railroad Square, "
     "Market District, Southside. Resources: Florida SBDC at FAMU (verify), Greater Tallahassee Chamber, Tallahassee-Leon "
     "County Office of Economic Vitality (verify).",
     ("generic", "images/heroes/how-to-hire-a-web-designer-hero.jpg"))

city("fort-lauderdale-fl", "B5", FULL, "web design fort lauderdale fl (1,300, SD 6)",
     "fort lauderdale website design (1,000, Question); web design fort lauderdale (880); website design fort lauderdale (880); "
     "fort lauderdale web design company (140, Question); web design company fort lauderdale (110, Question); web development / "
     "web design agency fort lauderdale (30 / 30); custom / responsive web design fort lauderdale (10 / 10). Ecommerce row: "
     "answer honestly or leave unused.",
     "The boating economy. Fort Lauderdale calls itself the yachting capital (verify the claim's source), with a marine "
     "industry of mechanics, detailers, canvas makers, captains and brokers along the canals and the New River, plus the "
     "International Boat Show each fall (verify). These trades sell to owners who search by service and marina. Second "
     "thread: Broward's other cities (Wilton Manors, Oakland Park, Plantation, Davie, Hollywood, Pompano Beach). Resources: "
     "Florida SBDC office serving Broward (verify host), Greater Fort Lauderdale Chamber, Broward County Office of Economic "
     "and Small Business Development (verify).",
     ("new", "images/heroes/san-diego-ca-hero.jpg"))
city("west-palm-beach-fl", "B5", FULL, "web design west palm beach (590, SD 12)",
     "web design west palm beach fl (590); west palm beach website design (590, Question); palm beach web design (70, Question); "
     "west palm beach web development (40, Question); west palm beach web design company (30, Question).",
     "Winter residents and Wall Street South. Seasonal residents arrive in the fall and leave in spring (verify), so home "
     "watch services, concierge, pool, cleaning and repair businesses must reach owners who are often in another state; and "
     "finance firms that moved down (the 'Wall Street South' nickname, verify) brought new professional demand. Places: "
     "Clematis Street, Rosemary Square (formerly CityPlace), Northwood Village, Flamingo Park, Palm Beach across the bridge, "
     "Lake Worth Beach. Do NOT copy the Wilmington page's summer season framing. Resources: Florida SBDC at FAU (verify), "
     "Chamber of Commerce of the Palm Beaches, City of West Palm Beach.",
     ("generic", "images/heroes/los-angeles-ca-hero.jpg"))
city("pensacola-fl", "B5", MID, "web design pensacola florida (170, SD 17)", "web design pensacola (170); pensacola website design (170, Question).",
     "The Navy town on the Gulf. NAS Pensacola trains aviators (verify) and is home to the Blue Angels (verify), so new "
     "students and families arrive all year and need everything found online. Downtown Palafox Street's comeback, Pensacola "
     "Beach, Perdido Key, Gulf Breeze. The Florida SBDC Network's lead office is at UWF in Pensacola (verify). Resources: "
     "Florida SBDC at UWF, Greater Pensacola Chamber, FloridaWest (verify).",
     ("generic", "images/heroes/seo-web-design-hero.jpg"))

city("st-petersburg-fl", "B6", MID, "web design st petersburg (260, SD 14)", "web design st petersburg fl (210); web design st pete (210, Question).",
     "Independent shops and murals. Central Avenue's independent businesses, the Grand Central District, the EDGE District, "
     "the Warehouse Arts District, the SHINE mural festival (verify) and a local-first business culture (verify any alliance "
     "you name). The Tampa page already covers the bay region: do NOT repeat its storm or bay-split framing. Say 'St. Petersburg, "
     "Florida' plainly (Russia's St. Petersburg shows in searches). Resources: Florida SBDC in Pinellas County (verify host), "
     "St. Petersburg Area Chamber, the city's Greenhouse small business center (verify).",
     ("real",))
city("sarasota-fl", "B6", MID, "web design sarasota florida (720, SD 17)",
     "web design sarasota (720); sarasota website development (90, Question); sarasota website design companies (30, Question). "
     "FAQ-able: how much do web designers charge for a website (210).",
     "An older customer base and an arts town. Sarasota County's median age is among the highest in Florida (verify with Census), "
     "so sites must be easy to read: larger text, plain buttons, a phone number at the top, no tiny gray type. Arts and culture "
     "(the Ringling, verify), Siesta Key, Lakewood Ranch growth to the east (verify). Places: Main Street, St. Armands Circle, "
     "Gulf Gate, Venice. Resources: Florida SBDC office serving Sarasota (verify), Greater Sarasota Chamber, EDC of Sarasota County.",
     ("generic", "images/heroes/faq-hero.jpg"))
city("fort-myers-fl", "B6", MID, "web design fort myers (390, SD 8)",
     "web design fort myers florida (590); web design fort myers fl (390); fort myers website design (390, Question); responsive "
     "web design fort myers (30: explain what responsive means).",
     "Spring training and Cape Coral's canals. Two MLB teams train here (Red Sox and Twins, verify parks), so February and March "
     "bring visitors; Cape Coral next door has hundreds of miles of canals (verify) and the boat, dock and seawall trades that come "
     "with them. The Edison and Ford Winter Estates. Storms (Hurricane Ian, 2022): one sentence at most. Places: downtown River "
     "District, McGregor Boulevard, Cape Coral, Estero, Lehigh Acres. Resources: Florida SBDC at FGCU, Greater Fort Myers Chamber, "
     "Lee County economic development.",
     ("generic", "images/heroes/website-builder-vs-web-designer-hero.jpg"))

city("new-orleans-la", "B7", FULL, "new orleans website design (1,900, SD 48)",
     "web design new orleans la (1,900); web design new orleans (1,300); web design louisiana (170). Unused: cookie designers, "
     "garden district safety, streetwear stores.",
     "Food, music and neighborhoods with names everyone knows. Restaurants, bars, musicians, tour guides and makers make up a "
     "big part of the owner-run economy (verify a hospitality employment source); neighborhoods: French Quarter, Marigny, "
     "Bywater, Treme, Mid-City, Uptown and Magazine Street, Freret, Gentilly, Algiers, plus Metairie and the Northshore. Event "
     "calendar (Mardi Gras, Jazz Fest, verify dates) in one paragraph. Short-term rental rules or permits only if verified and "
     "useful. Resources: Louisiana SBDC (verify which office serves Orleans Parish), New Orleans Chamber, the City's Office of "
     "Supplier Diversity (verify), Propeller (verify).",
     ("new", "images/heroes/web-design-packages-hero.jpg"))
city("baton-rouge-la", "B7", MID, "website design baton rouge (590, SD 27)",
     "none above 10 besides the target (the 'how to learn to design a website' rows are DIY learning: unused, though one FAQ "
     "may answer 'should I design my own website' honestly).",
     "Game days and plant shifts. LSU football Saturdays in Tiger Stadium bring huge crowds (verify capacity), and the chemical "
     "plants and refinery along the river (verify) run around the clock, so restaurants, auto shops and services keep odd hours. "
     "Also state government. Places: downtown, Mid City, Perkins Road, Southdowns, Highland Road, Prairieville, Denham Springs, "
     "Zachary. Resources: Louisiana SBDC at LSU (verify), Baton Rouge Area Chamber, Build Baton Rouge (verify).",
     ("real",))
city("shreveport-la", "B7", MID, "web design shreveport (70, SD 14)", "web design shreveport la (70).",
     "Twin cities on the Red River and close to East Texas. Shreveport and Bossier City, the riverboat casinos, Barksdale Air "
     "Force Base (verify), health care (verify the big hospital systems). Many customers drive in from East Texas and south "
     "Arkansas; Big Sandy is about a two-hour drive (verify before stating it; no office there). Places: downtown, Highland, "
     "Line Avenue, Youree Drive, Bossier's East Texas Street corridor. Resources: Louisiana SBDC office serving Shreveport "
     "(verify host, likely LSU Shreveport), Greater Shreveport Chamber, Bossier Chamber.",
     ("generic", "images/heroes/black-owned-web-design-hero.jpg"))

city("birmingham-al", "B8", FULL, "web design birmingham al (70, SD 37)",
     "website design birmingham al (70, Question); alabama website design (210, Question); alabama web design (170, Question); "
     "web development agency / company birmingham (40 / 30, National file; check they are Alabama, the tab is Birmingham AL).",
     "A medical city with an iron past. UAB is the state's largest employer (verify), so medical practices, home health, "
     "staffing, labs and the services around hospital workers are common. Steel history (Sloss Furnaces), Innovation Depot "
     "for startups (verify), neighborhoods (Avondale, Lakeview, Southside, Five Points South, Woodlawn) and the "
     "over-the-mountain suburbs (Homewood, Mountain Brook, Vestavia Hills, Hoover). Use the statewide 'alabama website design' "
     "searches for a short paragraph on serving Alabama. Resources: Alabama SBDC at UAB (verify), Birmingham Business Alliance.",
     ("generic", "images/heroes/st-louis-mo-hero.jpg"))
city("mobile-al", "B8", MID, "website design mobile al (50, SD 29)",
     "web design mobile al (50); how much of web traffic is mobile (40, Question: answer it as an FAQ with a cited figure); "
     "web designer mobile al (10, from the Montgomery tab).",
     "Shipyards, airplanes and a port. Austal USA builds ships here and Airbus assembles jetliners at Brookley (verify both), "
     "and the Port of Mobile handles a lot of cargo (verify), so suppliers, machine shops, staffing and trades sell to big "
     "buyers. Mardi Gras started here in America (verify the claim wording): one sentence only, the New Orleans page covers "
     "carnival. Places: downtown and Dauphin Street, Midtown, west Mobile, and the Eastern Shore (Daphne, Spanish Fort, "
     "Fairhope). Resources: Alabama SBDC at the University of South Alabama (verify), Mobile Chamber.",
     ("real",))
city("jackson-ms", "B8", MID, "web design jackson ms (30, SD 26)",
     "website design jackson ms (10); web design mississippi (50, Question). 'web design jackson mi' is Michigan and 'web "
     "mapping jackson county' is unrelated: unused.",
     "Posting what customers need to know, fast. During the 2022 water crisis (verify dates and what happened), businesses "
     "had to tell customers quickly whether they were open; a site that is easy to update matters. Keep the tone respectful and "
     "factual. Plus the state capital, Jackson State University (verify), Fondren, Belhaven, Farish Street history, and the "
     "suburbs Ridgeland, Madison, Brandon, Flowood. Use 'web design mississippi' for a short statewide paragraph. Resources: "
     "Mississippi SBDC (verify which office serves Jackson), Greater Jackson Chamber Partnership.",
     ("generic", "images/heroes/chicago-il-hero.jpg"))

city("knoxville-tn", "B9", FULL, "knoxville tn web design (480, SD 39)",
     "web design knoxville (390); web design knoxville tn (390); knoxville website design (390, Question); web development "
     "knoxville (30); knoxville web design company (30, Question).",
     "The gateway to the Smokies. Great Smoky Mountains National Park is the most visited national park (verify), and "
     "Knoxville businesses sell to visitors heading to Gatlinburg and Pigeon Forge as well as to locals: outfitters, cabin "
     "cleaners, guides, restaurants. Plus the University of Tennessee and Oak Ridge National Laboratory nearby (verify). "
     "Places: Market Square, the Old City, South Knoxville's Urban Wilderness, Bearden, Fountain City, Farragut, Maryville. "
     "Resources: TSBDC office serving Knoxville (verify host), Knoxville Chamber, The Development Corporation of Knox County (verify).",
     ("real",))
city("chattanooga-tn", "B9", MID, "chattanooga website design (140, SD 32)", "chattanooga web design (110, Question); chattanooga web developers (10, Question).",
     "Gig City. The city power company EPB built a fiber network and offered gigabit internet citywide early (verify year), "
     "which helped a startup scene (Co.Lab, verify); plus manufacturing (Volkswagen's plant, verify) and the downtown "
     "riverfront, Southside, North Shore, Main Street, Lookout Mountain. Do NOT make it an outdoor-tourism page (Knoxville does "
     "that). Resources: TSBDC at Chattanooga State (verify), Chattanooga Area Chamber, the Company Lab.",
     ("real",))
city("memphis-tn", "B9", FULL, "memphis website design (390, SD 26)", "neo memphis web design (10: reads like a style or brand, unused).",
     "A city that works overnight. FedEx's world hub (verify) and the logistics and distribution centers around it mean shift "
     "work all night, so restaurants, auto shops, child care and services keep late hours and need sites that say so; plus "
     "Beale Street, blues and barbecue for visitors. Memphis is majority Black (verify Census), with a long tradition of "
     "Black-owned business (you may link /black-owned-web-design/ once). Places: downtown, Midtown, Cooper-Young, Overton "
     "Square, Orange Mound, Whitehaven, Germantown, Bartlett, Collierville, and Southaven across the Mississippi line. "
     "Resources: TSBDC office serving Memphis (verify host), Greater Memphis Chamber, EPIcenter (verify), City of Memphis "
     "Office of Business Diversity and Compliance (verify).",
     ("generic", "images/heroes/cleveland-oh-hero.jpg"))

city("lexington-ky", "B10", FULL, "website design lexington (480, SD 19)",
     "web design lexington ky (480); lexington website design (70, Question); web design kentucky (90). 'web design lexington "
     "sc' is South Carolina: unused. FAQ-able: how much do web designers charge for a website (210).",
     "Horse country. Thoroughbred farms around Lexington support farriers, equine vets, fencing and barn builders, transport, "
     "tack shops (verify an industry source); Keeneland's spring and fall race meets and sales (verify months) bring buyers "
     "and visitors. Plus the University of Kentucky. Do NOT use bourbon as the angle (the Louisville page does). Places: "
     "downtown, Chevy Chase, the Distillery District (one mention), Hamburg, Southland Drive, Nicholasville, Georgetown. "
     "Resources: the Kentucky SBDC (lead office at UK, verify), Commerce Lexington, SCORE.",
     ("generic", "images/heroes/decatur-ga-hero.jpg"))
city("little-rock-ar", "B10", FULL, "website design little rock ar (880, SD 22)", "website design little rock (590, Question).",
     "A capital that serves a whole state. Customers from all over Arkansas come to Little Rock for state offices, hospitals "
     "and specialists (verify UAMS and the big systems), and professional firms here sell statewide, so their sites need to "
     "say which counties they cover. Places: the River Market District, SoMa (South Main), Hillcrest, the Heights, west Little "
     "Rock, North Little Rock across the river, Conway and Benton. The Clinton Presidential Center and Central High (verify) in "
     "one sentence. Resources: Arkansas SBTDC (lead center at UA Little Rock, verify), Little Rock Regional Chamber, City of "
     "Little Rock.",
     ("generic", "images/heroes/indianapolis-in-hero.jpg"))

# ---------------- Part C: West and Midwest ----------------
city("denver-co", "C1", FULL, "web design denver co (2,900, SD 9)",
     "web design denver (2,900); web design company in denver (1,600); web development company denver (880); wordpress web design "
     "denver (70); affordable web design denver (50); responsive web design denver (50); best web design denver (40); small business "
     "web design denver (30); professional / custom web design denver (10 / 10). FAQ-able: how much website design cost (40). "
     "'web design in colorado' (480) may be used once.",
     "Monthly bills add up in an expensive city. Denver owners pay high rent and many software subscriptions (verify a cost of "
     "living source), so compare honestly a one-time site plus $49 hosting with builder subscriptions; answer the WordPress search "
     "plainly (do not claim a platform INTAKE does not state; say the site is hand-built and owned by the client, and ask in the "
     "demo if they need WordPress). Places: RiNo, LoHi, the Highlands, South Broadway, Capitol Hill, Cherry Creek, Five Points, "
     "and Aurora, Lakewood, Englewood, Arvada. Resources: Denver Economic Development and Opportunity (verify), the Denver SBDC "
     "(verify host), Denver Metro Chamber, SCORE Denver.",
     ("new", "images/heroes/contact-hero.jpg"))
city("colorado-springs-co", "C1", MID, "colorado springs web design company (170, SD 9)",
     "web design in colorado springs (590); website design colorado springs (320, Question); web design colorado springs (210); "
     "web design colorado (210, Question); website design colorado (40).",
     "Olympic City USA and Pikes Peak visitors. The U.S. Olympic and Paralympic Committee headquarters, training center and "
     "museum are here (verify), so coaches, gyms, physical therapists and sports businesses are common; Pikes Peak and Garden of "
     "the Gods bring visitors (verify). Military bases: one sentence only. Places: downtown, Old Colorado City, Manitou Springs, "
     "the Broadmoor area, Briargate, Powers Boulevard, Monument. Resources: Pikes Peak SBDC (verify), Colorado Springs Chamber "
     "and EDC.",
     ("generic", "images/heroes/website-designer-cost-hero.jpg"))
city("fort-collins-co", "C1", MID, "web design fort collins co (320, SD 22)",
     "fort collins website design (260, Question); web design fort collins (210); web developer fort collins (10, Question); fort "
     "collins web development (10, Question).",
     "A university city with its own small companies. Colorado State University and its research spin-offs (verify), Old Town's "
     "shops (verify any claim about Disneyland's Main Street before using it), and craft brewing in one sentence (the Richmond "
     "page covers makers). Many owners compete with Denver agencies for the same searches. Places: Old Town, Campus West, "
     "Midtown on College Avenue, Harmony Road, Loveland, Windsor, Timnath. Resources: Larimer SBDC (verify), Fort Collins Area "
     "Chamber, City of Fort Collins economic health office (verify).",
     ("real",))

city("seattle-wa", "C2", FULL, "web design seattle (2,900, SD 77)",
     "web design seattle washington (1,900); web design seattle wa (1,000); website design seattle (880); seattle web design (880, "
     "Question); web development agency seattle (590); west seattle web design (30); seattle wordpress web design (10). Unused: 'all seattle web design' (reads like a "
     "company name) and 'web design seattle central' (a college course). Ecommerce row: unused or honest FAQ.",
     "Customers who judge websites for a living. With so many tech workers in town (verify), Seattle buyers notice a slow, "
     "clumsy site; speed, accessibility and plain writing matter. Neighborhood identity is strong: Ballard, Fremont, Capitol "
     "Hill, Columbia City, the U District, Georgetown, and West Seattle (searched on its own), plus the Eastside (Bellevue, "
     "Redmond, Kirkland). Also the city's high minimum wage and costs (verify) make every hour count for a small owner. "
     "Resources: Seattle Office of Economic Development, Washington SBDC (verify which office), Seattle Metropolitan Chamber.",
     ("new", "images/heroes/faq-hero.jpg"))
city("spokane-wa", "C2", MID, "web design spokane wa (880, SD 29)",
     "web design spokane (880); spokane website design (880, Question); spokane web design (720, Question); spokane valley web "
     "design (50); best web design spokane (30). FAQ-able: how often should a website be redesigned (30).",
     "Two cities and a big back country. Spokane Valley became its own city in 2003 (verify), so businesses should say which "
     "they serve; and the Inland Northwest's rural towns and north Idaho (Coeur d'Alene, Post Falls) drive in for shopping and "
     "medical care. Riverfront Park (Expo '74, verify), Gonzaga, Fairchild AFB (verify), the South Hill, Browne's Addition, "
     "Kendall Yards, Garland. Resources: Washington SBDC Spokane (verify), Greater Spokane Inc.",
     ("real",))
city("boise-id", "C2", MID, "web design boise idaho (1,000, SD 10)",
     "web design boise id (880); web design boise (720); boise web design (590, Question); web development boise (50); web design "
     "idaho (70). 'thrive web design boise' is another agency's name: unused.",
     "The Treasure Valley's young businesses. Meridian, Nampa, Eagle, Caldwell and Kuna grew fast (verify Census), many "
     "businesses are new, and Micron (verify its expansion) anchors high-tech jobs. Customers search by their own town. Boise's "
     "Basque Block (verify), the North End, Hyde Park, Bown Crossing, downtown's Eighth Street. Do NOT reuse the Nashville "
     "newcomer framing. Resources: Idaho SBDC at Boise State (lead center, verify), Boise Metro Chamber, City of Boise economic "
     "development.",
     ("real",))

city("portland-or", "C3", FULL, "web design portland oregon (1,600, SD 32)",
     "portland oregon website design (1,900, Question); web design portland (1,600); web design portland or (1,000); portland web "
     "design companies (70, Question); freelance / affordable web design portland (10 / 10). 'web design portland maine' / 'me' "
     "(70 / 50): say plainly the page is Portland, Oregon; Maine rows unused.",
     "Five quadrants and a lot of makers. Portland's address system splits the city into quadrants, now including South "
     "Portland (verify the 2020s change), and customers describe where they are that way; small manufacturers and makers "
     "(apparel, bikes, food products; verify a source) sell both locally and online. Vancouver, Washington across the river, "
     "Beaverton, Gresham, Lake Oswego. Neighborhoods: Alberta Arts, Mississippi Avenue, Hawthorne, Division, Sellwood, St. "
     "Johns. Resources: Oregon SBDC at Portland Community College (verify), Prosper Portland, Portland Metro Chamber (verify name).",
     ("new", "images/heroes/why-small-businesses-need-a-website-hero.jpg"))
city("salt-lake-city-ut", "C3", FULL, "website design salt lake city (590, SD 24)",
     "web design salt lake city (590); web design salt lake city utah (590); salt lake city web design company (480, Question); web "
     "development salt lake city (50). Unused: city safety, dry city, temperature, hunting stores, pros and cons, 'design firms'.",
     "A string of cities along I-15. The Wasatch Front runs from Ogden through Salt Lake City to Provo, with Sandy, West Valley "
     "City, Murray, South Jordan and Lehi, and Silicon Slopes tech companies in Lehi and Draper (verify). Customers search by "
     "their own city. Large families and young households (verify Utah median age) drive demand for home services, dentists, "
     "photographers. Neighborhoods: Sugar House, the Avenues, 9th and 9th, downtown, Central 9th. Resources: Utah SBDC at Salt "
     "Lake Community College (verify), Salt Lake Chamber, Salt Lake City Department of Economic Development.",
     ("new", "images/heroes/how-to-hire-a-web-designer-hero.jpg"))
city("reno-nv", "C3", MID, "web design reno nv (480, SD 41)", "wordpress web design reno (10).",
     "The industrial park and Midtown. The Tahoe-Reno Industrial Center east of town (Tesla's Gigafactory and data centers, "
     "verify) brought jobs and newcomers, while Midtown's independent shops and restaurants (verify) and the Riverwalk give the "
     "city a local side away from casinos. Sparks, South Meadows, Northwest Reno, Lake Tahoe trips. Answer the WordPress search "
     "honestly. Resources: Nevada SBDC at UNR (verify), Reno + Sparks Chamber, EDAWN (verify).",
     ("real",))

city("san-francisco-ca", "C4", FULL, "web design san francisco bay area (590, SD 8)",
     "web design san francisco (880); website design san francisco (880); website design in san francisco (590); web design bay area "
     "(480); web design sf (480, Question); web design san francisco ca (390); san francisco website design (390, Question); web design "
     "agency in san francisco (260); wordpress web design san francisco (70); best web design san francisco (40); small business / "
     "responsive / custom / seo / professional web design san francisco (10 each). FAQ-able: how much do web designers charge (210).",
     "Legacy businesses in an expensive city. San Francisco runs a Legacy Business Registry for long-running small businesses "
     "(verify rules and benefits), and its Office of Small Business helps owners with permits (verify). High rents push owners "
     "to watch every cost. Neighborhoods: the Mission, the Sunset, the Richmond, Chinatown, North Beach, the Castro, Bayview; "
     "and the Bay Area towns customers also search (Oakland, Berkeley, Daly City, South San Francisco). Resources: SF Office of "
     "Small Business, SF SBDC (verify host), SF Chamber.",
     ("new", "images/heroes/small-business-website-redesign-hero.jpg"))
city("san-jose-ca", "C4", FULL, "web design san jose (590, SD 12)",
     "san jose web design (720, Question); website design in san jose (590); web design san jose ca (590); website designer san jose "
     "ca (390); website design san jose (110); san jose web design company (40, Question); web design agency san jose (30); web "
     "development san jose (10). FAQ-able: how much do web designers charge for a website (210).",
     "A big city of neighborhood shops under the tech headlines. San Jose is the largest city in the Bay Area (verify), but "
     "most small businesses are neighborhood services in places like Japantown (one of the few remaining in the U.S., verify), "
     "Willow Glen, Little Saigon on Story Road (one sentence; the Orange County page covers Little Saigon in Westminster), "
     "Alum Rock, Berryessa, Santana Row, downtown's SoFA. Resources: City of San Jose's BusinessOwnerSpace (verify), SBDC "
     "serving Silicon Valley (verify host), San Jose Chamber (verify name).",
     ("new", "images/heroes/website-builder-vs-web-designer-hero.jpg"))
city("long-beach-ca", "C4", MID, "web design long beach ca (320, SD 33)",
     "long beach website design (320, Question); web design long beach (140); website design long beach (140, Question). FAQ-able: "
     "how much do web designers charge for a website (210). 'web design long island' is New York: unused.",
     "Its own city next to Los Angeles. The Port of Long Beach (verify ranking) and the trade and logistics around it, plus "
     "neighborhood shopping streets: Retro Row on 4th Street, Belmont Shore's 2nd Street, Bixby Knolls, the East Village Arts "
     "District, and Cambodia Town (verify its status). Do NOT reuse the Los Angeles page's 88 cities framing. Resources: "
     "Long Beach Economic Development (verify), the SBDC at Long Beach City College (verify), Long Beach Area Chamber.",
     ("generic", "images/heroes/pricing-hero.jpg"))

city("fresno-ca", "C5", FULL, "fresno website design (880, SD 42)",
     "web design fresno (720); web design fresno ca (720); fresno web designer (140, Question); fresno web design services (10, "
     "Question). 'loops marketing' row is another agency: unused.",
     "The farm economy's town. Fresno County is one of the top farm counties in the country by value (verify), so packing "
     "houses, equipment dealers, ag services, trucking and farm labor contractors are common, and many families are Hmong, "
     "Punjabi or Latino (verify Census or a credible source; keep it factual). Places: the Tower District, Fig Garden, downtown's "
     "Fulton Street, River Park, Clovis, Sanger, Selma. Resources: the SBDC serving Fresno (verify host), Fresno Chamber, City "
     "of Fresno economic development.",
     ("generic", "images/heroes/kansas-city-mo-hero.jpg"))
city("bakersfield-ca", "C5", MID, "bakersfield website design (480, SD 21)",
     "web design bakersfield (480); web design bakersfield ca (40); web design company bakersfield (10); web design services in "
     "bakersfield (10); website design in bakersfield (10). FAQ-able: how often should websites be redesigned (10).",
     "Oil fields, orchards and the Bakersfield sound. Kern County produces most of California's oil (verify) and big crops like "
     "carrots and almonds (verify); the honky-tonk Bakersfield sound (Buck Owens, Merle Haggard; verify) still shapes local "
     "venues. Do NOT copy the Midland page's boom-and-bust framing; focus on the two economies and the trades that serve both. "
     "Places: downtown, Oildale, the Northwest, Seven Oaks, Rosedale Highway. Resources: SBDC at CSU Bakersfield (verify), "
     "Greater Bakersfield Chamber.",
     ("generic", "images/heroes/indianapolis-in-hero.jpg"))
city("albuquerque-nm", "C5", FULL, "web design in albuquerque (210, SD 30)",
     "web design albuquerque nm (210); web design albuquerque (170); website development albuquerque (30); albuquerque web design "
     "company (30, Question); affordable web design albuquerque (20); web design new mexico (30, from the Nacogdoches tab).",
     "Balloon Fiesta and Route 66. The International Balloon Fiesta each October brings a huge wave of visitors (verify "
     "numbers), and Central Avenue (old Route 66) runs through Nob Hill, downtown and Old Town with independent shops. Kirtland "
     "AFB and Sandia National Laboratories employ many (verify). 'affordable' is searched; incomes run below the national median "
     "(verify Census): keep it brief and do not reuse the Tucson page's wording. Resources: New Mexico SBDC at CNM (verify), "
     "Albuquerque Hispano Chamber, Greater Albuquerque Chamber.",
     ("new", "images/heroes/las-vegas-nv-hero.jpg"))

city("scottsdale-az", "C6", FULL, "web design scottsdale az (880, SD 10)",
     "scottsdale website design (880, Question); scottsdale web design (720, Question); web design scottsdale (320).",
     "High-end service businesses where polish matters. Scottsdale's resorts, golf, spas, med spas, interior designers and "
     "luxury home trades (verify the tourism and industry claims) sell to customers who judge a business by its website before "
     "they call. Old Town, the Waterfront, Kierland, North Scottsdale, Gainey Ranch. Winter visitor season in one sentence. "
     "Resources: Scottsdale Area Chamber, City of Scottsdale economic development, Maricopa SBDC (verify host).",
     ("new", "images/heroes/el-paso-tx-hero.jpg"))
city("mesa-az", "C6", MID, "website design mesa (170, SD 13)",
     "mesa websites (110, Question); web design mesa az (30); web designer mesa (10, Question); web design in arizona (110); arizona "
     "web design (70, Question); web design az (140, from the Amarillo tab).",
     "Not a Phoenix suburb in its own eyes. Mesa is one of the largest cities in Arizona (verify Census rank), with a revived "
     "downtown on the light rail, the Asian District along Dobson Road (verify), Falcon Field, and family neighborhoods. The "
     "Phoenix page covers service-area trades across the Valley; Mesa's page should be about Mesa's own places and customers. "
     "Use the statewide 'web design in arizona' searches in one paragraph. Resources: City of Mesa Office of Economic "
     "Development, Mesa Chamber, Maricopa SBDC (verify).",
     ("generic", "images/heroes/website-cost-per-month-hero.jpg"))
city("tulsa-ok", "C6", MID, "web designers in tulsa (110, SD 25)", "web development tulsa (90); web designer tulsa (170, from the Texarkana tab of the Texas file). FAQ-able: web design rates (40).",
     "Greenwood and Tulsa Remote. The Greenwood District, once called Black Wall Street, and the 1921 Race Massacre (verify "
     "dates and Greenwood Rising museum) shape Tulsa's Black business history today (you may link /black-owned-web-design/ "
     "once); and the Tulsa Remote program paid remote workers to move to the city (verify terms), adding newcomers who freelance "
     "or start businesses. Art deco downtown, the Pearl District, Cherry Street, Brookside, Broken Arrow, Owasso, Jenks. "
     "Resources: Oklahoma SBDC office serving Tulsa (verify host), Tulsa Regional Chamber, Tulsa Economic Development "
     "Corporation (verify).",
     ("generic", "images/heroes/contact-hero.jpg"))

city("oklahoma-city-ok", "C7", FULL, "web design in oklahoma city (880, SD 26)",
     "website design oklahoma city (390, Question); website design oklahoma (110, Question); oklahoma website design (110, "
     "Question); web design in oklahoma (90); okc web design company (20, Question). Unused: rain, designer stores.",
     "Districts built by MAPS. Oklahoma City's voter-approved MAPS sales tax programs (verify history) helped revive districts, "
     "and owners there compete by district: Bricktown, Midtown, Automobile Alley, the Plaza District, the Paseo Arts District, "
     "the Asian District on Classen (verify), Film Row, Stockyards City. Plus energy and aviation (Tinker AFB, verify). Use the "
     "statewide searches in one paragraph. Resources: Oklahoma SBDC office serving OKC (verify host), Greater Oklahoma City "
     "Chamber, The Alliance for Economic Development of OKC (verify).",
     ("new", "images/heroes/cleveland-oh-hero.jpg"))
city("omaha-ne", "C7", FULL, "web design omaha ne (1,000, SD 57)",
     "web design omaha (1,000); website design omaha (140). FAQ-able: how much web design cost (40).",
     "Two weeks in June and a lot of headquarters. The NCAA Men's College World Series fills the city each June (verify), and "
     "Omaha hosts major headquarters (Berkshire Hathaway, Union Pacific, Mutual of Omaha; verify) whose staff are local "
     "customers and whose purchasing teams buy from small vendors. Neighborhoods: the Old Market, Benson, Dundee, the Blackstone "
     "District, Aksarben Village, west Omaha, and Council Bluffs, Iowa across the river. Resources: Nebraska Business Development "
     "Center at UNO (verify), Greater Omaha Chamber, SCORE.",
     ("generic", "images/heroes/black-owned-web-design-hero.jpg"))
city("des-moines-ia", "C7", FULL, "web design des moines (590, SD 46)",
     "web design des moines iowa (590); des moines website design (480, Question); web development des moines (50); website designers "
     "in des moines (50); web design des moines ia (50); des moines web development (50, Question). FAQ-able: how much do web "
     "designers charge (210); how much does web design cost (170); web design rates (40).",
     "Insurance agencies and the State Fair. Des Moines is an insurance capital (verify), so independent agents, advisors and "
     "claims-related services are common and need sites that show licenses and carriers; the Iowa State Fair in August draws "
     "huge crowds (verify) for food vendors and makers. Places: the East Village, Ingersoll Avenue, Valley Junction in West Des "
     "Moines, Beaverdale, Ankeny, Urbandale, Waukee. Resources: Iowa SBDC (verify which office), Greater Des Moines "
     "Partnership, SCORE.",
     ("generic", "images/heroes/seo-web-design-hero.jpg"))

city("minneapolis-mn", "C8", FULL, "web design minneapolis (590, SD 19)",
     "web design minneapolis mn (880); web design company minneapolis (260); minneapolis web designer (70, Question); responsive web "
     "design minneapolis (30); web design eden prairie mn (30); ('web design st cloud mn' is a different city: unused); ecommerce / custom / professional / wordpress / small business web design minneapolis (10 each); web design in "
     "minnesota (170). Unused: target headquarters.",
     "Lake Street and immigrant entrepreneurs. Lake Street's small businesses rebuilt after 2020 (verify how the city and "
     "nonprofits documented it; respectful and factual), and East African, Latino and Hmong owners (verify sources) run many "
     "shops and restaurants in Cedar-Riverside, along Lake Street and in the Twin Cities. Northeast's arts district, Uptown, "
     "North Loop, and suburbs Edina, Bloomington, Eden Prairie, St. Paul next door. Resources: City of Minneapolis small "
     "business team (verify), Minnesota SBDC (verify office), Minneapolis Regional Chamber, Lake Street Council (verify).",
     ("new", "images/heroes/web-design-packages-hero.jpg"))
city("madison-wi", "C8", MID, "madison website design (480, SD 15)",
     "web design madison wi (390); web madison (260, Question); website designer madison wi (50, Question). Unused: biggest web "
     "design companies.",
     "Farmers, the Capitol and the university. The Dane County Farmers' Market circles the Capitol Square on Saturdays (verify "
     "its 'largest producer-only' claim), so farms and food makers sell direct; UW-Madison and state government shape the "
     "rest, and Epic Systems in Verona (verify) brought many health tech workers. State Street, Monroe Street, Williamson Street, "
     "Atwood, Middleton, Fitchburg. Resources: Wisconsin SBDC at UW-Madison (verify), Greater Madison Chamber, City of Madison "
     "Office of Business Resources (verify).",
     ("generic", "images/heroes/sacramento-ca-hero.jpg"))
city("grand-rapids-mi", "C8", FULL, "web design grand rapids (1,600, SD 23)",
     "website design grand rapids (1,600); web design grand rapids michigan (1,600); grand rapids web design (1,300, Question); grand "
     "rapids website development (90, Question); web development grand rapids (30); grand rapids web design company (20, Question). "
     "'web design grand junction' is Colorado: unused.",
     "Furniture City and the Medical Mile. Office furniture makers (Steelcase in Grand Rapids, MillerKnoll in nearby Zeeland; "
     "verify) built a design and manufacturing supply chain, and the Medical Mile on Michigan Street grew a health sciences "
     "cluster (verify). Breweries in one sentence at most. Neighborhoods: Eastown, Wealthy Street, East Hills, Bridge Street on "
     "the West Side, Uptown; suburbs Wyoming, Kentwood, Grandville, Rockford. Resources: Michigan SBDC (headquartered at Grand "
     "Valley State, verify), Grand Rapids Chamber, Start Garden (verify).",
     ("new", "images/cost-page-hero.jpg"))

city("detroit-mi", "C9", FULL, "web design detroit (590, SD 21)",
     "web design detroit michigan (590); detroit web design company (50, Question); affordable web design detroit (20); detroit web "
     "design agencies (10, Question). FAQ-able or unused: web design and web development difference (70).",
     "Neighborhood storefronts coming back. Motor City Match gives grants and help to open storefront businesses (verify "
     "program details), and corridors like the Avenue of Fashion on Livernois, Eastern Market, Corktown, Southwest Detroit's "
     "Mexicantown and West Village show the comeback (verify). Detroit is majority Black (verify Census); you may link "
     "/black-owned-web-design/ once. Auto suppliers in one sentence. Resources: Detroit Economic Growth Corporation (Motor City "
     "Match), TechTown Detroit, Michigan SBDC, Detroit Regional Chamber.",
     ("generic", "images/heroes/las-vegas-nv-hero.jpg"))
city("cincinnati-oh", "C9", FULL, "web design cincinnati (880, SD 20)",
     "web design cincinnati ohio (590); cincinnati web design agency (30, Question); affordable web design cincinnati (10). FAQ-able: "
     "web design rates (40); how much website design cost (40); how long does website design take (10).",
     "Findlay Market and Over-the-Rhine. Findlay Market is Ohio's oldest continuously operated public market (verify) and its "
     "vendors, plus the restaurants and shops of a revived Over-the-Rhine, show the city's small business core; chili parlors "
     "and the corporate headquarters (P&G, Kroger; verify) round it out. Northern Kentucky (Covington, Newport) in one sentence, "
     "not as the lead. Places: OTR, Northside, Hyde Park, Oakley, Walnut Hills, Pleasant Ridge, West Chester. Resources: "
     "Cincinnati USA Regional Chamber, the Ohio SBDC office serving Cincinnati (verify host), MORTAR (verify), City of "
     "Cincinnati Department of Community and Economic Development.",
     ("generic", "images/heroes/faq-hero.jpg"))
city("columbus-oh", "C9", FULL, "website design columbus (590, SD 22)",
     "columbus ohio web design (880, Question); columbus web design company (260, Question); columbus web designers (140, Question); "
     "columbus web design agency (10, Question). Say Columbus, Ohio (not Georgia or Indiana).",
     "A test-market city that keeps growing. Columbus is known as a place brands test new products because its population "
     "looks like the country (verify a credible source), and it is Ohio's largest and fastest-growing city (verify Census), "
     "with Ohio State and the Intel project in Licking County (verify current status). Neighborhoods: the Short North, German "
     "Village, Clintonville, Olde Towne East, Franklinton; suburbs Dublin, Westerville, Grove City, Hilliard. Resources: Ohio "
     "SBDC at Columbus State (verify), Columbus Chamber, City of Columbus small business programs.",
     ("new", "images/heroes/website-designer-cost-hero.jpg"))

city("pittsburgh-pa", "C10", FULL, "web design pittsburgh pa (480, SD 12)",
     "web design pittsburgh (720); from keywords/Web-Design-5-Cities-Recheck.xlsx: pittsburgh web designs (720, SD 17); pittsburgh website design (480); pittsburgh web design (480, Question); pittsburgh web designer (110); website development pittsburgh (90); pittsburgh web design company (70, Question); pittsburgh web developers (30, Question); pittsburgh website design agency (10). FAQ-able: web design rates (40); how much web design cost (40).",
     "Ninety neighborhoods split by rivers and hills. Pittsburgh counts about 90 neighborhoods (verify), and rivers, hills and "
     "tunnels mean customers think in neighborhoods and 'which side of the river'. The economy runs on eds and meds (UPMC, Pitt, "
     "Carnegie Mellon; verify) and robotics. Places: the Strip District, Lawrenceville, Squirrel Hill, Bloomfield, the South "
     "Side, Mt. Lebanon, Cranberry. Resources: Pennsylvania SBDC at Pitt and Duquesne (verify), Greater Pittsburgh Chamber, URA "
     "(Urban Redevelopment Authority) small business help (verify).",
     ("generic", "images/heroes/how-to-hire-a-web-designer-hero.jpg"))
city("philadelphia-pa", "C10", FULL, "philadelphia web designer (720, SD 25)",
     "web designers in philadelphia (590). Unused: 'apa style web', card examples.",
     "Commercial corridors and city paperwork. Philadelphia has hundreds of neighborhood commercial corridors (verify the "
     "count) and city programs such as the Storefront Improvement Program (verify), and every business needs a Commercial "
     "Activity License (verify); a site should show where the shop is on its corridor and what licenses a trade holds. "
     "Neighborhoods: Fishtown, Passyunk Avenue in South Philly, Germantown Avenue, Chinatown, Kensington, Northern Liberties, "
     "Manayunk; suburbs in Montgomery and Delaware counties. The keyword is 'web designer' (a person): one short honest "
     "paragraph on hiring one person (do NOT copy the Chicago page's agency versus one person section). Resources: City of "
     "Philadelphia Department of Commerce, Pennsylvania SBDC at Temple and Wharton (verify), Philadelphia Chamber.",
     ("new", "images/heroes/los-angeles-ca-hero.jpg"))

BATCH_PART = {"A": "Part A (Texas)", "B": "Part B (South and East)", "C": "Part C (West and Midwest)"}


def assign_photos():
    use = Counter()
    out = {}
    batches = {}
    for slug, c in C.items():
        batches.setdefault(c["batch"], []).append(slug)
    i = 0
    for batch, slugs in batches.items():
        taken = set()
        for slug in slugs:
            picks = []
            while len(picks) < 3:
                cand = sorted(POOL, key=lambda p: (use[p], (POOL.index(p) * 7 + i) % len(POOL)))
                for p in cand:
                    if p not in taken and p not in picks:
                        picks.append(p)
                        use[p] += 1
                        taken.add(p)
                        break
                i += 1
            out[slug] = picks
    return out, use


def size_of(path):
    for k, v in SIZES.items():
        if path.startswith(k):
            return v
    return "?"


def main():
    photos, use = assign_photos()
    heroes_new = [s for s, c in C.items() if c["hero"][0] == "new"]
    lines = []
    lines.append("## The cities\n")
    lines.append("Keyword numbers verified from the Wave 4 keyword files (Ubersuggest US, pulled Oct 16 2026): the city tabs of "
                 "keywords/Web-Design-Texas-Cities-Keywords.xlsx, -South-East-, -West-Midwest- and -National-Cities-Keywords.xlsx. "
                 "Every 10+ row per tab is in docs/writers/kw-wave4-10plus.txt. Volume is searches a month; SD is SEO difficulty.\n")
    cur = None
    for slug, c in C.items():
        part = c["batch"][0]
        if part != cur:
            cur = part
            lines.append(f"### {BATCH_PART[part]}\n")
        lines.append(f"#### {slug} (batch {c['batch']}, aim for {c['words']} words of your own copy)")
        lines.append(f"- Main: {c['main']}")
        lines.append(f"- Supporting: {c['supporting']}")
        lines.append(f"- Angle: {c['angle']}")
        h = c["hero"]
        if h[0] == "new":
            lines.append(f"- Hero: NEW planned Artistly hero `images/heroes/{slug}-hero.jpg` (write `alt` and `desc` for it), "
                         f"`fallback: {h[1]}`, `fallback_alt: \"{GENERIC[h[1]]}\"`.")
        elif h[0] == "real":
            size, author, lic = REAL[slug]
            lines.append(f"- Hero: the real photo of the city already in the repo, `image: images/cities/{slug}.jpg` ({size}, Wikimedia "
                         f"Commons, by {author}, {lic}). Open it with Read, write an alt that describes exactly what it shows (you may "
                         f"name the city; name a building only if you verified it is that building), no fallback. Add one line near the "
                         f"sources, like the Tyler page: `<p class=\"small\">Photo at the top of this page: {author}, {lic}, via Wikimedia "
                         f"Commons.</p>`")
        else:
            lines.append(f"- Hero: reuse `image: {h[1]}` (no new file, no fallback), `alt: \"{GENERIC[h[1]]}\"` (keep this alt or "
                         f"tighten it after looking at the photo; it must not claim the city).")
        lines.append("- In-body photos: " + "; ".join(f"`{p}` ({size_of(p)})" for p in photos[slug]))
        lines.append("")
    body = "\n".join(lines)
    head = HEAD.replace("{N_NEW}", str(len(heroes_new))).replace("{N}", str(len(C)))
    OUT.write_text(head + "\n" + body)
    print(f"{len(C)} cities, {len(heroes_new)} new heroes, photo uses: max {max(use.values())}, min {min(use[p] for p in POOL)}")


HEAD = """# Writer brief: Wave 4 city pages (Oct 17 2026)

Generated by `python3 docs/writers/wave4_brief_gen.py`. Read first, in full: `CLAUDE.md`, `CITY-PAGES-WAVE4.md`,
`INTAKE.md`, `docs/WRITING-GUIDE.md` (every rule there applies unless this brief overrides it), then the model
pages `src/pages/web-design/st-louis-mo.html`, `src/pages/web-design/tucson-az.html` and
`src/pages/web-design/wilmington-nc.html`. Your pages use the same front matter shape, templates, macros and image
handling. INTAKE.md wins over everything.

{N} cities in total ({N_NEW} planned new Artistly heroes; the rest reuse photos already in the repo).

## Your files
- `src/pages/web-design/<slug>.html` for each assigned city: `url: "/web-design/<slug>.html"`, `type: area`,
  `city_name`, `state_name` (full name), `crumb: "City, ST"`, `summary:` (max 160 characters, one line for the
  city directory), `schema_service: {name: "Web design in City, State", type: "Web design"}`.
- `docs/writers/w4-<batch>.md` (for example `w4-a1.md`): per page, the main and supporting keywords used, every
  fact stated with its source URL, and what you left out because you could not verify it. The fact-checkers read it.
- Do NOT edit shared files (build.py, templates, static, site.json, scripts, SERVICES.md, docs/keyword-plan.md,
  other writers' pages, any existing city page). All Wave 4 cities are already in site.json with their region
  group. A city whose page does not exist yet is left out of menus and pills by the build, so:
  - Region pills: `{{ m.area_pills(group='<group>', exclude='<slug>') }}` with your city's group key:
    Texas: `east-texas`, `houston`, `dfw`, `austin`, `south-texas`, `central-west`; elsewhere: `georgia`,
    `florida`, `south` (AL, MS, LA, AR, TN, KY, OK), `east` (NC, SC, VA, PA, NY), `west`, `midwest`.
  - `m.related([...])` may link `area:<slug>` ONLY for pages that already exist (any page in
    src/pages/web-design/ when you start, or your own batch's pages). Services and guides: use slugs from
    src/data/site.json (`small-business-website`, `contractor-website-design`, `seo-web-design`,
    `small-business-website-redesign`, `affordable-website-design`, `web-design-for-plumbers`,
    `roofing-contractor-website-design`, `web-design-for-law-firms`, `web-design-for-therapists`,
    `guide:small-business-website-cost`, `guide:how-much-does-a-website-designer-cost`, `guide:website-cost-per-month`,
    `guide:web-design-packages-explained`, `guide:website-builder-vs-web-designer`, `guide:how-to-hire-a-web-designer`,
    `guide:why-small-businesses-need-a-website`; check the exact slugs in site.json before using one).

## Keyword rules
The main target goes in the title (50 to 65 characters), the H1, the first paragraph and one H2, naturally.
Supporting terms go in where they read naturally (an H2 or H3, body copy, the description, the summary); the
Question-type rows become FAQ questions where they read like real questions. Never stuff. Never use another
agency's brand name. A row about a different place with the same name is never used as if it were this city;
where searchers mix the two up, say once which place the page is about.

## Honesty rules (the ones that matter most here)
- Dominion Web Design Pro is Maurice Johnson in Big Sandy, East Texas, building remotely. No office, no team, no
  clients in the city. Use `{{ m.no_office('City') }}` exactly once. Never say Maurice has built for any business
  there or any named business anywhere. No reviews, ratings, awards, job counts, years in business, guarantees,
  ranking promises. Never "certified", "top-rated", "#1", "unlimited", "guarantee" in any form, "testimonial",
  "5-star", "our clients", "happy clients", "100+".
- Texas pages (Part A) may say Maurice is a Texan building for Texas businesses from Big Sandy. Still no office,
  team or clients in that town.
- Prices exactly: Starter $497, Pro $997, Agency $1,997, one time. Starter is live in 7 to 14 days; Agency pages
  arrive in waves, the first live inside two weeks (do not state a turnaround for Pro beyond what INTAKE says).
  Pro chat widget free 14 days then $297/mo. Agency includes AI phone agent SETUP; the agent is free for 7 days
  then $297/mo for up to 750 minutes, cancel any time, and it is not part of the one-time price. Hosting,
  maintenance and updates included while the client keeps the AI agent, otherwise $49/mo. Online stores and
  custom software are not in the packages: say so honestly if a keyword asks. Platform (WordPress, Shopify):
  INTAKE does not name one, so never claim one; say the site is hand-built, the client owns it, and to raise
  any platform need when asking for the demo. Keep "we do not sell page counts" if you discuss page counts.
- Phone: (903) 636-7511 is answered by an AI receptionist any hour that can transfer callers to Maurice. Never
  say a person always answers.
- Spanish or other languages: INTAKE does not say Maurice writes them. Never claim it.
- No em dashes or en dashes anywhere (also not in front matter, alt text or source labels). No eyebrow labels.
  American spelling. No banned phrases (CLAUDE.md list).
- The template adds the `dwdp:handwritten` mark; do not add it yourself.

## Make every page different (limit 15% Jaccard on 5-word shingles, against ALL city pages)
There are already 52 city pages and you are writing alongside other writers. Each city below has an assigned
ANGLE: build the outline around it, and choose a section order and section types of your own (a table, a
steps list, a split with a photo, a checklist, a short case walk-through of a typical owner, a grid of places).
Do not copy any section shape from another city page: no "Four reasons a X business would hire..." grid, no
"questions worth asking" table, no "Help that already exists for X owners" heading, no seasonal four-step list
copied from Wilmington, no "How our packages map to X" list. The remote / East Texas disclosure is
`m.no_office('City')` plus at most one or two fresh sentences of your own. "Getting started" is at most one
short line plus `m.demo_box('a fresh sentence')`. Write every heading and paragraph fresh; vary phrasing
between your own cities too (your cities are deliberately neighbors or similar, so this matters most there).
Before writing, skim two or three existing pages of nearby cities (listed in src/pages/web-design/) so you do
not repeat them. Word targets are given per city; short pages for small towns must stay honest and specific,
never padded (check.py may warn on word count for short pages; a warning is fine, an error is not).

## Research and sources
Research each city with WebSearch before writing (WebFetch may be blocked; verify from search results of the
official or credible source). Budget about 6 to 10 searches per city (fewer for the short pages). Every
"(verify)" in an angle is a claim you must confirm or drop. State only facts you verified, and cite each one in
`m.sources([...])` with a real URL that supports it. Cover: the city's small business makeup, real
neighborhoods, corridors or suburbs a resident would recognize, its chamber of commerce and small business
resources (SBDC, SCORE chapter, city small business office), and why local search matters there. When citing
Google on local ranking use https://support.google.com/business/answer/7091?hl=en (relevance, distance,
prominence). Keep numbers to ones you can source (Census QuickFacts, SBA Office of Advocacy 2024 or 2025 state
profiles, city or chamber pages, reputable news). Prefer current (2024 to 2026) figures. If you cannot verify
it, leave it out.

## Images
- Hero front matter for a NEW planned hero:
  ```yaml
  hero:
    image: images/heroes/<slug>-hero.jpg
    alt: "<describes the planned photo; never claims a real landmark>"
    desc: "Artistly scene: <bright scene of a real small business owner's setting typical of that city, no readable signs, no text, no logos, no recognizable faces, no real landmarks presented as fact>, wide cinematic landscape shot, subject positioned on right third of frame, well lit"
    fallback: <assigned fallback>
    fallback_alt: "<assigned fallback alt>"
    position: "65% 50%"
    lead: "One or two short sentences."
  ```
- Hero that reuses an existing photo: `image:` the assigned path, `alt:`, `position:`, `lead:` only.
- In-body: use the three assigned existing photos with `{{ img("path", "alt", w, h) }}` (sizes given; at least
  two, all three if they fit). Open each image with the Read tool first (files are in src/static/) and write alt
  text that describes what is really in it. Never write alt text that claims a photo shows the city (except the
  real city photos named above). You may swap ONE assigned photo for another from the usable pool in
  docs/WRITING-GUIDE.md if it fits the angle much better, as long as no photo repeats on the page (say so in your
  notes file). Never use a photo that names or shows a different real city (images/cities/*, images/body/<city>-*).

## Check before you report
```
python3 build.py --out /tmp/claude-0/w4-<batch>/dist
python3 scripts/check.py --skip-links --dist /tmp/claude-0/w4-<batch>/dist --only /web-design/<slug>.html
python3 scripts/similarity.py --dist /tmp/claude-0/w4-<batch>/dist
```
Fix every ERROR. In the similarity output look at every pair that involves your pages and keep each at or under
15% (aim for under 8%; other writers are writing at the same time, so re-run at the end). Do not touch git.
Report: pages, word counts, highest similarity pair per page, searches used, anything unverified.
"""

if __name__ == "__main__":
    main()
