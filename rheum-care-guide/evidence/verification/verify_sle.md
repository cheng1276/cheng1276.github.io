# Independent fact-check: 紅斑性狼瘡 (group "sle", rows SL-…)

Checked: 2026-10-06. Checker: independent verifier (did not write the content). Files checked: /home/claude/content/review_sle.md. Evidence notes consulted, treated as unverified: /home/claude/research/sle.md and /home/claude/research/common.md. No content or evidence file was edited.

Access used:
- PMC full text via PubMed MCP: BSR 2026 guideline (PMC13290301), BSR executive summary (PMC13290299), Blaess 2024 (PMC11002419), EULAR 2017 women's health (PMC5446003).
- PubMed abstracts/metadata: 42336388, 42336387, 37433575, 38580348, 27457513, 32090480, 37827694, 25648824, 31520802, 39191627, 37073886, 42373138.
- WebFetch: Parodis 2024 version-of-record PDF (shura.shu.ac.uk, 5 separate reads); SRUK lay summary of the EULAR non-pharmacological recommendations (independent document); ard.bmj.com/content/83/1/15 (EULAR 2023); ICNIRP-hosted WHO 2002 UV Index guide PDF; who.int UV index Q&A; cwa.gov.tw OBS_UVI page; iris.unibs.it published PDF of EULAR 2017 (2 reads).
- Not accessible: Europe PMC full-text XML for PMC5446003. The proxy refused it with HTTP 429 and said not to retry, so it was not retried. The shell is policy-blocked (CONNECT 403) for shura.shu.ac.uk, ebi.ac.uk and ard.bmj.com.

## 1. Summary counts

| Verdict | Rows |
|---|---|
| Critical | 0 |
| Major | 0 |
| Minor | 11 (SL-1.2, SL-1.T, SL-2.3, SL-3.5, SL-4.3, SL-4.4, SL-5.3, SL-6.1, SL-6.4, SL-6.T, SL-S1) |
| OK | 28 |
| **Total rows** | **39** |

Quote verification (74 quote entries in the evidence column):
- **54 verified against the original** (PMC full text or PubMed abstract), with the same wording and meaning. Every BSR grade on the page matches the executive summary and the full guideline (1B, 1D, 1C, 1A, 2C as printed).
- **20 partly verified** (WebFetch only). All 20 are consistent with the evidence file and, where repeated, consistent across independent reads. They come from EULAR 2024 Parodis (body text and Table 1), EULAR 2023, WHO and CWA. None was human-viewed.
- **0 could not be accessed. 0 mismatches.**

Suspect items named in the brief:
- **EULAR 2024 (Parodis) SoR letters: partly verified, consistent everywhere.** Photoprotection "4 | C", physical exercise "1–4 | C", aerobic exercise "1–3 | B", psychosocial "1–2 | B" (LoE | SoR as printed).
  - Evidence: two independent WebFetch reads of the VoR PDF Table 1, made with differently worded prompts, agree with each other and with the evidence file.
  - Independent corroboration: the SRUK lay summary gives the same ranking with stars (photoprotection \*\*, physical exercise \*\*, aerobic \*\*\*, psychosocial \*\*\*).
  - Caveat inside the source itself: the Parodis abstract (PubMed) and the Table 1 footnote define "D comprising LoE 4 or inconsistent studies". Under that definition the LoE-4 photoprotection item would read D, yet C is printed. The page correctly uses the printed letter C. A one-minute human look at Table 1 of the PDF is still advisable before publication.
  - No "A" appears in the SoR column, although the abstract says "SoR ranged from A to D". The footnote shows this sentence describes the scale.
- **Blaess 2024: fully verified in PMC.** Statements 10 and 12 are 1b/A; statements 4, 5 and 9 are 5/D; statement 2 is 1b/A. The 150–300 min/week statement carries "Unless otherwise indicated … with inactive disease or mild disease activity". "Perceived exertion levels of 5 or 6 on a 0–10 scale" is also verified.
- **EULAR 2017 women's health: verified.** "(in the last 6–12 months or at conception)" and "RR 2.1" (Table 2), plus all body-text quotes. **The Table 1 grades of recommendation could not be confirmed**; see SL-6.1, SL-6.4 and SL-6.T.
- **ACR 2020 abstract (guiding principles): verified.**
- **Chasset 2015 (OR 0.53, 95% CI 0.29–0.98; "2-fold decrease") and Parisis 2019 (OR 0.53, 95% CI 0.305–0.927): verified** against PubMed abstracts. See SL-2.3 for a statistical-wording caveat.
- **WHO UVI 8+ advice: verified** in both the WHO 2002 guide and the WHO 2022 Q&A. **CWA names "8-10 過量級" and "11+ 危險級": verified.**

## 2. Findings table

