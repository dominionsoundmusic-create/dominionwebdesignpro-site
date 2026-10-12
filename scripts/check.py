#!/usr/bin/env python3
"""Rule and SEO checks over the built site in dist/ (Dominion Web Design Pro).

Checks every built page for the hard rules in CLAUDE.md and INTAKE.md: banned phrases, invented
trust claims (reviews, testimonials, guarantees, rankings, years, job counts), em and en dashes
(except the Jesse Duplantis credit), eyebrow labels, the exact top-bar quote and John 3:16, GA4 with
phone-tap tracking, the EN/ES toggle and both social links on every page, the AI-receptionist
honesty rule, the package facts, the handwritten marker, SEO basics (one H1, unique title and
description, canonical, JSON-LD validity, 3 to 6 FAQs visible and in FAQPage JSON-LD, hero plus
two in-body images) and link/image integrity. Tool pages copied through from the live site (demo,
demo generator, Site Check, Before and After, tools, intake, thank-you pages) get the every-page
checks only; scripts/check_tool_pages.py proves their scripts and forms are unchanged.

Usage: python3 scripts/check.py [--dist DIR] [--only /pricing/]
Exit code 1 if any error is found.
"""
import argparse
import json
import re
import sys
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ORIGIN = "https://dominionwebdesignpro.com"
PHONE_TEL = "tel:+19036367511"
MARK = "dwdp:handwritten 2026-10-12"
QUOTE = "I believe the unbelievable, I receive the impossible, because it's doable."
GA = "G-3MZXMC1JKS"
TOOL_PAGES = {"/demo.html", "/demo-generator.html", "/site-check/", "/compare/", "/tools/", "/intake/", "/intake/thanks/",
              "/contact/thanks/"}
NO_FAQ = {"/404.html", "/privacy-policy.html", "/terms.html"}

BANNED = [
    # CLAUDE.md rule 9 filler phrases
    r"\byour trusted partner\b", r"\bone-stop solution\b", r"\blook no further\b", r"\bunmatched excellence\b",
    r"\bwe've got you covered\b", r"\bwe have got you covered\b", r"\bcutting-edge\b", r"\belevate your\b",
    r"\bin today's digital age\b",
    # CLAUDE.md final grep and rule 1: invented trust claims and promises
    r"\bunlimited pages\b", r"\bunlimited\b", r"100\+", r"\bguarantee", r"#1\b", r"\btestimonial", r"\b5[- ]star", r"\bfive[- ]star",
    r"\(832\)", r"\(928\)", r"\(689\)", r"\baward[- ]winning\b", r"\byears of experience\b", r"\btop[- ]rated\b",
    r"\bnumber one\b", r"\bcertified\b", r"\bhappy (?:clients|customers)\b", r"\bour clients\b", r"\bclients say\b",
    r"\bsites? (?:we|I) (?:have )?built for\b", r"\bwe have built for\b", r"\bhundreds of\b", r"\bthousands of (?:clients|businesses|sites)\b",
    r"\brank(?:s|ed)? (?:you )?(?:#|number|first|on page one|on the first page)\b(?![^.]*\b(?:no|not|nobody|cannot|can't|never)\b)",
    # INTAKE: never say a human always answers
    r"\b(?:a )?(?:real )?(?:person|human) (?:always )?answers\b", r"\balways (?:talk|speak) to a (?:real )?(?:person|human)\b",
    # leftovers from the build system this site was copied from
    r"\bPhoenix Pool\b", r"\bpool (?:service|cleaning|repair)\b", r"\(623\)", r"\bROC license\b",
    # retired live-site claims that INTAKE.md does not support
    r"\bthree-month minimum\b", r"\bten months instead of twelve\b", r"\bDominion Solar\b",
]


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.text = []
        self.skip = 0
        self.h1 = 0
        self.title = ""
        self._in_title = False
        self.meta = {}
        self.links = []
        self.imgs = []
        self.ids = []
        self.canonical = None
        self.jsonld = []
        self._in_ld = False
        self._ld = ""
        self.headings = []
        self._h = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.append(a["id"])
        if tag in ("script", "style"):
            self.skip += 1
            if tag == "script" and a.get("type") == "application/ld+json":
                self._in_ld = True
                self._ld = ""
        if tag == "title":
            self._in_title = True
        if tag == "h1":
            self.h1 += 1
        if tag in ("h1", "h2", "h3", "h4"):
            self._h = [tag, ""]
        if tag == "meta":
            k = a.get("name") or a.get("property")
            if k:
                self.meta[k] = a.get("content", "")
        if tag == "link" and a.get("rel") == "canonical":
            self.canonical = a.get("href")
        if tag == "a":
            self.links.append(a.get("href"))
        if tag == "img":
            self.imgs.append(a)

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip -= 1
            if self._in_ld:
                self.jsonld.append(self._ld)
                self._in_ld = False
        if tag == "title":
            self._in_title = False
        if self._h and tag == self._h[0]:
            self.headings.append((self._h[0], self._h[1].strip()))
            self._h = None

    def handle_data(self, data):
        if self._in_ld:
            self._ld += data
        if self._in_title:
            self.title += data
        if self._h:
            self._h[1] += data
        if not self.skip:
            self.text.append(data)


