#!/usr/bin/env python3
"""CLAUDE.md final grep: banned strings in the built site's visible text, titles, meta and alt text.

Checks every built page (tool pages included) for em and en dashes (the one allowed exception is the
Jesse Duplantis credit line), the banned phrases, "unlimited pages", "100+", "guarantee", "#1",
"testimonial", "5-star", "(832)", "(928)" and "(689)". Script and style blocks and HTML comments are
not visible text and are skipped.

Usage: python3 scripts/grep_check.py [--dist dist]. Exit code 1 on any hit.
"""
import argparse
import html
import re
import sys
from pathlib import Path

PATS = ["—", "–", "your trusted partner", "one-stop solution", "look no further", "unmatched excellence",
        "we've got you covered", "cutting-edge", "elevate your", "in today's digital age", "unlimited pages", "100+",
        "guarantee", "#1", "testimonial", "5-star", "(832)", "(928)", "(689)"]


def visible(raw):
    vis = re.sub(r"(?s)<(script|style)[^>]*>.*?</\1>", " ", raw)
    vis = re.sub(r"(?s)<!--.*?-->", " ", vis)
    vis = html.unescape(re.sub(r"<[^>]+>", " ", vis)) + " " + " ".join(
        html.unescape(a) for a in re.findall(r'(?:content|alt|title|aria-label|placeholder)="([^"]*)"', raw))
    vis = re.sub(r"\s+", " ", vis)
    # the Duplantis credit is the one place a dash is allowed
    return re.sub(r"[—–]\s*Jesse Duplantis", "Jesse Duplantis", vis)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dist", default=str(Path(__file__).resolve().parent.parent / "dist"))
    dist = Path(ap.parse_args().dist)
    total = 0
    pages = {"/" + f.relative_to(dist).as_posix(): visible(f.read_text()) for f in sorted(dist.rglob("*.html"))}
    for p in PATS:
        hits = []
        for u, vis in pages.items():
            for m in re.finditer(re.escape(p), vis, re.I):
                hits.append(f"{u}: ...{vis[max(0, m.start()-50): m.end()+50]}...")
        total += len(hits)
        print(f"{p!r}: {len(hits)} hits")
        for h in hits[:8]:
            print("   ", h)
    print(f"\n{total} hits in total across {len(pages)} pages")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
