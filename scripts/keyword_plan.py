#!/usr/bin/env python3
"""Assign every keyword in keywords/Web-Design-Keywords.xlsx (ALL tab, 1,501 rows, Ubersuggest US,
Oct 12 2026) to a page as its target or a supporting keyword, or to the deliberately-unused list with
a one-line reason. Writes docs/keyword-plan.md.

Maurice's 10+ rule: every keyword with 10 or more searches a month must be assigned to a page or be
listed as unused with a reason. The script exits 1 if any 10+ keyword is left unclassified, or if a
page target does not exist in the data.

Usage: python3 scripts/keyword_plan.py
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent

PAGES = {
    "home": "/", "services": "/services/", "pricing": "/pricing/", "how": "/how-it-works/", "about": "/about.html",
    "contact": "/contact/", "faq": "/faq/", "areas": "/service-areas.html", "cities": "/web-design/",
    "citypages": "/how-city-pages-work.html",
    "smb": "/small-business-website/", "contractor": "/contractor-website-design/", "seo": "/seo-web-design/",
    "redesign": "/small-business-website-redesign/", "affordable": "/affordable-website-design/",
    "plumbers": "/web-design-for-plumbers/", "roofing": "/roofing-contractor-website-design/",
    "law": "/web-design-for-law-firms/", "therapists": "/web-design-for-therapists/",
    "g-cost": "/small-business-website-cost.html", "g-designer": "/how-much-does-a-website-designer-cost/",
    "g-monthly": "/website-cost-per-month/", "g-packages": "/web-design-packages-explained/",
    "g-builder": "/website-builder-vs-web-designer/", "g-hire": "/how-to-hire-a-web-designer/",
    "g-need": "/why-small-businesses-need-a-website/",
    "houston": "/web-design/houston-tx.html", "dallas": "/web-design/dallas-tx.html", "austin": "/web-design/austin-tx.html",
    "tyler": "/web-design/tyler-tx.html", "longview": "/web-design/longview-tx.html", "east-texas": "/web-design/east-texas.html",
    "waco": "/web-design/waco-tx.html", "el-paso": "/web-design/el-paso-tx.html", "kingwood": "/web-design/kingwood-tx.html",
    "atlanta": "/web-design/atlanta-ga.html",
    # Wave 2 national city pages (Oct 16 2026): main targets come from the national keyword file
    # (scripts/keyword_plan_wave2.py); city phrases in this file are supporting keywords.
    "st-louis": "/web-design/st-louis-mo.html", "kansas-city": "/web-design/kansas-city-mo.html",
    "chicago": "/web-design/chicago-il.html", "indianapolis": "/web-design/indianapolis-in.html",
    "cleveland": "/web-design/cleveland-oh.html", "nashville": "/web-design/nashville-tn.html",
    "miami": "/web-design/miami-fl.html", "orlando": "/web-design/orlando-fl.html", "phoenix": "/web-design/phoenix-az.html",
    "las-vegas": "/web-design/las-vegas-nv.html", "los-angeles": "/web-design/los-angeles-ca.html",
    "san-diego": "/web-design/san-diego-ca.html", "sacramento": "/web-design/sacramento-ca.html",
    # Wave 3 national city pages (Oct 17 2026, scripts/keyword_plan_wave3.py)
    "new-york": "/web-design/new-york-ny.html", "orange-county": "/web-design/orange-county-ca.html",
    "tampa": "/web-design/tampa-fl.html", "huntsville": "/web-design/huntsville-al.html",
    "tucson": "/web-design/tucson-az.html", "richmond": "/web-design/richmond-va.html",
    "louisville": "/web-design/louisville-ky.html", "wilmington": "/web-design/wilmington-nc.html",
    # Wave 4 city pages (Oct 17 2026, scripts/keyword_plan_wave4.py): only the cities with phrases in this file
    "denver": "/web-design/denver-co.html", "boise": "/web-design/boise-id.html", "okc": "/web-design/oklahoma-city-ok.html",
    "columbus": "/web-design/columbus-oh.html", "jacksonville": "/web-design/jacksonville-fl.html",
    "fort-lauderdale": "/web-design/fort-lauderdale-fl.html", "long-beach": "/web-design/long-beach-ca.html",
    "salt-lake-city": "/web-design/salt-lake-city-ut.html", "detroit": "/web-design/detroit-mi.html",
    "portland": "/web-design/portland-or.html", "philadelphia": "/web-design/philadelphia-pa.html",
}

# Primary target keyword of each page (the page's other keywords are supporting).
TARGETS = {
    "website design company": "home", "web design services": "services", "small business website package": "pricing",
    "web design process": "how", "local web designer near me": "about", "find a web designer near me": "contact",
    "web design questions": "faq", "texas web designer": "areas", "website design company us": "cities",
    "seo structure for website": "citypages",
    "small business website design": "smb", "contractor website design": "contractor", "seo web design": "seo",
    "small business website redesign": "redesign", "affordable website design for small business": "affordable",
    "web design for plumbers": "plumbers", "roofing contractor website design": "roofing",
    "web design for law firms": "law", "web design for therapists": "therapists",
    "how much does a website cost for a small business": "g-cost", "how much does a website designer cost": "g-designer",
    "how much does a website cost per month": "g-monthly", "web design packages": "g-packages",
    "how much does a website builder cost": "g-builder", "how do i find a web designer": "g-hire",
    "why small business need a website": "g-need",
    "web design in houston": "houston", "web design in dallas tx": "dallas", "website design austin tx": "austin",
    "web design tyler tx": "tyler", "website design longview tx": "longview", "web design east texas": "east-texas",
    "web design waco tx": "waco", "web design el paso": "el-paso", "web design kingwood": "kingwood",
    "web design company atlanta": "atlanta",
    "website design company new york": "new-york", "web design company tucson": "tucson",
    "web design huntsville al": "huntsville", "web design louisville": "louisville", "web design wilmington nc": "wilmington",
}

U_JOBS = "jobs, salary, pay or internships: a career search, not someone hiring a web designer"
U_LEARN = "courses, degrees, books or tutorials for people learning web design"
U_CRAFT = "design craft, theory, inspiration or trends searched by designers, not by business owners hiring one"
U_TOOLS = "design software, templates or AI tools for people building sites themselves"
U_TRIVIA = "definitions, crossword clues or trivia, no hiring intent"
U_BRAND = "names another agency or company (CLAUDE.md: other agencies' brand names are not used)"
U_ABROAD = "a place outside the United States (wrong country)"
U_WAVE2 = "a U.S. city outside Texas: Wave 2 candidate, not built in this run (see the Wave 2 table)"
U_WEATHER = "weather, travel or things to do: no fit"
U_TRADE = "about running a web design business (names, cards, leads, LLC, for sale), not hiring one"
U_ECOM = "online store builds or a specific platform (Shopify, Squarespace, WordPress agencies): not in the INTAKE.md packages"
U_GOV = "government, funding or loan websites, not website design"
U_PERSONAL = "personal or wedding websites, not a business site"
U_OFF = "off-topic for this business"
U_HAIR = "a hairstyle, nothing to do with websites"
U_LOW = "under 10 searches a month and no page fits it (the 10+ rule does not require it)"

RULES = [  # (regex, page key or ("unused", reason)); first match wins
    # exact-match assignments that must beat the broad rules below
    (r"^(web design company edinburgh)$", ("unused", U_ABROAD)),
    (r"^(tyler texas companies|tyler web design|website design tyler tx|website design tyler texas)$", "tyler"),
    (r"^(web design longview tx|website design longview texas|website builder longview tx|longview graphic design companies)$", "longview"),
    (r"^(east texas web design)$", "east-texas"),
    (r"tyler tx weather|weather for tyler|tyler texas weather|tyler tx places|how far is tyler|closest cities to tyler", ("unused", U_WEATHER)),
    (r"tyler tx construction companies|web developers tyler tx", "tyler"),
    # other agencies, products and named companies
    (r"white peak|icepick|digitaleer|digitech|tracemark|coalition seo|reno seo|mankato|pizano|visualwebz|jce seo|pure marketing|"
     r"\badit\b|arihant|lc winford|outrank|wisevu|web design avalon|web design glory|webs vent|web design depot|web design museum|"
     r"web design maisters|web design harbour|web design mechanic|web design sigma|web design torque|web design velocity|"
     r"web design 360|web and design 360|web designer xara|xtensive|xcel web|web design tree|web design library|"
     r"seo company limited|design company limited|w home design|web design just for you|web design you$|web design vibe|web design yellow|"
     r"web design 99designs|website design 99", ("unused", U_BRAND)),
    (r"\bjobs?\b|salary|salaries|\bpay\b|paid|\bmake\b.*(per website|hour)|how much web designer make|intern|apprentice|"
     r"job description|resume|hiring$|can web designers work|web design remote$|web design work$|web designer jobs", ("unused", U_JOBS)),
    (r"course|degree|bachelor|certificate|bootcamp|class|education|university|training|learning web design|for beginners|"
     r"for dummies|\b101\b|basics|fundamentals|\bbooks?\b|major$|how long is a web design course|skills|quiz|questions and answers|"
     r"web design unit|web design notes|web design online compiler|web design code|web design html|web design help$", ("unused", U_LEARN)),
    (r"crossword|meaning|definition|what is it|\bterms$|vocabulary|language|words$|description$|web design names$|"
     r"web design index|web design 60 30 10|is 95 typography|web design what|web design 3\.0|web2 0|8 web design$|"
     r"5 example|5 website name|web design is my passion|website design x$|will web design|will seo$|web design naics", ("unused", U_TRIVIA)),
    (r"weather|places to go", ("unused", U_WEATHER)),
    (r"haircut|web design hair", ("unused", U_HAIR)),
    (r"business cards?|business names|company names|name ideas|web design llc|for sale|web design leads|web design business$|"
     r"web design company logo|website design company logo|web design logos|logo ideas|website design company templates|"
     r"website design company portfolio|website design company online|web design company jobs", ("unused", U_TRADE)),
    (r"administration website|funding website|loan website|grants for website|association of jamaica|corporation website|"
     r"virginia small business website|small business saturday|what makes a small business small|how often do small businesses fail|"
     r"websites to buy small businesses|small business facebook page|small business websites to shop|yahoo small business website login", ("unused", U_GOV)),
    (r"wedding|personal website", ("unused", U_PERSONAL)),
    (r"web design company wordpress|shopify|squarespace web designer|ecommerce website designer|small business ecommerce website$|ecommerce website for small business|"
     r"ecommerce website design compan|ecommerce website examples|best small business ecommerce website$", ("unused", U_ECOM)),
    # wrong country
    (r"\b(uk|london|birmingham|manchester|bristol|coventry|leeds|glasgow|edinburgh|newcastle|kent|milton keynes|stoke on trent|"
     r"middlesbrough|west midlands|oxford|dublin|ireland|india|delhi|bangalore|pune|hyderabad|chennai|kolkata|ahmedabad|mumbai|"
     r"noida|gurgaon|kerala|kochi|calicut|trivandrum|tirupati|lucknow|ludhiana|chandigarh|faridabad|bhopal|vashi|visakhapatnam|"
     r"pakistan|lahore|bangladesh|sri lanka|dubai|uae|sharjah|qatar|kuwait|egypt|lebanon|kenya|ghana|lagos|uganda|zimbabwe|"
     r"south africa|australia|sydney|melbourne|brisbane|perth|adelaide|gold coast|new zealand|nz|auckland|christchurch|"
     r"canada|toronto|calgary|edmonton|montreal|ottawa|quebec|kingston|brampton|oakville|hamilton|singapore|malaysia|kl|"
     r"hong kong|philippines|thailand|yerevan|zanzibar|united kingdom|vancouver)\b(?! wa)", ("unused", U_ABROAD)),
    (r"web design freelance", "about"),
    (r"biggest web design|top 10 website design|best website design company in world|how design websites|3d designers|"
     r"what is a design build contractor|web design (portfolio |dashboard |wireframe |table )?examples", ("unused", U_CRAFT)),
    (r"low cost web design", "affordable"),
    # Texas cities with pages
    (r"houston", "houston"), (r"kingwood", "kingwood"), (r"el paso", "el-paso"), (r"waco", "waco"),
    (r"dallas", "dallas"), (r"austin", "austin"), (r"tyler", "tyler"), (r"longview", "longview"), (r"east texas", "east-texas"),
    (r"atlanta", "atlanta"),
    (r"texas web design|web design tx$|website design company texas", "areas"),
    # Wave 2 national city pages (Oct 16 2026)
    (r"st\.? louis|\bstl\b", "st-louis"), (r"kansas city|\bkc$", "kansas-city"), (r"chicago", "chicago"),
    (r"indianapolis", "indianapolis"), (r"cleveland(?! tn)", "cleveland"), (r"nashville", "nashville"),
    (r"miami", "miami"), (r"orlando", "orlando"), (r"phoenix", "phoenix"), (r"las vegas|vegas", "las-vegas"),
    (r"los angeles|\bla$", "los-angeles"), (r"san diego", "san-diego"), (r"sacramento", "sacramento"),
    # Wave 3 national city pages (Oct 17 2026)
    (r"new york|\bnyc\b", "new-york"), (r"orange county", "orange-county"), (r"tampa", "tampa"),
    (r"huntsville", "huntsville"), (r"tucson", "tucson"), (r"richmond", "richmond"), (r"louisville", "louisville"),
    (r"wilmington", "wilmington"),
    # Wave 4 city pages (Oct 17 2026); statewide phrases go to the page in that state's largest market
    (r"denver", "denver"), (r"boise", "boise"), (r"\bokc\b|oklahoma city", "okc"), (r"columbus ohio", "columbus"),
    (r"jacksonville fl|website design florida|website design company florida", "jacksonville"),
    (r"fort lauderdale", "fort-lauderdale"), (r"long beach", "long-beach"), (r"utah(?! county)|salt lake", "salt-lake-city"),
    (r"michigan|detroit", "detroit"), (r"vancouver wa|portland", "portland"), (r"philadelphia", "philadelphia"),
    # U.S. cities outside Texas: still Wave 2 candidates
    (r"new york|nyc|long island|san diego|chicago|los angeles|orange county|tampa|phoenix|tucson|denver|orlando|nashville|"
     r"huntsville|richmond|louisville|wilmington|wichita|okc|kansas city|boston|jacksonville|fort lauderdale|las vegas|miami|"
     r"columbus|sacramento|boise|utah|michigan|maryland|hawaii|new jersey|\bnj\b|\bct\b|\bri\b|florida|california|"
     r"long beach|rochester|york pa|website design york|yakima|vancouver wa|philadelphia", ("unused", U_WAVE2)),
    # cost guides
    (r"law firm website cost", "law"),
    (r"redesign", "redesign"),
    (r"cost per month|cost a month|cost to run|keep a website running|cost per year|cost a year|cost per year|website cost per year|"
     r"domain|website name cost|\.com website cost|server cost|host cost|hosting|management|maintenance cost|website with email|"
     r"how much should a website cost per year", "g-monthly"),
    (r"builder|creator|website maker|make your own|create your own|templates|\bwix\b|squarespace|small business website free|"
     r"website for small business owners|create small business website|how to make (a )?small business website|how to create small business website|"
     r"how to start a small business website|platforms|free website design for small business|web design for free|"
     r"small business website cms|small business website wordpress|easy small business website|google small business website$|"
     r"yahoo small business website$|best website for small business|what is the best website for small business|small business online website", "g-builder"),
    (r"designers? (cost|charge)|designer cost|hire a website designer|hourly rate|charge per hour|web design rates|web design charges|"
     r"web designers charge", "g-designer"),
    (r"packages", "g-packages"),
    (r"how much|cost|web design prices|price", "g-cost"),
    (r"web design quotes?|quotation|small business website package", "pricing"),
    # guides
    (r"find a (web|website) designer|hire a web designer|choose web design company|web design hiring|web design rfp|questionnaire|"
     r"questions to ask|which web design company|website design company reviews|web design company reviews", "g-hire"),
    (r"why small business|need a website|website help my business|have a website|website statistics|no website|website tips", "g-need"),
    # services
    (r"plumber", "plumbers"), (r"roofing", "roofing"), (r"law firm", "law"), (r"therapist", "therapists"),
    (r"contractor|construction|tradesm|design build", "contractor"),
    (r"\bseo\b", "seo"),
    (r"affordable|cheap|inexpensive|low cost", "affordable"),
    (r"small business|small food business|startups|web page design for small|website design for small", "smb"),
    (r"small business website.*examples|company website examples|small business website design examples|how to design a company website", "smb"),
    # core pages
    (r"process|web design questions$|difference between web design|what is web design company|who designs websites", None),
    (r"local web designer|professional website designer|freelance web designer|best website designer near me|web designer companies near me|"
     r"web designer near me best|web designer in near me|web designer agency near me|web designer and developer near me|website developer near me", "about"),
    (r"find a web designer near me", "contact"),
    (r"web design services$|web design services near me|website design company services|web design for business|web design studio", "services"),
    (r"\b(usa|us|in usa)$|web design usa|best web design company usa", "cities"),
    (r"near me|web design company$|website design company$|design website companies|web design firm|web design agency$|"
     r"web designers?$|^web design$|web design online$|website design agency", "home"),
    # craft, tools, trends
    (r"software|tools|apps?$|figma|ai$|with ai|ai tools|templates|playground|games|wallpaper|youtube|videos|blogs|reddit|news|"
     r"prompts|visual studio|google web designer|web design online free|web design free|web design for free", ("unused", U_TOOLS)),
    (r"inspiration|inspo|ideas|examples|gallery|portfolio|awards|winners|trends|styles|aesthetic|color|fonts|ui|ux|wireframe|mockup|"
     r"grid|hero|modal|tabs|patterns|principles|guidelines|best practices|systems|frameworks|elements|features|theory|history|"
     r"archive|90s|80s|8bit|960|3d|2010|2025|2026|dimensions|size|drawing|background|dashboard|table examples|requirements|"
     r"references|resources|graphic design|branding|architects|experience|icon|images|development$|for therapists|"
     r"web design for law|web design ideas|web design kingston|web design nz|branding|tips$|projects|programs|web design sites|themes|"
     r"user interface", ("unused", U_CRAFT)),
    (r"in spanish", ("unused", U_OFF)),
]

PROCESS_MAP = {"web design process": "how", "web design questions": "faq", "difference between web design and web development": "faq",
               "what is web design company": "faq", "who designs websites": "faq"}


def classify(kw):
    k = kw.lower().strip()
    if k in TARGETS:
        return TARGETS[k]
    if k in PROCESS_MAP:
        return PROCESS_MAP[k]
    for pat, dest in RULES:
        if re.search(pat, k):
            if dest is None:
                continue
            return dest
    return None


def main():
    wb = openpyxl.load_workbook(ROOT / "keywords" / "Web-Design-Keywords.xlsx", read_only=True)
    rows = [r for r in list(wb["ALL"].iter_rows(values_only=True))[1:] if r[1]]
    by_page, unused, low_unused, missing = defaultdict(list), defaultdict(list), defaultdict(int), []
    found_targets = set()
    for seed, kw, typ, vol, sd, cpc, pd in rows:
        vol = vol or 0
        dest = classify(kw)
        if kw.lower() in TARGETS:
            found_targets.add(kw.lower())
        if dest is None:
            if vol >= 10:
                missing.append((kw, vol))
                continue
            dest = ("unused", U_LOW)
        if isinstance(dest, tuple):
            if vol >= 10:
                unused[dest[1]].append((kw, vol, sd, typ))
            else:
                low_unused[dest[1]] += 1
        else:
            by_page[dest].append((kw, vol, sd, typ, kw.lower() in TARGETS))
    for t in TARGETS:
        if t not in found_targets:
            missing.append((f"TARGET NOT IN DATA: {t}", 0))
    n10 = sum(1 for r in rows if (r[3] or 0) >= 10)
    assigned10 = sum(1 for v in by_page.values() for r in v if r[1] >= 10)
    unused10 = sum(len(v) for v in unused.values())
    out = ["# Keyword plan (Oct 12 2026)", "",
           "Source: keywords/Web-Design-Keywords.xlsx, ALL tab (Ubersuggest, United States, pulled Oct 12 2026): "
           f"{len(rows)} unique keywords, {n10} with 10 or more searches a month. Generated by "
           "`python3 scripts/keyword_plan.py`, which fails if any 10+ keyword is left unclassified.", "",
           "**Maurice's 10+ rule result:** of the " + f"{n10} keywords with 10+ searches a month, **{assigned10} are assigned to a page** "
           f"(as its target or a supporting keyword) and **{unused10} are listed below as deliberately unused**, each group with its "
           f"one-line reason. Unclassified: **{len([m for m in missing if m[1] >= 10])}**.", "",
           "Texas towns with a web design keyword at 10+ searches a month, each with its own page: Houston, Dallas, Austin, "
           "Tyler, Longview, East Texas, Waco, El Paso and Kingwood (exact keywords in SERVICES.md). No other Texas town "
           "appears in the data at 10+ (checked: San Antonio, Fort Worth, Plano, Frisco, McKinney, Round Rock, Katy, Sugar Land, "
           "The Woodlands, Lubbock, Amarillo, Corpus Christi, Beaumont, Midland, Killeen, Denton, Nacogdoches, Lufkin, "
           "Texarkana and the other existing city-page towns all show 0 or are absent).", "",
           "SD = Ubersuggest SEO difficulty (0 to 100). Type S = Suggestion row, Q = Question row.", "",
           "## Keywords by page", ""]
    order = list(PAGES)
    for key in order:
        items = sorted(by_page.get(key, []), key=lambda r: (not r[4], -r[1]))
        if not items:
            continue
        tgt = [r for r in items if r[4]]
        out.append(f"### {PAGES[key]}")
        out.append("")
        if tgt:
            out.append(f"Target: **{tgt[0][0]}** ({tgt[0][1]:,}/mo, SD {tgt[0][2]})")
            out.append("")
        sup = [r for r in items if not r[4] and r[1] >= 10]
        lows = [r for r in items if not r[4] and r[1] < 10]
        if sup:
            out.append("Supporting: " + "; ".join(f"{r[0]} ({r[1]:,}, SD {r[2]})" for r in sup))
            out.append("")
        if lows:
            out.append(f"Also covers {len(lows)} lower-volume variants (under 10/mo), e.g. " + "; ".join(r[0] for r in lows[:6]) + ".")
            out.append("")
    out += ["## Deliberately unused (10+ searches a month), grouped by reason", ""]
    for reason, items in sorted(unused.items(), key=lambda kv: -sum(r[1] for r in kv[1])):
        items.sort(key=lambda r: -r[1])
        out.append(f"### {reason} ({len(items)} keywords, {sum(r[1] for r in items):,} searches/mo)")
        out.append("")
        out.append("; ".join(f"{r[0]} ({r[1]:,})" for r in items))
        out.append("")
    out += ["## Wave 2 candidates: U.S. cities outside Texas with 10+ searches", "",
            "Not built yet. Listed for Maurice to choose from. Thirteen cities from this list and the national keyword "
            "files got pages in Wave 2 (Oct 16 2026), eight more in Wave 3 (Oct 17 2026: New York, Orange County, Tampa, "
            "Huntsville, Tucson, Richmond, Louisville, Wilmington NC) and 58 more outside Texas in Wave 4 (Oct 17 2026, "
            "CITY-PAGES-WAVE4.md), see those sections at the end; their phrases from this file are assigned to those pages "
            "above.", "",
            "| Keyword | Volume | SD |", "|---|---:|---:|"]
    for kw, vol, sd, typ in sorted(unused.get(U_WAVE2, []), key=lambda r: -r[1]):
        out.append(f"| {kw} | {vol:,} | {sd} |")
    out += ["", "## Keywords under 10 searches a month (summary)", "",
            f"{sum(1 for r in rows if (r[3] or 0) < 10)} rows show under 10 searches a month (most show 0). They are not "
            "required by the 10+ rule. Those that fit a page are counted on that page above; the rest by group:", ""]
    for reason, n in sorted(low_unused.items(), key=lambda kv: -kv[1]):
        out.append(f"- {reason}: {n}")
    (ROOT / "docs" / "keyword-plan.md").write_text("\n".join(out) + "\n")
    print(f"{len(rows)} rows, {n10} at 10+: {assigned10} assigned, {unused10} unused, {len(missing)} problems")
    for m in missing:
        print("UNCLASSIFIED", m)
    # The Atlanta add-on keyword file gets its own section at the end of the same plan.
    sys.path.insert(0, str(ROOT / "scripts"))
    import keyword_plan_atlanta
    atl = keyword_plan_atlanta.main()
    # Wave 2 national city pages (Oct 16 2026) come last.
    import keyword_plan_wave2
    w2 = keyword_plan_wave2.main()
    # Wave 3 national city pages (Oct 17 2026) after Wave 2.
    import keyword_plan_wave3
    w3 = keyword_plan_wave3.main()
    # Wave 4 city pages (Oct 17 2026) after Wave 3.
    import keyword_plan_wave4
    w4 = keyword_plan_wave4.main()
    return 1 if missing or atl or w2 or w3 or w4 else 0


if __name__ == "__main__":
    sys.exit(main())
