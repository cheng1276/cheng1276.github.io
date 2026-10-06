# Independent fact-check: common_gout (共通照護 CM-… and 痛風 GT-…)

Checked 2026-10-06 against the original publications (ground truth), following /home/claude/content/VERIFY.md. Files checked: /home/claude/content/review_common.md (36 rows) and /home/claude/content/review_gout.md (29 rows). The evidence files (/home/claude/research/common.md, /home/claude/research/gout.md) were treated as unverified notes. No content or evidence file was edited.

How the originals were read:
- PubMed metadata for every PMID; PubMed abstracts (ECTS 2024, EULAR 2019 vaccination, Parodis 2024, Gwinnutt 2022, Bull 2020, Taiwan 2018, Neogi 2014).
- PMC full text (get_full_text_article): Bull 2020 WHO summary (PMC7719906), ACR 2022 vaccination (PMC10291822), ACR 2020 gout (PMC10563586), Neogi 2014 (PMC3991555).
- WebFetch of original documents: NCBI Bookshelf NBK566048 (WHO 2020 guideline, 6 reads); ACR-hosted vaccination manuscript and summary PDFs; ACR-hosted GIOP 2022 manuscript PDF (2 reads); ACR 2020 gout co-published PDF (Deep Blue art41247.pdf, 4 reads); ard.bmj.com EULAR 2016 gout article (4 reads) and its PDF (2 reads); ard.bmj.com EULAR 2019 vaccination article (2 reads); Sheffield Hallam repository VoR PDF of Parodis 2024 (3 reads); Oviedo repository PDF of EULAR 2021 lifestyle (2 reads); JYX repository PDF of EULAR 2025 PA; Keele repository BSR 2017 manuscript (2 reads) and executive summary (1 read); NICE NG219 recommendations page (2 reads); Malaysian CPG PDF; WHO UV Q&A page; ICNIRP-hosted WHO 2002 UV guide PDF (2 reads); CWA UV page.
- Glued-word pitfalls were checked: ACR vaccination live-vaccine statement (PMC drops "deferring") and ACR gout vitamin C statement (PMC drops "against"). Both directions were confirmed from intact text in a second document.
- Not accessible: EULAR 2019 vaccination Tables 1–2 (grades and agreement). ard.bmj.com returned HTTP 429 for the PDF and table pages, and the article HTML does not contain the tables. One WebFetch read claimed "SoR B" for recommendations 1–2, but a second read reported the table absent, so that value is treated as unverified (possibly invented by the summariser).

---

## 1. Summary counts

| Verdict | Common (36 rows) | Gout (29 rows) | Total (65) |
|---|---|---|---|
| Critical | 0 | 0 | 0 |
| Major | 0 | 1 | 1 |
| Minor | 10 | 2 | 12 |
| OK | 26 | 26 | 52 |

Quotes: 95 unique quote entries (49 common, 46 gout; a quote reused in several rows is counted once).
- 94 verified against the original wording (same meaning). Of these, 25 were confirmed entirely in PMC full text or PubMed abstracts, 7 by PMC/PubMed plus WebFetch, and 62 by WebFetch of the publisher, repository or agency document. Each WebFetch-only quote matched the evidence file's earlier independent read, and every grade, number and direction was re-read or matched against a second document.
- 1 partly verified (C24/S2: S2 text statement and certainty read; the table-row wording itself was not read).
- 0 quote-wording mismatches. 0 quotes entirely inaccessible.
- Strength-metadata problems found in the evidence files (not shown on the site): S17 LoA is 9.2, not 9.6; EULAR 2016 principle B LoA is 8.4±1.1 (the file says "not found"); EULAR 2016 Rec 1 is graded "A, D" (the file says "not found").

Major item:
- GT-1.T: 「24小時內喝超過1到2份酒…高40%」. The study category ">1–2" means more than 1 and up to 2 drinks. The Chinese reads as "more than 2", which implies 2 drinks carry no risk. Also, 40% is ACR's rounding: the cited study (Neogi 2014, ACR ref. 97) gives OR 1.36 (95% CI 1.00–1.88).

No Critical items. Every other direction, number, population and strength checked as asked (WHO amounts and 65+; ACR GIOP calcium, vitamin D and lifestyle; ACR vaccine ages, "taking immunosuppressive medication" and live-vaccine deferral; EULAR 2019 wording; WHO and CWA UV bands; ACR 2020 gout directions and strengths; BSR 2017 Recs I, II, IX, X, XI; EULAR 2016 principle B; NICE NG219 1.2.1, 1.3.5, 1.4.1, 1.4.2) matched the originals.

---

## 2. Findings table (every row)

### 2a. 共通照護 (review_common.md)

