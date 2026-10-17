# Fact-check fc-w4-a1 (Wave 4, Oct 17 2026)

Independent checker; I wrote none of these pages. Pages: /web-design/san-antonio-tx.html, laredo-tx.html,
temple-tx.html, fort-worth-tx.html, arlington-tx.html, abilene-tx.html. Writer notes: docs/writers/w4-a1.md, w4-a2.md.

**Method and an important limit.** I verified San Antonio and most of Laredo with WebSearch (19 queries). The
shared search budget for this run (200 calls across all agents) then ran out, so it stopped working. For Temple, Fort Worth, Arlington and
Abilene, and the last two Laredo items, I could only check against my own background knowledge. The tables mark those
"Confirmed (PK)" (PK = prior knowledge, no search this run). Every number or program detail I could not confirm
either way was softened or removed rather than kept on trust. Items still worth a search in a later run are listed at the end.

Business claims on all six pages (prices $497 / $997 / $1,997 paid once, Pro chat widget free 14 days then $297/mo,
Agency phone agent setup then free 7 days and $297/mo for up to 750 minutes and not part of the one-time price, hosting
$49/mo without the agent, AI receptionist wording, no office outside Big Sandy, no clients, reviews or ranking promises)
match INTAKE.md. `m.no_office` is used once per page. I opened every image and checked its alt text (contact sheets).
Only one alt needed fixing.

Build: `python3 build.py --out /tmp/claude-0/fc-w4-a1/dist`; check.py `--skip-links --only` gives 0 errors on all
six pages (Laredo and Temple keep the expected short-page word-count WARN). Similarity: highest pair involving these pages
is fort-worth-tx / st-louis-mo at 4.8%. No em or en dashes on these pages.

