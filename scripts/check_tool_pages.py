#!/usr/bin/env python3
"""Prove the tool pages still work as on the live site.

For each tool page, every <script>...</script> block of the live-site version (docs/old-site/) must
appear byte for byte in the built page (dist/), so every endpoint and handler is unchanged. For every
form, the opening <form> tag (name, action, method, Netlify attributes) and every <input>, <textarea>,
<select>, <option> and <button> tag must be byte for byte the same and in the same order. Only visible
wording between tags may differ (dashes and one banned word were reworded on Oct 12 2026).

Usage: python3 scripts/check_tool_pages.py [--dist dist]   (exit 1 on any difference)
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OLD = ROOT / "docs" / "old-site"
TOOL_PAGES = ["demo.html", "demo-generator.html", "site-check/index.html", "compare/index.html", "tools/index.html",
              "intake/index.html", "intake/thanks/index.html", "contact/thanks/index.html"]


def blocks(raw):
    out = re.findall(r"(?s)<script\b.*?</script>", raw)
    for form in re.findall(r"(?s)<form\b.*?</form>", raw):
        out += re.findall(r"(?s)<(?:form|input|textarea|select|option|button)\b[^>]*>", form)
    return out


def fields(raw):
    return sorted(re.findall(r'<form\b[^>]*\bname="([^"]+)"', raw)), sorted(re.findall(r'<(?:input|textarea|select)\b[^>]*\bname="([^"]+)"', raw))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dist", default=str(ROOT / "dist"))
    dist = Path(ap.parse_args().dist)
    bad = 0
    for rel in TOOL_PAGES:
        old = (OLD / rel).read_text()
        new = (dist / rel).read_text()
        missing = [b for b in blocks(old) if b not in new]
        old_b, new_b = blocks(old), blocks(new)
        if not missing and old_b != new_b[:len(old_b)] and old_b != [b for b in new_b if b in old_b]:
            missing = ["(order changed)"]
        same_fields = fields(old) == fields(new)
        ok = not missing and same_fields
        bad += not ok
        print(f"{'OK  ' if ok else 'FAIL'} {rel}: {len(blocks(old))} script blocks and form tags unchanged={not missing}, "
              f"forms {fields(new)[0]} fields same={same_fields}")
        for b in missing:
            print("   changed block:", b[:120].replace("\n", " "))
    # the demo generator loads photos from /demo-images/<folder>/<n>.jpg
    imgs = list((dist / "demo-images").rglob("*.jpg"))
    old_imgs = [l for l in (OLD / "files.txt").read_text().split() if l.startswith("demo-images/")]
    missing_imgs = [l for l in old_imgs if not (dist / l).exists()]
    print(f"demo-images: {len(imgs)} photos in dist, {len(missing_imgs)} of the {len(old_imgs)} live files missing")
    bad += bool(missing_imgs)
    fn = ROOT / "netlify" / "functions" / "seo-audit.mjs"
    print("netlify/functions/seo-audit.mjs present:", fn.exists())
    bad += not fn.exists()
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
