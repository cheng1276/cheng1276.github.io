# Verification report — g3_diet_sun

**Summary: 19 entries checked — OK 10 · minor 9 · major 0.** New entry `uva-rating` drafted → `/home/claude/glossary/new_uva-rating.json` (valid JSON; links once, in SL-1.2).

OK: purine, alcohol-serving, mediterranean, refined-carbs, elemental-calcium, iu, xylitol, diagnostic-diet, spf, uv-index
Minor: uric-acid, hfcs, special-diets, saturated-fat, processed-food, bmi, uva-uvb, broad-spectrum, photosensitivity

## How the check was done (applies to all entries)
- **Quotes:** every quote was machine-checked after normalising whitespace, quote marks and dashes. The texts were PMC full text and the PMC abstract field, which holds the Cochrane plain-language summaries, plus the PubMed abstract. I read the surrounding sentence for each quote. 90 of 94 quotes were found verbatim at the stated location (alcohol-serving ev[0] matches in its two parts around the "…"). Four quotes are WebFetch-only and cannot be machine-checked:
  - ACR 2022 RA Table 1 (mediterranean ev[1], special-diets ev[0]).
  - ACR 2022 GIOP manuscript (elemental-calcium ev[0], iu ev[0]).

  The PMC web page is blocked by a CAPTCHA, and the PMC text omits Table 1. Each of these four quotes only supports how the site uses the term. No def/example/note depends on them.
- **Citations:** all 34 cited PMIDs were checked against PubMed metadata (first author, title, journal, year, volume/pages, DOI). All match. Argyrou 2020 genuinely has no DOI in PubMed. Print years are used for epub-early items (Kerr 2012, Ross 2011, Oslo 2013, Bakaloudi 2021), which is correct.
- **PMC pitfalls seen (none affect these entries):**
  - ACR 2020 has "Adding vitamin C supplementation is conditionally recommendedfor…", where "against" was dropped.
  - ACR 2022 has "Adherence to a formally defined diet, other than a Mediterranean-style diet, is conditionally recommended.", also missing "against".

  The drafters correctly avoided both sentences.
- **Access label:** the Cochrane plain-language-summary quotes (saturated-fat, xylitol) are marked "PMC full text". The PMC full_text field is empty for both reviews; the PLS is in the PMC record's abstract field. Suggest relabelling as "PMC record (plain language summary)".

---

## purine — OK
- **Quotes:** 5/5 verbatim (Keenan abstract; Jamnik PMC Intro; Zhang PMC Methods and Discussion; ACR 2020 PMC).
- **Support:** "dominant source of urate is endogenous purines" supports 「大多來自身體本身」. "especially of animal origin (that tend to have higher purine content than those of plant origin)" supports the note.
- **Example:** Zhang's list also contains beans, peas, lentils, oatmeal, spinach, asparagus, mushroom, yeast, beer and other alcohol. The example lists only animal foods plus 「等」. This is acceptable given GT-2.4 and the note; the physician's choice is already flagged in reviewer_notes.
- **Fit:** GT-2.1 and gout-food fit.
- **Length:** def 52 characters.

## uric-acid — minor
- **Quotes:** 5/5 verbatim.
- **def:** supported by Jamnik, Keenan and Dalbeth.
- **note:** faithful to ACR: "≥6.8 mg/dl with no prior gout flares or subcutaneous tophi".
- **Taiwan consensus** (PMID 29363262): the abstract was checked. It gives only ULT targets (<6.0 and <5.0 mg/dL) and no hyperuricaemia threshold, so there is nothing to reconcile from the abstract.
- **Problem (precision):** the label 「ACR 2020・定義」 implies that ACR defines uric acid and hyperuricaemia. The def actually rests on Jamnik, Keenan and Dalbeth; ACR supplies only the note.
  - **Fix:** label → 「文獻回顧與 ACR 2020・定義」
  - **Supporting quotes:**
    - "Increased concentration of serum urate (hyperuricaemia) is the most important risk factor for the development of gout." (PMID 33798500)
    - "…asymptomatic hyperuricemia, which is defined as an SU concentration of ≥6.8 mg/dl with no prior gout flares or subcutaneous tophi." (PMID 32391934)

