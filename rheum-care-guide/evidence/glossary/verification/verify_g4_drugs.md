# Verification report: g4_drugs (20 entries)

**Summary: 15 OK, 5 minor, 0 major.**
Minor: `biologic` (source tier), `nsaid` (safety caveat about aspirin), `low-dose-aspirin` (clarity), `non-live-vaccine` (wording nuance), `live-vaccine` (「病毒」 is too narrow).

## What was checked (all entries)
- **Citations.** All 27 cited PMIDs were fetched with `get_article_metadata`. Title, first author, DOI, journal, volume, issue and pages were machine-compared with every `sources[].citation` string, and all match. Where the cited year differs from PubMed's date, the cited year is the print year and PubMed shows the earlier epub date (24072562, 36357155, 31413005, 31672775, 35725297). That is correct. Every evidence item's PMID/DOI/PMCID triple also matches the metadata.
- **Quotes.** I machine-checked 124 evidence quotes against PMC full text (16 articles fetched), PMC-version abstracts and PubMed abstracts, after normalising whitespace, dashes and quote marks. **123 of 124 are verbatim.** The one exception is the EULAR 2020 eye-ointment quote, which is WebFetch only; I re-confirmed it this session (see `eye-ointment`). For each quote I also read about 300 characters of surrounding text, to check for a dropped "not" or "against", a different population, or a wrong section. Negations are intact where they matter: BSR Rec 46 "is not routinely recommended", ACR "recommended against administering live attenuated virus vaccines", GALEN "strongly recommended not to use 1st generation" and "not always necessary to abstain". Locations are correct.
- **Site fit.** I regenerated occurrences with `occ.py` and diffed the result against `occurrences.md`: no differences, so the file reflects the current site JSON. I read every [LINK] and [repeat] sentence, plus the full cards around them. No alias links in the wrong sense. 「類固醇」 never appears on the site for topical or inhaled steroids. 「活性疫苗」 inside 「非活性疫苗」 is consumed by the longer alias, so it is linked correctly.
- **Lengths.** No def is over 90. Several defs are over the soft 60 limit (counting all characters, including punctuation): dmard 65, low-dose-aspirin 63, antihistamine 63, flare-medicine 64, live-vaccine 61, rzv 62, pneumococcal 62, dhea 71 (mostly the Latin "dehydroepiandrosterone"). Every example is 40 or less. One note is over 50, but only if punctuation is counted (oral-glucocorticoid: 54 characters in total, 48 of them CJK). No entry uses 你.

---

## oral-glucocorticoid — OK
- **Quotes.** All 8 are verbatim: 6 in BSR 2026 PMC13290301 (Rec 46 in the recommendation list; the "Glucocorticoids" narrative section; the "Bone health" section), plus the ACR 2022 GIOP abstract and the ECTS 2024 abstract.
- **The note you asked about.** It is supported by BSR 2026:
  - 「長期使用對健康有不良影響」 rests on "owing to the detrimental effects of GC on longer-term health outcomes".
  - 「指引主張盡量減少用量」 rests on "the GWG members strongly advocate for minimisation of GC exposure".
  - 「例如增加骨質疏鬆風險」 rests on "This increased risk could be due to the disease process (i.e. chronic inflammation) and the side effects of therapies, particularly GC". The cited ACR GIOP abstract ("glucocorticoid-induced osteoporosis (GIOP)") supports it independently.
- **The editorial ending is appropriate.** 「調整劑量請和醫師討論，不要自行停藥。」 is also consistent with BSR's own text. Verified quote (PMC13290301, "Glucocorticoids" section): "We acknowledged that some people with SLE in remission and on low-dose prednisone could flare upon GC discontinuation". Without this ending, 「盡量減少用量」 could be read as an invitation to cut the dose oneself, so it should stay.
- **Def.** 「能快速控制病情」 is a faithful rendering of "uniquely consistent and rapid effect on disease activity". The example prednisolone appears in the quote.
- **Site fit.** Fits the common-bone title, CM-4.1/4.T, CM-5.1 and SL-5.5.
- **Optional (length).** If the 50 limit includes punctuation, use this 50-character version (same quotes, PMID 42336388 and 37845798):
  「長期使用對健康有不良影響（例如骨質疏鬆），指引主張盡量減少用量；調整劑量請和醫師討論，不要自行停藥。」

## dmard — OK
- **Quotes and site fit.** All 5 quotes are verbatim: Smolen 2014 abstract, EULAR RA 2022 and 2025 abstracts, SBR 2025 PMC. The cs/ts/b classes and the examples methotrexate and hydroxychloroquine are in the Smolen 2014 quote. Fits CM-5.1 (EULAR 2019 "DMARDs").
- **Optional.** 「標靶合成」 is a classification label that lay readers may not know. It is acceptable because the def only names the classes. The def is 65 characters (soft limit).

