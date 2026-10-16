# Fact-check fc-w2-c: Los Angeles, San Diego, Chicago, Cleveland (Wave 2, Oct 16 2026)

Checker: fc-w2-c (independent, did not write these pages). Writer notes: docs/writers/w2-c.md (LA, San Diego) and docs/writers/w2-e.md (Chicago, Cleveland).
About 40 WebSearch queries (WebFetch not used). Build: `python3 build.py --out /tmp/claude-0/fc-w2c/dist`; `check.py --skip-links --only` on each of the four URLs: 0 errors, 0 warnings. No em or en dashes in the four source files; no banned words.

## /web-design/los-angeles-ca.html
| Claim | Verdict | Source | Action |
|---|---|---|---|
| LA County has 88 incorporated cities | Confirmed | lacounty.gov guides; Wikipedia list | none |
| About 1 million people in unincorporated areas; Board of Supervisors acts as their city council | Confirmed | lacounty.gov Guide to Unincorporated Area Services ("more than 1 million residents"; Board is their "city council") | added that county PDF as a source |
| County population about 9.76 million (July 2024) | Corrected | census.gov QuickFacts: V2024 9,757,179, newer V2025 9,694,934 | updated to "about 9.69 million people in July 2025" |
| City of LA 3,898,747 in 2020 census | Confirmed | QuickFacts (April 1, 2020 count) | none |
| Hollywood and Venice are LA neighborhoods; West Hollywood, Beverly Hills, Santa Monica separate cities; Sherman Oaks, Studio City, Van Nuys in the city; Burbank, Glendale separate | Confirmed | Getty; Time Out; Wikipedia list | none |
| LAEDC CEO, Feb 2025: 94% of county companies have fewer than 20 employees | Confirmed | laedc.org and Business Wire release (Feb 13, 2025) | none |
| County 2020 policy: 42% of businesses have 5 or fewer employees, about 4% over 100 | Confirmed | LA County Policy on Doing Business with Small Business (Appendix F, 02/2020) | none |
| BTRC required of everyone doing business in the city, incl. outside businesses working in it 7+ days a year | Confirmed | finance.lacity.gov BTRC and FAQ pages | none |
| Small business exemption for gross receipts "under $100,000" with timely renewal | Corrected | finance.lacity.gov Small Business Exemption FAQ ($100,000 or less, total worldwide receipts, registered, timely renewal) | changed to "Registered owners whose total gross receipts are $100,000 or less"; added the FAQ as a source |
| Santa Monica issues its own business license | Confirmed | santamonica.gov | none |
| Burbank "sorts businesses into those needing a regulatory license and those needing only business tax registration" | Corrected | burbankca.gov Business Tax: all businesses doing business in Burbank must register; some industries also need a regulatory Business License | reworded to that; added Burbank business tax page as a source |
| Glendale: no business license or business tax; annual Business Registration Certificate for businesses with a physical location | Confirmed | Crescenta Valley Weekly; Glendale BMC 5.04.030 via city audit; glendaleca.gov BRC page | added the City of Glendale BRC page as the primary source |
| Google local results: relevance, distance, prominence | Confirmed | support.google.com/business/answer/7091 | none |
| EWDD BusinessSource Centers: free one-on-one consulting and business plan help | Confirmed | business.lacity.gov EWDD; ewdd.lacity.gov (count 9 or 10 deliberately not stated) | none |
| LA Regional SBDC hosted by Long Beach City College since 2006; LA, Santa Barbara, Ventura counties; no-cost consulting, low-cost training | Confirmed | lbcc.edu; smallbizla.org/about | none |
| SCORE LA: free mentoring "at more than 25 locations", "free and low-cost workshops" | Softened | the 25-location figure is from a 2017 SCORE LA release; current score.org/ca/los-angeles names Pasadena, Glendale, Santa Monica, Torrance and surrounding cities | now "Free one-on-one mentoring ... across the county, from Pasadena and Glendale to Santa Monica and Torrance, plus business workshops"; source changed to the chapter home page |
| LA Area Chamber "formed on October 10, 1888" | Softened | USC archives finding aid (founded 1888, no day); Oct 10, 1888 is the date of the founders' meeting per Wikipedia | now "Founded in 1888"; added USC/OAC finding aid source |
| Two-year math $497 + 24 x $49 = $1,673 | Confirmed | arithmetic from INTAKE.md | none |
| Packages, prices, chat widget 14 days then $297/mo, phone agent setup, free 7 days then $297/mo up to 750 minutes, separate from one-time price; hosting $49/mo or included with AI agent; 7 to 14 days; first wave inside two weeks | Confirmed | INTAKE.md section 3 | none |
| AI receptionist answers any hour and transfers to Maurice; no LA office; built from East Texas | Confirmed | INTAKE.md sections 1 and 5 | none |

