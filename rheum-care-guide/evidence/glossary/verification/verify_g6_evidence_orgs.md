# Independent verification: g6_evidence_orgs

**Summary: 23 entries checked: 14 OK, 9 minor, 0 major.**
There is also one **site-level problem**: SJ-M1 needs a population caveat, and newer Sjögren-specific trials disagree with each other (see §A).
The new entry `good-practice` was drafted and validated: /home/claude/glossary/new_good-practice.json.

| Verdict | Entries |
|---|---|
| OK | systematic-review, observational, clinical-significance, org-acr, org-bsr, org-nice, org-asas, org-wao, org-tfos, org-tra, org-aaaai, org-bsaci, org-ects, org-sf |
| minor | guideline, meta-analysis, rct, placebo, certainty, expert-consensus, org-eular, org-who, org-galen |
| major | none |

## What was checked (all entries)

- **Citations.** I fetched PubMed metadata for all 53 cited PMIDs. First author, title, journal, volume/issue/pages and DOI match in every case. Every `evidence[].doi` and `pmcid` matches the PubMed record, and every evidence PMID is listed in that entry's `sources`.
  - Some citation years differ from PubMed's (epub) year because they use the print-issue year, which matches the volume. This is correct, not an error. Affected records: Richette 2017 (PubMed 2016), Furer 2020 (2019), Ramos-Casals 2020 (2019), Wei 2020 (2019), Lee 2021 (2020), Zuberbier 2022 (2021), Gwinnutt 2023 (2022), Ramiro 2023 (2022).
- **Quotes.** All 120 evidence quotes were machine-checked as verbatim after normalising whitespace, quote marks and dashes: 60 against PubMed titles or abstracts, and 60 against PMC full text (22 PMC articles saved locally).
  - I read the context around every quote. None hides a dropped "not".
  - Extraction-glued words exist near some quotes (BSR 2025 "poweredmanual"; ACR 2022 "Using electrotherapy is conditionally recommended", where "not" is lost). No glued word falls inside a quoted string.
- **Site fit.** I read every [LINK] and [repeat] sentence in occurrences.md, plus the legend in src/template.html.
- **Language and safety.** I checked character counts (all within limits), use of 您/你 (no 你 anywhere), unexplained jargon, and anything that could prompt a change in medication.
- **Pages I could not read.** The full text of the Cochrane review CD009603 (PMC7100870) was not available:
  - the PubMed full-text tool returned the abstract only;
  - WebFetch of the PMC page hit a reCAPTCHA;
  - Europe PMC was refused by the proxy (rate limit).
  §A therefore relies on the PubMed and PMC abstract, as the task asked.

---

## §A. Special check: acupuncture vs placebo for dry mouth (SJ-M1 and the placebo example)

### 1. Population of the Cochrane evidence: radiotherapy-induced dry mouth only

The source is Furness 2013, PMID 24006231 (pub2 is PMID 23996155, same abstract).

The five acupuncture trials were all in people with dry mouth after radiotherapy:
- "Five small studies (total 153 participants, with dry mouth following radiotherapy treatment) compared acupuncture with placebo."

The symptom result comes from only two of them:
- "Two trials reported outcome data for dry mouth in a form suitable for meta-analysis. The pooled estimate of these two trials (70 participants, low quality evidence) showed no difference between acupuncture and control in dry mouth symptoms"

The only Sjögren's trials in the review tested electrostimulation, not acupuncture:
- "Two small studies, both at high risk of bias, compared the use of an electrostimulation device with a placebo device in participants with Sjögren's Syndrome (total 101 participants)."

The authors' conclusions:
- "There is low quality evidence that acupuncture is no different from placebo acupuncture with regard to dry mouth symptoms, which is the most important outcome. This may be because there were insufficient participants included in the two trials to show a possible effect or it may be that there was some benefit due to 'placebo' acupuncture which could have biased the effect to the null."
- "There is some low quality evidence that acupuncture results in a small increase in saliva production in patients with dry mouth following radiotherapy."
- "There is insufficient evidence to determine the effects of electrostimulation devices on dry mouth symptoms or saliva production in patients with Sjögren's Syndrome."