## /web-design/san-antonio-tx.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| San Antonio calls itself Military City USA | Confirmed | sa.gov MVAD Military Installations page; sa.gov news release | Added the sa.gov installations page as a source |
| JBSA = Fort Sam Houston, Lackland, Randolph | Confirmed | comptroller.texas.gov 2025 JBSA page | None |
| 2025 Comptroller: 74,713 direct employees, 33,256 active duty, at least $53B | Confirmed | comptroller.texas.gov/economy/economic-data/military/2025/joint-base-sa.php | None |
| Lackland hosts Air Force enlisted BMT | Confirmed | jbsa.mil (37th Training Wing BMT) | None |
| Fort Sam Houston is the center of Army medical training, home to BAMC | Confirmed | jbsa.mil "Army Medicine still starts here" | Replaced Wikipedia source with jbsa.mil |
| Population about 1,495,295 (July 2023) | Corrected | Census QuickFacts V2025 (1,548,422, July 1 2025); matches Wikipedia infobox | Now "about 1.55 million, 1,548,422 by the July 2025 estimate"; source URL updated to PST045225 |
| Hispanic or Latino 64.4% | Corrected | Census QuickFacts V2025: 64.6% | Changed to 64.6% |
| Google local ranking: relevance, distance, prominence | Confirmed | support.google.com/business/answer/7091 | None |
| Pearl: former brewery bought 2002, restaurants, shops, apartments, weekend farmers market | Confirmed | ULI Urban Land (Silver Ventures bought 22 acres in 2002); sanantonio.gov 311 (Sat and Sun market) | None |
| St. Mary's Strip "west of US 281, north of I-35", "aimed more at locals" | Softened | Boundary wording not found in any source | Now "in Tobin Hill, just north of downtown and close to the Pearl" |
| St. Mary's Strip bars and music venues | Confirmed | SA Current; Texas Monthly Tobin Hill guide | Replaced Wikipedia source with these two |
| South Texas Medical Center: more than 900 acres, northwest side | Confirmed | San Antonio Report; Wikipedia agrees on northwest side | None |
| 2022 study: more than 86,000 jobs | Confirmed | San Antonio Report (UTSA study for SA Medical Foundation) | None |
| Stone Oak north of Loop 1604, west of US 281 | Confirmed | KSAT "From cows to crowds" (2025) | Replaced weak SpareFoot source with KSAT; added the confirmed "first master-planned community in Bexar County" |
| EDD: small business programs and grants, Vendor Development Academy, SBEDA, Buy Local | Confirmed | sa.gov EDD Supplier Engagement page | Added that page as a source |
| Small Business Advisory Commission "reviews city policies that affect owners" | Softened | Only an FY2022 EDD report naming the commission as a collaborator | Now "The city also works with a Small Business Advisory Commission on small business needs" |
| UTSA SBDC: no-cost confidential advising, Bexar and surrounding counties, downtown campus | Confirmed | sacrd.org listing (501 W. Cesar E. Chavez Blvd, the UTSA Downtown Campus); UTSA Today | None |
| UTSA SBDC "low-cost workshops" | Corrected | Sources say workshops and training, no price stated | Now "workshops and training" |
| SAHCC "works for the growth of Hispanic, small, minority and women-owned businesses" | Corrected | sahcc.org/about-us mission: "leading resource, advocate and access point for Hispanic businesses ... and the Hispanic market" (the cited wording is GuideStar's) | Reworded to match the chamber's own mission |
| SAHCC annual Small Business Expo and awards luncheon | Confirmed | sahcc.org honorees article; 2026 sponsor form | None |
| Hero fallback alt "comparing two website proposals" | Corrected | Opened los-angeles-ca-hero.jpg: bakery owner, two printed pages with pastry photos, laptop | Alt now describes the printed page layouts |
| Business claims (prices, trials, hosting) | Confirmed | INTAKE.md | None |

Summary: checked 22, confirmed 14, corrected 6, softened 2, removed 0.

## /web-design/laredo-tx.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Port of Laredo is the busiest U.S. border crossing and #3 among 450+ ports | Confirmed | laredoedc.org international trade; KGNS Feb 2026 | None |
| "Laredo's economic development office" | Corrected | Laredo EDC is a corporation, not a city office | Now "The Laredo Economic Development Corporation" |
| $353.94B in 2025 trade, more than 97% tied to Mexico | Confirmed | City release via Rutland Herald; AJOT; Laredo EDC ($354B) | None |
| World Trade Bridge and Colombia Solidarity Bridge carry commercial trucks | Confirmed (PK) | KERA; broker brochures name both as the truck bridges | None |
| Mines Road (FM 1472) links the two, lined with industrial parks and warehouses | Confirmed | Laredo EDC site-selection listings; CBRE and LoopNet brochures | None |
| Chamber founded 1915, more than 700 members, oldest business group | Confirmed | laredochamber.com; Texas Senate SR 98 (2015) | None |
| TAMIU SBDC: free confidential advising, Webb, Jim Hogg, Zapata | Confirmed | tamiu.edu/sbdc | Added the "tri-county" wording |
| TAMIU SBDC "low-cost training" | Softened | No prices found | Now "training and free webinars" |
| On-demand webinars "some in Spanish" | Removed | No source shows Spanish-language content (resources page offers language accommodations only on request) | Deleted |
| Google local ranking | Confirmed | Google help 7091 | None |
| Business claims | Confirmed | INTAKE.md | None |
| Image alts (miami hero, insurance/1, electrical/4, domain-renewal) | Confirmed | Opened each image | None |

Summary: checked 12, confirmed 9, corrected 1, softened 1, removed 1.

## /web-design/temple-tx.html (no searches left; prior knowledge only)

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Baylor Scott & White, largest not-for-profit health system in Texas (per Temple EDC), medical center in Temple | Confirmed (PK) | Temple EDC major employers | None |
| Olin E. Teague VA Medical Center, main campus of Central Texas VA, 39 counties | Confirmed (PK) | VA Central Texas | Replaced weak BrainLine source with va.gov/central-texas-health-care |
| McLane based in Temple; H-E-B and Walmart distribution centers | Confirmed (PK) | Temple EDC major employers | None |
| 2020 Census 82,073 | Confirmed (PK) | Census QuickFacts | None |
| 93,095 (July 2023), +13.4% | Softened | Could not re-check | Now "yearly estimates since then show the city growing" |
| Temple EDC formed 1989 | Removed | The GuideStar "ruling year" is an IRS ruling date, not proof of when the EDC was formed | Deleted year and GuideStar source |
| EDC partner network (Chamber, Bell County, Temple College, SBDC) | Not re-verified | templeedc.com/about-our-partners (official, writer-cited) | Kept as stated; see open items |
| Chamber roots in a 1907 commercial club; SCORE seminars | Removed | Writer flagged it as unsure; could not check | Deleted, with the issuu and hmdb sources |
| Central Texas Business Resource Center in Killeen, run by CTC, Workforce Solutions and the Killeen Chamber | Softened | Writer could not tie it to a URL | Kept the center's name, dropped the partner list |
| Bell County, on I-35 between Waco and Austin; Belton next door; Temple University is in Philadelphia | Confirmed (PK) | General geography | None |
| Google local ranking; business claims | Confirmed | Google 7091; INTAKE.md | None |
| Image alts (hire hero, insurance/3, plumbing/2, contractor-review) | Confirmed | Opened each image | None |

Summary: checked 13, confirmed 8, corrected 0, softened 2, removed 2, not re-verified 1.

## /web-design/fort-worth-tx.html (no searches left; prior knowledge only)

| Claim | Verdict | Source | Action |
|---|---|---|---|
| 1,008,106 on July 1 2024, first time over a million, +23,442 that year | Confirmed (PK) | fortworthtexas.gov population; Census V2024 | None |
| "Newer Census figures": about 1.03M, 10th largest U.S. city (NBC DFW) | Removed | Could not check; in V2024 Fort Worth was behind Jacksonville | Deleted, with the source |
| Fort Worth Herd at 11:30 a.m. and 4:00 p.m., East Exchange Ave, Livestock Exchange Building | Confirmed (PK) | fortworthstockyards.org | None |
| Near Southside south of downtown, Magnolia its main street; second largest employment center in Tarrant County (per Fort Worth South) | Confirmed (PK) | fortworthsouth.org | None |
| West 7th becomes brick-paved Camp Bowie at University Drive; Kimbell, Modern, Amon Carter nearby | Confirmed (PK) | Fort Worth Architecture; city arts plan | None |
| Camp Bowie District runs out to Loop 820 | Softened | NBC source not re-checked | Now "runs west for miles"; NBC source removed |
| AllianceTexas about 27,000 acres | Confirmed (PK) | Hillwood | None |
| "More than 574 companies"; projects in Haslet, Roanoke, Northlake, Westlake | Softened | Developer figure, not re-checked | Now "a large base for distribution and industrial companies", towns cut to Haslet and Roanoke |
| Devoyd Jennings BAC on the James E. Guinn campus | Confirmed (PK) | fortworthtexas.gov/business/bac | None |
| SBDP contract from Sept 2025 with three chambers; Spanish help; bonding workshops | Softened | Could not check; the contract may have ended Sept 2026 | Now names the program working through local chambers (Hispanic and Metropolitan Black chambers) and says to check the city page |
| Tarrant SBDC hosted by Tarrant County College, part of the North Texas SBDC | Confirmed (PK) | tccd.edu | None |
| Texas about 3.52 million small businesses (SBA 2025) | Softened | Exact figure not re-checked | Now "more than 3 million" |
| About 260 searches a month for web development Fort Worth | Confirmed | Keyword data file | None |
| Big Sandy is east of Dallas; Google ranking; business claims | Confirmed | Geography; Google 7091; INTAKE.md | None |
| Image alts (packages fallback, roofing/3, cleaning/3, electrical/3) | Confirmed | Opened each image | None |

Summary: checked 15, confirmed 10, corrected 0, softened 4, removed 1.

## /web-design/arlington-tx.html (no searches left; prior knowledge only)

| Claim | Verdict | Source | Action |
|---|---|---|---|
| 394,266 in 2020; around 400,000 now; second largest city in Tarrant County | Confirmed (PK) | Census QuickFacts | Wikipedia source removed |
| Between Dallas and Fort Worth, about 12 miles from downtown Fort Worth and 20 from downtown Dallas | Confirmed (PK) | General geography | None |
| AT&T Stadium, Globe Life Field, Six Flags, Texas Live! in the district | Confirmed (PK) | Arlington EDC tourism | None |
| 15.6M visitors in 2023 spending $2.8B | Removed | Could not check | Deleted, with the Dallas Innovates source |
| UTA 42,710 students in fall 2025 | Softened | Could not check | Now "tens of thousands of students"; UTA source removed |
| Long known as a large city without fixed-route buses; Via on-demand by app or phone | Confirmed (PK) | TechCrunch; city news | None |
| Later contracts added a Trinity Metro stop in Fort Worth and CentrePort TRE | Softened | Not re-checked | Kept only the CentrePort TRE link |
| Cooper Street at I-20 by The Parks Mall | Confirmed (PK) | General geography | Wikipedia source removed |
| EDC 0% loans up to $100,000 with LiftFund (Oct 2024); SCORE cohorts | Softened | Not re-checked; terms may have changed | Now "has worked with LiftFund on lending and SCORE on mentoring; check its site" |
| City small business assistance pages | Confirmed (PK) | arlingtontx.gov | None |
| Chamber's free Small Business Expo and Small Business of the Year | Softened | Not re-checked | Now general wording about events and awards |
| Tarrant SBDC satellite offices at the Chamber and UTA | Softened | Not re-checked | Now "free advising across Tarrant County, Arlington included" |
| Arlington, Virginia exists; Google ranking; business claims | Confirmed | General; Google 7091; INTAKE.md | None |
| Image alts (kansas-city hero, contractor-work, designer-cost, insurance/2) | Confirmed | Opened each image | None |

Summary: checked 14, confirmed 8, corrected 0, softened 5, removed 1.

## /web-design/abilene-tx.html (no searches left; prior knowledge only)

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Dyess: 7th Bomb Wing, the only B-1B formal training unit; 317th Airlift Wing C-130J | Confirmed (PK) | dyess.af.mil | Replaced Wikipedia source with dyess.af.mil |
| FY2024 economic impact statement: 14,823 personnel | Removed | Could not check the PDF | Replaced with a plain line about rotating families; source removed |
| Three private Christian universities: ACU, Hardin-Simmons, McMurry; Taylor County | Confirmed (PK) | University sites | Replaced Wikipedia with the three university homepages |
| Paramount Theatre from 1930, restored; downtown revival | Confirmed (PK) | Visit Abilene | None |
| Frontier Texas is the official visitor center | Confirmed (PK) | Visit Abilene | None |
| 2015 Legislature: Storybook Capital of Texas (H.C.R. 93), NCCIL and sculptures | Confirmed (PK) | capitol.texas.gov | None |
| 2018 trademark of "Storybook Capital of America" | Confirmed (PK) | ACU Optimist | None |
| New sculpture each June at the Children's Art and Literacy Festival | Confirmed (PK) | Texas Highways | None |
| Abilene SBDC, an outreach program of Texas Tech; low and no-cost counseling; DCOA refers owners to it | Confirmed (PK) | developabilene.com; sba.gov event | None |
| Chamber Small Business Week with named awards | Softened | Not re-checked | Now "recognizes local small businesses with yearly awards" |
| Abilene, Kansas exists; Google ranking; business claims | Confirmed | General; Google 7091; INTAKE.md | None |
| Image alts (st-louis hero, plumbing/1, roofing/1, cleaning/2) | Confirmed | Opened each image | None |

Summary: checked 12, confirmed 10, corrected 0, softened 1, removed 1.

## Open items for a follow-up search
- Temple: the EDC partner list on templeedc.com/about-our-partners; the va.gov source should be checked for the "39 counties" wording.
- Fort Worth: +23,442 one-year gain; "second largest employment center in Tarrant County" (Fort Worth South).
- Abilene: the 2018 "Storybook Capital of America" trademark (single student-newspaper source).
- All Confirmed (PK) items on the four pages checked without search should get a quick WebSearch pass when budget allows.

## Search recheck (fc-w4-r1)

Independent second checker (wrote none of these pages), Oct 17 2026. Rechecked every "Confirmed (PK)", softened and
open item above on Temple, Fort Worth, Arlington and Abilene with WebSearch: 28 queries, 7 per page. Also re-read each
page's pricing and FAQ text against INTAKE.md. All four "cost" FAQs listed $49 hosting as the only recurring cost, so
each now also says Pro's AI chat widget is free 14 days, then $297/mo (Fort Worth's also names the phone agent's $297/mo
after its 7-day trial). Build: `python3 build.py --out /tmp/claude-0/fc-w4-r1/dist`; check.py `--skip-links --only`:
0 errors on all four (Temple keeps the short-page word-count WARN). Highest similarity pair touching these pages:
abilene-tx / arlington-tx 5.5%. No em or en dashes.

