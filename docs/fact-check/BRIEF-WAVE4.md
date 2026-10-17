# Fact-check brief, Wave 4 (Oct 17 2026)

Follow docs/fact-check/BRIEF.md in full (you did not write these pages; find every factual claim, verify it with
WebSearch, fix the source file in place: Confirmed, Corrected, Softened or Removed). Additions for Wave 4:

- Writer notes: docs/writers/w4-<batch>.md (each fact with the URL the writer used, plus the claims the writer
  flagged as weakest: check those first). The writer brief is docs/writers/BRIEF-WAVE4.md.
- Weak sources (real-estate blogs, moving-company guides, property listings, map sellers, job postings, Wikipedia
  without a better source behind it): replace with an official or reputable source, or soften or cut the claim.
- Check every cited URL is real and supports the claim. Remove a source from m.sources([...]) if no claim rests on it.
- Business claims must match INTAKE.md exactly (see BRIEF.md point 3). "Made-up example" owners are fine only if the
  page clearly labels them as illustrations, never as clients.
- Alt text must describe what the photo shows (open each image with Read; files are in src/static/) and must not claim
  a photo shows the city unless it is the real city photo from images/cities/.
- Keep the page within the rules: no em or en dashes, 3 to 6 FAQs, no banned words, `m.no_office` once, similarity
  under 15% (run `python3 scripts/similarity.py --dist /tmp/claude-0/<you>/dist` after edits).
- Build only into your own folder: `python3 build.py --out /tmp/claude-0/<you>/dist`, then
  `python3 scripts/check.py --skip-links --dist /tmp/claude-0/<you>/dist --only <url>` for each page: 0 errors.
- Write docs/fact-check/<you>.md: a table per page (Claim | Verdict | Source | Action) and a summary line per page
  (checked, confirmed, corrected, softened, removed). Do not touch git or shared files (templates, build.py,
  site.json, scripts, other pages than yours unless your assignment says so).
- Final report: per page counts, notable corrections, anything you could not settle.
