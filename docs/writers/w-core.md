# Writer notes: w-core (core pages)

Written Oct 12 2026. Prices, package contents, timelines, phone/AI receptionist wording, address and sister brands come from INTAKE.md and src/data/site.json (no outside source needed). 11 web searches used. WebFetch was not available, so every outside fact below was checked against search results that quoted the official or credible source.

## /services/ (src/pages/services.html): target "web design services"
- Google finished the move to mobile-first indexing in October 2023. Source: https://developers.google.com/search/blog/2023/10/mobile-first-is-here
- Google calls a submitted sitemap a hint, not a promise of crawling. Source: https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap
- The AI phone agent is run with sister brand AI Voice Agent Pros (INTAKE: "AI chat widget and AI phone agent (sister brand AI Voice Agent Pros)").
- Left out: no client or trade claims; "the demo generator already builds previews for" salons, auto shops, cleaners, veterinarians and dental offices is based on the demo-images folders that exist (salon, auto-repair, cleaning, veterinary, dental).

## /pricing/: target "small business website package"
- Comparison table built only from INTAKE.md section 3. INTAKE gives no separate timeline for Pro, so the table says "Timeline agreed when you order" instead of inventing one.
- "Work outside a package is quoted in writing before it starts": based on the old about page ("Bigger jobs cost more and we will say so before starting") and old terms ("written proposal or invoice"). Maurice should confirm.
- Example businesses (a barber in Big Sandy, a food truck, etc.) are hypothetical illustrations, not clients.

## /how-it-works/: target "web design process"
- Timelines exactly as INTAKE (Starter 7 to 14 days; Agency in waves, first inside two weeks; Pro not stated, so "agreed when you order").
- "The demo takes about a minute": from the live site's own text (old about.html and home).
- Sitemap is a hint: Google Search Central build-sitemap page (above).
- Payment through Stripe checkout: INTAKE buy buttons are Stripe links.

## /faq/: target "web design questions"
- Web design vs web development split (designers: layout, navigation, usability; developers: create and maintain sites, performance and capacity). Source: BLS Occupational Outlook Handbook, Web Developers and Digital Designers, https://www.bls.gov/ooh/computer-and-information-technology/web-developers.htm
- Mobile-first indexing complete October 2023 (source above).
- ICANN: the registrant is the person or entity holding the rights to a domain; a developer who registers with their own details may be listed as registrant; free lookup tool at lookup.icann.org. Sources: https://www.icann.org/registrants and https://lookup.icann.org/
- Google: no way to request or pay for a better local ranking. Source: https://support.google.com/business/answer/7091?hl=en
- Left out: BLS pay and growth figures (not relevant to buyers).

## /about.html: target "local web designer near me"
- Kept from docs/old-site/about.html: "built before you pay", phone-first, own photos, changes without a ticket system, sister brands paragraph.
- Dropped: "Bellingham to St. Petersburg" (client-sounding claim), "AI agent free for 14 days" (wrong per INTAKE: chat widget 14 days, phone agent 7 days), Dominion Solar Pro (not in INTAKE), "ring and talk to a person" (phone is an AI receptionist).
- Big Sandy is in Upshur County on U.S. Highway 80, about 14 miles southwest of Gilmer. Source: https://en.wikipedia.org/wiki/Big_Sandy,_Texas (also ETCOG listing https://www.etcog.org/big-sandy)
- Google: no way to pay for a better local ranking (source above).

## /contact/: target "find a web designer near me"
- Form copied byte for byte from src/pages/index.html (verified with diff: name="homepage-contact", action /contact/thanks/, data-netlify, honeypot company_url, fields name, business, phone, email, message).
- No street address on this page (per instructions). Phone note, email, Big Sandy, link to /intake/.
- "Maurice replies to form messages and email himself": based on INTAKE ("the person who builds the site can be reached"). Maurice should confirm.

## /how-city-pages-work.html: target "seo structure for website"
- Kept from docs/old-site/how-city-pages-work.html: what a city page is, the Kilgore flooring and Longview remodel examples, the multiplication idea, the Kilgore salon example, "what this does not promise".
- Fixed: Agency was "a hundred or more city pages", now "usually 30 to 60" per INTAKE. Multiplication table rows of 90 and 180 pages removed (they implied page counts above what is sold); new rows top out at 60. Removed the claim "This site is built the same way, nine ways of describing web design across the towns we serve. You are reading one of the pages it produced" (not true of this build). Removed the YouTube video thumbnail.
- Google spam policies, doorway abuse: "multiple domain names or pages targeted at specific regions or cities that funnel users to one page"; keyword stuffing includes "blocks of text that list cities and regions that a web page is trying to rank for". Source: https://developers.google.com/search/docs/essentials/spam-policies
- SEO Starter Guide: organize the site so people and search engines understand how pages relate; descriptive URLs. Source: https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- URL guidance: hyphens between words; one URL per piece of content (canonical/redirects). Sources: https://developers.google.com/search/docs/crawling-indexing/url-structure and the SEO Starter Guide.

## /privacy-policy.html and /terms.html
- Substance kept from docs/old-site versions (Aug 25 2026), date updated to Oct 12 2026. Business identity per INTAKE.
- Added: GA4 analytics and phone-tap event, Netlify hosting and forms, Google Translate toggle (loads only when ES is chosen, sets the `googtrans` cookie; checked in src/static/js/site.js), Stripe checkout, AI receptionist calls, Site Check sends the entered URL to a server function.
- Texas Data Privacy and Security Act took effect July 1, 2024. Source: https://www.hunton.com/insights/legal/texas-enacts-texas-data-privacy-and-security-act (and Fisher Phillips, Haynes Boone alerts in search results).
- Upshur County as the venue: from the old terms; Big Sandy is in Upshur County (source above).
- Terms changed from old: "Prices shown on this website are starting points, not binding offers" replaced with the INTAKE package prices plus "work outside a package is quoted in writing" (the old line contradicted the exact prices). "We do not guarantee" changed to "we do not promise" (banned word). "Package prices are paid in full at checkout through Stripe" follows from the INTAKE Stripe buy links. The AI receptionist call record line ("may include what you told the receptionist") is hedged because the provider's exact recording/transcript behavior was not verified. Maurice should confirm both legal pages; they say they are not legal advice.

## /404.html
- noindex, no hero, helpful links only. No outside facts.

## Images
- Reused: demo-images/default/3 and default/1, plumbing/2, legal/3, electrical/1, cleaning/1, hvac/1, photography/2, roofing/1, salon/1, real-estate/1; images/contractors/contractor-work and contractor-review; images/cities/marshall-business, longview-business, gladewater-business, kilgore-business, et-street-b, longview-tx.
- Planned (listed by the build in docs/image-list.md): images/heroes/pricing-hero.jpg, images/heroes/faq-hero.jpg, images/heroes/contact-hero.jpg.