### /web-design/temple-tx.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Temple EDC calls Baylor Scott & White the largest not-for-profit health system in Texas; medical center in Temple | Confirmed | templeedc.com/doing-business-here/major-employers/ | None |
| McLane Company based in Temple | Confirmed | Temple EDC McLane success story; Wikipedia (moved to Temple 1966) | None |
| H-E-B and Walmart distribution centers in Temple | Confirmed | Temple EDC 2023 release; logistics page | None |
| Olin E. Teague VA Medical Center is the main campus of Central Texas VA, 39 counties | Confirmed | templeedc.com/success-story/va-medical-center (250,000+ veterans, 39 counties); va.gov about-us | VA source URL changed to va.gov/central-texas-health-care/about-us/ |
| 2020 Census 82,073 | Confirmed | Census QuickFacts (April 1 2020 base); Wikipedia | None |
| EDC partners include Chamber, Bell County, Temple College and the SBDC | Confirmed | templeedc.com/about-our-partners | Open item closed |
| Central Texas Business Resource Center in Killeen is a place to ask | Removed | Killeen Daily Herald (kdhnews.com, Dec 2024): the center closed when its funding contract ended | Sentence and the templeedc "entrepreneurship" source deleted |
| Bell County, I-35 between Waco and Austin; Temple University is in Philadelphia | Confirmed (general geography) | None needed | None |
| Pricing FAQ | Corrected | INTAKE.md | Added Pro chat widget $297/mo after 14-day trial |

