"""Fixes from the independent verification round (verify_*.md, 2026-10-07).

Each item may set fields (def/example/note/term/aliases/label/confidence/en), drop evidence rows
(by PMID or by quote prefix), add evidence rows and sources, and rewrite reviewer notes.
Applied by merge.py after the editorial EDITS.
"""

SRC = {
    '19289413': {'short': 'NICE 2009 類風濕性關節炎指引摘要（BMJ）',
                 'citation': "Deighton C, O'Mahony R, Tosh J, Turner C, Rudolf M. Management of rheumatoid arthritis: summary of NICE guidance. BMJ 2009;338:b702.",
                 'pmid': '19289413', 'doi': '10.1136/bmj.b702'},
    '26641646': {'short': '歐洲肥胖處理指引 2015（EASO）',
                 'citation': 'Yumuk V, et al. European Guidelines for Obesity Management in Adults. Obes Facts 2015;8(6):402-24.',
                 'pmid': '26641646', 'doi': '10.1159/000442721'},
    '39824205': {'short': 'Lancet 委員會 2025 臨床肥胖定義',
                 'citation': 'Rubino F, et al. Definition and diagnostic criteria of clinical obesity. Lancet Diabetes Endocrinol 2025;13(3):221-262.',
                 'pmid': '39824205', 'doi': '10.1016/S2213-8587(24)00316-4'},
    '41618370': {'short': '巴西風濕病學會 2026 生物製劑立場聲明',
                 'citation': 'Pereira PC, et al. Position statement of the Biotechnology Committee of the Brazilian Society of Rheumatology on the interchangeability of originator and biosimilar biologics in immune-mediated rheumatic diseases. Adv Rheumatol 2026;66(1).',
                 'pmid': '41618370', 'doi': '10.1186/s42358-026-00523-5'},
    '36832130': {'short': '2023 薦腸關節解剖與影像回顧',
                 'citation': 'Ulas ST, Diekhoff T, Ziegeler K. Sex Disparities of the Sacroiliac Joint: Focus on Joint Anatomy and Imaging Appearance. Diagnostics (Basel) 2023;13(4):642.',
                 'pmid': '36832130', 'doi': '10.3390/diagnostics13040642'},
    '7667647': {'short': '1995 急性前葡萄膜炎回顧',
                'citation': 'Careless DJ, Inman RD. Acute anterior uveitis: clinical and experimental aspects. Semin Arthritis Rheum 1995;24(6):432-41.',
                'pmid': '7667647', 'doi': '10.1016/s0049-0172(95)80011-5'},
    '35602489': {'short': '2022 乾燥症針灸隨機對照試驗',
                 'citation': "Zhou X, et al. Efficacy and Safety of Acupuncture on Symptomatic Improvement in Primary Sjögren's Syndrome: A Randomized Controlled Trial. Front Med (Lausanne) 2022;9:878218.",
                 'pmid': '35602489', 'doi': '10.3389/fmed.2022.878218'},
}


def ev(quote, pmid, location, supports, access='PMC full text', doi='', pmcid=''):
    return {'quote': quote, 'location': location, 'access': access, 'pmid': pmid, 'doi': doi,
            'pmcid': pmcid, 'supports': supports}


