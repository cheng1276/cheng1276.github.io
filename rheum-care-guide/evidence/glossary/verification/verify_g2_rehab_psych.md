# Verification report: g2_rehab_psych

**Summary: 16 entries checked. OK 9 · minor 6 · major 1.**

| Verdict | Entries |
|---|---|
| major | physical-therapy (the note) |
| minor | activity-pacing, spinal-manipulation, cervical-traction, contact-sports, flare-plan, complementary |
| OK | occupational-therapy, hand-therapist, joint-protection, orthoses, assistive-devices, self-management, vocational-rehab, cbt, psychosocial |

## What I checked (all entries)

- **Quotes.** I checked every PMC/abstract quote by machine against the text returned by `get_full_text_article` (PMC) or the PubMed abstract, after normalising whitespace, quote marks and dashes. All of them were found verbatim, and every stated location is right. I read the surrounding sentence for each negative or directional quote ("not", "against", "without", "no evidence"). None of these quotes depends on a word dropped in extraction.
- **Citations.** The group cites 17 source PMIDs. For the 15 journal records, plus the 2 co-published ACR records named in the citations, I checked PMID, DOI, first author, title, journal, year, volume and pages against PubMed metadata. All match. The 2 NICE book records return no metadata, so I checked them by search; details are given below.
- **Proposed-fix quotes.** I also machine-verified the quotes behind my own proposed fixes, using the same normalisation: Regnaux 2019 (PMC6774752), BMJ 2009 (PMC3266846), and the EULAR 2021 Discussion and Wieland MeSH sentences.
- **Length and register.** Every def, example and note is within its limit: the longest def is 54 CJK characters, the longest example 26 and the longest note 33. All entries use 您, and none uses 你.
- **Site fit.** I read every [LINK] and [repeat] sentence in occurrences.md, the full cards in ra/axspa/sle/sjogren.json, and grepped all seven content files for each alias, so that no occurrence hidden by longest-match segmentation was missed. No alias is linked in a wrong sense. No other glossary entry has an alias that overlaps one of mine. The stop list contains only 「指引說明」.
- **Glossary code.** The site repo has no glossary code yet, so occ.py (longest match wins; first occurrence per card or page scope) is the reference I checked against.

### Cross-cutting 1: ACR 2022 Table 1 quotes (PMID 37227071), which are WebFetch only
The PMC full text from `get_full_text_article` (PMC10947582) **does not contain Table 1**. The text reads "The interventions considered in this guideline are defined in." with the table dropped. So **none of the Table 1 quotes can be machine-checked**. Europe PMC fullTextXML returned 404.

To confirm them independently, I ran my own WebFetch passes on **two different documents**:
- (a) the PMC table page, pmc.ncbi.nlm.nih.gov/articles/PMC10947582/table/T1/ (caption: "Table 1. Descriptions and examples of interventions included in the integrative management of rheumatoid arthritis guideline.");
- (b) the CDC Stacks author manuscript, stacks.cdc.gov/view/cdc/151745/cdc_151745_DS1.pdf.

Both documents returned **identical wording for all 13 rows** used in this group, and that wording matches the glossary quotes character for character:
- comprehensive physical therapy (2 segments): physical-therapy;
- comprehensive occupational therapy (2 segments): occupational-therapy. The row also contains the middle sentence "Receives patient-centered individualized treatment.", which the drafters simply did not quote. That is not an error;
- joint protection techniques: joint-protection;
- bracing and orthoses: orthoses;
- assistive devices, adaptive equipment, environmental adaptations: assistive-devices;
- activity pacing: activity-pacing;
- self-management program (first sentence): self-management;
- vocational rehabilitation, and work site evaluation and modifications: vocational-rehab;
- chiropractic: spinal-manipulation;
- cognitive behavioral therapy: cbt.

**Status:** all 13 are "confirmed by cross-document WebFetch agreement, not machine-checkable". None was contradicted.