| ID | Verdict | Problem | What I checked (source, location, verbatim text seen) | Suggested fix |
|---|---|---|---|---|
| SL-1.1 | OK | — (SoR C partly verified; see summary) | S04 Table 1 (WebFetch ×2): "In people with SLE, photoprotection should be advised for the prevention of flares (LoE: 4). \| 4 \| C \| 9.2 \| 1.0 \| 7–10". Body text: "Ultraviolet (UV) radiation is a well-acknowledged triggering factor of cutaneous and systemic lupus flares." SRUK lay summary: "Protecting yourself from sunlight can help prevent flares.\*\*" PubMed abstract: "Photoprotection and psychosocial interventions are important for SLE patients". | None. Optionally have a human confirm "C" on the PDF, because the paper's own footnote defines D as "LoE 4". |
| SL-1.2 | Minor | (1) "UVA 防護足夠" is vaguer than the source, which specifies high UVA protection ("UV-A logo or UV-A with 4-star or 5-star protection"). (2) The 1B grade covers "high SPF, broad-spectrum UV-A and UV-B sunscreen". The ≥30 threshold is the BAD definition, adopted because evidence was lacking, and is not graded. The label is acceptable but slightly overstates the evidence for the number. | S02 §E and S01 Rec 26: "…use high sun protection factor (SPF), broad-spectrum UV-A and UV-B sunscreen (1B) … (1D) (SoA 96.9%)." S01 rationale: "Due to the lack of high-quality evidence, we adopted the recommendation by the BAD (i.e. high SPF as defined by at least 30 and with a UV-A logo or UV-A with 4-star or 5-star protection)." | 「選擇高係數、廣效（同時防 UVA 和 UVB）的防曬乳：SPF 30 以上，UVA 防護等級也要高。」 Keep 強烈建議（1B） for the sunscreen recommendation. Optionally footnote that SPF 30 is the British Association of Dermatologists definition adopted by BSR. |
| SL-1.3 | OK | — | S01 Rec 26 rationale (PMC): "The sunscreen should be reapplied at least every two hours, regardless of its SPF []." Label 指引說明 is correct (rationale text, not graded). | None. |
| SL-1.4 | OK | — | S02 Rec 26: "…consider safe sun exposure strategies such as reduced sun exposure and the use of protective clothing (1D)". S01: "(e.g. physical barriers such as hats, sunglasses, long-sleeved shirts, trousers, leggings and dresses)". S04 (WebFetch): "…use physical barriers such as hats, sunglasses and long-sleeved shirts and pants…". | None. |
| SL-1.5 | OK | — | S04 body text (WebFetch): "Based on this evidence and expert opinion within the task force, people with SLE should avoid direct sun exposure, especially during days with high UV index, …". S03 (WebFetch): "…although patients with lupus should particularly avoid sun exposure due to the characteristic photosensitivity of the disease." | None. |
| SL-1.T | Minor | Safety caveat left out. The tip gives only the UVI ≥8 action. WHO advises protection from UVI 3, including "Seek shade during midday hours" at 3–7, and states that its scheme targets the general population. A photosensitive lupus patient could infer that midday outdoor time is fine below 8. Numbers, wording and CWA names are otherwise correct. | WHO 2002 guide (ICNIRP PDF, WebFetch): "EXTRA PROTECTION (UVI 8-11+): Avoid being outside during midday hours! Make sure you seek shade! Shirt, sunscreen and hat are a must!"; "PROTECTION REQUIRED (UVI 3-7): Seek shade during midday hours! Slip on a shirt, slop on sunscreen and slap on a hat!"; "Above the threshold value of 3, protection is necessary, and this message should be reinforced at UVI values of 8 and above." WHO Q&A (20 June 2022): same band wording. CWA: "8-10 過量級", "11+ 危險級", "紫外線指數分級係依據WHO相關規範". | 「出門前查中央氣象署紫外線指數：3 以上就要做好防曬（中午找陰涼處、穿長袖、擦防曬乳、戴帽子）；8 以上（過量級、危險級）時，中午時段盡量不要待在戶外。」 |
| SL-2.1 | OK | — | S02/S01 Rec 27: "In people with SLE, smoking habits should be assessed, and people guided to cessation strategies (1C, 98.2%)." S01: "…liaising with GPs and healthcare professionals in the community or signposting people to local stop-smoking support, if available…". | None. |
| SL-2.2 | OK | — | S03 (WebFetch): "The importance of smoking cessation should be emphasised, as smoking may also interfere with the efficacy of antimalarials and biologics (belimumab) among its other detrimental sequelae." Corroborated in S01 (PMC): "an SLR and meta-analysis of cohort studies showed that smoking may also reduce the efficacy of hydroxychloroquine and belimumab", and in the S18 abstract (OR 0.53, cutaneous lesions; HR 0.10, belimumab). "可能干擾" is appropriately hedged. | None. |
| SL-2.3 | Minor | Statistical overstatement carried over from the source's wording. The pooled estimate is an **odds ratio** (0.53; 95% CI 0.29–0.98, upper bound close to 1) from 10 observational studies. The authors' conclusion says "2-fold decrease in the proportion", but an OR of 0.53 does not mean the proportion improving is half. If 70% of non-smokers improve, the smoker figure is about 55%. Direction and population (CLE) are correct. | S19 abstract (PubMed 25648824): "The pooled odds ratio for the response to antimalarials in smoker patients with CLE (n = 797) was 0.53 (95% confidence interval 0.29-0.98) compared with nonsmokers (n = 601)." / "Smoking is associated with a 2-fold decrease in the proportion of patients with CLE achieving cutaneous improvement with antimalarials." S18 abstract: "(pooled OR 0.53; 95%CI: 0.305-0.927)". | 「研究發現，抽菸者的皮膚型狼瘡用抗瘧疾藥物治療時，皮膚改善的機會明顯比不抽菸者低。」 Keep 研究顯示. If a number is wanted: 「（改善的勝算約為不抽菸者的一半）」. |
| SL-3.1 | OK | — | S02/S01 Rec 28: "Physical activity should be encouraged as appropriate to disease status in adults (1B) and children (1C) with SLE. This will include tailored advice for some patients (SoA 97.0%)." | None. |
| SL-3.2 | OK | — | S09 Table 4 (PMC): statement 10 "A medical evaluation should be performed before starting exercise in SLE … (1b/A)", Mean (SD) 9.32 (2.15); statement 12 "Implementation of exercise should be gradual by adapting the frequency and intensity to the individual's capacities and comorbidities (1b/A)", 9.82 (0.50). "運動計畫" correctly limits this to structured exercise. | None. |
| SL-3.3 | OK | — | S09 Table 3, statement 9 (PMC): "Unless otherwise indicated, all persons with SLE with inactive disease or mild disease activity should gradually reach WHO recommendations and/or 150–300 min per week of moderate intensity associated with strengthening activities at least 2 days per week (5/D)." 9.68 (0.57). Population restriction and "unless otherwise indicated" are both kept. | None. |
| SL-3.4 | OK | — | S09 Table 2: statement 4 "In case of lupus flare, potential contraindication to physical activity and exercise should be reassessed (5/D)" 9.91 (0.43); statement 5 "During articular flares, we recommend avoiding involving the inflamed joints during physical activity and exercise (5/D)" 9.68 (0.89). The discussion adds: "people should strive to remain as active as possible". | Optional: add 「其他沒有發炎的部位，仍可盡量保持活動。」 |
| SL-3.5 | Minor | The label "建議強度 A" is printed for the whole of statement 2 (outdoor photoprotection plus "adequate clothing against cold … if Raynaud's phenomenon is present"). Gloves and avoiding cold surfaces come from discussion text ("the task force suggests"; "It is also advised"). EULAR 2024 grades cold avoidance in SLE as LoE 5 (expert opinion), SoR printed "C/D". The label therefore overstates the evidence for these specific measures. | S09 Table 2, statement 2 (PMC): "In case of outdoor activity, adapted measures such as photoprotection are necessary, and use of adequate clothing against cold is recommended if Raynaud's phenomenon is present (1b/A)" 9.95 (0.21). Discussion: "…the task force suggests protection against low temperatures by using gloves or heating devices. It is also advised to avoid direct contact with cold surfaces…". S04 (WebFetch): "In people with SLE (LoE: 5) and SSc (LoE: 4), avoidance of cold exposure should be considered…" row "4–5 \| C/D". | Text is fine. Change the label to 「國際共識 2024・建議強度 A（保暖衣物）；手套、避免碰觸冰冷表面為專家建議」, or simply 「國際共識 2024・專家共識」. |
| SL-3.T | OK | — | S09 discussion of statement 9 (WHO definition): "…or perceived exertion levels of 5 or 6 on a 0–10 scale." | None. |
| SL-4.1 | OK | — | S02/S01 Rec 34: "Health professionals should incorporate assessment of fatigue severity, impact and coping strategies alongside disease activity assessment during clinical consultations (1D, 95.4%)." S01: "Fatigue is prevalent in about two-thirds of people with SLE…". | None. |
| SL-4.2 | OK | — (SoR B partly verified) | S04 Table 1 (WebFetch ×2): "In people with SLE, aerobic exercise should be considered for increasing aerobic capacity (LoE: 1), and for reducing fatigue (LoE: 1–3) and depressive symptoms (LoE: 3). \| 1–3 \| B \| 9.2 \| 1.4 \| 4–10". The BSR paraphrase in PMC agrees. Lay summary \*\*\*. Examples from S01: "(e.g. walking, jogging, cycling and dancing)". "也可能有助" fits the conflicting certainty: Cochrane low, BSR low, He 2026 moderate. Note: BSR says trial participants "mostly had minimal disease activity". This is covered by SL-3.3 and SL-3.4. | None. |
| SL-4.3 | Minor | "有助改善" is firmer than the source. EULAR says "should be considered" (SoR B), and BSR found "low certainty evidence that psychological intervention may be effective". The listed interventions also map to different outcomes: group therapy showed HRQoL benefit only, and counselling showed anxiety benefit only. | S04 Table 1 (WebFetch ×2): "…psychosocial interventions should be considered for improving health-related quality of life (LoE: 1–2), anxiety (LoE: 1) and depressive symptoms (LoE: 1). \| 1–2 \| B". Body text (WebFetch): "…CBT, group therapy and psychoeducational programmes … improving HRQoL…"; "Counselling, CBT and supported psychotherapy improved anxiety…"; "CBT and psychoeducational self-management support ameliorated depressive symptoms…". S01 (PMC): "There was low certainty evidence that psychological intervention may be effective in improving HRQoL, anxiety and depression in SLE." | 「認知行為治療、團體治療、心理衛教或心理諮商等心理社會介入，可能有助改善生活品質、焦慮和憂鬱情緒。」 |
| SL-4.4 | Minor | The label shows only 1C, but the second clause (signposting or referral to mental-health services) is Rec 37, graded 1D. | S02: "Psychological support should be available to people with SLE, whenever possible as part of the multidisciplinary team (MDT) (1C, 96.7%)." / "All healthcare professionals … should know how to signpost towards and/or refer to mental health services … (1D, 97.8%)." | Label: 「BSR 2026・強烈建議（1C；轉介部分 1D）」. |
| SL-4.T | OK | — | S25 abstract (PubMed 39191627): "Support networks can help relieve a patient's isolation." | None. |
| SL-5.1 | OK | — | S02/S01 Rec 29: "A healthy, balanced diet, as recommended for people without SLE, should be recommended for people with SLE. More specific advice may be required for those with LN (1D, 96.8%)." | None. |
| SL-5.2 | OK | — | S01 Rec 29 rationale (PMC): "…at least 400 g of vegetables and fruit per day in adults and children above 10 years … mainly through legumes (e.g. lentils and beans) and wholegrain cereals; reducing total fats to <30% of total energy intake … reducing free sugars to <10% (ideally 5%) … limiting sodium intake to <2 g per day (equivalent to 5 g of salt)". Numbers and units are correct. "少油" is an acceptable lay simplification. | None. |
| SL-5.3 | Minor | The text follows EULAR's targeted approach ("assessment of the need … when indicated"), which is correctly quoted and labelled. It does not reflect that BSR 2026 **strongly recommends (1B)** that clinicians advise a daily vitamin D supplement all year for everyone with SLE, with testing where appropriate (1C). This is a real guideline difference with a UK/latitude context. It is not an error but needs an editorial decision. | S04 (WebFetch): "…assessment of the need for vitamin D supplements should be done when indicated." S02 Rec 30: "Clinicians should recommend that people with SLE take a daily vitamin D supplement throughout the year, particularly in autumn and winter (1B). Where deemed appropriate, vitamin D levels should be tested … (1C) (SoA 96.6%)." | Keep as is if the EULAR approach is preferred for Taiwan. Otherwise: 「是否需要補充維生素 D、要不要抽血檢查，請和醫師討論；英國 2026 指引建議狼瘡患者全年每天補充維生素 D。」 |
| SL-5.4 | OK | — | S02/S01 Rec 31: "…assessment and management of modifiable risk factors (e.g. hypertension, dyslipidaemia, diabetes, high BMI and smoking) should take place at baseline and at least annually … (1B, 96.6%)." S01: "two to three times more likely to develop cardiovascular diseases…". | None. Optional: 「評估並處理」. |
| SL-5.5 | OK | — | S02/S01 Rec 33: "Annual assessment and management of bone health should be performed including diet, exercise, lifestyle factors and medications … (2C, 97.6%)." S01: "…due to the disease process (i.e. chronic inflammation) and the side effects of therapies, particularly GC." | None. |
| SL-5.T | OK | — | S02 §B (Rec 12): "Urinalysis and blood pressure should be performed at every visit (2C, 97.2%)." §C (Rec 16): "Body weight should be checked at each visit… (2C, 97.0%)." | None. |
| SL-6.1 | Minor | Wording is verified. The quote is the abstract summary, echoed in "Scope and overarching principles" ("family planning should be discussed from the first physician–patient encounter"). It is not a graded Table 1 statement in any accessible text, so the GoR is unconfirmed and the label 「建議」 is a placeholder outside the mapping. | PMC5446003 abstract: "Family planning should be discussed as early as possible after diagnosis. Most women can have successful pregnancies and measures can be taken to reduce the risks of adverse maternal or fetal outcomes." Body: "Health professionals should support the patient and her family … by discussing individual pregnancy risks." PMC Table 1 has only item headings and LoA, with no statement text and no LoE/GoR. | Label: 「EULAR 2017・基本原則」 (or 「指引說明」). |
| SL-6.2 | OK | — | PMC5446003 Table 2: "SLE activity/flares\* (in the last 6–12 months or at conception)" → "Increased risk for (i) maternal disease activity (RR 2.1 for subsequent flare during pregnancy and puerperium);(ii) hypertensive complications (OR 1.8 for PE);(iii) fetal morbidity and mortality…". | Optional: add 「也會增加妊娠高血壓與胎兒方面的風險」. |
| SL-6.3 | OK | — | S08 abstract (PubMed 32090480): "…pre-pregnancy counseling to encourage conception during periods of disease quiescence and while receiving pregnancy-compatible medications…". Guiding principles → 基本原則 is correct. | None. |
| SL-6.4 | Minor | Content is verified (body text). The label 「建議」 implies a graded recommendation, but the EULAR 2017 Table 1 GoR could not be confirmed. Two WebFetch reads of the published PDF (iris.unibs.it) say the Table 1 contraception item is worded differently ("…counselled about the use of effective contraceptive measures … IUD can be offered … (1/A)"). This is unconfirmed because the evidence file records an earlier WebFetch fabrication of this table. | PMC5446003 "Contraceptive measures": "Women with SLE and/or APS should be counselled about contraception, especially for the prevention of unwanted pregnancies during high disease activity periods and intake of teratogenic drugs." S08 abstract: "use of safe and effective contraception to prevent unplanned pregnancy". | Label: 「EULAR 2017・指引說明」, unless a human confirms the Table 1 grade on the PDF; then use 「建議強度 X」. |
| SL-6.5 | OK | — | S02 §C / S01 Rec 21: "Anti-Ro/SSA and anti-La/SSB antibodies are associated with neonatal lupus (including congenital heart block) and should be re-assessed prior to pregnancy, and pre-pregnancy counselling provided (1A, 98.5%)." | None. |
| SL-6.T | Minor | Content is verified (body text). Two WebFetch reads of the published PDF report Table 1 item 3 as "…counselled about fertility issues, especially the adverse outcomes associated with increasing age and the use of alkylating agents (1/A)", with no tobacco or alcohol (unconfirmed). The tobacco/alcohol wording may therefore be narrative only, and the label 「建議」 is not supported. | PMC5446003 "Risk factors for reduced fertility": "Similar to the general population, women with SLE and/or APS should be counselled on fertility issues, especially on the negative impact of increasing age (general tendency to postpone childbearing) and certain lifestyle exposures (tobacco use, alcohol consumption)." | Label: 「EULAR 2017・指引說明」. |
| SL-M1 | OK | — | S04 Table 1 (WebFetch): OP C "Non-pharmacological management of SLE and SSc may be provided alone or as an adjunct to pharmaceutical treatment."; OP D "…should not substitute for pharmaceutical treatment when the latter is required." PubMed abstract: "It is not intended to preclude but rather complement pharmacotherapy." | None. |
| SL-M2 | OK | — | S09 (PMC): "It is imperative to communicate to healthcare professionals and caregivers including close entourage that engaging in physical activity is not contraindicated in SLE." S10 abstract: "…probably results in little to no difference in disease activity (moderate‐certainty evidence)…". S11 abstract: "…with no significant change in disease activity (g=0.18, 95% CI -0.16 to 0.51, p=0.30)." The flare caveat is kept. | Optional label: 「國際共識 2024・專家共識；系統性回顧・研究顯示」. |
| SL-M3 | OK | — | S01 Rec 26 rationale (PMC): "Detecting photosensitivity may be limited by a potential lag period of several weeks between sun exposure and skin lesions []." | None. |
| SL-M4 | OK | — | S01 Rec 29 rationale (PMC): "There was very low certainty that these dietary intervention programmes had a positive impact on measures of disease activity, fatigue or sleep in SLE." / "…there was low certainty that either of these supplements would improve disease activity…" / "For LN, in two RCTs [,], there was also low certainty and inconsistency in findings that fish oil supplementation would improve renal parameters…". | None. |
| SL-S1 | Minor | (1) Rec 100 (1C) is a **service standard** (the hospital should give timely advice "ideally within 1–2 working days"). It is not a patient-behaviour recommendation, so attaching "強烈建議（1C）" to a patient instruction is a stretch. (2) Safety gap: nothing on the page says what to do when symptoms are severe or rapidly worsening. A 1–2 working-day advice line is not for emergencies. | S01 Rec 100 (PMC): "People with SLE with disease flares or possible drug-related side effects should be able to receive timely advice (ideally within 1–2 working days) of contacting their hospital service (1C) [98.4% (86–100)]." S02: same, "(1C, 98.4%)". | Keep the text. Label: 「BSR 2026・指引說明（醫療服務標準，1C）」. Add an EDITORIAL line: 「如果症狀很嚴重或突然惡化，請不要等回診，立即就醫或掛急診。」 |
| SL-S2 | OK | — | S01 Rec 34 rationale (PMC): "The 2023 EULAR recommendations for management of fatigue in people with RMDs recommended that the presence or worsening of fatigue should trigger evaluation of inflammatory disease activity status…". BSR notes this was based mostly on RA/SpA evidence. Label 指引說明 is correct. | None. |
| SL-S3 | OK | — | S02 §I / S01 Rec 56: "Scarring and/or refractory cutaneous involvement in SLE should be managed in a timely manner in conjunction with dermatologists (1D, 98.3%)." | None. |

