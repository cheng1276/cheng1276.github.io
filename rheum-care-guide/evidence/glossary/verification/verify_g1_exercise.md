# Verification report: g1_exercise (15 entries)

**Summary: OK 7 / minor 7 / major 1**
- OK: moderate-intensity, vigorous-intensity, light-intensity, major-muscle-groups, sedentary, passive-therapy, aerobic-capacity
- minor: aerobic, muscle-strengthening, multicomponent, mind-body, aquatic, range-of-motion, perceived-exertion
- major: weight-bearing. The entry suggests jogging, tennis and ground impact, with no caution, on the long-term glucocorticoid bone card. Its own source (BHOF 2022) lists jogging and tennis as potentially injurious in osteoporosis.

## What I checked (all entries)
- **Citations:** I pulled PubMed metadata for all 13 PMIDs (33239350, 30418471, 42336388, 37227071, 38580348, 3920711, 35478046, 28599680, 42264828, 27007113, 26401907, 32686505, 21694556). For every source, the PMID, DOI, first author, title, journal, year, volume and pages match. Notes:
  - Caspersen 1985 has no DOI in PubMed, and the entry correctly leaves it empty.
  - Ward 2015 has its e-pub in 2015 and its print issue in 2016;68(2), so the entry's "2016" is the print citation.
  - BSR 2026 and Blaess 2024 use article numbers instead of pages.
- **Quotes:** I fetched PMC full text or the PMC/PubMed abstract for the 11 sources that have them. Then I machine-compared all 61 evidence quotes after normalising whitespace, quote marks and dashes.
  - **54 of 61 are verbatim** in the cited text. I read the surrounding sentence for each, so no quote hides a dropped "not".
  - The quotes with negatives are all intact in the source: "do not result in…", "can talk, but not sing", "cannot say more than a few words", "could supplement, but not substitute for", "evidence was insufficient…".
  - All stated locations are correct, including the WHO Table 1 rows, the US PAG "Key Concepts" subsections, the BHOF section heading, the Blaess Statement 9/14 discussions, the WHO "What is new?" section, Ward A2 Rehabilitation and the BSR Rec 28 rationale.
