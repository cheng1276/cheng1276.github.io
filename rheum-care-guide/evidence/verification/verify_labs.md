# Independent fact-check: 健檢報告異常 (labs) — 33 statements

Checked: /home/claude/newpages/review/review_labs.md (generated from /home/claude/newpages/content/labs.json), against the original publications. The evidence files (/home/claude/newpages/research/labs.md, .../evidence/research/common.md) were used only as leads. common.md is not cited by this page.
Date: 2026-10-10. Tools: PubMed metadata and PMC full text (machine-searchable), WebFetch (summarising tool; verbatim short segments requested), WebSearch. The shell could not reach any publisher or repository (proxy 403), so no PDF could be downloaded.

## 1. Summary counts

| Verdict | Count | Rows |
|---|---|---|
| Critical | 0 | — |
| Major | 0 | — |
| Minor | 10 | LB-1.1, LB-1.2, LB-1.3, LB-2.2, LB-3.T, LB-5.3, LB-6.2, LB-M1, LB-M3, LB-S2 |
| OK | 23 | all other rows (incl. EDITORIAL LB-6.T) |

**Quotes:** 44 unique evidence cells, 43 with a source quote plus 1 EDITORIAL. All 43 were checked against the originals: **43 verified, 0 mismatches, 0 could not access.**
- 31 against PMC full text or the PubMed abstract (exact text).
- 12 against the original pages through WebFetch (S8 ×2, S10, S23 ×2, S28, S29 ×2, S33, S34 ×2, S40). Each of my WebFetch reads matched the evidence agent's earlier reads word for word. Key numbers and directions were also confirmed a second way where possible (see the log).

**Points the brief asked me to check specifically:**
- **ACR 2020 on asymptomatic hyperuricaemia: confirmed as "conditionally recommended against".**
  - S33, Deep Blue PDF: "Initiating ULT is conditionally recommended against in patients with asymptomatic hyperuricemia."
  - S33 Table 1: "we conditionally recommend against initiating any pharmacologic ULT (allopurinol, febuxostat, probenecid)" … certainty "High†".
  - The PMC text of S32 does read "conditionally recommendedin patients with asymptomatic hyperuricemia", so the word is dropped there. Its rationale sentence ("the benefits of ULT would not outweigh potential treatment costs or risks …") is consistent with "against".
  - Independent confirmation from S40 ("ACR 2020 does not recommend administration of ULAs to patients with asymptomatic hyperuricemia") and MDedge ("conditionally recommends against initiating any pharmacologic urate-lowering therapy").
- **The common-ground wording on drug treatment (LB-6.1, LB-M4) is fair to all guidelines cited.**
  - ACR: conditional against.
  - China 2024: "should initiate ULT" at SU ≥9 mg/dL or with comorbidities.
  - Japan (secondary source): "Considering the use of ULA at SUA ≥9 mg/dL".
  - All three agree that not everyone needs drugs; they differ on who does.
- **Numbers:** the ANA titre rates, RF / anti-CCP sensitivity and specificity, "about 20% within 5 years above 9 mg/dL", "at least one swollen joint" and "within 6 weeks" were all verified in the originals. Population caveats are listed in the findings below.
- **EDITORIAL phrase** (LB-6.T and the end of LB-M4): neutral and harmless.

## 2. Findings table

