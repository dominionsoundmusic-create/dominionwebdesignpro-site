#!/usr/bin/env python3
"""Every URL the live site has today must still work on the rebuilt site.

Old URLs come from the live site on main, saved in docs/old-site/: every file in its tree
(docs/old-site/files.txt, the `git ls-files` of main: pages, photos, demo-images, icons), every <loc>
in its sitemap.xml, and every non-wildcard source in its _redirects. Pages are checked in every form
Netlify Pretty URLs serves today: about.html at /about.html and /about, folder pages at /x/ and
/x/index.html. Each URL must either be served by a file in dist/ or be caught by a 301 rule in
dist/_redirects whose target exists in dist/.

Usage: python3 scripts/check_old_urls.py [--dist dist] [--report docs/qa-old-urls.md]
Exit code 1 if any old URL would 404.
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OLD = ROOT / "docs" / "old-site"
SKIP_PREFIX = ("CLAUDE.md", "INTAKE.md", "PLAYBOOK.md", "keywords/", "netlify/", "_redirects", "_headers")


def old_urls():
    urls = set(re.findall(r"<loc>https://dominionwebdesignpro\.com(/[^<]*)</loc>", (OLD / "sitemap.xml").read_text()))
    for rel in (OLD / "files.txt").read_text().split():
        if rel.startswith(SKIP_PREFIX):
            continue
        u = "/" + rel
        if u.endswith("/index.html"):
            urls.add(u)
            urls.add(u[: -len("index.html")])
        elif u == "/index.html":
            urls.update({"/", "/index.html"})
        else:
            urls.add(u)
            if u.endswith(".html"):
                urls.add(u[: -len(".html")])  # Pretty URLs form
    for line in (OLD / "_redirects").read_text().splitlines():
        parts = line.split()
        if parts and not parts[0].startswith("#") and "*" not in parts[0]:
            urls.add(parts[0])
    return sorted(urls)


def served(url, dist):
    p = dist / url.lstrip("/")
    if url == "/":
        return (dist / "index.html").exists()
    if url.endswith("/"):
        return (p / "index.html").exists()
    return p.is_file() or (dist / (url.lstrip("/") + ".html")).exists() or (p / "index.html").exists()


def rules(dist):
    out = []
    for line in (dist / "_redirects").read_text().splitlines():
        parts = line.split()
        if parts and not parts[0].startswith("#"):
            out.append((parts[0], parts[1], parts[2] if len(parts) > 2 else "301"))
    return out


def redirected(url, rs):
    for src, dst, code in rs:
        if src == url or ("*" in src and url.startswith(src.split("*")[0]) and url != src.split("*")[0]):
            return src, dst, code
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dist", default=str(ROOT / "dist"))
    ap.add_argument("--report", default="")
    args = ap.parse_args()
    dist = Path(args.dist)
    rs = rules(dist)
    rows, bad = [], 0
    for u in old_urls():
        if served(u, dist):
            # a served file wins over any rule without "!" on Netlify
            rows.append((u, "200", "served by a rebuilt page or file at the same path"))
            continue
        r = redirected(u, rs)
        if r and served(r[1], dist):
            rows.append((u, r[2], f"redirect to {r[1]} (rule {r[0]})"))
        else:
            bad += 1
            rows.append((u, "404", "NOT FOUND"))
    for u, code, how in rows:
        print(f"{code}  {u}  {how}")
    print(f"\n{len(rows)} old URLs checked, {bad} would 404")
    if args.report:
        lines = ["| Old URL | Result | How |", "|---|---|---|"] + [f"| {u} | {c} | {h} |" for u, c, h in rows]
        lines.append(f"\n{len(rows)} old URLs checked, {bad} would 404.")
        Path(args.report).write_text("\n".join(lines) + "\n")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
