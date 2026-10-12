#!/usr/bin/env python3
"""One-time patch of the tool pages copied through from the live site (run Oct 12 2026).

The tool pages (demo, demo generator, Site Check, Before and After, tools, intake, thank-you
pages) are copied byte for byte from main into src/static/. Their scripts, forms, form names, field
names and endpoints are not touched. Only these static HTML additions are made, so every page carries
what CLAUDE.md asks for on every page:
  1. the `dwdp:handwritten 2026-10-12` marker comment after the doctype;
  2. "John 3:16" at the left of the existing social strip, if the page lacks it;
  3. the Jesse Duplantis quote line under the page's own nav, if the page lacks it;
  4. the branded EN/ES language bar the other tool pages already carry, if the page lacks it
     (intake, intake thanks, contact thanks).
scripts/check_tool_pages.py proves every <script> and <form> block is unchanged.
Idempotent: running it twice changes nothing.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATIC = ROOT / "src" / "static"
TOOL_PAGES = ["demo.html", "demo-generator.html", "site-check/index.html", "compare/index.html", "tools/index.html",
              "intake/index.html", "intake/thanks/index.html", "contact/thanks/index.html"]
MARK = "<!-- dwdp:handwritten 2026-10-12 -->"
QUOTE = ('<div class="dwdp-quote" style="background:#0a1628;border-bottom:1px solid rgba(201,168,76,.3);padding:9px 22px;'
         'text-align:center"><p style="font-size:.85em;color:#eae4d8;font-style:italic;margin:0">&ldquo;I believe the '
         'unbelievable, I receive the impossible, because it&rsquo;s doable.&rdquo; <span style="color:#c9a84c;'
         'font-style:normal;font-weight:700">&mdash; Jesse Duplantis</span></p></div>')
VERSE = '<span class="dwdp-verse" style="float:left;font-weight:700;letter-spacing:.08em;font-size:.78rem;line-height:26px">John 3:16</span>'


def lang_bar():
    raw = (STATIC / "demo.html").read_text()
    start = raw.index("<style>#lang-bar")
    return raw[start:raw.rindex("</body>")]


def main():
    bar = lang_bar()
    for rel in TOOL_PAGES:
        p = STATIC / rel
        raw = p.read_text()
        out = raw
        if MARK not in out:
            m = re.match(r"(?i)<!doctype html>\s*\n?", out)
            out = (out[:m.end()] + MARK + "\n" + out[m.end():]) if m else MARK + "\n" + out
        if "John 3:16" not in out:
            out = re.sub(r'(<div class="dwdp-social-strip"[^>]*>)', lambda m: m.group(1) + VERSE, out, count=1)
        if "Duplantis" not in out:
            i = out.index("</nav>") + len("</nav>")
            out = out[:i] + "\n" + QUOTE + out[i:]
        if 'class="dlang' not in out:
            i = out.rindex("</body>")
            out = out[:i] + bar + out[i:]
        if out != raw:
            p.write_text(out)
            print("patched", rel)


if __name__ == "__main__":
    main()
