# Wave 4: 80 more city pages for dominionwebdesignpro.com (Oct 16 2026)

RUN STRAIGHT THROUGH. DO NOT STOP. Maurice is not watching and cannot approve anything. Make
reasonable decisions, write them in docs/decisions.md, and keep going until every check below
passes. Read CLAUDE.md first: every hard rule and design rule in it applies to these pages.
This branch (cities-wave4) starts from cities-wave3, so Waves 2 and 3 (21 national pages) are
already here: do not rewrite them, but include them in the similarity check.

## Work in three parts, and save after each one
This is a big run. Do Part A, then Part B, then Part C. After EACH part: build, run check.py and
the similarity script on everything so far, commit, and push cities-wave4. If the session ends
early, the next session picks up at the first part that is not finished (say which in
docs/decisions.md). Use parallel writer sub-agents within each part, and give each writer the
pages already written so it can avoid repeating them.

## The pages
Add 80 hand-written city pages in src/pages/web-design/, built exactly like the existing city
pages (front matter shape of st-louis-mo.html, tucson-az.html and wilmington-nc.html, the same
templates, macros and image handling). Keyword data, Ubersuggest US, pulled Oct 16 2026:
- keywords/Web-Design-Texas-Cities-Keywords.xlsx (Part A)
- keywords/Web-Design-South-East-Cities-Keywords.xlsx (Part B)
- keywords/Web-Design-West-Midwest-Cities-Keywords.xlsx (Part C)
- keywords/Web-Design-National-Cities-Keywords.xlsx (Philadelphia, Columbus, Oklahoma City,
  Tulsa, Albuquerque, Baton Rouge, Little Rock, Memphis, Chattanooga)
Verify every number yourself from the files; the table below was picked by script (best volume
for its difficulty) and you may choose a better main target if the data supports it. Each page
targets ONE main term (title, H1, opening paragraph) and works its other 10+ volume city terms in
as supporting keywords and FAQ questions (use the Question rows).

Texas pages: Maurice is in Big Sandy, East Texas, so the Texas pages may say he is a Texan
building for Texas businesses, but still no office or team in that town. Small towns with about
10 to 40 searches a month (Nacogdoches, Texarkana, Temple, Laredo, Round Rock, Killeen and the
like) get shorter honest pages built on what is really true there; never pad them.
Lufkin, College Station and Wichita Falls had no real web design rows: no page (the East Texas
page covers Lufkin). Wichita Falls rows about Wichita, Kansas are not Texas.

### Part A: Texas (22 pages)

| File | Main target (volume, SD) | Supporting terms |
|---|---|---|
| san-antonio-tx.html | web design san antonio (1,900, SD 18) | web designer san antonio tx 720; san antonio website designers 260; web design san antonio texas 110; san antonio web design company 110; web design san antonio tx 90 |
| fort-worth-tx.html | web design fort worth texas (1,900, SD 34) | web design fort worth tx 1,600; fort worth website design 1,600; web design fort worth 1,300; web development fort worth 260; web design company fort worth 40 |
| arlington-tx.html | arlington website design (90, SD 18) | web design arlington tx 70; web design arlington 70; web design company arlington tx 20 |
| corpus-christi-tx.html | website design corpus christi (170, SD 19) | web design corpus christi 170; web design corpus christi tx 170 |
| lubbock-tx.html | web design lubbock tx (320, SD 43) | web design lubbock 320 |
| amarillo-tx.html | web design amarillo (140, SD 18) | web design amarillo tx 140 |
| beaumont-tx.html | web design beaumont tx (30, SD 15) | none above 10 besides the target |
| midland-tx.html | web design midland tx (70, SD 26) | none above 10 besides the target |
| odessa-tx.html | website design odessa tx (90, SD 5) | web design odessa tx 40 |
| killeen-tx.html | web design killeen tx (40, SD 20) | web design killeen 20 |
| mcallen-tx.html | web design mcallen texas (90, SD 11) | web design mcallen 90; web developer mcallen tx 10 |
| laredo-tx.html | web design laredo tx (30, SD 10) | web design laredo 30 |
| brownsville-tx.html | web design brownsville (40, SD 9) | web design brownsville tx 40 |
| sugar-land-tx.html | web design sugar land (40, SD 14) | web design sugar land tx 30; sugar land web design 30 |
| katy-tx.html | katy web design (40, SD 14) | katy web 50; web design katy tx 30 |
| the-woodlands-tx.html | web design the woodlands (40, SD 10) | web design the woodlands tx 20 |
| round-rock-tx.html | web design round rock (30, SD 11) | web design round rock tx 30 |
| abilene-tx.html | abilene website design (90, SD 11) | web design abilene tx 90 |
| san-angelo-tx.html | web design san angelo (20, SD 13) | none above 10 besides the target |
| temple-tx.html | web design temple tx (10, SD 5) | temple web design 40 |
| nacogdoches-tx.html | web design nacogdoches (10, SD 18) | none above 10 besides the target |
| texarkana-tx.html | website design texarkana (10, SD 13) | web design texarkana 10 |

