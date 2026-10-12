#!/usr/bin/env python3
"""Atlanta add-on keyword plan (Oct 12 2026).

Classifies every keyword in keywords/Atlanta-Web-Design-Keywords.xlsx (ALL tab, Ubersuggest US,
pulled Oct 12 2026) and rewrites the "## Atlanta add-on" section at the end of docs/keyword-plan.md.

Maurice's 10+ rule: every keyword with 10 or more searches a month is assigned to a page (target or
supporting) or listed as unused with a one-line reason. Exits 1 if any 10+ keyword is unclassified or
a page target is missing from the data. scripts/keyword_plan.py runs this automatically after it
rewrites the main plan.

Usage: python3 scripts/keyword_plan_atlanta.py
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent
PLAN = ROOT / "docs" / "keyword-plan.md"
HEAD = "## Atlanta add-on"

PAGES = {
    "black-owned": "/black-owned-web-design/",
    "atlanta": "/web-design/atlanta-ga.html",
    "decatur": "/web-design/decatur-ga.html",
    "mcdonough": "/web-design/mcdonough-ga.html",
    "conyers": "/web-design/conyers-ga.html",
    "douglasville": "/web-design/douglasville-ga.html",
    "lawrenceville": "/web-design/lawrenceville-ga.html",
    "east-texas": "/web-design/east-texas.html",
    "g-cost": "/small-business-website-cost.html",
    "g-designer": "/how-much-does-a-website-designer-cost/",
    "g-builder": "/website-builder-vs-web-designer/",
    "g-need": "/why-small-businesses-need-a-website/",
}

TARGETS = {
    "black owned web developers": "black-owned",
    "web design company atlanta": "atlanta",
    "web design decatur ga": "decatur",
    "web design mcdonough ga": "mcdonough",
    "web design conyers ga": "conyers",
    "web design douglasville ga": "douglasville",
}

U_GOV = "someone looking for a city or county government's own website, not hiring a designer"
U_JOBS = "jobs, pay, training or whether web design is a good career: no hiring intent"
U_LOOKALIKE = "a look-alike phrase about something else (lighting, stone, TV shows, parks, home builders, GIS maps, other companies)"
U_BRAND = "names another agency (CLAUDE.md: other agencies' brand names are not used)"
U_TRIVIA = "trivia or craft questions about the industry, not someone hiring a designer"
U_GA_WAVE2 = "a Georgia city with no page yet: Atlanta wave 2 candidate (see the table below)"
U_OUT = "a U.S. city or state outside Texas and Georgia: national Wave 2 candidate, not built in this run"
U_OFF = "off-topic for this business"
U_AMBIG = "ambiguous place name (Clayton, NC and Clayton, MO as well as Clayton County, GA, whose own seed showed 0): no page this run"
U_LOW = "under 10 searches a month and no page fits it (the 10+ rule does not require it)"

RULES = [  # (regex, page key or ("unused", reason)); first match wins
    (r"^web design clayton$", ("unused", U_AMBIG)),
    (r"^(clayton county website|henry county website|clayton website|lithonia website)$", ("unused", U_GOV)),
    (r"m16 marketing", ("unused", U_BRAND)),
    (r"william webb|^how mcdonough$|^mcdonough we$", ("unused", U_LOOKALIKE)),
    (r"jobs?\b|salary|paid|make$|training|colleges?|class\b|code examples|in demand|work from home|happy|obsolete|replaced", ("unused", U_JOBS)),
    (r"^black owned (web|website|internet)|^what brands are black owned", "black-owned"),
    (r"black owned", ("unused", U_OFF)),
    (r"atlanta", "atlanta"),
    (r"^(web design georgia|web design ga|web design in georgia|website design georgia|website development georgia)$", "atlanta"),
    (r"decatur ga|dekalb county", "decatur"),
    (r"mcdonough|henry county ga$", "mcdonough"),
    (r"conyers", "conyers"),
    (r"douglasville|^douglas web design$", "douglasville"),
    (r"lawrenceville|gwinnett", "lawrenceville"),
    (r"web design east texas", "east-texas"),
    (r"per hour", "g-designer"),
    (r"how much (is )?(web|website) design cost|how much web design cost|how much website design cost", "g-cost"),
    (r"which website creator is best", "g-builder"),
    (r"why website design matters|why is web design important for business", "g-need"),
    (r"lithonia|design a stone|designed stone|stone web|stone website|riverdale|forest|morrow design|clay web design|clayton (web )?design|"
     r"clayton home|webgis|web gis|designs by henry|south fulton development|east point company|neighborhood park|webb|when web|"
     r"web fair|web design union$|union website design|web design unit$|web design decal|southern web design|will web design", ("unused", U_LOOKALIKE)),
    (r"how many web|how web design goes|requirements|web design size|why city design|what website design software|why webflow", ("unused", U_TRIVIA)),
    (r"macon|marietta|athens ga|buford ga|kennesaw|columbus ga|gainesville ga|^web design gainesville$", ("unused", U_GA_WAVE2)),
    (r"web design (kc|kansas city mo|greensboro|fort myers|chattanooga|iowa city|winston salem|fairfax|deland|quad cities|eau claire|"
     r"st george utah|st george ut|missouri|wilson nc|south carolina|erie pa|south florida|fairfield ct|fairfield|hendersonville nc|kansas|"
     r"cleveland tn|park city|ellsworth)$|web design company jacksonville fl|clayton nc web design|website design jonesboro ar", ("unused", U_OUT)),
]

ZERO_CITIES = ["South Fulton", "College Park", "East Point", "Union City", "Fairburn", "Stonecrest", "Lithonia",
               "Stockbridge", "Riverdale", "Jonesboro", "Morrow", "Forest Park"]


def classify(kw):
    k = kw.lower().strip()
    if k in TARGETS:
        return TARGETS[k]
    for pat, dest in RULES:
        if re.search(pat, k):
            return dest
    return None


def section():
    wb = openpyxl.load_workbook(ROOT / "keywords" / "Atlanta-Web-Design-Keywords.xlsx", read_only=True)
    rows = [r for r in list(wb["ALL"].iter_rows(values_only=True))[1:] if r[1]]
    seeds = {r[0] for r in rows}
    by_page, unused, low_unused, missing, found = defaultdict(list), defaultdict(list), defaultdict(int), [], set()
    seen = set()
    for seed, kw, typ, vol, sd, cpc, pd in rows:
        vol = vol or 0
        k = kw.lower().strip()
        if k in seen:
            continue
        seen.add(k)
        if k in TARGETS:
            found.add(k)
        dest = classify(kw)
        if dest is None:
            if vol >= 10:
                missing.append((kw, vol))
                continue
            dest = ("unused", U_LOW)
        if isinstance(dest, tuple):
            if vol >= 10:
                unused[dest[1]].append((kw, vol, sd))
            else:
                low_unused[dest[1]] += 1
        else:
            by_page[dest].append((kw, vol, sd, k in TARGETS))
    for t in TARGETS:
        if t not in found:
            missing.append((f"TARGET NOT IN DATA: {t}", 0))
    n = len(seen)
    n10 = sum(1 for p in by_page.values() for r in p if r[1] >= 10) + sum(len(v) for v in unused.values()) + \
        len([m for m in missing if m[1] >= 10])
    a10 = sum(1 for p in by_page.values() for r in p if r[1] >= 10)
    u10 = sum(len(v) for v in unused.values())
    out = [HEAD, "",
           f"Source: keywords/Atlanta-Web-Design-Keywords.xlsx, ALL tab (Ubersuggest, United States, pulled Oct 12 2026): "
           f"{len(seeds)} seed tabs, {n} unique keywords, {n10} with 10 or more searches a month. Generated by "
           "`python3 scripts/keyword_plan_atlanta.py` (run automatically by scripts/keyword_plan.py), which fails if any "
           "10+ keyword is left unclassified.", "",
           f"**10+ rule result:** of the {n10} keywords with 10+ searches a month, **{a10} are assigned to a page** and "
           f"**{u10} are listed below as deliberately unused**, each with its reason. Unclassified: "
           f"**{len([m for m in missing if m[1] >= 10])}**.", "",
           "Seed keywords such as \"black owned web design atlanta\", \"web design dekalb county\" and \"web design henry "
           "county ga\" show no measured volume of their own; they are used as supporting phrases on the pages named below.", "",
           "### Keywords by page (Atlanta add-on)", ""]
    for key, url in PAGES.items():
        items = sorted(by_page.get(key, []), key=lambda r: (not r[3], -r[1]))
        if not items:
            continue
        out.append(f"#### {url}")
        out.append("")
        tgt = [r for r in items if r[3]]
        if tgt:
            out.append(f"Target: **{tgt[0][0]}** ({tgt[0][1]:,}/mo, SD {tgt[0][2]})")
            out.append("")
        sup = [r for r in items if not r[3] and r[1] >= 10]
        if sup:
            out.append("Supporting: " + "; ".join(f"{r[0]} ({r[1]:,}, SD {r[2]})" for r in sup))
            out.append("")
        lows = [r for r in items if not r[3] and r[1] < 10]
        if lows:
            out.append(f"Also covers {len(lows)} lower-volume variants (under 10/mo), e.g. " + "; ".join(r[0] for r in lows[:6]) + ".")
            out.append("")
    out += ["### Deliberately unused (10+ searches a month), Atlanta add-on", ""]
    for reason, items in sorted(unused.items(), key=lambda kv: -sum(r[1] for r in kv[1])):
        items.sort(key=lambda r: -r[1])
        out.append(f"**{reason}** ({len(items)} keywords, {sum(r[1] for r in items):,} searches/mo): " +
                   "; ".join(f"{r[0]} ({r[1]:,})" for r in items))
        out.append("")
    out += ["### Atlanta wave 2 candidates: Georgia cities with 10+ searches and no page yet", "",
            "| Keyword | Volume | SD |", "|---|---:|---:|"]
    for kw, vol, sd in sorted(unused.get(U_GA_WAVE2, []), key=lambda r: -r[1]):
        out.append(f"| {kw} | {vol:,} | {sd} |")
    out += ["", "### Atlanta wave 2 (0 measured volume)", "",
            "Each of these Atlanta-area cities had its own seed tab and showed 0 searches a month for \"web design <city> ga\" "
            "in this pull, so none gets a page in this run (ATLANTA-ADDON.md): " + ", ".join(ZERO_CITIES) + ". "
            "\"web design clayton county\" also showed 0; \"clayton county website\" (140) and \"henry county website\" (110) "
            "are people looking for the county government's own site and are listed as unused above.", "",
            "### Under 10 searches a month (summary)", ""]
    for reason, c in sorted(low_unused.items(), key=lambda kv: -kv[1]):
        out.append(f"- {reason}: {c}")
    return "\n".join(out) + "\n", missing, (n, n10, a10, u10)


def main():
    text, missing, (n, n10, a10, u10) = section()
    plan = PLAN.read_text()
    i = plan.find(HEAD)
    if i >= 0:
        plan = plan[:i].rstrip() + "\n"
    PLAN.write_text(plan + "\n" + text)
    print(f"Atlanta add-on: {n} keywords, {n10} at 10+: {a10} assigned, {u10} unused, {len(missing)} problems")
    for m in missing:
        print("UNCLASSIFIED", m)
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
