# Writing guide for page writers (Dominion Web Design Pro rebuild, Oct 12 2026)

Read first, in full: `CLAUDE.md`, `INTAKE.md`, `SERVICES.md`, and `src/pages/index.html` (the
finished home page is the model for front matter and markup). Your keyword assignments are in
`docs/keyword-plan.md` under each page's URL. INTAKE.md wins over everything else.

## 1. Files you write

- One file per page in `src/pages/`. Folder URLs: `src/pages/<slug>.html` builds to `/<slug>/`.
  Flat live URLs keep their exact URL with `url:` in front matter, e.g. `url: "/about.html"` or
  `url: "/web-design/houston-tx.html"` (file name `src/pages/web-design/houston-tx.html`).
- A notes file `docs/writers/<your-agent-name>.md`: for each page, the target keyword, the facts you
  stated and the source of each one (URL), and anything you left out because you could not verify it.
  The independent fact-checkers read this.
- Do NOT edit shared files: `build.py`, `src/templates/*`, `src/static/*`, `src/data/site.json`,
  `scripts/*`, other writers' pages. If you need a change there, say so in your final report.

## 2. Front matter (YAML between `---` lines)

```yaml
title: "Web Design in Houston, TX | Dominion Web Design Pro"   # unique, 50 to 65 characters
description: "..."            # unique, 120 to 160 characters, includes the target keyword
h1: "..."                     # unique, includes the target keyword naturally
type: area                    # home | page | service | guide | area | about | contact | legal
url: "/web-design/houston-tx.html"   # only for flat .html URLs
crumb: "Houston, TX"          # short breadcrumb label (optional)
summary: "..."                # area pages only: one line (max 160 chars) for the city directory cards
city_name: "Houston"          # area pages only ("East Texas" for the regional page)
state_name: "Texas"           # area pages only
schema_service: {name: "Web design in Houston, Texas", type: "Web design"}   # service and area pages
hero:
  image: images/cities/austin-skyline.jpg      # path inside src/static/
  alt: "..."
  desc: "Artistly scene description, used only if the file does not exist yet"
  position: "60% 50%"         # optional object-position
  lead: "One or two short sentences under the H1."
  secondary_label: "..."      # optional; default "See the packages" -> /pricing/
  secondary_href: "..."
faqs:                          # 3 to 6, written the way people ask (use the Question rows)
  - q: "..."
    a: "<p>...</p>"
cta_title: "..."               # optional custom heading for the closing call band
published: 2026-10-12          # guides only (optional)
```

The primary hero button is always "Get a free demo" (/demo.html). The hero note under the buttons
already gives the phone number and the AI receptionist sentence; do not repeat it in the lead.

## 3. Body markup

The body is `{% block content %} ... {% endblock %}`. Never put an `<h1>` in the body.

- White section: `<section class="prose"> ... </section>` (most sections are white).
- Color band: `<section class="band band--tint"><div class="wide"> ... </div></section>`. The build
  turns the first band deep blue and the second gold automatically. Use one or two bands per page,
  never more than three, never two in a row. The FAQ block and the closing call band are added by
  the template; do not write them.
- Layout helpers: `<div class="split">` (text and image side by side), `grid-2`, `grid-3`,
  `<div class="panel">`, `<div class="note">`, `<ol class="steps">` with `<li><strong>Title</strong>text</li>`,
  `<ul class="checks">`, `<ul class="facts">` with `<li><strong>label</strong>value</li>`,
  `<div class="table-wrap"><table><thead>...</thead><tbody>...</tbody></table></div>`.
- Macros (call as `{{ m.name(...) }}`): `m.pricing_cards()` (the three packages, exactly as INTAKE
  states them; use this instead of retyping package lists), `m.process_steps()`, `m.service_cards(['slug', ...])`,
  `m.guide_cards(['slug', ...])`, `m.area_pills(exclude='houston-tx')` or `m.area_pills(group='dfw')`,
  `m.area_directory()`, `m.related(['contractor-website-design', 'guide:small-business-website-cost', 'area:tyler-tx'], 'Related pages')`,
  `m.demo_box('custom sentence')`, `m.phone_note()`, `m.no_office('Houston')`,
  `m.sources([{'label': 'U.S. Census Bureau QuickFacts: Waco city, Texas', 'url': 'https://...'}])`.
