# Fact-check fc1: core pages (Oct 12 2026)

Checker: fc1 (independent; did not write these pages). Method per docs/fact-check/BRIEF.md.
Business claims compared word by word with INTAKE.md; claims not in INTAKE.md were traced to the
live site's own text (docs/old-site/) or softened. Outside facts checked with WebSearch (13 searches;
the shared search budget ran out before the last two, so the three Google documentation items marked
"known" below were confirmed from the wording of the cited Google pages as already known, not re-searched).
Build: `python3 build.py --out /tmp/claude-0/fc1/dist` then check.py on each page: 0 errors, 0 warnings.

## src/data/site.json vs INTAKE.md (report only, not edited)
| Item | Verdict |
|---|---|
| Name, d/b/a Dominion Digital Group, owner, phone (903) 636-7511 / +19036367511, email, address 279 Boyd Road Big Sandy TX 75755 | Match |
| phone_note "Our AI receptionist answers any hour and can put you straight through to Maurice." | Match (INTAKE's own example wording) |
| Starter $497 features (9 lines), Stripe link bJecN59ERe8u6OB4RwcMM0b | Match |
| Pro $997 features, Most Popular, chat widget free 14 days then $297/mo, Stripe eVq8wP9ERc0m1uh3NscMM0c | Match |
| Agency $1,997 features, 30 to 60 pages, waves first inside two weeks, phone agent setup + 7 days free then $297/mo up to 750 min, cancel any time, marked not part of one-time price, Stripe bJe4gz2cpfcy0qdbfUcMM0d | Match |
| hosting_note ($49/mo without the agent) and page_count_note ("thirty good ones rather than a hundred thin ones") | Match |
| Quote, Jesse Duplantis credit, John 3:16, GA4 G-3MZXMC1JKS, Facebook and YouTube links, sister brands | Match |
| same_as includes https://x.com/dominionwebpro (not listed in INTAKE) | Minor: it is on the live home page (docs/old-site/index.html), so allowed under "copy every social link the live site shows". No action. |
| plan "summary" lines (e.g. "For a business that needs a clean, working website...") | Not in INTAKE, descriptive only, no factual promise. No action. |
| google_review_url (footer "Review us on Google") | Not in INTAKE; it is on the live site. It is a link to leave a review, not a displayed review. No action. |
No price, feature or phone-wording mismatch found.

## / (index.html)
| Claim | Verdict | Source | Action |
|---|---|---|---|
| Prices $497 / $997 / $1,997 one time; Pro 10 pages + 10 city pages; Starter live 7 to 14 days; Agency waves first inside two weeks; hosting $49/mo without agent | Confirmed | INTAKE 3 | None |
| AI receptionist answers any hour, transfers on preview / Maurice / person | Confirmed | INTAKE 1 | None |
| "If he cannot pick up, it takes your name and number so he can call you back" | Removed | Not in INTAKE or live site | Deleted sentence |
| No deposit, no obligation, no contract | Confirmed | Live site (old about, demo pages) | None |
| Demo takes about a minute | Confirmed | src/static/demo.html text | None |
| Site Check reports titles, headings, speed; Before and After uses PageSpeed Insights | Confirmed | site-check/index.html, seo-audit.mjs, compare/index.html | None |
| Based in Big Sandy, East Texas; no office elsewhere | Confirmed | INTAKE 1, 5 | None |

## /services/
| Claim | Verdict | Source | Action |
|---|---|---|---|
| Google completed mobile-first indexing (Oct 2023) | Confirmed | developers.google.com/search/blog/2023/10/mobile-first-is-here (Oct 31 2023) | None |
| Sitemap is a hint, not a ranking switch | Confirmed | Google build-sitemap page ("merely a hint") | None |
| Package contents per tier, chat widget 14 days, phone agent 7 days then $297/mo up to 750 min cancel any time, hosting $49 | Confirmed | INTAKE 3 | None |
| Phone agent run with sister brand AI Voice Agent Pros | Confirmed | INTAKE 2 | None |
| Demo generator builds previews for salons, auto shops, cleaners, veterinarians, dental | Confirmed | demo.html / demo-generator.html trade lists | None |

## /pricing/
| Claim | Verdict | Source | Action |
|---|---|---|---|
| Comparison table rows (every row) | Confirmed | INTAKE 3 (Pro timeline correctly "agreed when you order", none in INTAKE) | None |
| No deposit, no contract | Confirmed | Live site | None |
| Work outside a package quoted in writing before it starts | Confirmed (live site) | Old about ("we will say so before starting"), old terms ("written proposal or invoice") | None; Maurice may confirm |
| "You can always add city pages later" | Softened | Not in INTAKE | Now "you can ask about more city pages later ... price given before any work starts" |

## /how-it-works/
| Claim | Verdict | Source | Action |
|---|---|---|---|
| Timelines table | Confirmed | INTAKE 3 | None |
| Stripe checkout | Confirmed | INTAKE buy links | None |
| Intake form collects "all of this" incl. "domain login" | Corrected | intake/index.html asks "Domain registered with", not a login | Now "most of this", "where your domain is registered", "domain access" |
| Changes by message, no ticket system | Softened | Old about page; but INTAKE ties updates to agent or $49/mo | Now "while your upkeep is active (included with the AI agent, or $49 a month)" (body and FAQ) |
| Sitemap a hint | Confirmed | Google build-sitemap | None |

## /faq/
| Claim | Verdict | Source | Action |
|---|---|---|---|
| BLS "describes the two roles the same way" (incl. performance/traffic for developers) | Softened | BLS OOH current page: designers = layout, navigation, usability; developers = construction (performance/capacity wording only in older version) | FAQ answer reworded to match current BLS wording |
| Developer can be listed as registrant; registrant definition; lookup.icann.org | Confirmed | ICANN Compliance FAQs; ICANN Acronyms and Terms: Registrant | Replaced unverified source URL icann.org/registrants with the two confirmed ICANN pages |
| No way to request or pay for a better local ranking | Confirmed | support.google.com/business/answer/7091 | None |
| Mobile-first complete Oct 2023 | Confirmed | Google blog | None |
| "Monthly services can be cancelled" | Softened | INTAKE says cancel any time only for the phone agent | Now "monthly add-ons are optional (the AI phone agent can be cancelled any time)" |
| "domain login" in what to send / what slows it | Corrected | intake form fields | Reworded |
| No reviews or portfolio on the site; prices, trials, hosting | Confirmed | INTAKE 3, 4 | None |

## /about.html
| Claim | Verdict | Source | Action |
|---|---|---|---|
| Big Sandy in Upshur County on U.S. 80, about 14 miles SW of Gilmer | Confirmed | Wikipedia Big Sandy, Texas; TexasEscapes (14 to 15 miles) | None |
| d/b/a of Dominion Digital Group; sister brands and what each does | Confirmed | INTAKE 1, 2; old about page | None |
| No setup fee, no contract, no early termination clause; "if it is wrong, it gets changed" | Confirmed | Old about page | None |
| "you can ring and talk it through" | Softened | Phone is an AI receptionist (INTAKE 1) | Now "a call can be put through to him" |
| "Nearly everyone who finds you will do it on a phone" | Softened | Unsourced statistic-like claim | Now "Many of the people who find you" |
| Changes without a ticket system | Softened | as above | Tied to active upkeep |
| Package summaries, phone agent not part of one-time price | Confirmed | INTAKE 3 | None |

## /contact/
| Claim | Verdict | Source | Action |
|---|---|---|---|
| Receptionist "or take your name and number so he can call you back" | Removed | Not in INTAKE | Deleted |
| "Maurice reads every one" / "replies himself" | Softened | INTAKE: person who builds the site can be reached; live site "Maurice will get back to you" | Now "goes to Maurice ... who gets back to you" |
| Form name homepage-contact, fields | Confirmed | Matches index.html form | None |
| Big Sandy only, no other office; email | Confirmed | INTAKE | None |

## /how-city-pages-work.html
| Claim | Verdict | Source | Action |
|---|---|---|---|
| Doorway abuse includes pages targeted at regions or cities that funnel users to one page | Confirmed | developers.google.com/search/docs/essentials/spam-policies | None |
| Keyword stuffing includes blocks of text listing cities a page tries to rank for | Confirmed (known) | Same spam-policies page | None |
| SEO Starter Guide: organize so pages' relationships are clear, descriptive URLs; hyphens in URLs; one URL per content | Confirmed (known) | SEO Starter Guide; URL structure page | None |
| Pro 10 city pages; Agency usually 30 to 60, waves, first inside two weeks; "We do not sell page counts" | Confirmed | INTAKE 3 | None |
| Rankings depend on "how established/long established the business is" | Corrected | Google local ranking: relevance, distance, prominence (how well known) | Now "how well known the business is" (FAQ and body) |
| "what it costs, once, not monthly" | Corrected | Agents are monthly add-ons | Now "website is one-time, any monthly add-on spelled out before you buy" |
| No ranking promise; no way to pay for local ranking | Confirmed | Google GBP help 7091 | None |

## /privacy-policy.html
| Claim | Verdict | Source | Action |
|---|---|---|---|
| TDPSA effective July 1, 2024 | Confirmed | Hunton; Fisher Phillips (authorized-agent part Jan 1 2025) | None |
| Google Translate loads only when ES chosen, sets googtrans cookie | Confirmed | src/static/js/site.js | None |
| GA4 incl. phone-tap, Netlify forms/hosting, Stripe, AI receptionist, Site Check server function | Confirmed | INTAKE; repo | None |
| Legal entity, address, phone wording | Confirmed | INTAKE 1 (address allowed on privacy) | None |

## /terms.html
| Claim | Verdict | Source | Action |
|---|---|---|---|
| Package prices, trials, $297/mo up to 750 min, hosting $49 | Confirmed | INTAKE 3 | None |
| Billed monthly in advance; 30-day interest; no proration; copy of site files; Upshur County venue | Confirmed | Old terms (live site); Big Sandy is in Upshur County (Wikipedia) | None |
| Paid in full at checkout via Stripe | Confirmed | INTAKE Stripe buy links | None |
| No promise of ranking, traffic, leads | Confirmed | INTAKE 3, 4 | None |

## /404.html
| Claim | Verdict | Source | Action |
|---|---|---|---|
| Prices, receptionist wording, tool descriptions | Confirmed | INTAKE; tool pages | None |

## /service-areas.html
| Claim | Verdict | Source | Action |
|---|---|---|---|
| Texas about 3.5 million small businesses (3.52M), second to California (4.34M) | Confirmed | SBA Advocacy 2025 release (advocacy.sba.gov/?p=30239) and Texas 2025 State Profile | None |
| "Most of them ... live or die on whether a nearby customer can find them" | Softened | Not in the SBA source | Now "Many ... depend on nearby customers finding them" |
| More than a quarter of Houston residents foreign born (28.8%) | Confirmed | Census QuickFacts Houston city, 2019 to 2023 | None |
| El Paso runs on Mountain Time | Confirmed (known) | El Paso and Hudspeth counties are in the Mountain Time Zone | None |
| Big Sandy in Upshur County | Confirmed | Wikipedia | None |
| "Houston, Dallas and Austin are where Texas owners type web design + city most often" | Softened | Keyword file is seed-limited (no San Antonio, Fort Worth seeds) | Now "In our keyword data ..." |
| Kingwood, Waco, El Paso clear 10 searches/mo | Confirmed | keywords xlsx (30, 50, 880) | None |
| "A meeting in person is possible" | Softened | Not in INTAKE | Now "If meeting in person would genuinely help, call and ask." |
| Georgia pages "from earlier work" / "into the Gwinnett County market" | Corrected | "earlier work" can read as client work; Atlanta is not in Gwinnett | Now "earlier research into metro Atlanta and Gwinnett County" |
| Packages, $49 hosting | Confirmed | INTAKE 3 | None |

## /web-design/ (web-design/index.html)
| Claim | Verdict | Source | Action |
|---|---|---|---|
| "from earlier work" | Softened | could imply clients | Now "earlier research" |
| "A town with no searches gets no page" | Removed | Contradicted by existing pages for small towns (e.g. Gladewater) kept from the live site | Deleted sentence |
| "Google has learned to ignore that [swapped city pages]" | Corrected | Google spam policies, doorway abuse | Reworded to the policy and added a Sources block |
| Receptionist wording; same prices everywhere; demo first; owns site | Confirmed | INTAKE | None |

## Summary
Checked 96 claims: 72 confirmed, 7 corrected, 14 softened, 3 removed.
No mismatch between src/data/site.json and INTAKE.md. Items for Maurice to confirm: "work outside a
package is quoted in writing" (pricing, terms, about) and the legal pages generally (not legal advice).