I also machine-verified all **19** distinct non-Table-1 ACR 2022 quotes used in this group against the PMC text. All 19 were found, none missing:
- the comprehensive OT/PT sentence;
- the resistance-exercise supervision sentence;
- the Discussion "Early referral…" sentence;
- the hand therapist sentence and the hand therapy statement;
- the 2 joint protection sentences;
- the orthoses prescription sentence and the 3 orthoses statements;
- the assistive-devices rationale;
- the activity pacing rationale and statement;
- the self-management statement;
- the vocational rehabilitation and work-site statements;
- the chiropractic "not" rationale;
- the CBT statement.

### Cross-cutting 2: other WebFetch-only quotes
I re-ran each of these myself:

| Source | Quotes | My pass | Machine-checkable copy |
|---|---|---|---|
| NICE NG65 (nice.org.uk/guidance/ng65/chapter/Recommendations) | 1.3.4, 1.3.5 (all 5 bullets), 1.5.1 (all bullets) | Identical to the glossary quotes (bullets joined with semicolons) | None found. A BMJ 2017 summary exists (McAllister K et al. BMJ 2017;356:j839; PMID 28249891; doi:10.1136/bmj.j839), but its PubMed metadata lists no PMC ID and no abstract. (The ID conversion call was rate-limited, so this rests on the metadata alone.) |
| NICE NG100 | 1.8.9 and 1.8.10 (first bullet), under the heading "Diet and complementary therapies" | Identical | **Yes.** The same [2009] recommendation is in PMC: see the complementary entry. |
| EULAR 2024 (ard.bmj.com/content/83/6/720; the ard.eular.org copy returned 403) | Both psychosocial example sentences | Identical. My pass also confirms that the text gives no definition of "psychosocial interventions". | None (no PMC copy) |

### Cross-cutting 3: the 「職能」 alias (occupational-therapy)
occ.py segments 「職能或物理治療師」 as 職能 | 或 | 物理治療師. Because the longest match wins, 職能治療師 and 職能治療 still match whole elsewhere. 「職能」 appears on the site only in these four RA sentences, so it is never linked in another sense.

- **RA-2.1 [LINK]** 「…手部治療師（多為受過進階訓練的職能或物理治療師）評估」: 職能 stands for 職能治療師. The popup term 「職能治療」 and the def 「職能治療是由職能治療師評估和治療…」 make sense here.
- **RA-2.2 [repeat]** 「向職能或物理治療師學習關節保護技巧」: makes sense.
- **RA-2.3 [repeat]** 「並請職能或物理治療師協助挑選和調整」: makes sense.
- **RA-2.5 [repeat]** 「職能治療」 matches whole: makes sense.

Note: in all three 「職能或物理治療師」 phrases, 物理治療師 is correctly attributed to physical-therapy but is **not tappable**, because physical-therapy is page-scoped and its RA link is used at RA-1.3. So the phrase does not make both halves tappable; only 職能 in RA-2.1 is. This works as designed, and nothing is mislinked.

Watch-point: if future site text uses 職能 in a non-therapy sense, such as job competencies, this short alias would link it.

### Cross-cutting 4: NICE book records (no DOI; get_article_metadata returns nothing)
Date-filtered PubMed searches show:
- **28350428**: NICE-published, dated **Feb 2017**. This matches NG65's first publication on 28 Feb 2017.
- **32049469**: NICE-published, dated **Jun 2017**. This matches the 2 June 2017 update.
- **30102507**: NICE-published, dated **Jul 2018**. This matches NG100's publication on 11 Jul 2018.

Either NG65 PMID can be defended. 28350428 matches the "published 28 February 2017" citation.

---

## physical-therapy: **major**

**Checked:**
- All 9 quotes:
  - ACR 2022 PMC ×2 machine-verified (Results → Rehabilitation; Exercise → resistance);
  - ACR 2015 PMC5123840 ×3 machine-verified, with locations A2, B2 and C/PICO 20 confirmed;
  - ACR Table 1 ×2 confirmed in 2 documents;
  - NICE 1.5.1 confirmed by my WebFetch;
  - Cochrane 2008 PLS sentence verbatim. The PMC record's body is empty and the sentence sits in the plain language summary within the abstract field, so "PMC full text" is really "abstract/PLS".
