# Dominion Web Design Pro (dominionwebdesignpro.com): PLAYBOOK 2.0 REBUILD. INSTRUCTIONS FOR CLAUDE CODE

You are rebuilding Maurice Johnson's own web design website by running Dominic & Dalton's Website
Builder Prompt Playbook 2.0 (PLAYBOOK.md), Prompts 1 to 20, in full. This is his money site: the
place prospects land after his outreach. Quality over speed.

## RUN STRAIGHT THROUGH. DO NOT STOP.
Maurice is not watching this session and cannot approve anything. Do NOT pause at the end of each
playbook phase, do NOT ask "continue?", do NOT wait for input. Make reasonable decisions yourself,
write them down in docs/decisions.md, and keep going until Prompt 20 is finished and every check
below passes. The only reasons to stop early: something would cost money, deploy, merge to main,
or change a repository other than this one.

## Source files (read all of them first)
- INTAKE.md: the facts and the exact pricing. It wins over anything else.
- PLAYBOOK.md: the playbook (Operating Rules, then Prompts 1 to 20). It was written for GHL AI
  Studio; apply its rules and its 20 steps to this static build system.
- keywords/Web-Design-Keywords.xlsx: Ubersuggest, United States, pulled Oct 12 2026. 1,501 unique
  keywords, a tab per seed plus an ALL tab, each row typed Suggestion or Question. Use it to choose
  pages and target keywords. Ignore rows about other countries/cities with no fit, jobs, salaries,
  courses, weather and brand names of other agencies; list them as unused with a reason in
  docs/keyword-plan.md (summarize by group, do not list all 1,501 one by one).
- The CURRENT live site in this repo (main). Read every existing page before writing. The 20
  hand-written city pages in web-design/ and the hand-written pages (about.html,
  small-business-website-cost.html, website-design-for-contractors.html, how-city-pages-work.html)
  hold researched content: keep their facts and good writing, move them into the new templates,
  and improve them for their keyword. Do not throw that research away.

## Copy the build system from Phoenix Pool Cleaning Pro (NOT its words)
Clone dominionsoundmusic-create/phoenix-pool-cleaning-pro, branch `build`. Copy its BUILD SYSTEM:
build.py (Jinja2, writes dist/), scripts/check.py, scripts/similarity.py if present, the old-URL
check script pattern, src/templates/, src/static/css/site.css and JS, the macros (img, faqs,
sources), the site.json structure, netlify.toml and the docs/playbook/ document set as a pattern.
Adapt every value to Dominion Web Design Pro. Never copy page text from any other site.
Keep the speed fix exactly (WebP 480/800/1200/1600/1920 srcset, preloaded hero with fetchpriority
high, self-hosted woff2 font) and the full-width layout.

## THINGS THAT MUST KEEP WORKING (test each one at the end)
- netlify/functions/seo-audit.mjs and the Site Check tool at /site-check/ (it calls that function).
  netlify.toml must keep `publish = "dist"` AND point functions at netlify/functions so the
  function still deploys. Do not edit the function's logic.