## hfcs — minor
- **Quotes:** 3/3 verbatim.
- **Problem:** the def says 「常加在含糖飲料裡」 ("commonly added"), but no quote says "commonly".
  - Jamnik says only "…high-fructose corn syrup (HFCS) in sugar-sweetened beverages (SSBs)".
  - White describes US use and says ">90% of the nutritive sweetener used worldwide is sucrose".
- **Fix (def, 47 characters):** 「高果糖玉米糖漿是由果糖和葡萄糖組成的液體甜味劑，用來取代一般砂糖（蔗糖），例如加在含糖飲料裡。」
  - Supporting quote: "Fructose is a monosaccharide found commonly in plants. It is also a major constituent of high-fructose corn syrup (HFCS) in sugar-sweetened beverages (SSBs)." (PMID 27697882)
- **Housekeeping:** ev[1].supports still refers to a note that the editors deleted.

## alcohol-serving — OK
- **Ounce values** match the Neogi PMC Methods sentence: "Explanation and pictorial depiction of standard serving sizes (, a 12-ounce bottle or can of beer; a 5-ounce glass of wine; and 1 to 1.5 ounces of liquor)were provided with color images." The PMC extractor drops "i.e."; the "…" in the quote is legitimate.
- **Arithmetic is correct** (1 US fl oz = 29.6 ml per Kerr, exact value 29.57):

  | Ounces | × 29.6 ml | Exact | Rounded |
  |---|---|---|---|
  | 12 | 355.2 | 354.9 | ≈355 ml |
  | 5 | 148.0 | 147.9 | ≈148 ml |
  | 1 | 29.6 | 29.6 | ≈30 ml |
  | 1.5 | 44.4 | 44.4 | ≈44 ml |

- **Other checks:**
  - Kerr "(1 US ounce=29.6ml)" and "common bottle size (355ml)" are verbatim.
  - The US setting is confirmed: "prospective Internet-based case-crossover study in the US".
  - The ACR ">1–2 … 40% higher" quote and Neogi OR 1.36 (1.00–1.88) are verbatim.
- **Optional wording:** 「這裡是該研究採用的美國份量」 → 「這裡是該美國研究採用的份量」. This is more literal; not required.

## mediterranean — OK
- The PMC in-text definition and the Discussion quote are verbatim. The Table 1 WebFetch quote is identical in content to the verified in-text sentence.
- Length: def 71 characters (60 CJK), which is at the ideal limit.

## special-diets — minor (length)
- **Each definition checked against PMC/abstract:**
  - 生酮: Paoli, "reduction in carbohydrates (usually to less than 50 g/day)…" in a "very-low-carbohydrate" diet review. 「大幅少吃醣類」 is faithful.
  - 無麩質: Oslo, "A gluten-free diet usually indicates a diet free from wheat, rye, barley, triticale, kamut and spelt." Faithful.
  - 純素: Bakaloudi "animal- and all their by-products are excluded", plus Craig ("lacto-ovo-vegetarian diets (this allows for the consumption of dairy products and eggs)"). 「包括蛋和奶」 is correctly inferred.
  - 間歇性斷食: Koppold, "repetitive fasting periods lasting up to 48 hours each". Faithful.
- **note:** ACR Introduction quote verbatim; good safety wording.
- **ACR diet list:** the PMC text lacks Table 1 and names only "vegan" in the Discussion. Ketogenic, gluten-free and intermittent fasting as ACR-evaluated diets rest on the WebFetch quote alone, which affects the site text (RA-3.2), not the glossary definitions.
- **Problem:** the def is 84 characters (72 CJK), above the ideal of 60 (maximum 90).
  - **Fix (70 characters / 56 CJK, same quotes):** 「生酮：大幅少吃醣類。無麩質：不吃小麥、黑麥、大麥等含麩質穀類。純素：不吃任何動物性食物，包括蛋和奶。間歇性斷食：反覆斷食，每次最長48小時。」 The "特定飲食法" framing is already in RA-3.2.
  - **Supporting quotes:** PMIDs 23801097, 22345659, 33341313 and 34836399, 39059384, as already listed.
- **Housekeeping:** the TRE evidence row still says "supports: example", but the editors deleted the example.

