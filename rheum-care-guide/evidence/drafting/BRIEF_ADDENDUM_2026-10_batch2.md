# Addendum to the drafting brief: second batch (October 2026)

Read /home/claude/cheng1276.github.io/rheum-care-guide/evidence/drafting/BRIEF.md first and follow it in
full, then apply this addendum. Where BRIEF.md names /home/claude/research/... or /home/claude/content/...,
use the paths below.

## Physician's standing style rules
- Taiwan Mandarin (台灣繁體中文), no emoji, no exclamation marks.
- Write 「就醫」 or 「回診」 / 「和醫師討論」, never 「聯絡醫療團隊」.
- Supplements a doctor recommends are 「醫師指示的…」, not 「醫師開的…」.
- A neutral safety phrase such as 「用藥調整請和醫師討論，不要自行停藥」 may be added with evidence code
  "EDITORIAL" (strength_label 「編輯加註・安全提醒」), sparingly, and must be listed in reviewer_notes.

## Paths
- Evidence files: /home/claude/newpages2/research/pregnancy.md, steroid.md, cardio.md (read yours
  COMPLETELY, including sections C, D and E — the caveats there decide what you must not say).
- Shared evidence file: /home/claude/cheng1276.github.io/rheum-care-guide/evidence/research/common.md
  (cite as "common:C12" with source "common:S6" only if needed).
- Style references: /home/claude/cheng1276.github.io/rheum-care-guide/src/content/infection.json,
  common.json and sle.json (its pregnancy card SL-6.x). Match field names, tone and length.
- The site's existing text you must not contradict or duplicate: common.json (bone card CM-4.x, smoking
  CM-2.x, diet/weight/alcohol CM-3.x, activity CM-1.x, vaccines CM-5.x), infection.json (glucocorticoid
  card IF-4.x and seek-care IF-S2), sle.json (pregnancy card SL-6.x).

## Task A — new topic page "pregnancy" (懷孕、哺乳與避孕), output /home/claude/newpages2/content/pregnancy.json
- slug "pregnancy", name "懷孕、哺乳與避孕". sid prefix "PG": points "PG-<card#>.<point#>", tips
  "PG-<card#>.T", myths "PG-M<n>", seek_care "PG-S<n>". Card ids "pregnancy-<short>" (e.g.
  pregnancy-plan, pregnancy-contraception, pregnancy-medicines, pregnancy-care, pregnancy-breastfeeding,
  pregnancy-baby; choose what the evidence supports).
- The page covers all rheumatic diseases, women and men. Where a statement applies only to some diseases
  (e.g. anti-Ro/SSA testing, antiphospholipid antibodies), name the diseases.
- STRICT medicine rule (the physician asked for more caution than elsewhere on the site): no individual
  drug names, no brand names, no doses, and no stop intervals or gestational weeks for medicines. Drug
  CLASSES only when a point cannot be made without them and a patient would recognise them (e.g. 生物製劑
  for the infant live-vaccine point; contraceptive method classes such as 子宮內避孕器, 避孕植入物,
  含雌激素的避孕方式). List every drug class or method class you use in reviewer_notes. Never imply that
  a reader should stop or change a medicine; the message is always to discuss with the doctor first.
- Where sources conflict (e.g. how long infants should wait for live vaccines; 4 vs 6 months of
  post-partum review; injectable contraception with antiphospholipid antibodies), write only the common
  ground with no number, and explain in reviewer_notes.
- Stay consistent with the SLE card: it says disease activity in the 6–12 months before conception raises
  flare risk. If you state ACR's "at least 6 months" of quiet disease, phrase it so the two do not clash
  and note it.
- Do not use claims the evidence file marks "drug-specific — not for site text", nor Low-confidence
  claims except as a second citation. The EULAR 2024 update was read only via a German summary (Low): do
  not let it be the only support for any sentence.
- 4 to 6 cards with 2 to 5 points each (a tip is optional), 2–4 myths that Taiwanese patients actually
  hold (from section C), seek_care only if a source states it. intro ≤ 70 characters.

## Task B — two new cards for the common page (共通照護), output
/home/claude/newpages2/content/common_additions.json
Structure: {"cards": [<card 1>, <card 2>], "sources": [...], "placement": "...", "reviewer_notes": [...]}
- Card 1, id "common-steroid": what people on long-term systemic glucocorticoids should know BESIDES bone
  (side effects to watch and the monitoring a source recommends, eyes, blood sugar, blood pressure, weight
  / swelling, mood and sleep, and so on; not changing the dose or stopping on one's own; tapering decided
  by the doctor). Do not repeat the bone card (CM-4.x) or the infection page's glucocorticoid sentences
  (IF-4.1–4.4, IF-S2); a point may refer readers to the infection page for what to do when ill, without
  repeating its facts. Title ≤ 10 characters (e.g. 「類固醇的其他注意事項」 or 「類固醇：骨頭以外」).
  sids "CM-7.<n>", tip "CM-7.T".
- Card 2, id "common-heart": cardiovascular risk in rheumatic diseases (higher risk, regular risk checks,
  managing blood pressure / lipids / blood sugar as in the general population, controlling the disease,
  glucocorticoids and NSAIDs at patient level, disease-specific items such as the SLE blood-pressure
  target if supported). Do not repeat the smoking, diet/weight/alcohol or activity cards: at most one
  short point may point to them. No individual drug names (no statins, aspirin, antimalarials,
  urate-lowering drugs by name). Title ≤ 10 characters. sids "CM-8.<n>", tip "CM-8.T".
- Evidence "c" codes: "steroid:C12" or "cardio:C34" (or "common:C12"). Sources: if the paper is already in
  common.json's sources (same PMID), reuse that S-ID (e.g. "S6", "S1"); otherwise use "steroid:S<n>" /
  "cardio:S<n>" with the evidence file's numbering, and include a full source record in "sources".
- "placement": one sentence suggesting where each card should sit among the existing common-page cards.
- 2 to 6 points per card (a tip is optional). No myths or seek_care in this file unless strongly sourced
  (if you add any, use sids "CM-M<n>" / "CM-S<n>" continuing after the existing ones and explain).

## Validation and reply
Validate each JSON with python3 -c "import json;json.load(open(path))". Check that every evidence quote is
copied exactly from the evidence file (cut with … only). Then reply with: the file path(s), the card
titles, the myths (Task A), and the top 5 reviewer notes.