| ID | Verdict | Problem | What I checked (source, location, verbatim text seen) | Suggested fix |
|---|---|---|---|---|
| CM-1.1 | OK | — | S5 NBK566048 adults (WebFetch): "Adults should do at least 150–300 minutes of moderate-intensity aerobic physical activity; or at least 75–150 minutes of vigorous-intensity aerobic physical activity; or an equivalent combination … throughout the week, for substantial health benefits." Label "Strong recommendation, moderate certainty evidence". S4 abstract (PubMed) "150-300 min … 75-150 min … per week". S5 chronic-conditions version is identical, strong/moderate; the conditions are cancer survivors, hypertension, type 2 diabetes and HIV (indirect for RMDs). S1 Table 1 OP3 "World Health Organisation recommendations for a healthy lifestyle are also applicable to people with RMDs", LoE 5, GoR D, LoA 9.3 (1.3). | Optional: 「或相當的兩者組合」 for "equivalent combination". |
| CM-1.2 | OK | — | S5: "Adults should also do muscle-strengthening activities at moderate or greater intensity that involve all major muscle groups on 2 or more days a week…", strong/moderate. S4 (PMC): "…on 2 or more days a week, a strong recommendation supported by moderate-certainty evidence." | — |
| CM-1.3 | Minor | (a) 「多樣化的活動」 renders "varied" but drops "multicomponent". WHO means activity that combines aerobic, muscle-strengthening and balance training. (b) It drops "As part of their weekly physical activity", so readers may add these 3 days on top of the 150–300 minutes. The age (65+), at least 3 days, moderate or greater intensity, the aims (function, falls) and the strength (strong, moderate certainty) are all correct. | S5 older adults: "As part of their weekly physical activity, older adults should do varied multicomponent physical activity that emphasizes functional balance and strength training at moderate or greater intensity, on 3 or more days a week, to enhance functional capacity and to prevent falls." Label "Strong recommendation, moderate certainty evidence". S4 (PMC): "…now applies to all older adults rather than specifically those with poor mobility"; "High-certainty evidence demonstrates that balance and functional exercises reduce the rate of falls"; S4 definition: multicomponent activities "combine all types of exercise (aerobic, muscle strengthening and balance training) into a session". | 「65歲以上：做為每週活動量的一部分，每週至少3天做結合平衡和肌力訓練的多元活動，強度中等以上，以增進身體功能、預防跌倒。」 |
| CM-1.4 | OK | — | S5 adults: "Adults should limit the amount of time spent being sedentary. Replacing sedentary time with physical activity of any intensity (including light intensity) provides health benefits.", strong/moderate. Chronic conditions: same wording, "Strong recommendation, low certainty evidence". | — |
| CM-1.5 | Minor | The statement and grade are correct. But 「…等疾病」 can be read as including 乾燥症 and 蕁麻疹, which are on this six-disease page. EULAR 2021 covered only 7 RMDs (OA, RA, axSpA, PsA, SLE, SSc, gout). EULAR 2025 OAP 3 covers only IA (RA, SpA) and OA. | S1 Table 1 Exercise 5 (Oviedo PDF): "People with RMDs should be advised that exercise is safe and that it is never too late to start exercising", LoE 1a, GoR A, LoA 9.9 (0.3) (100%). S1 abstract (PubMed) lists the seven RMDs. S2 OAP 3 (JYX PDF) verbatim, LoA 9.6 (0.7); IA = "rheumatoid arthritis [RA] and spondyloarthritis [SpA]". | 「運動是安全的，任何時候開始都不嫌晚。這項歐洲建議涵蓋痛風、類風濕性關節炎、中軸型脊椎關節炎、紅斑性狼瘡等，未包括乾燥症和蕁麻疹。」 |
| CM-1.T | OK | — | S5 adults, heading "GOOD PRACTICE STATEMENTS": "Doing some physical activity is better than doing none. If adults are not meeting these recommendations, doing some physical activity will benefit their health. Adults should start by doing small amounts of physical activity, and gradually increase the frequency, intensity and duration over time." S4 (PMC) verbatim as quoted. The label 良好實務建議 is correct. | — |
| CM-2.1 | OK | — | S1 Table 1 Smoking 1 verbatim; LoE 2a, GoR B, LoA 9.9 (0.2) (100%). | — |
| CM-2.2 | OK | — | Same item: "…smoking is detrimental to symptoms, function, disease activity, disease progression and occurrence of comorbidities in all RMDs". | — |
| CM-2.3 | OK | — | S1 body text (Oviedo PDF): "These people should be offered support to quit and progress towards quitting should be monitored by health professionals." Abstract (PubMed): "Smokers should be supported to quit." 指引說明 is correct (body text, not a table item). | — |
| CM-3.1 | OK | — | S1 Diet 1 verbatim; LoE 5, GoR D, LoA 9.5 (1.0) (100%). | — |
| CM-3.2 | OK | — | S1 Diet 2 verbatim; LoE 1a, GoR A, LoA 9.7 (0.8) (100%). | — |
| CM-3.3 | OK | — | S1 Weight 1 "People with RMDs should aim for a healthy weight"; LoE 5, GoR D, LoA 9.7 (0.7). | Optional: 「以達到並維持健康體重為目標」 ("aim for" includes reaching it). |
| CM-3.4 | OK | — | S1 Weight 2 verbatim; LoE 2a, GoR B, LoA 9.5 (1.6) (94.7%). The overweight/obese restriction is kept. | — |
| CM-3.5 | OK | — | S1 Alcohol 1 verbatim; LoE 5, GoR D, LoA 9.5 (1.0). | — |
| CM-3.T | OK | — | S1 Alcohol 3 (RA; LoE 2a, GoR B, LoA 9.1 (1.6) (89.5%)) and Alcohol 4 (gout; LoE 2a, GoR B, LoA 9.6 (0.7) (100%)) verbatim. Abstract: "people with rheumatoid arthritis and gout may be at risk of flares after moderate alcohol consumption". | — |
| CM-4.1 | Minor | Missing population restriction. ACR covers chronic glucocorticoid use "at a dose of ≥2.5 mg/day for >3 months" (systemic, prednisone-equivalent). 「使用類固醇」 gives no route, so it can be read as including steroid creams or inhalers, and the dose floor is dropped. The direction, the conditional strength (建議) and the certainty are correct. | ACR-hosted GIOP manuscript (WebFetch ×2): "…beginning or continuing chronic GC at a dose of ≥2.5 mg/day for >3 months, we conditionally recommended optimizing age appropriate dietary and supplemental calcium and vitamin D, in addition to lifestyle modifications". Table 2 row "…we conditionally recommend optimizing dietary and supplemental calcium and vitamin D in addition to lifestyle modifications", certainty "Low or very low". PubMed abstract: "receiving >3 months treatment with glucocorticoids (GCs) ≥2.5 mg daily". | 「開始或持續口服類固醇超過3個月的成人，建議從飲食和補充品補足鈣和維生素D，並調整生活習慣。」 The physician should decide whether to state the ≥2.5 mg/day threshold (the brief bars doses). |
| CM-4.2 | OK | — | Manuscript: "Dietary and supplemented elemental calcium intake of up to 1,000 to 1,200 mg daily is recommended for adults". The numbers, "elemental" and diet-plus-supplement total are correct. 「飲食加補充品合計…攝取到」 adequately renders "up to". | — |
| CM-4.3 | OK | — | Manuscript: "Serum vitamin D levels should be monitored, and vitamin D supplemented to maintain serum vitamin D 25(OH)D levels ≥30 to 50 ng/mL; 600 to 800 IU daily or more is typically required." | Optional: add 「補充劑量請和醫師討論」. |
| CM-4.4 | OK | — | Manuscript: "Lifestyle modifications include smoking cessation, limiting alcohol to ≤2 servings a day, eating a balanced diet, maintaining weight in the recommended range, and performing regular weight-bearing or resistance training exercises." | — |
| CM-4.5 | Minor | The ≤2 servings per day figure is correct, and the EDITORIAL phrase 「這是上限，不是鼓勵喝酒」 is neutral and helpful. But 「份」 is undefined, so a reader could count a whole bottle of beer or a glass of spirits as one 份. ACR does not define "serving" in the quoted sentence. | Same C57 sentence as CM-4.4. | Define the serving from a source the physician chooses (e.g. 「1份約等於…」), or say 「標準份量」. Keep the EDITORIAL phrase. |
| CM-4.T | Minor | Same route ambiguity as CM-4.1: ECTS addresses oral glucocorticoids. The strength is not stated in accessible text; 建議 is acceptable because the quote says "recommended". | PubMed abstract 39556468: "General measures are recommended for all patients who are being prescribed GCs for ≥3 months, ie, calcium and protein intake should be normalized, a 25(OH) vitamin D concentration of 50-125 nmol/L should be attained, and the risk of falls be minimized." Scope: "patients likely to receive oral GCs for ≥3 months". | 「口服類固醇3個月以上的人，也要盡量降低跌倒的風險。」 |
| CM-5.1 | OK | — | ard.bmj.com (WebFetch): OP E "Non-live vaccines can be administered to patients with AIIRD during the use of glucocorticoids and DMARDs"; OP D "Vaccines should be preferably administered prior to planned immunosuppression, in particular B cell depleting therapy". Abstract (PubMed): "Non-live vaccines can be safely provided to AIIRD patients regardless of underlying therapy". 「自體免疫風濕病」 matches AIIRD. The 基本原則 label is correct. | — |
| CM-5.2 | OK | — | Direction confirmed three ways. (1) ACR manuscript PDF: "For patients with RMD who are taking immunosuppressive medication, deferring live attenuated vaccines is conditionally recommended." (2) ACR summary PDF: "deferring live-attenuated vaccines is conditionally recommended". (3) PMC10291822: the statement is glued ("medication,live attenuated vaccines is conditionally recommended"), but the intact Discussion reads "the Voting Panel conditionally recommended against administering live attenuated virus vaccines to patients receiving those agents as well as other forms of immunosuppression". Table 7 certainty "Very low". EULAR OP F: "Live-attenuated vaccines may be considered with caution in patients with AIIRD". | — |
| CM-5.3 | OK | The wording is correct; the grade could not be verified. | Rec 1 "Influenza vaccination should be strongly considered for the majority of patients with AIIRD" and Rec 2 (pneumococcal, same wording), from ard.bmj.com and the PubMed abstract. Table 2 (SoR) was not accessible (see header). 建議 is acceptable per the brief because the quote says "should". | If Table 2 is obtained and shows a grade, change the label to 「EULAR 2019・建議強度 X」. |
| CM-5.4 | Minor | The text is faithful to the ACR statement, but a reader aged 65 or over may conclude the vaccine is not for them. ACR limits the statement to under-65s only because general advice already covers people 65 and over; its own highlights say the vaccine is for all RMD patients on immunosuppression. | PMC10291822: "For patients with RMD age <65 years who are taking immunosuppressive medication, pneumococcal vaccination is strongly recommended." Introduction highlight: "1) pneumococcal vaccination should be administered to all RMD patients taking immunosuppressive medication". Manuscript Table 7 certainty "Low". | 「正在使用免疫抑制藥物的風濕病患者，即使未滿65歲，也強烈建議接種肺炎鏈球菌疫苗。」 |
| CM-5.5 | OK | — | PMC: "For patients with RMD age >18 years who are taking immunosuppressive medication, administering the recombinant VZV vaccine is strongly recommended." Table 7 "Very low (indirect evidence only)"; the summary PDF matches. The source caveat (mild flares in some patients in one retrospective study; common reactogenicity) is not on the site, which is acceptable. | — |
| CM-5.T | OK | — | OP A "The vaccination status and indications for further vaccination in patients with AIIRD should be assessed yearly by the rheumatology team"; OP B verbatim; abstract sentence verbatim (PubMed). ACR guiding principle 4 (PMC): "shared decision-making with patients is a key component of any vaccination strategy". | — |
| CM-6.1 | OK | — | who.int UV Q&A (WebFetch): "The UVI is a measure of the level of UV radiation. The values of the index range from zero upward - the higher the UVI, the greater the potential for damage to the skin and eye, and the less time it takes for harm to occur." | — |
| CM-6.2 | OK | — | cwa.gov.tw OBS_UVI (WebFetch): "0-2 低量級" "3-5 中量級" "6-7 高量級" "8-10 過量級" "11+ 危險級"; "紫外線指數分級係依據WHO相關規範。" This matches the evidence-file read, and CNA uses the same names. WHO 2002 Table 1 (ICNIRP PDF): LOW "< 2", MODERATE "3 TO 5", HIGH "6 TO 7", VERY HIGH "8 TO 10", EXTREME "11+" (consistent). | — |
| CM-6.3 | Minor | The content is correct, but 「穿上衣服」 reads as "put clothes on", which is trivially true. WHO means cover the skin ("Slip on a shirt"; basic message "Wear protective clothing"). | ICNIRP PDF: "Above the threshold value of 3, protection is necessary, and this message should be reinforced at UVI values of 8 and above." Figure, UVI 3–7: "Seek shade during midday hours! Slip on a shirt, slop on sunscreen and slap on a hat!" The WHO Q&A "3 to 7" row matches. | 「指數3到7需要防護：中午時段找陰涼處，穿上能遮住皮膚的衣物、擦防曬乳、戴帽子。」 |
| CM-6.4 | Minor | Same wording point (「衣服…都不能少」). The content is correct. | ICNIRP PDF and WHO Q&A, UVI 8+: "Avoid being outside during midday hours! Make sure you seek shade! Shirt, sunscreen and hat are a must!" | 「指數8以上要加強防護：中午時段避免待在戶外，務必找陰涼處，遮住皮膚的衣物、防曬乳、帽子都不能少。」 |
| CM-6.5 | Minor | Strength label. The recommendation has a printed grade (SoR C), so the mapping requires 建議強度 C. The evidence file's LoA (9.6) is also wrong: the printed value is 9.2. | Sheffield Hallam VoR PDF, Table 1, raw row (3 consistent WebFetch reads): "In people with SLE, photoprotection should be advised for the prevention of flares (LoE: 4). 4 C 9.2 1.0 7–10". Abstract (PubMed): "Photoprotection and psychosocial interventions are important for SLE patients". | Change the label to 「EULAR 2024・建議強度 C」. |
| CM-6.T | OK | — | ICNIRP PDF: "Taking certain medications as well as using perfumes and deodorants can sensitize your skin, causing serious burns in the sun." Next sentence: "Ask your pharmacist for advice." | — |
| CM-M1 | OK | — | S4 (PMC), "What is new?": "the previous stipulation that physical activity should be accumulated in at least 10 min bouts has been removed. … physical activity of any bout duration is associated with improved health outcomes, including all-cause mortality." | — |
| CM-M2 | OK | — | ICNIRP PDF: "Sunscreen should never be used to prolong the duration of sun exposure."; "Applying sunscreen is not a means to prolong your stay in the sun but to reduce the health risk of your exposure." | — |
| CM-S1 | Minor | Strength label. This sentence is narrative text in the BJSM summary paper (S4), not a WHO good practice statement, so the mapping gives 指引說明. The content is correct. | S4 (PMC), narrative paragraph after "Pre-exercise medical clearance is generally unnecessary.": "Those who develop new symptoms when increasing their levels of activity should consult a healthcare provider." Not found among the S5 good practice statements (WebFetch of NBK566048 returned "NOT FOUND"). | Change the label to 「WHO 2020・指引說明」. |