**Caveat on the review itself.** Its plain-language summary (in the PMC abstract field) says:
- "The causes of dry mouth were radiotherapy for oral cancers in four trials, Sjögren's syndrome in three trials, medication-related in one trial, and in the remaining trial participants had a range of causes of dry mouth."

These counts do not reconcile with the abstract: five radiotherapy acupuncture trials plus one radiotherapy electrostimulation trial makes six, not four. The full text could not be read, so this cannot be resolved here. The abstract's results and conclusions consistently describe the acupuncture evidence as radiotherapy-related.

### 2. BSR 2025 repeats the conclusion without stating the population

Full guideline, PMID 38621708 (PMC12013823), key question 7: "In people with SD who have sicca (dryness) symptoms of the mouth, what is the most clinically effective topical treatment?"

The sentence about the topical-treatment review does name the population:
- "A Cochrane review [] of topical treatments for dry mouth of any cause (including SD) found no strong evidence supporting one topical therapy over another."

The next sentence, about non-drug treatments, does not:
- "A Cochrane review of non-pharmacological therapies for dry mouth [] including acupuncture (five studies), electrostimulation (three studies) and poweredmanual toothbrushing (one study) found low quality evidence that acupuncture is no different from placebo …"
- The 5 acupuncture / 3 electrostimulation / 1 toothbrush split identifies this review as Furness 2013.

