# Independent verification: g5a_allergy_urticaria (13 entries)

**Summary: OK 10 · minor 3 · major 0.**
Minor: `autoimmune` (note off-topic on the vaccine page), `solar-urticaria` (UVA spelled two ways), `stridor-wheeze` (precision, plus 喘鳴 is ambiguous in Taiwan).
Two OK entries (`anaphylaxis`, `cold-urticaria`) still have stale reviewer_notes from before the UR-2.3 change. Patients don't see these notes, but they should be tidied.

Checked 2026-10-07 against glossary.json (version 2026-10-07), occurrences.md, and the current working-tree site JSON, which includes the new UR-2.3 wording.

---

## How I checked (applies to every entry)

- **Citations.** I pulled PubMed metadata for all 18 cited PMIDs: 41649409, 23282382, 33204386, 31719946, 36446151, 19963079, 31413005, 36109590, 33249577, 41044831, 32179196, 41182243, 40869562, 36107396, 38670233, 23919330, 30358678, 24522090. PMID, DOI, first author, title, journal, volume/issue/pages and PMCID all match. Where PubMed's date is the e-pub year (Miller 2022→2023, Lleo 2009→2010, Furer 2019→2020, Maltseva 2020→2021, Fukunaga 2022→2023), the entries correctly cite the print-issue year. I also checked the PMIDs that appear only in reviewer_notes (26679383 TDA consensus, 26991006 CIndU consensus, 26647442 ERS lung sounds). They are correct, and what the notes say about them is accurate.
- **Quotes.** There are 90 evidence quotes. All 90 are verbatim and their locations are correct.
  - 47 quotes (GALEN 2026 ×36, WAO 2012 ×11) were machine-matched against the PMC full text after normalising whitespace, dashes and quote marks.
  - 23 abstract quotes were machine-matched against the PubMed abstracts.
  - 20 quotes were read in context in the PMC full text: WAO 2020 ×5, Turner 2019 ×1, Miller 2023 ×3, Bizjak 2025 ×4, Engler Markowitz 2025 ×3, Fukunaga 2023 ×4.
- **Dropped-word check.** Every quote that carries a negative or a direction is intact in the PMC text, and the surrounding sentence reads correctly: "not diagnostic", "cannot be described as life-threatening", "should not be the aim", "never when the trigger is absent", "not relevant". No quote relies on glued text; the Table 6 CSU cell is correctly cut before "knownor".
- **Fit with the site.** I compared every [LINK] and [repeat] sentence with urticaria.json and common.json. UR-2.3 now reads 「寒冷性蕁麻疹：游泳等水上活動讓全身受冷，可能引起全身性的過敏反應，下水前先問醫師。」 Its only link is 寒冷性蕁麻疹 (cold-urticaria); 「全身性的過敏反應」 links to nothing.
- **Length and register.** All def ≤ 64 CJK characters, example ≤ 23, note ≤ 39, so all are within limits. autoimmune (64) and csu-cindu (63) are slightly above the ideal 60, which is acceptable. No 你 anywhere.

---

## autoimmune — minor

**Checked**
- The def matches Miller 2023 (PMC9918670): "Autoimmunity can be considered as the presence of self-reactive adaptive immune components, and autoimmune diseases can be thought of as autoimmunity plus clinically apparent pathology"; "While autoantibodies alone are not diagnostic for disease, they do define the presence of autoimmunity."
- It also matches Lleo 2010 (abstract): "The critical function of the immune system is to discriminate self from non-self."
- The translation is faithful:
  - 外來的東西 is an acceptable plain-language rendering of "non-self".
  - 針對自己身體 renders "self-reactive" without adding "attack".
  - 明顯的病變 renders "clinically apparent pathology".
- Example: GALEN 2026 says "autoimmune disease such as systemic lupus" (verified). The site's SLE page is titled 紅斑性狼瘡.
- Note, both GALEN quotes verified in PMC:
  - "CU is predominantly an autoimmune condition" matches UR-3.1 and UR-M1.
  - "In more than 50% of CSU patients, the pathophysiology is driven by two main autoimmune mechanisms: Type I (autoallergy) involving IgE autoantibodies against autoallergens, and type IIb involving IgG autoantibodies" is rendered faithfully as 「超過一半自發型病人的病情和自體抗體有關」. 「有關」 slightly softens "driven by", and the population (CSU = 自發型) is correct.