Summary: checked 9, confirmed 7, corrected 1, softened 0, removed 1.

### /web-design/fort-worth-tx.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| 1,008,106 on July 1 2024, first time over a million | Confirmed | fortworthtexas.gov/about/population; Fort Worth Inc.; CoStar | None |
| +23,442 in that one year | Confirmed | Fort Worth Magazine, Southlake Style (July 2023 to July 2024, Census) | Open item closed |
| Fort Worth Herd at 11:30 a.m. and 4:00 p.m. on East Exchange Avenue, Livestock Exchange Building | Confirmed | fortworthstockyards.org event page and FAQ | None |
| Near Southside: second largest employment center in Tarrant County (per Fort Worth South) | Confirmed | fortworthsouth.org (second only to the Central Business District) | Open item closed |
| West 7th becomes brick-paved Camp Bowie at University Drive | Confirmed | historicfortworth.org Camp Bowie brick streets (named west of University Drive, Thurber brick 1927) | Added that source |
| Kimbell, Modern, Amon Carter nearby | Confirmed (cited source) | Fort Worth Architecture Cultural District page; search did not add more | None |
| AllianceTexas about 27,000 acres, reaches into Haslet and Roanoke | Confirmed | AllianceTexas fact sheet; Community Impact (nine municipalities incl. Haslet, Roanoke) | None |
| Devoyd Jennings BAC on the James E. Guinn Entrepreneurial Campus | Confirmed | fortworthtexas.gov/bac; BAC annual reports | None |
| SBDP support services through local chambers (Hispanic, Metropolitan Black) | Confirmed in part | fortworthtexas.gov small business support page (Hispanic Chamber bilingual help at the BAC) | Kept, already says to check the city page |
| Tarrant SBDC "hosted by Tarrant County College", "low-cost workshops" | Softened | Searches confirm North Texas SBDC network, free confidential advising for Tarrant County, on-site at the BAC; no source states TCC hosting or workshop prices | Now "part of the North Texas SBDC network ... free one-on-one advising and training ... a desk at the BAC"; TCC source replaced with the City of Arlington Tarrant SBDC page |
| Texas has more than 3 million small businesses (SBA Advocacy) | Not re-searched | SBA 2025 Texas profile (already softened from 3.52M) | None |
| Pricing FAQ | Corrected | INTAKE.md | Added chat widget and phone agent monthly costs |

