# Verification report: g5b_conditions

**Summary: 17 entries. OK 11, minor 6, major 0.**

- OK: osteoporosis, raynaud, lupus-nephritis, cutaneous-lupus, neonatal-lupus, disease-activity, cvd, ckd, urolithiasis, blepharitis, salivary-gland
- minor: axspa, uveitis, spinal-fusion, comorbidity, mgd, night-sweats
- major: none

## How this was checked (applies to every entry)

- **Quotes.** All 86 evidence quotes were found verbatim, after normalising whitespace, quote marks and dashes. Each was matched against PMC full text from `get_full_text_article` or the PubMed abstract from `get_article_metadata`. For every quote I read the sentences around it. No quote depends on a dropped "not" or "against", or on any other glued word. Every location label is correct, including the TRA 2020 recommendation numbers: Rec 4 is exercise/smoking and Rec 5 is extra-articular manifestations.
- **Citations.** All 37 cited PMIDs resolve. DOI, first author (and the named co-authors), title, journal and volume/pages all match PubMed. Some years differ, but only because PubMed shows the e-pub date while the citations correctly use the print-issue year:
  - TRA: 2019 e-pub, 2020 issue (23(1))
  - ACR/SAA/SPARTAN: 2015 e-pub, 2016 issue (68(2))
  - Ulas: 2023 e-pub, 2024 issue (196(6))
  - Kanis: 2018 e-pub, 2019 issue (30(1))
  - Kuhn: 2016 e-pub, 2017 issue (31(3))
  - Webster: 2016 e-pub, 2017 issue (389(10075))
  - Türk: 2015 e-pub, 2016 issue (69(3))

  BSR 2026 SLE has no page range in PubMed yet (65(6)), and Martin de Frémont 2026 has no volume yet. Both are cited correctly.
- **Site fit.** `occ.py` was re-run against the current site JSON (it includes the uncommitted edits to axspa, gout and urticaria). The output is identical to `occurrences.md`. Every [LINK], [repeat] and [excluded] sentence was read in its card.
- **Length and wording.** Every def is ≤ 60 CJK characters. uveitis is exactly 60, and neonatal-lupus is 59 CJK, or 80 characters counting the Latin antibody names, still under the 90 maximum. Every example is ≤ 40 and every note ≤ 50. No entry uses 你. All wording is Taiwan usage (心肌梗塞, 薦腸關節, 乾癬, 頷下腺 and so on).
- **Lymphoma wording (cross-cutting).** The site deliberately leaves lymphoma unnamed on SJ-S1/SJ-S2: sjogren.json reviewer_notes says "Lymphoma is not named, to keep the tone calm". Neither glossary note names it. However:
  - If the popup lists sources the way the page source list does (`short` + `citation`, template.html line 382), the night-sweats popup will show a leukaemia review title (see night-sweats, problem 1).
  - If the popup also shows evidence quotes, the BSR 2025 quotes in salivary-gland and night-sweats contain the word "lymphoma".

---

## 1. axspa — 中軸型脊椎關節炎 — **minor**

**What I checked**
- Six quotes, all verbatim:
  - BSR 2025 (PMC12107049): two in Background, one in the text under the "Active disease" (1B) recommendation.
  - TRA 2020 (PMC7004149): two in the Introduction.
  - Sieper 2017: abstract.
- The def, clause by clause:
  - 「主要影響脊椎和薦腸關節的慢性發炎性疾病」 is supported. BSR: "a chronic inflammatory condition that predominantly affects the spine and sacroiliac joints". TRA: "a chronic type of arthritis that primarily affects the sacroiliac joints and the spine".
  - 「X 光看得到結構破壞的僵直性脊椎炎」 is supported. TRA: "radiographic axSpA, which is largely synonymous with ankylosing spondylitis (AS) and presents with radiographically visible structural damage". BSR: "includes ankylosing spondylitis (radiographic axSpA)".
- The note is supported by BSR: "It can also involve peripheral joints and entheses, and extra-musculoskeletal manifestations (EMMs) such as acute anterior uveitis, psoriasis and IBD."
  - 其他關節 renders peripheral joints, and 肌腱附著處 renders entheses.
  - 「骨骼肌肉以外的表現」 matches the site's AS-4.2.