**Problem (site fit).** The entry is page-scoped and is also linked at **CM-5.1** on the common page (vaccines; [repeat] at CM-5.3). There the note is out of place:
- 「自發型」 is never explained on that page.
- 「國際指引」 reads as if it were the vaccine guideline.
- Urticaria facts are off-topic in a vaccination sentence.

On the urticaria page, the first half of the note repeats UR-3.1 word for word.

**Fix A (preferred; works on both pages).** Change the note to:
「自體抗體也可能出現在健康的人身上；單憑自體抗體，不能診斷自體免疫疾病。」 (35 characters)
- Supporting quotes:
  - Miller 2023, PMID 36446151 (PMC9918670): "While autoantibodies alone are not diagnostic for disease, they do define the presence of autoimmunity."
  - Lleo 2010, PMID 19963079 (abstract): "Antibodies against self-antigens are also found in cancer, during massive tissue damage and even in healthy subjects."
- Changes to the evidence list:
  - Add the Lleo quote as an evidence row.
  - Move the two GALEN note rows into reviewer_notes.
  - Keep the GALEN lupus row, which supports the example.

**Fix B (if you want to keep the urticaria figure).** Change the note to:
「慢性蕁麻疹也和自體免疫有關：國際蕁麻疹指引指出，超過一半的慢性自發型蕁麻疹和自體抗體有關。」 (45 characters)
- This reads correctly on any page.
- Support: the two GALEN quotes already in the evidence list (PMID 41649409, §3.3 and §4).

---

## csu-cindu — OK

**Checked all 12 quotes.**
- Def:
  - ">6 weeks": Kolkhir abstract, and GALEN Table 6.
  - Spontaneous appearance: GALEN Table 6.
  - No definite trigger (CSU) versus definite, subtype-specific triggers (CIndU): Kolkhir, and GALEN §3.2.
  - 「足夠強」 renders "at the individual threshold level" (§3.2).
  - The examples 冷／受壓／陽光 come from GALEN §3.2 and WAO 2012 Table 1.
- Example: GALEN Table 6 legend.
- Note:
  - The two types can co-exist: "CU patients can concomitantly show more than one form of CU … and they often do."
  - CSU can be worsened by "stress and infections" (§3.2).
- Site fit:
  - The intro link and all 14 repeats use 自發型／誘發型 to mean chronic spontaneous and chronic inducible urticaria.
  - The intro also lists 熱 as a trigger; the def's 「如…」 list leaves it out, which is not a conflict.
- No changes.

---

## cold-urticaria — OK (housekeeping)

**Checked**
- Def: Maltseva 2021 abstract says cold urticaria is a CIndU form with wheals and/or angioedema "in response to cold exposure", and that wheals "usually develop on rewarming" (verified).
- Example:
  - WAO 2012 Table 1: "cold objects/air/fluids/wind".
  - Bizjak 2025 triggers, including "ingestion of cold food or drinks".
  - GALEN §5.2.2: wind chill.
- Note:
  - Bizjak abstract: "most commonly triggered by full-body cold exposure, such as swimming".
  - WAO 2012: "systemic reactions … when patients jumped into cold water".
- Fit with the new UR-2.3 wording: the note's 嚴重過敏反應 is consistent with 「全身性的過敏反應」 (anaphylaxis is a systemic allergic reaction) and correctly conveys the risk. UR-2.4 (寒風) matches the example's 冷風.

**Housekeeping.** reviewer_notes still say "Site UR-2.3 (swimming → 全身性反應)". Change this to "→ 全身性的過敏反應".

---

## pressure-urticaria — OK

**Checked**
- Def:
  - WAO 2012 Table 1: "3-12 h latency".
  - Kulthanan 2020: "recurrent erythematous and often painful swelling after the skin is exposed to sustained pressure".
  - Kulthanan 2025: "chronic inducible subtype"; lesions appear "within 4 to 6 hours".
  - 「過了幾個小時」 stays within every reported latency.
- Example and note: the GALEN §5.2.2 and WAO 2012 bag-handle / "force per area" sentences (verified).
- 「壓力」 here means physical pressure. 「受壓」 and 「力量除以面積」 make that clear, so it won't be confused with psychological 壓力 on UR-1.4.
- No changes.

---

## solar-urticaria — minor

**Checked**
- Def: Engler Markowitz 2025 (PMC):
  - "classified as a subtype of inducible (physical) urticaria".
  - "rapid onset of pruritic erythema and wheals within minutes of exposure to light".
  - "most commonly within the ultraviolet A (UVA) and visible light (VL) spectra".
