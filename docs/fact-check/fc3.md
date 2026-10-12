# Fact-check fc3 (independent, Oct 12 2026)

Checker: fc3 (did not write these pages). Writer notes read: docs/writers/w-svc2.md.
Method: WebSearch restricted to official or primary domains where possible (WebFetch blocked).
16 WebSearch calls used; the shared search budget ran out on the 17th, so one citation that could
not be checked (HHS "Are you a covered entity?" URL) was replaced with a verified HHS page.
Build: `python3 build.py --out /tmp/claude-0/fc3/dist`, then `scripts/check.py --skip-links --only <url>`
for all five pages: 0 errors, 0 warnings.

Business claims on all five pages were compared with INTAKE.md (prices, page counts, Pro chat widget
14 days then $297/mo, Agency phone agent setup, free 7 days then $297/mo for up to 750 minutes,
hosting $49/mo without the agent, no clients, no reviews, no ranking or lead promises, Big Sandy
only). All matched, except one checklist line that implied schema on every package (fixed below).

## /contractor-website-design/

| Claim | Verdict | Source | Action |
|---|---|---|---|
| BrightLocal 2025 Local Consumer Review Survey: only 4% say they never read online reviews | Confirmed | brightlocal.com/research/local-consumer-review-survey-2025/ | None |
| Search Console "Discovered, currently not indexed" = Google found the URL but has not crawled it yet | Confirmed | support.google.com/webmasters/answer/7440203 and Google Search Central community guide | None |
| "Some sit there for months" | Softened | Not verifiable as a general fact | Now "Pages can stay in that state for a long time." |
| Package details (Starter, Pro, Agency, agent trial, $49 hosting) | Confirmed | INTAKE.md | None |
| No ranking promise; nationwide remote; based in Big Sandy | Confirmed | INTAKE.md | None |

## /web-design-for-plumbers/

| Claim | Verdict | Source | Action |
|---|---|---|---|
| 22 TAC 367.10: RMP of record and company owner must ensure advertisements soliciting plumbing business state the RMP's license number regardless of media | Confirmed | law.cornell.edu/regulations/texas/22-Tex-Admin-Code-SS-367-10 (subsection c) | None |
| Examples named in the rule: business cards, flyers, handouts | Corrected | Same | Added "referral coupons and other handouts" to match the rule text |
| Website = advertising, "safe practice" to show number; ask TSBPE | Confirmed as framed (opinion, not legal advice; disclaimer present) | Same | None |
| TSBPE public license search shows status, expiration, disciplinary actions | Confirmed | tsbpe.texas.gov How-To Public License Search PDF | None |
| "Board's consumer page tells homeowners to look for the license number on written estimates and invoices" | Corrected | 22 TAC 367.10(b) requires RMP name and license number on first page of proposals, invoices and contracts; the TSBPE consumer page says the number should be displayed in all advertisements | Rewritten to attribute each point to the right source |
| Google: service-area businesses should hide address, plumber at home is the example | Confirmed | support.google.com/business/answer/3038177 | None |
| Google: service area should not extend past about 2 hours driving | Confirmed | Same | None |
| Checklist: "Page titles, descriptions, schema and a sitemap" (every plumber site) | Corrected | INTAKE.md: schema is Pro | Now "...plus schema markup on Pro and Agency" |
| Package prices and contents | Confirmed | INTAKE.md | None |
| TSBPE still the regulator in 2026 | Confirmed (no transfer found; continued by HB 636, 2021) | capitol.texas.gov HB 636 (87R) analysis | None |

## /roofing-contractor-website-design/

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Illegal in Texas for a contractor to offer to waive, rebate or absorb a deductible | Confirmed | tdi.texas.gov roofing-and-insurance-know-the-law; Bus. & Com. Code 27.02 | None |
| Contractor may not act as public adjuster or advertise to adjust claims on property it does or may work on | Confirmed | Ins. Code 4102.163; TDI page | None |
| Contracts of $1,000 or more paid by insurance must include a notice that the policyholder must pay the deductible | Confirmed | TDI page | None |
| "In Texas [roofing rules] have been changing" | Corrected | HB 3344 (89R, 2025) House committee analysis: Texas does not currently require a state license for reroofing contractors; bill would create a TDLR license. Final passage could not be confirmed on any official source; no TDLR roofing program found on tdlr.texas.gov | Now names HB 3344 as a proposed 2025 bill and tells roofers to check TDLR and their city; does not state it passed or failed. Source added |
| RCAT / manufacturer credentials as "voluntary credential" | Confirmed as framed (general) | n/a | None |
| No insurance or legal advice | Confirmed: page says "We write marketing copy, not legal advice" | n/a | None |