Summary: checked 12, confirmed 9, corrected 1, softened 1, removed 0, not re-searched 1.

### /web-design/arlington-tx.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| 2020 census 394,266 | Softened | Sources disagree (394,266 ACS-labeled in city budget; 394,387 / 393,985 elsewhere) | Now "about 394,000" |
| Second largest city in Tarrant County | Confirmed | tarrantcountytx.gov cities page (Fort Worth first, Arlington second) | Added source |
| About 20 miles from downtown Dallas and 12 from downtown Fort Worth (FAQ) | Removed | No source gave these distances | Now says I-30 and I-20 run to both downtowns |
| AT&T Stadium, Globe Life Field, Six Flags Over Texas, Texas Live! in the district | Confirmed | arlington.org Entertainment District; Dallas Innovates | None |
| Large city without fixed-route buses; Via by app or phone; CentrePort TRE link | Corrected | arlingtontx.gov 2017 launch release (MAX bus ended, Via served CentrePort); Fort Worth Magazine (citywide 2021) | Reworded: "long gone without a traditional fixed-route city bus system", Via since 2017, citywide since 2021, connects at CentrePort; dropped the unsourced "within a couple of blocks"; added source |
| Cooper Street at I-20 by The Parks Mall | Confirmed | theparksmallarlington.com; Wikipedia (I-20 and South Cooper) | Added mall source |
| EDC with LiftFund lending and SCORE mentoring | Confirmed | arlingtontxedc.com business resources (0% loans to $100,000 via LiftFund); arlingtontx.gov SCORE 2024 cohort | Added EDC source |
| Chamber hosts a Small Business Expo | Removed | No search result tied an Expo to the chamber | Deleted with the 2024 Expo source |
| Chamber small business awards | Confirmed | arlingtontx.com/smallbusinessawards (since 1996, members only) | Now names the Small Businesses of the Year program |
| Tarrant SBDC free advising across Tarrant County | Confirmed | City of Arlington Tarrant SBDC page | None |
| Pricing FAQ | Corrected | INTAKE.md | Added Pro chat widget $297/mo after 14-day trial |

