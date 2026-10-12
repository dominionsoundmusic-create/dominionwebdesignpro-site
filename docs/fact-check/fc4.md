# Fact-check fc4: cost and package guides (Oct 12 2026)

Checker: fc4, independent (did not write these pages). Method: WebSearch only (WebFetch/curl blocked), restricted to the vendor's or publisher's own domain where possible; 22 searches. Keyword CPCs checked directly in keywords/Web-Design-Keywords.xlsx (ALL tab). Business claims checked against INTAKE.md. Build: `python3 build.py --out /tmp/claude-0/fc4/dist`, then `scripts/check.py --skip-links`: 0 errors on all four pages. (One error elsewhere in the build: /web-design/pflugerville-tx.html has the banned word "certified" in "Tourism Friendly Texas Certified Community". That page is not mine and I did not change it.)

## /small-business-website-cost.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Freelancer basic 5 to 10 page site $500 to $5,000 | Confirmed | clutch.co/resources/how-to-create-a-budget-for-a-new-website | none |
| Agencies about $2,000 to $100,000; most Clutch projects under $10,000 | Confirmed | clutch.co/web-designers/pricing (Oct 2026, updated Aug 27 2026) | none |
| Clutch shortlisted firms about $100 to $149/hr | Confirmed | clutch.co/web-designers/pricing | none |
| Upwork web designers about $15 to $30/hr | Confirmed | upwork.com/hire/web-designers/cost/ | none |
| Wix Light $17, Core $29, Business $39 (annual) | Confirmed | websitebuilderexpert.com Wix pricing; vp0.com | none |
| Squarespace Core $29 annual / $39 monthly, after a mid-2026 increase | Corrected | squarespace.com/pricing; PetaPixel Jul 17 2026; NoJoke Agency | Made it "July 2026" (took effect July 6 2026); added PetaPixel source |
| DIY $200 to $600 a year | Confirmed (arithmetic on plan prices) | as above | none |
| Domain $0 to $20/yr, hosting $2 to $80/mo, plugins $0 to $600/mo, support $2 to $300/mo | Confirmed | Clutch budget guide | none |
| .com wholesale $10.26, rising to $10.97 on Nov 1 2026 | Confirmed | Domain Name Wire Apr 23 2026; Verisign Q1 2026 materials; OSIR | none |
| "renewals under about $11 are at or near cost" | Corrected | ICANN fee $0.20 on top (OSIR, Openprovider) | Now says about $10.50 now, about $11.20 after Nov 1, with the $0.20 ICANN fee |
| Let's Encrypt free, nonprofit | Confirmed | letsencrypt.org (ISRG, 501(c)(3)) | none |
| Shopify Basic $29/mo yearly, $39 monthly | Confirmed | NerdWallet; websitebuilderexpert | NerdWallet URL had moved; updated to nerdwallet.com/business/software/learn/shopify-pricing |
| CPC: web design services $36.69, web designers near me $35.40, web design services for small business $22.40 | Confirmed | keywords xlsx: 36.69, 35.4, 22.4 | none |
| Year one/two math ($6,600/$3,600; $1,085/$588) | Confirmed (arithmetic) | n/a | none |
| Dominion packages, $49 hosting, trials (14 days chat, 7 days phone, $297/mo, 750 min) | Confirmed | INTAKE.md | none |
| No office outside Big Sandy; AI receptionist wording; no ranking promise | Confirmed | INTAKE.md | none |

## /how-much-does-a-website-designer-cost/

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Upwork $15 to $30/hr | Confirmed | upwork.com/hire/web-designers/cost/ | none |
| Clutch $100 to $149/hr; projects $2,000 to $100,000 | Confirmed | clutch.co/web-designers/pricing | none |
| BLS May 2025 median: web and digital interface designers $104,000; web developers $92,650 | Confirmed | bls.gov OOH web-developers.htm | none |
| $104,000 / 2,080 hours = about $50/hr | Confirmed (BLS OEWS hourly median is $50.00) | bls.gov | none |
| Self-employment tax 15.3% (12.4% SS + 2.9% Medicare), employer would split | Confirmed | irs.gov Topic 554 | none |
| Upwork project-type rates ($15 to $40+, $20 to $50+, $45 to $75+) and "10 hours to several dozen" | Corrected | Those figures come from an older Upwork page (about 3 years old). Current Upwork page lists flat project prices instead | Replaced with the current Upwork figures: about $300 to $1,500 for a landing page and $1,500 to $5,000 for a 5 to 10 page business website |
| "Independent U.S. designer billing $75 to $125 an hour is not overcharging" | Softened | no source (writer flagged it) | Now "well above $50 an hour is not necessarily overcharging" |
| FAQ: "Freelancers with a U.S. client list... usually fall between those two" | Softened | no source | Now "Many independent designers set their rates somewhere between those two" |
| Freelancer 5 to 10 pages $500 to $5,000 | Confirmed | Clutch budget guide | none |
| Dominion prices, $49, $297 after trials, not part of one-time price | Confirmed | INTAKE.md | none |