### Part B: South and East (29 pages)

| File | Main target (volume, SD) | Supporting terms |
|---|---|---|
| charlotte-nc.html | web design in charlotte nc (1,900, SD 65) | web design in charlotte 1,600; web design charlotte 1,000; website design charlotte 1,000; web design charlotte nc 1,000; charlotte web design company 390 |
| raleigh-nc.html | web design raleigh north carolina (590, SD 34) | raleigh web design 720; web design raleigh 590; raleigh web design company 50; custom web design raleigh nc 10; shopify web design raleigh 10 |
| durham-nc.html | web design durham nc (210, SD 23) | website design durham nc 210; durham website design 50; webb design durham nc 10; webb design durham 10 |
| greensboro-nc.html | web design greensboro (390, SD 28) | web design greensboro nc 30 |
| charleston-sc.html | charleston website design (1,300, SD 40) | web design charleston sc 1,000; charleston sc web design 880; charleston web designer 320 |
| columbia-sc.html | web design columbia (720, SD 55) | web design columbia sc 590; website design columbia sc 480; columbia web design 50; web design columbia mo 40 |
| greenville-sc.html | web design greenville sc (480, SD 49) | greenville web design 390; site design greenville sc 90; greenville sc web design company 40; web design greenville nc 10; web designer greenville nc 10 |
| savannah-ga.html | savannah website design (390, SD 31) | web design savannah 320; web design savannah georgia 320 |
| augusta-ga.html | web design augusta ga (140, SD 27) | web design augusta 140 |
| jacksonville-fl.html | jacksonville website design (1,600, SD 57) | web design jacksonville fl 1,000; jacksonville web design company 40; web design jacksonville nc 20 |
| fort-lauderdale-fl.html | web design fort lauderdale fl (1,300, SD 6) | fort lauderdale website design 1,000; web design fort lauderdale 880; website design fort lauderdale 880; fort lauderdale web design company 140; web design company fort lauderdale 110 |
| west-palm-beach-fl.html | web design west palm beach (590, SD 12) | web design west palm beach fl 590; west palm beach website design 590; palm beach web design 70; west palm beach web development 40; west palm beach web design company 30 |
| st-petersburg-fl.html | web design st petersburg (260, SD 14) | web design st petersburg fl 210 |
| sarasota-fl.html | web design sarasota florida (720, SD 17) | web design sarasota 720; sarasota website development 90; sarasota website design companies 30 |
| fort-myers-fl.html | web design fort myers (390, SD 8) | web design fort myers florida 590; web design fort myers fl 390; fort myers website design 390; responsive web design fort myers 30 |
| tallahassee-fl.html | web design tallahassee fl (140, SD 32) | web design tallahassee 140; tallahassee web design 90; tallahassee website design 70 |
| pensacola-fl.html | web design pensacola florida (170, SD 17) | web design pensacola 170; pensacola website design 170 |
| birmingham-al.html | web design birmingham al (70, SD 37) | website design birmingham al 70 |
| mobile-al.html | website design mobile al (50, SD 29) | web design mobile al 50; how much of web traffic is mobile 40 |
| montgomery-al.html | web design montgomery al (90, SD 32) | none above 10 besides the target |
| jackson-ms.html | web design jackson ms (30, SD 26) | web design jackson mi 20; website design jackson ms 10 |
| new-orleans-la.html | new orleans website design (1,900, SD 48) | web design new orleans la 1,900; web design new orleans 1,300 |
| shreveport-la.html | web design shreveport (70, SD 14) | web design shreveport la 70 |
| baton-rouge-la.html | website design baton rouge (590, SD 27) | none above 10 besides the target |
| knoxville-tn.html | knoxville tn web design (480, SD 39) | web design knoxville 390; web design knoxville tn 390; knoxville website design 390; web development knoxville 30; knoxville web design company 30 |
| chattanooga-tn.html | chattanooga website design (140, SD 32) | chattanooga web design 110; chattanooga web developers 10 |
| memphis-tn.html | memphis website design (390, SD 26) | neo memphis web design 10 |
| lexington-ky.html | website design lexington (480, SD 19) | web design lexington ky 480; web design lexington sc 70; lexington website design 70 |
| little-rock-ar.html | website design little rock ar (880, SD 22) | website design little rock 590 |