- WAO 2012 Table 1.
- Note: GALEN Table 8 and §5.2.2.
- Safety: 「可能有助」 matches GALEN's "may be important" and does not claim that sunscreen protects. Engler Markowitz notes the "limited effectiveness of sunscreens", but no change is needed.

**Problem (wording).** The def says 紫外線A, but the note and site UR-2.T say UV-A, and the uva-uvb glossary entry uses UVA／UV-A. That gives two names for the same thing in one popup.

**Fix.** Change the def to:
「日光性蕁麻疹是誘發型蕁麻疹的一種：皮膚照到光線後幾分鐘內，就冒出會癢的紅斑和膨疹；引發的光線多為紫外線A（UV-A）或可見光。」 (63 characters)
- Support: Engler Markowitz 2025, PMID 40869562 (PMC12386910): "most commonly within the ultraviolet A (UVA) and visible light (VL) spectra, as determined by phototesting".

---

## cholinergic-urticaria — OK

**Checked**
- Def:
  - Fukunaga 2023 (PMC, Introduction): "pinpoint, highly pruritic, or often painful wheals with surrounding erythema. These wheals occur after sweating induced by an increase in the body temperature, which occurs in response to hot bathing, physical exercise, and emotional stress".
  - Fukunaga abstract: a subtype of CIndU.
  - WAO 2012: core body temperature; exercise or emotional distress.
- Note: Fukunaga's differential-diagnosis section: "must be differentiated from EIA…" and "Strenuous exertion may provoke both EIA and CholU". This matches UR-S2 (請就醫讓醫師區分).
- The drafter was right not to say "exercise is fine": that would be unsafe next to UR-S2.

---

## wheal — OK

**Checked**
- Def:
  - WAO 2012 (PMC, 'Definition and Classification'): "sudden appearance … a cutaneous swelling of variable size, almost invariably surrounded by a reflex erythema, with associated itching or, sometimes, a burning sensation, and of transient nature, with the skin returning to its normal appearance in usually 1 to 24 hours".
  - Bizjak 2025: superficial; vary in size and shape; "often surrounded by erythematous flare".
- Note: the GALEN §4 photographs sentence.
- Site fit: [LINK] at UR-1.5, UR-5.1 and UR-S1; [repeat] at UR-5.5 and UR-S3. All fit.

**Duration (requested check).** The def says 「通常在24小時內消退、恢復原狀」. It keeps WAO's "usually" hedge and its 24-hour upper limit, and drops only the 1-hour lower bound. **Keep it as is.** Writing 「通常1到24小時」 would contradict the inducible-urticaria wheals described on the same page:
- GALEN 2026 §3.2 (PMID 41649409): "the symptoms appear usually within 10 min after exposure to the trigger and resolve within 1–3 h after cessation of exposure". The PMC extraction drops the subject word ("In most types of, the symptoms…"); from context it is CIndU.
- Maltseva 2021 (PMID 33249577, abstract): cold-induced wheals "resolve within an hour".

On 常有一圈紅暈: 常 is weaker than WAO's "almost invariably" but matches Bizjak's "often", which is acceptable.

---

## angioedema — OK (optional safety addition)

**Checked**
- Def:
  - WAO 2012: "sudden and pronounced swelling of the deep dermis and subcutaneous tissue or mucous membranes, with a painful rather than an itching sensation and a slower resolution than for wheals that can take up to 72 hours".
  - GALEN §3.3: lower dermis and subcutis.
  - DANCE, Weller 2013 and Bizjak (all verified).
  - 「可能會痛而不是癢」 softens WAO's categorical wording. This is justified by Weller 2013 ("may be painful") and GALEN Table 11, where the AAS asks about "pain, burning, itching".
- Note: DANCE ("may exhibit wheals or not") and GALEN §4.2.1. Matches UR-S3.

**Optional.** The popup appears on UR-5.T (the diary card) and never says that throat swelling is dangerous. If you want to add that, change the note to:
「可和膨疹一起或單獨出現；只有腫脹時請醫師找原因。喉嚨腫脹可能危及生命。」 (35 characters)
- Supporting quotes:
  - WAO 2012, PMID 23282382 (PMC3651155): "Angioedema of the upper airway can be life threatening." (add this as an evidence row)
  - DANCE, PMID 38670233 (abstract): "may exhibit wheals or not".
  - GALEN §4.2.1 sentence already in the evidence list.