### 2b. 痛風 (review_gout.md)

| ID | Verdict | Problem | What I checked (source, location, verbatim text seen) | Suggested fix |
|---|---|---|---|---|
| GT-1.1 | OK | — | PMC10563586, lifestyle statements: "Limiting alcohol intake is conditionally recommended for patients with gout, regardless of disease activity." S2 Table 7 (Deep Blue PDF): "For patients with gout, regardless of disease activity, we conditionally recommend limiting alcohol intake.", certainty Low. Malaysian CPG Rec 5: "limit intake of all types of alcohol (beer, wine and liquor)". Neogi abstract (PubMed): "Consuming wine, beer, or liquor was each associated with an increased risk of gout attack." | — |
| GT-1.2 | OK | — | S6 Table 1 Alcohol 4 verbatim (Oviedo PDF); LoE 2a, GoR B, LoA 9.6 (0.7) (100%). | — |
| GT-1.3 | OK | — | EULAR 2016 principle B (ard.bmj.com): "…avoidance of alcohol (especially beer and spirits) and sugar-sweetened drinks, heavy meals and excessive intake of meat and seafood." The principle has no grade (table: "NA"; LoA 8.4±1.1). BSR Rec IX: "sugar sweetened soft drinks containing fructose should be avoided". | — |
| GT-1.4 | Minor | The content and strength (conditional, very low certainty) are correct. But Taiwanese ingredient labels usually say 「高果糖糖漿」, so patients may not recognise 「高果糖玉米糖漿」. ACR also notes there were no data in people who already have gout (acceptable to omit). | PMC: "Limiting high-fructose corn syrup intake is conditionally recommended for patients with gout, regardless of disease activity."; "However, there were no data focused on patients with existing gout." S2 Table 7 wording, certainty Very low. Malaysian CPG: "limit intake of high-fructose corn syrup". | 「限制高果糖玉米糖漿（食品標示常寫「高果糖糖漿」）的攝取。」 This is a terminology note, not from the sources; the physician should confirm. |
| GT-1.5 | OK | — | ard.bmj.com, discussion of principle B: "Importantly, other modifiable risk factors have been identified since 2006, specifically sugar-sweetened drinks, foods rich in fructose and orange or apple juice." Two of three reads were verbatim; one read garbled the opening word. | — |
| GT-1.T | Major | (1) The threshold is misread. ">1–2" is the study category "more than 1 and up to 2 drinks" (Neogi's categories: none, >0–1, >1–2, >2–4 …). 「喝超過1到2份」 reads in Chinese as "more than 1–2 drinks", i.e. 3 or more, which implies 2 drinks carry no risk. That is the opposite of the finding, on alcohol, a safety topic. (2) "40%" is ACR's rounding. The cited study (ACR ref. 97 = Neogi 2014) reported OR 1.36 (95% CI 1.00–1.88), i.e. 36% higher; up to 1 drink was not significant (OR 1.13). | PMC10563586, verbatim: "In a case-crossover study, consuming >1–2 alcoholic beverage servings in the prior 24 hours was associated with a 40% higher risk of gout flare than periods without alcohol consumption, with a dose-response relationship". Deep Blue S2 shows the same sentence with "[97]"; ref 97 is "Neogi T, Chen C, Niu J, Chaisson C, Hunter DJ, Zhang Y. Alcohol quantity and type on risk of recurrent gout attacks… Am J Med 2014;127:311–8." Neogi full text (PMC3991555): "seven categories: no alcohol consumption, >0–1 drink, >1–2, >2–4, >4–6, >6–8, and more than 8 drinks"; "While having up to one drink in a 24-hour period did not increase the risk of attack significantly (OR=1.13, 95% CI 0.80–1.58), consuming >1–2 drinks in a 24-hour period was associated with 36% higher risk of recurrent attack (OR=1.36, 95% CI 1.00–1.88)". Serving: "a 12-ounce bottle or can of beer; a 5-ounce glass of wine; and 1 to 1.5 ounces of liquor". | 「研究發現，24小時內喝了1份多到2份酒，發作風險就比沒喝酒時高約4成，而且喝越多風險越高。」 Consider adding the study's serving size: 1份約為355毫升啤酒、150毫升葡萄酒或30–45毫升烈酒. |
| GT-2.1 | OK | — | PMC: "Limiting purine intake is conditionally recommended for patients with gout, regardless of disease activity." S2 certainty Low. BSR Rec IX: "excessive intake of alcoholic drinks and high purine foods should be avoided". | — |
| GT-2.2 | OK | — | EULAR 2016 principle B verbatim. S6 body text (Oviedo PDF): "…the 2016 EULAR guidelines on the management of gout recommend people with gout to avoid sugar-sweetened drinks, heavy meals and excessive intake of meat and seafood as well as encouraging low-fat dairy products—this TF supports these recommendations." | — |
| GT-2.3 | OK | — | BSR Rec IX (Keele manuscript and executive summary): "…a well-balanced diet low in fat and added sugars, and high in vegetables and fibre should be encouraged"; LoE I (vitamin C and skimmed milk), III (others); SOR 92%. NICE 1.4.1: "Advise them to follow a healthy, balanced diet." | — |
| GT-2.4 | OK | — | BSR Rec IX: "…inclusion of skimmed milk and/or low fat yoghurt, soy beans and vegetable sources of protein and cherries, in the diet should be encouraged." EULAR principle B: "Low-fat dairy products should be encouraged." 黃豆 is a correct rendering of "soy beans". | — |
| GT-2.5 | OK | — | PMC: "Dietary modifications likely yield only small changes in SU concentration, but dietary factors may serve as triggers for flares". | — |
| GT-3.1 | OK | — | NICE 1.4.2 (WebFetch ×2): "Advise people with gout that excess body weight or obesity, or excessive alcohol consumption, may exacerbate gout flares and symptoms." | — |
| GT-3.2 | OK | — | PMC: "Using a weight loss program (no specific program endorsed) is conditionally recommended for those patients with gout who are overweight/obese, regardless of disease activity." S2 certainty Very low. The overweight/obese restriction is kept. | — |
| GT-3.3 | OK | — | BSR Rec IX, first sentence: "In overweight patients, dietary modification to achieve a gradual reduction in body weight and subsequent maintenance should be encouraged." | — |
| GT-3.4 | OK | — | EULAR principle B: "Regular exercise should be advised." Rest during attacks is covered by GT-4.2. | — |
| GT-3.T | OK | — | PMC: "…a decrease in BMI of >5% was associated with 40% lower odds of recurrent flare compared with those without weight change (–3.5% ≤ BMI ≤ 3.5%)". It is correctly framed as observational (研究顯示/指引說明). | — |
| GT-4.1 | OK | — | PMC: "Using topical ice as an adjuvant treatment over no adjuvant treatment is conditionally recommended for patients experiencing a gout flare." S2 Table 6 wording, certainty Low. NICE 1.3.5: "…applying ice packs to the affected joint (cold therapy) in addition to taking prescribed medicine may help alleviate pain." | — |
| GT-4.2 | OK | — | BSR Rec II, verbatim in both files: "Affected joints should be rested, elevated and exposed in a cool environment. Bed-cages and ice-packs can be effective adjuncts to management." LoE Ib (ice-packs), IV (other); SOR 89% (range 54-100). | — |
| GT-4.3 | Minor | Strength label. EULAR Rec 1 has printed grades, so plain 建議 understates them: category of evidence "1b*, 4", grade "A, D". The asterisk covers the evidence for giving colchicine early; the self-medication part rests on category 4 (grade D). | ard.bmj.com Rec 1: "Acute flares of gout should be treated as early as possible. Fully informed patients should be educated to self-medicate at the first warning symptoms." ARD PDF table (2 WebFetch reads, consistent): "1b*, 4" ; "A, D" ; "8.4±1.1". Footnote: "*For the evidence that colchicine should be given as early as possible, within 12 hours of symptom onset." BSR Rec I: LoE IV, SOR 90%. | Change the label to 「EULAR 2016・建議強度 A、D」, or keep 建議 with a reviewer note. |
| GT-4.4 | OK | — | BSR Rec I, verbatim in both files: "…ensure that patients are aware of the importance of continuing any established urate-lowering therapy during an attack." LoE IV, SOR 90% (range 81-100). Malaysian algorithm: "Do not stop ULT during attack". The direction (continue) is correct. | — |
| GT-4.T | OK | — | PMC, both sentences verbatim: the Patient Panel's preference for an at-home "medication-in-pocket" strategy, and "the Voting Panel advocated a 'medication-in-pocket' strategy for gout flare management". | — |
| GT-5.1 | OK | — | PubMed abstract 29363262 verbatim: "…clearly associated with a variety of comorbidities, including cardiovascular diseases, chronic kidney disease, urolithiasis, metabolic syndrome, diabetes mellitus, thyroid dysfunction, and psoriasis." | — |
| GT-5.2 | OK | — | BSR Rec XI verbatim; LoE III, SOR 90%. EULAR principle C verbatim (ard.bmj.com). | — |
| GT-5.3 | OK | The restriction to people with past stones is kept. The EDITORIAL phrase 「喝水量請和醫師確認」 is neutral and needed for fluid-restricted patients. Note: this has the lowest agreement of the BSR items used (SOR 57%) but carries the same 建議 label as items near 90%. | BSR Rec X, verbatim in both files: "Patients with gout and a history of urolithiasis should be encouraged to drink >2litres of water daily and avoid dehydration." LoE IV; SOR 57% (range 17-100). SOR is "graded anonymously on a 0 – 100 mm Visual Analogue Scale". | Optional reviewer note on the low SOR. |
| GT-5.T | OK | — | ard.bmj.com: "…this overarching principle was mainly based on expert opinion. However, given the high prevalence of cardiovascular comorbidities in patients with gout, lifestyle modifications should also be implemented as part of cardiovascular prevention." | — |
| GT-M1 | OK | — | PMC: "The Voting Panel aimed to provide guidance without implying any 'patient-blaming' for the manifestations of gout given its strong genetic determinants." NICE 1.2.1 bullet verbatim (genetics, excess body weight or obesity, medicines, CKD or hypertension). | — |
| GT-M2 | OK | — | EULAR 2016 principle B verbatim. S6 Table 1 OP1: "Lifestyle improvements complement medical treatment and do not replace it" (LoE 5, GoR D, LoA 9.4 (1.2)). | — |
| GT-M3 | OK | — | Direction confirmed two ways. (1) S2 PDF text: "Adding vitamin C supplementation is conditionally recommended against for patients with gout, regardless of disease activity."; Table 7: "we conditionally recommend against adding vitamin C supplementation", certainty Low. (2) The S1 PMC statement is glued ("recommendedfor"), but its unglued paragraph reads "data on vitamin C were insufficient to support continued recommendation for its use in patients with gout. Two small RCTs (n = 29 and n = 40) showed clinically insignificant changes in SU concentrations…". | — |
| GT-M4 | OK | — | PMC: "The certainty of evidence drawn mainly from observational studies was low or very low, precluding specific recommendations on these topics." ard.bmj.com: "In contrast, according to epidemiological studies, consumption of coffee, and cherries is negatively associated with gout, and eating cherries may reduce the frequency of acute gout flares." | Optional: 「證據確定性低或非常低」. |

---

## 3. Quote verification log

Status key: Verified = found in the original with the same meaning. PMC = PMC full text; Abs = PubMed abstract; WF = WebFetch of the named original document.

### 3a. Common (S-IDs as in review_common.md)

| S-ID / C-ID | Quote (first words) | Status | Where verified |
|---|---|---|---|
| S5 / C14 | "Adults should do at least 150–300 minutes…" | Verified (with label) | WF NBK566048, adults |
| S4 / C14 | "All adults should undertake 150-300 min…" | Verified | Abs 33239350 |
| S5 / C19 | "Adults and older adults with these chronic conditions should do at least 150–300…" | Verified (with label) | WF NBK566048 |
| S1 / C03 | "World Health Organisation recommendations for a healthy lifestyle…" | Verified (LoE 5, GoR D, LoA 9.3) | WF Oviedo PDF, Table 1 |
| S5 / C15 | "Adults should also do muscle-strengthening activities…" | Verified (with label) | WF NBK566048 |
| S4 / C15 | "additional health benefits will occur through participation in muscle-strengthening…" | Verified | PMC7719906 |
| S5 / C17 | "As part of their weekly physical activity, older adults should do varied multicomponent…" | Verified (with label) | WF NBK566048 |
| S4 / C17 | "the recommendation regarding multicomponent physical activity…all older adults" | Verified | PMC7719906, "What is new?" |
| S4 / C60 | "High-certainty evidence demonstrates that balance and functional exercises…" | Verified | PMC7719906 |
| S5 / C32 | "Adults should limit the amount of time spent being sedentary…" | Verified (strong, moderate) | WF NBK566048 |
| S5 / C33 | "Adults and older adults with chronic conditions should limit…" | Verified (strong, low) | WF NBK566048 |
| S1 / C11 | "People with RMDs should be advised that exercise is safe…" | Verified (1a, A, 9.9) | WF Oviedo PDF, Table 1 |
| S2 / C25 | "General PA recommendations including the 4 domains…" | Verified (LoA 9.6 (0.7)) | WF JYX PDF, Table 1 |
| S4 / C21 | "For all populations, doing some physical activity is better than doing none…" | Verified | PMC7719906 |
| S5 / C21 | "Doing some physical activity is better than doing none." | Verified (under "GOOD PRACTICE STATEMENTS") | WF NBK566048 |
| S1 / C37 | "People with RMDs should be encouraged to stop smoking…" | Verified (2a, B, 9.9) | WF Oviedo PDF, Table 1 |
| S1 / C38 | "These people should be offered support to quit… Smokers should be supported to quit." | Verified | WF Oviedo PDF body; Abs 35260387 |
| S1 / C44 | "A healthy, balanced diet is integral…" | Verified (5, D, 9.5) | WF Oviedo PDF |
| S1 / C46 | "People with RMDs should be informed that consuming specific food types…" | Verified (1a, A, 9.7) | WF Oviedo PDF |
| S1 / C47 | "People with RMDs should aim for a healthy weight" | Verified (5, D, 9.7) | WF Oviedo PDF |
| S1 / C48 | "People with RMDs who are overweight or obese should work with health professionals…" | Verified (2a, B, 9.5) | WF Oviedo PDF |
| S1 / C50 | "The alcohol consumption of people with RMDs should be discussed…" | Verified (5, D, 9.5) | WF Oviedo PDF |
| S1 / C52 | "People with rheumatoid arthritis and health professionals should be aware…" | Verified (2a, B, 9.1) | WF Oviedo PDF; Abs consistent |
| S1 / C53 | "People with gout and health professionals should be aware…" | Verified (2a, B, 9.6) | WF Oviedo PDF; Abs consistent |
| S6 / C54 | "For adults and children beginning or continuing chronic GC at a dose of ≥2.5 mg/day…" | Verified; Table 2 certainty "Low or very low" | WF ACR-hosted GIOP manuscript ×2 (one read began "For all adults and children"; immaterial) |
| S6 / C55 | "Dietary and supplemented elemental calcium intake of up to 1,000 to 1,200 mg daily…" | Verified | WF GIOP manuscript |
| S6 / C56 | "Serum vitamin D levels should be monitored… 600 to 800 IU daily or more is typically required." | Verified | WF GIOP manuscript ×2 |
| S6 / C57 | "Lifestyle modifications include smoking cessation, limiting alcohol to ≤2 servings a day…" | Verified | WF GIOP manuscript |
| S8 / C59 | "General measures are recommended for all patients who are being prescribed GCs for ≥3 months…" | Verified | Abs 39556468 |
| S9 / C66 | "Non-live vaccines can be administered to patients with AIIRD during the use of glucocorticoids and DMARDs" | Verified | WF ard.bmj.com OP E; Abs consistent |
| S9 / C65 | "Vaccines should be preferably administered prior to planned immunosuppression…" | Verified | WF ard.bmj.com OP D; Abs consistent |
| S10 / C77 | "…deferring live attenuated vaccines is conditionally recommended. … conditionally recommended against administering…" | Verified (direction confirmed three ways; Table 7 "Very low") | WF ACR manuscript and summary PDFs; PMC10291822 Discussion (statement glued in PMC) |
| S9 / C67 | "Live-attenuated vaccines may be considered with caution in patients with AIIRD" | Verified | WF ard.bmj.com OP F; Abs |
| S9 / C68 | "Influenza vaccination should be strongly considered… Pneumococcal vaccination should be strongly considered…" | Verified (wording); grade not accessible | WF ard.bmj.com; Abs |
| S10 / C74 | "For patients with RMD age <65 years who are taking immunosuppressive medication, pneumococcal…" | Verified (strong; Table 7 "Low") | PMC10291822; WF manuscript and summary |
| S10 / C75 | "For patients with RMD age >18 years… recombinant VZV vaccine is strongly recommended." | Verified (strong; Table 7 "Very low (indirect evidence only)") | PMC10291822; WF manuscript and summary |
| S9 / C62 | "The vaccination status and indications for further vaccination… assessed yearly… The former address…" | Verified | WF ard.bmj.com OP A; Abs (second sentence) |
| S9 / C63 | "The individualised vaccination programme should be explained…" | Verified | WF ard.bmj.com OP B |
| S10 / C71 | "4) shared decision-making with patients is a key component…" | Verified | PMC10291822, Methods |
| S12 / C81 | "The UVI is a measure of the level of UV radiation…" | Verified | WF who.int Q&A |
| S13 / C90 | "0-2 低量級" … "11+ 危險級"; "紫外線指數分級係依據WHO相關規範" | Verified | WF cwa.gov.tw OBS_UVI (matches the evidence-file read) |
| S11 / C83 | "PROTECTION REQUIRED (UVI 3-7) … EXTRA PROTECTION (UVI 8+)…" | Verified (the original prints exclamation marks; same meaning) | WF ICNIRP PDF |
| S12 / C83 | "[3 to 7] Seek shade during midday hours!… [8 and above] Avoid being outside…" | Verified | WF who.int Q&A |
| S11 / C84 | "Above the threshold value of 3, protection is necessary…" | Verified | WF ICNIRP PDF |
| S17 / C89 | "In people with SLE, photoprotection should be advised for the prevention of flares (LoE: 4)…" | Verified; SoR C found; LoA in evidence file wrong (printed 9.2, not 9.6) | WF Sheffield Hallam VoR PDF ×3; Abs (second sentence) |
| S11 / C88 | "Taking certain medications as well as using perfumes and deodorants… Ask your pharmacist for advice." | Verified | WF ICNIRP PDF |
| S4 / C23 | "the previous stipulation that physical activity should be accumulated in at least 10 min bouts has been removed…" | Verified | PMC7719906 |
| S11 / C86 | "Sunscreen should never be used to prolong… Applying sunscreen is not a means to prolong…" | Verified | WF ICNIRP PDF |
| S4 / C22 | "Those who develop new symptoms when increasing their levels of activity should consult a healthcare provider." | Verified (narrative text, not a good practice statement) | PMC7719906 |

### 3b. Gout (S-IDs as in review_gout.md)

| S-ID / C-ID | Quote (first words) | Status | Where verified |
|---|---|---|---|
| S1 / C13 | "Limiting alcohol intake is conditionally recommended…" | Verified | PMC10563586 |
| S2 / C13 | "For patients with gout, regardless of disease activity, we conditionally recommend limiting alcohol intake." | Verified (certainty Low) | WF Deep Blue art41247.pdf, Table 7 |
| S12 / C21 | "…limit intake of all types of alcohol (beer, wine and liquor)" | Verified (no grade printed) | WF Malaysian CPG PDF, Rec 5 |
| S32 / C22 | "…Consuming wine, beer, or liquor was each associated with an increased risk of gout attack." | Verified (n=724) | Abs 24440541; PMC3991555 |
| S6 / C19 | "People with gout and health professionals should be aware that moderate alcohol consumption…" | Verified (2a, B, 9.6) | WF Oviedo PDF, Table 1 |
| S3 / C44 | "…avoidance of alcohol (especially beer and spirits) and sugar-sweetened drinks…" | Verified | WF ard.bmj.com principle B |
| S4 / C45 | "sugar sweetened soft drinks containing fructose should be avoided" | Verified | WF Keele manuscript, Rec IX |
| S1 / C42 | "Limiting high-fructose corn syrup intake is conditionally recommended… no data focused on patients with existing gout." | Verified | PMC10563586 |
| S2 / C42 | "…we conditionally recommend limiting high- fructose corn syrup." | Verified (certainty Very low) | WF Deep Blue, Table 7 |
| S12 / C30 | "…limit intake of high-fructose corn syrup" | Verified | WF Malaysian CPG PDF |
| S3 / C44 (text) | "Importantly, other modifiable risk factors have been identified since 2006…orange or apple juice." | Verified (2 of 3 reads verbatim) | WF ard.bmj.com |
| S1 / C14 | "In a case-crossover study, consuming >1–2 alcoholic beverage servings…40% higher risk…" | Verified (ACR ref 97 = Neogi 2014, whose estimate is OR 1.36) | PMC10563586; WF Deep Blue reference list; PMC3991555 |
| S1 / C24 | "Limiting purine intake is conditionally recommended…" | Verified | PMC10563586 |
| S2 / C24 | "For patients with gout, regardless of disease activity, we conditionally recommend limiting purine intake." | Partly verified (S2 text statement and certainty Low read; table-row wording not read) | WF Deep Blue |
| S4 / C28 | "excessive intake of alcoholic drinks and high purine foods should be avoided" | Verified | WF Keele manuscript, Rec IX |
| S3 / C16 | "Every person with gout should receive advice regarding lifestyle…" | Verified (principle; grade NA; LoA 8.4±1.1) | WF ard.bmj.com and ARD PDF |
| S6 / C12 | "However, the 2016 EULAR guidelines on the management of gout recommend…" | Verified | WF Oviedo PDF body |
| S4 / C33 | "Diet and exercise should be discussed with all patients with gout, and a well-balanced diet…" | Verified (LoE I/III; SOR 92%) | WF Keele manuscript |
| S5 / C08 | "…Advise them to follow a healthy, balanced diet." | Verified | WF NICE NG219 1.4.1 |
| S4 / C50 | "inclusion of skimmed milk and/or low fat yoghurt, soy beans and vegetable sources of protein…" | Verified | WF Keele manuscript |
| S3 / C49 | "Low-fat dairy products should be encouraged." | Verified | WF ard.bmj.com |
| S1 / C05 | "Dietary modifications likely yield only small changes in SU concentration…" | Verified | PMC10563586 |
| S5 / C72 | "Advise people with gout that excess body weight or obesity…" | Verified | WF NICE 1.4.2 |
| S1 / C67 | "Using a weight loss program (no specific program endorsed)…" | Verified (S2 certainty Very low) | PMC10563586; WF Deep Blue |
| S4 / C71 | "In overweight patients, dietary modification to achieve a gradual reduction…" | Verified (LoE III; SOR 92%) | WF Keele manuscript |
| S3 / C77 | "Regular exercise should be advised." | Verified | WF ard.bmj.com |
| S1 / C68 | "An increase in BMI of >5% was associated with 60% higher odds…" | Verified | PMC10563586 |
| S1 / C87 | "Using topical ice as an adjuvant treatment over no adjuvant treatment…" | Verified | PMC10563586 |
| S2 / C87 | "For patients experiencing a gout flare, we conditionally recommend using topical ice…" | Verified (certainty Low) | WF Deep Blue, Table 6 |
| S5 / C89 | "Advise people with gout that applying ice packs to the affected joint…" | Verified | WF NICE 1.3.5 |
| S4 / C88 | "Affected joints should be rested, elevated and exposed in a cool environment…" | Verified (Ib/IV; SOR 89%, range 54-100) | WF Keele manuscript and executive summary |
| S3 / C93 | "Acute flares of gout should be treated as early as possible…" | Verified (grade "1b*, 4 / A, D"; LoA 8.4±1.1) | WF ard.bmj.com; ARD PDF table ×2 |
| S4 / C94 | "Educate patients to understand that attacks should be treated as soon as an attack occurs…" | Verified (IV; SOR 90%, range 81-100) | WF Keele manuscript and executive summary |
| S12 / C95 | "Do not stop ULT during attack" | Verified | WF Malaysian CPG PDF, algorithm |
| S1 / C96 | "…an at-home 'medication-in-pocket' strategy… the Voting Panel advocated…" | Verified | PMC10563586 |
| S8 / C105 | "Moreover, gout or hyperuricemia is clearly associated with a variety of comorbidities…" | Verified | Abs 29363262 |
| S4 / C100 | "Cardiovascular risk factors and co-morbid conditions such as cigarette smoking…" | Verified (III; SOR 90%) | WF Keele manuscript |
| S3 / C99 | "Every person with gout should be systematically screened…" | Verified (principle; grade NA; LoA 8.5±0.9) | WF ard.bmj.com and ARD PDF |
| S4 / C83 | "Patients with gout and a history of urolithiasis should be encouraged to drink >2litres…" | Verified (IV; SOR 57%, range 17-100) | WF Keele manuscript and executive summary |
| S3 / C101 | "However, given the high prevalence of cardiovascular comorbidities in patients with gout…" | Verified | WF ard.bmj.com |
| S1 / C06 | "The Voting Panel aimed to provide guidance without implying any 'patient-blaming'…" | Verified | PMC10563586 |
| S5 / C03 | "any risk factors for gout they have, including genetics, excess body weight or obesity…" | Verified | WF NICE 1.2.1 |
| S6 / C09 | "Lifestyle improvements complement medical treatment and do not replace it" | Verified (5, D, 9.4) | WF Oviedo PDF, Table 1 |
| S2 / C63 | "For patients with gout, regardless of disease activity, we conditionally recommend against adding vitamin C supplementation." | Verified (certainty Low) | WF Deep Blue text and Table 7 |
| S1 / C63 | "The Voting Panel reached consensus that data on vitamin C were insufficient…" | Verified (the S1 statement itself is glued "recommendedfor"; direction taken from S2) | PMC10563586 |
| S1 / C53 | "The Voting Panel reviewed the data for cherries/cherry extract and dairy protein…" | Verified | PMC10563586 |
| S3 / C55 | "In contrast, according to epidemiological studies, consumption of coffee, and cherries…" | Verified | WF ard.bmj.com |

---

## 4. Citation check results (PubMed metadata unless noted)

| Page / S-ID | Citation as listed | Result |
|---|---|---|
| CM S1 = GT S6 | Gwinnutt JM et al. Ann Rheum Dis 2023;82(1):48–56; PMID 35260387; DOI 10.1136/annrheumdis-2021-222020 | Correct (Epub 2022-03-08; vol 82, issue 1, pp 48–56). |
| CM S2 | Rausch Osthoff AK et al. Ann Rheum Dis 2026;85(6):1026–1038; PMID 42036268; DOI 10.1016/j.ard.2026.03.006 | Correct. |
| CM S4 | Bull FC et al. Br J Sports Med 2020;54(24):1451–1462; PMID 33239350; DOI 10.1136/bjsports-2020-102955 | Correct (PMC7719906). |
| CM S5 | WHO guidelines on physical activity and sedentary behaviour, 2020; NBK566048 | Correct (no PMID). |
| CM S6 | Humphrey MB et al. Arthritis Rheumatol 2023;75(12):2088–2102; PMID 37845798; DOI 10.1002/art.42646; co-pub. Arthritis Care Res 2023;75(12):2405–2419; PMID 37884467; DOI 10.1002/acr.25240 | Correct (both). |
| CM S8 | Paccou J et al. Eur J Endocrinol 2024;191(6):G1–G17; PMID 39556468; DOI 10.1093/ejendo/lvae146 | Correct. |
| CM S9 | Furer V et al. Ann Rheum Dis 2020;79(1):39–52; PMID 31413005; DOI 10.1136/annrheumdis-2019-215882 | Correct (Epub 2019-08-14). |
| CM S10 | Bass AR et al. Arthritis Care Res 2023;75(3):449–464; PMID 36597813; DOI 10.1002/acr.25045; co-pub. Arthritis Rheumatol 2023;75(3):333–348; PMID 36597810; DOI 10.1002/art.42386 | Correct (both; PMC10291822 / PMC12320478). |
| CM S11 | WHO/WMO/UNEP/ICNIRP. Global Solar UV Index: A Practical Guide. 2002. ISBN 92-4-159007-6 | Content confirmed in the ICNIRP-hosted PDF; the WHO publication item 9241590076 exists. |
| CM S12 | WHO UV index Q&A page | Content confirmed. The page date (20 June 2022) was not re-checked. |
| CM S13 | CWA 紫外線觀測 page | Content confirmed (accessed 2026-10-06). |
| CM S17 | Parodis I et al. Ann Rheum Dis 2024;83(6):720–729; PMID 37433575; DOI 10.1136/ard-2023-224416 | Correct. |
| GT S1 | FitzGerald JD et al. Arthritis Care Res 2020;72(6):744–760; PMID 32391934; DOI 10.1002/acr.24180 | Correct (PMC10563586). |
| GT S2 | FitzGerald JD et al. Arthritis Rheumatol 2020;72(6):879–895; PMID 32390306; DOI 10.1002/art.41247 | Correct. |
| GT S3 | Richette P et al. Ann Rheum Dis 76(1):29–42 (online 25 Jul 2016); PMID 27457514; DOI 10.1136/annrheumdis-2016-209707 | PMID, DOI and volume/pages correct. Minor: the print year is missing; it is the January 2017 issue (Serval record). Write "Ann Rheum Dis 2017;76(1):29–42". |
| GT S4 | Hui M et al. Rheumatology (Oxford) 2017;56(7):e1–e20; PMID 28549177; DOI 10.1093/rheumatology/kex156; exec. summary 1056–1059 (PMID 28549195); erratum 1246 (PMID 28605531) | Correct (exec. summary DOI kex150; erratum DOI kex250). |
| GT S5 | NICE NG219, Gout: diagnosis and management | Wording confirmed on nice.org.uk. The publication date (9 June 2022) was not re-checked (the overview page returned 403). |
| GT S8 | Yu KH et al. Int J Rheum Dis 2018;21(4):772–787; PMID 29363262; DOI 10.1111/1756-185X.13266 | Correct. |
| GT S12 | MaHTAS, Management of Gout (2nd ed.), CPG 2021; URL "—" | Content confirmed. Minor: add the URL https://mymahtas2.moh.gov.my/files/e-CPG_Management_of_Gout_(Second_Edition)%20(3).pdf |
| GT S32 | Neogi T et al. Am J Med 2014;127(4):311–8; PMID 24440541; DOI 10.1016/j.amjmed.2013.12.019 | Correct (PMC3991555). |

---

## 5. Other notes for the physician

1. Common-page intro (not a table row): 「這頁整理六種疾病都可參考的基本生活照護」. The EULAR lifestyle (2021) and physical-activity (2025) recommendations do not include Sjögren's or chronic urticaria. The WHO amounts apply to all adults, and the GIOP and UV items apply to anyone. The CM-1.5 fix addresses the clearest instance.
2. Evidence-file metadata corrected by this check (the site text is unaffected unless the labels are changed):
   - Parodis 2024 photoprotection: SoR C, LoA 9.2 (SD 1.0).
   - EULAR 2016 gout: principles A–C have no grade ("NA"), with LoA 8.9, 8.4 and 8.5.
   - EULAR 2016 gout Rec 1: grade "A, D".
3. Still unverified: the EULAR 2019 vaccination grades (Table 2) for CM-5.3. If they can be read, apply the mapping (建議強度 X).
4. The live-vaccine (CM-5.2) and vitamin C (GT-M3) directions were each confirmed from intact text in a second document, not from the glued PMC sentences.
