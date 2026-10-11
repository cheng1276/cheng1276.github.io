"""Fixes from the independent verification of the new-page glossary terms (2026-10-11).

Reports: verification/verify_n1a_oa.md, verify_n1b_bone.md, verify_n2_labs.md, verify_n3_infection.md,
verify_n4_orgs.md. The research files (research/research_n*.json) are kept exactly as drafted; every change
the verifiers asked for is recorded here, in the same format as postfix.py, and applied by merge.py after
postfix.py. A few items also touch existing entries, because they now link from the new pages.

Every added evidence quote below was read verbatim in PubMed or PMC by the verifier who proposed it.
"""
import glob
import json
import pathlib

import postfix

HERE = pathlib.Path(__file__).resolve().parent

# Sources that no research file lists yet.
SRC = {
    '34527924': {'short': 'Öncel 2021 手部退化性關節炎石蠟浴與流體治療隨機試驗（Arch Rheumatol）',
                 'citation': 'Öncel A, Küçükşen S, Ecesoy H, Sodali E, Yalçin Ş. Comparison of efficacy of fluidotherapy and paraffin bath in hand osteoarthritis: A randomized controlled trial. Arch Rheumatol 2021;36(2):201-209 (epub 2020).',
                 'pmid': '34527924', 'doi': '10.46497/ArchRheumatol.2021.8123'},
    '40498227': {'short': 'BHOF 2025 骨折聯絡服務遠距教學計畫回顧（作者所屬單位）',
                 'citation': 'Patel AR, Laberee N, Medeiros AP. Impact of the BHOF FLS TeleECHO program: a review of role and outcomes. Arch Osteoporos 2025;20(1):75.',
                 'pmid': '40498227', 'doi': '10.1007/s11657-025-01557-w'},
}

# One short name per source wherever it appears (popups list sources publicly).
SHORT_FIX = {
    '35478046': 'BHOF 2022 骨質疏鬆預防與治療臨床指南（Bone Health and Osteoporosis Foundation；美國的骨骼健康與骨質疏鬆基金會）',
    '37816527': '加拿大骨鬆指引 2023（Osteoporosis Canada 2023 Guideline Update Group；加拿大骨質疏鬆組織的指引小組）',
    '40921943': 'NOGG 2024 英國骨質疏鬆症指引（National Osteoporosis Guideline Group；英國的骨質疏鬆指引小組）',
    '38724043': 'ESE/ES 2024 類固醇引起腎上腺功能不足指引（歐洲的內分泌學會與美國的內分泌學會）',
    '30324412': 'ESCEO/IOF 2019 歐洲停經後骨質疏鬆症指引',
    '24126457': 'EASI/IUIS 2014 抗核抗體檢驗國際建議',
    '29405329': 'AASLD 2018 B 型肝炎指引更新（美國的肝病研究學會）',
    '34427860': 'APASL 2021 免疫抑制治療相關 B 型肝炎再活化指引（亞太地區的肝臟研究學會）',
    '29799677': 'G-CAN 2019 痛風基本要素命名共識',
    '38212040': 'EULAR 2023 膝、髖退化性關節炎非藥物核心治療建議（European Alliance of Associations for Rheumatology；歐洲的風濕病學會聯盟）',
}


def ev(quote, pmid, location, supports, access='PMC full text'):
    # doi / pmcid are filled in from the research files (same PMID) at apply time
    return {'quote': quote, 'location': location, 'access': access, 'pmid': pmid, 'doi': '', 'pmcid': '',
            'supports': supports}