- Site fit: CM-1.5 (the list of diseases covered by the EULAR exercise recommendation) is consistent.

**Problem 1 (minor: precision; could worry patients with nr-axSpA).** The def says 「X 光**已**看得到…以及 X 光**還**看不到破壞的非放射線型」. 「還看不到」 implies the damage is only "not yet" visible and will appear later. The sources say something different:
- TRA describes nr-axSpA as a form that "does not exhibit such structural damage".
- BSR says that not everyone progresses.

Proposed def (54 CJK):
> 一種主要影響脊椎和薦腸關節的慢性發炎性疾病；包括 X 光看得到結構破壞的僵直性脊椎炎，以及 X 光看不到這種破壞的非放射線型。

Support:
- PMID 31777200: "non‐radiographic axSpA (nr‐axSpA), a milder form of axSpA that does not exhibit such structural damage"
- PMID 40199504: "Not all people with axSpA will undergo structural progression detectable on radiographs (radiographic progression)"

**Optional (plain language).** 薦腸關節 is unexplained jargon, and the site itself never uses it. A source for a short gloss now exists, verified in PMC: Ulas ST, Diekhoff T, Ziegeler K. Sex Disparities of the Sacroiliac Joint: Focus on Joint Anatomy and Imaging Appearance. *Diagnostics (Basel)* 2023;13(4):642. PMID 36832130, DOI 10.3390/diagnostics13040642, PMC9955570 (Tier 3).
- Quote (Introduction): "The sacroiliac joint (SIJ) is the articulation surface between the sacrum and the ilium and plays an important role in the distribution of axial load between the spine and pelvis"
- Def with the gloss (64 CJK):
  > 一種主要影響脊椎和薦腸關節（脊椎和骨盆之間的關節）的慢性發炎性疾病；包括 X 光看得到結構破壞的僵直性脊椎炎，以及 X 光看不到這種破壞的非放射線型。

**Housekeeping (not shown to patients)**
- reviewer_notes still asks to check the 「骨盆」 gloss, which is no longer in the def.
- evidence[1].supports says "example"; that text is now the note.
- evidence[2].supports says 「note：由風濕科醫師確認診斷」, which the note no longer says.

---

## 2. uveitis — 急性前葡萄膜炎（虹彩炎） — **minor**

**What I checked**
- Eleven quotes, all verbatim:
  - SUN 2021 (PMC8526627): two in the Introduction.
  - Bolletta 2025: abstract.
  - Kopplin 2016 (PMC6733982): three.
  - SUN 2021 SpA/HLA-B27 AU (PMC8594762): Introduction.
  - TRA, Rec 5 text: two.
  - BSR 2025: one.
  - ACR 2015, PICO 27: one.

**The def, clause by clause**
1. 「葡萄膜炎是眼球內部的發炎。」 is supported. SUN 2021: "characterized by intraocular inflammation". Kopplin: "Uveitis, defined as intraocular inflammation".
2. 「前葡萄膜炎是眼睛前段（虹彩等處）的發炎」 is supported. SUN: "anterior uveitis (primary site in the anterior chamber)". Bolletta: "characterized by the inflammation of the iris and ciliary body"; 等 covers the ciliary body.
3. 「虹彩炎就屬於這一類」 is acceptable. It is inferred from item 2 and from ACR 2015's own use of "acute iritis"; no current quote states it outright. A PubMed abstract that does state it exists (Tier 3, 1995) and could optionally be added as evidence: Careless DJ, Inman RD. Acute anterior uveitis: clinical and experimental aspects. *Semin Arthritis Rheum* 1995;24(6):432-41. PMID 7667647, DOI 10.1016/s0049-0172(95)80011-5. Quote: "Acute anterior uveitis (AAU) or iritis is an inflammatory disorder of the anterior structures of the eye that may be associated with a number of disease entities."
4. 「急性型會突然發作，常只有一眼，也可能兩眼輪流復發」 is supported:
   - Kopplin: "symptomatic, unilateral, sudden onset, and limited duration" and "Recurrence can occur in either eye and it is common to see inflammatory episodes ‘flip-flop’ between eyes".
   - SUN SpA: "recurrent acute, unilateral or unilateral alternating".
   - Bolletta (PMC text): "with a tendency to recur in either eye alternately".

   Population caveat: this pattern is described for HLA-B27/SpA-associated AAU. It fits here because the term is linked only on the axSpA page. If the entry is reused elsewhere, prefix 「在脊椎關節炎，」.