## /website-cost-per-month/

| Claim | Verdict | Source | Action |
|---|---|---|---|
| .com wholesale $10.26 to $10.97 Nov 1 2026, announced April | Confirmed | Domain Name Wire; Verisign Q1 2026 | none |
| Registrars add a small ICANN fee | Confirmed ($0.20) | OSIR; Openprovider | none |
| Cloudflare at cost just over $10, Namecheap about $14, GoDaddy about $23 | Corrected | domainoffer.net: Cloudflare $10.46, Namecheap $14.78, GoDaddy $22.99 | Now about $10.50 (wholesale plus ICANN fee, before November), about $15 and about $23. Replaced the unverified DevToolPicks source with the two DomainOffer pages |
| Hostinger Premium intro $3 to $4, renews $10.99 | Corrected | findstack; websitebuilderexpert: $2.99 intro, $10.99 renewal | Intro now "around $3 a month on a long term" |
| Bluehost Basic intro $3 to $4, renews $9.99 | Softened | Reviews disagree: $8.99, $9.99, $10.99 and $11.99 renewal; $2.95 intro on 36 months (Tooltester, websiterating) | Now "around $3 on a three-year term" and renews "somewhere between about $9 and $12". Table row is now "$9 to $12". Added Tooltester source |
| Hosting $2 to $80, SSL $0 to $1,000/yr, plugins $0 to $600, support $2 to $300 | Confirmed | Clutch budget guide | none |
| Google Workspace Business Starter $7 annual, $8.40 flexible | Confirmed | emailvendorselection.com and others | none |
| Microsoft 365 Business Basic $6 to $7 on July 1 2026 | Confirmed | office-watch.com; UC Today; TechInformed | none |
| Wix Light $17, Core $29, Business $39, Business Elite $159 annual; Core first with ecommerce | Confirmed | websitebuilderexpert; CostBench | none |
| Squarespace Core $29/$39; Basic $19, Plus $49, Advanced $99 annual; Basic 2% fee, Core and up 0% | Confirmed | squarespace.com/pricing; PetaPixel; NoJoke; CostBench | Added PetaPixel source |
| Let's Encrypt free nonprofit | Confirmed | letsencrypt.org | none |
| FAQ: DIY year cost $300 to $600 | Corrected | arithmetic: Squarespace Plus $588 + inbox $84 + domain is about $690 | Now "$300 to $700 ... depending on the plan" |
| Budget examples (about $37/mo, about $450/yr; about $18/mo) | Confirmed (arithmetic) | n/a | none |
| Dominion: $49/mo or included with agent; chat 14 days then $297; phone agent setup, 7 days then $297 up to 750 min, cancel any time | Confirmed | INTAKE.md | none |
| "no contract on the website itself" | Removed | not in INTAKE.md | Deleted |

## /web-design-packages-explained/

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Google warns about SEOs who claim a special relationship or promise first place, and says to find someone else | Confirmed | developers.google.com/search/docs/fundamentals/do-i-need-seo | none |
| Dominion packages (m.pricing_cards), $49, $297 after trials, optional agents, no stores/logins | Confirmed | INTAKE.md | none |
| "All three are one-time prices with no contract on the website" | Corrected | INTAKE.md says one-time and owned outright; no contract terms stated | Now "All three are one-time build prices." |
| "Three tiers / most popular" market pattern; red flags | Opinion and advice, no factual claim | n/a | none |

## Summary
Checked 48 claims: 35 confirmed, 8 corrected, 4 softened, 1 removed.