- Images: `{{ img("demo-images/plumbing/2.jpg", "alt text", 1344, 768) }}`. Every page needs a hero plus
  at least two in-body `img()` figures. Wide 1536x640 photos read best as a full-width figure, not
  inside a `split`. 1344x768 and 1200x686 photos work in a split.

### Existing photos you may use (paths inside src/static/)

Reuse these first, only where they genuinely fit the page:

- `images/cost-page-hero.jpg` (person at a laptop, 1536x640, used on the home page hero too)
- `images/contractors/contractor-hero.jpg` (contractor with phone at sunset, 1536x640),
  `contractor-work.jpg` and `contractor-review.jpg` (1200x686)
- `images/cities/`: `austin-skyline.jpg`, `cedar-park-hero.jpg`, `denton-hero.jpg`, `dripping-springs-hero.jpg`,
  `frisco-hero.jpg`, `kyle-hero.jpg`, `leander-hero.jpg`, `mckinney-hero.jpg`, `new-braunfels-hero.jpg`,
  `pflugerville-hero.jpg`, `plano-hero.jpg`, `san-marcos-hero.jpg`, `longview-tx.jpg`, `gilmer-street.jpg`,
  `et-street-b.jpg` (East Texas main street), `lawrenceville-courthouse-district.jpg`, `lawrenceville-storefronts.jpg`,
  `gwinnett-international-corridor.jpg`, `atlanta-small-business.jpg`, `atlanta-sole-proprietor.jpg`,
  `atlanta-food-truck.jpg` (all 1536x640); `gilmer-business.jpg`, `gilmer-industry.jpg`, `gladewater-business.jpg`,
  `kilgore-business.jpg`, `kilgore-industry.jpg`, `longview-business.jpg`, `longview-industry.jpg`,
  `marshall-business.jpg`, `marshall-industry.jpg` (1200x686); `tyler-tx.jpg` (1280x813, photo by Larry D. Moore,
  CC BY 4.0: give a figcaption credit "Photo: Larry D. Moore, CC BY 4.0").
  Look at what the old page used each photo for before reusing it.
- `demo-images/<trade>/<n>.jpg` (1344x768). Use ONLY these (the others have words printed on them):
  auto-repair 1-4, chiropractic 4, 5, 6, 8, cleaning 1-4, default 1-3, dental 1-4, electrical 1-4, gym 1-4,
  hvac 1-4, insurance 1-4 (offices), landscaping 1, 2, 4, legal 3, photography 1-4, plumbing 1-4,
  real-estate 1-3, restaurant 1-4, roofing 1, 3, 4, salon 1-4, veterinary 1-4.

### Photos that do not exist yet

If no existing photo fits, plan one: `{{ img("images/body/houston-<topic>.jpg", "alt", 1200, 800, desc="Artistly scene: ...") }}`
for in-body (1200x800) and `hero.image: images/heroes/<slug>-hero.jpg` with `desc:` for heroes (1920x1080).
The build lists them in docs/image-list.md and shows a brand-color block until they arrive. The desc
is the Artistly prompt: a real small business owner's setting in that place or trade, bright, no
text, no logos, no recognizable faces. Do not invent a landmark you have not verified.

## 4. Hard rules (scripts/check.py fails the build on most of these)

1. Never invent reviews, testimonials, clients, portfolio pieces, ratings, awards, certifications,
   years in business, job counts, statistics about the business, guarantees or ranking promises.
   Spec demos are not clients. Do not say Maurice has built sites for any named business, town or
   trade ("we have built for businesses from X to Y" is out).
2. Prices and package contents only exactly as INTAKE.md. Use `m.pricing_cards()` where you show the
   packages. In prose: Starter $497, Pro $997, Agency $1,997, all one time. Pro's AI chat widget is
   free for 14 days then $297/mo. Agency includes AI phone agent SETUP; the agent is free for 7 days,
   then $297/mo for up to 750 minutes, cancel any time, and it is NOT included free with the one-time
   price. Hosting, maintenance and updates: included while the client keeps the AI agent, otherwise
   $49/mo. Never "unlimited pages", "100+ pages", a three-month minimum, a yearly discount, or any
   number of leads or rankings. Keep the "We do not sell page counts" idea where pages are discussed.
3. The phone (903) 636-7511 is answered by an AI receptionist any hour, which transfers callers who
   ask about a website preview, or ask for Maurice or a person, to Maurice. Never say a person always
   answers.
4. No em dashes or en dashes anywhere (write "$500 to $1,000", not a dash range). No eyebrow labels
   above headings. American spelling.
