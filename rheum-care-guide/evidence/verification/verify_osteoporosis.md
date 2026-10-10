# Independent fact-check: 骨質疏鬆症 (slug: osteoporosis)

- Checked: /home/claude/newpages/review/review_osteoporosis.md (41 statements) against /home/claude/newpages/content/osteoporosis.json and the original publications.
- Evidence files used only as leads (unverified secondary notes): /home/claude/newpages/research/osteoporosis.md; /home/claude/cheng1276.github.io/rheum-care-guide/evidence/research/common.md.
- Date: 2026-10-10. I did not write this content. I did not edit any content or evidence file.

**How the originals were read**
- PubMed full text (PMC), searched with python: S1 NOGG 2024 (PMC12417299), S3 BHOF 2022 (PMC9546973), S4 Osteoporosis Canada 2023 (PMC10610956), S5 RACGP 2024 (PMC12088310), S7 ESCEO/IOF 2019 (PMC7026233), S11 World Falls Guidelines 2022 (PMC9523684), S16 Strong, Steady and Straight 2022 (PMC9304091), S17 Asia-Pacific men 2025 (PMC12209010), S18 AFOS MRONJ 2026 (PMC13069298).
- PubMed abstracts: S8 Endocrine Society 2024 (PMID 38828931); S21 Kunutsor 2018 (PMID 32300705).
- Publisher pages via WebFetch: BHOF Springer PDF and Springer HTML (to check the dropped words). TOA 2021 PDF (cghdpt.cgmh.org.tw), read 3 times. MOHW 2014 press release cp-16-22557-1. MOHW 2018 press release cp-16-40152-1, read twice. News reports (CNA, CommonHealth, UDN, TheNewsLens, 2026) on the draft revision of the 每日飲食指南.
- My WebFetch reads were separate from the writers' reads. I asked for verbatim Chinese, character by character, and gave only the location to look in, never the target sentence.
- Not accessible: TOA 2025 PDF (toa1997.org.tw; ROBOTS_DISALLOWED, not circumvented); Europe PMC (robots / server error). Shell downloads from Springer were refused by the egress proxy (HTTP 403). I did not retry.
- A programmatic comparison found the review table identical to the JSON (41/41 rows: text, strength labels and quotes; the intro also matches).

---

## 1. Summary counts

| Verdict | Statements (of 41) |
|---|---|
| OK | 27 |
| Minor | 13 (OP-2.2, OP-2.5, OP-3.3, OP-3.T, OP-4.5, OP-5.3, OP-5.5, OP-6.2 [EDITORIAL], OP-6.3, OP-6.4, OP-6.5, OP-M2, OP-M3) |
| Major | 1 (OP-2.3) |
| Critical | 0 |

- **Quotes:** 88 non-editorial evidence quotes, plus 1 EDITORIAL entry.
  - 88 of 88 were verified against the originals, with no mismatches.
  - 76 matched programmatically against the PMC full text (after normalising quotation marks and dashes, and splitting at "…").
  - 5 were read in the PMC full text (S5 ×4, S17 ×1).
  - 3 were checked against PubMed abstracts (S8 ×1, S21 ×2).
  - 4 were verbatim WebFetch reads of Taiwanese originals (S26 ×2, S29 ×2). Each of these now has two independent reads that agree, the writers' and mine.
  - Could not access: none of the quoted originals. Not accessible but relevant: TOA 2025 (S28).
- **Every number on the page and its population were checked** (see the table in section 2b). All are correct for the source cited. One number is outdated or under revision at the national level: OP-2.3, dairy cups and the "低脂" wording.

### Extra checks requested

**A. BHOF 2022 (S3) dropped words: CONFIRMED.** The PMC text has four glued words. I checked each one against two separate publisher renderings, the Springer PDF and the Springer HTML article page.

| PMC text (glued) | Publisher text | Springer PDF | Springer HTML |
|---|---|---|---|
| "when an adequate dietary intakebe achieved" | "calcium supplements should be used when an adequate dietary intake **cannot** be achieved" | ✓ | ✓ ("cannot be achieved") |
| "intake ofcalcium above 1200 to 1500 mg/day" | "However, there is evidence that intake of **supplemental** calcium above 1200 to 1500 mg/day" | ✓ | ✓ ("supplemental") |
| "milligrams ofcalcium in the supplement" | "Calcium intake recommendations refer to milligrams of **elemental** calcium in the supplement." | ✓ | not asked |
| "that havefound supplemental vitamin D" | "in populations around the world that have **not** found supplemental vitamin D" | ✓ | ✓ ("not") |

None of these four sentences is quoted on the page. The page wording is consistent with the restored meaning: OP-2.1 says to add supplements only when food is not enough. The page makes no claim that vitamin D prevents falls, and none about kidney stones.

**B. Taiwanese sources.**
- **TOA 2021 (S26): verified.**
  - BMD-testing list (Ch. 3 §2, my independent read; page numbers not returned): 「(1) 65歲以上的婦女或70歲以上男性。」「(2) 65歲以前且具有危險因子的停經婦女。」「(4) 50至70歲並具有骨折高風險因子的男性。」「(5) 脆弱性骨折者 (指在低衝擊力下就發生骨折)。」 These match the evidence-file quotes character by character.
  - Calcium and vitamin D: 「50 歲以上成人每日至少需攝取飲食鈣量 1200 毫克(包括鈣片補充劑量)和維生素 D 800 至 1000 國際單位」. This is relevant to OP-2.2.
  - Citation: cover and copyright page give 「2021 台灣成人骨質疏鬆症防治之共識及指引」, 中華民國骨質疏鬆症學會, 主編 黃兆山, 「中華民國 110 年 10 月版」, ISBN 978-986-88615-6-5. This matches the source list.
  - TOA 2025 could not be read (robots.txt), so I cannot say whether the 2021 list or calcium figure changed.
- **MOHW/HPA 2014 (S29): quotes verified verbatim, but the source is outdated for dairy.**
  - Title 「「聰明補鈣，堅固骨本」近100%兒童與青少年及8成以上成人鈣攝取不足」, 建檔日期 103-01-23.
  - 「我國每日飲食指南建議每人每日應攝取1.5-2杯低脂乳品，每杯240 c.c.的低脂乳品約含240 mg的鈣質。」 and 「2.攝取高鈣食物: 包括起司、黑芝麻、小魚干、傳統豆腐、深綠色蔬菜等(附件2)。」
  - The 2018 national guide (MOHW press release 107-03-13, read twice) says: 「不再強調乳品需選用低脂或脫脂為佳的說法，將「低脂乳品類」名稱改成「乳品類」」 and 「全脂與低脂乳品好處相同，建議每日攝取1.5-2杯乳品類，增進鈣質攝取，保持骨質健康。」
  - In March 2026 the 國健署 published a draft 9th edition that lowers dairy to 1 cup (about 240 mL) a day. CommonHealth 2026-03-13: 「乳品類建議量從每天1.5～2杯，下修為1杯（1杯約240毫升）」; 「目前為草案」. CNA 2026-04-01: the comment period had closed, and the aim was for the new guide 「今年內…正式上線」. CNA also reports that the agency will set individual recommendations for 長者.
  - I could not confirm whether the 9th edition has been finalised as of today. See OP-2.3.

**C. Drug names (OP-6.3, OP-6.4, OP-S2).**
- The safety messages say exactly what the sources say:
  - NOGG Recs 7, 8, 9 and 12 (all Strong).
  - Osteoporosis Canada Rec 4.5 remark: "risk of rapid bone loss and vertebral fractures with delayed dosing or discontinuation of denosumab".
  - RACGP Rec 26 (Grade C): "Denosumab therapy should not be interrupted." The RACGP text adds: "even delaying the injection by more than four months can be associated with rebound bone resorption and vertebral fractures".
- 「雙磷酸鹽類」 is the term the Taiwanese guideline itself uses (TOA 2021: 「口服雙磷酸鹽」). TOA writes denosumab in English, as 「RANKL 單株抗體(denosumab)」.
- **Harm if misread.** If someone who is not on denosumab applies these warnings to themselves, no harm follows: they would keep taking their drug and see their doctor, which is safe. The real risk is the opposite. A patient on denosumab may not recognise the INN, and then misses the most important warning on the page.
  - The sources give an identifying interval that is not a dose: NOGG "a subcutaneous injection of 60 mg once every 6 months"; TOA 2021 drug table 「Denosumab 每半年」 (my single read); RACGP "specified six‐monthly intervals".
  - Fix: add 「每半年打一次的…皮下注射針劑」 without the dose (OP-6.3), and a short descriptor for the bisphosphonate class (OP-6.4).