---

## anaphylaxis — OK (housekeeping)

**Checked**
- Def:
  - WAO 2020 (abstract and Introduction): "Anaphylaxis is the most severe clinical presentation of acute systemic allergic reactions." 「最嚴重的一種全身性過敏反應」 renders this faithfully. WAO 2020 also says "Anaphylaxis represents the most severe end of the spectrum of allergic reactions."
  - 「通常發作很快…可能危及呼吸或血液循環，甚至致命」 matches Turner 2019 (WAO Anaphylaxis Committee, PMC): "usually rapid in onset and may cause death. Severe anaphylaxis is characterized by potentially life-threatening compromise in breathing and/or the circulation".
  - The word 可能 keeps the def consistent with WAO 2020: "the majority of anaphylaxis reactions cannot be described as life-threatening in themselves" ("cannot" is present in the PMC text).
- Example: **every item appears in** the WAO 2020 list "(eg, tingling in the extremities, sense of heat, sense of dizziness/fainting, swollen lips-tongue-uvula, shortness of breath, wheeze, stridor, collapse)". Nothing has been added.

  | Example item | WAO 2020 wording |
  |---|---|
  | 呼吸困難 | shortness of breath |
  | 咻咻聲 | wheeze |
  | 喘鳴 | stridor |
  | 嘴唇或舌頭腫 | swollen lips-tongue(-uvula) |
  | 頭暈或昏倒 | dizziness/fainting |

- Note:
  - 急症／立刻處理: WAO 2020 "medical emergency that requires rapid identification and treatment".
  - 不一定有皮膚症狀: Turner 2019 "may occur without typical skin features"; also "the possibility of anaphylaxis occurring in the absence of skin involvement".
  - Swimming in cold urticaria: Bizjak abstract.
- Alias: only 嚴重過敏反應 remains. UR-2.3 is not linked to this entry, and its new wording is consistent with the def.
- Safety: the entry stays clearly urgent and is consistent with UR-S1 (119).

**Housekeeping (not shown to patients)**
- (a) reviewer_notes still discuss the alias 全身性反應 and advise rewording UR-2.3; both have been done. Replace that passage with: "Alias 全身性反應 removed. UR-2.3 now reads 「…可能引起全身性的過敏反應…」 (AAAAI/ACAAI 2014 'systemic reactions') and is not linked to this entry; its popup is cold-urticaria, whose note cites Bizjak 2025."
- (b) In evidence row 5 (Bizjak abstract), `supports` still reads 「（alias「全身性反應」的語境）」. Change it to 「note：寒冷性蕁麻疹病人全身受冷可能發生」.
- (c) `aka` lists "systemic allergic reaction" as a synonym, but WAO 2020 treats anaphylaxis as a subset: "In this classification, only some grade 3 or grades 4–5 would be consistent with the definition of anaphylaxis, while grades 1–2 constitute non-anaphylaxis." (PMID 33204386). Change `aka` to "anaphylaxis".

**Optional (terminology consistency, visible to patients if sources are shown).** The source short names 「WAO 2020 全身性過敏反應指引」 and 「WAO 全身性過敏反應委員會 2019 定義修訂」, and S7 on the urticaria page, use 全身性過敏反應 to mean "anaphylaxis". This def uses the same words for the wider class that anaphylaxis belongs to. Consider renaming them 「WAO 2020 嚴重過敏反應指引」 and 「WAO 嚴重過敏反應委員會 2019 定義修訂」.

---

## stridor-wheeze — minor

**Checked**
- Def: Bizjak 2025 Table 2 (PMC): "wheeze (whistling sound, mainly during exhalation due to bronchoconstriction), stridor (high-pitched sound during inhalation due to airway obstruction)". Every clause is translated faithfully.
- Clark 2018 abstract (verified).
- Note: WAO 2020 lists both signs, and "medical emergency" (verified).
- Source quality: a quick PubMed search found no Tier 1–2 definition (the ERS nomenclature paper, PMID 26647442, has no definitions in its abstract and no PMC copy). I agree with Medium confidence.