5. 3 to 6 FAQs per page (not privacy, terms, 404), phrased like real searches, answered fully.
6. Hero plus at least two in-body images, each with real alt text.
7. Facts must be real and current. Research with WebSearch (WebFetch and curl are blocked in this
   environment, so verify from search results of the official or credible source). Cite sources with
   `m.sources([...])` on guide pages and on every page that states a researched fact (city pages
   included). If you cannot verify something, leave it out. No made-up numbers, no "studies show".
   You have a limited search budget: about 15 to 20 searches for your whole assignment, so search
   only for facts you will actually state.
8. Each page is written for its own keyword and its own reader. Do not reuse sentences or paragraph
   structures across pages, even your own. Pages of the same type must stay under 15% Jaccard
   similarity (5-word shingles); write each one fresh.
9. Banned: "your trusted partner", "one-stop solution", "look no further", "unmatched excellence",
   "we've got you covered", "cutting-edge", "elevate your", "in today's digital age", "guarantee"
   (in any form, even "we can't guarantee": say "promise" instead), "#1", "testimonial", "5-star",
   "top-rated", "certified", "award-winning", "our clients", "happy clients", "unlimited".
10. Never imply an office anywhere except Big Sandy. On every city page use `m.no_office('City')`
    once and say plainly that the site is built remotely from East Texas.
11. The target keyword goes in the title, the H1, the first paragraph and one H2, naturally. Weave
    supporting keywords in where they read naturally; use question keywords as FAQ questions.
    Never stuff.
12. Every internal link uses an exact URL from SERVICES.md (`/about.html`, `/pricing/`,
    `/web-design/tyler-tx.html`, `/demo.html`, `/site-check/`, `/contact/`, `/faq/`, `/how-it-works/`).

## 5. Page-type requirements

**Service pages (Playbook Prompt 9).** What the service is, who it fits, common problems for that
kind of business, the verified approach (demo first, hand-written pages, the package contents), the
process, which package fits, related services, 3 to 6 service-specific FAQs. At least one design
treatment suited to the service (a comparison table, a checklist of what the site must have, a
before/after list, a page plan). Aim for 1,400 to 2,200 words of your own copy.

**Guides.** Answer the question in the first paragraph, then go deep: real price ranges or facts
with cited sources, a table where it helps, what changes the answer, how Dominion's packages
compare (honestly, including when Dominion is not the right choice). 1,500 to 2,500 words. Sources
block at the end of the content.

**City pages (Playbook Prompt 11 plus CLAUDE.md).** Written for THAT city: its business makeup,
real neighborhoods and commercial corridors, its chamber of commerce and small business resources
(SBDC, SCORE, city economic development), why local search matters there, and what kind of local
businesses benefit. A localized H2 with two local paragraphs and an image beside it. Services that
fit the city. A section "Four reasons a [City] business would hire Dominion Web Design Pro" with
four distinct, honest, local reasons (no client claims). Area FAQs. `m.no_office()`. Sources.
Existing city pages: keep their researched local facts and good writing, re-verify the facts you
keep, drop anything that breaks the rules above (old pages contain "Unlimited pages", "three-month
minimum", "ten months instead of twelve", "14 days" for the phone agent, and client-sounding claims:
all of that goes). The Gilmer page's statement that Maurice grew up in Gilmer is his own statement
on the live site and may stay. 1,400 to 2,200 words of your own copy.

## 6. Voice

Plain, direct, specific, like a capable tradesman explaining his work. Short paragraphs. Talk to a
small business owner who has been burned by a web company before. "We" is the business; Maurice is
the person who writes and builds the site. No hype, no filler, no rhetorical questions stacked up.

## 7. Check your work before you report

Other writers build at the same time, so always build into your own folder (never plain `python3 build.py`):
```
python3 build.py --out /tmp/claude-0/<your-agent-name>/dist
python3 scripts/check.py --skip-links --dist /tmp/claude-0/<your-agent-name>/dist --only /your-url
python3 scripts/similarity.py --dist /tmp/claude-0/<your-agent-name>/dist
```
Fix every ERROR on your pages. Warnings about word count mean the page is too thin. Links to pages
another writer has not finished yet are expected (that is what `--skip-links` is for), but every URL
must be one listed in SERVICES.md. Your final report: pages written, word counts, searches used,
anything you could not verify, any shared-file change you need.