**D. EDITORIAL phrase 「不要自行停藥」 (OP-6.2).**
- It is neutral and appropriate in almost all cases. It matches the purpose of NOGG Rec 7, "should not be stopped or delayed without discussion with a healthcare professional".
- As an absolute rule, though, it is not harmless in every case. Some situations call for stopping and seeking care. Example: oral bisphosphonate leaflets tell patients to stop and seek medical attention for painful swallowing or chest pain. This is general knowledge, not in the evidence files; BHOF lists "difficulty swallowing, esophageal inflammation" as side effects.
- A softer wording is suggested under OP-6.2 (Minor).

---

## 2. Findings table

| ID | Verdict | Problem | What I checked (source, location, verbatim text seen) | Suggested fix |
|---|---|---|---|---|
| OP-1.1 | OK | — | S5 Box 1 Rec 1, Grade "A": "All individuals over the age of 50 years who sustain a fracture following minimal trauma (such as a fall from standing height, or less) should be considered to have a presumptive diagnosis of osteoporosis." 「超過50歲」 = "over the age of 50". | — |
| OP-1.2 | OK | — | S3 "Secondary fracture prevention": "…tripping and breaking a bone is not bad luck, or a particularly hard fall, it is osteoporosis and it will lead to additional fractures if untreated, particularly in the short term." S1 "Summary of main recommendations" (ungraded list) item 10: "Start treatment promptly following a fragility fracture, because the risk of re-fracture is highest immediately after a fracture and the risk remains elevated." S4 Table 3 Rec 3.8 "Strong recommendation; high-certainty evidence" (supporting only). 指引說明 is correct. | — |
| OP-1.3 | OK | TOA 2021 may have been superseded by TOA 2025, which neither the writers nor I could read. The BHOF support is independent and verified. | S3 Synopsis "Diagnostic assessment recommendations": "Perform BMD testing in the following: / –Women aged ≥ 65 years and men aged ≥ 70 years." S26 Ch. 3 §2, my WebFetch read: 「(1) 65歲以上的婦女或70歲以上男性。」 The softening to 「可和醫師討論」 is a justified understatement, given the USPSTF, RACGP and Canada differences in the evidence file. | Check against TOA 2025 if the physician can download it. |
| OP-1.4 | OK | Same TOA 2025 caveat. | S3: "–Postmenopausal women and men aged 50–69 years, based on risk profile." / "–Postmenopausal women and men aged ≥ 50 years with history of adult-age fracture." S26: 「(2) 65歲以前且具有危險因子的停經婦女。」「(4) 50至70歲並具有骨折高風險因子的男性。」「(5) 脆弱性骨折者 (指在低衝擊力下就發生骨折)。」 「成年後曾骨折」 matches BHOF's "adult-age fracture". | — |
| OP-2.1 | OK | — | S1 "Non-pharmacological management: Recommendations". Population: "Postmenopausal women and men, age ≥ 50 years, with osteoporosis or who are at risk of fragility fracture". Text: "An adequate intake of calcium (minimum 700 mg daily) preferably achieved through dietary intake or otherwise by supplementation (Strong recommendation)." S4 Table 2 Rec 2.1, "Conditional recommendation; moderate-to-high-certainty evidence", verbatim. Consistent with the restored BHOF "cannot be achieved". | — |
| OP-2.2 | Minor | Numbers and populations are correct for BHOF and Canada (Canada's band starts at 51). They differ from the Taiwanese figures a reader may hear locally. TOA 2021 gives ≥1,200 mg for all adults over 50, so the page's 1,000 mg for men 50–70 is lower. The HPA 2014 adult DRI is 「成人則為1000 mg」, so the page's 1,200 mg for women ≥51 is higher. The writers flagged this too. | S3 Synopsis "Universal recommendations": "Recommend a diet with adequate total calcium intake (1000 mg/day for men aged 50–70 years; 1200 mg/day for women ≥ 51 years and men ≥ 71 years), incorporating calcium supplements if intake is insufficient." S4 Rec 2.1 remark: "1000 mg/d (males aged 51–70 yr) and 1200 mg/d (females > 50 yr and males > 70 yr)." S26 calcium sentence (my read, quoted in section B). | Physician's decision. The text is accurate as attributed. Optionally add BHOF's verified caveat at the end: 「超過建議量並沒有額外好處。」 (S3: "There is no evidence that calcium intakes in excess of recommended amounts confer additional bone benefit."). Re-check once TOA 2025 is available. |
| OP-2.3 | **Major** | The text reproduces a 2014 press release that quotes an older food guide. (1) The 「低脂」 qualifier was dropped from the national guide in 2018. (2) The 1.5–2 cup figure is under revision: a 9th-edition draft (March 2026) lowers it to 1 cup a day, and I could not confirm whether that draft has been finalised. The label 「國健署 2014」 points readers to a superseded source. The quotes themselves are accurate to the 2014 page. | S29 (my read): 「我國每日飲食指南建議每人每日應攝取1.5-2杯低脂乳品，每杯240 c.c.的低脂乳品約含240 mg的鈣質。」 MOHW 107-03-13 (cp-16-40152-1, read twice): 「不再強調乳品需選用低脂或脫脂為佳的說法，將「低脂乳品類」名稱改成「乳品類」」; 「全脂與低脂乳品好處相同，建議每日攝取1.5-2杯乳品類…」. CommonHealth 2026-03-13: 「第9版《每日飲食指南》草案」, 「從每天1.5～2杯，下修為1杯（1杯約240毫升）」. CNA 2026-04-01: comment period closed, aim to go live within 2026. The food list (S29 item 2) and BHOF "low-fat dairy products…" are verified. | Replace the text with 「多選含鈣食物：每天1.5到2杯乳品（每杯240毫升），再搭配起司、傳統豆腐、深綠色蔬菜、小魚干、黑芝麻等。」 and cite 衛福部國健署 2018-03-13「國健署公布107年最新版『每日飲食指南』」 (https://www.mohw.gov.tw/cp-16-40152-1.html) as 「國健署 2018」. **Before publishing, check whether the 9th edition has been finalised.** If it has, use its figure, or drop the cup count: 「多選含鈣食物，例如乳品（每杯240毫升）、起司、傳統豆腐、深綠色蔬菜、小魚干、黑芝麻等。」 |
| OP-2.4 | OK | The text is faithful. Small simplifications, with no change needed: NOGG's "from foods or be prescribed vitamin D supplements" becomes 補充, and 「至少」 has no upper bound. NOGG's text says "800 up to 2000 IU daily may—be appropriate" (IV). | S1 Recommendations (Strong) verbatim, including "Those who are either housebound or living in residential or nursing care are more likely to require calcium and vitamin D supplementation…". TOA 2021 agrees: 「50 歲以上成人應每日攝取 800 至 1000 IU 維生素 D」. | Optional: 「…建議和醫師討論，每天至少補充800國際單位。」 |
| OP-2.5 | Minor | NOGG says "**Routine** intermittent administration… is not advised", but the page drops "routine". NOGG itself recommends treating deficiency, including an oral loading dose before zoledronate. A patient could therefore refuse a dose their doctor prescribed. | S1 "Calcium and vitamin D" (Ia) verbatim. S8 abstract verbatim ("suggests…daily administration…rather than intermittent use of high doses"). S1 denosumab/zoledronate text: "treated with vitamin D (e.g., 100,000 to 300,000 IU orally as a loading dose in divided doses) before zoledronate treatment is initiated". S1 Rec 17: "Treat vitamin D deficiency and insufficiency prior to initiation of parenteral anti-osteoporosis drug treatment…". | 「需要補充維生素D時，以每天補充為原則；不建議常規隔一段時間才吃一次很大劑量（例如60,000國際單位以上），有報告指出這和骨折、跌倒增加有關。醫師為治療缺乏而另外開立的劑量，請依醫囑。」 |
| OP-2.T | OK | — | S1 "Dietary modification": "Protein is an important constituent of bone and muscle tissue, and good dietary intake is necessary to maintain the health of the musculoskeletal system." | — |
| OP-3.1 | OK | — | S1 Recommendations (Strong): "A combination of regular weight-bearing and muscle strengthening exercise, tailored according to the individual patient's needs and ability". S3 "Regular weight-bearing…": "…include walking, jogging, tai chi, stair climbing, dancing, and tennis." Leaving out jogging and tennis is justified by the BHOF injurious-activities list. | — |
| OP-3.2 | OK | The frequency (≥ twice weekly) is left out, which is acceptable. | S4 Table 2 Rec 1.1, "Strong recommendation; moderate-certainty evidence": "…balance and functional training ≥ twice weekly to reduce the risk of falls…(e.g., chair stands for sit-to-stand ability, stair-climbing to train for hiking)". The PMC list after "such as:" is missing; the quote is unaffected. | Optional: add 「每週至少2次」. |
| OP-3.3 | Minor | The text is faithful, but readers may take 「練到腹部」 to mean sit-ups or crunches, the very movement OP-4.1 warns about. SSS Box 3: "Movements or exercise that involve sustained, repeated or end-range flexion should be modified or avoided. [C]"; "alternatives to exercises such as the 'roll down' and 'curl up' in Pilates should be considered. [C]". Kunutsor: sit-ups were "associated with a greater risk of vertebral fractures but these events were rare". | S4 Table 2 Rec 1.2, "Conditional recommendation; low-certainty evidence": "…including exercises targeting abdominal and back extensor muscles…". S16 Box 1: "All muscle groups should be targeted, including back muscles to promote bone strength in the spine. [C]". | 「肌力訓練要循序漸進增加強度，並練到腹部和背部肌肉；練腹部時，仰臥起坐這類反覆彎腰的動作要小心（見「保護脊椎」）。」 |
| OP-3.4 | OK | Drops "or modified for safety", a small omission. | S4 Table 2 Rec 1.3, "Conditional recommendation; very low-certainty evidence", verbatim including "in addition to, but not instead of, balance, functional and resistance training." | Optional: 「能安全進行（或調整後能安全進行）就可以做」 |
| OP-3.5 | OK | — | S3: "To avoid injury, patients should be evaluated before initiating a new exercise program, particularly one involving compressive or contractile stressors (such as running or weightlifting)." | — |
| OP-3.T | Minor | The WFG sentence is about falls-prevention exercise programmes. Placed in the bone-exercise card, it stretches "benefits" to cover bone. | S11 "Exercise and physical activity interventions": "Benefits of exercise are lost on cessation so opportunities to continue with appropriate activity at the end of the programme are important." | Move it to the 預防跌倒 card, or write 「停止運動後，預防跌倒等好處會消失；運動課程結束後，也要繼續做適合的活動。」 |
| OP-4.1 | OK | — | S1 "Exercise to improve or maintain bone density" (narrative, Ia): "…repetitive forced spinal forward flexion exercises should be undertaken with care…". S16 Box 3 [C] verbatim. S21 abstract verbatim. Labels 指引說明 and 專家共識 are correct. | — |
| OP-4.2 | OK | — | S16 Box 3, "Safe techniques for day-to-day moving and lifting are: [C]", followed by the "Think straight", safe-lifting and "hip hinge" bullets verbatim. S3 "Protecting fragile bones…": "– Modification: Bend with knee and hips not spine, stand close to load when bending, hold load close to body." and "BHOF recommends guidance on spine-sparing techniques (e.g., hip hinge) by trained occupational and/or physical therapy professionals…". | — |
| OP-4.3 | OK | The text is faithful. BHOF's preceding bracing clause, which conflicts with NOGG, is correctly not used. The BHOF sentence is conditional ("If bed rest is recommended"), and 「需要臥床時」 is an acceptable rendering. | S3 "Vertebral fracture rehabilitation": "…partial bed rest (4 days or less). If bed rest is recommended, a few 30- to 60-min periods each day of sitting upright and walking around are valuable… Prolonged inactivity should be avoided." S7 "General management / Mobility and falls" sentence verbatim (grammar as printed). | Optional: 「醫師建議臥床時」 |
| OP-4.4 | OK | The Strong recommendation covers what the programme contains. Physiotherapist supervision comes from NOGG's narrative (Ib) and SSS [C], which is acceptable. The page correctly claims no pain benefit. | S1 "Management of symptomatic osteoporotic vertebral fractures": Strong recommendation verbatim, and "Physiotherapist supervised exercise following vertebral fracture improves pain and physical performance []; (Evidence level Ib)". S16 Box 3 "For people with osteoporosis with vertebral fracture" verbatim. | — |
| OP-4.5 | Minor | The text is faithful. The population is confirmed by the SSS abstract: "People with vertebral fracture or multiple low trauma fractures should usually exercise only up to an impact equivalent to brisk walking." But 衝擊性運動 is not explained (no glossary entry), so readers may not know what to limit. SSS's "usually" and its precautionary framing are lost, which errs on the safe side. | S16 Box 1 [C] verbatim (sub-headings glued in PMC; mapping confirmed by the abstract). S1 narrative: "People at risk of falls, or with vertebral fractures, may need more specific advice and assessment before increasing exercise intensity []." | 「曾有脊椎骨折或多次輕微外傷骨折的人，衝擊性運動（例如跑步、跳躍）一般以快走的程度為上限；想加強運動前，先請醫療人員評估。」 SSS examples of moderate impact: "stamping, jogging, low-level jumping, hopping". |
| OP-4.T | OK | — | S1 Conditional recommendation verbatim, and narrative (Ia) "…in an unloaded position, such as supine". | — |
| OP-5.1 | OK | 「或」 is correct. NOGG's own summary says "Assess falls risk in patients with osteoporosis and/or fragility fractures…". This answers the writers' question. | S1 Recommendations (Strong) verbatim. S1 "Summary of main recommendations". | — |
| OP-5.2 | OK | — | S11 Table 5, WG 4, 1A: "…balance challenging and functional exercises (e.g. sit-to-stand, stepping), with sessions three times or more weekly which are individualised, progressed in intensity for at least 12 weeks and continued longer for greater effect." | — |
| OP-5.3 | Minor | The 1B label belongs to clinician-delivered home modification within a multidomain intervention, for which WFG reports the greatest benefit at highest risk. The page presents a self-help list, with the occupational therapist as optional. The four list items come from the ungraded ESCEO/IOF narrative. | S11 Table 5, WG 10, 1B: "We recommend modifications of an older adult's physical home environment for fall hazards… should be provided by a trained clinician, as part of a multidomain falls prevention intervention." S7 "(slippery floors, obstacles, insufficient lighting, handrails)". S3 synopsis and S1 (Ia) verbatim. | 「改善居家環境：地面防滑、移開雜物、照明充足、加裝扶手；跌倒風險較高的人，最好請職能治療師等受過訓練的人員到家評估。」 |
| OP-5.4 | OK | — | S11 Table 5, WG 2, 1B verbatim. S3 synopsis ("sedating medications, polypharmacy…") verbatim. S7 fragment verbatim. The wording does not encourage stopping medicines on one's own. | — |
| OP-5.5 | Minor | WFG frames the multifocal advice as "achieving optimal safe functional vision… avoiding the wearing of multifocal glasses when outside". 「避免戴多焦點眼鏡」 on its own could be read as going out without glasses. The new-glasses clause gives the risk but not the point of the counselling (take care). WFG also says many older adults "would benefit from wearing new spectacles with the correct prescription". | S11 "Vision interventions": "Evidence from randomised controlled trials… cataract surgery for the first eye, [] and both eyes [] and achieving optimal safe functional vision by active older adults avoiding the wearing of multifocal glasses when outside [] are effective fall prevention strategies." and "…counsel their clients about likely short-term increased fall risk when dispensing new prescription glasses." | 「處理視力問題：需要時接受白內障手術；常外出活動的人，在戶外避免戴多焦點眼鏡，改戴其他能看清楚的眼鏡；剛配新眼鏡的一段時間內，跌倒風險可能增加，走路要特別小心。」 |
| OP-5.T | OK | — | S11: "Pendent or wrist alarms, telehealth falls detectors, cord alarms or mobile telephones are also important in enabling people to call for help if they cannot get up if they live alone…" | — |
| OP-6.1 | OK | — | S1 Summary item 16 verbatim. S3 abstract: "All antifracture therapeutics treat but do not cure the disease." / "The diagnosis of osteoporosis persists even if subsequent DXA T-scores are above − 2.5." S3 "Duration of treatment" verbatim. | — |
| OP-6.2 | Minor (EDITORIAL) | The source quotes are verbatim. The EDITORIAL 「不要自行停藥」 is neutral in almost all cases, but as an absolute it can clash with cases where stopping and seeking care is correct. Example: oral bisphosphonate leaflets say to stop and seek medical attention for painful swallowing or chest pain (general knowledge, not in the evidence). In NOGG, stopping after an AFF is the doctor's decision (Rec 15). | S3 "Duration of treatment": "Therapeutic benefits can be maintained only with treatment." S1 "Models of care", Strong recommendation, verbatim. BHOF lists "difficulty swallowing, esophageal inflammation" as oral bisphosphonate side effects. | 「骨鬆藥的效果，要持續用藥才能維持；有疑問或出現難以接受的副作用時，請盡快和醫師討論，不要因為擔心就自行停藥；出現嚴重不適時，請立即就醫。」 |
| OP-6.3 | Minor | All four quotes are verbatim, and the message matches the sources exactly (Strong label correct). The risk is non-recognition: patients often do not know the INN. An identifying interval is available in the sources (see section C), and no dose would be printed. | S1 Recs 7 and 8 (Strong) verbatim. S1: "Denosumab is given as a subcutaneous injection of 60 mg once every 6 months." S4 Table 4, Rec 4.5 remark verbatim. S5 Rec 26 (Grade C) verbatim, and "even delaying the injection by more than four months can be associated with rebound bone resorption and vertebral fractures". S26 drug table 「Denosumab 每半年」. | 「使用 denosumab（一種每半年打一次的骨鬆皮下注射針劑）的人，不要自行停藥或延後注射；需要停藥時，請醫師安排接續的治療，以免脊椎骨折風險增加。」 |
| OP-6.4 | Minor | Verbatim to NOGG Rec 9 (Strong). 「雙磷酸鹽類」 matches the TOA term. Two issues: (a) patients may not recognise the class name; (b) mouth symptoms should also go to the dentist. | S1 "Rare adverse effects…", Rec 9 verbatim. S18 §3.5.2 verbatim. S4 GPS 6.6 remark: "oral cavity lesions should be evaluated by a dentist". S1 lists "Oral bisphosphonates (alendronate, ibandronate and risedronate)" and IV zoledronate. | 「使用雙磷酸鹽類藥物（有口服和靜脈注射兩種）或 denosumab 期間，保持口腔清潔、定期看牙醫；牙齒鬆動、口腔疼痛或腫脹時，請告訴醫師或牙醫師。」 |
| OP-6.5 | Minor | Both quotes are verbatim. The text leaves out NOGG Rec 11's own caveat that the treating physician guides the plan. For denosumab, the timing of extractions is planned, and the sources even disagree on it. The AFOS sentence is about not delaying the start of therapy; AFOS also says care "may proceed concurrently in patients already receiving antiresorptive agents", so 「不需要延後」 is acceptable. | S1 Rec 11 (Conditional), full text: "…Clinical judgment of the treating physician should guide the management plan of each patient based on individual benefit/risk assessment, ensuring patients continue to access routine dental care". S5 Rec 45: "Invasive dental procedures in patients on denosumab should be performed just before the next six‐monthly injection…". S18: "…should ideally be performed 3–4 months after the last injection". | 「洗牙、補牙、做假牙，不需要延後骨鬆治療；拔牙等侵入性治療宜盡量減少，有需要時，請先讓醫師和牙醫師一起評估、安排時間，多數人仍可安全進行。」 |
| OP-6.T | OK | — | S1 Rec 16 (Strong) verbatim. S4 Table 2, GPS 2.4 verbatim. | — |
| OP-M1 | OK | — | S5 introduction: "Deterioration of skeletal tissue proceeds with no symptoms until a symptomatic fracture occurs…". S3 "Vertebral fracture rehabilitation": "Two thirds of vertebral fractures are subclinical 'silent' fractures." S3 "Vertebral fractures": "…5-fold increased risk for additional vertebral fractures and a 2- to 3-fold increased risk for fractures at other sites." S1 "Vertebral fracture assessment" (Ia) verbatim. | — |
| OP-M2 | Minor | The figure is correct, but it is a UK estimate. 「英國指引估計」 can be read as a universal figure that applies to Taiwan. | S1 Introduction: "In adults, approximately one in two women and one in five men will sustain one or more fragility fractures… in their lifetime []." The next sentence begins "In the UK, the prevalence…". S4 introduction verbatim. S3 "Hip fractures" verbatim. S17 quote verbatim, found in the **Discussion** (the evidence file says Introduction; trivial). | 「男性也會。英國指引估計，在英國約每5位男性就有1位一生中會因輕微外力骨折；男性常沒被檢查和治療，骨折後的結果往往也比女性差。」 |
| OP-M3 | Minor | The quotes are verbatim, but the two sentences can read as contradictory. 「單靠鈣片不能降低骨折風險」 follows ESCEO: calcium alone, no effect. 「只補鈣或維生素D，降低骨折的效果很小」 follows RACGP, whose "alone" means without drug treatment: small effect. | S7 "General management / Nutrition": "…(1) calcium and vitamin D supplementation may lead to a modest reduction in fracture risk…; (2) supplementation with calcium alone does not reduce fracture risk". S5 "Calcium, vitamin D and protein supplementation": "In healthy non‐institutionalised individuals, the relative reduction in fracture risk with calcium and/or vitamin D supplementation alone is small and, thus, these should not be considered for routine use in healthy people or as first line treatment for people with osteoporosis." | 「單靠鈣片不能降低骨折風險；鈣和維生素D一起補充，降低骨折的效果也不大。對沒有住在照護機構的健康成人，不建議常規補充；對骨鬆患者，它們也不是第一線治療。」 |
| OP-M4 | OK | — | S1 (Ia) verbatim. S3 "The fear of fracture can be a powerful incentive…" verbatim. S16 "Safety of exercise in people with osteoporosis or fragility fractures" verbatim. S21 abstract conclusion verbatim. | — |
| OP-S1 | OK | — | S1 "Models of care" (Strong) verbatim. S1 VFA recommendation (Strong) verbatim; "BMD-score" has a dropped "T", which is not printed on the page. NOGG defines ≥4 cm height loss as "either in comparison with recalled young adult height or a documented loss on serial measurements". | — |
| OP-S2 | OK | Recognition of the drug class: see OP-6.4. | S1 Rec 12 (Strong) verbatim. S4 GPS 6.6 remark: "Unexplained thigh or groin pain should be evaluated." | Optional: the same class descriptor as OP-6.4. |
| OP-S3 | OK | — | S11 Table 5, WG 11, 1A: "We recommend clinicians should routinely ask about falls in their interactions with older adults". S16 Box 2 "For people with osteoporosis who are already having falls" [C] verbatim. | — |

### 2b. Numbers and populations

| Row | Number on page | Source wording | Status |
|---|---|---|---|
| OP-1.1 | 超過50歲 | RACGP "over the age of 50 years" | ✓ |
| OP-1.3 | 女性65、男性70歲以上 | BHOF "≥ 65 / ≥ 70"; TOA 「65歲以上的婦女或70歲以上男性」 | ✓ |
| OP-1.4 | 50歲以上男性 | BHOF "aged 50–69 years, based on risk profile"; TOA 「50至70歲」 | ✓ |
| OP-2.2 | 1,000 mg (men 50–70); 1,200 mg (women ≥51, men ≥71), total intake | BHOF Synopsis; Canada RDA (51–70) | ✓ for cited sources; differs from TOA 2021 and HPA DRI (Minor) |
| OP-2.3 | 1.5–2 杯、每杯240毫升 | HPA 2014 (low-fat); 2018 guide 1.5–2 cups of any dairy; 2026 draft 1 cup | Outdated qualifier; number under revision (Major) |
| OP-2.4 | 至少800國際單位 | NOGG "at least 800 IU/day" (Strong) | ✓ |
| OP-4.3 | 每次30到60分鐘 | BHOF "a few 30- to 60-min periods each day" | ✓ |
| OP-5.2 | 每週3次以上、至少12週 | WFG "three times or more weekly… for at least 12 weeks" (1A) | ✓ |
| OP-M1 | 約三分之二 | BHOF "Two thirds of vertebral fractures are subclinical" | ✓ |
| OP-M2 | 每5位男性有1位 | NOGG "one in five men" (UK) | ✓ (add 在英國) |
| OP-S1 | 4公分、50歲 | NOGG "≥ 4 cm height loss", "men age ≥ 50 years" | ✓ |
| Alcohol units | none printed (intro points to the common page) | — | ✓ |

---

## 3. Quote verification log

"PMC" = PubMed Central full text retrieved in this session. "Prog." = programmatic exact match after normalisation. "WebFetch" = my independent verbatim read.

| # | Row | S-ID | Quote (first words) | Status | Where verified |
|---|---|---|---|---|---|
| 1 | OP-1.1 | S5 | "All individuals over the age of 50…" | Verified | PMC12088310 Box 1 Rec 1, Grade A |
| 2 | OP-1.2 | S3 | "Clinicians may find it challenging…" | Verified (Prog.) | PMC9546973 "Secondary fracture prevention" |
| 3 | OP-1.2 | S1 | "Start treatment promptly following a fragility fracture…" | Verified (Prog.) | PMC12417299 Summary of main recommendations, item 10 |
| 4 | OP-1.2 | S4 | "We recommend that postmenopausal females and males aged ≥ 50 yr…" | Verified (Prog.) | PMC10610956 Table 3 Rec 3.8 (Strong; high) |
| 5 | OP-1.3 | S3 | "Perform BMD testing in the following: … –Women aged ≥ 65…" | Verified (Prog.) | Synopsis, Diagnostic assessment |
| 6 | OP-1.3 | S26 | 「65歲以上的婦女或70歲以上男性。」 | Verified (WebFetch, verbatim) | TOA 2021 Ch. 3 §2 item (1) |
| 7 | OP-1.4 | S3 | "Perform BMD testing… –Postmenopausal women and men aged 50–69…" | Verified (Prog.) | Synopsis, Diagnostic assessment |
| 8 | OP-1.4 | S26 | 「65歲以前且具有危險因子的停經婦女。…」 | Verified (WebFetch, verbatim) | TOA 2021 Ch. 3 §2 items (2), (4), (5) |
| 9 | OP-2.1 | S1 | "An adequate intake of calcium (minimum 700 mg daily)…" | Verified (Prog.) | Non-pharmacological management: Recommendations (Strong) |
| 10 | OP-2.1 | S4 | "2.1. For people who meet the recommended dietary allowance…" | Verified (Prog.) | Table 2 Rec 2.1 (Conditional) |
| 11 | OP-2.2 | S3 | "Recommend a diet with adequate total calcium intake…" | Verified (Prog.) | Synopsis, Universal recommendations |
| 12 | OP-2.2 | S4 | "Health Canada's recommended dietary allowance for calcium…" | Verified (Prog.) | Table 2 Rec 2.1 remark |
| 13 | OP-2.3 | S29 | 「我國每日飲食指南建議每人每日應攝取1.5-2杯低脂乳品…」 | Verified (WebFetch, verbatim); content superseded by the 2018 guide | MOHW press release 103-01-23 |
| 14 | OP-2.3 | S29 | 「攝取高鈣食物: 包括起司、黑芝麻…」 | Verified (WebFetch; printed with "2." prefix and "(附件2)。" suffix) | same page |
| 15 | OP-2.3 | S3 | "A balanced diet rich in low-fat dairy products…" | Verified (Prog.) | "Adequate intake of calcium" |
| 16 | OP-2.4 | S1 | "To consume vitamin D from foods or be prescribed…" | Verified (Prog.) | Recommendations (Strong) |
| 17 | OP-2.5 | S8 | "For nonpregnant people older than 50 years…" | Verified | PubMed abstract (PMID 38828931) |
| 18 | OP-2.5 | S1 | "Routine intermittent administration of large doses…" | Verified (Prog.) | "Calcium and vitamin D" (Ia) |
| 19 | OP-2.T | S1 | "Protein is an important constituent…" | Verified (Prog.) | "Dietary modification" |
| 20 | OP-3.1 | S1 | "A combination of regular weight-bearing…" | Verified (Prog.) | Recommendations (Strong) |
| 21 | OP-3.1 | S3 | "Weight-bearing exercises (in which bones…" | Verified (Prog.) | "Regular weight-bearing and muscle-strengthening physical activity" |
| 22 | OP-3.2 | S4 | "1.1. We recommend balance and functional training…" | Verified (Prog., 2 segments) | Table 2 Rec 1.1 (Strong; moderate) |
| 23 | OP-3.3 | S4 | "1.2. We suggest progressive resistance training…" | Verified (Prog., 2 segments) | Table 2 Rec 1.2 (Conditional; low) |
| 24 | OP-3.3 | S16 | "All muscle groups should be targeted…" | Verified (Prog.) | PMC9304091 Box 1 [C] |
| 25 | OP-3.4 | S4 | "1.3. We suggest that people who want to participate…" | Verified (Prog.) | Table 2 Rec 1.3 (Conditional; very low) |
| 26 | OP-3.5 | S3 | "To avoid injury, patients should be evaluated…" | Verified (Prog.) | "Regular weight-bearing…" |
| 27 | OP-3.T | S11 | "Benefits of exercise are lost on cessation…" | Verified (Prog.) | PMC9523684 "Exercise and physical activity interventions" |
| 28 | OP-4.1 | S1 | "In people with osteoporosis, repetitive forced spinal…" | Verified (Prog.) | "Exercise to improve or maintain bone density" (Ia) |
| 29 | OP-4.1 | S16 | "Movements or exercise that involve sustained…" | Verified (Prog.) | Box 3 [C] |
| 30 | OP-4.1 | S21 | "Activities that involved spinal flexion…" | Verified | PubMed abstract (PMID 32300705) |
| 31 | OP-4.2 | S16 | "'Think straight'—a straight upper back…" | Verified (Prog., 3 segments) | Box 3 "Safe techniques… [C]" |
| 32 | OP-4.2 | S3 | "– Modification: Bend with knee and hips…" | Verified (Prog., 2 segments) | "Protecting fragile bones in daily life and recreation" |
| 33 | OP-4.3 | S3 | "If bed rest is recommended, a few 30- to 60-min…" | Verified (Prog.) | "Vertebral fracture rehabilitation" |
| 34 | OP-4.3 | S7 | "Immobilised patients when confined to bed…" | Verified (Prog.) | PMC7026233 "General management / Mobility and falls" |
| 35 | OP-4.4 | S1 | "It is recommended that exercise programmes following vertebral fracture…" | Verified (Prog.) | "Management of symptomatic osteoporotic vertebral fractures" (Strong) |
| 36 | OP-4.4 | S1 | "Physiotherapist supervised exercise…" | Verified (Prog.) | same section (Ib) |
| 37 | OP-4.4 | S16 | "Daily exercises to strengthen back muscles…" | Verified (Prog.) | Box 3, vertebral fracture [C] |
| 38 | OP-4.5 | S16 | "Impact exercise on most days at a level up to brisk walking…" | Verified (Prog.); population verified in abstract | Box 1 [C]; abstract |
| 39 | OP-4.5 | S1 | "People at risk of falls, or with vertebral fractures…" | Verified (Prog.) | "Exercise to improve…" (narrative) |
| 40 | OP-4.T | S1 | "When a patient is in pain…" | Verified (Prog.) | vertebral fracture recommendations (Conditional) |
| 41 | OP-4.T | S1 | "In the presence of pain…" | Verified (Prog.) | narrative (Ia) |
| 42 | OP-5.1 | S1 | "A falls assessment should be undertaken…" | Verified (Prog.) | Recommendations (Strong) |
| 43 | OP-5.2 | S11 | "We recommend exercise programmes for fall prevention…" | Verified (Prog.) | Table 5 WG 4 (1A) |
| 44 | OP-5.3 | S11 | "We recommend modifications of an older adult's physical home environment…" | Verified (Prog.) | Table 5 WG 10 (1B) |
| 45 | OP-5.3 | S7 | "Modifiable factors such as correcting decreased visual acuity…" | Verified (Prog.) | "Mobility and falls" |
| 46 | OP-5.3 | S3 | "In community-dwelling patients, refer for at-home fall hazard…" | Verified (Prog.) | Synopsis, Universal recommendations |
| 47 | OP-5.3 | S1 | "Home safety interventions (best delivered by an occupational therapist)…" | Verified (Prog.) | "Falls interventions" (Ia) |
| 48 | OP-5.4 | S11 | "We recommend that medication review and appropriate deprescribing…" | Verified (Prog.) | Table 5 WG 2 (1B) |
| 49 | OP-5.4 | S3 | "Identify and address modifiable risk factors…" | Verified (Prog.) | Synopsis |
| 50 | OP-5.4 | S7 | "reducing consumption of medication that alters alertness…" | Verified (Prog.) | "Mobility and falls" |
| 51 | OP-5.5 | S11 | "Evidence from randomised controlled trials… cataract surgery…" | Verified (Prog.) | "Vision interventions" |
| 52 | OP-5.5 | S11 | "it is recommended that optometrists counsel…" | Verified (Prog.) | "Vision interventions" |
| 53 | OP-5.T | S11 | "Pendent or wrist alarms…" | Verified (Prog.) | "Exercise and physical activity interventions" |
| 54 | OP-6.1 | S1 | "Remember long-term treatment is often required…" | Verified (Prog.) | Summary item 16 |
| 55 | OP-6.1 | S3 | "All antifracture therapeutics treat but do not cure…" | Verified (Prog., 2 segments) | Abstract |
| 56 | OP-6.1 | S3 | "However, in a person with a history of osteoporosis…" | Verified (Prog.) | "Duration of treatment" |
| 57 | OP-6.2 | S3 | "Therapeutic benefits can be maintained only with treatment." | Verified (Prog.) | "Duration of treatment" |
| 58 | OP-6.2 | S1 | "Patients recommended drug treatment for osteoporosis…" | Verified (Prog.) | "Models of care" (Strong) |
| 59 | OP-6.3 | S1 | "Before starting denosumab, ensure…" | Verified (Prog.) | Pharmacological treatment Rec 7 (Strong) |
| 60 | OP-6.3 | S1 | "Avoid unplanned cessation of denosumab…" | Verified (Prog.) | Rec 8 (Strong) |
| 61 | OP-6.3 | S4 | "It is important to communicate the need for commitment…" | Verified (Prog.) | Table 4 Rec 4.5 remark (Conditional) |
| 62 | OP-6.3 | S5 | "Denosumab therapy should not be interrupted." | Verified | Box 1 Rec 26, Grade C |
| 63 | OP-6.4 | S1 | "During bisphosphonate or denosumab therapy, encourage all patients…" | Verified (Prog.) | "Rare adverse effects…" Rec 9 (Strong) |
| 64 | OP-6.4 | S18 | "To reduce the risk of MRONJ, patients should be informed…" | Verified (Prog.) | PMC13069298 §3.5.2 |
| 65 | OP-6.5 | S18 | "Nonsurgical procedures, such as dental cleaning…" | Verified (Prog.); context is starting therapy | §3.5.2 |
| 66 | OP-6.5 | S1 | "During bisphosphonate or denosumab treatment, although ideally…" | Verified (Prog.) | Rec 11 (Conditional) |
| 67 | OP-6.T | S1 | "Offer calcium and/or vitamin D supplementation as an adjunct…" | Verified (Prog.) | Rec 16 (Strong) |
| 68 | OP-6.T | S4 | "For people initiating pharmacotherapy…" | Verified (Prog.) | Table 2 GPS 2.4 |
| 69 | OP-M1 | S5 | "Deterioration of skeletal tissue proceeds with no symptoms…" | Verified | Introduction, paragraph 1 |
| 70 | OP-M1 | S3 | "Two thirds of vertebral fractures are subclinical…" | Verified (Prog.) | "Vertebral fracture rehabilitation" |
| 71 | OP-M1 | S3 | "Vertebral fractures, whether clinically apparent or silent…" | Verified (Prog.) | "Vertebral fractures" |
| 72 | OP-M1 | S1 | "Moderate or severe vertebral fractures, even when asymptomatic…" | Verified (Prog.) | "Vertebral fracture assessment" (Ia) |
| 73 | OP-M2 | S1 | "In adults, approximately one in two women and one in five men…" | Verified (Prog.) | Introduction |
| 74 | OP-M2 | S4 | "Although osteoporosis is often considered a disease of older females…" | Verified (Prog.) | Introduction |
| 75 | OP-M2 | S3 | "Hip fractures are associated with 8.4–36% excess mortality…" | Verified (Prog.) | "Hip fractures" |
| 76 | OP-M2 | S17 | "Historically, osteoporosis was considered primarily a woman's disease…" | Verified | PMC12209010 Discussion |
| 77 | OP-M3 | S7 | "Overall, it can be concluded that (1)…" | Verified (Prog.) | "General management / Nutrition" |
| 78 | OP-M3 | S5 | "In healthy non‐institutionalised individuals…" | Verified | "Calcium, vitamin D and protein supplementation" |
| 79 | OP-M4 | S1 | "in general, people with osteoporosis can safely participate…" | Verified (Prog.) | "Exercise to improve…" (Ia) |
| 80 | OP-M4 | S3 | "The fear of fracture can be a powerful incentive…" | Verified (Prog.) | "Protecting fragile bones…" |
| 81 | OP-M4 | S16 | "Exercise is therefore unlikely to cause a fracture…" | Verified (Prog.) | "Safety of exercise in people with osteoporosis or fragility fractures" |
| 82 | OP-M4 | S21 | "Patients with osteoporosis/osteopenia can safely participate…" | Verified | PubMed abstract (conclusion) |
| 83 | OP-S1 | S1 | "Primary care clinicians should always have in mind…" | Verified (Prog.) | "Models of care" (Strong) |
| 84 | OP-S1 | S1 | "Vertebral fracture assessment (VFA) is indicated…" | Verified (Prog.) | Recommendations (Strong) |
| 85 | OP-S2 | S1 | "During bisphosphonate or denosumab therapy, advise patients to report…" | Verified (Prog.) | Rec 12 (Strong) |
| 86 | OP-S2 | S4 | "Unexplained thigh or groin pain should be evaluated." | Verified (Prog.) | Table 7 GPS 6.6 remark |
| 87 | OP-S3 | S11 | "We recommend clinicians should routinely ask about falls…" | Verified (Prog.) | Table 5 WG 11 (1A) |
| 88 | OP-S3 | S16 | "People who fall repeatedly or have started to avoid activity…" | Verified (Prog.) | Box 2 [C] |
| — | OP-6.2 | EDITORIAL | 「不要自行停藥」 | Not a quote. Checked for neutrality: Minor (see OP-6.2) | — |

Additional source text I verified while checking support and safety (not quote cells):
- NOGG: denosumab "once every 6 months"; Rec 15 (AFF → discontinue, Conditional); the vitamin D loading dose before zoledronate; Summary "Assess falls risk in patients with osteoporosis and/or fragility fractures".
- BHOF: "There is no evidence that calcium intakes in excess of recommended amounts confer additional bone benefit."
- RACGP: Rec 45; "delaying the injection by more than four months"; "six‐monthly intervals".
- AFOS: denosumab extraction timing "3–4 months after the last injection"; "may proceed concurrently in patients already receiving antiresorptive agents".
- SSS: Box 3 Pilates "roll down"/"curl up"; the abstract's brisk-walking population.
- WFG: new spectacles "would benefit".
- TOA 2021: 「Denosumab 每半年」 and 「口服雙磷酸鹽」 (single WebFetch read each).

---

## 4. Citation check results

Checked with mcp__PubMed__get_article_metadata.

| S-ID | Page citation | PubMed | Result |
|---|---|---|---|
| S1 | Gregson CL. Arch Osteoporos 2025;20(1):119. PMID 40921943; DOI 10.1007/s11657-025-01588-3 | Same (published 2025-09-08) | ✓ |
| S3 | LeBoff MS. Osteoporos Int 2022;33(10):2049-2102. PMID 35478046; DOI 10.1007/s00198-021-05900-y | Same | ✓ |
| S4 | Morin SN. CMAJ 2023;195(39):E1333-E1348. PMID 37816527; DOI 10.1503/cmaj.221647 | Same | ✓ |
| S5 | Wong P. Med J Aust 2025;222(9):472-480. PMID 40134107; DOI 10.5694/mja2.52637 | Same | ✓ |
| S7 | Kanis JA. Osteoporos Int 2019;30(1):3-44. PMID 30324412; DOI 10.1007/s00198-018-4704-5 | Same (epub 2018-10-15). Correction PMID 32072205 (Osteoporos Int 2020;31(4):801) concerns open-access status only | ✓ |
| S8 | Demay MB. J Clin Endocrinol Metab 2024;109(8):1907-1947. PMID 38828931; DOI 10.1210/clinem/dgae290 | Same | ✓ |
| S11 | Montero-Odasso M. Age Ageing 2022;51(9):afac205. PMID 36178003; DOI 10.1093/ageing/afac205 | Same (article number; no page range) | ✓ |
| S16 | Brooke-Wavell K. Br J Sports Med 2022;56(15):837-846. PMID 35577538; DOI 10.1136/bjsports-2021-104634 | Same | ✓ |
| S17 | Huang CF. Osteoporos Int 2025;36(7):1105-1114. PMID 40464984; DOI 10.1007/s00198-025-07559-1 | Same | ✓ |
| S18 | Taguchi A. Osteoporos Sarcopenia 2026;12(1):1-17. PMID 41969602; DOI 10.1016/j.afos.2026.02.001 | Same (PubMed type "Review"; title says consensus statement) | ✓ |
| S21 | Kunutsor SK. J Frailty Sarcopenia Falls 2018;3(4):155-178. PMID 32300705; DOI 10.22540/JFSF-03-155 | Same | ✓ |
| S26 | 中華民國骨質疏鬆症學會. 2021 台灣成人骨質疏鬆症防治之共識及指引. 黃兆山 主編. 2021年10月. ISBN 978-986-88615-6-5; URL cghdpt.cgmh.org.tw/…603d060e….pdf | Not indexed. Cover and copyright page (WebFetch): title, society, 主編 黃兆山, 「中華民國 110 年 10 月版」, ISBN 978-986-88615-6-5 (平裝); URL resolves | ✓ (possibly superseded by TOA 2025, unreadable) |
| S29 | 衛生福利部（國民健康署）「聰明補鈣，堅固骨本」…新聞稿, 2014-01-23; URL mohw.gov.tw/cp-16-22557-1.html | Not indexed. Title and 建檔日期 103-01-23 confirmed; URL resolves | ✓ as a citation, but **superseded for the dairy statement** by MOHW 2018-03-13 (cp-16-40152-1), and a 2026 draft revision is pending (see OP-2.3) |

No citation errors were found.

---

## Re-check after fixes (2026-10-11)

**Scope.** The 22 changed or new rows listed by the coordinator: OP-1.2, OP-1.3, OP-1.4, OP-2.2, OP-2.3, OP-2.4, OP-2.5, OP-3.3, OP-3.4, OP-3.T, OP-4.3, OP-4.5, OP-5.1, OP-5.3, OP-5.5, OP-6.2, OP-6.3, OP-6.4, OP-6.5, OP-M2, OP-M3, OP-S2. I checked them against the original sources with the same standards as before. No content or evidence file was edited.

**Method**
- A programmatic diff of review_osteoporosis.v1.md against the updated review_osteoporosis.md shows that exactly these 22 rows changed. No other row's text, label or quote changed, and no rows were added or removed.
- The JSON is identical to the updated table (41/41 rows: text, labels and quotes; the intro also matches). Card 6's summary is now 「骨鬆常需長期治療，停藥前先和醫師討論，也要照顧牙齒。」, which is consistent with OP-6.2 and OP-6.3.
- The changed rows contain 64 evidence quotes plus 2 EDITORIAL entries. Every quote was re-checked against the original source, not against my first report:
  - 52 matched programmatically against the PMC full text.
  - The remaining 12 were checked by WebFetch, PubMed abstract or a reading of the PMC text (details below).
- All 10 VERIFY entries (8 distinct fragments) were checked in the originals:

| Row(s) | VERIFY quote (first words) | Result | Where verified |
|---|---|---|---|
| OP-2.2 | "There is no evidence that calcium intakes in excess of recommended amounts…" | Verbatim | S3 PMC, "Adequate intake of calcium" |
| OP-2.3 | 「不再強調乳品需選用低脂或脫脂為佳的說法，將「低脂乳品類」名稱改成「乳品類」 … 全脂與低脂乳品好處相同，建議每日攝取1.5-2杯乳品類，增進鈣質攝取，保持骨質健康。」 | Verbatim; brackets on the page are 「」 as quoted | V1, my third WebFetch read today. Page title 「國健署公布107年最新版「每日飲食指南」  提倡均衡飲食更健康」, 建檔日期 107-03-13. On the page the first fragment is followed by 「：過去低脂乳品被認為…」; the colon was trimmed, which is acceptable. Fragment 1 now has two reads and fragment 2 has three. |
| OP-2.5 | "Treat vitamin D deficiency and insufficiency prior to initiation of parenteral…" … "treated with vitamin D (e.g., 100,000 to 300,000 IU orally as a loading dose in divided doses) before zoledronate treatment is initiated" | Verbatim, 2 segments | S1 PMC. Segment 1: Rec 17 in the pharmacological recommendations list. Segment 2: bisphosphonate narrative, whose full sentence begins "Pre-existing hypocalcaemia must be investigated and, where due to vitamin D deficiency, treated with vitamin D…". The location "Rec 17 and narrative" is correct. It is used only as context for an editorial clause. |
| OP-4.5 | "People with vertebral fracture or multiple low trauma fractures should usually exercise only up to…" | Verbatim | S16 abstract |
| OP-5.1 | "Assess falls risk in patients with osteoporosis and/or fragility fractures" | Verbatim | S1 PMC, Summary of main recommendations |
| OP-6.3, OP-6.4, OP-S2 | "Denosumab is given as a subcutaneous injection of … once every 6 months." | Verbatim; the cut text is "60 mg" (dose correctly not printed) | S1 PMC, "Anti-resorptive drugs: denosumab" |
| OP-6.3 | 「Denosumab 每半年」 | Verbatim; now **two** independent reads agree | TOA 2021 表四「骨質疏鬆症之藥物及其臨床實證」, 「使用頻率」 column: 「Denosumab 每半年」. The same table has 「Zoledronate 每年」 and 「Teriparatide 每天」. TOA also writes 「denosumab皮下注射」 in its COVID-19 vaccine section. The strength field still says "a single WebFetch read" and can be updated (optional). |
| OP-6.5 | "Clinical judgment of the treating physician should guide the management plan…" | Verbatim | S1 PMC, Rec 11 (Conditional), later part |
| OP-6.5 | "Invasive dental procedures in patients on denosumab should be performed just before the next six‐monthly injection" | Verbatim | S5 PMC, Box 1 Rec 45 (Grade C) |
| OP-6.5 | "should ideally be performed 3–4 months after the last injection" | Verbatim | S18 PMC, §3.5.2 |

- The other quotes newly added to the changed rows come from the evidence file. All are verbatim:
  - OP-3.3: C44/S1 (Ia narrative) and C45/S21 (abstract).
  - OP-4.5: C37/S16, "Moderate impact exercise is recommended on most days… (eg, stamping, jogging, low-level jumping, hopping)…", Box 1 [C]. It is used only for the examples, as its strength field correctly says.
  - OP-6.4: C81/S4 "oral cavity lesions should be evaluated by a dentist.", Table 7 GPS 6.6 remark.
- All other quotes in these rows are unchanged and were verified in the first check.

### Specific checks requested

- **2018 dairy wording and V1.**
  - OP-2.3 now matches V1 (2018) exactly: 「乳品」 without 「低脂」, 1.5–2 cups.
  - The cup size (240 毫升) correctly still rests on S29 (2014: 「每杯240 c.c.」). The label 「國健署 2018／2014」 is accurate.
  - **Citation error, Minor; it came from my own first report.** I gave the V1 title in shortened form, and the writers copied it. The page title is 「國健署公布107年最新版「每日飲食指南」 提倡均衡飲食更健康」; the source entry has 『每日飲食指南』 and lacks the subtitle.
  - **Still open:** whether the draft 9th edition (dairy 1 cup a day) has been finalised. On 2026-10-11 I searched again and found no report of finalisation. The latest coverage is still SETN and CNA, 2026-04-01: 「會在這1至2個月內邀集專家召開會議，新版指引今年就會上線」. The pre-publication check in the reviewer notes must stay.
- **Denosumab descriptor 「每半年打一次的骨鬆皮下注射針劑」.**
  - Supported by NOGG ("subcutaneous injection … once every 6 months"), TOA 2021 (「Denosumab 每半年」, two reads; 「denosumab皮下注射」) and RACGP ("specified six‐monthly intervals").
  - It fits no other osteoporosis drug named in the sources. NOGG: "Zoledronate 5 mg once yearly by intravenous infusion"; IV ibandronate "every 3 months"; "Teriparatide and abaloparatide are injected once daily; romosozumab is injected once monthly". Denosumab biosimilars are denosumab.
  - No dose is printed. The INN is kept in OP-6.3 and OP-S2, which is good for recognition.
  - The stop-or-delay wording is still exactly as strong as NOGG Recs 7–8, with no new safety concern.
- **EDITORIAL wording.** Both phrases are neutral and harmless.
  - OP-6.2: 「請盡快和醫師討論，不要因為擔心就自行停藥；出現嚴重不適時，請立即就醫」. It no longer forbids stopping when severe symptoms need care, and it still discourages fear-driven stopping, which is the aim of NOGG Rec 7.
  - OP-2.5: 「醫師開立的治療劑量，請依醫囑」. It does not clash with the preceding advice: NOGG says "Routine" intermittent dosing is not advised, and NOGG itself treats deficiency, including a loading dose.
- **Numbers and populations.** No number changed except that OP-2.2 adds a no-extra-benefit clause, which matches BHOF. OP-M2 「在英國」 is confirmed:
  - NOGG reference [7] is van Staa TP et al., "Epidemiology of fractures in England and Wales", Bone 2001;29(6):517-22 (PMID 11728921). Source: Springer article page, citation tooltip.
  - Its abstract: "The lifetime risk of any fracture was 53.2% at age 50 years among women, and 20.7% at the same age among men."
  - The underlying figure is therefore "any fracture, from age 50" in England and Wales. NOGG's own sentence says "fragility fractures" and "In adults". The page follows NOGG's wording and attributes it to the guideline (「英國指引估計」), which is acceptable; no change is needed.
- **Safety.** No changed row creates a new risk. OP-3.3 now warns about sit-ups. OP-4.5 explains impact exercise. OP-6.5 asks patients to let the doctor and dentist plan extractions together. OP-5.5 no longer reads as "go out without glasses".

### Findings for the changed rows

| ID | Verdict | Check | Exact fix (if any) |
|---|---|---|---|
| OP-1.2 | OK | Strength field only ("ungraded list"), which is accurate | — |
| OP-1.3 | OK | Strength field only; "two reads agree" is accurate | — |
| OP-1.4 | OK | Same as OP-1.3 | — |
| OP-2.2 | Minor | The new clause 「超過建議量，未證實對骨骼有額外好處」 is faithful to BHOF. But 「（含補充品）」 is less clear than the earlier 「（食物加補充品合計）」: a reader could take the figure as a supplement amount rather than a total, and over-supplement. | Replace 「每天的鈣（含補充品）：」 with 「每天的鈣（食物加補充品）：」 (the row becomes 70 characters). |
| OP-2.3 | Minor | The text is correct per V1 (2018). The V1 citation title is truncated (my error, copied by the writers). The 9th-edition status is still unconfirmed. | Source V1 citation: 「衛生福利部（國民健康署）. 國健署公布107年最新版「每日飲食指南」 提倡均衡飲食更健康. 新聞稿, 2018-03-13.」 (also in JSON `sources`). Before publication: if the 9th edition has been finalised, replace the row text with 「多選含鈣食物，例如乳品（每杯240毫升）、起司、傳統豆腐、深綠色蔬菜、小魚干、黑芝麻等。」 or with its new figure, and cite it. |
| OP-2.4 | OK | 「和醫師討論後」 reflects NOGG "be prescribed"; Strong label correct | — |
| OP-2.5 | OK | 「例行性地」 renders "Routine"; 「久久吃一次大劑量」 renders "intermittent administration of large doses"; EDITORIAL neutral | — |
| OP-3.3 | OK | The caution matches NOGG (Ia) and Kunutsor; label 「加拿大骨鬆指引 2023・建議；NOGG 2024・指引說明」 correct | — |
| OP-3.4 | OK | 「必要時調整動作」 renders "or modified for safety" | — |
| OP-3.T | OK | 「預防跌倒等好處」 matches the WFG falls-programme context | — |
| OP-4.3 | OK | 「醫師建議臥床時」 renders "If bed rest is recommended" | — |
| OP-4.5 | OK | 「一般」 renders "usually" (abstract). 「慢跑、跳躍」 come from the SSS moderate-impact list. The population is confirmed. | — |
| OP-5.1 | OK | "and/or" quote added; 「或」 correct | — |
| OP-5.3 | OK | 「最好請職能治療師等受過訓練的人員」 is supported by NOGG ("best delivered by an occupational therapist") and WFG ("trained clinician"); label correct. Optional: the writers said no verbatim WFG sentence existed for 「跌倒風險較高的人」. There is one, in S11 "Environmental interventions": "The greatest reductions are seen when the intervention is delivered to those at highest risk of falling [,,,,]." | Optional only |
| OP-5.5 | OK | 「改戴非多焦點、看得清楚的眼鏡」 matches "achieving optimal safe functional vision… avoiding the wearing of multifocal glasses when outside". 「走路要小心」 is the purpose of the WFG counselling. | — |
| OP-6.2 | OK | EDITORIAL neutral and harmless (see above) | — |
| OP-6.3 | OK | Descriptor verified; wording as strong as NOGG Recs 7–8 | Optional: update the S26 VERIFY strength field to "two independent WebFetch reads agree (表四, 使用頻率)" |
| OP-6.4 | OK | 「或牙醫師」 matches Canada GPS 6.6; label 「良好實務建議」 correct. Optional: the writers said the IV form lacked a verbatim quote. NOGG Rec 2 (Strong) has one: "Offer oral bisphosphonates (alendronate or risedronate) or intravenous zoledronate as the most cost-effective interventions." Adding a class descriptor would exceed 70 characters unless the row is shortened. | Optional only |
| OP-6.5 | OK | NOGG Rec 11, RACGP Rec 45 and AFOS §3.5.2 verified; no timing printed, correctly, because the sources disagree | — |
| OP-M2 | OK | 「在英國」 confirmed (van Staa 2001, England and Wales) | — |
| OP-M3 | OK | 「單靠鈣片不能降低骨折風險」 matches ESCEO (2). 「鈣加維生素D，降低骨折的效果也有限」 matches ESCEO (1) "may lead to a modest reduction". 「不是第一線治療」 matches RACGP. The contradiction is resolved. | — |
| OP-S2 | OK | Same descriptor as OP-6.3, with the INN kept; matches NOGG Rec 12 | — |

### Updated counts

- **Changed rows (22):** 20 OK, 2 Minor (OP-2.2, OP-2.3), 0 Major, 0 Critical.
- **Whole page (41):** 39 OK, 2 Minor, 0 Major, 0 Critical. The 19 unchanged rows were all OK in the first check.
- **Quotes in changed rows:** 64 of 64 verified against the originals, including all 10 VERIFY entries. No mismatches; none inaccessible.
- **Still not accessible:** TOA 2025 (robots.txt). The 9th-edition 每日飲食指南 status is unconfirmed (open pre-publication check for OP-2.3).