- Citations: all correct. The NICE PMID is discussed above.
- def and example: supported and faithful. They fit every linked and repeated sentence (RA-1.3, RA-2.x, AS-1.x, AS-M3, axspa-exercise).

**Problem (major): the note overstates benefits from an outdated background sentence.**
The note reads 「在僵直性脊椎炎，物理治療有助維持或改善脊椎活動、增進體能，並減輕疼痛。」

- **Source type.** The source is a Cochrane systematic review (Tier 3) from 2008, with searches to January 2007. The quoted sentence is a *background* line in the plain language summary ("Physiotherapy is an important treatment to maintain or improve movement in the spine, improve fitness and decrease pain."). It states what physiotherapy is used for, not what the review found.
- **What the evidence shows.**
  - That review's own findings are low- to moderate-quality evidence for spinal mobility and function. A pain effect appeared only for spa therapy added to group physiotherapy, and fitness was not an outcome.
  - The newer Cochrane review on the same population is Regnaux 2019 (PMID 31578051). Its conclusion says: "We are uncertain whether exercise programmes improve spinal mobility, reduce fatigue, or induce adverse effects."
  - ACR 2015, which the site cites (PMC-verified), reports for stable AS: "improvement in disease activity and physical functioning but no significant improvement in pain or stiffness".
- **Site consistency.** The site's own evidence file explicitly decided "Do not promise mobility gains" (research/axspa.md, M12).
- **Wording.** 「有助…」 turns a statement of purpose into a statement of effect. Because the entry is page-scoped, this AS-specific note also appears on the RA page (RA-1.3).

**Proposed fix (preferred):** delete the note, so that note = "". The def and example already explain physical therapy, and the AS page text needs no benefit claim here.

**Alternative, if an AS note is wanted** (44 CJK):
「在僵直性脊椎炎，和不運動相比，運動計畫可能稍微改善身體功能、減輕疼痛；對脊椎活動度的效果還不確定。」

Supporting quote, verbatim from the PMC record's plain language summary, Key results, "Exercise programmes versus no intervention":

> "Exercise probably slightly improves function (moderate‐quality evidence), slightly reduces patient‐reported disease activity (moderate‐quality evidence), and may reduce pain (low‐quality evidence). We are uncertain of the effect on spinal mobility and fatigue (very low‐quality evidence)."

Source: Regnaux JP, et al. Exercise programmes for ankylosing spondylitis. Cochrane Database Syst Rev 2019;10(10):CD011321. PMID 31578051; doi:10.1002/14651858.CD011321.pub2; PMC6774752. Metadata checked.

If this alternative is used, replace source 4 (Cochrane 2008) with this record.

**Minor (information only):** on the evidence item for PMID 18254008, change access "PMC full text" to "abstract (plain language summary)".

## occupational-therapy: **OK**

**Checked:**
- Cochrane 2004 (PMID 14974005) Background, Objectives and plain-language-summary quotes: all verbatim in the abstract field of PMC7017227.
- ACR quotes: the PMC ones are machine-verified; Table 1 is confirmed in 2 documents.
- EULAR 2021 R7 text (PMID 33962964, PMC8458093): verbatim.
- The def (穿衣、煮飯、打掃、工作; 較少的疼痛) matches the summary sentence "Occupational therapists can give advice on how to do every day activities with less pain".
- The example matches the Objectives list. The note is faithful.
- The 「職能」 alias works: see cross-cutting 3.

No problems.

## hand-therapist: **OK**

**Checked:**
- Both ACR quotes are verbatim in PMC (Rehabilitation recommendations, hand therapy).
- The def is faithful. 「通常是受過額外訓練的職能或物理治療師」 extends the source's description of a CHT ("typically an occupational or physical therapist with additional training") to hand therapists in general. That is a small generalisation, and the site's RA-2.1 says the same 「多為…」. Acceptable.
- Fits RA-2.1.

Metadata nit (not patient-facing): the evidence "supports" field says "and note (CHT)", but the note is empty.

## joint-protection: **OK**

**Checked:**
- The Table 1 definition was confirmed in 2 documents.
- The two PMC quotes are verbatim.
- The def and example are a faithful translation. 「以減少疼痛、發炎和關節負擔」 keeps the "aims to … reduce" purpose framing.
- The note is supported by "stressed the importance of proper patient education in joint protection techniques by occupational or physical therapists".
- Fits ra-intro, the ra-hands title and summary, and RA-2.2.

