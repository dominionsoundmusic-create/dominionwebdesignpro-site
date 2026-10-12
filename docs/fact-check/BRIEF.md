# Fact-check brief (independent checkers, Oct 12 2026)

You did not write any of the pages you check. Your job is to find every factual claim on your
assigned pages and verify it, then fix the page in place.

1. Read CLAUDE.md, INTAKE.md and docs/WRITING-GUIDE.md (the rules the writers followed), then the
   writer notes in docs/writers/ for your pages (they list each fact and the source the writer used).
2. For each assigned page (source file in src/pages/), list every non-obvious claim: numbers, dates,
   populations, rankings of cities, laws and rule numbers, agencies and organizations, chambers, SBDC
   and SCORE offices, street names, neighborhoods, corridors, employers, events, prices of third-party
   products, survey statistics, quotes, and anything stated about Dominion Web Design Pro.
3. Business claims must match INTAKE.md exactly (packages, prices, trials: Pro chat widget 14 days,
   Agency phone agent 7 days then $297/mo for up to 750 minutes, hosting $49/mo without the agent,
   AI receptionist wording, no clients, no reviews, no office outside Big Sandy, no ranking promises).
4. Verify the rest with WebSearch (WebFetch and curl are blocked here; verify from search results of
   the official or credible source, preferably restricting to that domain). Check that each cited
   source URL in the page's m.sources([...]) block is real and supports the claim.
5. For each claim: Confirmed, Corrected (fix the text), Softened (make it less specific to what you
   can confirm) or Removed (delete it if you cannot verify it). Fix the source file directly. Keep the
   page's rules intact: no em or en dashes, 3 to 6 FAQs, sources block, no banned words.
6. After editing, build into your own folder and check your pages:
   `python3 build.py --out /tmp/claude-0/<you>/dist && python3 scripts/check.py --skip-links --dist /tmp/claude-0/<you>/dist --only <url>`
7. Write docs/fact-check/<you>.md: a table per page with Claim | Verdict | Source | Action, and a
   summary line with counts (checked, confirmed, corrected, softened, removed).
Do not touch git. Do not edit shared files (templates, build.py, site.json, scripts).
