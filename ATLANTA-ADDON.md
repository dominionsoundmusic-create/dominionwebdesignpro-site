# ATLANTA ADD-ON: INSTRUCTIONS FOR CLAUDE CODE (Oct 12 2026)

The Playbook 2.0 rebuild on this `build` branch is finished. This is a follow-up run that adds
Atlanta-area pages. Read CLAUDE.md, INTAKE.md (note section 7, OWNERSHIP) and WRITING-GUIDE.md /
docs/decisions.md first: every rule in CLAUDE.md applies here too (hand-written, researched,
sourced, no invented claims, FAQs + FAQPage JSON-LD, hero + 2 in-body images, full-width layout,
no em dashes, similarity under 15%, the `dwdp:handwritten 2026-10-12` marker, independent
fact-check by separate sub-agents). Use the existing build system and templates; do not redesign.

RUN STRAIGHT THROUGH. DO NOT STOP. Maurice is not watching. Record decisions in docs/decisions.md.

## Keyword source
keywords/Atlanta-Web-Design-Keywords.xlsx (Ubersuggest, United States, Oct 12 2026; 22 seed tabs
plus ALL, 385 keywords). Apply Maurice's 10+ rule: every keyword with 10 or more searches a month
is assigned to a page or listed as unused with a reason in docs/keyword-plan.md (new section
"Atlanta add-on"). "clayton county website" and "henry county website" are people looking for the
county government's own site: list as unused. Cities that showed 0 searches (South Fulton, College
Park, East Point, Union City, Fairburn, Stonecrest, Lithonia, Stockbridge, Riverdale, Jonesboro,
Morrow, Forest Park) get NO page in this run; list them under "Atlanta wave 2 (0 measured volume)".

## Pages to build or rebuild
1. NEW /black-owned-web-design/ (national page). Targets: "black owned web developers" 880/mo SD 10,
   "black owned website design companies" 50 SD 9, "black owned web design company" 50 SD 14,
   "black owned web designers near me" 30 SD 15, "black owned web designers" 20 SD 24,
   "black owned web design agency" 10 SD 21, "black owned web design" 10 SD 28,
   "black owned web design atlanta" (seed). Honest and specific: Maurice Johnson owns and builds,
   East Texas based, works nationwide, the free demo, the hand-written standard, real prices.
   Useful sourced content for readers: how to verify a business is Black-owned (for example
   directories and certification programs such as NMSDC MBE certification, explained as what it
   is, NOT claimed for Dominion), why supporting Black-owned businesses matters, cited from
   reputable sources (Census Annual Business Survey data on Black-owned employer firms, SBA,
   Federal Reserve small business credit survey, etc.; verify every number). No stereotypes, no
   claims about other agencies.
2. STRENGTHEN /web-design/atlanta-ga (keep the URL and its researched facts). Add targets
   "web developers in atlanta" 1,300 SD 11, "web design in atlanta ga" 1,300 SD 36,
   "atlanta web designer" 590 SD 20, "atlanta web design" 880 SD 36, "web design company atlanta ga"
   1,300 SD 46 as supporting, "atlanta wordpress web design" 50 SD 19, "best web designers in
   atlanta" 10 SD 5, "black owned web design atlanta". Mention it is a Black-owned business and
   link to /black-owned-web-design/. Never imply an Atlanta office.
3. NEW city pages (10+ rule), each researched for THAT city (its downtown or business corridors,
   chamber of commerce, Main Street or small business resources, county, why local search matters
   there): /web-design/decatur-ga ("web design decatur ga" 20 SD 5),
   /web-design/mcdonough-ga ("web design mcdonough ga" 10 SD 5, "mcdonough website" 10 SD 18 if it
   fits), /web-design/conyers-ga (10 SD 5), /web-design/douglasville-ga (10 SD 5).
   Built remotely from East Texas; never imply an office there.
4. Link the new pages from the service areas overview, the Georgia section of the city index, the
   Atlanta and Lawrenceville pages, and the sitemap. Add /black-owned-web-design/ to the About page
   and footer.

## Images
Reuse photos already in the repo first. Add every new image still needed to docs/image-list.md
(File name, Size, Artistly prompt), heroes first; show brand-color blocks until they arrive.

## Finish
All checks in CLAUDE.md must pass (build, check.py, old URLs, banned-phrase grep, overflow at
1440/1024/768/390, independent fact-check of the 6 pages recorded in docs/fact-check.md).
Commit and push to origin `build` only. Do NOT merge to main or deploy.
Final report, 5 lines max: pages added/rebuilt, checks passed, similarity range, fact-check
result, images needed.