## orthoses: **OK**

**Checked:**
- The Table 1 "Bracing and orthoses" row was confirmed in 2 documents.
- The 4 PMC quotes are verbatim. The orthoses prescription sentence keeps "without a prescription".
- The def and example are faithful. 貼紮 is listed in the source.
- The note is faithful and safe: it buys OTC, but with guidance from an OT or PT.
- Fits RA-2.3.

## assistive-devices: **OK**

**Checked:**
- Cochrane 2009 (PMID 19821383) Background sentence: verbatim in the abstract field of PMC7389411.
- The 3 Table 1 rows were confirmed in 2 documents. The PMC rationale is verbatim.
- The example (拐杖、助行器、長柄或加粗握把用具、取物夾) and the note (扶手、加高馬桶座) all appear in the quotes.
- Fits the ra-hands summary and RA-2.4.

## activity-pacing: **minor**

**Checked:**
- The Table 1 row was confirmed in 2 documents.
- BSR 2025 quote (PMID 38621708, PMC12013823): verbatim, in the Fatigue section after question 14.
- The ACR rationale and statement are verbatim in PMC.
- The def and example are faithful.
- Fits the ra-fatigue-work summary, RA-5.1 and SJ-4.2.

**Problem (minor, precision): the note says the evidence is "很少", but ACR says it found none.**
The note reads 「目前研究證據很少，但一般認為安全；可請職能或物理治療師指導。」 ACR says "There was no evidence found for this PICO question." 「很少」 implies that some evidence was found.

The entry is also linked on the Sjögren page (SJ-4.2, BSR grade 2C), so the fix must be scoped to RA rather than saying 「沒有證據」 in general.

**Proposed** (36 CJK):
「類風濕性關節炎指引沒有找到相關研究，但認為一般安全；可請職能或物理治療師指導。」

Supporting quote (PMID 37227071, PMC10947582, Results → Rehabilitation recommendations), verbatim:

> "There was no evidence found for this PICO question. However, these interventions are generally safe and may help preserve physical function and manage fatigue. Proper instruction in these approaches by occupational or physical therapists as well as periodic reminders to employ them were suggested by the Patient Panel and Voting Panel."

## self-management: **OK**

**Checked:**
- EULAR 2021 definition, the two-components sentence, R2 and R3: all verbatim in PMC8458093.
- ACR statement: verbatim in PMC. The Table 1 first sentence was confirmed in 2 documents.
- The def omits "cultural" (disclosed by the drafters). That is acceptable simplification.
- Fits the ra-fatigue-work summary and RA-5.3.

**Optional evidence addition (no text change).** The Discussion of PMC8458093 directly supports 「自我管理不是要您獨自面對」:

> "The concept of self-management to some may imply needing to deal alone with a chronic condition."

PMID 33962964; location: Discussion, first paragraph. Its next sentence reads "Receiving adequate support from a variety of sources is crucial." In the extracted text the two sentences are glued together by a dropped reference mark, so quote only the first one.

## vocational-rehab: **OK**

**Checked:**
- Both ACR PMC statements are verbatim.
- Both Table 1 rows were confirmed in 2 documents.
- The def and note are faithful (安全和健康 for "safety and well-being").
- Fits RA-5.5.

**Optional:**
1. 「克服工作障礙」 could be read as "work disability". Consider 「克服就業阻礙」 (def would then be: 職業重建是幫助克服就業阻礙、支持就業的訓練課程，適合目前有工作或想要工作的人。, 36 CJK). The support is the same Table 1 quote: "Training programs to overcome barriers preventing successful employment."
2. A physician check, not sourced from PubMed: in Taiwan 職業重建服務 is a government service whose eligibility may be restricted. No PubMed source covers this, so the def should not mention it, but the site sentence RA-5.5 may deserve a local check.

## spinal-manipulation: **minor**