## refined-carbs — OK
- Ludwig PMC quotes are verbatim: "Refined grains are processed to remove the protein and fat rich germ and fibre rich bran, leaving only the starchy endosperm."
- White rice as a refined grain is supported.
- The term-scope caveat is already in reviewer_notes.

## saturated-fat — minor (housekeeping only; patient text OK)
- **Rewritten def checked against the Cochrane quotes.** Both PLS sentences are verbatim in the PMC record:
  - "…cutting down on saturated fat in our food (replacing animal fats and hard vegetable fats with plant oils, unsaturated spreads or starchy foods)"
  - "…reducing the amount of saturated fat we eat, by cutting down on animal fats…"
- **Assessment:** these support 「在動物油脂和植物性的固態油脂中含量較多」 as a fair, not overstated, reading. Cutting these fats is how saturated fat is reduced, relative to plant oils. 「植物性的固態油脂」 correctly renders "hard vegetable fats". The quotes never say "solid at room temperature", and the text no longer claims it.
- **Example and note** are verbatim in Liu (PMC):
  - "palmitic acid, the major saturated fatty acid in the diet, … predominant fatty acid present in dairy and meats"
  - "ingredients high in saturated fat (e.g., palm oil)"
- **Problem:** `confidence` and `reviewer_notes` still describe Campos 2018 (PMID 29788879) and the 'solid at room temperature' phrase, both removed by the editors.
  - **Fix confidence:** "Medium (Tier 3: Cochrane plain language summary and a Nutr J review; no site-cited guideline defines saturated fat)".
  - **Fix reviewer_notes:** delete the sentence beginning "Campos 2018 is a drug-delivery review…".

## processed-food — minor
- **Quotes:** 7/7 verbatim (Monteiro abstract ×4, Poti abstract ×2, ACR). def and example are supported.
- **Problem:** the note's 「國際常用的」 is not in any quote.
  - **Fix (note, 36 characters):** 「指引沒有定義這個詞；這裡借用 NOVA 食品分類中「超加工食品」的說明。」
  - **Alternative without the jargon (48 characters):** 「指引沒有定義這個詞；這裡借用一套依工業加工程度分類食品的系統（NOVA）對「超加工食品」的說明。」
  - **Supporting quote:** "Ultra-processed foods are defined within the NOVA classification system, which groups foods according to the extent and purpose of industrial processing." (PMID 30744710)