**Other fields**
- The example matches Kopplin exactly: "Symptoms frequently include photophobia, ocular pain, eye redness and blurred vision".
- Site fit: AS-4.1 is the [LINK]; AS-4.1, 4.2, 4.3 and 4.4 are [repeat]s. All are consistent. AS-4.1's 「當天就看眼科」 also agrees with BSR's "within 24 hours".

**Problem 1 (minor: understatement in an urgency note).** The note says 「延誤治療**少數人**可能出現…」. TRA says "in some cases". 「少數」 adds a "few" quantifier that softens the urgent message.

Proposed note (30 CJK):
> 屬急症，要盡快看眼科；延誤治療，有些人可能出現青光眼或視力嚴重受損。

Support, PMID 31777200:
- "should be managed as an emergency to avoid complications"
- "glaucoma and severe impairment of vision can occur in some cases if adequate treatment is delayed"

**Optional (Taiwan usage).** Lay readers in Taiwan know the iris as 虹膜; 虹彩 survives mainly in the disease name. Optional def (64 CJK):
> 葡萄膜炎是眼球內部的發炎。前葡萄膜炎是眼睛前段（虹膜等處）的發炎，虹彩炎（虹膜發炎）就屬於這一類；急性型會突然發作，常只有一眼，也可能兩眼輪流復發。

Support: PMID 40182969 "inflammation of the iris and ciliary body"; PMID 7667647 (quote above).

---

## 3. spinal-fusion — 脊椎融合 — **minor**

**What I checked**
- Seven quotes, all verbatim:
  - Ulas 2024 (PMC11111289): three, in the sections "Ankylosis" and "Role of imaging".
  - ACR 2015 (PMC5123844): two.
  - TRA: two.
- The def is supported:
  - 長出新骨頭: "new bone formation".
  - 互相連成一體（骨性融合）: "bony fusion at the attachment sites of the annulus fibrosus (known as “bridging syndesmophytes”) and/or bony fusion of the facet joints".
  - 使脊椎僵硬、活動度大減: "the joint or disc space stiffens" and "associated with extensive loss of motion".
  - 通常出現在較晚期: "Ankylosis usually occurs at an advanced stage".
- Site fit: AS-3.2 is the [LINK]; AS-3.3 and AS-3.4 are [repeat]s. All are consistent. The site's own gloss 「黏在一起」 also fits.

**Problem 1 (minor: example precision).** The example is 「晚期僵直性脊椎炎**常**被稱為「竹節狀脊椎」。」
- 「常」 is not in TRA, which says only "advanced AS (known as “bamboo spine”) patients".
- The sentence equates a disease stage with what Ulas describes as the imaging appearance of the most advanced fusion. Ulas reports that appearance "in up to 15 % of axSpA patients", so readers may wrongly assume every late-stage patient has it.

Proposed example (24 CJK):
> 融合最嚴重時，影像上會呈現特殊的樣子，稱為「竹節狀脊椎」。

Support, PMID 37944938 (PMC, section "Ankylosis"): "Its most advanced form has a characteristic imaging appearance known as “bamboo spine”". "Its" refers to ankylosis.
- In the full sentence, the PMC text runs on as "…“bamboo spine”and has been observed…". That glue sits at a stripped citation marker after the closing quote mark. The truncated quote above contains no glued word.
- A minimal alternative using the TRA wording: 「晚期僵直性脊椎炎也被稱為「竹節狀脊椎」。」 (PMID 31777200).