POST = {
    # ---------- n1a: OA page ----------
    'sarcopenia': {
        'example': '可能的徵兆：跌倒、覺得無力、走路變慢、從椅子站起來有困難、肌肉變少',
        'loc_by_prefix': {'sarcopenia is a muscle disease (muscle failure)':
                          "Abstract (Recommendations); the PMC 'Summary and call-to-action' section has a reworded version "
                          "(\"Sarcopenia, i.e. muscle failure, is a muscle disease rooted in adverse muscle changes that accrue across a lifetime; …\")"},
    },
    'paraffin': {
        'def': '石蠟浴是一種手部熱療方式：把手反覆浸入以專用機器加熱融化的石蠟，讓蠟在手上形成一層層，再用毛巾包住保溫一段時間後取下。',
        'add_ev': [ev('During the application, patients dipped their hands into the paraffin bath for 10 times. Their hands were covered with a towel and waited for 20 minutes to preserve the heat. For the treatment, a standard paraffin boiler of 28 L with an automatic thermostat and a temperature of 53°C was used.',
                      '34527924', 'Patients and Methods', 'def（反覆浸入、專用機器加熱、毛巾包住保溫）')],
    },
    'wedged-insoles': {
    },
    'glucosamine': {
        'def': '葡萄糖胺是人體本來就有的物質，是構成軟骨的原料之一；可做成口服的營養補充品。',
        'note': '品質較好的研究顯示，和安慰劑相比，它沒有明顯減輕關節疼痛，也沒有減緩X光上關節退化的進展。',
        'drop_quote_prefix': ['In Europe, glucosamine is prescribed'],
        'supports_replace': [('def（可由醫師開立，也可自行購買）', '背景：醫師處方與自行購買都有（定義未寫入）')],
        'add_ev': [
            ev('To determine the effect of glucosamine, chondroitin, or the two in combination on joint pain and on radiological progression of disease in osteoarthritis of the hip or knee.',
               '20847017', 'Abstract (Objective)', 'note（疼痛與X光上的進展）', access='abstract'),
            ev('Compared with placebo, glucosamine, chondroitin, and their combination do not reduce joint pain or have an impact on narrowing of joint space.',
               '20847017', 'Abstract (Conclusions)', 'note', access='abstract'),
            ev('Glucosamine can also be taken as a pill as a supplement to the diet, or sometimes as an injection.',
               '15846645', 'Plain language summary (PMC record)', 'def（口服的營養補充品）', access='PMC full text'),
        ],
        'dedupe': True,
    },
    'balance-functional': {
        'loc_by_prefix': {
            'Fall prevention exercise should focus': "Section 'Interventions for community dwelling older adults at intermediate fall risk', 'Recommendation details and justification'",
            'Effective fall prevention programmes include': "Section 'Interventions for community dwelling older adults at intermediate fall risk', 'Recommendation details and justification'",
        },
    },
    'weight-bearing': {
        'exclude_pages': ['oa'],
    },

    # ---------- n1b: osteoporosis page ----------
    'vertebral-fracture': {
        'note': '骨鬆引起的，約三分之二沒有明顯症狀，也可能背痛、身高變矮或背變駝；不論有無症狀，之後都較易再骨折。',
        'add_ev': [ev("The Clinician's Guide offers concise recommendations regarding prevention, risk assessment, diagnosis, and treatment of osteoporosis in postmenopausal women and men aged 50 years and older.",
                      '35478046', 'Abstract', 'note（「約三分之二」的數字來自骨鬆族群）', access='abstract')],
        'dedupe': True,
    },
    'onj': {
        'def': '指正在或曾經使用雙磷酸鹽類骨鬆藥或骨鬆皮下注射針劑（denosumab）的人，顎骨露出來超過8週，經適當治療仍未癒合，且顎部沒做過放射線治療。',
    },
    'bisphosphonate': {
        'example': '口服的 alendronate，或靜脈注射的 zoledronic acid',
        'add_ev': [ev('zoledronate–zoledronic acid (a potent intravenous bisphosphonate)',
                      '40134107', "Section 'Transition of bone protective agents'", 'example（zoledronic acid，靜脈注射）')],
        'dedupe': True,
    },
    'denosumab': {
        'term': '骨鬆皮下注射針劑（denosumab）',
    },
    'fragility-fracture': {
        'loc_by_prefix': {'Often referred to as fragility':
                          "Recommendations section, introductory text (after 'Scope'); paragraph begins 'In adults older than 40 years…'"},
    },
    'osteoporosis': {
        'label': 'ESCEO/IOF 2019・定義',
    },

    # ---------- n2: labs page ----------
    'ana': {
        'def': '抗核抗體是會和自己細胞核等成分結合的抗體。常用螢光染色法檢驗，報告可能列出稀釋倍數（力價，如1:160）和螢光型態。',
        'example': '1:160，表示血清稀釋160倍仍看得到螢光；倍數越大，抗體越多。',
        'label': 'ICAP 2019、克羅埃西亞檢驗建議 2021・定義',
        'add_ev': [
            ev('Based on titration or appropriate evaluation of the fluorescence intensity, the antibody level can be determined and this information has general concordance with the clinical relevance of the test result.',
               '30862649', 'Introduction, paragraph 2', 'example（倍數越大，抗體越多）'),
            ev('besides the titre or fluorescence intensity, it also provides fluorescence pattern(s).',
               '30862649', 'Abstract', 'def（螢光型態）', access='abstract'),
        ],
        'dedupe': True,
    },
    'rf': {
        'def': '類風濕因子是一種自體抗體，會和身體自己的抗體（IgG）的一部分結合；因和類風濕性關節炎有關而得名，是診斷這個病的參考指標之一。',
        'example': 'C型肝炎感染者，也可能驗出類風濕因子。',
    },
    'anti-ccp': {
        'def': '抗CCP抗體是一種自體抗體（針對自身成分的抗體），是診斷類風濕性關節炎的參考指標之一。',
        'note': '沒有類風濕性關節炎的人也可能陽性，但機會比類風濕因子低；病人也可能陰性。',
        'add_ev': [ev('In participants without RA, 311 (0.8%) were ACPA-positive.', '28043998', 'Abstract', 'note（沒病的人也可能陽性）', access='abstract')],
        'dedupe': True,
    },
    'ctd': {
        'label': '克羅埃西亞檢驗建議 2021・定義',
    },
    'ult': {
        'exclude_pages': ['labs'],
    },
    'org-eular': {
        'note': '網站引用的部分較早文件，用的是舊的英文全名。',
    },

    # ---------- n3: infection page ----------
    'ltbi': {
        'note': '按時、完整做完治療，是能否預防發病的重要關鍵。',
        'add_ev': [ev('Adherence to the full course and completion of LTBI treatment are important determinants of clinical benefit to the individual as well as to the success of the programme.',
                      '26405286', "Results, 'Adherence and completion of preventive treatment'", 'note')],
        'dedupe': True,
    },
    'igra': {
        'def': 'IGRA（抽血）和皮膚測試（結核菌素皮膚測試）都是看身體對結核菌有沒有免疫反應，可幫助判斷是否感染過結核菌，但無法分辨是潛伏結核還是已經發病。',
        'note': '皮膚測試較易受類固醇等藥物影響；免疫力較低時兩者都可能偽陰性。是否發病，醫師會看症狀和胸部 X 光。',
        'add_ev': [
            ev('Evidence suggests that both TST and IGRA are acceptable but imperfect tests. They represent indirect markers of Mycobacterium tuberculosis exposure and indicate a cellular immune response to M. tuberculosis.',
               '24396134', 'Abstract', 'def（可幫助判斷，不是確定）', access='abstract'),
            ev('Both TST and IGRA have reduced sensitivity in immunocompromised patients and have low predictive value for progression to active TB.',
               '24396134', 'Abstract', 'note（免疫力較低時可能偽陰性）', access='abstract'),
            ev('Therefore, the diagnosis of active TB must be excluded prior to embarking on treatment for LTBI. This is typically done by determining whether or not symptoms suggestive of TB disease are present, performing a chest radiograph and, if radiographic signs of active TB (eg, airspace opacities, pleural effusions, cavities, or changes on serial radiographs) are seen, then sampling is performed and the patient managed accordingly.',
               '28052967', 'Executive summary', 'note（是否發病看症狀和胸部 X 光）'),
        ],
        'dedupe': True,
    },
    'hbv-serology': {
        'example': '三項都陰性：表示沒感染過，也可能沒有免疫力，可和醫師討論打疫苗。',
        'note': '曾感染過的人即使有表面抗體，接受免疫抑制治療時仍可能再活化，需依醫師安排追蹤。',
        'add_ev': [
            ev('The presence of HBsAg indicates HBV infection, either acute or chronic, except when it might be transiently positive shortly after a dose of HepB vaccine',
               '36893044', 'Interpretation of hepatitis B test results', 'def（表面抗原陽性表示目前感染，含急性與慢性）'),
            ev('Anti-HBs concentrations might wane over time among vaccine responders', '36893044', 'Table 1, footnote', 'example（也可能沒有免疫力）'),
            ev('Among vaccine responders who completed a vaccine series, anti-HBs can decline over time to levels of <10 mIU/mL; however, the majority are still immune and will mount an immune response to a vaccine challenge ≥35 years after vaccination',
               '36893044', 'Interpretation of hepatitis B test results', 'example（三項都陰性不等於一定沒有免疫力）'),
            ev('The presence of anti-HBs does not prevent HBV reactivation, but anti-HBs may be useful for detecting prior infection in HBsAg negative, anti-HBc positive patients, and in surveillance as the loss of anti-HBs may be a predictor of HBV reactivation',
               '29405329', '§6D.2 Screening Recommendations in the Setting of Immunosuppressive or Cytotoxic Drugs', 'note（接受免疫抑制治療時）'),
        ],
        'dedupe': True,
    },
    'hbv-reactivation': {
        'def': 'B 型肝炎再活化是指因使用免疫抑制治療，身體壓不住 B 型肝炎病毒，病毒又明顯增加；帶原者和已痊癒的人都可能發生，有時在治療結束後才出現，之後可能引起肝炎發作。',
        'add_ev': [
            ev('1.1.2. Reactivation of past HBV infection (HBsAg negative, anti-HBc positive) after the start of immunosuppressive therapy',
               '34427860', 'Recommendation 1.1.2 (definition)', 'def（因使用免疫抑制治療）'),
            ev('Reactivation beyond 12 months has been reported, so further monitoring should be considered, particularly for patients who received anti-CD20 antibody therapy',
               '29405329', '§6D', 'def（有時在治療結束後才出現）'),
        ],
        'dedupe': True,
    },
    'tsdmard': {
        'def': '口服標靶藥物指「標靶合成」抗風濕藥物（tsDMARDs），是針對身體裡特定分子設計的藥。JAK 抑制劑是其中一類，是用吃的藥。',
        'example': 'tofacitinib、baricitinib、upadacitinib',
        'note': '用藥前也要篩檢潛伏結核。',
        'drop_quote_prefix': ['Serious infections (similar to bDMARDs)'],
        'add_ev': [ev('In addition to biologic/targeted synthetic disease-modifying antirheumatic drugs (DMARDs) for which screening for latent tuberculosis (TB) should be performed, screening could be considered also before conventional synthetic DMARDs, glucocorticoids and immunosuppressants.',
                      '36328476', 'Abstract', 'note（用藥前篩檢潛伏結核）', access='abstract')],
        'dedupe': True,
    },
    'zoster': {
        'def': '帶狀疱疹（皮蛇）是得過水痘（或打過水痘疫苗）後，潛伏在體內的水痘帶狀疱疹病毒重新活化，引起的疼痛水泡疹，通常長在身體一側的局部區域。',
        'add_ev': [
            ev('Persons who have neither experienced varicella nor received varicella vaccine are not at risk for herpes zoster.',
               '35051134', 'Special Populations', 'def（得過水痘或打過水痘疫苗）'),
            ev('Children and adolescents who have received live-attenuated varicella vaccines are at lower risk for herpes zoster than are those who experienced varicella',
               '35051134', 'Special Populations', 'def（打過水痘疫苗的人也可能得，但風險較低）'),
        ],
        'dedupe': True,
    },
    'pjp': {
        'def': '肺囊蟲肺炎是由肺囊蟲引起的肺炎；肺囊蟲名稱有「蟲」，其實是一種真菌。主要發生在免疫力較低的人，雖然不常見，但可能致命。',
        'add_ev': [ev('Although the incidence of PcP in such patients is usually low, mortality is quite high, ranging between 30% and 50% in the majority of autoimmune diseases.',
                      '30853123', 'Abstract', 'def（雖然不常見，但可能致命）', access='abstract')],
        'dedupe': True,
    },
    'good-practice': {
        'def': '良好實務建議是指引裡「不分級」的建議：多半是專家依臨床經驗與共識，認為照護上應該這樣做，所以不另評證據等級。',
        'note': '沒有分級不代表不重要。',
        'label': '指引方法說明・定義',
        'add_ev': [ev('Recommendations that were based on good clinical practice and experience of the working group members are not formally graded but acknowledged in the guideline as "good clinical practice".',
                      '38724043', 'Methods (grading of recommendations)', 'def（專家依臨床經驗，不另分級）')],
        'dedupe': True,
    },

    # ---------- n4: organisations ----------
    'org-bhof': {
        'def': '美國的骨骼健康與骨質疏鬆基金會；網站引用它2022年寫給臨床醫療人員的骨質疏鬆症預防與治療指南。',
        'drop_quote_prefix': ['the National Osteoporosis Foundation of the USA', 'BHOF previously estimated', 'The BHOF does not advocate'],
        'add_ev': [ev('Bone Health & Osteoporosis Foundation, 251 18th Street S, Suite 630, Arlington, VA, 22202, USA.',
                      '40498227', 'Author affiliation (PubMed record)', 'def（美國）', access='abstract')],
        'confidence': 'High (PubMed abstract, PMC full text and PubMed affiliation)',
    },
    'org-esceo-iof': {
        'term': 'ESCEO／IOF',
        'en': 'European Society for Clinical and Economic Aspects of Osteoporosis, Osteoarthritis and Musculoskeletal Diseases; International Osteoporosis Foundation',
        'label': 'ESCEO/IOF 2019・名稱',
        'drop_pmids': ['40921943'],
    },
    'org-easi-iuis': {
        'term': 'EASI／IUIS',
        'en': 'European Autoimmunity Standardisation Initiative; International Union of Immunological Societies',
        'def': 'EASI是歐洲多國參與、推動自體抗體檢驗標準化與一致化的組織；IUIS是國際性的免疫學會聯盟。網站引用兩方專家2014年的抗核抗體檢驗國際建議。',
        'drop_pmids': ['29679532'],
        'add_ev': [ev('The European Autoimmunity Standardisation Initiative (EASI) was founded to facilitate both standardisation as well as harmonisation of autoantibody tests, but over the years the focus has drifted away from standardisation in favour of harmonisation.',
                      '32127033', 'Abstract', 'def（標準化與一致化）', access='abstract')],
        'dedupe': True,
    },
    'org-ese-es': {
        'term': 'ESE／ES',
        'en': 'European Society of Endocrinology; Endocrine Society',
    },
    'org-idst': {
        'def': '台灣的感染症醫學會；網站引用它指派的成人預防接種工作小組2024年發表的台灣成人帶狀疱疹（皮蛇）疫苗建議。',
    },
    'org-ace': {
        'def': '新加坡衛生部的一個機構，制定新加坡的臨床指引；網站引用的論文，說明它2026年膝關節退化性關節炎指引的建議依據。',
    },
    'org-aasld': {
        'label': 'AASLD 2018・名稱',
    },
}