Cosmetic (outside the rows): the page heading reads 「紅斑性狼瘡（sle）」; consider 「（SLE）」.

## 3. Quote verification log

Status: **Verified** = located in the original (PMC full text or PubMed abstract) with the same wording and meaning. **Partly verified** = read only through WebFetch (summarising model), consistent with the evidence file and, where stated, across independent reads.

| S-ID / C-ID | Quote (first words) | Status | Where verified |
|---|---|---|---|
| S04 / C21 | "In people with SLE, photoprotection should be advised…" (LoE 4; SoR C) | Partly verified | VoR PDF Table 1, WebFetch ×2 (row "4 \| C \| 9.2 \| 1.0 \| 7–10"); SRUK lay summary \*\*; PubMed abstract (content) |
| S04 / C20 | "Ultraviolet (UV) radiation is a well-acknowledged triggering factor…" | Partly verified | VoR PDF body text, WebFetch; similar wording in S09 (PMC) |
| S02 / C25 | "People with SLE should be advised at diagnosis…" (1B; 1D; 96.9%) | Verified | PMC13290299 §E; PMC13290301 Rec 26 "[96.9% (84–100)]" |
| S01 / C28 | "Due to the lack of high-quality evidence, we adopted…" | Verified | PMC13290301, Rec 26 rationale |
| S01 / C29 | "The sunscreen should be reapplied at least every two hours…" | Verified | PMC13290301, Rec 26 rationale |
| S02 / C26 | "…consider safe sun exposure strategies… (1D)" | Verified | PMC13290299 §E |
| S01 / C27 | "…(e.g. physical barriers such as hats, sunglasses…" | Verified | PMC13290301, Rec 26 rationale |
| S04 / C22 | "…use physical barriers such as hats, sunglasses and long-sleeved shirts and pants…" | Partly verified | VoR PDF body text, WebFetch |
| S04 / C22 | "…people with SLE should avoid direct sun exposure, especially during days with high UV index…" | Partly verified | VoR PDF body text, WebFetch |
| S03 / C24 | "…although patients with lupus should particularly avoid sun exposure…" | Partly verified | ard.bmj.com/content/83/1/15, WebFetch |
| common:S11 / C83 | "EXTRA PROTECTION" (UVI 8+) "Avoid being outside during midday hours"… | Partly verified | ICNIRP-hosted WHO 2002 PDF, WebFetch (printed "UVI 8-11+", with exclamation marks) |
| common:S12 / C83 | [8 and above] "Avoid being outside during midday hours!…" | Partly verified | who.int Q&A (20 June 2022), WebFetch |
| common:S13 / C90 | "8-10 過量級" "11+ 危險級" "紫外線指數分級係依據WHO相關規範" | Partly verified | cwa.gov.tw OBS_UVI, WebFetch |
| S02 / C53 | "In people with SLE, smoking habits should be assessed…" (1C, 98.2%) | Verified | PMC13290299 §E; PMC13290301 Rec 27 |
| S01 / C53 | "The latter could be done by liaising with GPs…" | Verified | PMC13290301, Rec 27 rationale |
| S04 / C51 | "In people with SLE (LoE: 3) and SSc (LoE: 4), smoking habits…" (SoR B/C) | Partly verified | VoR PDF Table 1, WebFetch ×2 (row "3–4 \| B/C") |
| S04 / C52 | "…it was consensual among the task force members…" | Partly verified | VoR PDF body text, WebFetch |
| S03 / C50 | "The importance of smoking cessation should be emphasised…" | Partly verified | ard.bmj.com, WebFetch; content corroborated by S01 (PMC) and S18 (PubMed) |
| S18 / C54 | "Tobacco smoking significantly reduced the therapeutic effectiveness…" (OR 0.53; 0.305–0.927) | Verified | PubMed abstract 31520802 |
| S19 / C55 | "Smoking is associated with a 2-fold decrease…" | Verified | PubMed abstract 25648824 |
| S19 / C55 | "The pooled odds ratio… was 0.53 (95% confidence interval 0.29-0.98)…" | Verified | PubMed abstract 25648824 |
| S02 / C72 | "Physical activity should be encouraged as appropriate to disease status…" (1B/1C; 97.0%) | Verified | PMC13290299 §E; PMC13290301 Rec 28 |
| S04 / C70 | "Physical exercise should be considered for people with SLE (LoE: 1–3)…" (SoR C) | Partly verified | VoR PDF Table 1, WebFetch ×2 (row "1–4 \| C \| 9.6 \| 0.7"); lay summary \*\* |
| S09 / C78 | "A medical evaluation should be performed before starting exercise…" (1b/A; 9.32 (2.15)) | Verified | PMC11002419 Table 4, statement 10 |
| S09 / C79 | "Implementation of exercise should be gradual…" (1b/A; 9.82 (0.50)) | Verified | PMC11002419 Table 4, statement 12 |
| S09 / C74 | "Unless otherwise indicated, all persons with SLE with inactive disease or mild disease activity…" (5/D; 9.68 (0.57)) | Verified | PMC11002419 Table 3, statement 9 |
| S09 / C83 | "In case of lupus flare, potential contraindication…" (5/D; 9.91 (0.43)) | Verified | PMC11002419 Table 2, statement 4 |
| S09 / C83 | "During articular flares, we recommend avoiding involving the inflamed joints…" (5/D; 9.68 (0.89)) | Verified | PMC11002419 Table 2, statement 5 |
| S09 / C35 | "In case of outdoor activity, adapted measures such as photoprotection…" (1b/A; 9.95 (0.21)) | Verified | PMC11002419 Table 2, statement 2 |
| S09 / C61 | "Additionally, for persons living with SLE with Raynaud's phenomenon…" | Verified | PMC11002419, discussion of statement 2 |
| S04 / C60 | "In people with SLE (LoE: 5) and SSc (LoE: 4), avoidance of cold exposure…" (SoR C/D) | Partly verified | VoR PDF Table 1, WebFetch ×2 (row "4–5 \| C/D") |
| S09 / C76 | "…perceived exertion levels of 5 or 6 on a 0–10 scale." | Verified | PMC11002419, discussion of statement 9 |
| S02 / C95 | "Health professionals should incorporate assessment of fatigue…" (1D, 95.4%) | Verified | PMC13290299 §E; PMC13290301 Rec 34 |
| S01 / C96 | "Fatigue is prevalent in about two-thirds…" | Verified | PMC13290301 |
| S04 / C71 | "In people with SLE, aerobic exercise should be considered…" (SoR B) | Partly verified | VoR PDF Table 1, WebFetch ×2 (row "1–3 \| B \| 9.2 \| 1.4 \| 4–10"); lay summary \*\*\*; BSR paraphrase (PMC) |
| S01 / C100 | "…our SLR showed low certainty evidence that exercise…" | Verified | PMC13290301 |
| S01 / C73 | "…(i) aerobic which refers to the type of repetitive…" | Verified | PMC13290301, Rec 28 rationale |
| S04 / C105 | "In people with SLE, psychosocial interventions should be considered…" (SoR B) | Partly verified | VoR PDF Table 1, WebFetch ×2 (row "1–2 \| B \| 9.2 \| 1.2 \| 6–10"); lay summary \*\*\*; BSR paraphrase (PMC) |
| S04 / C106 | "...psychological interventions in the form of cognitive behavioural therapy…" | Partly verified | VoR PDF body text, WebFetch; S01 (PMC) names the same three formats |
| S02 / C107 | "Psychological support should be available…" (1C, 96.7%) | Verified | PMC13290299 §E; PMC13290301 Rec 35 |
| S02 / C109 | "All healthcare professionals assessing people with SLE should know how to signpost…" (1D, 97.8%) | Verified | PMC13290299 §E; PMC13290301 Rec 37 |
| S25 / C14 | "Support networks can help relieve a patient's isolation." | Verified | PubMed abstract 39191627 |
| S02 / C114 | "A healthy, balanced diet, as recommended for people without SLE…" (1D, 96.8%) | Verified | PMC13290299 §E; PMC13290301 Rec 29 |
| S03 / C01 | "Non-pharmacological interventions, including sun protection…" | Partly verified | ard.bmj.com Table 1 OP C, WebFetch |
| S01 / C115 | "…the consensus from the BSR GWG is to recommend a healthy balanced diet as defined by WHO…" | Verified | PMC13290301, Rec 29 rationale |
| S04 / C22 | "…assessment of the need for vitamin D supplements should be done when indicated." | Partly verified | VoR PDF body text, WebFetch |
| S02 / C120 | "Clinicians should recommend that people with SLE take a daily vitamin D supplement…" (1B; 1C) | Verified | PMC13290299 §E; PMC13290301 Rec 30 |
| S02 / C110 | "People with SLE are at increased risk of cardiovascular comorbidities…" (1B, 96.6%) | Verified | PMC13290299 §E; PMC13290301 Rec 31 |
| S01 / C111 | "People with SLE are two to three times more likely…" | Verified | PMC13290301 |
| S02 / C123 | "Annual assessment and management of bone health…" (2C, 97.6%) | Verified | PMC13290299 §E; PMC13290301 Rec 33 |
| S01 / C124 | "People with SLE are at risk of osteoporosis…" | Verified | PMC13290301 |
| S02 / C113 | "Urinalysis and blood pressure should be performed at every visit (2C, 97.2%)." | Verified | PMC13290299 §B; PMC13290301 Rec 12 |
| S02 / C113 | "Body weight should be checked at each visit…(2C, 97.0%)." | Verified | PMC13290299 §C; PMC13290301 Rec 16 |
| S06 / C140 | "Family planning should be discussed as early as possible after diagnosis…" | Verified | PMC5446003 abstract (Results) and PubMed abstract |
| S06 / C141 | "Health professionals should support the patient and her family…" | Verified | PMC5446003, "Scope and overarching principles" |
| S06 / C143 | "SLE activity/flares… (in the last 6–12 months or at conception)" | Verified | PMC5446003 Table 2 |
| S06 / C143 | "Increased risk for (i) maternal disease activity (RR 2.1…)" | Verified | PMC5446003 Table 2 |
| S08 / C144 | "…pre-pregnancy counseling to encourage conception during periods of disease quiescence…" | Verified | PubMed abstract 32090480 |
| S06 / C145 | "Women with SLE and/or APS should be counselled about contraception…" | Verified (body text). Table 1 GoR not confirmed | PMC5446003, "Contraceptive measures" |
| S08 / C144 | "…use of safe and effective contraception to prevent unplanned pregnancy…" | Verified | PubMed abstract 32090480 |
| S02 / C150 | "Anti-Ro/SSA and anti-La/SSB antibodies are associated with neonatal lupus…" (1A, 98.5%) | Verified | PMC13290299 §C; PMC13290301 Rec 21 |
| S06 / C146 | "Similar to the general population, women with SLE and/or APS should be counselled on fertility issues…" | Verified (body text). Table 1 GoR not confirmed | PMC5446003, "Risk factors for reduced fertility" |
| S04 / C04 | OP D "…should not substitute for pharmaceutical treatment when the latter is required." | Partly verified | VoR PDF Table 1, WebFetch; PubMed abstract (content) |
| S04 / C04 | OP C "…may be provided alone or as an adjunct to pharmaceutical treatment." | Partly verified | VoR PDF Table 1, WebFetch |
| S09 / M09 | "It is imperative to communicate to healthcare professionals…" | Verified | PMC11002419, discussion of OP C |
| S10 / C84 | "Compared with education or relaxation therapy, exercise…" | Verified | PubMed abstract 37073886 |
| S11 / C85 | "…with no significant change in disease activity (g=0.18…)" | Verified | PubMed abstract 42373138 |
| S01 / C32 | "Detecting photosensitivity may be limited by a potential lag period…" | Verified | PMC13290301, Rec 26 rationale |
| S01 / M06 | "There was very low certainty that these dietary intervention programmes…" | Verified | PMC13290301, Rec 29 rationale (adjacent comparator words are glued in PMC; not part of the quote) |
| S01 / M05 | "…there was low certainty that either of these supplements would improve disease activity…" | Verified | PMC13290301, Rec 29 rationale |
| S01 / M05 | "For LN, in two RCTs [,], there was also low certainty…fish oil…" | Verified | PMC13290301, Rec 29 rationale |
| S01 / C160 | "People with SLE with disease flares or possible drug-related side effects…" (1C) [98.4% (86–100)] | Verified | PMC13290301 Rec 100; PMC13290299 §M |
| S01 / C97 | "The 2023 EULAR recommendations for management of fatigue… presence or worsening of fatigue…" | Verified (as reported by BSR; the EULAR fatigue paper itself was not checked) | PMC13290301, Rec 34 rationale |
| S02 / C161 | "Scarring and/or refractory cutaneous involvement…" (1D, 98.3%) | Verified | PMC13290299 §I; PMC13290301 Rec 56 |

