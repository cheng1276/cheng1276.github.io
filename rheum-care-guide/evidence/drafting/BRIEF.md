# Drafting brief: patient-facing content for 生活照護圖解

You turn ONE evidence file into patient-facing Traditional Chinese (Taiwan) content for a
public website run by a Taiwanese rheumatologist. The physician requires that nothing on
the site is wrong or unsupported. You may only say what the evidence file's verbatim
quotes support. You may not add facts, numbers, foods, products, time frames or
reasons from your own knowledge.

## Inputs
- Your evidence file: /home/claude/research/<slug>.md (read it COMPLETELY, including
  sections C, D, E — the caveats there decide what you must not say).
- Shared evidence file: /home/claude/research/common.md (exercise amounts, smoking,
  diet/weight/alcohol, glucocorticoid bone health, vaccines, UV index). Disease pages
  should not repeat these generic topics; cite them only when a disease card needs one
  generic point. Cross-file citations use the prefix "common:", e.g. "common:C12".
- The protocol the evidence files followed: /home/claude/research/PROTOCOL.md.

## Selection rules (strict)
1. Use claims rated High first; Medium is allowed. A Low claim may appear only as a
   second citation next to a High/Medium claim that already supports the sentence.
2. Do not rely on drafts, pre-publication summaries or documents the evidence file marks
   as not peer-reviewed / not final (e.g. a 2026 US urticaria draft, a 2026 ACR axSpA
   summary, the 2025 ACR SLE pre-publication summary if only the summary was read).
3. Respect every population restriction (e.g. "if overweight", "people who have had
   kidney stones", "when disease is inactive or mild").
4. Do not use any quote the evidence file flags as possibly altered (glued words, dropped
   words) unless the file records how the meaning was confirmed.
5. Where sources conflict, write only the common ground, or leave the topic out, and
   explain in reviewer_notes.
6. Prefer fewer, solid points over many weak ones. If a topic lacks solid support, drop it.
7. Medication-adjacent items: only patient-behaviour messages that a guideline states.
   No drug names except generic classes the patient would recognise (e.g. 抗組織胺,
   消炎止痛藥 NSAIDs, 降尿酸藥), no doses, no brand names. A neutral safety phrase such as
   「用藥調整請和醫師討論」 may be added with evidence code "EDITORIAL" (use sparingly).

## Chinese style
- 台灣繁體中文與台灣慣用詞（冰敷、含糖飲料、防曬乳、人工淚液、回診、物理治療師、職能治療師）。
- Readers: patients and families. Aim for junior-high reading level. Short sentences.
  Start points with a concrete action where possible (「選擇…」「每天…」「避免…」).
- No exclamation marks, no fear tactics, no blame (gout: genetics matter; avoid
  "patient-blaming", which ACR explicitly warns against).
- Arabic numerals; units in Chinese or standard symbols (分鐘、公升、毫克、國際單位).
- Avoid absolute words (一定、絕對、完全) unless the source is that absolute.
- Each point ideally ≤ 45 Chinese characters; never more than 70.
- Do not say "研究不足" / "沒有證據" unless a cited source itself says so.

## Strength labels (strength_label field, short Chinese)
Format: "<Org Year>・<label>", e.g. "ACR 2020・建議", "EULAR 2021・建議強度 A".
- GRADE strong for → 強烈建議; conditional / weak for → 建議;
  conditional / weak against → 不建議; strong against → 強烈不建議.
- EULAR with grade of recommendation A–D → 建議強度 A/B/C/D; overarching principle → 基本原則.
- BSR GRADE codes (1 = strong, 2 = conditional/weak; A–D = evidence quality) →
  e.g. 「強烈建議（1B）」「建議（2C）」.
- Good practice statement → 良好實務建議. NICE (no grade) → 建議.
- Systematic review / cohort finding → 研究顯示. Guideline narrative text (not a graded
  recommendation) → 指引說明. Expert consensus → 專家共識.
If the evidence file says the strength was not found, use 「指引說明」 or 「建議」 only if the
quote itself uses recommendation language ("should", "recommend"), and note it.

## Output: write valid UTF-8 JSON to /home/claude/content/<slug>.json
{
  "slug": "<slug>",
  "name": "<中文病名>",
  "intro": "一到兩句：這頁的重點（≤ 70 字）",
  "cards": [
    {
      "id": "<slug>-<short>",
      "title": "≤ 10 字",
      "summary": "一句重點（≤ 30 字）",
      "illustration": "English: a simple generic illustration that adds no claims beyond the points (no text, no brands)",
      "points": [
        {
          "text": "中文句子",
          "strength_label": "ACR 2020・建議",
          "evidence": [
            {"c": "C14", "s": "S1", "quote": "exact excerpt copied from the evidence file quote cell; you may cut with … but never change words", "strength": "as stated in the file", "confidence": "High"}
          ]
        }
      ],
      "tip": null or {"text": "...", "strength_label": "...", "evidence": [...]}
    }
  ],
  "myths": [ {"belief": "常見說法", "fact": "依據指引的說明", "strength_label": "...", "evidence": [...]} ],
  "seek_care": [ {"text": "...", "strength_label": "...", "evidence": [...]} ],
  "sources": [ {"s": "S1", "short": "中文簡稱，如 ACR 2020 痛風指引", "citation": "First author et al. Title. Journal Year;Vol:Pages.", "pmid": "...", "doi": "...", "url": "only for non-PubMed sources"} ],
  "reviewer_notes": ["English or Chinese notes for the physician: conflicts, omissions, items needing a check against the original PDF"]
}
- 4 to 6 cards, each with 2 to 5 points. "myths" 0–4 items. "seek_care" only if sourced.
- "sources" must list every S-ID you cite (use the file's PMID/DOI exactly).
- Validate the JSON (e.g. python3 -c "import json;json.load(open(path))") before finishing.

When done, reply with: the file path, the card titles, and the top 3 reviewer notes.