**Is the mapping reasonable for Taiwanese readers?** Yes, with one caveat:
- 咻咻聲 for wheeze is the everyday Taiwanese way to describe a whistling, asthma-type breath sound.
- 喘鳴 for stridor is an accepted Taiwanese clinical rendering (吸氣性喘鳴).
- However, 喘鳴 is also widely used in Taiwan for **wheezing**, for example in asthma education. Many lay readers will therefore take 「咻咻聲或喘鳴」 as two words for the same sound.
- Safety is not affected: UR-S1 lists both as emergency signs, and the def separates them by breathing phase.

This is my judgment about Chinese usage; no PubMed source covers it, so please confirm.

**Problem 1 (precision).** Clark 2018 places the obstruction in the *upper* airway. Saying so also sharpens the contrast with wheeze, which comes from the 支氣管.

**Problem 2 (terminology).** The def should signal which sense of 喘鳴 the site uses.

**Fix.** Change the def to:
「咻咻聲是呼吸時像吹口哨的聲音，多在吐氣時出現，因為支氣管收縮；喘鳴在這裡指吸氣時發出的尖銳高音，因為上呼吸道阻塞。」 (57 characters)
- Supporting quotes:
  - Bizjak 2025, PMID 41044831 (PMC12511795), Table 2 quote above.
  - Clark 2018, PMID 30358678 (abstract): "Stridor is a high-pitched respiratory sound that signals upper airway obstruction."

**Optional (site text, your call).** UR-S1 could read 「…呼吸有咻咻聲、吸氣時有尖銳高音（喘鳴）…」.

---

## uas7 — OK

**Numbers (requested check).** GALEN §4.2.6 (PMC): "(0–3 for wheals +0–3 for pruritis) for each day is summarized over 1 week (7 days) for a maximum of 42"; "daily self‐assessments by the patient"; "sum of daily scores over 7 consecutive days … monitor disease activity and treatment response in patients with CSU". The def's figures all match:
- 0–3 points each for wheals and itch.
- Scored daily by the patient.
- Summed over 7 consecutive days, maximum 42.
- Used for 自發型 patients.
- Used to track 病情活躍度 and 治療效果.

The Table 11 anchors are 0–3. The note matches "Given the fluctuating nature of urticaria, the most reliable way…". The entry matches UR-5.1.

**Optional (site level).** "Activity Score" is 活性 in 蕁麻疹活性分數 but 活動 in 血管性水腫活動分數. You may want to make them the same.

---

## uct — OK

**Numbers (requested check).**
- GALEN §4.2.6: "simple four‐item tool"; "recall period is 4 weeks"; "cutoff value for well‐controlled disease is 12 out of 16 possible points".
- The def matches: 4 questions, 4-week recall, maximum 16, 12 or more means well controlled.
- Bizjak 2025 (PMC) confirms this independently: "It contains 4 questions, each scored from 0 to 4; a total score of ≥12 indicates controlled disease."
- Weller 2014 abstract: 4 items, 4-week recall, covers CSU and CIndU.

**Note.**
- Applies to all forms of CU (GALEN): verified.
- The goal is UCT = 16 (GALEN §5.1): verified.
- The Fig. 3 legend ("UCT 12–15 … a step up might also be required") explains why the note gives 16 as the goal.
- Consistent with UR-5.4, and nothing invites patients to adjust treatment on their own.

---

## aas — OK

**Numbers (requested check).**
- Weller 2013 abstract: "consisted of five items".
- GALEN §4.2.6: "AAS day sum score (0–15), 7 AAS day sum scores to an AAS week sum score (AAS7, 0–105)".
- GALEN Table 11 shows five items scored 0–3, after an unscored yes/no question ("Have you had a swelling episode in the last 24 h?"). That gives a daily maximum of 15 and is consistent with 「5題」.

**Population.** Weller covers recurrent angioedema in general, and GALEN covers CSU with angioedema, so 「有血管性水腫的病人」 is fine.

**Note.** Matches "CSU patients who experience wheals and angioedema should use the UAS7 and the AAS in combination". Consistent with UR-5.T.

---

## Limits of this check
- Whether 喘鳴 reads as stridor in Taiwanese usage is my judgment as a reviewer and cannot be checked against a source.
- WAO 2020's Table 1 (its list of definitions) is missing from the PMC text. The formal definition is quoted from Turner 2019, which I verified. Whether WAO 2020 repeats that wording word for word is still unverified, as the drafter also noted.
- The glossary popup renderer is not yet in template.html. I assumed that patients see def, example, note, label and sources (per VERIFY.md), and that `aka` is metadata only (per the merge.py comment).
