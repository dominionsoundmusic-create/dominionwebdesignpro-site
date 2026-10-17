# Decisions log (Playbook 2.0 rebuild, Oct 12 2026)

Maurice was not available to approve anything during this run (CLAUDE.md: run straight through).
Each decision below was made from INTAKE.md, CLAUDE.md, the keyword data and the live site, and can
be reversed later.

## Build system and structure

1. **Build system copied from Phoenix Pool Cleaning Pro (branch `build`), words not copied.**
   build.py (Jinja2, writes dist/), scripts/check.py, check_old_urls.py, similarity.py,
   grep_check.py, keyword_plan.py, responsive_check.js, the templates and macros (img, faqs,
   sources), site.css, site.js, the self-hosted Inter woff2 font, the site.json structure and
   netlify.toml. The speed work is unchanged: WebP srcset at 480/800/1200/1600/1920 (up to each
   photo's own width), preloaded hero with fetchpriority high, woff2 font preloaded. The full-width
   layout (text, photos, cards and bands share one `--rail` left and right edge) is unchanged. Every
   value, color, label and sentence was replaced for Dominion Web Design Pro.
2. **Image paths.** Photos live in src/static/ at the paths the live site used (/images/...,
   /demo-images/...), so every old image URL still resolves. build.py takes image paths relative to
   src/static and writes WebP copies to /images/w/ (named after the full path, because
   demo-images/*/1.jpg would otherwise collide).
3. **Old live site kept as the reference in docs/old-site/** (every HTML file, _redirects, _headers,
   sitemap.xml, robots.txt, and files.txt = `git ls-files` of main). scripts/check_old_urls.py reads it.
4. **dist/ is committed and Netlify publishes it** (`publish = "dist"` in the new netlify.toml, no
   build command), the same as the Phoenix build. `[functions] directory = "netlify/functions"` keeps
   the Site Check function deploying; its own `config.path` serves /api/seo-audit. The function's
   logic was not touched.
5. **URLs.** Every page the live site served keeps its URL and its canonical exactly as today:
   /about.html, /service-areas.html, /how-city-pages-work.html, /small-business-website-cost.html,
   /privacy-policy.html, /terms.html and all /web-design/<town>.html pages stay flat .html files
   (Netlify Pretty URLs keeps serving both forms as now). Folder URLs stay folders. New city pages
   use the same /web-design/<town>.html pattern. New pages use folder URLs (/pricing/, /faq/ ...).

## Tool pages

6. **Tool pages copied through, not re-templated.** /demo.html, /demo-generator.html, /site-check/,
   /compare/, /tools/, /intake/, /intake/thanks/ and /contact/thanks/ have dark inline-styled layouts
   and global CSS selectors (nav, footer, a) that would collide with the new header. CLAUDE.md says
   "if in doubt, copy the tool page through unchanged", so they keep their own header and footer.
   Static HTML additions only (scripts/patch_tool_pages.py): the handwritten marker, "John 3:16" in
   the existing top strip, the Duplantis quote line under the nav where missing, and the live site's
   own branded EN/ES language bar on the three pages that lacked it (intake, intake thanks, contact
   thanks). Visible wording was edited in a few places to remove em dashes and one "guarantee" (an
   intake form label; the field name is unchanged). scripts/check_tool_pages.py proves every script
   block and every form, input, textarea, select, option and button tag is byte for byte the same.
7. **Tool pages are exempt from the FAQ and hero-image rules.** Adding FAQ blocks or hero photos would
   mean re-templating them (decision 6). They are listed in docs/qa.md as such.

## Pages and keywords

8. **Page list from the keyword data** (SERVICES.md, docs/keyword-plan.md). Core: home, /services/,
   /pricing/, /how-it-works/, /about.html, /contact/, /faq/, /service-areas.html, /web-design/,
   /how-city-pages-work.html, privacy, terms, 404. Services: small business, contractor, SEO web
   design, redesign, affordable, plumbers, roofing contractors, law firms, therapists. Seven guides.
   26 city pages.
9. **/services/ added** (Playbook Prompt 8): "web design services" has 8,100 searches a month and the
   live site had no services overview.
10. **/pricing/ built** ("small business website package" 170/mo SD 13, "web design quotes" 210 SD 19)
    and the packages stay on the home page as now (#pricing anchor kept).
11. **/contact/ built.** The live site had /contact/thanks/ but no /contact/ page. The new contact page
    carries the same `homepage-contact` Netlify form as the home page (same name, attributes, hidden
    input, honeypot and field names), rendered in static HTML.
12. **Trade pages:** plumbers (720/mo SD 16), roofing contractors (50/mo SD 35), law firms (2,900/mo
    SD 42) and therapists (590/mo SD 32) have keywords in the data and got pages. HVAC, electricians
    and landscapers have no keyword in the data, so no page (recorded in SERVICES.md).
13. **Retired hubs.** restaurant-, real-estate-, professional- and ecommerce-website-design have no
    10+ keyword (ecommerce rows are online-store builds, which the INTAKE packages do not include):
    301 to /small-business-website/. medical-website-design 301s to /web-design-for-therapists/,
    the closest page the data supports. The old wildcard rules for these hubs were re-pointed to the
    same targets so no redirect chains.
14. **website-design-for-contractors.html folded into /contractor-website-design/** (its research
    moved there) and 301-redirected, both the .html and extensionless forms, so the two pages no
    longer compete for the same keyword.
15. **Redesign and affordable pages at new URLs.** /small-business-website-redesign/ (2,400/mo) and
    /affordable-website-design/ (720/mo) avoid the existing /website-redesign/ and
    /affordable-web-design/ redirect sources; those rules were kept and re-pointed from
    /small-business-website/ to the new, closer pages.
16. **Wave 2 cities** (New York, San Diego, Chicago, Orange County, Huntsville AL, Richmond VA, Tucson,
    Louisville, Jacksonville FL, Fort Lauderdale, Las Vegas, Wilmington NC, Vancouver WA and the rest)
    are listed in docs/keyword-plan.md with keyword, volume and SD, not built.
17. **10+ rule.** scripts/keyword_plan.py classifies all 1,501 rows and fails if any of the 794 rows
    at 10+ searches is unclassified. Every one is assigned to a page or listed as unused with a reason.

## Facts and claims

18. **Package facts from INTAKE.md, not the live site.** The live pricing said the Agency AI phone
    agent was "free 14 days"; INTAKE says the phone agent is free for 7 days, then $297/mo for up to
    750 minutes, and that the AI chat widget (Pro) is free for 14 days. The new site follows INTAKE.
    The live city pages' "Unlimited pages" for $1,997, the three-month minimum and the "ten months
    instead of twelve" yearly price are not in INTAKE and were removed. scripts/check.py fails on them.
19. **Pricing lives in one place.** The three plans, Stripe links, hosting note and the "We do not
    sell page counts" paragraph are in src/data/site.json and rendered by one macro on the home page
    and /pricing/. Each card has the Stripe buy button and "Or get a free demo first".
20. **"Most Popular" on Pro** (INTAKE) is shown as a small flag next to the plan name, not as an
    eyebrow label above the heading.
21. **Phone honesty.** Every page says the line is answered by an AI receptionist any hour that can put
    the caller through to Maurice. scripts/check.py fails a page without that note.
22. **Dominion Solar Pro removed from the footer.** INTAKE lists only AI Voice Agent Pros, Dominion
    Review Pro and Dominion AI Agency as sister brands to mention.
23. **The GoHighLevel affiliate link** on the live home page was not carried into the new home page
    (the /tools/ page, copied through, still has its own software notes). Maurice can add it back.
24. **Footer "Review us on Google" link kept** (the live footer's g.page review link). It asks for a
    review; it does not display any review.
25. **"Maurice grew up in Gilmer"** is Maurice's own statement on the live Gilmer page and was kept on
    that page as his statement.
26. **Address** appears only on privacy, terms and in the LocalBusiness (ProfessionalService) schema,
    as on the live site.
27. **Copyright line:** "© 2026 Dominion Web Design Pro, a d/b/a of Dominion Digital Group", from the
    INTAKE business name.

## Design

28. **Header in brand blue #1D4ED8** with white links, the gold call button and the live site's EN/ES
    pill (dark with a gold outline, active language in blue). The John 3:16 and Duplantis quote bar sits
    above it in near-black with the Facebook and YouTube icons at the right (the top social links).
29. **Bands:** pages are pure white with color bands: the first band on a page is deep blue (white
    text), the second gold #F5A623 (near-black text, for contrast), the closing call band near-black.
    The FAQ block is white. No pale tinted sections.
30. **Missing photos show as a brand-blue block** (CLAUDE.md), not as a stand-in photo: heroes become
    the blue gradient hero band, in-body figures a blue block of the planned size. All are listed in
    docs/image-list.md with Artistly prompts.
31. **Demo photos with words printed on them are not used on content pages** (accounting, most
    chiropractic, construction, three of the legal, pest control and one each of landscaping, roofing
    and real estate) and default/4.jpg (shows a coffee chain's logo).

## Atlanta add-on (Oct 12 2026, ATLANTA-ADDON.md)

32. **Keyword source and the 10+ rule.** keywords/Atlanta-Web-Design-Keywords.xlsx (385 unique keywords,
    154 at 10+). scripts/keyword_plan_atlanta.py classifies every one and writes the "Atlanta add-on"
    section of docs/keyword-plan.md; scripts/keyword_plan.py runs it and fails if any 10+ keyword is
    unclassified. 44 are assigned to pages, 110 listed as unused with a reason.
33. **Six pages.** NEW /black-owned-web-design/ (national service page, target "black owned web
    developers" 880/mo SD 10), STRENGTHENED /web-design/atlanta-ga.html (same URL; adds "web developers
    in atlanta" 1,300 SD 11 and the other Atlanta phrases), NEW /web-design/decatur-ga.html,
    /web-design/mcdonough-ga.html, /web-design/conyers-ga.html, /web-design/douglasville-ga.html. City
    pages keep the flat /web-design/<town>.html pattern every other city page uses.
34. **Black-owned wording.** INTAKE section 7: the business is Black-owned (Maurice Johnson, owner) and
    the site may say so. No MBE, NMSDC, state or city certification and no association membership is
    claimed anywhere; certification programs are explained on the page only as something a reader can
    check for any vendor. "Certified" stays a banned word in scripts/check.py.
35. **The black-owned page is type "service"** (it sells the same packages to a defined audience) but it
    is not added to the Services menu; it is linked from the footer Company list, the About page and
    the Atlanta page, as ATLANTA-ADDON.md asks.
36. **Georgia cities with 0 measured volume** (South Fulton, College Park, East Point, Union City,
    Fairburn, Stonecrest, Lithonia, Stockbridge, Riverdale, Jonesboro, Morrow, Forest Park) get no page;
    listed as "Atlanta wave 2 (0 measured volume)". Georgia cities that do show 10+ but were not in the
    add-on (Macon, Marietta, Athens, Buford, Kennesaw, Columbus, Gainesville) are listed as Atlanta
    wave 2 candidates rather than built, since ATLANTA-ADDON.md names the pages for this run.
37. **County-government searches** ("clayton county website" 140, "henry county website" 110, "clayton
    website", "lithonia website") are people looking for the government's own site: unused.
38. **Links.** The four new towns are in site.json's Georgia area group, so they appear automatically in
    the city directory, the service areas pills, the footer city list and the sitemap. The service
    areas Georgia panel, the Atlanta page and the Lawrenceville page link them by name.

## Wave 2: 13 national city pages (Oct 16 2026, CITY-PAGES-WAVE2.md)

39. **Branch.** All Wave 2 work is on `cities-wave2`, pushed as it goes. Nothing merged or pushed to main.
40. **Keyword numbers re-read from the files.** Every main and supporting number in CITY-PAGES-WAVE2.md matched the
    city tabs of keywords/Web-Design-National-Cities-Keywords.xlsx and the ALL tab of
    keywords/Web-Design-5-Cities-Recheck.xlsx. scripts/keyword_plan_wave2.py classifies every 10+ row of the 13
    cities (target, supporting, FAQ question, or unused with a reason) and fails on anything unclassified; it runs
    from scripts/keyword_plan.py. Phrases for these cities in the original Web-Design-Keywords.xlsx (for example
    "website design company chicago" 1,900) now count as supporting keywords on the new pages instead of
    "Wave 2 candidate"; "web design kc" and "web design kansas city mo" from the Atlanta file go to the Kansas City page.
41. **Orlando.** The only other 10+ Orlando web design phrase is "duogeeks web design in orlando", another agency's
    brand: unused. The page relies on its main term plus generic cost questions as FAQs.
42. **Kansas phrases.** "web design kansas" (30) and "kansas web design" (30) are assigned to the Kansas City page as
    supporting, since that page covers the Kansas side of the metro; "web design cleveland tn" and "web design san
    luis obispo" are different places and unused.
43. **Grouping.** A new site.json area group "Other U.S. cities" (key other-us) holds the 13 pages, so they appear in the
    city directory, the Cities menu, the footer city list, the service areas page (new "Other U.S. cities" pills plus
    links in the "rest of the country" panel) and the sitemap, all from the one list.
44. **One angle per city.** To keep every pair of city pages under 15% similarity and to make each page useful, each
    city got its own angle (docs/writers/BRIEF-WAVE2.md): St. Louis city/county split, Kansas City two-state metro,
    Indianapolis business-to-business firms, Phoenix service-area trades, Las Vegas locals' economy, Sacramento capital
    economy, Los Angeles comparison shopping across 88 cities, San Diego neighborhood business districts, Miami
    bilingual market, Orlando visitor versus resident economy, Nashville newcomers, Chicago agency versus one person
    and neighborhood corridors, Cleveland old houses and design versus development.
45. **Images.** No new in-body images: each page reuses generic photos already in the repo (demo-images and generic
    images/body or images/contractors photos, none showing another named city), with alt text that describes what is
    actually in the photo. Each city has one planned hero (images/heroes/<slug>-hero.jpg, 1920x1080) listed in
    docs/image-list.md; until it arrives the build shows a reused generic hero (`fallback`) with its own accurate alt.
46. **Spanish on the Miami page.** INTAKE.md does not say Maurice writes Spanish copy, so the page does not claim it;
    it explains what a bilingual site needs and how to get the Spanish reviewed by a fluent person.

## Wave 3: 8 more national city pages (Oct 17 2026, CITY-PAGES-WAVE3.md)

47. **Branch.** All Wave 3 work is on `cities-wave3` (started from cities-wave2), pushed as it goes. Nothing merged or
    pushed to main. The 13 Wave 2 pages were not rewritten; they are included in the similarity check.
48. **Keyword numbers re-read from the files.** Every main and supporting number in CITY-PAGES-WAVE3.md matched the city
    tabs of keywords/Web-Design-Wave3-Cities-Keywords.xlsx, and the three "original file" numbers (website design
    company new york 3,600 SD 12; website design company tampa 2,400 SD 35; web design company tucson 590 SD 7) matched
    the ALL tab of keywords/Web-Design-Keywords.xlsx. New scripts/keyword_plan_wave3.py classifies every 10+ row of the
    Wave 3 file (target, supporting, FAQ question, or unused with a reason) and fails on anything unclassified; it runs
    from scripts/keyword_plan.py after Wave 2.
49. **Original-file phrases for the 8 cities** (for example "web design company new york" 1,900, "website design
    companies orange county" 1,900, "web design company richmond va" 720) moved from "Wave 2 candidate" to supporting
    keywords on the new pages, so the 8 cities no longer appear in the "Wave 2 candidates" table. "web design long
    island" (1,300) and "web design rochester ny" (50) are different places and stay candidates. The older Oct 12 national
    file also had New York, Tampa, Tucson, Richmond and Louisville tabs; the newer Wave 3 pull supersedes them, and the
    Wave 2 "remaining national candidates" table now leaves those cities out.
50. **Edge rows.** "web design nc" (170) is assigned to the Wilmington page (the only North Carolina page). "black web design
    louisville" (10) is supporting on the Louisville page, which links /black-owned-web-design/ (INTAKE section 7; no
    certification claimed). "ecommerce web design new york" is unused (online store builds are
    not in the INTAKE.md packages); the Louisville page answers "ecommerce web design louisville" honestly as an FAQ.
    Huntsville answers "who is hosting my website" and "cheapest web design and hosting" as FAQs (hosting is part of the
    offer); the other hosting rows ("web hosting low cost") and generic rows ("biggest web design companies", "web design
    definition") are unused.
    "orange county ny" and "williamsburg va" are other places.
51. **One angle per city** (docs/writers/BRIEF-WAVE3.md): New York five boroughs plus website accessibility lawsuits;
    Orange County named cities and HOA-governed planned communities; Tampa storm season and a region split by the bay;
    Huntsville small firms selling to prime contractors and the government; Tucson food businesses (City of Gastronomy)
    and budget-minded owners; Richmond makers, breweries and historic districts; Louisville an event-calendar town;
    Wilmington NC a coastal city that runs on seasons, plus the film industry.
52. **Writers and checkers.** Four writer sub-agents (two cities each) wrote the pages; separate fact-check sub-agents
    that wrote none of them checked every claim (docs/fact-check.md, Wave 3).
53. **Images.** Same as Wave 2: no new in-body images; each page reuses generic repo photos with alt text describing what
    is really in them; one planned hero per city (images/heroes/<slug>-hero.jpg, 1920x1080) listed in docs/image-list.md,
    shown as a reused generic hero (`fallback`) with its own accurate alt until it arrives.
54. **Copy counts.** The service areas page and the city directory now say twenty-one other U.S. cities and regions
    (Orange County is a county, hence "and regions").

## Wave 4: 81 more city pages (Oct 17 2026, CITY-PAGES-WAVE4.md)

55. **Branch and resume point.** All Wave 4 work is on `cities-wave4` (started from cities-wave3), committed and pushed
    after each part. Nothing merged or pushed to main. The Wave 2 and 3 pages were not rewritten; they are in the
    similarity check. Progress: see the "Wave 4 status" line at the end of this file; a new session resumes at the
    first part not marked done there.
56. **81 pages, not 80.** CLAUDE.md's 10+ rule says any Texas town with a web design keyword at 10+ searches a month gets
    a page. The Texas file has "web design cypress tx" (170/mo, SD 9, in the Temple TX tab), so Cypress, TX was added to
    Part A. Lufkin ("lufkin website", 20) stays covered by the East Texas page as CITY-PAGES-WAVE4.md says; College Station
    and Wichita Falls have no Texas web design rows and get no page.
57. **Regions replace "Other U.S. cities".** site.json now groups every city page by region: East Texas, Houston and
    Southeast Texas, Dallas-Fort Worth, Austin and the Hill Country, San Antonio and South Texas (new), Central and West
    Texas, Georgia, Florida, The South, The Carolinas, Virginia and the Northeast, The West, The Midwest. The 21 Wave 2/3
    pages moved from `other-us` into their region. Their `m.area_pills(group='other-us', exclude=slug)` calls were left
    untouched: the macro now reads `other-us` plus an excluded slug as "that city's region".
58. **Cities menu and footer.** With 132 city pages, the Cities menu and the footer city bar list the region names
    (linking to anchors on the /web-design/ directory) plus "All cities" and "Service areas", instead of every city. The
    directory lists every page under its region heading; the service areas page shows region pills.
59. **Pages not written yet stay hidden.** build.py drops any site.json city whose page does not exist from menus, pills,
    the directory and structured data, so each part builds and checks clean on its own.
60. **Structured data fix.** The organization's areaServed listed every city as Texas unless it was in Georgia (wrong for
    the 21 national pages). build.py now maps each state abbreviation to its full name.
61. **Heroes.** 24 new Artistly heroes, kept for the largest markets and for looks the repo cannot cover (Gulf Coast,
    Permian Basin, Rio Grande Valley, desert, mountains, Pacific Northwest): San Antonio, Fort Worth, Corpus Christi,
    Midland, McAllen, Charlotte, Raleigh, Charleston, Jacksonville, Fort Lauderdale, New Orleans, Denver, Seattle, Portland,
    Salt Lake City, San Francisco, San Jose, Scottsdale, Albuquerque, Philadelphia, Columbus, Grand Rapids, Oklahoma City,
    Minneapolis. Each shows a reused generic hero (`fallback`) until it arrives. Thirteen cities use the real Wikimedia
    Commons photo of that city already in images/cities/ (Lubbock, Knoxville, Chattanooga, Mobile, St. Petersburg,
    Spokane, Reno, Boise, Fort Collins, Durham, Greenville SC, Columbia SC, Baton Rouge) with a credit line, as the Tyler
    page does; Savannah's portrait photo is used in-body. The other 44 reuse a generic hero already in the repo (shop
    counters, offices, trucks; nothing that names a place), shared only between cities far apart.
62. **In-body photos.** No new in-body images. docs/writers/wave4_brief_gen.py assigns three photos per page from the
    reusable pool (demo-images without printed words, generic images/body and images/contractors photos), spread so each
    photo is used three or four times across the site, never twice on a page and never twice within one writer batch.
63. **Angles.** docs/writers/BRIEF-WAVE4.md (generated by docs/writers/wave4_brief_gen.py) gives every city its own
    angle, chosen so neighbors and look-alike cities do not overlap: for example Midland boom-and-bust versus Odessa
    field crews and hiring pages, Knoxville the Smokies gateway versus Chattanooga Gig City, New Orleans food and music
    versus Mobile shipyards and Airbus, Durham tobacco warehouses and startups versus Tulsa Greenwood and Tulsa Remote.
64. **Writers and checkers.** Writer sub-agents work three cities each (neighbors together so one writer keeps them
    apart); separate fact-check sub-agents that wrote none of the pages check every claim per part.

Wave 4 status: DONE. All 81 pages written, fact-checked (docs/fact-check.md, Wave 4), built and checked (docs/qa.md, Wave 4), committed and pushed to cities-wave4. Not merged to main.

65. **Search budget.** Web searches are capped at 200 per orchestrator turn, shared by every running agent. The first Part B round ran 14 agents at once and ran dry, so later rounds run about five agents at a time with a per-agent cap (12 searches per city), and pages left unwritten or written without research were redone in follow-up rounds rather than filled from memory.
66. **Detroit hero.** The assigned shared hero (las-vegas-nv-hero.jpg) shows desert mountains through the bay door, which plainly is not Michigan, so Detroit reuses the why-small-businesses-need-a-website-hero.jpg bakery scene instead (the kansas-city auto shop hero was tried first, but it shows a readable car maker emblem).