# Physician decisions, 2026-10-11 (after reading the verified drafts).
DECISIONS = {
    'false-results': {
        'term': '偽陽性與偽陰性',
        'aliases': ['偽陽性', '偽陰性'],
        'def': '偽陽性是其實沒有這種病或狀況，檢查卻呈陽性；偽陰性則是其實有，檢查卻呈陰性。',
        'note': '偽陽性可能帶來不必要的追加檢查和擔心；偽陰性可能漏掉真正有病或受感染的人。',
    },
    'adrenal': {
        'def': '腎上腺功能不足是腎上腺做不出足夠的皮質醇（身體自己的類固醇）；長期用類固醇會壓抑身體自己製造。腎上腺危象是它的急性發作，會危及生命，必須緊急治療。',
    },
    'glucosamine': {
        'cat': 'diet',
    },
    'rf': {
        'example': '',
        'drop_quote_prefix': ['RFs can be found in 40'],
    },
    'denosumab': {
    },
    'onj': {
    },
}
for _tid, _fix in DECISIONS.items():
    _cur = POST.setdefault(_tid, {})
    for _k, _v in _fix.items():
        if _k == 'rn_append' and _cur.get('rn_append'):
            _cur['rn_append'] = _cur['rn_append'] + ' ' + _v
        else:
            _cur[_k] = _v