- /demo.html, /demo-generator.html (the free demo flow and its backend calls), /compare/, /tools/,
  /intake/ and /intake/thanks/ (Netlify form "client-intake"), /contact/ and /contact/thanks/,
  the homepage contact form, and the demo-images/ folder (the demo generator loads photos from
  https://dominionwebdesignpro.com/demo-images/<folder>/<n>.jpg; those paths must still resolve).
  These tool pages may get the new header and footer ONLY if their scripts, form names, field names
  and endpoints stay byte-for-byte the same. If in doubt, copy the tool page through unchanged.
- Every Netlify form keeps its exact name and fields, rendered in the static HTML (not injected by
  JS), so Netlify still detects it.
- _redirects and _headers: keep every existing rule. Every URL that exists today (find them with
  `git ls-files '*.html'` on main plus the _redirects targets) must still return a page or a 301 to
  the closest page. Write scripts/check_old_urls.py that lists every old URL and proves it resolves
  in dist/ or has a redirect. Pretty URLs: keep both the .html and extensionless forms working
  exactly as they do now (Netlify Pretty URLs is ON; do not break existing indexed URLs).
- GA4 G-3MZXMC1JKS with phone-tap tracking, the social links top and footer, the EN/ES toggle
  (the branded toggle the live site has, in brand colors), on every page.

## Pages to build (decide the final list from the keywords, then follow it)
Write SERVICES.md (every page, URL, target keyword with volume and SEO difficulty) and
docs/keyword-plan.md BEFORE writing pages. Expect at least:
- Core: home, pricing/packages section (on the home page as now, plus a /pricing/ page if the
  keywords "web design packages", "small business website package" justify it), how it works,
  about, contact, FAQ, service areas overview, privacy, terms, 404.
- Services, keeping existing URLs: small business website design (/small-business-website/),
  contractor website design (/contractor-website-design/, plus website-design-for-contractors.html
  folded in or redirected), SEO web design (/seo-web-design/). The other existing hubs
  (professional-, ecommerce-, medical-, real-estate-, restaurant-website-design) are rebuilt only
  if the data or the business supports them; otherwise 301 them to the closest page. Never 404.
- Trade pages where the data shows demand, for example web design for plumbers (720/mo, SD 16),
  roofers, HVAC, electricians, landscapers. Check each in the data and record it.
- Guides for the strongest questions: how much does a website cost for a small business (keep and
  improve /small-business-website-cost.html), how much does a website designer cost, how to find
  and hire a web designer, web design packages explained. Research and cite sources.
- City pages: NEW /web-design/houston-tx (web design in houston 5,400/mo SD 9; web design company
  houston 720 SD 8), /web-design/dallas-tx (web design in dallas tx 5,400 SD 13; website design
  agency dallas 590 SD 7), /web-design/tyler-tx (140 SD 23), and an East Texas page. Rebuild ALL 20
  existing city pages in web-design/ at their same URLs, keeping their researched local facts.
  Austin and Longview already exist; strengthen them for their keywords.
- Every city page is written for THAT city (its business makeup, real neighborhoods and corridors,
  its chamber or small business resources, why local search matters there). Never imply an office
  there. Be honest: built remotely from East Texas.

## Hard rules for every page
1. Never invent reviews, testimonials, clients, portfolio pieces, ratings, awards, certifications,
   years in business, job counts, statistics about the business, guarantees or ranking promises.
2. Prices and package contents only exactly as in INTAKE.md. Buy buttons use the Stripe links in
   INTAKE.md; every card also offers "Or get a free demo first".
3. The phone is answered by an AI receptionist that can transfer to Maurice. Say so honestly.
4. No em dashes or en dashes in visible copy (the one exception is the Jesse Duplantis credit
   line). No eyebrow labels above headings. American spelling.
5. Every page except privacy, terms and 404 has 3 to 6 FAQs written the way people ask (use the
   Question rows), rendered visibly AND as FAQPage JSON-LD.
6. Every page has a full-width hero image plus at least two in-body images, each with filename,
   alt, width, height and loading="lazy" (hero eager). Reuse the photos already in the repo first
   (images/, images/cities/, images/contractors/, demo-images/ where they genuinely fit). Every
   image that does not exist yet goes in docs/image-list.md and shows as a brand-color block until
   it arrives, never a broken image.
7. Facts must be real and current. Research on the web and cite sources on guide pages and
   wherever a fact is stated. If you cannot verify it, leave it out.
8. Each page is written for its own keyword. Measure Jaccard similarity on 5-word shingles between
   every pair of pages of the same type; any pair above 15% gets rewritten. Record numbers in
   docs/qa.md.
9. Banned phrases: "your trusted partner", "one-stop solution", "look no further", "unmatched
   excellence", "we've got you covered", "cutting-edge", "elevate your", "in today's digital age".
10. Mark every page with the HTML comment `dwdp:handwritten 2026-10-12` in the first 4KB.

## Design (Maurice's standing rules, check each one)
- Header/menu bar in a real brand color (blue), never dull gray. EN/ES toggle in the header on
  every page, in brand colors. Phone visible with tap-to-call.
- Hero stretches edge to edge on every page: full-strength photo, dark left-to-right fade behind
  the headline, logo/headline/buttons aligned to the left rail at 1440, 1920 and 2560 wide (use a
  `--rail: clamp(22px, 5.5vw, 140px)` style rail, not a narrow centered box). Hero stays above the
  fold (max-height about 700px) with the main button visible.
- Body text, photos and cards run FULL WIDTH, sharing the same left and right edge as the header
  and color bands. Never box text into a narrow center strip.
- Mostly WHITE sections broken by occasional bold color bands: hero, white, a deep blue band,
  white, a second band in gold or near-black. Plain sections are pure white, never pale off-white
  tints. Never every section tinted.
- No white text or white boxes on white. Every card, box, form field and button has clear
  contrast. Pricing cards must be easy to read.

## Before you finish (all must pass)
- `python3 build.py` then `python3 scripts/check.py`: 0 errors.
- `python3 scripts/check_old_urls.py`: every old URL resolves or redirects.
- Grep the built site for em/en dashes in visible text (except the Duplantis credit), the banned
  phrases, "unlimited pages", "100+", "guarantee", "#1", "testimonial", "5-star", "(832)", "(928)",
  "(689)". Fix every hit.
- No horizontal overflow at 1440, 1024, 768 and 390 px wide. Screenshot the home page and one
  city page at 1440, 1920 and 2560 and confirm the hero content starts near the left edge.
- Open the built Site Check, demo, intake and contact pages in a headless browser and confirm the
  scripts load without console errors and the forms are present with their original names.
- Independent fact-check: start separate sub-agents that did not write the pages, have them check
  every factual claim and source, and fix what they find. Record it in docs/fact-check.md. Never
  say "fact-checked" unless this was actually run.
- docs/image-list.md lists every image still needed, heroes first: File name, Size (heroes
  1920x1080, in-body 1200x800), then an Artistly prompt (bright, clearly visible, real small
  business owners' settings, no text, no logos, no recognizable faces, "wide cinematic landscape
  shot, subject positioned on right third of frame, well lit").

## Git
- Work on the branch `build`. Commit as you go with clear messages.
- Push to origin `build` at the end. Do NOT merge to main, do NOT push to main, do NOT change
  Netlify settings, do NOT pay for anything. Maurice decides when it goes live.

## Final report (Maurice reads on his phone, 5 lines max)
Pages built (count by type), checks passed, old URLs all resolving (yes/no), duplication range,
fact-check result, how many images need Artistly, and the one thing Maurice must do next.
