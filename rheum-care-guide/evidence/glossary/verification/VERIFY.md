# Independent verification of the glossary (read fully before starting)

## Context
A Taiwanese rheumatologist runs a public patient-education site, 風濕免疫生活照護圖解
(https://cheng1276.github.io/rheum-care-guide/). A glossary is being added: patients tap a term on the
site and see a short plain-language explanation (白話解釋 = "def", 例子 = "example", 補充 = "note") with its
PubMed-indexed sources. Another team drafted the entries. You are an independent checker: you did not
write them, and your job is to find every error before patients see them. Errors are unacceptable;
"probably fine" is not good enough.

## Inputs
- Entries: /home/claude/glossary/glossary.json → "entries" (fields: id, term, en, aliases, def, example,
  note, label, sources[], evidence[{quote, location, access, pmid, doi, pmcid, supports}], reviewer_notes).
  Check only the ids assigned to you.
- Where each alias appears on the site, with the full site sentence:
  /home/claude/glossary/occurrences.md ([LINK] = the occurrence that will become tappable; [repeat] = same
  term again in the same card/page, not linked; [excluded] = not linked on that page).
- Writing rules the drafters followed: /home/claude/glossary/PROTOCOL.md (section "Writing rules").
- Background evidence from the site's research phase (optional): /home/claude/research/*.md

## Tools
- Load PubMed tools first with ToolSearch:
  "select:mcp__PubMed__search_articles,mcp__PubMed__get_article_metadata,mcp__PubMed__get_full_text_article,mcp__PubMed__convert_article_ids,mcp__PubMed__lookup_article_by_citation"
- Large outputs are saved to a file; search them with python (json.load(f)['articles'][0]['full_text']
  for full text) or Grep. Normalise whitespace and quote characters when comparing.
- KNOWN PITFALL: PMC full-text extraction drops some formatted words (e.g. "against", "not",
  italic names, subscripts), leaving glued words. A quote that looks fine may hide a dropped "not":
  read the surrounding sentence before accepting a quote that supports a negative or a direction.
- WebFetch passes pages through a summarising model and may paraphrase. Quotes marked access "WebFetch"
  cannot be machine-checked: try to confirm them in the PubMed abstract or PMC full text; if you cannot,
  say so, and judge whether the Chinese text is still supported by other, verified quotes.
- The shell cannot reach NCBI or publisher sites; do not try curl/wget.

## For every assigned entry, check
1. Quotes: each evidence quote is verbatim (allowing whitespace/quote-mark/dash differences) in the
   cited article (PMC full text or PubMed abstract), and the location is right. Note any quote you
   could not find.
2. Citations: each source's PMID, DOI, first author, title, journal and year match PubMed metadata.
3. Support: every claim in def, example and note is supported by a verified quote — no added facts,
   numbers, mechanisms, examples or advice; the Chinese translation is faithful (no overstatement,
   no understatement, correct direction, correct population). Examples must appear in the quotes.
4. Fit with the site: the explanation matches how the site uses the term in every [LINK] and [repeat]
   sentence in occurrences.md, and does not contradict the site text. Flag any alias that is linked in a
   sentence where it means something else (wrong sense) or where the explanation would mislead.
5. Plain language: understandable for a Taiwanese lay reader (國中程度), Taiwan Traditional Chinese
   usage, no unexplained jargon, not condescending. def ideally ≤ 60 Chinese characters (max 90),
   example ≤ 40, note ≤ 50. Polite 您, not 你.
6. Safety: nothing that could lead a patient to change or stop medication on their own, delay care,
   or feel falsely reassured; emergencies stay clearly urgent.
7. Source quality: Tier 1 guideline/consensus > Tier 2 consensus definition paper > Tier 3 review.
   If a better (higher-tier) PubMed-indexed source clearly exists for a claim, say so (optional).

## Output
Write /home/claude/glossary/verify_<your group>.md:
- A summary line: counts of OK / minor / major.
- One section per entry: verdict (OK | minor | major), what you checked, each problem found, and for
  each problem an exact proposed replacement text (Chinese) plus the verbatim quote + PMID that supports
  the fix. "major" = factual error, unsupported claim, wrong source, misleading or unsafe wording;
  "minor" = wording, clarity, length, small precision issues.
Do NOT edit glossary.json or any site file. Keep your final reply ≤ 250 words: counts, the major
problems in one line each, and the report path.

## New entries (only if your assignment includes one)
Research it following PROTOCOL.md exactly (sources, quotes, writing rules) and write the entry as JSON to
/home/claude/glossary/new_<id>.json using the entry schema from PROTOCOL.md, plus two extra fields:
"cat" (category id given in your assignment) and "en" (clean English name). Validate the JSON.