- **The 7 WebFetch quotes** fall in two groups:
  - **5 quotes from ACR 2022 Table 1** (rows: Aerobic, Resistance, Mind-body exercise, Mind-body approaches, Aquatic). The PMC extraction (PMC10947582) contains no Table 1. The PMC page returned a CAPTCHA, Wiley returned 403 and the Europe PMC XML returned 404. I made **two independent WebFetch reads of a different copy**: the CDC Stacks PDF of the Arthritis Rheumatol manuscript (https://stacks.cdc.gov/view/cdc/151745/cdc_151745_DS1.pdf, Table 1 on p. 19). My prompts did **not** include the expected wording. Both reads returned exactly the drafters' wording for all 5 rows. These quotes are still not machine-checkable, but 4 reads across 2 copies agree.
  - **2 quotes from AHA 2020** where an italic word ("flexibility", "CRF") was dropped in extraction. The rest of each quote is verbatim in the PMC text. The restored word is confirmed by context: the next sentence begins "Flexibility is important…", and the CRF sentence repeats the abstract's CRF definition. I treat both as verified.
- **Site fit:** I read every [LINK] and [repeat] sentence in occurrences.md, plus the site's own evidence quote behind each one (src/content/*.json). No alias is linked in a wrong sense.
- **Length:** every def is ≤ 60 characters, every example ≤ 40 and every note ≤ 50. No entry uses 「你」.

---

## aerobic — 有氧運動 — **minor**
**Checked:**
- All 5 non-WebFetch quotes are verbatim: WHO Table 1, US PAG, BSR, Blaess and Caspersen.
- The ACR Table 1 "Aerobic exercise" row matches my 2 CDC-copy reads.
- The def, example and note are fully supported: WHO "large muscles move in a rhythmic manner for a sustained period of time… also called endurance activity—improves cardiorespiratory fitness. Examples include walking, running, swimming and bicycling"; US PAG "heart rate to increase and breathing to become more labored"; BSR "dancing".
- The entry fits every linked sentence: CM-1.1, RA-1.2, AS-1.2, SL-4.2 (its examples match BSR's), SJ-4.4 and RA-1.T.

**Problem:** Two listed sources support nothing that is displayed:
- Caspersen 1985 (PMID 3920711) and Blaess 2024 (PMID 38580348).
- Their evidence "supports" fields and the reviewer_notes refer to a note about 「運動」 vs 「身體活動」. The current note does not contain it (it is only 「又稱耐力運動，可提升心肺耐力。」).
- Patients would see two sources that the text does not use.

**Proposed fix:** No Chinese text change. Remove those two sources and their two evidence items (Blaess "On the other hand, exercise refers to…" and the Caspersen abstract), and delete the last sentence of reviewer_notes. The remaining sources (WHO 33239350, Piercy 30418471, BSR 42336388, ACR 37227071) cover every displayed claim.

## moderate-intensity — 中等強度 — **OK**
**Checked:**
- All 7 quotes are verbatim.
- **The def follows WHO, not Blaess.** 「3倍到未滿6倍」 corresponds to WHO "between 3 and <6 times the intensity of rest (METs)" (PMID 33239350, Table 1). US PAG "3 to 5.9 METs" agrees.
- Blaess's "3–5 times" (PMID 38580348) appears only as an evidence item flagged in reviewer_notes. It is not used in any displayed text.
- 「約5–6分」 is supported by WHO "usually a 5 or 6", US PAG and Blaess.
- The example 「快走、打排球」 is from US PAG ("walking briskly…, playing volleyball").
- The note matches the talk test ("can talk, but not sing").

**Fit:**
- CM-1.1, SL-3.3 and SL-3.T fit, and SL-3.T's 「0–10 分…約 5–6 分」 is identical to the entry.
- In RA-1.T, EULAR defines moderate intensity by heart rate (64–76% of maximal). That is a different measure, not a contradiction.

**No change needed.**

## vigorous-intensity — 高強度（激烈）運動 — **OK**
**Checked:**
- All 5 quotes are verbatim.
- **The example 「提很重的購物袋」 is in the quote.** US PAG (PMID 30418471): "Examples of vigorous-intensity activities include jogging or running, carrying heavy groceries, or participating in a strenuous fitness class." Translating "carrying heavy groceries" as 「提很重的購物袋」 is natural Taiwan usage and faithful. A more literal option, 「提很重的採買物品」, is not needed.
- The def uses WHO "6.0 or more METs" and "usually a 7 or 8", plus US PAG "begins at a level of 7 or 8". So 「約在7–8分或以上」 is correct.
- The note matches "cannot say more than a few words without pausing for a breath".

**Fit:**
- CM-1.1 「高強度有氧活動」 is exactly WHO "vigorous-intensity aerobic physical activity".
- AS-1.T and AS-M1 (site sources: "intense strenuous exercise… flare-up") and RA-1.5 (EULAR 2025: "a flare might prevent someone from performing high-intensity activities, activities of lower intensity such as going for a walk or range of motion exercises might still be possible") are explained correctly by the WHO definition.
- Nothing in the entry encourages vigorous exercise during a flare.

## light-intensity — 輕度活動 — **OK**
**Checked:** All 4 quotes are verbatim.

**The example is in the quotes:**
- 「慢慢走路、洗澡」 and 「等不太讓心跳呼吸加快的活動」 come from WHO Table 1 (PMID 33239350): "Examples include slow walking, bathing or other incidental activities that do not result in a substantial increase in heart rate or breathing rate." The "not" is intact in the source.
- 「做輕鬆家事」 comes from US PAG (PMID 30418471): "walking slowly at 2 mph or less or doing light household chores".
- The drafters correctly kept "do not result in a substantial increase…" in the example rather than turning it into the definition.

**Rest of the entry:**
- The def (1.5–3 METs, about 2–4 points) is from WHO.
- The note is supported by WHO "replacing sedentary time with any intensity of physical activity (including light intensity) has health benefits".
- The entry fits CM-1.4.

## muscle-strengthening — 肌力訓練（阻力訓練） — **minor**
**Checked:**
- All 4 non-WebFetch quotes are verbatim.
- The ACR "Resistance exercise" row matches my 2 CDC reads.
- The def is supported:
  - "work against an applied force or weight": Blaess (citing WHO) and US PAG.
  - 「目的是增加肌力」: BSR "resistance which builds strength" (verified) and ACR (WebFetch).
  - 「也叫阻力訓練」: Blaess "resistance training, or strength training".
- The entry fits all 4 [LINK] and 3 [repeat] sentences, including CM-4.4 「阻力訓練」 and RA-1.3, which it does not contradict.

**Problem (clarity):** The example item 「用自己的體重」 is an incomplete phrase. It does not say what the body weight is for.

**Proposed example:** 「舉啞鈴、拉彈力帶、用自身體重當阻力，或爬樓梯、從椅子上站起來」 (30 characters)
**Support:**
- Blaess, PMID 38580348: "Muscle-strengthening activities may incorporate weights, elastic bands or using body weight for resistance training."
- BSR, PMID 42336388: "(e.g. using resistance bands, hand weights and machines), or achieved via functional means such as stair climbing and rising from a chair".

## major-muscle-groups — 全身主要肌群 — **OK**
**Checked:**
- Both quotes are verbatim.
- The def lists the same body parts as US PAG (PMID 30418471): "all the major muscle groups of the body–the legs, hips, back, abdomen, chest, shoulders, and arms".
- The note matches "The effects of muscle-strengthening activity are limited to the muscles doing the work."
- The entry fits CM-1.2, where WHO says "involve all major muscle groups" (also quoted via BSR).

## weight-bearing — 負重運動 — **major (safety)**
**Checked:**
- Both quotes are verbatim and the locations are correct:
  - BHOF 2022 (PMID 35478046, PMC9546973), "Universal bone health recommendations" > "Regular weight-bearing and muscle-strengthening physical activity".
  - US PAG, "Bone-Strengthening Activity".
- The def is faithful to "bones and muscles work against gravity with feet and legs bearing body weight".
- The example is a faithful transcription of BHOF's list.
- The note's impact claim is accurately quoted from US PAG: "This force is commonly produced by impact with the ground."

**Problem (unsafe in site context):**
- This entry is linked only at CM-4.4, in the card 「類固醇與骨骼保健」. That card is for adults on oral glucocorticoids for more than 3 months, at low to very high fracture risk (ACR 2022 GIOP).
- The example recommends 「慢跑」 and 「打網球」, and the note stresses 「身體與地面的撞擊」, with no caution.
- The **same BHOF source** warns about exactly these:
  - In the same paragraph as the quoted sentence: "To avoid injury, patients should be evaluated before initiating a new exercise program, particularly one involving compressive or contractile stressors (such as running or weightlifting)."
  - In "Protecting fragile bones in daily life and recreation": "Recreational pursuits and athletic activities that exert intense forces on weakened bone and/or involve abrupt or high-impact loading can break bones in people with osteoporosis".
  - Its list of "Potentially injurious activities for individuals with osteoporosis" includes "Running/jogging (beneficial for hip BMD, can be dangerous for low spinal BMD)" and "Golf, tennis/racquet ball, and bowling (done conventionally with twisting at waist)".
- As written, the entry could lead a glucocorticoid-treated patient with fragile bones to start jogging, tennis or impact activity without assessment.

**Proposed fix:**
- example: 「走路、太極拳、爬樓梯、跳舞」. This is a subset of the BHOF quote that drops the two activities BHOF flags as potentially injurious in osteoporosis.
- note (43 characters): 「這類活動對骨骼施力，有助骨骼強壯；開始跑步、舉重等新運動前，宜先請醫師評估，以免受傷。」
  - Support 1: PMID 30418471 (US PAG, Bone-Strengthening Activity), "Bone-strengthening (also called weight-bearing or weight-loading) activities produce a force on the bones of the body that promotes bone growth and strength."
  - Support 2: PMID 35478046 (BHOF, "Regular weight-bearing and muscle-strengthening physical activity", paragraph 1, PMC full text, machine-verified), "To avoid injury, patients should be evaluated before initiating a new exercise program, particularly one involving compressive or contractile stressors (such as running or weightlifting)."
  - The BHOF sentence is passive. 「請醫師評估」 is the natural reading in a clinician's guide; for strictly literal wording, use 「宜先接受評估」.
- Alternative note, more specific to osteoporosis (47 characters): 「已有骨質疏鬆的人，突然或強力撞擊的活動可能造成骨折；開始跑步、舉重等新運動前，宜先請醫師評估。」
  - Support: PMID 35478046, "Recreational pursuits and athletic activities that exert intense forces on weakened bone and/or involve abrupt or high-impact loading can break bones in people with osteoporosis" (section "Protecting fragile bones in daily life and recreation", PMC full text, verified), plus the evaluation sentence above.
- Add the BHOF sentence(s) you use as new evidence items.
- Do **not** add WHO's "Bone-strengthening activity" row ("any type of jumps, running and lifting weights") for this card.

## multicomponent — 多元活動（平衡與肌力） — **minor**
**Checked:**
- All 3 quotes are verbatim.
- The def matches WHO Table 1: "can be done at home or in a structured group or class setting and combine all types of exercise (aerobic, muscle strengthening and balance training) into a session".
- The example comes from the same row, and the note's activities come from US PAG.
- The entry fits CM-1.3, where WHO says "emphasizes functional balance and strength training".

**Problems:**
1. The term label 「（平衡與肌力）」 implies the activity is only balance plus strength, but the def (WHO) includes aerobic. **Proposed term:** 「多元活動（有氧、肌力與平衡）」. Support: PMID 33239350, "combine all types of exercise (aerobic, muscle strengthening and balance training) into a session".
2. 「舉重物」 renders "lifting weights", which is the exercise. Lay readers, including 65+ readers on this card, may take it to mean lifting heavy household objects. **Proposed example:** 「走路、舉啞鈴，再加上倒退走、側走或單腳站等平衡練習」 (25 characters). Support: PMID 33239350, "could include walking (aerobic activity), lifting weights (muscle strengthening)… walking backwards or sideways or standing on one foot". 「啞鈴」 matches the wording used in the muscle-strengthening entry.
3. The note phrase 「常同時包含多種活動」 is circular ("activities that contain several activities"). **Proposed note:** 「跳舞、瑜伽、太極拳、園藝等活動常同時包含多種類型的身體活動，也可算是多元活動。」 (39 characters). Support: PMID 30418471, "because they often incorporate multiple types of physical activity."

## sedentary — 久坐（靜態行為） — **OK**
**Checked:**
- All 5 quotes are verbatim.
- The def follows WHO "Any waking behaviour… 1.5 METs or lower while sitting, reclining or lying"; SBRN 2017 agrees and adds "lying".
- The example comes from WHO.
- 「睡覺不算」 follows directly from "waking".
- The threshold note is supported by the WHO abstract "evidence was insufficient to quantify a sedentary behaviour threshold" and by the "What is new?" text.
- The entry fits CM-1.4, and the note does not undercut it: the site sentence itself says 減少久坐.

## mind-body — 身心運動與身心療法 — **minor**
**Checked:** Both machine-checkable quotes are verbatim:
- ACR PMC text: "Consistent engagement in mind-body exercise (yoga, Tai Chi, qigong)…" and "Use of cognitive behavioral therapy and/or mind-body approaches…".
- da Silva 2026 abstract: "practices integrating physical movement, controlled breathing, and focused attention".

**WebFetch status:**
- I **could not machine-confirm** the two Table 1 rows ("Mind-body exercise", "Mind-body approaches").
- My 2 independent CDC-copy reads gave the same wording as the drafters' 2 PMC reads: "Exercise that combines movement, mental focus, and controlled breathing. Examples include yoga, Tai Chi, Qigong." and "Practices engaging both mind and body functions. Examples include biofeedback, goal setting, meditation, mindfulness, breathing exercises, progressive muscle relaxation, guided imagery."

**What is supported by what:**
- **The 身心運動 half of the def is also supported by verified quotes** (ACR PMC text; da Silva).
- **The 身心療法 half and the example rest only on the WebFetch row.**
- Given 4 identical reads from 2 copies, I judge the text supported.
- The da Silva source is only corroboration: its population is people with dementia, and its definition also includes dance and mindfulness.

**Fit:** RA-1.2 matches mind-body exercise and RA-5.4 matches mind-body approaches. These are distinct Table 1 rows, and the entry keeps them distinct.

**Problem (location precision):** My reads give the Table 1 caption as "Descriptions and examples of interventions included in the integrative management of rheumatoid arthritis guideline." The drafters' location cites a different title from their read 2.
**Proposed location (both WebFetch items):** "Table 1 ('Descriptions and examples of interventions included in the integrative management of rheumatoid arthritis guideline'), row '…'; not in the PMC extraction; WebFetch: PMC page ×2 (drafters) and CDC Stacks author manuscript p.19 ×2 (verifier), identical wording."

No Chinese text change.

## aquatic — 水中運動 — **minor**
**Checked:**
- 「泡在水中」 is verified. Cochrane 2016 (PMID 27007113): "Aquatic exercise is physical exercises taking place while the participant are immersed in water". The "are" is as printed.
- The note is verified. Ward 2015 (PMID 26401907): "can be used by those with access to a swimming pool or hydrotherapy tub".
- The ACR "Aquatic exercise" row, which is the only support for 「同時包含有氧運動和肌力（阻力）訓練的成分」 and for the example, matches my 2 CDC reads: "Exercise performed in water, containing elements of both aerobic and resistance exercise. Examples include swimming, water aerobics, water walking or jogging."
- That row is not machine-checkable. The ACR PMC text only says "comfort in water".
- The entry fits RA-1.2.

**Problems (labels only):**
1. Use the same Table 1 location wording as in mind-body.
2. The Cochrane quote is in the plain-language summary carried in the PMC record's abstract field. It is not in the PubMed abstract. **Proposed access:** "PMC abstract (plain language summary)".

No Chinese text change.

## range-of-motion — 關節活動度運動 — **minor**
**Checked:**
- 3 quotes are verbatim.
- The AHA "flexibility" quote is confirmed from context (see above).
- ACSM abstract: "Crucial to maintaining joint range of movement, completing a series of flexibility exercises…".
- BSR: "improve range of movement of specific joints (e.g. yoga, tai chi or stretching)".

**Fit:**
- RA-1.5 fits; the EULAR 2025 site quote is "range of motion exercises".
- AS-1.2 fits; the NICE site quote is "range of motion exercises for the lumbar, thoracic and cervical sections of the spine". 「（或一組關節）」 covers the spine.

**Problems:**
1. The label 「AHA 2020・定義」 overstates. AHA defines *flexibility*, not ROM exercise, and 「維持或改善這個範圍」 comes from ACSM and BSR statements about flexibility exercises.
   - **Proposed label:** 「AHA 2020、ACSM 2011・綜合說明」.
   - Support: PMID 32686505, "Third, flexibility refers to an individual's range of motion around a joint, or group of joints."; PMID 21694556, "Crucial to maintaining joint range of movement, completing a series of flexibility exercises for each the major muscle-tendon groups".
2. FYI, no change needed:
   - The note's source is an AHA statement on youth, but the sentence used is general.
   - My PubMed search for a guideline, consensus or systematic-review definition of "range of motion exercises" returned nothing, so no better source is evident.

## passive-therapy — 被動治療與主動運動 — **OK**
**Checked:**
- Both quotes are verbatim in the Arthritis Care Res PMC text (A2 Rehabilitation, PICO 17 and rationale).
- The def is faithful: "active physical therapy interventions (supervised exercise) over passive physical therapy interventions (massage, ultrasound, heat)".
- The note is faithful: "one of the goals of physical therapy is to educate patients in self-management in using an independent exercise program… Passive interventions could supplement, but not substitute for…".
- The population (adults with active AS) suits the axSpA page.
- The entry fits AS-M2 in both the belief and the fact sentence.

**Optional:** Write 「超音波治療」 instead of 「超音波」 so readers don't confuse it with an ultrasound scan. Proposed def: 「被動治療指按摩、超音波治療、熱療這類治療；主動運動指自己動起來做的運動，例如有人督導的運動訓練。」 (48 characters; same quote, PMID 26401907).

## aerobic-capacity — 心肺耐力 — **OK**
**Checked:**
- The def matches the AHA abstract (verbatim): "capacity of the circulatory and respiratory systems to supply oxygen to skeletal muscle mitochondria for energy production". Rendering this as 「心臟、血管和肺」 is a fair simplification.
- The synonyms are supported by AHA ("also known as cardiorespiratory endurance, cardiovascular fitness, aerobic capacity…"; the subject "CRF" is confirmed from context) and by US PAG "cardiorespiratory fitness or aerobic capacity" (verbatim).
- WHO supports 「有氧運動可以提升心肺耐力」.
- The entry fits SL-4.2 (EULAR "increasing aerobic capacity").

## perceived-exertion — 自覺費力程度 — **minor**
**Checked:**
- All 4 quotes are verbatim.
- The def's anchors (0 = sitting, 10 = highest possible effort) and the note's "lower fitness → higher score" come from US PAG (PMID 30418471): "a scale of 0 to 10, where sitting is 0 and the highest level of effort possible is 10" and "relative intensity will be higher for a person with lower aerobic capacity".
- The cut-points (5–6 and 7–8) come from WHO and US PAG.
- The entry fits SL-3.T.

**Problem (label precision):** The label 「WHO 2020・定義」 credits WHO with a definition whose content is mainly from US PAG; WHO gives only the cut-points.
**Proposed label:** 「WHO 2020、美國身體活動指引・定義」.

No text change.