Strength items that could not be confirmed:
- **EULAR 2017 Table 1 grades of recommendation.** The PMC text has item headings and LoA only. Its footnote says "the LoE (range 1–3) and the GoR (range A–D) is given in parentheses". The Europe PMC XML was refused with HTTP 429 (not retried). Two WebFetch reads of the published PDF on iris.unibs.it agreed with each other. They give Table 1 wording that differs from the body-text quotes used on the page:
  - item 1: "In women with SLE, major risk factors … active/flaring SLE (1/A) …";
  - item 2: "Women with SLE should be counselled about the use of effective contraceptive measures … IUD can be offered … (1/A)";
  - item 3: "…increasing age and the use of alkylating agents (1/A)".

  The evidence file records an earlier fabricated WebFetch output for this same table, so these grades are **not confirmed**. A human should check the PDF if a 「建議強度」 label is wanted.

Note for editors: common.md records LoA 9.6 (photoprotection) and 9.7 (smoking) from a single HTML read. My Table 1 reads give 9.2 (1.0) and 9.4 (1.1), matching sle.md. LoA is not shown on the page, so nothing needs to change.

## 4. Citation check results

| S-ID | Check (PubMed metadata unless stated) | Result |
|---|---|---|
| S01 | PMID 42336388; DOI 10.1093/rheumatology/keag223; Rheumatology (Oxford) 2026;65(6); epub 3 Jun 2026; authors Md Yusof MY, Smith EMD, Lythgoe H… | Correct. PubMed gives no page or article number. |
| S02 | PMID 42336387; DOI 10.1093/rheumatology/keag224; Rheumatology (Oxford) 2026;65(6) | Correct |
| S03 | PMID 37827694; DOI 10.1136/ard-2023-224762; Ann Rheum Dis 2024;83(1):15–29; Fanouriakis A, Kostopoulou M, Andersen J… | Correct |
| S04 | PMID 37433575; DOI 10.1136/ard-2023-224416; Ann Rheum Dis 2024;83(6):720–729; Parodis I, Girard-Guyonvarc'h C, Arnaud L… | Correct. It was first published online in 2023; BSR and Blaess call it the "2023 EULAR recommendations". "EULAR 2024" (print year) is acceptable. |
| S06 | PMID 27457513; DOI 10.1136/annrheumdis-2016-209770; Ann Rheum Dis 2017;76(3):476–485 (epub 25 Jul 2016); Andreoli L, Bertsias GK, Agmon-Levin N… | Correct |
| S08 | PMID 32090480; DOI 10.1002/art.41191; Arthritis Rheumatol 2020;72(4):529–556; Sammaritano LR, Bermas BL, Chakravarty EE… | Correct |
| S09 | PMID 38580348; DOI 10.1136/rmdopen-2024-004171; RMD Open 2024;10(2):e004171; Blaess J, Geneton S, Goepfert T… | Correct. The title is abbreviated: the full title reads "…Systemic Lupus Erythematosus (SLE)…". |
| S10 | PMID 37073886; DOI 10.1002/14651858.CD014816.pub2; Cochrane Database Syst Rev 2023;4(4):CD014816; Frade S, O'Neill S, Greene D… | Correct |
| S11 | PMID 42373138; DOI 10.1136/lupus-2026-002027; Lupus Sci Med 2026;13(1); He Z, Jia S, Chen M… | Correct but incomplete: **add article number e002027** (pii 13/1/e002027). |
| S18 | PMID 31520802; DOI 10.1016/j.autrev.2019.102393; Autoimmun Rev 2019;18(11):102393; Parisis D, Bernier C, Chasset F, Arnaud L | Correct |
| S19 | PMID 25648824; DOI 10.1016/j.jaad.2014.12.025; J Am Acad Dermatol 2015;72(4):634–9; Chasset F, Francès C, Barete S, Amoura Z, Arnaud L | Correct |
| S25 | PMID 39191627; DOI 10.1016/j.revmed.2024.07.006; Rev Med Interne 2024;45(9):559–599; Amoura Z, Bader-Meunier B, Antignac M… | Correct |
| common:S11 | WHO/WMO/UNEP/ICNIRP, Global Solar UV Index: A Practical Guide, Geneva: WHO 2002, ISBN 92-4-159007-6 (ICNIRP publication page) | Correct. The PDF is at icnirp.org/cms/upload/publications/ICNIRPWHOSolarUVI.pdf. |
| common:S12 | WHO, "Radiation: The ultraviolet (UV) index", Q&A page dated 20 June 2022 | Correct |
| common:S13 | 交通部中央氣象署 紫外線觀測 page, https://www.cwa.gov.tw/V8/C/W/OBS_UVI.html | Correct; the page loads and the category names match |
