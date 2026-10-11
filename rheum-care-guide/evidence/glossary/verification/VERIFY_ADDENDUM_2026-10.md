# Addendum to the glossary verification rules: new terms (October 2026)

Read /home/claude/cheng1276.github.io/rheum-care-guide/evidence/glossary/verification/VERIFY.md first and
follow it in full; then apply this addendum, whose paths replace those in VERIFY.md.

## What you are checking
Four new pages are in physician review (not public): 退化性關節炎 (oa), 骨質疏鬆症 (osteoporosis),
健檢報告異常 (labs) and 治療期間防感染 (infection). Another team drafted glossary entries for new terms on
them. You did not write these entries. Find every error before patients see them.

## Inputs
- Drafted entries for your group: /home/claude/newpages/glossary/research_<group>.json → "entries"
  (fields: id, term, en, cat, aliases, aka, def, example, note, label, evidence[{quote, location, access,
  pmid, doi, pmcid, supports}], sources[], confidence, status, reviewer_notes).
- Where each alias appears on the site (all 11 pages), with the full sentence and whether that occurrence
  becomes the tappable link: /home/claude/newpages/glossary/context_<group>.md
- Writing rules the drafters followed: /home/claude/cheng1276.github.io/rheum-care-guide/evidence/glossary/research/PROTOCOL.md
  ("Writing rules") and /home/claude/newpages/glossary/GLOSSARY_ADDENDUM.md ("Extra writing rules").
- Site text with its own sources: /home/claude/newpages/content/{oa,osteoporosis,labs,infection}.json and
  /home/claude/cheng1276.github.io/rheum-care-guide/src/content/*.json
- Evidence files from the site's research phase (optional background):
  /home/claude/newpages/research/*.md and /home/claude/cheng1276.github.io/rheum-care-guide/evidence/research/*.md
- Existing glossary (125 entries, already verified and public):
  /home/claude/cheng1276.github.io/rheum-care-guide/src/glossary/glossary.json

## Part 2: existing entries in their new sentences
Your assignment also lists existing glossary ids. These entries were verified for the old pages; now
they will also link from sentences on the new pages. For each listed id, read the entry in glossary.json
and its new occurrences in /home/claude/newpages/glossary/context_existing_on_new_pages.md, then check
only VERIFY.md checks 4 (fit with the site, in every new [LINK] and [repeat] sentence) and 6 (safety).
Two of them get a proposed new alias, marked in that file: immunosuppressant + 免疫抑制劑,
multicomponent + 綜合性的運動課程. Judge whether each alias should be added.
If an entry does not fit a new sentence, propose the smallest fix: an exact replacement text supported
by a verbatim quote + PMID (read in this session), or excluding that page (exclude_pages), or not adding
the alias.

## Output
Write /home/claude/newpages/glossary/verify_<group>.md in the format VERIFY.md describes, with a Part 2
section for the existing entries (verdict OK | minor | major for each). Do NOT edit research_*.json,
glossary.json or any site file. Final reply ≤ 250 words: counts, the major problems in one line each,
and the report path.