FLAT = set()  # every flat page keeps its .html URL


def url_of(path, dist):
    rel = path.relative_to(dist).as_posix()
    if rel == "index.html":
        return "/"
    if not rel.endswith("/index.html"):
        # pages the live site served without .html keep that URL (/pool-repair)
        return "/" + rel
    return "/" + rel[: -len("index.html")]


def resolve(href, dist):
    href = href.split("#")[0].split("?")[0]
    if not href:
        return True
    if href.startswith(ORIGIN):
        href = href[len(ORIGIN):] or "/"
    p = dist / href.lstrip("/")
    if href.endswith("/"):
        return (p / "index.html").exists()
    # flat live URLs (/pool-repair) are served from pool-repair.html
    return p.exists() or (dist / (href.lstrip("/") + ".html")).exists()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dist", default=str(ROOT / "dist"))
    ap.add_argument("--only", default="")
    ap.add_argument("--skip-links", action="store_true", help="ignore links to pages not built yet")
    args = ap.parse_args()
    dist = Path(args.dist).resolve()
    errors, warnings = [], []
    titles, descs = defaultdict(list), defaultdict(list)
    files = sorted(dist.rglob("*.html"))
    sitemap = (dist / "sitemap.xml").read_text() if (dist / "sitemap.xml").exists() else ""
    for f in files:
        url = url_of(f, dist)
        if args.only and not url.startswith(args.only):
            continue
        raw = f.read_text()
        p = PageParser()
        p.feed(raw)
        text = re.sub(r"\s+", " ", " ".join(p.text))
        noindex = 'name="robots" content="noindex' in raw

        def err(msg):
            errors.append(f"{url}: {msg}")

        def warn(msg):
            warnings.append(f"{url}: {msg}")

        # every page, tool pages included
        if MARK not in raw[:4096]:
            err("dwdp:handwritten marker missing from the first 4KB")
        if GA not in raw or "phone_call_click" not in raw:
            err("GA4 or phone-tap tracking missing")
        if 'class="dlang' not in raw:
            err("EN/ES toggle missing")
        if "facebook.com/dominionwebdesignpro" not in raw or "youtube.com/@DominionWebDesignPro" not in raw:
            err("social links missing")
        if "John 3:16" not in raw or "Jesse Duplantis" not in raw:
            err("John 3:16 or the Duplantis quote missing")
        if url in TOOL_PAGES:
            continue

        # hard copy rules (visible text + title + meta + alt text)
        alts = " ".join(i.get("alt") or "" for i in p.imgs)
        visible = text + " " + p.title + " " + p.meta.get("description", "") + " " + alts
        for pat in BANNED:
            for mt in re.finditer(pat, visible, re.I):
                ctx = visible[max(0, mt.start() - 50): mt.end() + 50]
                err(f"banned phrase /{pat}/ in: ...{ctx}...")
        dash_text = visible.replace("\u2014\u00a0Jesse Duplantis", "").replace("\u2014 Jesse Duplantis", "")
        for mt in re.finditer("[\u2014\u2013]", dash_text):
            err(f"em/en dash in: ...{dash_text[max(0, mt.start()-40): mt.end()+40]}...")
        for mt in re.finditer(r"[^.]*\b(?:phone|AI) agent\b[^.]*\.", visible, re.I):
            if re.search(r"14 days|fourteen days", mt.group(0), re.I) and not re.search(r"chat", mt.group(0), re.I):
                err(f"AI phone agent trial is 7 days, not 14: {mt.group(0).strip()[:160]}")
        for mt in re.finditer(r"[^.]*\bchat widget\b[^.]*\.", visible, re.I):
            if re.search(r"\b7 days|seven days", mt.group(0), re.I) and not re.search(r"phone", mt.group(0), re.I):
                err(f"AI chat widget trial is 14 days, not 7: {mt.group(0).strip()[:160]}")
        for mt in re.finditer(r"\$\s?(\d[\d,]*)", visible):
            pass
        if re.search(r'class="[^"]*(?:eyebrow|kicker|overline|badge)', raw):
            err("eyebrow/badge label found")
        if QUOTE not in raw.replace("&#39;", "'").replace("&rsquo;", "'"):
            err("top-bar quote missing or not exact")
        if "Dominion Digital Group" not in raw:
            err("footer d/b/a line missing")
        if "AI receptionist" not in visible:
            err("AI receptionist note missing")
        if "lorem" in visible.lower() or "TODO" in visible or "PHONE_" in raw or "UNKNOWN" in visible:
            err("placeholder text")
        if re.search(r"\b(?:our|the) office in (?!Big Sandy)", visible, re.I):
            err("implies an office outside Big Sandy")

        # SEO basics
        if p.h1 != 1:
            err(f"expected exactly one h1, found {p.h1}")
        if not p.title.strip():
            err("missing title")
        if len(p.title) > 70:
            warn(f"title is {len(p.title)} chars: {p.title}")
        d = p.meta.get("description", "")
        if not d:
            err("missing meta description")
        elif not (110 <= len(d) <= 170):
            warn(f"meta description is {len(d)} chars")
        titles[p.title].append(url)
        descs[d].append(url)
        if url != "/404.html" and not noindex:
            if p.canonical != ORIGIN + url:
                err(f"canonical {p.canonical} != {ORIGIN + url}")
            if f"<loc>{ORIGIN}{url}</loc>" not in sitemap:
                err("indexable page missing from sitemap.xml")
        if noindex and f"<loc>{ORIGIN}{url}</loc>" in sitemap:
            err("noindex page listed in sitemap")
        # images: hero plus at least two in-body figures on every content page
        figs = raw.count('<figure class="fig')
        has_hero = '<section class="hero ' in raw
        if url not in NO_FAQ and (not has_hero or figs < 2):
            err(f"needs a hero and at least two in-body images (hero={has_hero}, body images={figs})")
        for k in ("og:title", "og:description", "og:url", "og:image"):
            if not p.meta.get(k):
                err(f"missing {k}")
        if p.meta.get("og:image") and not p.meta["og:image"].startswith("https://"):
            err("og:image not absolute")
        # JSON-LD
        if len(p.jsonld) > 1:
            err("more than one JSON-LD block")
        faq_count = 0
        for block in p.jsonld:
            try:
                data = json.loads(block)
            except json.JSONDecodeError as e:
                err(f"invalid JSON-LD: {e}")
                continue
            types = [g.get("@type") for g in data.get("@graph", [])]
            if len(types) != len(set(types)):
                err(f"duplicate JSON-LD types: {types}")
            for g in data.get("@graph", []):
                if g.get("@type") == "FAQPage":
                    faq_count = len(g["mainEntity"])
        visible_faq = raw.count('class="faq__item"')
        if visible_faq != faq_count:
            err(f"visible FAQ items ({visible_faq}) != FAQPage entries ({faq_count})")
        max_faq = 6
        if url not in NO_FAQ:
            if not (3 <= visible_faq <= max_faq):
                err(f"page needs 3 to 6 common questions, has {visible_faq}")
            if 'id="faq-title">Common questions<' not in raw:
                err("visible 'Common questions' block missing")
            if faq_count == 0:
                err("FAQPage JSON-LD missing")
        # headings order
        last = 1
        for tag, label in p.headings:
            lvl = int(tag[1])
            if lvl > last + 1:
                warn(f"heading jumps from h{last} to {tag}: {label[:50]}")
            last = lvl
        # links and images
        for href in p.links:
            if href is None or href.strip() in ("", "#"):
                err("empty href")
                continue
            if href.startswith(("tel:", "mailto:", "http://", "https://", "javascript:")) and not href.startswith(ORIGIN):
                if href.startswith("tel:") and href != PHONE_TEL:
                    err(f"unexpected phone link {href}")
                continue
            if not resolve(href, dist):
                if not args.skip_links:
                    err(f"broken internal link {href}")
            elif href.startswith("/") and not href.split("#")[0].endswith(("/", ".html", ".xml", ".txt", ".svg", ".jpg", ".png", ".pdf")) \
                    and not (dist / (href.split("#")[0].lstrip("/") + ".html")).exists():
                warn(f"internal link without trailing slash {href}")
        if url not in ("/404.html",):
            for m_img in re.finditer(r'<figure class="fig[^"]*">(?:<picture>.*?</source>?)?.*?<img ([^>]*)>', raw, re.S):
                if 'loading="lazy"' not in m_img.group(1):
                    err("in-body figure image without loading=lazy")
        for im in p.imgs:
            src = im.get("src", "")
            if not im.get("alt") and im.get("alt") != "":
                err(f"img missing alt: {src}")
            if not im.get("width") or not im.get("height"):
                err(f"img missing width/height: {src}")
            if src.startswith("/") and not (dist / src.lstrip("/")).exists():
                err(f"missing image file {src}")
        dup_ids = {i for i in p.ids if p.ids.count(i) > 1}
        if dup_ids:
            err(f"duplicate ids: {sorted(dup_ids)}")
        words = len(text.split())
        body_type = re.search(r'<body class="type-([a-z]+)', raw)
        if body_type and body_type.group(1) in ("service", "guide", "area") and words < 1800:
            warn(f"only {words} words on page (including template)")

    for t, urls in titles.items():
        if len(urls) > 1:
            errors.append(f"duplicate title '{t}' on {urls}")
    for d, urls in descs.items():
        if len(urls) > 1 and d:
            errors.append(f"duplicate description on {urls}")

    # _redirects: every target must exist, and no rule may shadow a real page
    red = dist / "_redirects"
    if args.skip_links:
        pass
    elif red.exists():
        for line in red.read_text().splitlines():
            parts = line.split()
            if not parts or parts[0].startswith("#"):
                continue
            src, dst = parts[0], parts[1]
            if not resolve(dst, dist):
                errors.append(f"_redirects: target {dst} does not exist (from {src})")
            if "*" not in src and src != "/" and resolve(src, dist) and not src.endswith(".html"):
                errors.append(f"_redirects: rule {src} shadows a real page")
            # Netlify serves an existing file before applying a rule that has no "!" (force), so a
            # wildcard never hides a real page; a forced rule would.
            if len(parts) > 2 and parts[2].endswith("!"):
                errors.append(f"_redirects: forced rule {src} would hide real pages")
    else:
        errors.append("dist/_redirects missing")
    errors = list(dict.fromkeys(errors))
    for w in warnings:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    print(f"\n{len(files)} pages checked, {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