**Checked:**
- Rubinstein 2019 (PMID 30867144, PMC6396088): 3 Introduction quotes verbatim.
- ACR 2015 (PMC5123840) PICO 21 quotes: verbatim. "strongly against" and "Several case reports" are intact.
- ACR 2022 "not" rationale: verbatim.
- TRA 2020 (PMC7004149) quote: verbatim, located under Overarching Principle 3.
- Table 1 chiropractic row: confirmed in 2 documents.
- The def is faithful (high velocity, short amplitude, end of range, audible crack; 整脊 is chiropractic spinal manipulation).
- Fits RA-M4, AS-3.1 and AS-3.2.

**Note check (as requested).** The quote is verbatim in PMC, and 「病例報告」 correctly renders "case reports". The note does not claim that people without fusion are safe.

**Problems (minor, precision):**
- 「嚴重骨鬆」 drops "of the spine" ("advanced osteoporosis of the spine"). 骨鬆 is also colloquial: the site (AS-3.2) and the osteoporosis glossary entry use 骨質疏鬆.
- The note omits "particularly of the cervical spine" and "paraplegia". Both are worth keeping for safety, and the cervical part ties in with the RA-page context (ACR 2022 "cervical spine complications").

**Proposed** (44 CJK):
「曾有病例報告：脊椎已融合或嚴重脊椎骨質疏鬆的人整脊後（尤其是頸部）發生脊椎骨折、脊髓受傷，甚至癱瘓。」

**Minimal alternative:**
「脊椎已融合或嚴重脊椎骨質疏鬆的人，曾有扳動後脊椎骨折、脊髓受傷的病例報告。」

Supporting quote (PMID 26401991, PMC5123840, Recommendations C, PICO 21, Evidence and rationale), verbatim:

> "Several case reports of spine fractures, spinal cord injury, and paraplegia following chiropractic spinal manipulation, particularly of the cervical spine in patients with spinal fusion or advanced osteoporosis of the spine, have been reported"

## cervical-traction: **minor**

**Checked:**
- Cochrane 2008 (PMID 18646151) plain-language-summary quote: verbatim in the abstract field of PMC13429286.
- TRA quote: verbatim (statement accompanying Recommendation 4).
- The def is faithful. Leaving out the source's "lying on their back" is fine.
- Fits AS-3.1.

**Problem (minor):** 「可能較脆弱」 understates "often have fragile … spines". The site's AS-3.1 says 「脊椎常較脆弱」.

**Proposed** (27 CJK):
「僵直性脊椎炎患者的脊椎常較脆弱，台灣共識建議避免頸椎牽引。」

Supporting quote (PMID 31777200, PMC7004149), verbatim:

> "AS patients often have fragile and osteoporotic spines that can develop spinal fractures or dislocations from only mild trauma, and therefore contact sports, cervical traction, and spinal manipulation should be avoided."

## contact-sports: **minor**

**Checked:**
- Kichloo 2021 (PMID 33443051) definition: verbatim in the PubMed abstract. The metadata is correct: J Investig Med 69(3):781-784, e-published Dec 2020.
- TRA quote: verbatim.
- The def and the example 籃球、足球 are in the quote.
- Fits AS-3.1 and AS-M1.

**Problem (minor):** the same 「可能較脆弱」 understatement as cervical-traction.

**Proposed** (30 CJK):
「僵直性脊椎炎的脊椎常較脆弱，輕微外力就可能骨折，台灣共識建議避免。」

The support is the same TRA quote (PMID 31777200), above.

Source-tier remark (optional): the def comes from a Tier-3 narrative review about anticoagulation. No better accessible PubMed definition was found, which matches the drafters' note.

## flare-plan: **minor**

**Checked:**
- NICE NG65 1.3.4 and 1.3.5: my WebFetch pass matches the glossary quotes verbatim. They are not machine-checkable; see cross-cutting 2 and 4.
- The def, example and note are faithful.
- Fits AS-1.T, the axspa-support summary and AS-5.2.

**Problem (minor, safety wording).** 「可能的藥物調整」 could be read as permission to change medicines yourself during a flare. In NICE it is information that health professionals provide when discussing the plan. The site's AS-5.2 leaves medicines out.