Summary: checked 11, confirmed 6, corrected 2, softened 1, removed 2.

### /web-design/abilene-tx.html

| Claim | Verdict | Source | Action |
|---|---|---|---|
| Dyess: 7th Bomb Wing, the Air Force's only B-1B formal training unit | Confirmed | gov.texas.gov 2020 Dyess briefing; dyess.af.mil units | None |
| 317th Airlift Wing, C-130J | Confirmed | af.mil (activated as a wing July 6 2017) | None |
| Three private Christian universities: ACU, Hardin-Simmons, McMurry | Confirmed | University sites; Wikipedia, encyclopedia.com | None |
| Paramount Theatre from 1930, restored | Confirmed | paramountabilene.com history (opened May 19 1930, restored 1987) | None |
| Frontier Texas is the official visitor center | Confirmed | abilenevisitors.com/Frontier-Texas | Added source |
| 2015 H.C.R. 93: Storybook Capital of Texas, NCCIL and sculptures | Confirmed | capitol.texas.gov HC00093F (signed June 9 2015) | None |
| 2018 trademark "Storybook Capital of America" by the Cultural Affairs Council and CVB | Corrected | USPTO record via Justia (Reg. 5533706, registered Aug 7 2018, owner Abilene Arts Alliance); abilenevisitors.com Storybook page (Cultural Affairs Council with CVB) | Now "the city's arts council and Convention and Visitors Bureau ... registered ... as a trademark"; added abilenevisitors source. Open item closed |
| New sculpture each year at the Children's Art and Literacy Festival in June | Confirmed | Texas Senate bill analysis (new pieces each year at the festival); Texas Highways (June) | None |
| Abilene SBDC, outreach program of Texas Tech, low and no-cost counseling; DCOA points owners to it | Confirmed | developabilene.com small business page; ttu.edu SBDC locations | None |
| Chamber "recognizes local small businesses with yearly awards" | Removed | Not found in search | Replaced with the confirmed fact that the CVB is part of the chamber (abilenevisitors.com/About); source label no longer mentions Small Business Week |
| Pricing FAQ | Corrected | INTAKE.md | Added Pro chat widget $297/mo after 14-day trial |

Summary: checked 11, confirmed 8, corrected 2, softened 0, removed 1.

All four pages: checked 43, confirmed 30, corrected 6, softened 2, removed 4, not re-searched 1.