| ID | Verdict | Problem | What I checked (source, location, verbatim text seen) | Suggested fix |
|---|---|---|---|---|
| LB-1.1 | Minor | The numbers match the source. However, they are a single secondary figure from a Choosing Wisely text (CRA 2015). CRA cites Kavanaugh 2000 for them, and they apply to the HEp-2 method ("With the HEp-2 substrate" was dropped) in unspecified "normal people". Another High source gives a higher upper bound at 1:40, so a flat 「約2成」 may understate. This matters more for Asian readers: a Japanese health-check study found 26.0% at 1:40 and 9.5% at 1:160 (Low). | S8, jrheum.org, WebFetch ×2: "With the HEp-2 substrate, about 20% of normal people have an ANA titer of 1:40 or higher," / "while 5% of normal people have an ANA titer of 1:160 or higher" (reference 10 = Kavanaugh A et al. 2000, Arch Pathol Lab Med). S5, PMC Discussion: "Indeed, up to 35% of healthy controls may be positive if a screening dilution of 1/40 is used." | 「健康的人也可能驗出抗核抗體（ANA）陽性：在1:40約2到3成，在1:160約5%（各研究數字不同）。」 Cite CRA 2015 and ICAP 2019. Alternatively, keep the text and add 「（數字因研究而不同）」. |
| LB-1.2 | Minor | The first clause is verified. The second clause leaves out the condition ICAP puts in the same table cell: the "healthy" association of this pattern holds only if the antibody is confirmed as anti-DFS70 with no other common ENA. ICAP also says the pattern may come from other antibodies. Because the pattern is not named, a reader with a high titre or a "speckled" report may wrongly reassure themselves. (The Hung 2026 meta-analysis in the evidence file also weakens this association.) | S5, PMC Introduction: "Indeed, higher antibody levels are better associated with SARD and have an increased likelihood to identify the autoantigen in follow-up testing." Table 1 (AC-2): "Commonly found as high titer HEp-2 IIFA-positive in apparently healthy individuals or in patients who do not have a systemic autoimmune rheumatic disease (SARD)", immediately followed by "The negative association with SARD is only valid if the autoreactivity is confirmed as being directed to DFS70 … and if no other common ENA is recognized" and "the AC-2 pattern may be caused by autoantibodies to other antigens than DFS70". Discussion: "this association only holds if the specificity is confirmed as monospecific for DFS70." S4 abstract: specificity 66.9% → 96.6% from 1:40 to 1:320 (verified). | 「抗核抗體數值越高（如1:160高於1:40），和自體免疫風濕病關聯越強；不過有一種型態即使數值高，也常見於看似健康的人，報告的意義要由醫師判斷。」 Or delete the second clause. |
| LB-1.3 | Minor | This is a faithful paraphrase of the ICAP sentence. Its implied converse, however, is that a centromere pattern on a report points clearly to one disease, and the disease is not named. That can alarm a health-check reader. ICAP itself recommends confirmation for the centromere pattern too, "especially in case of low titers", and lists more than one association. | S5, PMC Discussion: "Altogether, it is evident that, with the exception of the centromere pattern (AC-3), all patterns are to be confirmed by antigen-specific immunoassay for a solid association with the respective autoimmune diseases." Table 1 (AC-3): "especially in case of low titers, confirmation by an antigen-specific immunoassay is recommended to support the association with limited cutaneous SSc"; "The AC-3 pattern is also apparent in a subset of patients with PBC". | 「單看報告上的抗核抗體型態，通常不能確定和哪一種疾病有關，要由醫師配合症狀判斷。」 |
| LB-1.4 | OK | — | S6, PubMed abstract: "These alternative platforms differ in their antigen profiles, sensitivity and specificity, raising uncertainties regarding standardisation and interpretation of incongruent results." S5, PMC: "each laboratory verifies that the screening dilution is defined by a cut-off set at the 95th percentile." | — |
| LB-1.T | OK | — | S5, PMC Discussion: "…the number of clinically unexpected positive results, that is, positive test results with no clinical evidence of an associated autoimmune disease, is ever increasing and may even equal the likelihood of a clinically true-positive result." | — |
| LB-2.1 | OK | — | S3, PMC abstract: "include positive ANA at least once as obligatory entry criterion". Phase 2a: "They endorsed “positive ANA (≥1:80 by HEp-2 immunofluorescence)” as an entry criterion." S4 abstract (C13) verified. | — |
| LB-2.2 | Minor | 「累積10分以上」 is correct. However, the criteria also require at least one clinical criterion. 「其他臨床表現或免疫檢驗結果」 joined by 「或」 lets a reader whose only abnormal findings are blood tests think those tests alone can reach classification, which points in the alarming direction for this page's readers. The rule appears in the criteria figure. That figure is an image and is not in the PMC or ARD text, so I confirmed the rule through two secondary sources. | S3, PMC abstract: "…weighted from 2 to 10. Patients accumulating ≥10 points are classified." The Rheumatologist (ACR magazine), WebFetch: "SLE classification requires at least one clinical criterion and 10 or more points;". ebm.one criteria summary, WebFetch: "Classification as SLE requires ≥10 points and ≥1 clinical criterion present." ARD 78(9):1151: Figure 2 not readable (image). | 「通過入門條件後，還要有其他臨床表現或免疫檢驗結果累積10分以上，而且至少要有1項臨床表現，才歸類為紅斑性狼瘡。」 Confirm against the Aringer 2019 criteria figure and add it to the evidence file. |
| LB-2.3 | OK | The label 基本原則 is correct. | S3, PMC Discussion: "The concept that all criteria are only to be counted if SLE is thought to be the most likely cause of the manifestation (i.e. no other more likely cause exists) is central to these new EULAR/ACR criteria, and is explicitly stated as an overarching principle." | — |
| LB-2.4 | OK | — | S3, PMC Discussion: "However, it is important to stress that classification criteria are not designed for diagnosis or treatment decisions ()." … "Diagnosis of SLE remains the purview of an appropriately trained physician evaluating an individual patient ()." | — |
| LB-2.T | OK | — | S3, PMC Methods: "Such an approach was thought to reflect underlying SLE pathogenesis, and take into account ANA test characteristics of high sensitivity and limited specificity." Discussion: "In the phase 1 early SLE cohort, 99.5% of the 389 SLE patients were ANA positive ()." | — |
| LB-3.1 | OK | S10's population is children and S31's is hepatitis C patients. Both are used only as supporting citations, which is acceptable. | S24 abstract: IgM RF specificity "85% (CI, 82% to 88%)". S10 First Release PDF, WebFetch: "RF may also be elevated in healthy individuals, as well as in scenarios such as infection and malignancy." S31 abstract: RF "20.8%". | — |
| LB-3.2 | OK | Specificity comes from the control groups of diagnostic studies, not the general population (as the reviewer notes say). The direction is correct. | S24 abstract: anti-CCP specificity "95% (CI, 94% to 97%)" vs IgM RF "85%"; "Anti-CCP antibodies are more specific than RF for diagnosing rheumatoid arthritis". S25 abstract: "Anti-CCP2 had greater specificity than rheumatoid factor (96% vs. 86%), with similar sensitivity." | — |
| LB-3.3 | OK | "At least one swollen joint" is confirmed in two places. | S23, PubMed abstract: "confirmed presence of synovitis in at least one joint, absence of an alternative diagnosis better explaining the synovitis". ard.bmj.com, WebFetch: "first, there must be evidence of currently active clinical synovitis (ie, swelling) in at least one joint" / "as determined by an expert assessor (table 3)" / "Second, the criteria may be applied only to those patients in whom the observed synovitis is not better explained" / "by another diagnosis (table 3)". | — |
| LB-3.4 | OK | 「3成以上」 is 1 minus sensitivity: anti-CCP 33%, RF 31% (CI 27–35%), anti-CCP2 in early RA 43%. | S24 abstract (sensitivity 67% and 69%). S25 abstract (57% in early RA). NICE 1.1.1, WebFetch: "Refer urgently (even with a normal acute-phase response, negative anti-cyclic citrullinated peptide [CCP]" / "antibodies or rheumatoid factor) if any of the following apply:". | — |
| LB-3.T | Minor | Slightly narrower and more absolute than the source. The source also says these patients "may therefore benefit from DMARD intervention" and that the criteria "will likely also be used as a diagnostic aid". Diagnosis stays with the physician. | S23, ard.bmj.com Discussion, WebFetch ×2: "The working group has deliberately labelled these criteria as ‘classification criteria’" / "as opposed to ‘diagnostic criteria’." / "…who may be enrolled into clinical trials and other studies through the use of uniform criteria." / "These individuals are also the ones who may therefore benefit from DMARD intervention." / "The criteria do not remove the onus on individual physicians…" / "Nonetheless, it is recognised that the new criteria will likely also be used as a diagnostic aid". | 「類風濕性關節炎的分類標準主要是為研究而訂，不是診斷標準；是否罹病仍由醫師判斷。」 |
| LB-4.1 | OK | Labelling this ungraded "Do not" item 不建議 is reasonable. | S8, jrheum.org, WebFetch: "Do not order antinuclear antibodies (ANA) as a screening test in patients without specific signs or symptoms" / "of systemic lupus erythematosus (SLE) or another connective tissue disease (CTD)". | — |
| LB-4.2 | OK | The logic is correct: ANA positive but no clinical suspicion means no sub-serologies. 1C means a strong recommendation with low-quality evidence under the paper's modified GRADE, so 強烈不建議（1C） is right. The text saying 「不建議」 under that label is acceptable. | S7, PMC: "1. Do not test antinuclear antibody (ANA) subserologies without a positive ANA and clinical suspicion of immune-mediated disease" … "Grade 1C." … "classifies recommendations as strong (grade 1) or weak (grade 2)" … "low (grade C)". | — |
| LB-4.3 | OK | — | S7, PMC: "tests should not be performed if results will not change management or if the pretest probability of disease is low enough to raise the likelihood of a false-positive test higher than the likelihood of a true-positive result." | — |
| LB-4.4 | OK | — | S7, PMC: "newer testing may complicate patient care if it results in undirected or very broad testing that increases false-positive results, leading to unnecessary followup tests and patient concern." | — |
| LB-5.1 | OK | — | S32, PMC Methods (machine-checked): "…which is defined as an SU concentration of ≥6.8 mg/dl with no prior gout flares or subcutaneous tophi." | — |
| LB-5.2 | OK | The label 指引說明 is conservative; the grade of Recommendation 4 is not visible in the accessible text. | S34, ard.bmj.com, WebFetch: "The diagnosis of gout should not be made on the presence of hyperuric a emia alone."; "Therefore, hyperuricaemia alone should be considered solely as a strong risk factor for incident gout" / "and not as a surrogate marker for its diagnosis." PubMed abstract: "There was consensus that a diagnosis of gout should not be based on the presence of hyperuricaemia alone." S36, PMC abstract (C54) verified. | — |
| LB-5.3 | Minor | The figures are verified. The 5-year figure matches Campion 1987: 2,046 initially healthy **US men**, SU ≥9 mg/dl, "22 percent after five years". The 15-year figure matches Dalbeth 2018: US cohorts, 49% (95% CI 31–67) at ≥10 mg/dL. The page applies these old, non-Taiwanese data (men only for the 5-year figure) to everyone without saying so. The guidelines do the same. | S32, PMC (machine-checked): "…among patients with asymptomatic hyperuricemia with SU concentrations of >9 mg/dl, only 20% went on to develop gout within 5 years ()." S34, WebFetch ×2: "For instance, only 22% of asymptomatic patients with SUA levels above 9 mg/dL developed incident gout over a 5-year period."; "For instance, a recent study found that only half of patients with SUA levels above 10 mg/dL" / "will develop gout over 15 years." PubMed abstracts: PMID 3826098 (Campion) and PMID 29463518 (Dalbeth). | Optional: 「國外研究顯示，尿酸超過9 mg/dL的人，5年內約2成發生痛風；超過10 mg/dL的人，15年內約一半。」 |
| LB-5.T | OK | The wording 「為界」 avoids the text (≥6.8) vs Table 1 (>6.8) discrepancy. | S32 text ≥6.8. S33 Table 1, WebFetch: "SU >6.8 mg/dl". S37, PMC: "it was considered beyond the scope of this nomenclature project to include a specific threshold of blood urate concentration in its definition"; "‘an elevated blood urate concentration over the saturation threshold’". S42, PMC: "420 μmol/L (7 mg/dL)". | — |
| LB-6.1 | OK | The direction is confirmed and the wording is fair to all three cited positions. | S33, Deep Blue PDF, WebFetch: "Initiating ULT is conditionally recommended against in patients with asymptomatic hyperuricemia."; Table 1 "we conditionally recommend against initiating any pharmacologic ULT" … "High†". S32, PMC: "conditionally recommendedin" (dropped word). S40, J-STAGE: "ACR 2020 does not recommend administration of ULAs to patients with asymptomatic hyperuricemia". MDedge: "conditionally recommends against initiating any pharmacologic urate-lowering therapy". S42, PMC §3.1: "Patients with asymptomatic hyperuricemia and SU ≥ 9 mg/dL, or those with comorbidities … should initiate ULT as per the 2019 Guideline []"; Table 2 Rec 1 (GoR 1, LoE A) lists first-line ULT for asymptomatic hyperuricaemia. S40 Table 1: "Considering the use of ULA at SUA ≥9 mg/dL and target to SUA ≤6 mg/dL". | Optional EDITORIAL, which would also serve readers the Chinese or Japanese guidelines would treat: 「需不需要用藥，請和醫師討論個人狀況。」 |
| LB-6.2 | Minor | The quote is verbatim, but its context is lost. In Chinese 2024 §3.1 the sentence belongs to the paragraph on **stopping ULT**: "Currently, there is insufficient evidence to support discontinuing medication in patients with asymptomatic hyperuricemia. A small subset of patients may be able to maintain SU levels below 360 μmol/L …". Out of that context it reads as a general verdict that lifestyle works for only a few. That quietly favours drugs, and it rests on the guideline at one end of the conflict the page set aside. | S42, PMC §3.1, verbatim as above. A neutral alternative in S44, PMC Discussion (verified, but not yet in the evidence file): "Finally, lifestyle modification is a cornerstone in the management of hyperuricemia and gout, and relevant patient education regarding diet and exercise should be espoused when treating these patients." | Preferred, after adding the HKSR sentence to the evidence file: 「調整生活型態（飲食、運動）是處理高尿酸的基礎。」（香港風濕病學會 2023・指引說明）. Or keep the source and restore its context: 「已在用降尿酸藥的人，少數可以靠飲食、運動和控制代謝症候群，把尿酸維持在較低的範圍；能否減藥，要和醫師討論。」 |
| LB-6.3 | OK | 「如家庭醫師」 is an explanatory example. | S44, PMC Discussion: "In most cases, gout and hyperuricemia can be managed in the primary care setting. Patients who are refractory to standard care may require specialist management and should be referred as and when necessary." | — |
| LB-6.T | OK (EDITORIAL) | Neutral and harmless. It agrees with S42's own caution that evidence for stopping medication is insufficient. | — | — |
| LB-M1 | Minor | Same single-figure issue as LB-1.1. Everything else is verified (LB-2.1, LB-2.4). | As for LB-1.1, LB-2.1 and LB-2.4. | 「不一定。健康的人在1:40約2到3成也呈陽性；抗核抗體只是紅斑性狼瘡分類的入門條件，診斷要由醫師評估。」 |
| LB-M2 | OK | — | S23 (abstract and WebFetch), S24 and S10 as above. | — |
| LB-M3 | Minor | Same population note as LB-5.3. The flat 「不是」 is justified by G-CAN and EULAR. | As for LB-5.2 and LB-5.3. | Optional: 「不是。尿酸高是痛風的重要危險因子，但不能只憑它診斷痛風；國外研究中，尿酸超過9 mg/dL的人，5年內約2成發生痛風。」 |
| LB-M4 | OK | The EDITORIAL ending is neutral. | As for LB-6.1. | — |
| LB-S1 | OK | — | S28, ard.bmj.com, WebFetch: "Patients presenting with arthritis (any joint swelling, associated with pain or stiffness)" / "should be referred to, and seen by, a rheumatologist, within 6 weeks after the onset of symptoms." / "The strength of this recommendation was considered ‘good’ (category B)". | — |
| LB-S2 | Minor | Faithful, but it leaves out NICE's third urgent trigger and "of undetermined cause". The page has no other route to urgency for someone who has already waited months. | NICE NG100 1.1.1, WebFetch: "Refer for specialist opinion any adult with suspected persistent synovitis of undetermined cause." / "Refer urgently (even with a normal acute-phase response, negative anti-cyclic citrullinated peptide [CCP]" / "antibodies or rheumatoid factor) if any of the following apply:" / "the small joints of the hands or feet are affected" / "more than one joint is affected" / "there has been a delay of 3 months or longer between onset of symptoms and seeking medical advice." Tag: "[2009, amended 2018]". | 「關節持續腫脹，應請專科醫師評估；如果是手腳小關節、不只一個關節腫，或症狀已超過3個月才就醫，即使類風濕因子或抗CCP抗體陰性，也應盡快。」 |