## immunosuppressant — OK
- **Quotes.** All 5 are verbatim (ACR 2022 PMC; SBR 2025 abstract; EULAR SLE 2023 abstract; ACIP 2022 PMC Table 1 footnote; EULAR 2019 abstract). 「可用疫苗預防的感染…感染也可能比較嚴重」 is a faithful rendering of "higher risk of vaccine-preventable infections and of more serious complications of infection". 「會壓低免疫系統作用」 has no quote of its own, but it is the literal meaning of the term, so it is acceptable.
- **Example: confirmed in ACR 2022, as you asked.** All three drugs are treated as immunosuppression in the PMC text (PMID 36597813, PMC10291822). ACR's Table 1 medication list is not in the PMC extraction.
  - Methotrexate: "For patients with RMD, continuing immunosuppressive medications other than methotrexate around the time of influenza vaccination is conditionally recommended." This counts methotrexate as an immunosuppressive medication.
  - Azathioprine and prednisone: "The AAP Red Book () and the Infectious Diseases Society of America () define low-level immunosuppression as methotrexate ≤0.4 mg/kg/week, azathioprine ≤3 mg/kg/day, prednisone <20 mg/day (or <2 mg/kg/day for patients weighing <10 kg), or alternate-day glucocorticoid therapy ()."
  - The word "long-term" in 「長期使用的類固醇」 is not in ACR. It comes from ACIP's "long-term systemic corticosteroids" (verified in PMC9351524).
- **Optional.** Add the two ACR quotes above as evidence for the example.
- **Site fit.** Fits CM-5.1 (免疫抑制治療) and CM-5.2/5.4/5.5.

## biologic — minor (source tier)
- **Quotes and wording.** All 5 quotes are verbatim. The def 「用活細胞製造、結構很複雜的藥物」 faithfully renders Vulto 2017: "Biologic drugs are highly complex molecules produced by living cells through a multistep manufacturing process." The examples belimumab and rituximab are in the EULAR SLE 2023 abstract. The note matches BSR 2026 ("smoking may also reduce the efficacy of hydroxychloroquine and belimumab"). Fits SL-2.2.
- **Problem: source tier.** The defining claim rests only on a Tier-3 narrative review in a journal supplement. Its second author is from "Department of Medical Affairs, Biogen International GmbH" (PubMed affiliation), so there is an industry conflict. A **Tier-2, PMC-accessible rheumatology consensus statement** gives the same definition. Verified in PMC full text, Introduction, first sentence:
  > "Biological medicines (or immunobiologics) are large, structurally complex molecules produced by living cells [,]."
  — Pereira PC et al. Position statement of the Biotechnology Committee of the Brazilian Society of Rheumatology on the interchangeability of originator and biosimilar biologics in immune-mediated rheumatic diseases. Adv Rheumatol 2026;66(1). PMID 41618370; DOI 10.1186/s42358-026-00523-5; PMC13488687. PubMed type: Consensus Statement. (This quote was read in the tool output directly, not machine-diffed.)