**Proposed example** (34 CJK):
「內容可包括聯絡誰、自我照護、疼痛與疲倦處理，以及醫療團隊說明的可能藥物調整」

Supporting quote, NICE NG65 Rec 1.3.5 (PMID 28350428; WebFetch, confirmed this session):

> "When discussing any flare management plan, provide information on: … potential changes to medicines"

**Optional note polish** (35 CJK), because 「因應對…的影響」 is awkward:
「自我照護例如運動、伸展和關節保護；也包括如何處理發作對日常生活和工作的影響。」

Supporting quote, same recommendation: "self-care (for example, exercises, stretching and joint protection); … managing the impact on daily life and ability to work."

## cbt: **OK**

**Checked:**
- Cochrane 2020 (PMID 32794606) two plain-language-summary sentences: verbatim in the abstract field of PMC7437545.
- ACR Table 1 CBT row: confirmed in 2 documents. The ACR statement is verbatim in PMC.
- EULAR 2021 R3 text: verbatim in PMC8458093.
- Fits RA-5.4 and SL-4.3.

**Note check (as requested).** 「常由心理師或心理治療師提供，也有受過這項訓練的護理師。」 faithfully renders "often delivered by psychologists/psychotherapists, but also by some nurse specialists who have done a course in CBT". 「也有」 conveys "some". Rendering "nurse specialists" as 護理師 is a safe localisation, because Taiwan's 專科護理師 is a different licensed role.

**Optional polish** (29 CJK; it completes the verb and keeps "some" and "course"):
「常由心理師或心理治療師提供，也有一些上過相關課程的護理師提供。」

The support is the same EULAR quote (PMID 33962964).

## psychosocial: **OK**

**Checked:**
- Poort 2017 (PMID 28708236) definition: verbatim in the PubMed abstract (Selection criteria).
- EULAR 2024 (PMID 37433575) abstract sentence: verbatim.
- The two EULAR 2024 text quotes: my WebFetch matches (not machine-checkable; no PMC copy).
- EULAR 2021 "CBT is a psychosocial intervention": verbatim in PMC.
- The def is faithful (想法、情緒、行為、人際互動). 「非藥物」 rests on EULAR 2024 being a non-pharmacological guideline, which is reasonable.
- The examples match the site's SL-4.3.

## complementary: **minor**

**Checked:**
- Wieland 2011 Box 1 IOM definition: verbatim in PMC3196853. PubMed lists no DOI, which is correct.
- NICE NG100 1.8.9 and 1.8.10: my WebFetch matches.
- The def is a faithful simplification ("politically dominant health system" rendered as 主流醫療體系).
- Fits RA-M1, both the belief and the fact.

**Problem 1 (minor, precision):** 「長期效果的證據很少」 understates NICE's "little **or no** evidence".

**Proposed note** (31 CJK):
「有些可能短期緩解症狀，但長期效果的證據很少或沒有，不應取代正規治療。」

**Problem 2 (minor, verifiability):** the note rests only on WebFetch, but a machine-checkable PubMed/PMC copy of the same [2009] recommendation exists. Suggest adding it as a source and an evidence item:

- Source: Deighton C, O'Mahony R, Tosh J, Turner C, Rudolf M. Management of rheumatoid arthritis: summary of NICE guidance. BMJ 2009;338:b702. PMID 19289413; doi:10.1136/bmj.b702; PMC3266846 (metadata checked).
- Location: section "Diet and complementary therapies"; access: PMC full text. Verbatim:

> "Inform those wishing to try complementary therapies that little or no evidence exists for their long term efficacy and that although some may provide short term symptomatic benefit, complementary therapies should not replace conventional treatment."

**Problem 3 (minor, label):** 「IOM・定義」 has no year, unlike other labels, and IOM is unexplained. Suggest 「IOM 2005・定義」. The PMC box cites "[Institute of Medicine, 2005]".

**Optional:** Wieland 2011 also quotes the MeSH definition of "complementary therapies", an exact term match: "Therapeutic practices which are not currently considered an integral part of conventional allopathic medical practice." The current relative (IOM) definition handles Taiwan's licensed Chinese medicine better, so keeping it is reasonable.
