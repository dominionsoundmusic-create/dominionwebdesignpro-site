#!/usr/bin/env python3
"""Wave 2 keyword plan (Oct 16 2026): 13 national city pages.

Reads keywords/Web-Design-National-Cities-Keywords.xlsx (one tab per city) and
keywords/Web-Design-5-Cities-Recheck.xlsx (ALL tab; Cleveland rows) and rewrites the "## Wave 2"
section at the end of docs/keyword-plan.md.

For the 13 built cities, every keyword with 10 or more searches a month is assigned to that city's
page (target or supporting) or listed as unused with a one-line reason. Cities in the files that got
no page are summarized as remaining candidates. Exits 1 if any 10+ keyword of a built city is
unclassified or a page target is missing from the data. scripts/keyword_plan.py runs this after the
Atlanta add-on section.

Usage: python3 scripts/keyword_plan_wave2.py
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent
PLAN = ROOT / "docs" / "keyword-plan.md"
HEAD = "## Wave 2"
NAT = ROOT / "keywords" / "Web-Design-National-Cities-Keywords.xlsx"
RECHECK = ROOT / "keywords" / "Web-Design-5-Cities-Recheck.xlsx"

# tab name -> (slug, main target, regex that marks a keyword as this city's web design phrase)
CITIES = {
    "St Louis": ("st-louis-mo", "website design st louis", r"st\.? louis|\bstl\b"),
    "Phoenix": ("phoenix-az", "web design company in phoenix", r"phoenix"),
    "San Diego": ("san-diego-ca", "web design in san diego", r"san diego"),
    "Las Vegas": ("las-vegas-nv", "website design las vegas nevada", r"las vegas|vegas"),
    "Los Angeles": ("los-angeles-ca", "los angeles web design companies", r"los angeles|\bla$"),
    "Miami": ("miami-fl", "web design in miami", r"miami"),
    "Nashville": ("nashville-tn", "web design in nashville", r"nashville"),
    "Chicago": ("chicago-il", "web design agency in chicago", r"chicago"),
    "Orlando": ("orlando-fl", "web design in orlando", r"orlando"),
    "Indianapolis": ("indianapolis-in", "indianapolis website design", r"indianapolis|indiana"),
    "Sacramento": ("sacramento-ca", "website design sacramento", r"sacramento"),
    "Kansas City": ("kansas-city-mo", "kansas city website design", r"kansas city|^web design kansas$|^kansas web design$"),
    "Cleveland": ("cleveland-oh", "website design cleveland ohio", r"cleveland(?! tn)"),
}

U_BRAND = "names or reads like the name of another agency (other agencies' brand names are not used)"
U_CITE = "a citation-style question (Chicago style for citing a website), nothing to do with hiring a designer"
U_JOBS = "jobs, salary, pay or classes: a career search, not someone hiring a designer"
U_TRIVIA = "a generic web design definition, craft or trivia question with no city and no hiring intent"
U_PLACE = "a question about the city itself (location, safety, wealth, size, weather, shopping, addresses), not web design"
U_OTHER = "a different place with a similar name (San Luis Obispo, Cleveland TN), not this city"
U_GENERIC_COST = "a national cost question already answered by the cost guides; used only as a city FAQ where it fits"

UNUSED_RULES = [
    (r"spinx|duogeeks|web design group|agency coalition", U_BRAND),
    (r"cite a website", U_CITE),
    (r"jobs?\b|salary|paid|make per website|classes|still in demand", U_JOBS),
    (r"san luis obispo|cleveland tn", U_OTHER),
    (r"where's st louis|difference between st louis|is west end|designer stores|how wealthy|how large is vegas|what to wear|"
     r"design district address|iron district|clothing company", U_PLACE),
    (r"definition|description|explain|color codes|code examples|requirements|facts|size$|effects|card examples|"
     r"system examples|table examples|redesign examples|design website examples|who we are|how many web|will web design|"
     r"why website design matters|graphic design difference|how often should websites", U_TRIVIA),
]

# Generic question rows that a page uses as an FAQ (tab -> keywords).
FAQ_USE = {
    "San Diego": {"how much do web designers charge", "how much web design cost"},
    "Orlando": {"how much web design cost"},
    "Indianapolis": {"how much do web designers charge per hour", "how much web design cost", "web design rates"},
    "Las Vegas": {"how much do web designers charge per hour", "how much web design cost"},
    "Los Angeles": {"how much do web designers charge for a website", "how much web design cost"},
}


def rows_for(tab):
    if tab == "Cleveland":
        wb = openpyxl.load_workbook(RECHECK, read_only=True)
        rows = [r for r in list(wb["ALL"].iter_rows(values_only=True))[1:] if r[0]]
        return [r for r in rows if "cleveland" in (r[5] or "")]
    wb = openpyxl.load_workbook(NAT, read_only=True)
    return [r for r in list(wb[tab].iter_rows(values_only=True))[1:] if r[0]]


def classify(tab, kw):
    slug, target, pat = CITIES[tab]
    k = kw.lower().strip()
    if k == target:
        return ("target", None)
    for p, reason in UNUSED_RULES:
        if re.search(p, k):
            return ("unused", reason)
    if re.search(pat, k):
        return ("support", None)
    if k in FAQ_USE.get(tab, set()):
        return ("faq", None)
    if re.search(r"how much|rates|per hour|cost", k):
        return ("unused", U_GENERIC_COST)
    return (None, None)


def section():
    out = [HEAD, "", "Thirteen national city pages (CITY-PAGES-WAVE2.md, Oct 16 2026). Sources: "
           "keywords/Web-Design-National-Cities-Keywords.xlsx (one tab per city, Ubersuggest US) and "
           "keywords/Web-Design-5-Cities-Recheck.xlsx (Cleveland rows). Generated by `python3 scripts/keyword_plan_wave2.py` "
           "(run by scripts/keyword_plan.py), which fails if any 10+ keyword of a built city is unclassified. Every row "
           "with 10 or more searches a month is either on the page (target, supporting, or an FAQ question) or listed "
           "as unused with its reason.", ""]
    problems, totals = [], defaultdict(int)
    unused_all = defaultdict(list)
    for tab, (slug, target, _) in CITIES.items():
        rows = rows_for(tab)
        seen, tgt, sup, faq, low = set(), None, [], [], 0
        for kw, typ, vol, sd, cpc, seed in rows:
            k = kw.lower().strip()
            if k in seen:
                continue
            seen.add(k)
            vol = vol or 0
            if vol < 10:
                low += 1
                continue
            kind, reason = classify(tab, kw)
            if kind == "target":
                tgt = (kw, vol, sd)
            elif kind == "support":
                sup.append((kw, vol, sd, typ))
            elif kind == "faq":
                faq.append((kw, vol, sd))
            elif kind == "unused":
                unused_all[reason].append((kw, vol, sd, tab))
            else:
                problems.append((tab, kw, vol))
            totals[kind or "missing"] += 1
        if not tgt:
            problems.append((tab, f"TARGET NOT IN DATA: {target}", 0))
            continue
        out.append(f"### /web-design/{slug}.html")
        out.append("")
        out.append(f"Target: **{tgt[0]}** ({tgt[1]:,}/mo, SD {tgt[2]})")
        out.append("")
        if sup:
            sup.sort(key=lambda r: -r[1])
            out.append("Supporting: " + "; ".join(f"{r[0]} ({r[1]:,}, SD {r[2]})" for r in sup))
            out.append("")
        if faq:
            out.append("Used as FAQ questions: " + "; ".join(f"{r[0]} ({r[1]:,}, SD {r[2]})" for r in faq))
            out.append("")
        if low:
            out.append(f"Rows under 10/mo in this city's data: {low} (not required by the 10+ rule).")
            out.append("")
    n_assigned = totals["target"] + totals["support"] + totals["faq"]
    n_unused = totals["unused"]
    out.insert(2, f"**10+ rule result for the 13 cities:** {n_assigned + n_unused + totals['missing']} keywords at 10+; "
               f"**{n_assigned} on a page** (13 targets, {totals['support']} supporting, {totals['faq']} FAQ questions) and "
               f"**{n_unused} deliberately unused**. Unclassified: **{totals['missing']}**.\n")
    out += ["### Deliberately unused (10+ searches a month), Wave 2 cities", ""]
    for reason, items in sorted(unused_all.items(), key=lambda kv: -sum(r[1] for r in kv[1])):
        items.sort(key=lambda r: -r[1])
        out.append(f"**{reason}** ({len(items)} keywords): " + "; ".join(f"{r[0]} ({r[1]:,}, {r[3]} tab)" for r in items))
        out.append("")
    # Remaining candidates: cities in the files with no page yet.
    out += ["### Remaining national candidates (no page yet)", "",
            "Cities in the two national files that did not get a page in Wave 2. The strongest city-specific "
            "web design phrase for each (10+ searches a month, other agencies' names excluded):", "",
            "| City | Best keyword | Volume | SD |", "|---|---|---:|---:|"]
    wb = openpyxl.load_workbook(NAT, read_only=True)
    cand = []
    for tab in wb.sheetnames[1:]:
        if tab in CITIES:
            continue
        first = r"\b" + re.escape(tab.lower().split()[0]) + r"\b"
        best = None
        for kw, typ, vol, sd, cpc, seed in list(wb[tab].iter_rows(values_only=True))[1:]:
            if not kw or (vol or 0) < 10 or not re.search(first, kw.lower()) or not re.search(r"web|website", kw.lower()):
                continue
            if re.search(r"jobs?|salary|cite|group|coalition", kw.lower()):
                continue
            if not best or vol > best[1]:
                best = (kw, vol, sd)
        if best:
            cand.append((tab,) + best)
    wb2 = openpyxl.load_workbook(RECHECK, read_only=True)
    for city in ("Milwaukee", "Pittsburgh", "Greensboro", "Wichita"):
        best = None
        for kw, typ, vol, sd, cpc, seed in list(wb2["ALL"].iter_rows(values_only=True))[1:]:
            if kw and (vol or 0) >= 10 and city.lower() in kw.lower() and re.search(r"web|website", kw.lower()) \
                    and not re.search(r"jobs?|salary", kw.lower()):
                if not best or vol > best[1]:
                    best = (kw, vol, sd)
        if best:
            cand.append((city,) + best)
    for c in sorted(cand, key=lambda r: -r[2]):
        out.append(f"| {c[0]} | {c[1]} | {c[2]:,} | {c[3]} |")
    return "\n".join(out) + "\n", problems, totals


def main():
    text, problems, totals = section()
    plan = PLAN.read_text()
    i = plan.find("\n" + HEAD + "\n")
    if i >= 0:
        plan = plan[:i].rstrip() + "\n"
    PLAN.write_text(plan + "\n" + text)
    print(f"Wave 2: {dict(totals)}, {len(problems)} problems")
    for p in problems:
        print("UNCLASSIFIED", p)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