**Problem 2 (minor: understatement).** The note 「…脊椎**可能**較脆弱」 renders TRA's "often have fragile … spines" as "may". The site's AS-3.1 says 「脊椎常較脆弱」.

Proposed note:
> 僵直性脊椎炎的脊椎常較脆弱，輕微外傷就可能骨折。

Support, PMID 31777200: "AS patients often have fragile and osteoporotic spines that can develop spinal fractures or dislocations from only mild trauma"

**Optional.** To tie the risk to fusion itself (as AS-3.2 and AS-3.3 do), use PMID 26401907 (PMC): "Several case reports of spine fractures, spinal cord injury, and paraplegia following chiropractic spinal manipulation, particularly of the cervical spine in patients with spinal fusion or advanced osteoporosis of the spine, have been reported".

---

## 4. osteoporosis — 骨質疏鬆 — **OK**

- **Quotes.** Four, all verbatim: Kanis 2019 (PMC7026233), two in "Osteoporosis in Europe"; the Taiwan 2022 abstract; BSR 2026 "Bone health".
- **Def.** A faithful rendering of the 1993 consensus definition: "systemic skeletal disease characterised by low bone mass and microarchitectural deterioration of bone tissue, with a consequent increase in bone fragility and susceptibility to fracture".
- **Note.** Faithful: "the diagnosis of the disease relies on the quantitative assessment of bone mineral density … the clinical significance of osteoporosis lies in the fractures that arise".
- **Site fit.** AS-3.2 and SL-5.5 are the [LINK]s; AS-3.4 and AS-3.T are [repeat]s. All are consistent.
- **Problems.** None.

## 5. raynaud — 雷諾氏現象 — **OK**

- **Quotes.** Five, all verbatim (PMC4018202, Introduction).
- **Def.** Supported: microvasculature of the fingers and toes; ischaemia in response to cold; triphasic colour change (pale, then blue, then red); numbness and swelling.
- **Example.** Supported (nose and ears; the source also lists nipples).
- **Note.** Supported. Dropping the hedge "is thought to be" is acceptable.
- **Glued sentence.** The drafters correctly avoided "Attacks may even occur after minorin temperature…", which is confirmed glued in PMC.
- **Site fit.** SL-3.5 (keeping warm) is consistent.
- **Problems.** None.

## 6. lupus-nephritis — 狼瘡腎炎 — **OK**

- **Quotes.** Three, all verbatim: Anders 2020 abstract; EULAR 2025 SLR (PMC) Introduction; BSR 2026, text under recommendation 66.
- **Def.** Faithful. 腎臟發炎 is an acceptable lay simplification of "glomerulonephritis".
- **Site fit.** SL-5.1 is consistent, and so is the urine-test tip SL-5.T.
- **Optional wording.** BSR says "Regular monitoring of urine dipstick at all assessment appointments is essential for detection of nephritis." 「及早」 is not in that quote, and 「有助」 is weaker than "essential". A closer version (19 CJK):
  > 每次回診都要驗尿，這是發現腎炎的必要檢查。

## 7. cutaneous-lupus — 皮膚型狼瘡 — **OK**

- **Quotes.** Five, all verbatim: two guideline abstracts, BSR 2026 PMC ×2, and the Chasset 2015 abstract.
- **Def.** Supported: an inflammatory autoimmune disease with heterogeneous manifestations; it can occur "‘alone’ as an isolated skin condition", or together with SLE.
  - A more direct BSR quote is available for "together with SLE", if preferred: "the need to distinguish evidence and recommendations for the assessment and management of CLE with SLE and CLE only" (PMID 42336388).
- **Example.** Supported by Lu 2021: acute, subacute and chronic forms; discoid LE.
- **Note.** Supported. Chasset: "antimalarials, the mainstay of treatment". Lu 2021 adds "antimalarials are the first-line systemic treatment for all types of CLE".
- **Labels.** 「2021 亞洲…指引」 is a fair label: Lu 2021 was led by the Asian Dermatological Association, the AADV and the Chinese Society of Dermatology.
- **Site fit.** SL-2.3 is consistent.
- **Problems.** None.