Summary LA: 20 claims checked: 14 confirmed, 3 corrected (population year, exemption threshold, Burbank rule), 2 softened (SCORE locations, chamber date), 0 removed (1 source swapped to official for Glendale, counted under confirmed).

## /web-design/san-diego-ca.html
| Claim | Verdict | Source | Action |
|---|---|---|---|
| BIDs: business owners assessed each year to promote their district | Confirmed | sandiego.gov/economic-development/about/bids | none |
| 18 active districts, more than 11,000 small businesses | Confirmed (as the City states it) | City BID page ("eighteen (18) active BIDs", 11,000+ small businesses); 2024 City presentation also says 18. A 2026 City fact sheet mentions about 20 designated BIDs | kept, worded as the City's count |
| Treasurer collects BID assessments with the Business Tax Certificate | Confirmed | City audit 16-005 (2015); Council Policy | none |
| District map has included North Park, Hillcrest, Little Italy, Ocean Beach, Pacific Beach, City Heights | Confirmed | FY2018 BID map; City BID organizations directory | added bidorgs directory as a source |
| City names Adams Avenue Street Fair and Hillcrest CityFest "among events this funding has paid for" | Corrected | City BID page says BID associations "coordinate" these festivals (with Gaslamp Mardi Gras); it does not say assessments paid for them | now "among the large festivals they coordinate", Gaslamp's Mardi Gras added |
| City minimum wage $17.75 from Jan 1, 2026; state $16.90 | Confirmed (current 2026 figure) | sandiego.gov press release Dec 31, 2025; Constangy; state rate $16.90 | none |
| Business Tax Certificate for nearly every business incl. home-based, self-employed, independent contractors; due within 15 days | Confirmed | sandiego.gov btaxhow and btaxfaq | none |
| "One of the country's largest concentrations of Navy personnel" | Softened | SDMAC advocacy wording; not independently verified | replaced with "San Diego is a Navy and Marine Corps town." |
| SDMAC: more than 115,000 active duty | Confirmed | sdmac.org/military-in-san-diego (115,165; homepage gives 136,350, so "more than 115,000" holds) | labeled SDMAC as a regional advocacy group |
| Split about evenly Navy/Marine Corps | Confirmed (as SDMAC states it) | sdmac.org text "roughly split" | worded "roughly split" |
| About one-third of the Marine Corps active-duty force | Removed | SDMAC's own materials conflict (one-third, over one-fourth, 1 in 4) | sentence deleted |
| 72,793 veterans in the city (2019 to 2023) | Confirmed | census.gov QuickFacts San Diego city | added the survey years in text |
| Naval Base San Diego and Miramar exist near the city | Confirmed | sdmac.org | none |
| Google local ranking factors | Confirmed | support.google.com/business/answer/7091 | none |
| SBDC network: "Four regional centers, including one hosted by Southwestern College in National City and another at the University of San Diego" | Corrected | sdivsbdc.org; swccd.edu: Southwestern College hosts the lead center (prime grant holder); South San Diego SBDC at 880 National City Blvd; North San Diego SBDC; The Brink at USD; sources disagree on the number of centers | rewritten without a count; added sdivsbdc.org About, South San Diego SBDC and swccd.edu sources; removed the two third-party East County sources |
| SCORE San Diego: free mentoring, San Diego, Chula Vista, Carlsbad, Escondido; low-cost workshops "on planning, financing and marketing" | Corrected (minor) | score.org/ca/san-diego and its workshop list (starting a business, business plan, financing) | workshop topics now match the chapter's list |
| Packages, prices, trials, hosting, Pro 10 city pages, Agency 30 to 60 pages in waves | Confirmed | INTAKE.md section 3 | none |
| No San Diego office; Big Sandy; AI receptionist wording | Confirmed | INTAKE.md | none |
| Kearny Mesa chiropractor page plan | Not a factual claim | explicit hypothetical | none |