POST = {
    # ---------- g1 exercise ----------
    'aerobic': {
        'drop_pmids': ['38580348', '3920711'],
        'rn_replace': [('註解中「運動」與「身體活動」的區別依 Caspersen 1985 摘要與 2024 國際共識（Blaess）。', '')],
    },
    'muscle-strengthening': {
        'example': '舉啞鈴、拉彈力帶、用自身體重當阻力，或爬樓梯、從椅子上站起來',
        'add_ev': [ev('Muscle-strengthening activities may incorporate weights, elastic bands or using body weight for resistance training.',
                      '38580348', 'Blaess 2024, statement text (exercise types)', 'example（啞鈴、彈力帶、用自身體重當阻力）',
                      doi='10.1136/rmdopen-2024-004171', pmcid='PMC11002419')],
    },
    'weight-bearing': {
        'example': '走路、太極拳、爬樓梯、跳舞',
        'note': '這類活動對骨骼施力，有助骨骼強壯；開始跑步、舉重等新運動前，宜先請醫師評估，以免受傷。',
        'add_ev': [
            ev('Bone-strengthening (also called weight-bearing or weight-loading) activities produce a force on the bones of the body that promotes bone growth and strength.',
               '30418471', 'Key Concepts, Bone-Strengthening Activity', 'note（對骨骼施力、有助骨骼強壯）',
               doi='10.1001/jama.2018.14854', pmcid='PMC9582631'),
            ev('To avoid injury, patients should be evaluated before initiating a new exercise program, particularly one involving compressive or contractile stressors (such as running or weightlifting).',
               '35478046', 'Universal bone health recommendations > Regular weight-bearing and muscle-strengthening physical activity', 'note（開始跑步、舉重等新運動前先評估）',
               doi='10.1007/s00198-021-05900-y', pmcid='PMC9546973'),
        ],
        'rn_append': '查核後修訂：此詞條只連結在「類固醇與骨骼保健」卡片；同一份 BHOF 指引把慢跑、網球列為骨質疏鬆者可能受傷的活動，所以例子刪去這兩項，補充改為「先請醫師評估」。',
    },
    'multicomponent': {
        'term': '多元活動（有氧、肌力與平衡）',
        'example': '走路、舉啞鈴，再加上倒退走、側走或單腳站等平衡練習',
        'note': '跳舞、瑜伽、太極拳、園藝等活動常同時包含多種類型的身體活動，也可算是多元活動。',
    },
    'mind-body': {'loc_replace': ('Table 1', "Table 1 ('Descriptions and examples of interventions included in the integrative management of rheumatoid arthritis guideline'); not in the PMC extraction; WebFetch: PMC page ×2 (drafters) and CDC Stacks author manuscript p.19 ×2 (verifier), identical wording")},
    'aquatic': {'loc_replace': ('Table 1', "Table 1 ('Descriptions and examples of interventions included in the integrative management of rheumatoid arthritis guideline'); not in the PMC extraction; WebFetch: PMC page ×2 (drafters) and CDC Stacks author manuscript p.19 ×2 (verifier), identical wording")},
    'range-of-motion': {'label': 'AHA 2020、ACSM 2011・綜合說明'},
    'passive-therapy': {'def': '被動治療指按摩、超音波治療、熱療這類治療；主動運動指自己動起來做的運動，例如有人督導的運動訓練。'},
    'perceived-exertion': {'label': 'WHO 2020、美國身體活動指引・定義'},

    # ---------- g2 rehab ----------
    'physical-therapy': {
        'note': '',
        'drop_pmids': ['18254008'],
        'rn_replace': [('Note is AS-specific (Cochrane 2008, search to Jan 2007). ', '')],
        'rn_append': '查核後修訂：原補充（物理治療有助改善脊椎活動、體能與疼痛）引自 2008 年 Cochrane 回顧的背景句，不是研究結論；2019 年 Cochrane 回顧對脊椎活動度的效果仍不確定，所以刪除補充。',
    },
    'activity-pacing': {
        'note': '一般認為安全；可請職能或物理治療師指導。',
        'add_ev': [ev('There was no evidence found for this PICO question. However, these interventions are generally safe and may help preserve physical function and manage fatigue. Proper instruction in these approaches by occupational or physical therapists as well as periodic reminders to employ them were suggested by the Patient Panel and Voting Panel.',
                      '37227071', 'Results → Rehabilitation recommendations (activity pacing)', 'note（一般認為安全；由職能或物理治療師指導）',
                      doi='10.1002/art.42507', pmcid='PMC10947582')],
    },
    'self-management': {
        'add_ev': [ev('The concept of self-management to some may imply needing to deal alone with a chronic condition.',
                      '33962964', 'Discussion, first paragraph', 'note（自我管理不是要您獨自面對）',
                      doi='10.1136/annrheumdis-2021-220249', pmcid='PMC8458093')],
    },
    'vocational-rehab': {'def': '職業重建是幫助克服就業阻礙、支持就業的訓練課程，適合目前有工作或想要工作的人。'},
    'spinal-manipulation': {
        'note': '曾有病例報告：脊椎已融合或嚴重脊椎骨質疏鬆的人整脊後（尤其是頸部）發生脊椎骨折、脊髓受傷，甚至癱瘓。',
        'supports_replace': [('def: 整脊屬於這類手法; note', 'def: 整脊屬於這類手法; note（病例報告：骨折、脊髓受傷、癱瘓；尤其頸部）')],
    },
    'cervical-traction': {'note': '僵直性脊椎炎患者的脊椎常較脆弱，台灣共識建議避免頸椎牽引。'},
    'contact-sports': {'note': '僵直性脊椎炎的脊椎常較脆弱，輕微外力就可能骨折，台灣共識建議避免。'},
    'flare-plan': {
        'example': '內容可包括聯絡誰、自我照護、疼痛與疲倦處理，以及醫療團隊說明的可能藥物調整',
        'note': '自我照護例如運動、伸展和關節保護；也包括如何處理發作對日常生活和工作的影響。',
    },
    'cbt': {'note': '常由心理師或心理治療師提供，也有一些上過相關課程的護理師提供。'},
    'complementary': {
        'note': '有些可能短期緩解症狀，但長期效果的證據很少或沒有，不應取代正規治療。',
        'label': 'IOM 2005・定義（文獻引述）',
        'add_ev': [ev('Inform those wishing to try complementary therapies that little or no evidence exists for their long term efficacy and that although some may provide short term symptomatic benefit, complementary therapies should not replace conventional treatment.',
                      '19289413', 'Diet and complementary therapies', 'note（短期緩解；長期效果證據很少或沒有；不應取代正規治療）',
                      doi='10.1136/bmj.b702', pmcid='PMC3266846')],
    },
    'hand-therapist': {'supports_replace': [('def (all parts) and note (CHT)', 'def (all parts)')]},

    # ---------- g3 diet / sun ----------
    'uric-acid': {'label': '文獻回顧與 ACR 2020・定義'},
    'hfcs': {
        'def': '高果糖玉米糖漿是由果糖和葡萄糖組成的液體甜味劑，用來取代一般砂糖（蔗糖），例如加在含糖飲料裡。',
        'supports_replace': [('def：常加在含糖飲料裡；note：果糖是植物中常見的單醣，也是 HFCS 的主要成分。', 'def：例如加在含糖飲料裡。')],
    },
    'alcohol-serving': {'note': '各國對「一份酒」的定義不同，這裡是該美國研究採用的份量。'},
    'special-diets': {
        'def': '生酮：大幅少吃醣類。無麩質：不吃小麥、黑麥、大麥等含麩質穀類。純素：不吃任何動物性食物，包括蛋和奶。間歇性斷食：反覆斷食，每次最長48小時。',
        'drop_quote_prefix': ['TRE was finally defined'],
        'rn_replace': [('The def (84 characters) is close to the 90-character limit; physician may prefer to split it into four separate glossary items.', '')],
    },
    'saturated-fat': {
        'confidence': 'Medium (Tier 3: Cochrane plain language summary and a Nutr J review; no site-cited guideline defines saturated fat)',
        'rn_replace': [("Campos 2018 is a drug-delivery review, a weak authority for nutrition; it is used only for the chemistry/'solid at room temperature' phrase, which the physician may delete. ", '')],
    },
    'processed-food': {'note': '指引沒有定義這個詞；這裡借用一套依工業加工程度分類食品的系統（NOVA）對「超加工食品」的說明。'},
    'bmi': {
        'label': 'EASO 2015、WHO 2004・定義',
        'drop_pmids': ['35254432'],
        'add_ev': [
            ev('In clinical practice, the body fatness is usually estimated by BMI. BMI is calculated as measured body weight (kg) divided by measured height squared',
               '26641646', 'Definition of obesity (PMC full text)', 'def（BMI 的算法）', doi='10.1159/000442721', pmcid='PMC5644856'),
            ev('overweight (also termed pre-obesity) by a BMI between 25 and 29.9', '26641646', 'Definition of obesity (PMC full text)',
               'note（25 以上為過重）', doi='10.1159/000442721', pmcid='PMC5644856'),
            ev('According to WHO, an adult with a BMI of 30 … or higher is considered to have obesity.', '39824205',
               'PMC full text ("kg/m²" glued in the PMC extraction, replaced by …)', 'note（30 以上為肥胖）',
               doi='10.1016/S2213-8587(24)00316-4', pmcid='PMC11870235'),
        ],
        'rn_append': '查核後修訂：BMI 算法與 30 以上為肥胖改以 EASO 2015 指引與 2025 Lancet 委員會為出處（原出處為囊腫性纖維化研究摘要，已刪除）。台灣國健署切點（24、27）沒有 PubMed 收錄的出處，請醫師決定是否另加。',
    },
    'spf': {'def': 'SPF（防曬係數）表示防曬乳對UVB的防護力，是以「讓皮膚曬紅所需的紫外線量」測出來的；UVA的防護要另看UVA防護等級標示。'},
    'uva-uvb': {
        'note': '在紅斑性狼瘡，兩種都可能促成皮膚病灶；英國狼瘡指引建議用同時防 UVA 和 UVB 的防曬乳。',
        'rn_replace': [("Wavelength boundaries are as stated by Kim & Chong 2013; other sources may use slightly different boundaries for UVA/UVB, so the def says 約 (about). ",
                        "Wavelength boundaries (UVA 320–400 nm, UVB 290–320 nm, Kim & Chong 2013) are kept in the evidence; the def gives no numbers. ")],
    },
    'broad-spectrum': {
        'note': 'SPF 主要代表 UVB 防護、看不出 UVA；UVA 要另看 UVA 防護等級標示。',
        'add_ev': [ev('The sun protection factor (SPF) is primarily a measure of UVB protection against erythema and does not quantify protection from UVA, which is the major component of solar UVR.',
                      '41968398', 'Abstract', 'note（SPF 主要代表 UVB、看不出 UVA）', access='abstract',
                      doi='10.1111/phpp.70092', pmcid='PMC13071116')],
    },
    'photosensitivity': {
        'add_ev': [ev('several photoprovocation studies have clearly demonstrated that the onset of true photosensitive reactions is often delayed',
                      '23281691', "Section 'Photosensitivity in lupus patients'", 'def（皮疹常延遲出現）',
                      doi='10.1111/phpp.12018', pmcid='PMC3539182')],
    },
    'uva-rating': {
        'def': '防曬品標示 UVA 防護力高低的方式，各地不同：亞洲常見 PA 等級，「+」越多防護越高；英國則用 UVA 標誌或 1 到 5 顆星。',
        'example': 'PA+、PA++、PA+++、PA++++',
        'note': 'PA+++ 代表 UVA 防護「高」，PA++++ 代表「很高」。',
    },

    # ---------- g4 drugs ----------
    'oral-glucocorticoid': {'note': '長期使用對健康有不良影響（例如骨質疏鬆），指引主張盡量減少用量；調整劑量請和醫師討論，不要自行停藥。'},
    'immunosuppressant': {
        'add_ev': [
            ev('For patients with RMD, continuing immunosuppressive medications other than methotrexate around the time of influenza vaccination is conditionally recommended.',
               '36597813', 'Recommendations (influenza vaccination)', 'example（methotrexate 屬免疫抑制藥物）', doi='10.1002/acr.25045', pmcid='PMC10291822'),
            ev('The AAP Red Book () and the Infectious Diseases Society of America () define low-level immunosuppression as methotrexate ≤0.4 mg/kg/week, azathioprine ≤3 mg/kg/day, prednisone <20 mg/day (or <2 mg/kg/day for patients weighing <10 kg), or alternate-day glucocorticoid therapy ().',
               '36597813', 'Live attenuated vaccines section ("()" = stripped citation markers)', 'example（azathioprine、類固醇屬免疫抑制）', doi='10.1002/acr.25045', pmcid='PMC10291822'),
        ],
    },
    'biologic': {
        'label': '巴西風濕病學會 2026・定義',
        'drop_pmids': ['28903544'],
        'add_ev': [ev('Biological medicines (or immunobiologics) are large, structurally complex molecules produced by living cells [,].',
                      '41618370', 'Introduction, first sentence ("[,]" = stripped citation markers)', 'def（用活細胞製造、結構很複雜）',
                      doi='10.1186/s42358-026-00523-5', pmcid='PMC13488687')],
        'rn_append': '查核後修訂：定義的主要出處改為巴西風濕病學會 2026 共識聲明（Tier 2）；原出處為有藥廠作者的綜論，已刪除。',
    },
    'antimalarial': {
        'note': '指引建議使用期間接受眼睛檢查，監測可能的視網膜副作用。',
        'drop_quote_prefix': ['combined antimalarials'],
    },
    'mtx-lef': {
        'label': 'EULAR 2025・分類',
        'drop_quote_prefix': ['Initially, MTX'],
        'rn_replace': [('「指引建議治療一開始先用 methotrexate」: EULAR recommends MTX together with (short-term) glucocorticoids.', '')],
    },
    'nsaid': {
        'note': '醫師為預防血栓開的低劑量阿斯匹靈，不一定要停用；請勿自行停藥，先和醫師討論。',
        'drop_quote_prefix': ['Non‐IgE‐mediated reactions to drugs'],
        'add_ev': [ev('However, if low‐dose acetylsalicylic acid is needed as an antithrombotic treatment, it is not always necessary to abstain from using this drug.',
                      '41649409', 'Section 4 (medications that may aggravate CSU)', 'note（低劑量阿斯匹靈不一定要停用）',
                      doi='10.1111/all.70210', pmcid='PMC13466004')],
        'rn_replace': [('「換藥前請先問醫師」 is an editorial safety phrase, not from a source.', '「請勿自行停藥，先和醫師討論」 is an editorial safety phrase (same as site UR-1.3). The guideline names paracetamol and COX-2 inhibitors as safer options in CSU; the site does not name safer analgesics (physician decision), so that quote is not shown here.')],
    },
    'low-dose-aspirin': {'note': '蕁麻疹病人不一定要停用；醫師可能暫改用其他抗血栓藥4週，判斷是否和蕁麻疹有關；請勿自行停藥。'},
    'antihistamine': {
        'term': '抗組織胺',
        'aliases': ['較不會嗜睡的抗組織胺', '抗組織胺'],
        'rn_replace': [("The guideline says 2nd-generation H1-antihistamines are \"minimally or nonsedating\", so the site's 「不會嗜睡」 slightly overstates; consider 「較不會嗜睡」. ",
                        "The guideline says 2nd-generation H1-antihistamines are \"minimally or nonsedating\"; the site now says 「較不會嗜睡」. ")],
    },
    'ult': {'access_fix': {'0': 'PMC abstract'}},
    'flare-medicine': {'def': '痛風發作時用來壓下關節發炎和疼痛的藥，第一線是 colchicine（秋水仙素）、消炎止痛藥（NSAIDs）或類固醇；發作後及早使用效果較好。',
                       'exclude_pages': ['common', 'urticaria', 'ra', 'axspa', 'sle', 'sjogren']},
    'non-live-vaccine': {
        'note': '部分藥物會讓疫苗反應變弱（但通常不會完全沒效）；如果可以，最好在開始免疫抑制治療前接種。',
        'add_ev': [ev('If possible, vaccinations should be administered prior to immunosuppressive drugs, but necessary treatment should never be postponed.',
                      '35725297', 'Abstract', 'note（如果可以，最好在免疫抑制治療前接種；必要的治療不應延後）', access='abstract',
                      doi='10.1136/annrheumdis-2022-222574')],
    },
    'live-vaccine': {
        'def': '活性減毒疫苗含有活的、但已減弱的病原；正在使用免疫抑制藥物的人接種後，可能被疫苗裡的病原感染，所以通常建議延後或謹慎接種。',
        'add_ev': [ev('In addition, studies were included that reported on the live-attenuated vaccines against Measles, Mumps and Rubella (MMR, …), Varicella Zoster Virus (VZV, 5 studies) (–), one study which included 1 patient with oral polio vaccine () and one case report on the Bacillus Calmette-Guérin (BCG) vaccine ().',
                      '35874582', 'Results ("()" = stripped citation markers)', 'def（活性減毒疫苗也包括細菌疫苗，例如卡介苗，所以寫「病原」）',
                      doi='10.3389/fped.2022.910026', pmcid='PMC9298835')],
    },
    'pneumococcal': {'def': '肺炎鏈球菌疫苗是預防肺炎鏈球菌感染的非活性疫苗。肺炎鏈球菌是引起肺炎等呼吸道感染的常見細菌，也可能造成血液感染和腦膜炎。'},
    'eye-ointment': {
        'drop_quote_prefix': ['Several of the commercially available eye ointments', 'Consider vitamin A containing'],
        'access_fix': {'0': 'WebFetch (publisher page ard.bmj.com/content/79/1/3; 3 passes in the research phase + 2 passes on 2026-10-07, identical)'},
        'rn_replace': [('Re-confirmation was attempted this session, but WebFetch permission was not granted, so the physician should check it against the published article (Ann Rheum Dis 2020;79:3-18, ocular dryness recommendation). ',
                        'Re-confirmed by the verifier on 2026-10-07 (2 WebFetch passes of the publisher page, identical wording); still not machine-checkable. ')],
    },

    # ---------- g5a allergy / urticaria ----------
    'autoimmune': {
        'note': '自體抗體也可能出現在健康的人身上；單憑自體抗體，不能診斷自體免疫疾病。',
        'drop_quote_prefix': ['It is also important to explain to the patient that CU is predominantly', 'In more than 50% of CSU patients'],
        'add_ev': [ev('Antibodies against self-antigens are also found in cancer, during massive tissue damage and even in healthy subjects.',
                      '19963079', 'Abstract', 'note（健康的人也可能有自體抗體）', access='abstract', doi='10.1016/j.autrev.2009.12.002')],
        'rn_append': '查核後修訂：此詞條也連結在疫苗卡片（CM-5.1），原補充（慢性蕁麻疹主要和自體免疫有關、超過一半自發型和自體抗體有關，GALEN 2026 §3.3、§4）放在那裡離題，改為兩頁都適用的說明；蕁麻疹頁的 UR-3.1 本身已寫明慢性蕁麻疹和自體免疫有關。',
    },
    'solar-urticaria': {'def': '日光性蕁麻疹是誘發型蕁麻疹的一種：皮膚照到光線後幾分鐘內，就冒出會癢的紅斑和膨疹；引發的光線多為紫外線A（UV-A）或可見光。'},
    'stridor-wheeze': {'def': '咻咻聲是呼吸時像吹口哨的聲音，多在吐氣時出現，因為支氣管收縮；喘鳴在這裡指吸氣時發出的尖銳高音，因為上呼吸道阻塞。'},
    'angioedema': {
        'note': '可和膨疹一起或單獨出現；只有腫脹時請醫師找原因。喉嚨腫脹可能危及生命。',
        'add_ev': [ev('Angioedema of the upper airway can be life threatening.', '23282382', 'Definition and Classification',
                      'note（喉嚨腫脹可能危及生命）', doi='10.1097/WOX.0b013e3182758d6c', pmcid='PMC3651155')],
    },
    'anaphylaxis': {
        'aka': 'anaphylaxis',
        'supports_replace': [('note：寒冷性蕁麻疹可能引起嚴重過敏反應（alias「全身性反應」的語境）', 'note：寒冷性蕁麻疹病人全身受冷可能發生')],
        'rn_replace': [("Alias 全身性反應 (site UR-2.3) renders 'systemic reactions' in the AAAAI/ACAAI 2014 sentence cited for UR-2.3 (claim C51 in /home/claude/research/urticaria.md). WAO 2012 and Bizjak 2025 describe these as systemic/anaphylactic reactions, so linking the alias here is reasonable, but 'systemic reaction' can be broader than anaphylaxis; consider rewording UR-2.3 to 「全身性過敏反應」 or not linking that alias. ",
                        "Alias 全身性反應 removed. UR-2.3 now reads 「…可能引起全身性的過敏反應…」 (AAAAI/ACAAI 2014 'systemic reactions') and is not linked to this entry; its popup is cold-urticaria. ")],
        'src_short': {'33204386': 'WAO 2020 嚴重過敏反應指引', '31719946': 'WAO 嚴重過敏反應委員會 2019 定義修訂'},
    },
    'uas7': {'term': '蕁麻疹活動分數（UAS7）'},
    'cold-urticaria': {
        'rn_replace': [('Site UR-2.3 (swimming → 全身性反應)', 'Site UR-2.3 (swimming → 全身性的過敏反應)')],
        'supports_replace': [('note：部分病人會出現寒冷誘發的嚴重過敏反應（全身性反應）', 'note：部分病人會出現寒冷誘發的嚴重過敏反應')],
    },

    # ---------- g5b conditions ----------
    'axspa': {
        'def': '一種主要影響脊椎和薦腸關節（脊椎和骨盆之間的關節）的慢性發炎性疾病；包括 X 光看得到結構破壞的僵直性脊椎炎，以及 X 光看不到這種破壞的非放射線型。',
        'add_ev': [
            ev('The sacroiliac joint (SIJ) is the articulation surface between the sacrum and the ilium and plays an important role in the distribution of axial load between the spine and pelvis',
               '36832130', 'Introduction', 'def（薦腸關節＝脊椎和骨盆之間的關節）', doi='10.3390/diagnostics13040642', pmcid='PMC9955570'),
            ev('Not all people with axSpA will undergo structural progression detectable on radiographs (radiographic progression)',
               '40199504', 'Background', 'def（非放射線型不一定會出現 X 光可見的破壞）', doi='10.1093/rheumatology/keaf089', pmcid='PMC12107049'),
        ],
        'supports_replace': [('example：急性前葡萄膜炎、乾癬、發炎性腸道疾病', 'note：其他關節、肌腱附著處；急性前葡萄膜炎、乾癬、發炎性腸道疾病'),
                             ('def：包括僵直性脊椎炎與非放射線型；note：由風濕科醫師確認診斷', 'def：包括僵直性脊椎炎與非放射線型')],
        'rn_replace': [('The gloss 「骨盆」 for 薦腸關節 (sacroiliac joint) is an anatomical explanation not printed in the quotes; please check. ',
                        'The gloss 「脊椎和骨盆之間的關節」 for 薦腸關節 rests on Ulas 2023 (sacrum–ilium articulation between spine and pelvis). ')],
    },
    'uveitis': {
        'def': '葡萄膜炎是眼球內部的發炎。前葡萄膜炎是眼睛前段（虹膜等處）的發炎，虹彩炎（虹膜發炎）就屬於這一類；急性型會突然發作，常只有一眼，也可能兩眼輪流復發。',
        'note': '屬急症，要盡快看眼科；延誤治療，有些人可能出現青光眼或視力嚴重受損。',
        'add_ev': [ev('Acute anterior uveitis (AAU) or iritis is an inflammatory disorder of the anterior structures of the eye that may be associated with a number of disease entities.',
                      '7667647', 'Abstract', 'def（虹彩炎屬於急性前葡萄膜炎）', access='abstract', doi='10.1016/s0049-0172(95)80011-5')],
    },
    'spinal-fusion': {
        'example': '融合最嚴重時，影像上會呈現特殊的樣子，稱為「竹節狀脊椎」。',
        'note': '僵直性脊椎炎的脊椎常較脆弱，輕微外傷就可能骨折。',
        'add_ev': [ev('Its most advanced form has a characteristic imaging appearance known as “bamboo spine”',
                      '37944938', 'New bone formation in the spine – Ankylosis', 'example（融合最嚴重時的影像樣子：竹節狀脊椎）',
                      doi='10.1055/a-2193-1970', pmcid='PMC11111289')],
    },
    'lupus-nephritis': {'note': '每次回診都要驗尿，這是發現腎炎的必要檢查。'},
    'neonatal-lupus': {
        'note': '皮疹、血球或肝指數異常多為短暫，常隨寶寶體內媽媽的抗體消失而好轉；心臟傳導阻滯則多半無法恢復。',
        'add_ev': [ev('The most severe manifestation is congenital heart block (CHB), which occurs in structurally normal fetal hearts, is most often complete and irreversible',
                      '42680608', 'Abstract', 'note（心臟傳導阻滯多半無法恢復）', access='abstract', doi='10.1016/j.revmed.2026.08.006')],
    },
    'comorbidity': {'example': '痛風的共病包括心血管疾病、慢性腎臟病、尿路結石、糖尿病等。'},
    'cvd': {
        'def': '心臟和血管的疾病，主要是缺血性心臟病和中風，也包括動脈粥狀硬化、心肌梗塞、周邊血管疾病與心臟衰竭。',
        'supports_replace': [('def：包含的疾病；note：2–3 倍', 'def：包含的疾病')],
        'rn_replace': [("The note’s 2–3 倍 is SLE-specific (matches SL-5.4 context). ", '')],
    },
    'ckd': {'def': '腎臟受損，或腎臟的過濾功能（腎絲球過濾率，eGFR）低於 60，持續 3 個月以上，不論是什麼原因。'},
    'urolithiasis': {'supports_replace': [('note', 'background (stones are common and often recur; not shown)')]},
    'mgd': {
        'note': '乾燥症的眼睛不適，除了淚水不足，也和瞼板腺功能不良、眼睛表面發炎有關。',
        'add_ev': [ev('SD is associated with complex eye disease [] with aqueous tear deficiency, meibomian gland dysfunction [,] and surface inflammation contributing to the symptom load.',
                      '38621708', 'Eye section ("[]" = stripped citation markers)', 'note（淚水不足、瞼板腺功能不良、眼睛表面發炎）',
                      doi='10.1093/rheumatology/keae152', pmcid='PMC12013823')],
    },
    'night-sweats': {
        'def': '睡覺時出汗；很多沒有特別疾病的人也會有。',
        'note': '乾燥症病人若持續夜間盜汗，或有發燒、3 個月內體重減輕 10% 以上，請盡早回診。',
        'drop_pmids': ['36943212'],
        'supports_by_index': {'0': 'note：持續夜間盜汗、發燒、3 個月內體重減輕 10% 以上', '1': 'note：盡早回診檢查',
                              '2': 'def：睡覺時出汗；沒有相關疾病的人也常有', '3': 'def：不具特異性（很多人都有）'},
        'rn_replace': [('「全身濕透」 renders "drenching" (JAMA 2023 CLL review abstract). ', ''),
                       ('Mold 2012 (systematic review) notes the lack of a uniform definition.', 'van Meeuwen 2024 (PMID 39435709) notes the lack of a uniform definition.'),
                       ('describes B symptoms as fever >38°C, drenching night sweats and unexplained weight loss >10% within the preceding 6 months (as restated, e.g., in the abstract of PMID 37034003)',
                        'describes B symptoms as fever, drenching night sweats and unintentional weight loss >10% within the preceding 6 months (as restated in the abstract of PMID 37034003)')],
    },

    # ---------- g6 evidence / orgs ----------
    'guideline': {
        'def': '臨床指引是一套照護建議，目的是讓照護做到最好；建議依據有系統整理過的研究證據，並比較不同做法的好處與壞處。',
        'label': 'IOM 2011・定義（文獻引述）',
    },
    'meta-analysis': {
        'example': '2015年一篇統合分析，合併了10項研究（共1398名皮膚型狼瘡病人）的結果。',
        'add_ev': [ev('Individual study odds ratios were combined in the meta-analysis using a random effects model.',
                      '25648824', 'Abstract (Methods)', 'example（合併的是各研究的結果）', access='abstract', doi='10.1016/j.jaad.2014.12.025')],
    },
    'rct': {
        'term': '隨機對照試驗',
        'note': '隨機分組讓各組條件相近；設計良好時被視為評估治療效果的黃金標準，但人數少時結果較不精確。',
        'supports_replace': [('note（評估治療效果的標準方法）', 'note（設計良好時是評估治療效果的黃金標準）')],
    },
    'placebo': {
        'example': '一項乾燥症試驗中，針灸是和「假針灸」比較。',
        'add_ev': [
            ev('A placebo is a pill or liquid that looks like the new treatment but does not have any treatment value from active ingredients.',
               '25423149', 'Table 3, NIH row', 'def（假藥丸）', doi='10.1371/journal.pone.0113654', pmcid='PMC4244087'),
            ev("A total of 120 patients with primary Sjögren's syndrome were randomized in a parallel-group, controlled trial. Participants received acupuncture or sham acupuncture for the first 8 weeks, then were followed for 16 weeks thereafter.",
               '35602489', 'Abstract', 'example（乾燥症試驗：針灸和假針灸比較）', access='abstract', doi='10.3389/fmed.2022.878218', pmcid='PMC9121854'),
        ],
        'supports_replace': [('example；site usage SJ-M1', 'site usage SJ-M1（研究回顧中的針灸研究對象是放射治療後口乾的人）')],
    },
    'certainty': {
        'note': '確定性低，表示新研究很可能改變這個結果，結論也可能不同；「證據品質」是較早的說法，現在仍常用。',
        'add_ev': [ev('GRADE defines low quality evidence as evidence where further research is very likely to have an important influence on our confidence in the estimates, or is likely to change the estimate.',
                      '35654458', 'Methods (PMC full text)', 'note（新研究很可能改變結果）', doi='10.1136/rmdopen-2021-002167', pmcid='PMC9096533')],
        'dedupe': True,
    },
    'expert-consensus': {'def': '專家共識是一群專家討論後，對建議達成的共同意見；正式的共識方法通常會投票，同意的人要達到事先訂好的比例。'},
    'org-eular': {'def': '歐洲的風濕病學會聯盟，發表多份風濕病照護建議；英文全名已更改，縮寫仍是EULAR。'},
    'org-who': {'def': '世界衛生組織；網站引用它發表的資料，例如2020年的身體活動與久坐行為指引。'},
    'org-galen': {
        'def': '全球性的過敏與氣喘專業網絡；2026年國際蕁麻疹指引由它和其他幾個學術團體共同發起，有59國、107個學會的代表參與。',
        'add_ev': [ev('The guideline is an initiative of the Global Allergy and Asthma Excellence Network (GALEN) and its Urticaria and Angioedema Centers of Reference and Excellence (UCAREs and ACAREs), the European Dermatology Forum (EDF), the Asia Pacific Association of Allergy, Asthma and Clinical Immunology (APAAACI), the American Academy of Dermatology (AAD), the British Society for Allergy & Clinical Immunology (BSACI), and the Gulf Academy of Allergy and Clinical Immunology (GA2CI)',
                      '41649409', 'Introduction', 'def（和其他學術團體共同發起）', doi='10.1111/all.70210', pmcid='PMC13466004')],
    },
    'good-practice': {
        'def': '良好實務建議是指引裡「不分級」的建議：專家一致認為這樣做的好處明顯大於壞處，只是支持它的多是間接證據，所以不另評證據等級。',
        'example': '',
        'drop_pmids': ['37609066'],
    },
}