### Part C: West and Midwest (29 pages)

| File | Main target (volume, SD) | Supporting terms |
|---|---|---|
| denver-co.html | web design denver co (2,900, SD 9) | web design denver 2,900; web design company in denver 1,600; web development company denver 880; wordpress web design denver 70; affordable web design denver 50 |
| colorado-springs-co.html | colorado springs web design company (170, SD 9) | web design in colorado springs 590; website design colorado springs 320; web design colorado springs 210 |
| fort-collins-co.html | web design fort collins co (320, SD 22) | fort collins website design 260; web design fort collins 210; web developer fort collins 10; fort collins web development 10 |
| seattle-wa.html | web design seattle (2,900, SD 77) | web design seattle washington 1,900; web design seattle wa 1,000; website design seattle 880; seattle web design 880; web development agency seattle 590 |
| spokane-wa.html | web design spokane wa (880, SD 29) | web design spokane 880; spokane website design 880; spokane web design 720; spokane valley web design 50; best web design spokane 30 |
| portland-or.html | web design portland oregon (1,600, SD 32) | portland oregon website design 1,900; web design portland 1,600; web design portland or 1,000; web design portland maine 70; portland web design companies 70 |
| boise-id.html | web design boise idaho (1,000, SD 10) | web design boise id 880; web design boise 720; boise web design 590; web development boise 50; thrive web design boise 10 |
| salt-lake-city-ut.html | website design salt lake city (590, SD 24) | web design salt lake city 590; web design salt lake city utah 590; salt lake city web design company 480; web development salt lake city 50 |
| reno-nv.html | web design reno nv (480, SD 41) | wordpress web design reno 10 |
| san-francisco-ca.html | web design san francisco bay area (590, SD 8) | web design san francisco 880; website design san francisco 880; website design in san francisco 590; web design san francisco ca 390; san francisco website design 390 |
| san-jose-ca.html | web design san jose (590, SD 12) | san jose web design 720; website design in san jose 590; web design san jose ca 590; website designer san jose ca 390; website design san jose 110 |
| fresno-ca.html | fresno website design (880, SD 42) | web design fresno 720; web design fresno ca 720; fresno web designer 140; loops marketing web design fresno & seo 10; fresno web design services 10 |
| bakersfield-ca.html | bakersfield website design (480, SD 21) | web design bakersfield 480; web design bakersfield ca 40; web design company bakersfield 10; web design services in bakersfield 10; website design in bakersfield 10 |
| long-beach-ca.html | web design long beach ca (320, SD 33) | long beach website design 320; web design long beach 140; website design long beach 140 |
| scottsdale-az.html | web design scottsdale az (880, SD 10) | scottsdale website design 880; scottsdale web design 720; web design scottsdale 320 |
| mesa-az.html | website design mesa (170, SD 13) | mesa websites 110; web design mesa az 30; web designer mesa 10 |
| albuquerque-nm.html | web design in albuquerque (210, SD 30) | web design albuquerque nm 210; web design albuquerque 170; website development albuquerque 30; albuquerque web design company 30; affordable web design albuquerque 20 |
| oklahoma-city-ok.html | web design in oklahoma city (880, SD 26) | website design oklahoma city 390; website design oklahoma 110; oklahoma website design 110; web design in oklahoma 90 |
| tulsa-ok.html | web designers in tulsa (110, SD 25) | web development tulsa 90 |
| omaha-ne.html | web design omaha ne (1,000, SD 57) | web design omaha 1,000; website design omaha 140 |
| des-moines-ia.html | web design des moines (590, SD 46) | web design des moines iowa 590; des moines website design 480; web development des moines 50; website designers in des moines 50; web design des moines ia 50 |
| minneapolis-mn.html | web design minneapolis (590, SD 19) | web design minneapolis mn 880; web design company minneapolis 260; minneapolis web designer 70; responsive web design minneapolis 30; ecommerce web design minneapolis 10 |
| madison-wi.html | madison website design (480, SD 15) | web design madison wi 390; web madison 260; website designer madison wi 50 |
| grand-rapids-mi.html | web design grand rapids (1,600, SD 23) | website design grand rapids 1,600; web design grand rapids michigan 1,600; grand rapids web design 1,300; grand rapids website development 90; web development grand rapids 30 |
| detroit-mi.html | web design detroit (590, SD 21) | web design detroit michigan 590; detroit web design company 50; affordable web design detroit 20; detroit web design agencies 10 |
| cincinnati-oh.html | web design cincinnati (880, SD 20) | web design cincinnati ohio 590; cincinnati web design agency 30; affordable web design cincinnati 10 |
| columbus-oh.html | website design columbus (590, SD 22) | columbus ohio web design 880; columbus web design company 260; columbus web designers 140; columbus web design agency 10 |
| pittsburgh-pa.html | web design pittsburgh pa (480, SD 12) | web design pittsburgh 720 |
| philadelphia-pa.html | philadelphia web designer (720, SD 25) | web designers in philadelphia 590 |