## 8. neonatal-lupus — 新生兒狼瘡 — **OK**

- **Quotes.** Six, all verbatim: the French review abstract, BSR 2026 PMC ×4, and the Ambrosi 2014 abstract.
- **Def.** Faithful. It covers transplacental anti-Ro/SSA with or without anti-La/SSB; the skin, blood and liver features; congenital heart block (CHB) as the most severe; and "electric signal conduction" (Ambrosi).
- **Note.** Faithful to BSR: "These complications are short-lived and often resolve spontaneously as the child’s maternal antibodies disappear".
- **Reviewer notes.** Both claims are verified. BSR lists "Areas the guideline does not cover: Neonatal lupus…", and the review's authors are from the French National Referral Centre for Rare Autoimmune and Systemic Diseases.
- **Site fit.** SL-6.5 is consistent.
- **On 「少見」.** The word follows the source ("rare syndrome"). It describes the disease overall, not an exposed baby's risk: among infants of antibody-positive mothers, BSR reports a rash in about 10%, transient cytopenia in 20% and transaminitis in 30%. Acceptable as written.
- **Optional (safety clarity).** The note could be read as saying that all neonatal lupus fades. Proposed note (43 CJK):
  > 皮疹、血球或肝指數異常多為短暫，常隨寶寶體內媽媽的抗體消失而好轉；心臟傳導阻滯則多半無法恢復。

  Support, PMID 42680608: "The most severe manifestation is congenital heart block (CHB), which occurs in structurally normal fetal hearts, is most often complete and irreversible"

## 9. disease-activity — 疾病活動度 — **OK**

**Quotes.** Nine, all verbatim: England 2019 PMC ×2, Anderson 2012 ×1, BSR 2025 ×2, BSR 2026 ×3, Suresh 2026 ×1.

**Def, clause by clause**
- 醫師會綜合症狀、身體檢查、抽血和影像: England, "patient reported measures, provider assessments, laboratory values, and/or imaging modalities". Optional extra evidence for axSpA, TRA Rec 2 (PMID 31777200): "The diagnosis and monitoring of axSpA disease activity should be based on clinical symptoms and signs, laboratory tests, and imaging".
- 緩解或不活躍、低、中、高: England "low, moderate, and high"; Anderson "have remission criteria"; BSR 2026 "inactive disease". BSR 2025 Table 2 also gives ASDAS "Inactive disease <1.3".
- 主要反映發炎: BSR 2025 "inflammatory disease activity" and "whether residual symptoms are related to active inflammation".
- 會隨時間起伏: BSR 2026 "periods of relapse and remission"; Suresh "relapsing-remitting activity".

**Note.** Supported. BSR 2026: "suppressing systemic disease activity, and preventing organ damage". Suresh: "irreversible organ damage".

**Fit with all five phrasings (10 occurrences)**
- 病情活動: CM-2.2 [LINK] fits.
- 疾病活動度: RA-3.4 [LINK], RA-4.1, RA-M2 and AS-2.1 [LINK] all fit. On RA-M2, the note's "activity is not irreversible damage" matches 「X 光上的關節變化」 well.
- 病情不活躍: SL-3.3 [LINK] fits, because the def names 不活躍.
- 病情活躍: SL-6.4 fits.
- 疾病活性: SL-M2 and SL-M4 fit.

**Urticaria exclusion.** UR-4.2 is correctly [excluded]. There, 「病情活躍或控制不好」 refers to inducible-urticaria symptom activity. A def about blood tests, imaging and inflammation would mislead in that sentence. Because `exclude_pages: ["urticaria"]` consumes the alias, no other entry can link it there.