def apply(e, src_lookup):
    """Apply POST fixes to a merged entry dict in place."""
    p = POST.get(e['id'])
    if not p:
        return e
    for k in ('def', 'example', 'note', 'term', 'aliases', 'label', 'confidence', 'en', 'aka', 'exclude_pages'):
        if k in p:
            e[k] = p[k]
    if p.get('drop_pmids'):
        e['evidence'] = [x for x in e['evidence'] if str(x.get('pmid')) not in p['drop_pmids']]
        e['sources'] = [x for x in e['sources'] if str(x.get('pmid')) not in p['drop_pmids']]
    for pre in p.get('drop_quote_prefix', []):
        before = len(e['evidence'])
        e['evidence'] = [x for x in e['evidence'] if not x['quote'].startswith(pre)]
        assert len(e['evidence']) < before, (e['id'], 'no evidence row starts with', pre)
    for old, new in p.get('supports_replace', []):
        hit = False
        for x in e['evidence']:
            cur = x.get('supports', '')
            if cur == old:
                x['supports'] = new
                hit = True
            elif len(old) > 8 and old in cur:
                x['supports'] = cur.replace(old, new)
                hit = True
        assert hit, (e['id'], 'supports not found', old)
    for i, s in p.get('supports_by_index', {}).items():
        e['evidence'][int(i)]['supports'] = s
    for i, a in p.get('access_fix', {}).items():
        e['evidence'][int(i)]['access'] = a
    if p.get('loc_replace'):
        old, new = p['loc_replace']
        n = 0
        for x in e['evidence']:
            if x.get('access', '').startswith('WebFetch') and old in x.get('location', ''):
                x['location'] = new
                n += 1
        assert n, (e['id'], 'no WebFetch Table 1 row')
    for x in p.get('add_ev', []):
        if p.get('dedupe') and any(y['quote'].strip() == x['quote'].strip() for y in e['evidence']):
            continue
        e['evidence'].append(dict(x))
        pm = str(x['pmid'])
        if not any(str(s.get('pmid')) == pm for s in e['sources']):
            s = SRC.get(pm) or src_lookup.get(pm)
            assert s, (e['id'], 'no source record for', pm)
            e['sources'].append({k: s.get(k) for k in ('short', 'citation', 'pmid', 'doi')})
    for pm, short in p.get('src_short', {}).items():
        for s in e['sources']:
            if str(s.get('pmid')) == pm:
                s['short'] = short
    rn = e.get('reviewer_notes', '')
    for old, new in p.get('rn_replace', []):
        assert old in rn, (e['id'], 'rn text not found', old[:40])
        rn = rn.replace(old, new)
    if p.get('rn_append'):
        rn = (rn.rstrip() + ' ' + p['rn_append']).strip()
    e['reviewer_notes'] = rn
    return e