## elemental-calcium — OK
- **Percentages verified** in the Babey abstract: "calcium carbonate because it is 40% elemental calcium by weight. However, calcium citrate (21% elemental calcium)…". The note's 40% and 21% are correct.
- **Example verified** in the Argyrou abstract: "1.25 g calcium carbonate (equivalent to 500 mg of elemental calcium)". This is consistent with 40%.
- **Not done:** a guideline-tier source (BHOF Clinician's Guide 2022, PMID 35478046) could not be checked because PubMed was persistently rate-limited.
- **Optional:** the def speaks of supplements, whereas CM-4.2 counts diet plus supplements. Not contradictory.

## iu — OK
- **Conversion source verified (Tier 1, site-cited).** The BSR 2026 PMC sentence reads: "…the NHS recommend that people aged 4 years or older should be given a daily supplement containing 10 micrograms (400 IU) of vitamin D throughout the year". It sits in the rationale for Recommendation 30.
- This gives 10 µg = 400 IU (1 µg = 40 IU) for vitamin D, which is correct. Ross 2011 is verbatim.

## bmi — minor (source quality)
- **Quotes:** 4/4 verbatim. The formula and cut-offs are correct as written, but the formula and the ≥30 cut-off rest on a cystic-fibrosis meta-analysis abstract (Nagy 2022).
- **WHO 2004 Lancet abstract** (PMID 14726171) states:
  - the WHO overweight cut-off (≥25 kg/m²);
  - that WHO cut-offs remain the international classification;
  - the Asian caveat.

  It does **not** state the formula or the ≥30 obesity cut-off, and the full text is not in PMC.
- **Better sources, both PMC:**
  1. **Yumuk V et al. European Guidelines for Obesity Management in Adults.** Obes Facts 2015;8(6):402-24. PMID 26641646, DOI 10.1159/000442721, Tier 1 (EASO guideline). Quotes:
     - "In clinical practice, the body fatness is usually estimated by BMI. BMI is calculated as measured body weight (kg) divided by measured height squared"
     - "overweight (also termed pre-obesity) by a BMI between 25 and 29.9"
     - "Lower BMI cut-off points apply for some ethnic groups (e.g. Southeast Asians)"

     ⚠ Do **not** quote its obesity clause. PMC renders it as "obesity is defined by a BMI 30 kg/mand overweight", with the "≥" and "²" dropped.
  2. **Rubino F et al. Definition and diagnostic criteria of clinical obesity.** Lancet Diabetes Endocrinol 2025;13(3):221-262. PMID 39824205, DOI 10.1016/S2213-8587(24)00316-4, Commission consensus endorsed by 76 organisations. Quotes:
     - "The current diagnosis of obesity worldwide is based on BMI, calculated as weight in kilograms divided by height in metres squared."
     - "According to WHO, an adult with a BMI of 30 … or higher is considered to have obesity."

     The "…" replaces "kg/m²", which PMC glues to "or" ("kg/mor").
- **Fix:** keep the def and note text, which are accurate. Add sources 1 and 2 with the quotes above, and keep WHO 2004 for ≥25 and the Asian caveat. Nagy 2022 can be dropped or kept as supplementary.
- **Note accuracy:** 「25 以上為過重、30 以上為肥胖」 is correct WHO classification. 「亞洲人在 BMI 較低時，健康風險就可能升高」 is faithful to WHO 2004: "high risk of type 2 diabetes and cardiovascular disease is substantial at BMIs lower than the existing WHO cut-off point for overweight (≥25 kg/m2)".
- **Taiwan 24/27 cut-offs:** no PubMed-indexed source that defines them was found. Pan 2004 AJCN (PMID 14684394) only argues for lower Asian cut-offs. The physician's decision remains open.
- **Optional caveat for the physician:** Rubino 2025 recommends "BMI should be used only as a surrogate measure of health risk at a population level, for epidemiological studies, or for screening purposes, rather than as an individual measure of health".

## xylitol — OK
- BSR 2025 PMC and four Cochrane PLS quotes are verbatim.
- 「甜度…差不多」 is a slightly softened rendering of "equally as sweet" and is acceptable.

## diagnostic-diet — OK
- GALEN 2026 PMC quotes are verbatim, and the context was read: "may be considered in selected patients … 2–3 weeks are usually recommended … should not delay effective treatment".
- Safe wording.

## spf — OK
- BSR quotes (×4) and the Bens abstract are verbatim.
- Further support is in Young 2026 (PMID 41968398) and Patel 2026 (PMID 41869094): "SPF is defined as the ratio of the minimal erythema dose (MED) on sunscreen-protected skin to the MED on unprotected skin".
- Fit with SL-1.2 and SL-1.3 is correct.
- **Optional:** 「UVA的防護要另看UVA標示」 → 「…要另看UVA防護等級標示」 to tie this entry to the new `uva-rating` entry.

## uva-uvb — minor
- **Quotes:** 5/5 verbatim. The Kim & Chong wavelengths and the "deeper dermis" statement are supported.
- **Problem 1 (fit):** the entry is linked from UR-2.T (solar urticaria, urticaria page). Its lupus-specific note and the unqualified 「指引建議」 can be read as urticaria advice. GALEN instead says sunscreen choice depends on the eliciting wavelengths.
  - **Fix (note, 47 characters):** 「在紅斑性狼瘡，兩種都可能促成皮膚病灶；英國狼瘡指引建議用同時防 UVA 和 UVB 的防曬乳。」
  - **Supporting quotes:**
    - "Assessment of both ultraviolet-A (UVA) (320–400 nm) and ultraviolet-B (UVB) (290–320 nm) radiation suggest that each contributes via different mechanisms towards promoting cutaneous lesion development" (PMID 23281691)
    - "26. People with SLE should be advised … to use high sun protection factor (SPF), broad-spectrum UV-A and UV-B sunscreen (1B)…" (PMID 42336388)
- **Problem 2 (housekeeping):** reviewer_notes says "the def says 約 (about)", but the current def no longer gives wavelengths. Update or remove that phrase.

## broad-spectrum — minor
- **Quotes:** 4/4 verbatim.
- **Problem:** the note 「SPF只代表UVB防護；UVA防護要另看UVA標誌或星等。」 has two issues:
  - 「只」 overstates the sources. Young 2026 says SPF "is primarily a measure of UVB protection against erythema and does not quantify protection from UVA".
  - The UVA logo and star rating are UK labels; Taiwanese products usually carry PA grades. The same sentence (SL-1.2) now links 「UVA 防護等級」.
  - **Fix (note, 43 characters):** 「SPF 主要代表 UVB 防護、看不出 UVA；UVA 要另看 UVA 防護等級標示。」
  - **Supporting quotes:**
    - "The sun protection factor (SPF) is primarily a measure of UVB protection against erythema and does not quantify protection from UVA, which is the major component of solar UVR." (PMID 41968398, abstract)
    - "…UV-B protection is indicated by the SPF while UV-A protection is indicated by the UV-A logo or the UV-A star system (i.e. one to five stars)." (PMID 42336388)

## uv-index — OK
- 6/6 abstract quotes are verbatim.
- No year is given, which correctly avoids the 1994/1995 conflict.
- The Lehmann 2019 UVI-2 caution remains an optional physician addition.

## photosensitivity — minor (evidence record)
- **Quotes:** 5/5 verbatim, including the ACR definition quoted by Kim & Chong.
- **Problem:** the def's 「常」 (often delayed) is supported by an unlisted sentence. The listed quotes say flares "occur days to weeks after", and BSR says only a "potential lag period of several weeks".
- **Fix:** no text change. Add the evidence row "several photoprovocation studies have clearly demonstrated that the onset of true photosensitive reactions is often delayed" (Kim & Chong, PMID 23281691, PMC3539182, 'Photosensitivity in lupus patients'). Optionally also add "In fact, positive reactions have been observed up to three weeks after phototesting".
- **Alternative**, if the physician prefers the site's own hedge (SL-M3 「可能隔幾週」): 「紅斑性狼瘡的這類皮疹，可能在曬後幾天到幾週才出現。」

---

## NEW ENTRY: uva-rating (cat "sun") → `/home/claude/glossary/new_uva-rating.json`
- **def (70 characters / 42 CJK):** 「防曬產品標示 UVA 防護力高低的方式，各地不同：亞洲常見 PA 等級，「+」越多防護越高；英國指引則看 UVA 標誌或 1 到 5 顆星。」
- **example:** 「PA+、PA++、PA+++、PA++++。」
- **note (50 characters):** 「PA+++ 屬「高」、PA++++ 屬「很高」；英國指引則要求有 UVA 標誌或 4 到 5 顆星。」
- **Sources:** all quotes were machine-checked.
  - BSR 2026 (PMC): UVA logo or 1–5 star system; the BAD-based "high" standard of a UV-A logo or 4–5 stars.
  - **Patel MN, Patel N. Cureus 2026;18(2):e103757.** PMID 41869094, PMC13000865. "Japan employs a PA rating system to communicate the extent of UVA protection. This system, developed domestically and now widely used in Asian markets, categorizes UVA effectiveness based on the persistent pigment darkening (PPD) method…" Table 1: PA+ Some / PA++ Moderate / PA+++ High / PA++++ Very high UVA protection.
  - Young 2026 (PMID 41968398, PMC): "no worldwide consensus on how to measure and label the level of UVA protection".
  - Bens 2014 abstract: national labelling regulation.
- **Source quality (stated in reviewer_notes):** Patel 2026 is the only PubMed-indexed, readable source found that describes PA. It is a Cureus editorial and only a weak authority, so confidence is Low for the PA part. Moyal 2010 and 2012 likely describe PA but are abstract-only. The PPD ranges behind each grade are unsourced, so no numbers are given. No source covers Taiwanese labelling rules.
- **Conflict (in reviewer_notes):** BSR says higher SPF usually means more UVA protection, whereas Young 2026 reports "a lack of relationship between SPF and UVA-PF values". The entry makes neither claim.
- **Linking (simulated with occ.py rules):** the alias 「UVA 防護等級」 matches only SL-1.2. It takes over the second 「UVA」 there, which is currently an uva-uvb [repeat]. The first 「UVA」 stays linked to uva-uvb.
