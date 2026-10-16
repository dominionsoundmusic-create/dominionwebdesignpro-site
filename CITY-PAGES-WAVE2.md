# Wave 2: 13 national city pages for dominionwebdesignpro.com (Oct 16 2026)

RUN STRAIGHT THROUGH. DO NOT STOP. Maurice is not watching and cannot approve anything. Make
reasonable decisions, write them in docs/decisions.md, and keep going until every check below
passes. Read CLAUDE.md first: every hard rule and design rule in it applies to these pages.

## The pages
Add 13 hand-written city pages in src/pages/web-design/, built exactly like the existing city pages
(front matter shape of src/pages/web-design/dallas-tx.html and atlanta-ga.html, the same templates,
macros and image handling). Keyword data: keywords/Web-Design-National-Cities-Keywords.xlsx (ALL tab
plus one tab per city) and keywords/Web-Design-5-Cities-Recheck.xlsx (Cleveland). Verify every number
yourself from the files. Each page targets ONE main term (title, H1, opening paragraph) and works its
other 10+ volume city terms in as supporting keywords and FAQ questions.

| File | Main target (volume, SEO difficulty) | Supporting terms to use |
|---|---|---|
| st-louis-mo.html | website design st louis (2,400, SD 8) | st louis website design 1,300; st louis web design company 1,600 |
| phoenix-az.html | web design company in phoenix (2,900, SD 9) | web design in phoenix 1,900 (SD 7) |
| san-diego-ca.html | web design in san diego (2,900, SD 9) | san diego website design 2,400; website design san diego 1,300; san diego web design company 320 |
| las-vegas-nv.html | website design las vegas nevada (2,900, SD 9) | las vegas website design 880 (SD 10); web design in las vegas 3,600; web design vegas 1,900 |
| los-angeles-ca.html | los angeles web design companies (1,900, SD 9) | web design in la 1,000 (SD 13); web design in los angeles 4,400; website design in los angeles 9,900 |
| miami-fl.html | web design in miami (1,900, SD 10) | web design agency in miami 480 (SD 13); miami web design companies 210 |
| nashville-tn.html | web design in nashville (880, SD 10) | website designer in nashville 140 (SD 9); nashville website design 1,000 |
| chicago-il.html | web design agency in chicago (880, SD 11) | web design in chicago 2,900; web design company in chicago 880 |
| orlando-fl.html | web design in orlando (1,600, SD 13) | other 10+ Orlando web design terms in the file (never another agency's brand name) |
| indianapolis-in.html | indianapolis website design (1,900, SD 16) | indianapolis web design company 210 |
| sacramento-ca.html | website design sacramento (2,400, SD 17) | sacramento web design 1,600; web design in sacramento ca 2,400 |
| kansas-city-mo.html | kansas city website design (390, SD 6) | kansas city web design 320; web design kansas city mo 590; website design in kansas city 720 |
| cleveland-oh.html | website design cleveland ohio (880, SD 8) | cleveland website design 480; website design cleveland 480; cleveland web development 720 |

Ignore rows that are another agency's brand, a citation-style question ("how to cite a website
chicago style"), jobs, salaries or courses. List every unused 10+ row for these 13 cities in
docs/keyword-plan.md under "Wave 2" with a one-line reason, and add the 13 pages to SERVICES.md.

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
- Add all 13 to src/data/site.json areas (or wherever the existing city pages are listed), to the
  service areas page (/service-areas/, a new "Other U.S. cities" group or the right regional
  groups), to the Cities menu if the menu lists cities, and to sitemap.xml.
- Images: reuse generic photos already in the repo (images/body, images/contractors and similar,
  never a photo showing a different named city). One hero per city may be new: add it to
  docs/image-list.md (File name, Size 1920x1080, Artistly prompt per CLAUDE.md, bright, no text,
  no logos, no recognizable faces, no real landmarks presented as fact) and show a reused photo in
  its place until it arrives. If an image does not show the real place, the alt text must not
  claim it does.

## Before you finish (all must pass)
- python3 build.py, then python3 scripts/check.py: 0 errors. python3 scripts/check_old_urls.py: clean.
- scripts/similarity.py (Jaccard, 5-word shingles): every pair of city pages, old and new, at or
  under 15%. Rewrite any pair above. Record the numbers in docs/qa.md under "Wave 2".
- Grep the built pages for the banned phrases and checks listed in CLAUDE.md. Fix every hit.
- No horizontal overflow at 1440, 1024, 768 and 390 px.
- Independent fact-check: separate sub-agents that did not write the pages check every factual
  claim and source on the 13 pages; fix what they find; record it in docs/fact-check.md.

## Git
Work on the branch cities-wave2. Commit as you go and push cities-wave2 after every few pages so
nothing is lost. Do NOT merge to main or push to main: main is the live site. Maurice approves
going live.

## Final report (Maurice reads on his phone, 5 lines max)
Pages built, checks passed, duplication range, fact-check result, how many hero images need
Artistly, and the one thing Maurice must do next.