- **Fix.** The def text does not need to change. Add this source as the primary definitional evidence and change the label to 「巴西風濕病學會 2026・定義」 (this matches the site's existing 「巴西風濕病學會 2015」 label style). Keep Smolen 2014 for the 「生物型 DMARDs」 clause. Vulto 2017 can then be dropped or kept as secondary.

## antimalarial — OK
- **Quotes and site fit.** All 7 quotes are verbatim. 「最早用來治療瘧疾…用於紅斑性狼瘡、乾燥症」 matches Nirk 2020 (Tier 3; abstract). 「基石藥物」 matches "HCQ is a cornerstone therapy for SLE" (BSR 2026). The note matches BSR's "monitor for possible ocular toxicity" and EULAR 2023's "retinal toxicity". Fits SL-2.2 and SL-2.3.
- **Optional wording.** 「醫師會安排」 states what the doctor will do, while the source states what the guideline recommends. 「指引建議使用期間接受眼睛檢查，監測可能的視網膜副作用。」 is more faithful to "The GWG recommend following the RCOphth guideline to monitor…" (PMID 42336388).

## mtx-lef — OK
- **Quotes and site fit.** All 5 quotes are verbatim. csDMARD status and the sulfasalazine example are in EULAR 2022 and 2025. The note matches EULAR Sjögren 2020: "synthetic immunosuppressive agents (cyclophosphamide, azathioprine, methotrexate, leflunomide and mycophenolate)". Fits RA-4.4.
- **Optional.** The label 「EULAR 2022・分類」 could become 「EULAR 2025・分類」. The 2025 update (PMID 41826212) is current and keeps the same classes.

## nsaid — minor (safety)
- **Quotes.** All 7 are verbatim. The def is supported:
  - "most ubiquitously used", "anti-inflammatory, antipyretic, and analgesic" (EAACI 2022).
  - Aspirin is an NSAID: "should avoid NSAIDs, including ASA at anti-platelet doses" (WAO 2025).
  - ibuprofen and diclofenac appear in the WAO NSAID chemical-group list.
- **Problem.** The def says 「阿斯匹靈也屬於這一類」. In the same card, UR-1.2 says 「曾因消炎止痛藥變嚴重，就避免這類藥」, and the term is also linked at UR-5.3 (the diary card), where there is no aspirin caveat. A patient taking low-dose aspirin for heart or stroke prevention could read this as a reason to stop it on their own. UR-1.3 counters this, but only in the triggers card. The entry's note is currently empty.
- **Proposed note** (38 characters):
  「醫師為預防血栓開的低劑量阿斯匹靈，不一定要停用；請勿自行停藥，先和醫師討論。」
  - Support: "However, if low‐dose acetylsalicylic acid is needed as an antithrombotic treatment, it is not always necessary to abstain from using this drug." (2026 urticaria guideline, Section 4 on medications; PMID 41649409, PMC13466004).
  - 「請勿自行停藥」 is the same editorial safety phrase as site UR-1.3.

## low-dose-aspirin — minor (clarity)
- **Quotes and site fit.** All 5 are verbatim and in context (CSU patients with an NSAID history; "antithrombotic"; "reducing cardiovascular risk"; "ASA at anti-platelet doses"). The safety wording is good. Fits UR-1.3.
- **Problem.** In 「…暫改用其他抗血栓藥4週來判斷」, the object of 判斷 is missing, so a lay reader cannot tell what is being judged.
- **Proposed note** (46 characters):
  「蕁麻疹病人不一定要停用；醫師可能暫改用其他抗血栓藥4週，判斷是否和蕁麻疹有關；請勿自行停藥。」
  - Support: "A four‐week transition to another antithrombotic agent can help to assess causality, and if symptoms persist, reintroduction can be considered." (PMID 41649409, PMC13466004).

## antihistamine — OK (housekeeping only)
- **Quotes.** All 9 are verbatim. The subscript 1 is dropped in the PMC text ("H‐antihistamines"), as the drafters noted. "First-line" and the examples cetirizine and loratadine are in the quotes. The note matches Wolff 2017's "anti-histamines for systemic use".
- **Consistency check you asked for.** Def 「新的第二代很少或不會讓人想睡」 matches GALEN "Modern 2nd generation H‐antihistamines are minimally or nonsedating" (PMID 41649409). The site's 「較不會嗜睡的抗組織胺」 (UR-4.1, UR-4.T, UR-M2 fact) says the same thing more loosely. The two are consistent and neither overstates.
- **Housekeeping.**
  - The alias 「不會嗜睡的抗組織胺」 no longer matches anywhere on the site. Its only occurrences are inside 「較不會嗜睡的抗組織胺」, and that longer alias matches first. Removing it is optional and harmless.
  - The reviewer_notes sentence suggesting 「較不會嗜睡」 is stale, since the site has already been changed.
- **Optional.** At the SJ-3.2 link (drugs that cause dry mouth), the title's parenthetical 「（較不會嗜睡的）」 is slightly off-topic. Consider plain 「抗組織胺」. The def already covers both generations.

## ult — OK
- **Quotes and site fit.** All 5 quotes are verbatim. "Continuing ULT indefinitely over stopping ULT is conditionally recommended" is intact, with the direction correct. The note matches "at least 3–6 months … strongly recommended" and "risk of flare associated with initiation". Fits the gout-flare summary and GT-4.4 (keep taking it).
- **Trivial.** Quote [0] matches the **PMC** version of the abstract exactly. PubMed's abstract shows "stage >3" and "febuxostat (<40 mg/day)", where the PMC version has ≥ and ≤. Set access to "PMC abstract". This has no effect on the Chinese text.

## flare-medicine — OK
- **Quotes and site fit.** All 6 quotes are verbatim. First-line colchicine, NSAIDs or glucocorticoids is a strong recommendation. 「及早使用效果較好」 rests on "…demonstrating efficacy … particularly when administered early after symptom onset", which is a fair rendering. 「口袋藥」 renders "medication-in-pocket". Fits GT-4.T.
- **Optional.** Add 秋水仙素 after colchicine to help lay readers.

## non-live-vaccine — minor (wording nuance)
- **Quotes.** All 6 are verbatim. "can be safely provided to AIIRD patients regardless of underlying therapy" supports the def. The note matches ACR's "diminished, but not completely abrogated" and EULAR's "preferably prior to the initiation of immunosuppression".
- **Examples checked, as you asked.** Pneumococcal, hepatitis B and recombinant zoster are all in the SBR 2025 PMC quote. Note that SBR calls them "inactivated" vaccines, not "non-live".
- **Problem.** 「最好在開始免疫抑制治療前接種」 drops the 「如果可以」 that the site's CM-5.1 has, so a patient could read it as a reason to delay treatment.
- **Proposed note** (44 characters):
  「部分藥物會讓疫苗反應變弱（但通常不會完全沒效）；如果可以，最好在開始免疫抑制治療前接種。」
  - Support: "If possible, vaccinations should be administered prior to immunosuppressive drugs, but necessary treatment should never be postponed." (EULAR/PRES 2021 abstract, PMID 35725297).
  - Also: "preferably prior to the initiation of immunosuppression" (PMID 31413005).
- **Optional evidence (exact "non-live" wording).** Verified in Jansen 2022 PMC9298835, Results (PMID 35874582): "The studies covered the non-live vaccines against Diphtheria Tetanus Polio (DTP, 6 studies), Hepatitis A virus (HAV, 4 studies), Hepatitis B virus (HBV, 7 studies) … and Pneumococci (both the pneumococcal conjugate vaccination (PCV) and/or the 23-valent pneumococcal polysaccharide vaccine (PPSV-23) vaccine, 6 studies)".

## live-vaccine — minor (precision)
- **Quotes.** All 7 are verbatim. The ACR sentence with the dropped word ("…medication,live attenuated vaccines is conditionally recommended") is correctly *not* quoted. The direction comes from the intact sentence "conditionally recommended against administering live attenuated virus vaccines". Examples: MMR is in the Jansen PMC quote and yellow fever in the SBR PMC quote. The note matches ACR's "inactivated alternatives that can be safely given". Fits the common-vaccine summary and CM-5.2.
- **Problem.** The def says 「含有活的、但已減弱的**病毒**」. That is too narrow: some live-attenuated vaccines are bacterial, such as BCG (卡介苗, routinely given to infants in Taiwan) and oral typhoid. Jansen 2022 lists BCG among the live-attenuated vaccines. Verified in PMC9298835, Results (PMID 35874582): "In addition, studies were included that reported on the live-attenuated vaccines against Measles, Mumps and Rubella (MMR, …), Varicella Zoster Virus (VZV, 5 studies) (–), one study which included 1 patient with oral polio vaccine () and one case report on the Bacillus Calmette-Guérin (BCG) vaccine ()." ACR also lists "oral typhoid" among live attenuated vaccines (PMID 36597813).
- **Proposed def** (61 characters):
  「活性減毒疫苗含有活的、但已減弱的病原；正在使用免疫抑制藥物的人接種後，可能被疫苗裡的病原感染，所以通常建議延後或謹慎接種。」
  The other supporting quotes stay as they are. 「病原」 mirrors the non-live-vaccine def (「不含活病原」).

## rzv — OK
- **Quotes and site fit.** All 7 quotes are verbatim. The def matches IDST 2024 ("painful, vesicular, cutaneous eruption from reactivation of varicella zoster virus"; "increased risk in the elderly and immunocompromised"). RZV as non-live rests on SBR's "inactivated vaccines … recombinant adjuvanted herpes zoster vaccine". The note matches "Two types of HZ vaccines, zoster vaccine live and recombinant zoster vaccine" and ACR's "reactogenicity is common with this vaccine". Fits CM-5.5.
- **Label.** PubMed lists IDST as the appointing body and the Taiwan College of Rheumatology among the endorsers, which supports 「IDST 2024・指引說明」.

## pneumococcal — OK
- **Quotes and site fit.** All 7 quotes are verbatim. In the MMWR 2024 first sentence, the italic species name is dropped before "(pneumococcus)", but the meaning is intact. PCV and PPSV23 are in the ACR quote. The note matches ACIP 2022 ("doses and intervals … differ by age and underlying conditions"). Fits CM-5.3 and CM-5.4.
- **Optional, closer to "a common bacterial cause of…"** (60 characters; PMID 39773952):
  「肺炎鏈球菌疫苗是預防肺炎鏈球菌感染的非活性疫苗。肺炎鏈球菌是引起肺炎等呼吸道感染的常見細菌，也可能造成血液感染和腦膜炎。」

## artificial-tears — OK
- **Quotes and site fit.** All 7 quotes are verbatim. The Cochrane plain-language summary is in the PMC record's abstract field; it is not in the PubMed abstract. The note matches BSR's "toxic, proinflammatory and detergent effects of the preservative" and "Always prescribe preservative free drops". The sodium hyaluronate example is in the BSR quote. Fits the sjogren-eyes summary and SJ-1.1.
- **Extra support from EULAR 2020** (WebFetch this session): "AT containing methylcellulose or hyaluronate".

## eye-ointment — OK (main quote confirmed via WebFetch; still not machine-checkable)
- **WebFetch re-confirmation, as you asked.** EULAR 2020 (PMID 31672775) has no PMC version, and the quote is not in the abstract. I re-fetched ard.bmj.com/content/79/1/3 twice this session; publisher DOI routes returned a redirect or 403. Both passes returned the sentence word for word. The second pass reproduced the whole paragraph:
  > "…The use of preservative-free formulations of AT is mainly recommended in patients requiring four or more applications per day. Ophthalmic ointments are thicker than AT and may be used to provide symptom control overnight; they are typically used before bedtime because they produce blurred vision and their use should be followed by morning lid hygiene to prevent blepharitis.37"
  - Location: explanatory text of the recommendation "The first-line therapeutic approach to ocular dryness includes artificial tears and ocular gels/ointments" (LoE 1a, LoA 9.5).
  - This is consistent with the 3 research-phase passes (sjogren.md C08).
- **What this supports.** Def and note are fully supported. BSR 2025 (PMC) independently supports night-time use. The blurred-vision point has no machine-checkable source.
- **Housekeeping.** Update the `access` and `reviewer_notes` fields to say "WebFetch re-confirmed 2026-10-07 (2 passes)". The evidence for a vitamin-A example is unused, because the example field is empty.

## saliva-substitute — OK
- **Quotes and site fit.** All 5 quotes are verbatim. The def matches Wolff ("intraoral topical agents … to moisten or lubricate the mouth") and BSR ("for symptomatic relief of oral dryness"). The note faithfully renders "no strong evidence supporting one topical therapy over another". Fits SJ-2.4.
- **SJ-2.4 second clause.** It is now WebFetch-confirmed this session (1 pass): "Saliva substitution should be considered the preferred therapeutic approach to alleviate symptoms in patients with no residual glandular function" (EULAR 2020).

## fluoride — OK
- **Quotes and site fit.** All 7 quotes are verbatim. "topical fluoride should be used in all patients (strong)" is in the abstract. The examples (toothpaste, varnish) are in the BSR quotes. Fits the sjogren-mouth summary, SJ-2.1 and SJ-2.2.
- **Label verified.** The label 「Sjögren's Foundation」 can be checked in PubMed: a search for "Sjogren's Syndrome Foundation Clinical Practice Guidelines Committee" returns only PMID 26762707, as its collective author.

## dhea — OK
- **Quotes and site fit.** All 7 quotes are verbatim. "precursor of sex hormones: androgens and estrogens" matches 「轉變成男性和女性荷爾蒙」. The note matches "results in … SS are disappointing" and "androgenic effects such as acne and hirsutism, which were considered mild". Fits SJ-M3 (5 studies, 240 women, no difference from placebo).
- **Source tier.** Tier 3. This is acceptable because the site already cites this source.

---

## Housekeeping (not patient-facing; no verdict impact)
- **nsaid.** reviewer_notes mention 「換藥前請先問醫師」, and evidence[5] says it supports "note: 乙醯胺酚…". The note is now empty, so both are stale.
- **mtx-lef.** Evidence [1] and [2] and the reviewer_notes refer to 「一開始先用 methotrexate」, which is no longer in the def.
- **antimalarial.** Evidence [3] supports an example, but the example field is empty.
- **eye-ointment.** Evidence [2] and [3] support a vitamin-A example, but the example field is empty.
- **immunosuppressant.** The reviewer note says it is unverified whether ACR counts HCQ or SSZ as immunosuppressive. That is still true; the PMC text has no Table 1. The def makes no such claim.
- **flare-medicine.** The alias 「發作時用的藥」 is generic. It currently occurs only on the gout page. If RA or axSpA text ever uses the same phrase, the gout definition would be linked in the wrong sense, so consider adding non-gout pages to exclude_pages.