**Other phrasings.** Same-sense phrasings that are not linked (SL-6.2 「狼瘡活躍」, SL-6.3 「病情穩定不活躍」, the SLE seek-care block's 「狼瘡的活性」) are coverage gaps, not wrong-sense links.

**Problems.** None.

## 10. comorbidity — 共病 — **minor**

**What I checked**
- Four quotes, all verbatim: Harrison 2021 PMC ×2, the Valderas 2009 abstract (its PMC body is empty, as the drafters noted), and the Taiwan 2018 gout abstract.
- Def: faithful to Feinstein. "the index disease under study" becomes 主要關注的疾病, and "has existed or may occur during the clinical course" becomes 同時存在或之後出現.
- Note: faithful to Valderas ("worse health outcomes, more complex clinical management").
- Site fit: the card title 「共病與定期檢查」 is consistent with GT-5.1.

**Problem (minor: added frequency claim).** The example begins 「痛風**常見**的共病：…」. The quote says gout is "clearly associated with" these conditions; it gives no frequency.

Proposed example (27 CJK):
> 例如痛風的共病包括心血管疾病、慢性腎臟病、尿路結石、糖尿病等。

Support, PMID 29363262: "gout or hyperuricemia is clearly associated with a variety of comorbidities, including cardiovascular diseases, chronic kidney disease, urolithiasis, metabolic syndrome, diabetes mellitus, thyroid dysfunction, and psoriasis"

## 11. cvd — 心血管疾病 — **OK**

- **Quotes.** Three, all verbatim.
- **Def.** Supported. The list comes from BSR 2026 ("atherosclerosis, myocardial infarction, stroke, peripheral vascular disease and heart failure"), and GBD adds "principally ischemic heart disease (IHD) and stroke". 「心臟和血管的疾病」 is simply the literal meaning.
- **Site fit.** GT-5.1 and SL-5.4 are the [LINK]s; GT-5.T is a [repeat]. All are consistent.
- **Optional.** For precision, 「動脈硬化」 could become 「動脈粥狀硬化」 (atherosclerosis).
- **Housekeeping.** reviewer_notes and evidence[0].supports still mention the 2–3 倍 note, which has been removed.

## 12. ckd — 慢性腎臟病 — **OK**

- **Quotes.** Four, all verbatim (abstracts).
- **Def.** Faithful to KDIGO 2005 and Lancet 2017 (kidney damage or reduced GFR, ≥ 3 months, irrespective of cause).
- **Note.** Faithful: "Many people are asymptomatic …" and "Diagnosis is commonly made after chance findings from screening tests (urinary dipstick or blood tests)".
- **Site fit.** GT-5.1 is consistent.
- **Optional.** 「下降」 has no threshold. Taiwanese patients see eGFR values on their lab reports, so the def could say 「腎絲球過濾率降到 60 以下」 (KDIGO 2005, PMID 15882252: "<60 mL/min/1.73 m(2)").

## 13. urolithiasis — 尿路結石 — **OK**

- **Quotes.** Five, all verbatim.
- **Def.** Acceptable. Khan 2016 gives the supersaturation mechanism for kidney stones, and the def extends it to the urinary tract; EAU 2016 uses "urolithiasis" for renal and ureteral stones.
- **Example.** Supported by EAU ("renal and ureteral stones").
- **Site fit.** GT-5.1 and GT-5.3 are consistent.
- **Housekeeping.** evidence[1].supports says "note", but the note is now empty.

## 14. mgd — 瞼板腺功能不良 — **minor**

**What I checked**
- Four quotes, all verbatim: the Cote 2020 plain-language summary in the PMC record, its abstract, and BSR 2025 PMC ×2.
- Def: faithful to the Cochrane plain-language summary.
- Site fit: the SJ-1.3 alias is 瞼板腺, and the def explains both the gland and the dysfunction.

**Problem (minor: added frequency claim).** The note says 「也**常**合併瞼板腺功能不良」. BSR lists MGD as one contributor to the eye disease in Sjögren's disease, but gives no frequency anywhere (I checked every MGD sentence in BSR 2025).

Proposed note (31 CJK):
> 乾燥症的眼睛不適，除了淚水不足，也和瞼板腺功能不良、眼睛表面發炎有關。

Support, PMID 38621708 (PMC): "SD is associated with complex eye disease [] with aqueous tear deficiency, meibomian gland dysfunction [,] and surface inflammation contributing to the symptom load." The brackets are stripped citation markers.

## 15. blepharitis — 眼瞼炎 — **OK**

- **Quotes.** Two, all verbatim (Cochrane abstract).
- **Def.** Faithful.
- **Note.** Faithful: "may provide symptomatic relief" becomes 可能緩解.
- **Site fit.** SJ-1.T is about prevention. The note complements it and does not contradict it.
- **Problems.** None.

## 16. salivary-gland — 唾液腺 — **OK**

- **Quotes.** Three, all verbatim.
- **Def.** Faithful to Proctor 2016 (three pairs of major glands plus many minor submucosal glands).
- **Note.** Supported by BSR 1A: "Individuals with SD should be offered further investigation early if they present with new salivary gland swelling…". It renders this as 「新的腫脹…應盡早回診檢查」 and does not mention lymphoma.
- **Consistency with SJ-S1.** The note covers the "new swelling" half of SJ-S1. The site's "persistent swelling" half comes from another source and is not contradicted; BSR itself never says "persistent" salivary swelling (checked).
- **Problems.** None. The only caveat is the evidence-quote display issue described in "How this was checked".

## 17. night-sweats — 夜間盜汗 — **minor**

**What I checked**
- Five quotes, all verbatim: BSR 2025 PMC ×2, the Shadman 2023 abstract, and the Mold 2012 abstract ×2.
- Def, clause by clause:
  - 「睡覺時出汗」 is supported (Mold: "Nighttime sweating").
  - 「很多沒有特別疾病的人也會有」 is supported (Mold: "in primary care settings, night sweats are commonly reported by persons without these conditions"; also "appears to be nonspecific").
  - 「嚴重時會全身濕透」 rests only on Shadman 2023, a chronic lymphocytic leukaemia (CLL) review ("drenching night sweats").

**Problem 1 (minor, editorial; needs the physician's decision).** The site's SJ-S2 deliberately leaves lymphoma unnamed to keep the tone calm. This popup's source list would show 「JAMA 2023 慢性淋巴球性白血病回顧」 and "Diagnosis and Treatment of Chronic Lymphocytic Leukemia" on the Sjögren seek-care block. I found no non-oncology PubMed source for "drenching": van Meeuwen 2024 (PMID 39435709) and Mold 2002 (PMID 12019054) say night sweats are common, but do not describe drenching.

Recommendation: drop the clause and the Shadman source. Proposed def:
> 睡覺時出汗；很多沒有特別疾病的人也會有。

Support, PMID 23136329: "Nighttime sweating is a symptom linked to menopause, malignancies, autoimmune diseases, and infections. However, in primary care settings, night sweats are commonly reported by persons without these conditions."

If you want to keep "全身濕透", keep Shadman knowingly.

**Problem 2 (minor: consistency with SJ-S2).** The note 「若持續夜間盜汗，或合併發燒、體重減輕」 differs from the site sentence in two ways:
- It makes fever and weight loss conditional on night sweats. SJ-S2 lists each as a separate trigger.
- It drops the threshold "≥10% over the preceding 3 months".

Proposed note (30 CJK, no lymphoma wording):
> 乾燥症病人若持續夜間盜汗，或有發燒、3 個月內體重減輕 10% 以上，請盡早回診。

A shorter alternative: 「乾燥症病人若持續夜間盜汗，請盡早回診。」

Support, PMID 38621708 (PMC):
- "These include B symptoms (persistent night sweats, fevers and weight loss of ≥10% over the preceding 3 months)"
- "Individuals with SD should be offered further investigation early if they present with new salivary gland swelling or other symptoms that might suggest the development of lymphoma (1, A)"

**Reviewer_notes precision (not shown to patients)**
- The cited PMID 37034003 abstract says "B symptoms (fever, drenching night sweats, unintentional loss >10% of body weight within the preceding 6 months)". It does not say ">38°C".
- The claim that "Mold 2012 notes the lack of a uniform definition" is not in Mold's abstract, and there is no PMC text to check. van Meeuwen 2024 (PMID 39435709, Dutch, English abstract) does say: "There is a lack of a uniform definition and a diagnostic guideline."
- The evidence `supports` labels are swapped: ev0 and ev1 support the note, and ev3 supports the def.
