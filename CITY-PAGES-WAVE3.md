# Wave 3: 8 more national city pages for dominionwebdesignpro.com (Oct 16 2026)

RUN STRAIGHT THROUGH. DO NOT STOP. Maurice is not watching and cannot approve anything. Make
reasonable decisions, write them in docs/decisions.md, and keep going until every check below
passes. Read CLAUDE.md first: every hard rule and design rule in it applies to these pages.
This branch (cities-wave3) starts from cities-wave2, so the 13 Wave 2 pages are already here:
do not rewrite them, but include them in the similarity check.

## The pages
Add 8 hand-written city pages in src/pages/web-design/, built exactly like the existing city pages
(front matter shape of src/pages/web-design/st-louis-mo.html and miami-fl.html, the same templates,
macros and image handling). Keyword data: keywords/Web-Design-Wave3-Cities-Keywords.xlsx (ALL tab
plus one tab per city, Ubersuggest US, pulled Oct 16 2026) and keywords/Web-Design-Keywords.xlsx
(the original file, where three of the main targets below come from). Verify every number
yourself from the files. Each page targets ONE main term (title, H1, opening paragraph) and works
its other 10+ volume city terms in as supporting keywords and FAQ questions (use the Question rows).

| File | Main target (volume, SEO difficulty) | Supporting terms to use |
|---|---|---|
| new-york-ny.html | website design company new york (3,600, SD 12, original file) | new york web design company 2,400; website design new york 1,900; web design new york city 1,900; web design new york 1,600; web design company in new york 260 |
| orange-county-ca.html | orange county website design (1,900, SD 16) | orange county web design company 1,600 (SD 16); web design orange county california 1,600; web design orange county ca 1,300; orange county website designers 480 (SD 9) |
| tampa-fl.html | web design tampa florida (1,600, SD 28) | website design company tampa 2,400 (original file); web design company in tampa 2,400; web design in tampa 2,900; tampa web design company 210; tampa web design agency 170 |
| huntsville-al.html | web design huntsville al (880, SD 29) | huntsville website design 210 |
| tucson-az.html | web design company tucson (590, SD 7, original file) | web design tucson az 590; web design tucson arizona 720; tucson website design 720; affordable web design tucson 10 |
| richmond-va.html | richmond va web design (480, SD 14) | web design richmond va 590 (SD 26); web design in richmond 590; richmond website design 720 |
| louisville-ky.html | web design louisville (480, SD 20) | louisville web design 590 (SD 26); louisville website design 880; web design louisville ky 480 |
| wilmington-nc.html | web design wilmington nc (260, SD 30) | website design wilmington nc 260; wilmington website design 70 (Wilmington, North Carolina only, never Delaware) |

Ignore rows that are definitions, design tips, hosting, jobs, salaries, courses, another
agency's brand (e.g. "creative813"), other places ("orange county ny", "williamsburg va") or
off-topic ("where is the fashion district in new york", "nyc design stores"). List every unused
10+ row from the Wave 3 file in docs/keyword-plan.md under "Wave 3" with a one-line reason, move
these 8 cities out of the "Wave 2 candidates" table, and add the 8 pages to SERVICES.md.

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
- Add all 8 to src/data/site.json areas (or wherever the existing city pages are listed), to the
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
  under 15%. Rewrite any pair above. Record the numbers in docs/qa.md under "Wave 3".
- Grep the built pages for the banned phrases and checks listed in CLAUDE.md. Fix every hit.
- No horizontal overflow at 1440, 1024, 768 and 390 px.
- Independent fact-check: separate sub-agents that did not write the pages check every factual
  claim and source on the 8 pages; fix what they find; record it in docs/fact-check.md.

## Git
Work on the branch cities-wave3. Commit as you go and push cities-wave3 after every few pages so
nothing is lost. Do NOT merge to main or push to main: main is the live site. Maurice approves
going live.

## Final report (Maurice reads on his phone, 5 lines max)
Pages built, checks passed, duplication range, fact-check result, how many hero images need
Artistly, and the one thing Maurice must do next.