Summary San Diego: 19 claims checked: 12 confirmed, 4 corrected (BID events wording, SBDC list, SCORE workshop topics, plus veterans wording clarified counted as confirmed), 1 softened (Navy concentration), 1 removed (one-third of Marine Corps), 1 not a claim.

## /web-design/chicago-il.html
| Claim | Verdict | Source | Action |
|---|---|---|---|
| 77 community areas, drawn in the 1920s by University of Chicago researchers to compare census data; only two changes (O'Hare added, Edgewater split from Uptown); no official neighborhoods | Confirmed | Wikipedia; IECAM; WTTW 2022 citing Encyclopedia of Chicago | none |
| Population roughly 2.7 million | Confirmed | Census 2024 estimates via NBC Chicago, Illinois Policy (2.72 million) | none |
| SSAs: local property tax districts for services beyond city services; DPD contracts nonprofits (usually chambers or business associations) | Confirmed | chicago.gov SSA program page; SSA Program Guide | none |
| SSA commission "appointed by the mayor" | Corrected | SSA Program Guide: commissioners nominated by the Mayor and approved by City Council | now "nominated by the mayor and approved by the City Council"; added Program Guide source |
| "The city lists 55 active SSAs" | Corrected | chicago.gov SSA page currently says 58 active SSAs | changed to 58 |
| SSA services: cleaning, planters, safety, facades, events, marketing | Confirmed | chicago.gov SSA page | none |
| 26th Street: 2 miles Western to Pulaski; second-highest-grossing district after the Mag Mile; about $900 million in 2015 (Bisnow) | Confirmed | Bisnow; WTTW 2015 (Crain's) | none (stated as 2015 and "long described") |
| Little Village Chamber is an NBDC, Spanish and English | Confirmed | littlevillagechamber.org; chicago.gov NBDC flyer | none |
| Devon: first sari shop opened in 1972 | Softened | ABC7 says first Indian store (India Sari Palace) 1972; Chicago History Museum says 1973 | now "the first Indian shops opened" in the early 1970s |
| Patel Brothers 1974; runs through West Ridge toward Rogers Park | Confirmed | ABC7; WBEZ; Wikipedia Devon Avenue | none |
| Milwaukee Avenue diagonal, through Wicker Park, Logan Square, Avondale; Diversey to Addison called the Polish Village | Confirmed | Wikipedia Milwaukee Ave and Avondale; DNAinfo 2013; Encyclopedia of Chicago | none |
| Andersonville Chamber supports 400+ local and independent businesses near and along Clark | Confirmed | Chamber podcast description (also 430+ members on andersonville.org) | none |
| Chinatown (Wentworth and Cermak) 400+ businesses per WTTW | Confirmed | wttw.com/southside/near-southwest/chinatown | none |
| NBDCs: BACP-funded, no-cost, hyper-local help with licensing and public way permits | Confirmed | chicago.gov NBDC flyer and program page | none |
| BACP Small Business Center at City Hall, 121 N. LaSalle | Confirmed | chicago.gov 2026 fee notice; business licensing pages (room 800 vs 805 differs, not stated) | added 2026 fee notice source; text now also says to check whether to book an appointment |
| Illinois SBDC hosts: Chicagoland Chamber, Polsky Exchange on 53rd Street, Chinese Mutual Aid Association on Argyle (multilingual) | Confirmed | chicagolandchamber.org SBDC page; polsky.uchicago.edu; CMAA flyer (1016 W Argyle) | source for Chicagoland Chamber changed to its current SBDC page |
| Google local ranking factors | Confirmed | support.google.com/business/answer/7091 | none |
| Prices, trials, no Chicago office, built remotely | Confirmed | INTAKE.md | none |
| Agency comparison table (agencies quote by proposal, retainers) | Not a specific factual claim | general description, no numbers | none |

Summary Chicago: 19 claims checked: 15 confirmed, 2 corrected (SSA count, commission appointment), 1 softened (Devon 1972 sari shop), 0 removed, 1 not a specific claim.

## /web-design/cleveland-oh.html
| Claim | Verdict | Source | Action |
|---|---|---|---|
| About 365,000 residents, 2024 Census estimate (365,379) | Confirmed | Spectrum News May 28, 2025 (Census estimate) | none |
| ACS 2012 to 2016: 53.6% of 211,387 housing units built 1939 or earlier | Confirmed | CSU Levin College NEOMDR profile (113,229 of 211,387) | none (dated survey named in text) |
| 2011 AHS: Cleveland area median occupied home built 1959 vs 1974 nationally | Confirmed | census.gov CB13-R.42 (July 11, 2013) is the Cleveland AHS release; HUD archive copy states 1959 vs 1974; HUD Cleveland factsheet 2011 | added HUD archive copy as a second source (the census.gov copy has a metro-name typo) |
| Cleveland Clinic passed Walmart as Ohio's largest private employer, 50,825 vs 49,330 | Corrected | those counts are from an older AP/WKYC report of unstated year; Walmart regained the top spot in 2017; the December 2022 Ohio Major Employers Report has Cleveland Clinic first at 56,986 vs Walmart 55,262 | now cites the December 2022 report and its figures; WKYC source replaced with the ohio.gov report |
| Lead Safe: rentals built before 1978; clearance exam or lead risk assessment by private state-approved professionals; renew every 2 years via Building and Housing; owner-occupied exempt; enforcement from March 31, 2021, phased by ZIP, all due March 31, 2023 | Confirmed | clevelandohio.gov Lead Safe pages and 2024 guidance; Cleveland City Council | none |
| West Side Market at W. 25th and Lorain, hall opened 1912 | Confirmed | westsidemarket.org; clevelandhistorical.org | none |
| West Side Market "now holds more than 100 vendors" | Corrected | westsidemarket.org About says over 70 vendors (1912 hall had 100 indoor stalls) | now "today houses more than 70 vendors" |
| Ohio City grew up around the market; Tremont across the bridge from downtown; Gordon Square Arts District in Detroit Shoreway | Confirmed | Redfin; Cleveland Historical; Wikipedia | none |
| Slavic Village "sometimes called the South Side" | Softened | not found in search; Encyclopedia of Cleveland History places it on the southeast side | now "sits on the southeast side" |
| North Collinwood includes Waterloo | Confirmed | Wikipedia Neighborhoods in Cleveland | none |
| COSE: small business arm of the Greater Cleveland Partnership; networking, education, advocacy, group purchasing | Confirmed | cose.org/aboutcose | added cose.org source |
| SCORE Cleveland SBA-affiliated; COSE members get free mentoring and workshops through the partnership | Confirmed | score.org/oh/cleveland/cose-score-cleveland-partnership | none |
| SBDCs hosted by Cleveland State, Urban League, Hispanic Business Center, Lakeland CC | Softened | CSU SBDC confirmed on business.csuohio.edu; the other three appear only on 2016/2017 state maps | now "the SBDC at Cleveland State University's business college and its regional partner sites"; added CSU source |
| Lakewood, Parma, Euclid, Shaker Heights are suburbs | Confirmed | general knowledge | none |
| Google local ranking factors | Confirmed | support.google.com/business/answer/7091 | none |
| Prices, trials, schema and GBP on Pro, no Cleveland office, AI receptionist | Confirmed | INTAKE.md | none |
| Wording avoids "certified" for the city's Lead Safe Certification | Confirmed | WRITING-GUIDE banned words | none |

Summary Cleveland: 17 claims checked: 12 confirmed, 2 corrected (Ohio employer figures, West Side Market vendor count), 3 softened (Slavic Village label, SBDC host list, and the employer claim now dated), 0 removed.

## Totals
75 claims checked across 4 pages: 53 confirmed, 11 corrected, 7 softened, 1 removed, 3 not specific factual claims.
