# Addendum to the drafting brief: four new pages (October 2026)

Read /home/claude/cheng1276.github.io/rheum-care-guide/evidence/drafting/BRIEF.md first and follow it in
full, then apply this addendum. Where BRIEF.md names /home/claude/research/... or /home/claude/content/...,
use the paths below instead.

## Paths
- Your evidence file: /home/claude/newpages/research/<slug>.md (read it COMPLETELY, including sections C,
  D, E).
- Shared evidence file (generic topics already on the site's common page):
  /home/claude/cheng1276.github.io/rheum-care-guide/evidence/research/common.md — cite as "common:C12" /
  source "common:S6" only when a card needs one generic point; do not repeat common-page topics
  (physical-activity amounts, smoking, generic diet/weight/alcohol, glucocorticoid bone health, general
  vaccine principles, UV index).
- Style references (read at least one): /home/claude/cheng1276.github.io/rheum-care-guide/src/content/
  sjogren.json and common.json. Match their field names, tone and length.
- Output: /home/claude/newpages/content/<slug>.json (validate with python json.load).

## Extra fields and IDs
Add a "sid" to every point, tip, myth and seek_care item, as the existing JSON files do:
points "<P>-<card#>.<point#>", tips "<P>-<card#>.T", myths "<P>-M<n>", seek_care "<P>-S<n>", where
<P> is OA (oa), OP (osteoporosis), LB (labs), IF (infection).
Page names: oa → 退化性關節炎; osteoporosis → 骨質疏鬆症; labs → 健檢報告異常; infection → 治療期間防感染.

## Topic notes
- oa: knee, hip and hand osteoarthritis. The 2026 ACR update exists only as a non-peer-reviewed summary:
  do NOT cite it (BRIEF rule 2); record in reviewer_notes every place where it would change what you
  wrote. Respect population restrictions (e.g. weight loss only for people with overweight; knee vs hip
  vs hand). Do not repeat the common page's physical-activity amounts.
- osteoporosis: postmenopausal women and men ≥50. Glucocorticoid users are covered on the common page;
  do not repeat that card, but you may say in the intro or a point that long-term glucocorticoid users
  should also read the common page only if you can phrase it without a factual claim. Medication-adjacent
  safety messages (e.g. not stopping a treatment without a plan, dental care) only exactly as sources
  state them; use generic, recognisable wording rather than brand or INN names where possible, and flag
  any drug name you think is needed in reviewer_notes.
- labs: this page explains abnormal health-check results (ANA, RF / anti-CCP, high uric acid without
  gout). It is education about what results mean, not diagnosis. Never imply the reader has or does not
  have a disease; say the doctor interprets results together with symptoms and examination when a
  source supports it. Where guidelines conflict (asymptomatic hyperuricaemia drug treatment), write only
  the common ground and set out the conflict in reviewer_notes (BRIEF rule 5). Do not repeat the gout
  page's diet/drink details; at most one point may point readers to general uric-acid lifestyle measures
  if a source supports it for asymptomatic hyperuricaemia.
- infection: people taking glucocorticoids, conventional/biologic/targeted DMARDs or immunosuppressants.
  Patient-behaviour messages only (screening and why, completing latent-TB treatment, hepatitis B
  status and monitoring, what to do when ill, glucocorticoid safety, everyday precautions that a source
  states). Generic drug classes the patient would recognise are allowed (類固醇、生物製劑、免疫抑制劑);
  no doses. A neutral safety phrase such as 「用藥調整請和醫師討論，不要自行停藥」 may be added as
  EDITORIAL, sparingly. Taiwan-specific facts (Taiwan CDC latent TB programme, 都治) are welcome when
  the evidence file quotes them.

## Myths
Prefer myths that Taiwanese patients actually hold and that a source clearly addresses; 2–4 per page.
These will also be used for short videos, so the fact must stand on its own in one or two sentences.

## Reply
When done, reply with: the file path, the card titles, the myths, and the top 5 reviewer notes.
