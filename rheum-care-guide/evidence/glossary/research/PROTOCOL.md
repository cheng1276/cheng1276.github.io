# Glossary protocol: sourced plain-language definitions (read fully before starting)

## Purpose
A Taiwanese rheumatologist runs a public patient-education website, 風濕免疫生活照護圖解
(https://cheng1276.github.io/rheum-care-guide/). Patients may not understand some words on the
site (e.g. 有氧運動). For each assigned term you must (1) find an authoritative definition in a
PubMed-indexed source, quote it verbatim, and (2) draft a short plain-language Traditional
Chinese explanation that says no more than the quote supports. Errors are unacceptable.

## Inputs
- Your term list with the exact site sentences where each term appears:
  /home/claude/glossary/context_<group>.md  (the definition must fit how the site uses the term)
- Existing evidence notes from the site's research phase (many definitions are already quoted
  there; reuse them when they fit, but re-confirm the quote in the original):
  /home/claude/research/{gout,urticaria,ra,axspa,sle,sjogren,common}.md
- Site content with all source citations: /home/claude/cheng1276.github.io/rheum-care-guide/src/content/*.json

## Source rules (in order of preference)
1. A definition stated in a clinical guideline / consensus that the site already cites
   (e.g. WHO 2020 physical activity guidelines in BJSM, ACR 2022 RA integrative guideline,
   2026 international urticaria guideline, WAO 2020 anaphylaxis guidance, BSR 2026 SLE,
   BSR 2024/25 Sjögren, EULAR 2020 Sjögren, ASAS-EULAR 2022, ACR/SAA/SPARTAN 2015/2019,
   ACR 2022 vaccine guideline, ACR 2022 glucocorticoid-induced osteoporosis guideline).
2. A PubMed-indexed consensus definition or nomenclature paper (e.g. terminology consensus,
   standardisation of nomenclature, definition workshops), or another current guideline.
3. A PubMed-indexed systematic review, Cochrane review, or authoritative review in a major
   journal that explicitly defines the term.
Every source must be PubMed-indexed (record PMID and DOI from mcp__PubMed__get_article_metadata).
Do not use Wikipedia, commercial sites, patient forums, or general web pages.

## Tools
- Load PubMed tools first with ToolSearch:
  "select:mcp__PubMed__search_articles,mcp__PubMed__get_article_metadata,mcp__PubMed__get_full_text_article,mcp__PubMed__convert_article_ids,mcp__PubMed__lookup_article_by_citation"
- Prefer quotes you can read in PMC full text (get_full_text_article) or in the PubMed abstract;
  those are machine-checkable. Large outputs are saved to a file: search them with python
  (json.load(f)['articles'][0]['full_text']) or Grep.
- WebFetch passes pages through a summarising model and may paraphrase: use it only as a last
  resort, request verbatim short segments, and mark access as "WebFetch".
- KNOWN PITFALL: PMC full-text extraction drops formatted words (e.g. "against", "not"),
  leaving glued words such as "recommendedfor". Never rely on a quote with glued words.

## Writing rules for the Chinese explanation
- 台灣繁體中文，病友看得懂（國中程度），不用術語解釋術語；若不得不用，順便說明。
- "def": 1–2 short sentences, ideally ≤ 60 Chinese characters, never more than 90.
- "example": optional, ≤ 40 characters, and ONLY examples that appear in your quotes.
- "note": optional caution or clarification that a quote supports (≤ 50 characters).
- Say only what the quotes support. No extra facts, numbers, mechanisms or advice from memory.
- Must fit the site's usage of the term (see the context sentences) and must not contradict
  the site text. If the site's wording is inaccurate for this term, say so in reviewer_notes.
- No brand names. Generic drug names only if the quote contains them.
- Organisations: give the English full name exactly as printed in a PubMed-indexed publication
  by that organisation, plus a short descriptive Chinese gloss (e.g. 「美國的風濕病醫學會」).
  Do not invent an "official" Chinese name; if you translate, it is a description.
- If no adequate PubMed-indexed definition exists, set "status":"no_source" and explain; do not
  write a definition from memory.

## Output: write valid UTF-8 JSON to /home/claude/glossary/research_<group>.json
{
 "group": "<group>",
 "entries": [
  {
   "id": "<term id from the context file>",
   "term": "<中文詞條名稱，可微調>",
   "aliases": ["<exact strings as they appear on the site>"],
   "aka": "<English term(s)>",
   "def": "<白話解釋>",
   "example": "<例子或空字串>",
   "note": "<補充或空字串>",
   "label": "<short source label, e.g. WHO 2020・定義 / ACR 2022・定義 / 系統性回顧・定義 / MeSH 不用>",
   "evidence": [
     {"quote": "<verbatim English quote>", "location": "<section/table/abstract>",
      "access": "PMC full text | abstract | WebFetch", "pmid": "...", "doi": "...", "pmcid": "...",
      "supports": "<which part of def/example/note this quote supports>"}
   ],
   "sources": [{"short": "<中文簡稱>", "citation": "<First author et al. Title. Journal Year;Vol:Pages.>", "pmid": "...", "doi": "..."}],
   "confidence": "High (PMC full text or abstract, Tier 1–2) | Medium | Low",
   "status": "ok | no_source",
   "reviewer_notes": "<conflicts, caveats, anything the physician should check>"
  }
 ]
}
Validate the JSON (python3 -c "import json;json.load(open(path))") before finishing.
Reply with ≤ 250 words: counts (ok / no_source), the weakest entries, and the output path.