Ignore rows that are definitions, design tips, hosting, jobs, salaries, courses, safety or
weather questions, schedules, another agency's brand, or a different place with the same name
(Jackson County, Columbia MO, Wichita KS, Lexington outside Kentucky, Columbus GA). List every
unused 10+ row from the three new files in docs/keyword-plan.md under "Wave 4" with a one-line
reason, remove these cities from the "Wave 2 candidates" table, and add the 80 pages to SERVICES.md.
The Cities menu will get long: group it by region (Texas, South, East, West, Midwest) or link a
"See all cities" directory page instead of listing 150 links, whichever the existing menu
supports cleanly.

## Every page must be written for THAT city
Research each city on the web before writing, and cite every fact in the page's sources:
its small business makeup (what kinds of owner-run businesses are common there), real
neighborhoods, corridors or suburbs residents would recognize, its chamber of commerce or
small business resources (SBDC, city small business office), and why local search matters there.
Give each page a DIFFERENT angle and outline, the way atlanta-ga.html (sole proprietors) and
lawrenceville-ga.html (a multilingual customer base, the courthouse economy) differ. Never reuse a
paragraph or section shape from another city page with the name swapped. The sections that
earlier city pages repeat ("questions worth asking", the remote / East Texas disclosure,
"getting started") must be written fresh on each page or kept to one short line linking to a
shared page; they must not push any pair over the similarity limit.

Be honest on every page: Dominion Web Design Pro is Maurice Johnson in Big Sandy, East Texas,
building remotely. No office in the city, no local team, no clients there unless INTAKE.md lists
them. Prices and package contents exactly as INTAKE.md. The phone is answered by an AI
receptionist that can transfer to Maurice. Turnaround wording must match INTAKE.md.

## Wiring
- Add all 80 to src/data/site.json areas (or wherever the existing city pages are listed), to the
  service areas page (/service-areas/, a new "Other U.S. cities" group or the right regional
  groups), to the Cities menu if the menu lists cities, and to sitemap.xml.
- Images: reuse generic photos already in the repo (images/body, images/contractors and similar,
  never a photo showing a different named city). Maurice's rule is reuse first: one photo may fill
  several spots across the site, never twice on one page. Heroes may be shared between cities
  that are far apart (a generic shop counter, kitchen, truck or office with nothing that names a
  place). Aim for 24 or fewer NEW Artistly heroes in total, kept for the biggest cities and for
  looks the existing photos cannot cover (desert, coast, mountains, Gulf Coast). For each new one, add it to
  docs/image-list.md (File name, Size 1920x1080, Artistly prompt per CLAUDE.md, bright, no text,
  no logos, no recognizable faces, no real landmarks presented as fact) and show a reused photo in
  its place until it arrives. If an image does not show the real place, the alt text must not
  claim it does.

## Before you finish (all must pass)
- python3 build.py, then python3 scripts/check.py: 0 errors. python3 scripts/check_old_urls.py: clean.
- scripts/similarity.py (Jaccard, 5-word shingles): every pair of city pages, old and new, at or
  under 15%. Rewrite any pair above. Record the numbers in docs/qa.md under "Wave 4".
- Grep the built pages for the banned phrases and checks listed in CLAUDE.md. Fix every hit.
- No horizontal overflow at 1440, 1024, 768 and 390 px.
- Independent fact-check: separate sub-agents that did not write the pages check every factual
  claim and source on the 80 pages (split the pages among several checkers); fix what they find; record it in docs/fact-check.md.

## Git
Work on the branch cities-wave4. Commit as you go and push cities-wave4 after every few pages so
nothing is lost. Do NOT merge to main or push to main: main is the live site. Maurice approves
going live.

## Final report (Maurice reads on his phone, 5 lines max)
Pages built, checks passed, duplication range, fact-check result, how many hero images need
Artistly, and the one thing Maurice must do next.