The executive summary (PMID 38785300, PMC12013822, cited as the site's S2) is the same:
- "A Cochrane review of non-pharmacological therapies for dry mouth [] concluded that acupuncture was no different from placebo, there was insufficient evidence on the effect of an electrostimulation device and no difference between manual and powered toothbrushing symptoms."

### 3. Sjögren-specific evidence on PubMed that BSR 2025 did not discuss (all quotes verified in abstracts)

**Systematic reviews**
- Al Hamad 2019, Oral Dis 25(4):1027-1047, PMID 30086205, DOI 10.1111/odi.12952. This review covers dry mouth in Sjögren's. Its abstract names pilocarpine, rituximab and interferon-alpha, then states: "The use of other treatment modalities cannot be supported on the basis of current evidence." Acupuncture appears among its keywords. Search date: "up to February 2018".
- Hackett 2015, Rheumatology 54(11):2025-32, PMID 26135587. "The included studies investigated the effectiveness of an oral lubricating device for dry mouth, acupuncture for dry mouth, lacrimal punctum plugs for dry eyes and psychodynamic group therapy for coping with symptoms. Overall, the studies were of low quality and at high risk of bias."

**Sham-controlled randomised trials in Sjögren's**
- No difference from sham (Zhou 2022, Front Med 9:878218, PMID 35602489, DOI 10.3389/fmed.2022.878218):
  - "A total of 120 patients with primary Sjögren's syndrome were randomized in a parallel-group, controlled trial. Participants received acupuncture or sham acupuncture for the first 8 weeks, then were followed for 16 weeks thereafter."
  - "In patients with primary Sjögren's syndrome, acupuncture did not satisfactorily improve symptoms compared to placebo."
- Benefit reported (Gomes-Silva 2025, Clin Rheumatol 44(5):1971-1982, PMID 40178679, DOI 10.1007/s10067-025-07410-2):
  - "Forty-six patients were randomized and 27 completed the study (acupuncture, n = 15; sham, n = 12)."
  - "The acupuncture group exhibited significant improvement in total ESSPRI and ESSPRI dryness scores."
- Benefit reported (Li 2026, Chin J Integr Med, epub 2026 Oct 2, PMID 42826003, DOI 10.1007/s11655-026-4253-2):
  - "included 138 pSS patients who were equally and randomly assigned to the treatment group or the sham acupuncture control group (69 cases in each group)"
  - "Compared with the control group, the treatment group had significantly lower ESSPRI scores, eye dryness NRS, and mouth dryness NRS and significantly higher salivary flow rates, Schirmer test results, and BUT scores (all P<0.05)"
  - Both arms also took hydroxychloroquine.

**Older trial with no-treatment control**
- List 1998, PMID 9669460. The control group had no active treatment, not placebo: "No statistically significant differences between the acupuncture group and the control group were seen in unstimulated salivary secretion or most of the subjective variables."

### 4. Verdict and proposed text (site file, for the physician)

**SJ-M1 needs a caveat.** As written, 「研究回顧發現，針灸改善口乾的效果和安慰劑沒有差別（證據品質低）」 faithfully restates BSR 2025. On the Sjögren page, however, readers will assume the trials were in Sjögren's patients. The acupuncture evidence behind it is indirect (radiotherapy-induced dry mouth only). In addition, sham-controlled trials in Sjögren's itself now disagree: 2022 found no difference; 2025 and 2026 report benefit.

Two options for the physician:

- **(A) Minimal fix**, keeps the BSR/Cochrane basis and label:
  - Text: 「研究回顧發現，針灸改善口乾的效果和假針灸（安慰劑）沒有差別（證據品質低）；不過這些研究的對象是放射治療後口乾的人。」
  - Support: PMID 24006231, "Five small studies (total 153 participants, with dry mouth following radiotherapy treatment) compared acupuncture with placebo."
- **(B) Fuller fix**:
  - Text: 「針灸能否改善乾燥症的口乾，目前證據不足：研究回顧中的針灸研究對象是放射治療後口乾的人，效果和假針灸沒有差別（證據品質低）；乾燥症病人的試驗結果不一致。」
  - Support: PMID 24006231 as above; PMID 30086205, "The use of other treatment modalities cannot be supported on the basis of current evidence."; PMID 35602489 (no difference) versus PMIDs 40178679 and 42826003 (benefit).
  - This adds primary RCTs and a non-guideline systematic review as sources, so the label would need e.g. 「BSR 2025・指引說明；研究顯示」.

**Placebo example.** It is accurate but needs the population added. See the placebo entry below.

---

## §B. Special check: expert-consensus note (rewritten)

Note under review: 「常用在缺乏高品質研究證據時；有些指引會把它列在較低的證據等級。」 **Both halves are supported.**

First half, 「常用在缺乏高品質研究證據時」:
- PMID 33075377 (PMC): "The formal consensus process was deemed especially critical in view of the lack of high-quality evidence."
- PMID 41220535 (PMC): "When systematic reviews are not feasible but recommendations are still needed, developers may issue consensus statements. These rely on expert consensus, logical reasoning, and limited available data."
- Optional extra evidence, an abstract already cited in org-bsaci: PMID 25711134, "Where evidence was lacking, a consensus was reached by the experts on the committee."

Second half, 「有些指引會把它列在較低的證據等級」:
- PMID 38621708 (PMC): "…summarize the quality of the body of evidence for each recommendation as high (A), moderate (B) or low/very low (C) …" followed by "Please note that C will include expert consensus where we could find no evidence within the literature."
- Also consistent with PMID 41649409, where the label is "Expert consensus" unless "further supported by evidence from a systematic review".

The remaining problems are in the **def**, not the note. They are listed under the expert-consensus entry below.

---

## §C. Organisation names (English full name as printed in a PubMed-indexed publication by the body)

| Entry | `en` | Printed in (PMID, where) | Result |
|---|---|---|---|
| org-acr | American College of Rheumatology | 32391934, 37227071, 37845798 (titles) | ✓ |
| org-eular | European Alliance of Associations for Rheumatology | 42036268 abstract (EULAR 2025); old name in 27457514, 31413005 | ✓ |
| org-bsr | British Society for Rheumatology | 28549177, 38621708, 42336388, 40199504 (titles) | ✓ |
| org-nice | National Institute for Health and Care Excellence | 38274510 (PMC text; editorial *about* NICE). NICE's own guidelines are not PubMed text records | ✓ (best available) |
| org-asas | Assessment of SpondyloArthritis international Society | 36270658 abstract | ✓ |
| org-who | World Health Organization | 33239350 title | ✓ |
| org-galen | Global Allergy and Asthma Excellence Network | 41649409 abstract and introduction. The abbreviation list prints "Global Asthma and Allergy Excellence Network" (already in RN) | ✓ |
| org-wao | World Allergy Organization | 33204386 abstract | ✓ |
| org-tfos | Tear Film & Ocular Surface Society | 37659474 abstract ("and" form in 41005521) | ✓ |
| org-tra | Taiwan Rheumatology Association | 31777200 title | ✓ |
| org-aaaai | American Academy of Allergy, Asthma & Immunology; American College of Allergy, Asthma & Immunology | 24766875 abstract | ✓ |
| org-bsaci | British Society for Allergy and Clinical Immunology | 25711134 abstract | ✓ |
| org-ects | European Calcified Tissue Society | 39556468 title and abstract | ✓ |
| org-sf | Sjögren's Foundation | 33075377 abstract (old name: 27431353, 27390247) | ✓ |

No entry invents an official Chinese name. All Chinese glosses are descriptive.

---

## Per-entry results

### guideline: minor
- **Checked:** 5 quotes (all verbatim), 4 sources. Def is faithful to the IOM definition quoted in PMID 41220535. Example (59 countries, 107 societies) matches the 41649409 abstract. Note matches ACR 2022 GRADE wording and the site legend.
- **Problem 1 (consistency of label).** The label 「IOM 2011・定義」 names a report that is neither PubMed-indexed nor listed in `sources`; the definition is read second-hand in Morizane 2025. The placebo entry handles the same situation with 「（文獻引述）」.
  - Proposed label: 「IOM 2011・定義（文獻引述）」
  - Support: PMID 41220535, "The Institute of Medicine (IOM)defined clinical practice guidelines (CPGs) in 2011 as: "Clinical practice guidelines are statements…""
- **Problem 2 (fit, optional).** The [LINK] in CM-M1 is the WHO 2020 *public-health* guideline, which is aimed at the general population, not patients. 「讓病人得到最好的照護」 fits there less well.
  - Optional def: 「臨床指引是一套照護建議，目的是讓照護做到最好；建議依據有系統整理過的研究證據，並比較不同做法的好處與壞處。」 (49 CJK characters)
  - Support: PMID 41220535, "…recommendations intended to optimize patient care that are informed by systematic reviews of evidence and assessments of the benefits and harms of alternative care options."
  - Context: PMID 33239350 describes WHO's as "evidence-based public health recommendations".

### systematic-review: OK
- **Checked:** 6 quotes verbatim (PRISMA Box 1 definition, scope sentence, Skare 2023 ×3, Furness abstract). Example numbers are correct: 4 databases; 5 Sjögren's studies; 28+12+107+33+60 = 240 women.
- **Fit:** fits SJ-M1 (Cochrane review) and SJ-M3 (Skare). The RN already flags the radiotherapy population; see §A for the stronger caveat.

### meta-analysis: minor
- **Checked:** 8 quotes verbatim (PRISMA Box 1 ×2; Chasset abstract ×6). The def merges PRISMA's "statistical synthesis" and "meta-analysis of effect estimates" definitions acceptably.
- **Problem (precision of example).** 「合併了10項研究、共1398名…病人的資料」 can be read as pooling raw patient data. Chasset pooled study-level odds ratios.
  - Proposed example: 「2015年一篇統合分析，合併了10項研究（共1398名皮膚型狼瘡病人）的結果。」
  - Support: PMID 25648824, "Individual study odds ratios were combined in the meta-analysis using a random effects model." and "Of 240 citations retrieved, 10 studies met inclusion criteria, for a total of 1398 patients."
- **Information:** the existing RN about 「明顯」 in SL-2.3 (OR 0.53, 95% CI 0.29–0.98) is correct.

### rct: minor
- **Checked:** 6 quotes verbatim (CONSORT E&E item 8a, Hariton ×2, CONSORT statement, ACR 2022 Discussion, ACR 2020 gout). The alias 小型試驗 in GT-M3 is used in the RCT sense (✓).
- **Problem 1 (term name).** 「隨機對照試驗（試驗）」 reads oddly as a heading.
  - Proposed term: 「隨機對照試驗」. Wording only; no quote needed.
- **Problem 2 (optional, slight understatement).** 「是評估治療效果的標準方法」 renders "gold standard" and drops "when appropriately designed".
  - Proposed note: 「隨機分組讓各組條件相近；設計良好時被視為評估治療效果的黃金標準，但人數少時結果較不精確。」 (41 CJK characters)
  - Support: PMID 20332509, "Randomised controlled trials, when appropriately designed, conducted, and reported, represent the gold standard in evaluating healthcare interventions."

### observational: OK
- **Checked:** 10 quotes verbatim (Grimes ×2, STROBE, STROBE E&E, Thiese, Zhang ×2, GRADE, ACR 2020 ×2). The cherry example is a case-crossover comparison of intake and no-intake periods (✓).
- **Fit:** GT-3.T (cohort) and GT-M4 both fit.

### placebo: minor
- **Checked:** 9 quotes verbatim (Hernández ×4 including the WHO definition in Table 3, Hróbjartsson ×2, Furness, Evers, Skare). The note is supported: placebo can influence patient-reported outcomes, and placebo is used to establish actual efficacy.
- **Problem 1 (example in def not in quotes).** 「假藥丸」 appears in no evidence quote.
  - Fix: keep the def and add this evidence: PMID 25423149 (PMC4244087, Table 3, NIH row), "A placebo is a pill or liquid that looks like the new treatment but does not have any treatment value from active ingredients."
- **Problem 2 (population of example; see §A).** Choose one:
  - Option (a): 「放射治療後口乾的研究中，針灸是和「假針灸」比較。」
    - Support: PMID 24006231, "Five small studies (total 153 participants, with dry mouth following radiotherapy treatment) compared acupuncture with placebo."
  - Option (b), Sjögren-specific: 「一項乾燥症試驗中，針灸是和「假針灸」比較。」
    - Support: PMID 35602489, "A total of 120 patients with primary Sjögren's syndrome were randomized … Participants received acupuncture or sham acupuncture for the first 8 weeks…"

### certainty: minor
- **Checked:** 12 quotes verbatim (GRADE abstract, GALEN 2026 ×2, BSR 2026 ×4, PRISMA, Gwinnutt, ACR 2020, BSR 2025 ×2). The def, example and site fit are all ✓: GT-M4 = "low or very low", SJ-M1 = "low quality", SL-M4 = "very low" and "low".
- **Problem (slight overstatement).** 「新研究很可能影響這個結果，甚至改變結論」 makes the change of conclusion sound "very likely"; the source says "may change the conclusion". 「舊說法」 is also too strong, because BSR 2025 and GALEN 2026 still use "quality".
  - Proposed note: 「確定性低，表示新研究很可能改變這個結果，結論也可能不同；「證據品質」是較早的說法，現在仍常用。」 (40 CJK characters)
  - Support:
    - PMID 35654458 (PMC): "GRADE defines low quality evidence as evidence where further research is very likely to have an important influence on our confidence in the estimates, or is likely to change the estimate."
    - PMID 42336388 (PMC): "…suggest that further research is likely or very likely to have an important impact on the confidence in the intervention effect estimate and may change the conclusion."
    - PMID 33782057: "…the shift from assessing "quality" to assessing "certainty" in the body of evidence."
    - PMID 38621708: "…to summarize the quality of the body of evidence…"
    - PMID 41649409: "…the quality rating indicates the confidence that can be attributed to a result."

### clinical-significance: OK
- **Checked:** 6 quotes verbatim (Devji ×2, Gwinnutt ×3, ACR 2020). Fits GT-M3 and RA-M3.
- **Optional:** 「（例如病人感覺得到）」 suits patient-reported outcomes better than serum urate in GT-M3. It is framed as an example, so it is acceptable.

### expert-consensus: minor
- **Checked:** 12 quotes verbatim. The note is supported (see §B). The example matches the Yu 2018 abstract.
- **Problem 1 (redundancy).** The def ends 「常用在研究證據不足的問題」, which the note repeats.
- **Problem 2 (overstatement for the GT-5.1 link).** The def says agreement is reached 「經過討論和投票…同意的人要達到事先訂好的比例」. The Taiwan 2018 consensus abstract reports only "consensuses from two multidisciplinary meetings", with no vote or threshold stated.
- Proposed def, note unchanged: 「專家共識是一群專家討論後，對建議達成的共同意見；正式的共識方法通常會投票，同意的人要達到事先訂好的比例。」 (48 CJK characters)
- Support:
  - PMID 27390247: "…using a modified Delphi process. A CEP agreement level of 75% was set as a minimum for adoption of a guideline recommendation."
  - PMID 41649409 (PMC): "…strong consensus was defined as more than 95% agreement, whereas consensus was defined as 75%–95% agreement."
  - Optional Taiwan example, PMID 41546150: "The expert panel reviewed and refined statements through two meetings with anonymous voting based on a 5-point Likert scale. Consensus is defined as ≥ 75% agreement to the proposed statements."
  - PMID 29363262: "…as well as consensuses from two multidisciplinary meetings…"

### org-acr: OK
Checked 4 quotes; the def's examples match the three guideline titles.

### org-eular: minor
- **Checked:** 7 quotes verbatim. The name change is supported by PMID 38587826 ("formerly the European League Against Rheumatism"), and the note's years are correct.
- **Problem (narrow wording).** 「治療建議」 does not fit what the site cites under EULAR: lifestyle 2021, physical activity 2025, vaccination 2019, non-pharmacological management 2024.
  - Proposed def: 「歐洲的風濕病學會聯盟，發表多份風濕病照護建議；英文全名已更改，縮寫仍是EULAR。」
  - Support:
    - PMID 35260387: "…develop recommendations on lifestyle behaviours for rheumatic and musculoskeletal diseases (RMDs)."
    - PMID 42036268: "…recommendations for physical activity (PA) in people with inflammatory arthritis (IA) and osteoarthritis (OA)…"
    - PMID 31413005: "…recommendations for vaccination in adult patients…"

### org-bsr: OK
Checked 5 quotes. The four guideline topics match the titles; "英國" is supported by PMID 38274510.

### org-nice: OK
Checked 4 quotes (Roddy 2024 PMC ×3, BJGP 2018 title). 「國家級」 is a description of "National", not an official name.

### org-asas: OK
Checked 1 quote (abstract). The def correctly explains the linked alias "ASAS-EULAR".

### org-who: minor
- **Checked:** 1 quote (title).
- **Problem (fit).** The [LINK] on the SLE page is SL-1.T 「WHO 2002・指引說明」, which is the UV-index guide, not a physical-activity guideline. CM-6.x cite the WHO 2002 and 2022 UV documents in the same way. The def implies the site cites only the 2020 PA guideline.
  - Proposed def: 「世界衛生組織；網站引用它發表的資料，例如2020年的身體活動與久坐行為指引。」
  - Support: PMID 33239350, title "World Health Organization 2020 guidelines on physical activity and sedentary behaviour."
  - The UV-index documents are not PubMed-indexed, so they are not described.

### org-galen: minor
- **Checked:** 6 quotes verbatim. The note about the old name in 2018 and 2022 is correct.
- **Problem (precision).** 「由它發起」 comes from the abstract only. The guideline's own introduction lists co-initiators.
  - Proposed def: 「全球性的過敏與氣喘專業網絡；2026年國際蕁麻疹指引由它和其他幾個學術團體共同發起，有59國、107個學會的代表參與。」
  - Support: PMID 41649409 (PMC, Introduction), "The guideline is an initiative of the Global Allergy and Asthma Excellence Network (GALEN) and its Urticaria and Angioedema Centers of Reference and Excellence (UCAREs and ACAREs), the European Dermatology Forum (EDF), the Asia Pacific Association of Allergy, Asthma and Clinical Immunology (APAAACI), the American Academy of Dermatology (AAD), the British Society for Allergy & Clinical Immunology (BSACI), and the Gulf Academy of Allergy and Clinical Immunology (GA2CI)". The 59 countries and 107 societies come from the abstract quote already in the entry.
- **Information:** the introduction says 213 experts, the abstract 210 delegates. The glossary uses neither number.

### org-wao: OK
Checked 3 quotes. The 2011 guidelines and 2020 guidance years are correct.

### org-tfos: OK
Checked 2 quotes. DEWS = Dry Eye Workshop ✓.

### org-tra: OK
- Checked 3 quotes. "2020" is the print year; the PubMed epub year is 2019.
- **Information for the physician:** the 2026 Taiwanese SLE consensus is issued as "Taiwan College of Rheumatology" (PMID 41546150). Whether this is the same body was not verifiable on PubMed, so leaving the two unlinked is correct.

### org-aaaai: OK
Checked 1 quote. The RN correctly notes the third body, the Joint Council.

### org-bsaci: OK
Checked 3 quotes.

### org-ects: OK
- Checked 2 quotes.
- Optional second example of ECTS osteoporosis advice: PMID 28789921, "The European Calcified Tissue Society (ECTS) formed a working group to perform a systematic review of existing literature on the effects of stopping denosumab and provide advice on management."

### org-sf: OK
Checked 4 quotes. The US location and the four guideline areas are supported.

---

## New entry: good-practice (written to /home/claude/glossary/new_good-practice.json)

**Format.** It is a single entry object, which is the format merge.py reads from `new_*.json`. Fields: cat "evidence", en "good practice statement", alias 「良好實務建議」, plus a `group` field. The JSON is valid. The alias collides with no existing alias.

**Text** (CJK character counts: def 63, example 18, note 28):
- def: 「良好實務建議是指引裡不分級的建議：專家共識認為這樣做的好處明顯大於壞處，但依據的多是間接證據（不是直接研究這個做法），所以不另評證據等級。」
- example: 「兒童癌症疲倦指引中的「定期評估疲倦程度」。」
- note: 「沒有分級不代表不重要；這類建議原本就是要當成強烈建議來看待。」
- label: 「GRADE・定義」

**Sources.** All 9 quotes were machine-verified (PMC full text or abstract):
- Dewidar 2022/2023 (BMJ EBM, PMID 35428694, PMC10313969), 5 quotes:
  - definition: "…actionable statements deemed to be necessary for practice (desirable effects … clearly outweigh its undesirable effects) but are supported by indirect evidence…"
  - "ungraded best or good practice statement"
  - GRADE "inappropriate"
  - "intended to be interpreted as strong recommendations"
  - "adding 'ungraded' next to the statement"
- Morizane 2025 (PMID 41220535): "grounded in expert consensus rather than direct evidence"
- ACR 2025 SLE guideline abstract (PMID 41187097): "ungraded, consensus-based good practice statements"
- Patel 2023 (PMID 37609066), for the example
- Bull 2020 (PMID 33239350), for the content of CM-1.T

**Caveats (also in the entry's reviewer_notes):**
1. **The WHO label is unconfirmed on PubMed.** "good practice" does not occur in the PMC text of Bull 2020. Table 4's heading for this advice is lost in extraction (text reads ":.If not currently meeting these recommendations…"). The label therefore rests on the WHO guideline book (site source S5, NBK566048), which is not PubMed-indexed; please confirm it there.
2. **The primary GRADE papers could not be quoted.** Guyatt 2015 (PMID 25660962) and Guyatt 2016 (PMID 27452192) have no abstract or PMC text in the tool.
3. **The example comes from a paediatric oncology guideline.** It can be dropped if it looks out of place.
4. **The site legend has no entry for 良好實務建議.** Consider adding one.
