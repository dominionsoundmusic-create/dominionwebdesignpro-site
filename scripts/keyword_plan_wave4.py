#!/usr/bin/env python3
"""Wave 4 keyword plan (Oct 17 2026): 81 more city pages (CITY-PAGES-WAVE4.md).

Reads the city tabs of keywords/Web-Design-Texas-Cities-Keywords.xlsx, -South-East-, -West-Midwest- and the matching
tabs of -National-Cities-Keywords.xlsx (Ubersuggest US, pulled Oct 16 2026), plus the Pittsburgh and Greensboro rows
of keywords/Web-Design-5-Cities-Recheck.xlsx, and rewrites the "## Wave 4" section at the end of docs/keyword-plan.md.

Every row with 10 or more searches a month in those tabs is either assigned (the page's target, a supporting keyword
on that page or on another page of the site, an FAQ question on the page) or listed as unused with a one-line reason.
Exits 1 if any 10+ keyword is unclassified, a page's target is missing from the data, or a page file is missing.
scripts/keyword_plan.py runs this after Wave 3.

Usage: python3 scripts/keyword_plan_wave4.py
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

import openpyxl
import yaml

ROOT = Path(__file__).resolve().parent.parent
PLAN = ROOT / "docs" / "keyword-plan.md"
HEAD = "## Wave 4"
KW = ROOT / "keywords"
FILES = {"TX": "Web-Design-Texas-Cities-Keywords.xlsx", "SE": "Web-Design-South-East-Cities-Keywords.xlsx",
         "WM": "Web-Design-West-Midwest-Cities-Keywords.xlsx", "NAT": "Web-Design-National-Cities-Keywords.xlsx"}
RECHECK = KW / "Web-Design-5-Cities-Recheck.xlsx"

# slug -> (part, [(file, tab), ...], main target, regex for this city's own web design phrases)
CITIES = {
    "san-antonio-tx": ("A", [("TX", "San Antonio")], "web design san antonio", r"san antonio"),
    "fort-worth-tx": ("A", [("TX", "Fort Worth")], "web design fort worth texas", r"fort worth"),
    "arlington-tx": ("A", [("TX", "Arlington TX")], "arlington website design", r"arlington"),
    "corpus-christi-tx": ("A", [("TX", "Corpus Christi")], "website design corpus christi", r"corpus christi"),
    "lubbock-tx": ("A", [("TX", "Lubbock")], "web design lubbock tx", r"lubbock"),
    "amarillo-tx": ("A", [("TX", "Amarillo")], "web design amarillo", r"amarillo"),
    "beaumont-tx": ("A", [("TX", "Beaumont TX")], "web design beaumont tx", r"beaumont"),
    "midland-tx": ("A", [("TX", "Midland TX")], "web design midland tx", r"midland"),
    "odessa-tx": ("A", [("TX", "Odessa TX")], "website design odessa tx", r"odessa"),
    "killeen-tx": ("A", [("TX", "Killeen")], "web design killeen tx", r"killeen"),
    "mcallen-tx": ("A", [("TX", "Mcallen")], "web design mcallen texas", r"mcallen"),
    "laredo-tx": ("A", [("TX", "Laredo")], "web design laredo tx", r"laredo"),
    "brownsville-tx": ("A", [("TX", "Brownsville TX")], "web design brownsville", r"brownsville"),
    "sugar-land-tx": ("A", [("TX", "Sugar Land")], "web design sugar land", r"sugar land"),
    "katy-tx": ("A", [("TX", "Katy TX")], "katy web design", r"\bkaty\b"),
    "the-woodlands-tx": ("A", [("TX", "The Woodlands")], "web design the woodlands", r"woodlands"),
    "round-rock-tx": ("A", [("TX", "Round Rock")], "web design round rock", r"round rock"),
    "abilene-tx": ("A", [("TX", "Abilene TX")], "abilene website design", r"abilene"),
    "san-angelo-tx": ("A", [("TX", "San Angelo")], "web design san angelo", r"san angelo"),
    "temple-tx": ("A", [("TX", "Temple TX")], "web design temple tx", r"temple"),
    "nacogdoches-tx": ("A", [("TX", "Nacogdoches")], "web design nacogdoches", r"nacogdoches"),
    "texarkana-tx": ("A", [("TX", "Texarkana")], "website design texarkana", r"texarkana"),
    "cypress-tx": ("A", [], "web design cypress tx", r"cypress"),
    "charlotte-nc": ("B", [("SE", "Charlotte"), ("NAT", "Charlotte")], "web design in charlotte nc", r"charlotte(?!sville)"),
    "raleigh-nc": ("B", [("SE", "Raleigh"), ("NAT", "Raleigh")], "web design raleigh north carolina", r"raleigh"),
    "durham-nc": ("B", [("SE", "Durham NC")], "web design durham nc", r"durham"),
    "greensboro-nc": ("B", [("SE", "Greensboro"), ("NAT", "Greensboro"), ("RECHECK", "greensboro")], "web design greensboro", r"greensboro"),
    "charleston-sc": ("B", [("SE", "Charleston SC")], "charleston website design", r"charleston"),
    "columbia-sc": ("B", [("SE", "Columbia SC")], "web design columbia", r"columbia(?! mo)"),
    "greenville-sc": ("B", [("SE", "Greenville SC")], "web design greenville sc", r"greenville(?! nc)"),
    "savannah-ga": ("B", [("SE", "Savannah")], "savannah website design", r"savannah"),
    "augusta-ga": ("B", [("SE", "Augusta GA")], "web design augusta ga", r"augusta"),
    "jacksonville-fl": ("B", [("SE", "Jacksonville FL"), ("NAT", "Jacksonville")], "jacksonville website design", r"jacksonville(?! nc)"),
    "fort-lauderdale-fl": ("B", [("SE", "Fort Lauderdale")], "web design fort lauderdale fl", r"fort lauderdale"),
    "west-palm-beach-fl": ("B", [("SE", "West Palm Beach")], "web design west palm beach", r"palm beach"),
    "st-petersburg-fl": ("B", [("SE", "St. Petersburg FL")], "web design st petersburg", r"st\.? pete"),
    "sarasota-fl": ("B", [("SE", "Sarasota")], "web design sarasota florida", r"sarasota"),
    "fort-myers-fl": ("B", [("SE", "Fort Myers")], "web design fort myers", r"fort myers"),
    "tallahassee-fl": ("B", [("SE", "Tallahassee")], "web design tallahassee fl", r"tallahassee"),
    "pensacola-fl": ("B", [("SE", "Pensacola")], "web design pensacola florida", r"pensacola"),
    "birmingham-al": ("B", [("SE", "Birmingham AL"), ("NAT", "Birmingham")], "web design birmingham al", r"birmingham|alabama"),
    "mobile-al": ("B", [("SE", "Mobile AL")], "website design mobile al", r"mobile al|traffic is mobile"),
    "montgomery-al": ("B", [("SE", "Montgomery AL")], "web design montgomery al", r"montgomery"),
    "jackson-ms": ("B", [("SE", "Jackson MS")], "web design jackson ms", r"jackson ms|mississippi"),
    "new-orleans-la": ("B", [("SE", "New Orleans"), ("NAT", "New Orleans")], "new orleans website design", r"new orleans|louisiana"),
    "shreveport-la": ("B", [("SE", "Shreveport")], "web design shreveport", r"shreveport"),
    "baton-rouge-la": ("B", [("NAT", "Baton Rouge")], "website design baton rouge", r"baton rouge"),
    "knoxville-tn": ("B", [("SE", "Knoxville")], "knoxville tn web design", r"knoxville"),
    "chattanooga-tn": ("B", [("NAT", "Chattanooga")], "chattanooga website design", r"chattanooga"),
    "memphis-tn": ("B", [("NAT", "Memphis")], "memphis website design", r"^memphis"),
    "lexington-ky": ("B", [("SE", "Lexington KY")], "website design lexington", r"lexington(?! sc)|kentucky"),
    "little-rock-ar": ("B", [("NAT", "Little Rock")], "website design little rock ar", r"little rock"),
    "denver-co": ("C", [("WM", "Denver"), ("NAT", "Denver")], "web design denver co", r"denver"),
    "colorado-springs-co": ("C", [("WM", "Colorado Springs")], "colorado springs web design company", r"colorado"),
    "fort-collins-co": ("C", [("WM", "Fort Collins")], "web design fort collins co", r"fort collins"),
    "seattle-wa": ("C", [("WM", "Seattle"), ("NAT", "Seattle")], "web design seattle", r"seattle"),
    "spokane-wa": ("C", [("WM", "Spokane")], "web design spokane wa", r"spokane"),
    "portland-or": ("C", [("WM", "Portland"), ("NAT", "Portland")], "web design portland oregon", r"portland(?! (maine|me)\b)"),
    "boise-id": ("C", [("WM", "Boise"), ("NAT", "Boise")], "web design boise idaho", r"boise|idaho"),
    "salt-lake-city-ut": ("C", [("WM", "Salt Lake City"), ("NAT", "Salt Lake City")], "website design salt lake city", r"salt lake city (web|website)|web design salt lake|web development salt lake"),
    "reno-nv": ("C", [("WM", "Reno")], "web design reno nv", r"reno"),
    "san-francisco-ca": ("C", [("WM", "San Francisco")], "web design san francisco bay area", r"san francisco|bay area|\bsf$"),
    "san-jose-ca": ("C", [("WM", "San Jose")], "web design san jose", r"san jose"),
    "fresno-ca": ("C", [("WM", "Fresno")], "fresno website design", r"fresno"),
    "bakersfield-ca": ("C", [("WM", "Bakersfield")], "bakersfield website design", r"bakersfield"),
    "long-beach-ca": ("C", [("WM", "Long Beach")], "web design long beach ca", r"long beach"),
    "scottsdale-az": ("C", [("WM", "Scottsdale")], "web design scottsdale az", r"scottsdale"),
    "mesa-az": ("C", [("WM", "Mesa AZ")], "website design mesa", r"mesa|arizona"),
    "albuquerque-nm": ("C", [("WM", "Albuquerque"), ("NAT", "Albuquerque")], "web design in albuquerque", r"albuquerque"),
    "oklahoma-city-ok": ("C", [("NAT", "Oklahoma City")], "web design in oklahoma city", r"oklahoma|\bokc\b"),
    "tulsa-ok": ("C", [("NAT", "Tulsa")], "web designers in tulsa", r"tulsa"),
    "omaha-ne": ("C", [("WM", "Omaha"), ("NAT", "Omaha")], "web design omaha ne", r"omaha"),
    "des-moines-ia": ("C", [("WM", "Des Moines"), ("NAT", "Des Moines")], "web design des moines", r"des moines"),
    "minneapolis-mn": ("C", [("WM", "Minneapolis"), ("NAT", "Minneapolis")], "web design minneapolis", r"minneapolis|minnesota|eden prairie"),
    "madison-wi": ("C", [("WM", "Madison WI")], "madison website design", r"madison"),
    "grand-rapids-mi": ("C", [("WM", "Grand Rapids")], "web design grand rapids", r"grand rapids"),
    "detroit-mi": ("C", [("WM", "Detroit"), ("NAT", "Detroit")], "web design detroit", r"detroit"),
    "cincinnati-oh": ("C", [("WM", "Cincinnati"), ("NAT", "Cincinnati")], "web design cincinnati", r"cincinnati"),
    "columbus-oh": ("C", [("NAT", "Columbus")], "website design columbus", r"columbus"),
    "pittsburgh-pa": ("C", [("WM", "Pittsburgh"), ("NAT", "Pittsburgh"), ("RECHECK", "pittsburgh")], "web design pittsburgh pa", r"pittsburgh"),
    "philadelphia-pa": ("C", [("NAT", "Philadelphia")], "philadelphia web designer", r"philadelphia"),
}
# Cypress has no tab: its only row sits in the Temple TX tab.
EXTRA_TARGET_TAB = {"cypress-tx": ("TX", "Temple TX")}

# Rows in a city's tab that belong to another page of the site (checked before the unused rules).
OTHER_PAGES = [
    (r"^web design cypress tx$", "/web-design/cypress-tx.html"),
    (r"^web design in nc$", "/web-design/raleigh-nc.html"),
    (r"^web design north carolina$", "/web-design/durham-nc.html"),
    (r"^web design nc$", "/web-design/wilmington-nc.html"),
    (r"^web design sc$", "/web-design/greenville-sc.html"),
    (r"^web design ga$", "/web-design/augusta-ga.html"),
    (r"^web design az$|web design in arizona|arizona web design", "/web-design/mesa-az.html"),
    (r"^web design new mexico$", "/web-design/albuquerque-nm.html"),
    (r"^web design in colorado$", "/web-design/colorado-springs-co.html"),
    (r"^webpage design near me$", "/"),
    (r"^web design summerville sc$", "/web-design/charleston-sc.html"),
    (r"^web design lexington sc$", "/web-design/columbia-sc.html"),
    (r"^web designer mobile al$", "/web-design/mobile-al.html"),
    (r"^web designer tulsa$", "/web-design/tulsa-ok.html"),
    (r"^web design (houston|houston tx|houston texas)$", "/web-design/houston-tx.html"),
    (r"^web design kingwood$", "/web-design/kingwood-tx.html"),
    (r"^web design east texas$", "/web-design/east-texas.html"),
    (r"^web design new braunfels$", "/web-design/new-braunfels-tx.html"),
    (r"^web design mckinney tx$", "/web-design/mckinney-tx.html"),
    (r"^web design tyler (tx|texas)$", "/web-design/tyler-tx.html"),
    (r"^web design in las vegas$", "/web-design/las-vegas-nv.html"),
    (r"^web design kansas$", "/web-design/kansas-city-mo.html"),
    (r"^web design (katy|katy tx)$", "/web-design/katy-tx.html"),
    (r"^web design the woodlands$", "/web-design/the-woodlands-tx.html"),
    (r"^web design midland tx$", "/web-design/midland-tx.html"),
    (r"^website design odessa tx$|^web design odessa tx$", "/web-design/odessa-tx.html"),
    (r"^web design beaumont tx$", "/web-design/beaumont-tx.html"),
    (r"^web design arlington tx$", "/web-design/arlington-tx.html"),
    (r"^web design lubbock$", "/web-design/lubbock-tx.html"),
    (r"^web design knoxville$", "/web-design/knoxville-tn.html"),
    (r"^web design salt lake city$", "/web-design/salt-lake-city-ut.html"),
    (r"^web design raleigh$", "/web-design/raleigh-nc.html"),
    (r"san antonio", "/web-design/san-antonio-tx.html"),
    (r"^(web design tx|web design in texas|web designing texas|texas web designers|web design texas|web design services texas)$",
     "/service-areas.html"),
    (r"how often should (a )?websites? be redesigned", "/small-business-website-redesign/"),
]

U_JOBS = "jobs, salary, pay or whether designers are in demand: a career search, not someone hiring a designer"
U_LEARN = "courses, colleges or learning to design a site yourself"
U_TRIVIA = "a generic web design definition, craft, example or trivia question with no city and no hiring intent"
U_PLACE = "a question about the place itself (safety, weather, distance, schedules, shops, headquarters), not web design"
U_BRAND = "names or reads like the name of another agency, person or product (other agencies' brand names are not used)"
U_OTHERPLACE = "a different place with a similar name or another town with no page yet (Wave 2 candidate)"
U_OFF = "off-topic: nothing to do with websites"
U_ECOM = "an online store build: not in the INTAKE.md packages (the page says so where it comes up)"
U_TOOL = "a design tool or template product, not hiring a designer"

UNUSED_RULES = [
    (r"loops marketing|thrive web design|neo memphis|webb design|web design corp reviews|all seattle web design|williams web design|"
     r"web designs your way|web design by kate|99designs|portland design works|web design square$|web design shop$", U_BRAND),
    (r"jobs?\b|salary|get paid|designers make|companies make|make per website|in demand|work from home|where do web designers work", U_JOBS),
    (r"course|colleges|seattle central|how to learn|how to start designing|for beginners|how to web design", U_LEARN),
    (r"is .* (safe|dangerous)|bourbon street safe|snow|temperature|raining|hooks schedule|dress code|close to dallas|where is katy|"
     r"target headquarters|dry city|streetwear|designer stores|hunting stores|how wealthy|pros and cons|cookie designers|"
     r"salt lake city design firms", U_PLACE),
    (r"sugar landing|sugaring|web mapping|apa style", U_OFF),
    (r"ecommerce", U_ECOM),
    (r"web design kits|google web designer", U_TOOL),
    (r"charlottesville|port charlotte|columbia mo|greenville nc|jacksonville nc|lexington sc(?!x)|jackson mi|portland (maine|me)\b|"
     r"long island|grand junction|st cloud|naples|hickory|lawrence ks|durango|rock hill|roanoke|rockville|lancaster|logan utah|"
     r"wichita|for landscapers", U_OTHERPLACE),
    (r"definition|tips$|meaning|description|requirements|explain|examples|color codes|ideas|effects|short form|difference|"
     r"accessibility standards|survey questions|test questions|how many web|who designs websites|biggest web design|"
     r"why design mobile|ada compliant|why is web design important|why website design matters|will web design|"
     r"^web design az$", U_TRIVIA),
]
COST = r"how much|rates$|how long does website design take"
COST_PAGE = "/how-much-does-a-website-designer-cost/"


def load(file, tab):
    if file == "RECHECK":
        wb = openpyxl.load_workbook(RECHECK, read_only=True)
        out = []
        for r in list(wb["ALL"].iter_rows(values_only=True))[1:]:
            if r[0] and tab in r[0].lower():
                out.append((r[0], r[1], r[2] or 0, r[3]))
        return out
    wb = openpyxl.load_workbook(KW / FILES[file], read_only=True)
    rows = list(wb[tab].iter_rows(values_only=True))
    h = rows[0]
    iv, isd = h.index("Volume"), h.index("SEO Difficulty")
    return [(r[0], r[1], r[iv] or 0, r[isd]) for r in rows[1:] if r[0]]


def page_faqs(slug):
    p = ROOT / "src" / "pages" / "web-design" / f"{slug}.html"
    if not p.exists():
        return None
    fm = yaml.safe_load(p.read_text().split("---")[1])
    return [re.sub(r"<[^>]+>", " ", f["q"]).lower() for f in (fm.get("faqs") or [])]


def words(s):
    return set(re.findall(r"[a-z]+", s)) - {"a", "the", "for", "do", "does", "is", "to", "in", "of", "web", "website"}


def classify(slug, kw, faqs, own_pat, target):
    k = kw.lower().strip()
    if k == target:
        return ("target", None)
    for p, reason in UNUSED_RULES[:4]:  # brands, jobs, learning, questions about the place
        if re.search(p, k):
            return ("unused", reason)
    if re.search(COST, k):  # national cost questions: an FAQ on the page if it answers one, else the cost guide
        if any(len(words(k) & words(q)) >= max(2, len(words(k)) - 1) for q in faqs):
            return ("faq", None)
        return ("other", COST_PAGE)
    for p, url in OTHER_PAGES:
        if re.search(p, k) and url != f"/web-design/{slug}.html":
            return ("other", url)
    for p, reason in UNUSED_RULES[4:]:
        if re.search(p, k):
            return ("unused", reason)
    if re.search(own_pat, k) or any(re.search(p, k) for p, _ in OTHER_PAGES):
        return ("support", None)
    return (None, None)


SVC_ROWS = []
SERVICES = ROOT / "SERVICES.md"
SVC_HEAD = "## Wave 4: city pages"
PART_NAME = {"A": "Part A: Texas", "B": "Part B: South and East", "C": "Part C: West and Midwest"}


def write_services():
    """Rewrites the Wave 4 section at the end of SERVICES.md from the same data (every number read from the files)."""
    out = [f"{SVC_HEAD} (Oct 17 2026, CITY-PAGES-WAVE4.md)", "",
           "Keyword sources: the city tabs of keywords/Web-Design-Texas-Cities-Keywords.xlsx, -South-East-Cities-, "
           "-West-Midwest-Cities- and -National-Cities-Keywords.xlsx (Ubersuggest US, pulled Oct 16 2026), plus "
           "keywords/Web-Design-5-Cities-Recheck.xlsx for Pittsburgh and Greensboro. Generated by "
           "`python3 scripts/keyword_plan_wave4.py`; full supporting and unused lists are in docs/keyword-plan.md, section "
           "\"Wave 4\". Every page is in its region group in site.json (city directory, service areas page, Cities menu "
           "regions, sitemap).", ""]
    cur = None
    for slug, part, tgt, sup in SVC_ROWS:
        if part != cur:
            cur = part
            out += [f"### {PART_NAME[part]}", "", "| Page | URL | Target keyword | Vol | SD | Main supporting terms | Status |",
                    "|---|---|---|---:|---:|---|---|"]
        sup_txt = "; ".join(f"{r[0]} {r[1]:,}" for r in sup) or "none at 10+ besides the target"
        out.append(f"| {slug} | /web-design/{slug}.html | {tgt[0]} | {tgt[1]:,} | {tgt[2]} | {sup_txt} | new |")
        nxt = SVC_ROWS[SVC_ROWS.index((slug, part, tgt, sup)) + 1][1] if (slug, part, tgt, sup) != SVC_ROWS[-1] else None
        if nxt != part:
            out.append("")
    text = SERVICES.read_text()
    i = text.find("\n" + SVC_HEAD)
    if i >= 0:
        text = text[:i].rstrip() + "\n"
    SERVICES.write_text(text + "\n" + "\n".join(out))


def section():
    out = [HEAD, "", "81 more city pages (CITY-PAGES-WAVE4.md, Oct 17 2026). Sources: the city tabs of "
           "keywords/Web-Design-Texas-Cities-Keywords.xlsx, -South-East-Cities-, -West-Midwest-Cities- and the matching tabs of "
           "-National-Cities-Keywords.xlsx (Ubersuggest US, pulled Oct 16 2026), plus the Pittsburgh and Greensboro rows of "
           "keywords/Web-Design-5-Cities-Recheck.xlsx. Generated by `python3 scripts/keyword_plan_wave4.py` (run by "
           "scripts/keyword_plan.py), which fails if any 10+ keyword is unclassified. A keyword that appears in several tabs is "
           "counted once per tab. \"On another page\" means the row is a supporting keyword of a different page on the site (for "
           "example a Houston row inside the Beaumont tab, or a national cost question that the cost guide answers). These cities "
           "were removed from the \"Wave 2 candidates\" and \"Remaining national candidates\" tables above.", ""]
    problems, totals = [], defaultdict(int)
    unused_all = defaultdict(list)
    elsewhere = defaultdict(list)
    for slug, (part, tabs, target, pat) in CITIES.items():
        faqs = page_faqs(slug)
        if faqs is None:
            problems.append((slug, "PAGE FILE MISSING", 0))
            faqs = []
        rows = []
        for f, t in tabs:
            rows += [(r, f"{t} tab" if f != "RECHECK" else "5-Cities-Recheck file") for r in load(f, t)]
        if slug in EXTRA_TARGET_TAB:
            f, t = EXTRA_TARGET_TAB[slug]
            rows += [(r, f"{t} tab") for r in load(f, t) if r[0].lower().strip() == target]
        seen, tgt, sup, faq, low = set(), None, [], [], 0
        for (kw, typ, vol, sd), src in rows:
            k = kw.lower().strip()
            if (k, src) in seen:
                continue
            seen.add((k, src))
            if vol < 10:
                low += 1
                continue
            kind, info = classify(slug, kw, faqs, pat, target)
            if kind == "target":
                if not tgt:
                    tgt = (kw, vol, sd)
                    totals["target"] += 1
                else:
                    totals["dup-target"] += 1
                continue
            if kind == "support":
                if k not in {s[0].lower() for s in sup}:
                    sup.append((kw, vol, sd))
            elif kind == "faq":
                faq.append((kw, vol, sd))
            elif kind == "other":
                elsewhere[info].append((kw, vol, sd, src))
            elif kind == "unused":
                unused_all[info].append((kw, vol, sd, src))
            else:
                problems.append((slug, kw, vol))
            totals[kind or "missing"] += 1
        if not tgt:
            problems.append((slug, f"TARGET NOT IN DATA: {target}", 0))
            continue
        SVC_ROWS.append((slug, part, tgt, sorted(sup, key=lambda r: -r[1])[:4]))
        out.append(f"### /web-design/{slug}.html")
        out.append("")
        out.append(f"Target: **{tgt[0]}** ({tgt[1]:,}/mo, SD {tgt[2]})")
        out.append("")
        if sup:
            sup.sort(key=lambda r: -r[1])
            out.append("Supporting: " + "; ".join(f"{r[0]} ({r[1]:,}, SD {r[2]})" for r in sup))
            out.append("")
        if faq:
            out.append("Answered in an FAQ (close wording): " + "; ".join(f"{r[0]} ({r[1]:,}, SD {r[2]})" for r in faq))
            out.append("")
        if low:
            out.append(f"Rows under 10/mo in this city's tabs: {low} (not required by the 10+ rule).")
            out.append("")
    n_on = totals["target"] + totals["support"] + totals["faq"] + totals["other"]
    out.insert(2, f"**10+ rule result for the 81 cities:** {n_on + totals['unused'] + totals['missing'] + totals['dup-target']} "
               f"keyword rows at 10+ (counted per tab); **{n_on + totals['dup-target']} assigned** ({totals['target']} targets"
               f"{', ' + str(totals['dup-target']) + ' repeats of a target in a second tab' if totals['dup-target'] else ''}, "
               f"{totals['support']} supporting, {totals['faq']} FAQ questions, {totals['other']} on another page) and "
               f"**{totals['unused']} deliberately unused**. Unclassified: **{totals['missing']}**.\n")
    out += ["### Wave 4 rows assigned to another page", ""]
    for url, items in sorted(elsewhere.items()):
        uniq = {}
        for r in items:
            uniq.setdefault(r[0].lower(), r)
        out.append(f"**{url}**: " + "; ".join(f"{r[0]} ({r[1]:,}, {r[3]})" for r in sorted(uniq.values(), key=lambda r: -r[1])))
        out.append("")
    out += ["### Wave 4: deliberately unused (10+ searches a month)", ""]
    for reason, items in sorted(unused_all.items(), key=lambda kv: -sum(r[1] for r in kv[1])):
        uniq = {}
        for r in items:
            uniq.setdefault(r[0].lower(), r)
        out.append(f"**{reason}** ({len(uniq)} keywords): " + "; ".join(
            f"{r[0]} ({r[1]:,}, {r[3]})" for r in sorted(uniq.values(), key=lambda r: -r[1])))
        out.append("")
    return "\n".join(out) + "\n", problems, totals


def main():
    text, problems, totals = section()
    plan = PLAN.read_text()
    i = plan.find("\n" + HEAD + "\n")
    if i >= 0:
        plan = plan[:i].rstrip() + "\n"
    PLAN.write_text(plan + "\n" + text)
    write_services()
    print(f"Wave 4: {dict(totals)}, {len(problems)} problems")
    for p in problems:
        print("PROBLEM", p)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
