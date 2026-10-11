# Addendum to the glossary protocol: terms on four new pages (October 2026)

Read /home/claude/cheng1276.github.io/rheum-care-guide/evidence/glossary/research/PROTOCOL.md first and
follow it in full (source tiers, verbatim quotes, PMID/DOI from get_article_metadata, the dropped-word
pitfall, writing rules, JSON schema). Then apply this addendum. Where PROTOCOL.md names
/home/claude/glossary/... or /home/claude/research/..., use the paths below instead.

## Background
The site is adding four pages, still in physician review and not public yet:
退化性關節炎 (oa: knee, hip and hand osteoarthritis), 骨質疏鬆症 (osteoporosis: postmenopausal women
and men aged 50 or over), 健檢報告異常 (labs: what a positive ANA, RF or anti-CCP test or a high uric acid
on a health check means), 治療期間防感染 (infection: people taking glucocorticoids, conventional, biologic
or targeted antirheumatic drugs or immunosuppressants). The glossary already has 125 entries for the
seven existing pages; you are writing entries for NEW terms only.

## Inputs
- Your term list, with every site sentence where each alias occurs (existing pages included) and
  whether that occurrence becomes the tappable link:
  /home/claude/newpages/glossary/context_<group>.md
  Your definition must fit EVERY listed sentence, including any on the existing pages.
- Evidence files for the new pages (sources already read for the site, with verbatim quotes, S-IDs and
  access level; reuse leads, but re-confirm every quote yourself in this session):
  /home/claude/newpages/research/{oa,osteoporosis,labs,infection}.md
  Older pages: /home/claude/cheng1276.github.io/rheum-care-guide/evidence/research/*.md
- Site text with sources per statement: /home/claude/newpages/content/{oa,osteoporosis,labs,infection}.json
  and /home/claude/cheng1276.github.io/rheum-care-guide/src/content/*.json
- Existing glossary (style reference; avoid overlap and never contradict it):
  /home/claude/cheng1276.github.io/rheum-care-guide/src/glossary/glossary.json
  Read the related existing entries named in your assignment before writing.

## Output
Write /home/claude/newpages/glossary/research_<group>.json with the PROTOCOL.md schema, plus two fields
per entry: "cat" (category id from your assignment) and "en" (clean English name for the popup, e.g.
"bone mineral density (BMD) test"). Keep "id" and "aliases" exactly as in the context file. If an alias
is wrong for a sentence (wrong sense, or the definition would mislead there), keep it but explain in
reviewer_notes and propose the fix; never add an alias that does not appear verbatim on the site.
Validate the JSON with python3 before finishing. Do not edit any other file.

Categories: condition 疾病與症狀, drug 藥物與疫苗, exercise 運動, rehab 復健與療法, diet 飲食與營養,
evidence 研究與出處用語, org 出處機構, and a new one: test 檢查與檢驗.

## Extra writing rules for this round
- Polite 您, never 你. Taiwan usage (e.g. 皮蛇, 帶原者, 骨鬆). Use the same Chinese words as the site.
- def ideally ≤ 60 Chinese characters (hard limit 90); example ≤ 40; note ≤ 50.
- Tests (ANA, RF, anti-CCP, hepatitis B markers, IGRA, bone density): explain what the test measures and,
  where a quote supports it, what a result can and cannot tell. Never imply that a result diagnoses or
  rules out a disease; where a quote supports it, say the doctor interprets results together with
  symptoms and examination. No reference ranges or numbers unless the quote has them and they match the
  site text.
- Drugs and drug classes (glucosamine, bisphosphonates, denosumab, oral targeted drugs / JAK inhibitors):
  what it is and how it is given if quoted; generic names only if quoted; no doses; no brand names.
  Nothing that could lead a reader to stop or skip a medicine. Side effects only if a quote supports
  them AND they are needed to understand the site text; if you mention one, keep the proportion the
  source gives (e.g. "rare").
- Conditions with emergencies (adrenal crisis): keep them clearly urgent, consistent with the site.
- Do not add advice that the site does not give. A note may restate a site message only if a quote
  supports it.
- Organisations (org entries): term = the abbreviation as on the site; en = the full English name exactly
  as printed in a PubMed-indexed publication by (or on behalf of) that organisation, with that sentence or
  author line as the evidence quote; def = a short descriptive Chinese gloss of what kind of body it is and
  where, plus what the site cites from it (year and topic, taken from the site's sources), following the
  style of the existing org entries (e.g. org-tra, org-ects, org-nice); label "<ABBR> <year>・名稱". Do not
  invent an official Chinese name. If the site's label pairs two bodies (e.g. ESE/ES), one entry covers
  both.
- reviewer_notes: write in English or Chinese; list anything the physician should decide.

## Reply
≤ 250 words: counts (ok / no_source), the weakest entries and why, any alias or site-wording problems you
found, and the output path.