## /web-design-for-law-firms/

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Model Rule 7.1: no false or misleading communication about the lawyer or services | Confirmed | americanbar.org Rule 7.1 and comment | None |
| "Misleading even if literally true ... when it is likely to create unjustified expectations" (stated as the rule) | Corrected | Unjustified-expectation language is in Comment [3], not the rule text since the 2002/2018 amendments | Rule text and comment now described separately; FAQ says "the comments to ABA Model Rule 7.1" |
| "ABA Model Rules limit when a lawyer may say they are a specialist" | Corrected | Model Rule 7.2(c) limits claims of certification as a specialist; lawyers may say they specialize subject to 7.1 | Now "may claim a specialist certification"; ABA 7.2 comment cited |
| Texas Rules 7.01 to 7.03 "cover the content" | Softened | Rule 7.01 is definitions; 7.02 and 7.03 content | Now "set out the definitions and the content rules" |
| Rule 7.04: file with Advertising Review Committee no later than ten days after dissemination | Confirmed | legalethicstexas.com Rule 7.04 | None |
| Rule 7.05(b): website content exempt except homepage unless otherwise exempt; whole site must still comply | Confirmed | legalethicstexas.com Rule 7.05 and comment 2; July 2025 Ethics Question of the Month | None |
| ABA Formal Opinion 10-457 (2010): contact info alone generally does not create prospective client; specifically inviting information can; Rule 1.18 duties and conflicts | Confirmed | americanbar.org product page for 10-457; ABA Formal Op. 492 quoting Rule 1.18 cmt [2] | Replaced the secondary ezel.ai summary with the ABA's own listing |
| No legal advice; client's counsel decides wording | Confirmed (disclaimers present in band intro, FAQs and intake section) | n/a | None |
| Package prices | Confirmed | INTAKE.md | None |

## /web-design-for-therapists/

| Claim | Verdict | Source | Action |
|---|---|---|---|
| HIPAA covered entity: provider covered only if it transmits health information electronically in connection with a standard transaction (claims) | Confirmed | hhs.gov covered-entities page; HHS Privacy Rule summary | None |
| "Plenty of private-pay therapists fall outside that, and plenty of in-network ones fall inside it" | Softened | HHS Privacy Rule summary (email alone does not make a provider covered; billing services count) | Rewritten to say what HHS says, with "may" and "generally" |
| Source URL hhs.gov/guidance/document/are-you-covered-entity | Removed | Could not verify (search budget exhausted) | Replaced with HHS Summary of the HIPAA Privacy Rule |
| 988: free, confidential, call, text or chat, 24/7; 911 for emergencies | Confirmed | 988lifeline.org; samhsa.gov 988 FAQs | SAMHSA FAQ added as a source |
| Psychology Today: professionals pay a fixed monthly fee to be listed | Confirmed | psychologytoday.com/us/about | Source changed from the UK (/gb/) page to the US page |
| Counseling and psychology licenses are issued by states | Confirmed (general knowledge, uncontroversial) | n/a | None |
| No medical or compliance advice | Confirmed: page sends readers to their compliance advisor or attorney | n/a | None |
| Package prices, Starter live in 7 to 14 days | Confirmed | INTAKE.md | None |

## Summary

Checked 44 | Confirmed 32 | Corrected 8 | Softened 3 | Removed 1

Most important fixes: ABA 7.1 "unjustified expectations" moved from the rule to its comments;
specialization limit restated as certification (Model Rule 7.2(c)); TSBPE consumer-page claim
re-attributed to 22 TAC 367.10(b); Texas roofing license status now names HB 3344 without claiming
it passed; schema limited to Pro/Agency on the plumber checklist; secondary or wrong-country sources
replaced with ABA, HHS, SAMHSA and Psychology Today US pages.

Open item for Maurice or a later checker: confirm HB 3344's final status on capitol.texas.gov bill
history. If it was enacted, the roofing page can say Texas now licenses reroofing contractors
through TDLR.