**Other visible text (not numbered rows).**
- **Intro:** neutral; it never implies the reader is sick or healthy.
- **Card summaries:** all six are consistent with the verified points. 「數值越高越少見」 is supported by CRA's 20% at 1:40 vs 5% at 1:160.
- **Optional EDITORIAL line:** I support adding the line the writers proposed, 「對報告有疑問，可以帶著報告和醫師討論。」. It is neutral, harmless, and gives worried readers without symptoms somewhere to go.

**Writer requests not resolved.**
- **APLAR 2021 statements on asymptomatic hyperuricaemia:** could not access. The Murdoch research portal has the abstract only, and the medthority summary gives no direction.
- **Taiwan 2018 consensus full text:** not re-attempted. It is closed access, as the evidence file records.

**Cross-page note for the gout page.** The S32 PMC extraction also drops a word in the first-flare recommendation ("Initiating ULT is conditionally recommendedin patients with gout experiencing their first gout flare"). Please make sure the gout page did not take any direction from the PMC text.

## 3. Quote verification log

| S-ID | Quote (first words) | Status | Where verified |
|---|---|---|---|
| S3 | "The 2019 EULAR/ACR classification criteria for SLE include positive ANA at least once…" (C14, both cuts) | Verified | PMC6827566 abstract; also the ARD co-published abstract (PubMed; British spelling) |
| S3 | "They endorsed “positive ANA (≥1:80 by HEp-2 immunofluorescence)”…" | Verified | PMC, Results Phase 2a |
| S3 | "Such an approach was thought to reflect underlying SLE pathogenesis…" | Verified | PMC, Methods |
| S3 | "In the phase 1 early SLE cohort, 99.5%… / Using ANA as entry criterion…" | Verified | PMC, Discussion |
| S3 | "The concept that all criteria are only to be counted…" | Verified | PMC, Discussion |
| S3 | "However, it is important to stress that classification criteria are not designed…" / "Diagnosis of SLE remains the purview…" | Verified | PMC, Discussion |
| S4 | "For ANA at titers of 1:40, 1:80, 1:160, and 1:320…" | Verified | PubMed abstract (PMID 28544593) |
| S4 | "ANAs at a titer of 1:80 have sufficiently high sensitivity…" | Verified | PubMed abstract |
| S5 | "Indeed, higher antibody levels are better associated with SARD…" | Verified | PMC6585284, Introduction |
| S5 | "Commonly found as high titer HEp-2 IIFA-positive in apparently healthy individuals…" | Verified (caveat in the same cell, see LB-1.2) | PMC, Table 1 (AC-2) |
| S5 | "Altogether, it is evident that, with the exception of the centromere pattern (AC-3)…" | Verified | PMC, Discussion |
| S5 | "Therefore, in the EASI/IUIS recommendations, it is advocated…" | Verified | PMC, Discussion |
| S5 | "the number of clinically unexpected positive results…" | Verified | PMC, Discussion |
| S6 | "These alternative platforms differ in their antigen profiles…" | Verified | PubMed abstract (PMID 24126457) |
| S7 | "1. Do not test antinuclear antibody (ANA) subserologies… Grade 1C…" | Verified | PMC4106486, Final Top 5 item 1 and grading paragraph |
| S7 | "This suggestion follows from several principles…" | Verified | PMC, item 1 discussion |
| S7 | "However, newer testing may complicate patient care…" | Verified | PMC, item 1 discussion |
| S8 | "With the HEp-2 substrate, about 20% of normal people…" | Verified (WebFetch ×2; matches the evidence file's reads; cites Kavanaugh 2000) | jrheum.org/content/42/4/682 |
| S8 | "Do not order antinuclear antibodies (ANA) as a screening test…" | Verified (WebFetch) | jrheum.org, item 1 |
| S10 | "RF may also be elevated in healthy individuals, as well as in scenarios such as infection and malignancy." | Verified (WebFetch; now 2 independent reads) | jrheum.org First Release PDF, main text |
| S23 | "The classification criteria can be applied to any patient or otherwise healthy individual…" | Verified (WebFetch; "at least one joint" also in PubMed abstract) | ard.bmj.com/content/69/9/1580; PubMed 20699241 |
| S23 | "The working group has deliberately labelled these criteria as ‘classification criteria’…" | Verified (WebFetch ×2; see LB-3.T for the following sentences) | ard.bmj.com, Discussion |
| S24 | "The pooled sensitivity, specificity… / Anti-CCP antibodies are more specific than RF…" | Verified | PubMed abstract (PMID 17548411) |
| S25 | "In cohort studies that investigated second-generation…" / "Anti-CCP2 had greater specificity…" | Verified | PubMed abstract (PMID 20368651) |
| S28 | "Patients presenting with arthritis (any joint swelling, associated with pain or stiffness)…" plus "category B" | Verified (WebFetch; matches the evidence file's 2 reads) | ard.bmj.com/content/76/6/948, Rec 1 |
| S29 | "Refer for specialist opinion…" / "Refer urgently (even with…)" plus bullets | Verified (WebFetch) | nice.org.uk/guidance/ng100/chapter/Recommendations, 1.1.1 |
| S31 | "Autoantibody screening revealed rheumatoid factor (RF)… 20.8%…" | Verified | PubMed abstract (PMID 37055257) |
| S32 | "Recommendations in this guideline apply to patients with gout, except for a single recommendation…" | Verified (machine-checked) | PMC10563586, Methods |
| S32 | "From observational studies… only 20% went on to develop gout within 5 years ()." | Verified (machine-checked) | PMC, Results |
| S33 | "Initiating ULT is conditionally recommended against in patients with asymptomatic hyperuricemia." | Verified (WebFetch). Direction independently corroborated by S40, MDedge and the S32 rationale. | Deep Blue art41247.pdf (text and Table 1, "High†") |
| S34 | "The diagnosis of gout should not be made on the presence of hyperuric a emia alone." / "…solely as a strong risk factor…" | Verified (WebFetch; Rec 4 also in the PubMed abstract) | ard.bmj.com/content/79/1/31 |
| S34 | "For instance, only 22% of asymptomatic patients…" / "…only half of patients with SUA levels above 10 mg/dL…" | Verified (WebFetch; the 22% sentence read twice) | ard.bmj.com |
| S36 | "There was consensus agreement that the label ‘gout’ should be restricted…" | Verified | PMC7288724 abstract; PubMed abstract |
| S37 | "For ‘hyperuric(a)emia’, it was considered beyond the scope…" | Verified | PMC6252290, Results |
| S40 | "Considering the use of ULA at SUA ≥9 mg/dL…" / "In patients with a SUA ≥8 mg/dL who have complications…" | Verified (WebFetch) | J-STAGE html, Table 1 and Figure 4 legend |
| S42 | "Hyperuricemia, defined by elevated concentration of serum urate (SU) exceeding…" | Verified | PMC12280528, Introduction |
| S42 | "Patients with asymptomatic hyperuricemia and SU ≥ 9 mg/dL…" | Verified | PMC, §3.1 |
| S42 | "A small subset of patients may be able to maintain SU levels below 360 μmol/L…" | Verified (context: stopping ULT, see LB-6.2) | PMC, §3.1 |
| S44 | "In most cases, gout and hyperuricemia can be managed in the primary care setting…" | Verified | PMC10345000, Discussion |
| — | EDITORIAL (LB-6.T, end of LB-M4) | Not applicable (no source); wording checked, neutral | — |

**Additional facts checked (not in quote cells):**
- **2019 SLE criteria, "≥1 clinical criterion" rule:** confirmed by 2 secondary sources; the primary figure is an image and was not readable.
- **Campion 1987 and Dalbeth 2018:** populations confirmed from the PubMed abstracts.
- **CRA 2015:** the 20%/5% sentence cites reference 10, Kavanaugh 2000.

## 4. Citation check results

All PMIDs and DOIs match PubMed (mcp__PubMed__get_article_metadata). Journal, volume, issue and pages are correct for every PubMed-indexed source. The only issues are missing or incomplete print years or final citations, listed below; none affects the content.

| S-ID | Result |
|---|---|
| S3 | OK: Arthritis Rheumatol 2019;71(9):1400-1412, PMID 31385462, DOI 10.1002/art.40930. Co-published Ann Rheum Dis 2019;78(9):1151-1159, PMID 31383717, DOI 10.1136/annrheumdis-2018-214819. |
| S4 | OK: Arthritis Care Res 2018;70(3):428-438, PMID 28544593, DOI 10.1002/acr.23292. |
| S5 | OK: Ann Rheum Dis 2019;78(7):879-889, PMID 30862649, DOI 10.1136/annrheumdis-2018-214436. |
| S6 | OK: Ann Rheum Dis 73(1):17-23 (online 14 Oct 2013), PMID 24126457, DOI 10.1136/annrheumdis-2013-203863. Volume 73 is the 2014 print year, consistent with the label "2014". |
| S7 | OK: Arthritis Care Res 2013;65(3):329-39, PMID 23436818, DOI 10.1002/acr.21930. |
| S8 | OK: J Rheumatol 2015;42(4):682-9, PMID 25641889, DOI 10.3899/jrheum.141140. |
| S10 | PMID 37527858 and DOI 10.3899/jrheum.2023-0043 correct. **Citation incomplete:** Crossref gives J Rheumatol 2023;50(12):1610-1618 (published online 1 Aug 2023; the PDF says "First Release September 1 2023"). Suggest "J Rheumatol 2023;50(12):1610-1618". |
| S23 | OK: Ann Rheum Dis 2010;69(9):1580-8, PMID 20699241, DOI 10.1136/ard.2010.138461. Co-published Arthritis Rheum 2010;62(9):2569-81, PMID 20872595, DOI 10.1002/art.27584. |
| S24 | OK: Ann Intern Med 2007;146(11):797-808, PMID 17548411. |
| S25 | OK: Ann Intern Med 2010;152(7):456-64; W155-66, PMID 20368651. |
| S28 | PMID 27979873, DOI, 76(6):948-959 correct (online 15 Dec 2016). Print year **not confirmed**: the Crossref lookup was rate-limited. Volume 76 is expected to be 2017; please add once confirmed. |
| S29 | URL correct. The page shows only "Last reviewed: 19 November 2024", so the citation's wording is accurate. Recommendation 1.1.1 is tagged "[2009, amended 2018]". |
| S31 | OK: J Microbiol Immunol Infect 2023;56(4):739-746, PMID 37055257. |
| S32 | OK: Arthritis Care Res 2020;72(6):744-760, PMID 32391934, DOI 10.1002/acr.24180 (PMC10563586). |
| S33 | OK: Arthritis Rheumatol 2020;72(6):879-895, PMID 32390306, DOI 10.1002/art.41247. |
| S34 | PMID 31167758, DOI, 79(1):31-38 correct. **Print year 2020** (Crossref published-print 2020-01). Suggest "Ann Rheum Dis 2020;79(1):31-38". |
| S36 | OK: Ann Rheum Dis 2019;78(11):1592-1600, PMID 31501138. |
| S37 | OK: Arthritis Care Res 2019;71(3):427-434, PMID 29799677. |
| S40 | PMID 33342914, DOI, 85(2):130-138 correct. **Print year 2021** (J-STAGE: "2021 Volume 85 Issue 2 Pages 130-138", advance online 18 Dec 2020). Suggest "Circ J 2021;85(2):130-138". |
| S42 | OK: Int J Rheum Dis 2025;28(7):e70375, PMID 40692263, DOI 10.1111/1756-185x.70375. |
| S44 | OK: Clin Rheumatol 2023;42(8):2013-2027, PMID 37014501, DOI 10.1007/s10067-023-06578-9. |

## Re-check after fixes (2026-10-11)

**Scope.**
- **Rows:** LB-1.1, LB-1.2, LB-1.3, LB-2.2, LB-3.T, LB-5.3, LB-6.2, LB-6.T, LB-M1, LB-M3, LB-S2 and the new LB-S3.
- **Sources:** S10, S29, S34, S38, S39 and S40.

**Diff check.**
- I compared review_labs.v1.md with review_labs.md row by row by script. Only the rows listed above changed in text, label, quotes or C-IDs.
- Every other row differs only by the appended "Fact-check 2026-10-10" notes. Those notes describe the 10 Oct verification accurately.
- labs.json matches the table.
- All changed texts are within 70 characters; the longest is LB-S2 at 69.

**Result.**
- No Critical, Major or Minor problems remain in the page text.
- All 10 Minor findings from 10 Oct are resolved.
- Two notes remain, both outside the page text (a reviewer note and evidence-field notes), plus one optional wording.

### Row-by-row

| ID | Verdict | What I checked (verbatim where relevant) | Note / exact fix |
|---|---|---|---|
| LB-1.1 | OK (resolved) | CRA 2015: about 20% at ≥1:40 and 5% at ≥1:160 (verified 10 Oct, WebFetch ×2). ICAP (PMC6585284, Discussion), verbatim: "Indeed, up to 35% of healthy controls may be positive if a screening dilution of 1/40 is used." The text 「1:40以上約20%、最多可達35%，1:160以上約5%」 matches both. The added label ICAP 2019・專家共識 is correct. | The HEp-2 method is not stated; acceptable, because LB-1.4 covers method differences. |
| LB-1.2 | OK (resolved) | The DFS70 clause is removed. What remains is ICAP C19 (verbatim) plus the S4 specificities (verbatim). | Balance for high titres comes from LB-1.1 (5% of healthy people at ≥1:160) and LB-1.3. |
| LB-1.3 | OK (resolved) | Wording as suggested. C22 is verbatim. The added S7 quote is verbatim (PMC4106486): "1. Do not test antinuclear antibody (ANA) subserologies without a positive ANA and clinical suspicion of immune-mediated disease". Label ICAP 2019・專家共識 is correct, since S7 is only supporting. | — |
| LB-2.2 | OK (resolved) | 「或」 is gone. The sentence is now an accurate necessary condition and makes no claim about which combinations of findings are enough. | **Correction to my 10 Oct rationale, which the writers' note repeats ("no longer suggests that blood tests alone could reach classification").** One of the 7 clinical domains is hematologic, and it is scored from blood counts. Evidence: the page's own S3 quote reads "7 clinical (constitutional, hematologic, …)"; the PMC text gives "leukopenia defined as a white blood cell count (WBC) <4000/mm at least once"; the MSD Manual's reproduction of the Aringer 2019 table lists Leukopenia (<4000/mcL) 3, Thrombocytopenia (platelet count <100,000/mcL) 4 and Autoimmune hemolysis 4. So classification can in principle rest on laboratory results alone, for example ANA ≥1:80 plus thrombocytopenia (4) plus anti-dsDNA (6). The accurate statement is that antibody and complement results alone cannot classify, because at least 1 clinical criterion is required. **The page must not be edited to say that blood tests alone can never qualify.** A third reproduction of the criteria table now confirms the rule. MSD Manual: "If the patient's score is 10 or more, and at least 1 clinical criterion is fulfilled, disease is classified as SLE." The primary figure is still unreadable (it is an image, and the ARD PDF fetch failed). Optional wording (68 characters) if the physician accepts that: 「通過入門條件後，還要依7類臨床表現（如皮膚黏膜、腎臟、血球）和3類免疫檢驗評分，累積10分以上且至少1項是臨床表現，才歸類為紅斑性狼瘡。」 |
| LB-3.T | OK (resolved) | 「主要」 removes the overstatement. | For information, the full S23 sentence from a single WebFetch read on 10 Oct, in two segments: "The criteria do not remove the onus on individual physicians, especially in the face of unusual presentations," / "to reach a diagnostic opinion that might be at variance from the assignment obtained using the criteria." It would support 「診斷仍由醫師判斷」 after a second read. Not required. |
| LB-5.3 | OK (resolved) | 「國外研究顯示」 is added. The S39 and S38 quotes were character-checked against the PubMed abstracts: "With urate levels of 9 mg/dl or higher, cumulative incidence of gouty arthritis reached 22 percent after five years." (PMID 3826098) and "Nonetheless, only about half of those with serum urate concentrations ≥10mg/dL develop clinically evident gout over 15 years, implying a role for prolonged hyperuricaemia and additional factors in the pathogenesis of gout." (PMID 29463518). The populations stated in the strength fields are right. S39: 2,046 initially healthy men, Normative Aging Study, followed for 14.9 years; the MeSH term is Massachusetts. S38: 18,889 gout-free participants from 4 US cohorts (ARIC, CARDIA, Framingham Original and Offspring); 15-year cumulative incidence at ≥10 mg/dL was 49% (95% CI 31–67). Low second citations beside High guideline quotes are allowed by BRIEF rule 1. | The S38/S39 notes ("this exact sentence was not quoted by the fact-check") can now read "verified verbatim in the PubMed abstract (fact-check 2026-10-11)". |
| LB-M3 | OK (resolved) | Same as LB-5.3 (S39). | — |
| LB-6.2 | OK (resolved) | The HKSR sentence is verbatim (PMC10345000, Discussion, last paragraph before "Local registry studies…"): "Finally, lifestyle modification is a cornerstone in the management of hyperuricemia and gout, and relevant patient education regarding diet and exercise should be espoused when treating these patients." 基礎 translates "cornerstone"; 例如飲食和運動 comes from "diet and exercise". Label 香港風濕病學會 2023・指引說明 is correct (Discussion text, not a numbered statement). There are no diet details, and LB-6.T stops readers from taking it as "stop medicine". | Add the quote to the evidence file, as the writers note. |
| LB-6.T | OK (EDITORIAL) | Neutral and harmless. The new first clause sends readers whom the Chinese or Japanese guideline would treat to a doctor, and it fits ACR's conditional, shared-decision recommendation. | — |
| LB-M1 | OK (resolved) | 「以1:40檢驗，健康的人約20%、最多35%會陽性」 matches CRA and ICAP. All three labels are correct. | — |
| LB-S2 | OK (resolved) | NICE 1.1.1 third bullet, verbatim (WebFetch, 10 Oct): "there has been a delay of 3 months or longer between onset of symptoms and seeking medical advice." It is rendered correctly as 「症狀出現3個月以上才就醫」. | — |
| LB-S3 | OK (EDITORIAL) | 「對報告有疑問，可以帶著報告和醫師討論。」 is neutral and harmless. | — |

**Quote cells new or changed since 10 Oct:** 6, all verbatim.
- S5 C20 ("up to 35%")
- S7 C25 (item 1)
- S29 C46 (including the third bullet)
- S44 FACT-CHECK (HKSR lifestyle sentence)
- S38 C56
- S39 C57

### Sources

| S-ID | Result |
|---|---|
| S10 | Correct. Crossref gives volume 50, issue 12, pages 1610-1618, print December 2023, online 1 Aug 2023. The PDF reads "First Release September 1 2023". |
| S29 | Correct. Matches the NICE page ("Last reviewed: 19 November 2024"; 1.1.1 tagged "[2009, amended 2018]"). |
| S34 | Correct. Crossref published-print 2020-01; PubMed date 5 Jun 2019. |
| S38 | Correct (PubMed): Ann Rheum Dis 2018;77(7):1048-1052, PMID 29463518, DOI 10.1136/annrheumdis-2017-212288. |
| S39 | Correct (PubMed): Am J Med 1987;82(3):421-6, PMID 3826098, DOI 10.1016/0002-9343(87)90441-4. |
| S40 | Correct. J-STAGE: "2021 Volume 85 Issue 2 Pages 130-138"; advance online 18 Dec 2020. |
| S28 (unchanged) | Print year still unconfirmed; the Crossref record was unreachable again. |

### Remaining items (none in the page text)

1. **Minor, reviewer note on LB-2.2.**
   - Replace "means the sentence no longer suggests that blood tests alone could reach classification" with "means the sentence no longer suggests that antibody or complement results alone could reach classification (blood-count abnormalities belong to the hematologic clinical domain)".
   - Also delete "The fact-check confirmed it only through two secondary sources" or update it to "three secondary sources (The Rheumatologist; ebm.one; MSD Manual)".
   - Do not add any patient text saying that blood tests alone cannot qualify.
2. **Cosmetic, evidence fields.**
   - S38/S39 notes: change to "Fact-check 2026-10-11: verified verbatim in the PubMed abstract".
   - The C33 note in LB-3.T: remove the irrelevant "'at least one joint' also in the PubMed abstract".
3. **Optional:** the LB-2.2 wording in the table above.