def _evidence_index():
    idx = {}
    for f in sorted(glob.glob(str(HERE / 'research' / 'research_*.json'))) + sorted(glob.glob(str(HERE / 'research' / 'new_*.json'))):
        d = json.load(open(f, encoding='utf-8'))
        for e in d.get('entries', [d]):
            for x in e.get('evidence', []):
                pm = str(x.get('pmid') or '')
                if pm and (x.get('doi') or x.get('pmcid')):
                    cur = idx.setdefault(pm, {'doi': '', 'pmcid': ''})
                    cur['doi'] = cur['doi'] or x.get('doi', '')
                    cur['pmcid'] = cur['pmcid'] or x.get('pmcid', '')
    return idx


_IDX = None


def apply(e, src_lookup):
    global _IDX
    if _IDX is None:
        _IDX = _evidence_index()
        for pm, s in SRC.items():
            _IDX.setdefault(pm, {'doi': s.get('doi', ''), 'pmcid': ''})
        _IDX['34527924']['pmcid'] = 'PMC8418774'
        _IDX['40498227']['pmcid'] = 'PMC12158823'
    p = POST.get(e['id'])
    if p:
        for x in p.get('add_ev', []):
            meta = _IDX.get(str(x['pmid']), {})
            x['doi'] = x['doi'] or meta.get('doi', '') or (SRC.get(str(x['pmid'])) or src_lookup.get(str(x['pmid'])) or {}).get('doi', '')
            x['pmcid'] = x['pmcid'] or meta.get('pmcid', '')
        postfix.apply(e, src_lookup, POST, SRC)
    for s in e.get('sources', []):
        fix = SHORT_FIX.get(str(s.get('pmid')))
        if fix:
            s['short'] = fix
    return e
