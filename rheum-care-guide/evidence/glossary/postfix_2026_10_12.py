"""Wording approved by the reviewing physician after the legal and dispute-risk review (2026-10-12).

Applied by merge.py after postfix.py and postfix_2026_10.py. Every change states the text it replaces, and
apply() stops if the merged entry no longer has that text, so a change made elsewhere cannot be overwritten
silently.

Why these changes: drug-allergy exception for urate-lowering drugs (Taiwan Ministry of Health and Welfare
allopurinol notice, 2014-12-16); emergency lines that name 119; sentences that promised what a reader's
doctor "will" do (「醫師會…」), now attributed to the guideline or framed as a discussion; and small wording
fixes. Safety phrases with no quoted source (for example 「請立刻撥打 119」, 「請當天就看眼科」) are editorial,
as on the disease pages.
"""
import re

CHANGES = {
    'ult': {
        'def': ('降尿酸藥是把血中尿酸降下來、減少痛風發作的藥，指引建議長期持續使用；醫師會依抽血的尿酸值調整劑量。',
                '降尿酸藥是把血中尿酸降下來、減少痛風發作的藥，指引建議長期持續使用，並由醫師依抽血的尿酸值調整劑量。'),
        'note': ('剛開始吃可能誘發發作，指引強烈建議同時使用至少3到6個月的預防發作藥物。',
                 '剛開始吃可能誘發發作，指引強烈建議同時使用至少3到6個月的預防發作藥物；吃藥期間起紅疹、嘴巴破、喉嚨痛或眼睛癢，請立即停藥並就醫。'),
    },
    'adrenal': {
        'note': ('使用類固醇期間或剛停藥，若嘔吐、腹瀉或吃不下藥，請盡快就醫。',
                 '使用類固醇期間或最近停藥，若嘔吐或腹瀉，請盡快就醫；吃不下藥請立即就醫；快昏倒或意識不清，請撥打 119 或到急診。'),
    },
    'anaphylaxis': {
        'note': ('這是急症，需立刻處理；不一定有皮膚症狀。寒冷性蕁麻疹病人游泳等全身受冷時也可能發生。',
                 '這是急症，請立刻撥打 119；不一定有皮膚症狀。寒冷性蕁麻疹病人游泳等全身受冷時也可能發生。'),
    },
    'angioedema': {
        'note': ('可和膨疹一起或單獨出現；只有腫脹時請醫師找原因。喉嚨腫脹可能危及生命。',
                 '可和膨疹一起或單獨出現；只有腫脹時請醫師找原因。喉嚨腫脹可能危及生命，請立刻撥打 119。'),
    },
    'uveitis': {
        'note': ('屬急症，要盡快看眼科；延誤治療，有些人可能出現青光眼或視力嚴重受損。',
                 '屬急症，請當天就看眼科；延誤治療，有些人可能出現青光眼或視力嚴重受損。'),
    },
    'denosumab': {
        'note': ('不要自行停藥或延後打針；需要停藥時，請醫師安排接續治療，以免脊椎骨折風險增加。',
                 '不要自行停藥或延後打針；停藥前請和醫師討論接續治療，以免脊椎骨折風險增加。'),
    },
    'fracture-risk-factors': {
        'def': ('和骨質疏鬆骨折風險較高有關的因素。醫師會依這些因素評估骨折風險，幫助決定是否需要做骨密度檢查。',
                '和骨質疏鬆骨折風險較高有關的因素。指引建議依這些因素評估骨折風險，再決定是否需要做骨密度檢查。'),
    },
    'lupus-nephritis': {
        'note': ('每次回診都要驗尿，這是發現腎炎的必要檢查。',
                 '英國指引指出，每次回診都驗尿，是發現腎炎的必要檢查。'),
    },
    'disease-activity': {
        'def': ('指疾病目前「活躍」的程度，主要反映發炎，會隨時間起伏。醫師會綜合症狀、身體檢查、抽血和影像來評估，常分成緩解或不活躍、低、中、高等程度。',
                '指疾病目前「活躍」的程度，主要反映發炎，會隨時間起伏。評估時通常綜合症狀、身體檢查、抽血和影像，常分成緩解或不活躍、低、中、高等程度。'),
    },
    'igra': {
        'note': ('皮膚測試較易受類固醇等藥物影響；免疫力較低時兩者都可能偽陰性。是否發病，醫師會看症狀和胸部 X 光。',
                 '皮膚測試較易受類固醇等藥物影響；免疫力較低時兩者都可能偽陰性。是否發病，通常要看症狀和胸部 X 光判斷。'),
    },
    'foodborne': {
        'note': ('飲食與環境衛生建議可能減少這類感染（以專家意見為主），可請醫療團隊提供。',
                 '飲食與環境衛生建議可能減少這類感染（以專家意見為主），可以和醫師討論。'),
    },
    'nsaid': {
        'note': ('醫師為預防血栓開的低劑量阿斯匹靈，不一定要停用；請勿自行停藥，先和醫師討論。',
                 '醫師為預防血栓開的低劑量阿斯匹靈不一定要停用，請先和醫師討論、勿自行停藥；其他消炎止痛藥若曾讓蕁麻疹變嚴重，就避免使用。'),
    },
    'antihistamine': {
        'def': ('抗組織胺是常用來治療蕁麻疹和過敏性鼻炎的抗過敏藥。舊的第一代容易讓人想睡；新的第二代很少或不會讓人想睡，是蕁麻疹的第一線用藥。',
                '抗組織胺是常用來治療蕁麻疹和過敏性鼻炎的抗過敏藥。舊的第一代容易讓人想睡；新的第二代較不會讓人想睡（少數人仍可能想睡），是蕁麻疹的第一線用藥。'),
    },
    'night-sweats': {
        'def': ('睡覺時出汗；很多沒有特別疾病的人也會有。',
                '睡覺時出汗；可能和感染、更年期等有關，但很多沒有特別疾病的人也會有。'),
    },
    'dhea': {
        'def': ('DHEA（dehydroepiandrosterone）是腎上腺分泌的一種荷爾蒙，身體可把它轉變成男性和女性荷爾蒙；也有口服的 DHEA 補充劑。',
                'DHEA（dehydroepiandrosterone）是腎上腺分泌的一種荷爾蒙，身體可把它轉變成男性和女性荷爾蒙；也有口服的 DHEA 製劑。'),
        'note': ('研究回顧發現，DHEA 用於乾燥症的結果令人失望；副作用多為輕微的長痘痘和多毛。',
                 '研究回顧發現，DHEA 用於乾燥症的結果令人失望；研究中的副作用主要是長痘痘和多毛。'),
    },
    'cbt': {
        'note': ('常由心理師或心理治療師提供，也有一些上過相關課程的護理師提供。',
                 '在台灣常由臨床心理師或諮商心理師提供；是否適合、到哪裡接受，可以和醫師討論。'),
    },
    'biologic': {
        'example': ('治療狼瘡的 belimumab、rituximab', '歐洲狼瘡指引列出的 belimumab、rituximab'),
    },
    'non-live-vaccine': {
        'note': ('部分藥物會讓疫苗反應變弱（但通常不會完全沒效）；如果可以，最好在開始免疫抑制治療前接種。',
                 '部分藥物會讓疫苗反應變弱（但通常不會完全沒效；rituximab 影響較大）；如果可以，最好在開始免疫抑制治療前接種。'),
    },
    'ltbi': {
        'def': ('潛伏結核是感染了結核菌、但還沒發病：沒有症狀，也還不會傳染。日後仍可能發病（再活化）成為結核病；接受治療可以預防發病。',
                '潛伏結核是感染了結核菌、但還沒發病：沒有症狀，也還不會傳染。日後仍可能發病（再活化）成為結核病；完整接受治療可以大幅降低發病機會。'),
    },
    'special-diets': {
        'note': ('指引的「不建議」只針對治療類風濕性關節炎；有些人可能因其他疾病而有使用的需要。',
                 '指引的「不建議」只針對治療類風濕性關節炎；有些人可能因其他疾病、宗教或個人選擇而採用。'),
    },
    'flare-plan': {
        'example': ('內容可包括聯絡誰、自我照護、疼痛與疲倦處理，以及醫療團隊說明的可能藥物調整',
                    '內容可包括怎麼就醫、自我照護、疼痛與疲倦處理，以及醫療團隊說明的可能藥物調整'),
    },
    'onj': {
        'note': ('骨鬆治療引起的很少見；保持口腔清潔、定期看牙醫有助降低風險；洗牙、補牙、做假牙不必延後骨鬆治療。',
                 '骨鬆治療引起的很少見；保持口腔清潔、定期看牙醫有助降低風險；洗牙、補牙、做假牙不必延後骨鬆治療，拔牙等侵入性治療請先和醫師、牙醫師討論。'),
    },
}

# What each quote supports (kept with the evidence; not shown on the site). (old, new) pairs.
SUPPORTS = {
    'ult': [('def: 依抽血尿酸值調整劑量；example: allopurinol、febuxostat',
             'def: 由醫師依抽血尿酸值調整劑量；example: allopurinol、febuxostat')],
    'adrenal': [('(also fits IF-4.3 「剛停用」)', '(also fits IF-4.3 「最近停用」)'),
                ('note: 使用類固醇期間或剛停藥，嘔吐、腹瀉時請盡快就醫 (site IF-S2)',
                 'note: 使用類固醇期間或最近停藥，嘔吐、腹瀉時請盡快就醫 (site IF-S2)')],
    'anaphylaxis': [('note：急症，需立刻處理；症狀常同時影響多個器官',
                     'note：急症，需立刻處理（「請立刻撥打 119」為台灣的在地化說法）；症狀常同時影響多個器官')],
    'uveitis': [('note：盡快看眼科；延誤治療少數人可能青光眼或嚴重視力受損',
                 'note：盡快看眼科（「當天」為編輯加註）；延誤治療少數人可能青光眼或嚴重視力受損')],
    'denosumab': [('note：停藥須考慮接續治療，否則脊椎骨折風險增加（OP-6.3）',
                   'note：停藥前要討論接續治療，否則脊椎骨折風險增加（OP-6.3）')],
    'fracture-risk-factors': [('def：有臨床風險因子時評估骨折風險，以決定是否測骨密度',
                               'def：指引建議有臨床風險因子時評估骨折風險，以決定是否測骨密度')],
    'lupus-nephritis': [('note', 'note（英國 BSR 指引）')],
    'igra': [('note: 醫師會配合症狀和胸部 X 光判斷', 'note: 通常要配合症狀和胸部 X 光判斷')],
    'antihistamine': [('def: 新的第二代很少或不會讓人想睡', 'def: 新的第二代較不會讓人想睡（minimally sedating；少數人仍可能想睡）')],
    'night-sweats': [('def：睡覺時出汗；沒有相關疾病的人也常有',
                      'def：睡覺時出汗；可能和更年期、感染等有關，但沒有相關疾病的人也常有')],
    'dhea': [('def: 口服 DHEA 補充劑', 'def: 口服 DHEA 製劑'),
             ('note: 副作用多為輕微的長痘痘和多毛', 'note: 研究中的副作用主要是長痘痘和多毛')],
    'cbt': [('note', 'context: in Europe CBT is often delivered by psychologists/psychotherapists or trained nurses; '
                     'the note now describes Taiwan (臨床心理師、諮商心理師, 心理師法 §5)')],
    'biologic': [('example: belimumab、rituximab (biologics in SLE)',
                  'example: belimumab、rituximab (biologics in SLE; 歐洲狼瘡指引列出的)')],
    'non-live-vaccine': [('note: 疫苗反應變弱但通常不會完全沒效', 'note: 疫苗反應變弱但通常不會完全沒效；rituximab 除外（影響較大）')],
    'ltbi': [('def: 接受治療可以預防發病', 'def: 完整接受治療可以大幅降低發病機會')],
    'special-diets': [('note：指引只針對治療 RA；有人可能因其他疾病而有需要。',
                       'note：指引只針對治療 RA；有人可能因其他疾病、宗教或個人選擇而採用。')],
}

# Quotes added for new wording (read verbatim in the original; same quote as urticaria C28 on the site).
ADD_EV = {
    'nsaid': [{
        'quote': 'Physicians should therefore ask patients about the intake of NSAIDs, including on‐demand use, and advise patients '
                 'with a history to NSAID‐induced urticaria to avoid these drugs (NSAID challenges may be considered to avoid '
                 'unnecessary restrictions when clinical history is not clear).',
        'location': 'Section 4.2.3 (medications that may aggravate CSU)', 'access': 'PMC full text',
        'pmid': '41649409', 'doi': '10.1111/all.70210', 'pmcid': 'PMC13466004',
        'supports': 'note: 其他消炎止痛藥若曾讓蕁麻疹變嚴重，就避免使用 (site UR-1.2, urticaria C28)',
    }],
}


# Item 9.5: the evidence panel shows each quote's location and access publicly. Keep where the quote is in the
# source; drop tool names, read counts, internal file names and who read it.
ACCESS = {
    'WebFetch': 'Web page or PDF',
    'WebFetch (author manuscript copy on CDC Stacks, cdc_151745_DS1.pdf)': 'Author manuscript (CDC Stacks)',
    'WebFetch (ACR-hosted manuscript PDF giop-guideline-manuscript-2022.pdf, linked from rheumatology.org)':
        'Manuscript PDF hosted by ACR (rheumatology.org)',
    'WebFetch (publisher page ard.bmj.com/content/79/1/3; 3 passes in the research phase + 2 passes on 2026-10-07, identical)':
        'Publisher page (ard.bmj.com/content/79/1/3)',
    "PMC full text (the word 'i.e.' before 'a 12-ounce' is dropped by the PMC extractor; full sentence confirmed by WebFetch of the PMC page)":
        "PMC full text (the word 'i.e.' before 'a 12-ounce' is missing from the PMC text extraction; as on the PMC page)",
}
LOCATION = {
    'Table 1 (definitions of the interventions; table title in WebFetch read 2: "Integrative Management of Rheumatoid Arthritis Interventions"), row "Aerobic exercise"; not present in the get_full_text_article extraction, read twice via WebFetch with identical wording':
        'Table 1 (definitions of the interventions), row "Aerobic exercise" (PMC table page)',
    'Table 1 (definitions of the interventions; table title in WebFetch read 2: "Integrative Management of Rheumatoid Arthritis Interventions"), row "Resistance exercise"; not present in the get_full_text_article extraction, read twice via WebFetch with identical wording':
        'Table 1 (definitions of the interventions), row "Resistance exercise" (PMC table page)',
    "Table 1 ('Descriptions and examples of interventions included in the integrative management of rheumatoid arthritis guideline'); not in the PMC extraction; WebFetch: PMC page ×2 (drafters) and CDC Stacks author manuscript p.19 ×2 (verifier), identical wording":
        "Table 1 ('Descriptions and examples of interventions included in the integrative management of rheumatoid arthritis guideline'); PMC page and CDC Stacks author manuscript p.19",
    'Section "Health-Related Fitness And Associated Physiological Changes", paragraph 1. The PMC extraction reads "Third,refers to an individual’s range of motion around a joint, or group of joints." (italic word dropped); "flexibility" restored from two WebFetch reads of the PMC page':
        'Section "Health-Related Fitness And Associated Physiological Changes", paragraph 1. The PMC text extraction reads "Third,refers to an individual’s range of motion around a joint, or group of joints." (italic word dropped); "flexibility" restored as on the PMC page',
    'Section "Health-Related Fitness And Associated Physiological Changes", paragraph 1. The PMC extraction drops the italic subject "CRF" ("components., also known as …"); restored from two WebFetch reads of the PMC page':
        'Section "Health-Related Fitness And Associated Physiological Changes", paragraph 1. The PMC text extraction drops the italic subject "CRF" ("components., also known as …"); restored as on the PMC page',
    'Box 1 Glossary of terms, entry "Systematic review" (the bold term label is dropped in the PMC extraction; label confirmed verbatim on bmj.com via WebFetch)':
        'Box 1 Glossary of terms, entry "Systematic review" (the bold term label is missing from the PMC text extraction; label as on bmj.com)',
    'Box 1 Glossary of terms, entry "Statistical synthesis" (label dropped in PMC text; confirmed on bmj.com via WebFetch)':
        'Box 1 Glossary of terms, entry "Statistical synthesis" (label missing from the PMC text; as on bmj.com)',
    'Box 1 Glossary of terms, entry "Meta-analysis of effect estimates" (label dropped in PMC text; confirmed on bmj.com via WebFetch)':
        'Box 1 Glossary of terms, entry "Meta-analysis of effect estimates" (label missing from the PMC text; as on bmj.com)',
    "Plain language summary, 'What is osteoarthritis and glucosamine?' (PMC record; see reviewer_notes on version)":
        "Plain language summary, 'What is osteoarthritis and glucosamine?' (PMC record)",
    "Table 2, Recommendation 1.1 (strong recommendation per the site's evidence file)": 'Table 2, Recommendation 1.1 (strong recommendation)',
    'Text under Recommendation 4 (sentence continues; WebFetch returns short segments only)': 'Text under Recommendation 4 (sentence continues)',
    'Table 1, Recommendation 8 (read as two WebFetch segments; consistent with evidence file C53)': 'Table 1, Recommendation 8',
    "Discussion (assembled from three WebFetch segments; the superscript reference number after 'shown,' is omitted; consistent with evidence file C67)":
        "Discussion (the superscript reference number after 'shown,' is omitted)",
}
LOC_RULES = [
    (re.compile(r' \[WebFetch of the PMC table page pmc\.ncbi\.nlm\.nih\.gov/articles/PMC10947582/table/T1/; the get_full_text_article output omits Table 1\]$'),
     ' (PMC table page)'),
    (re.compile(r'\(PMC text of the Arthritis Care & Research version, S2 in research/oa\.md\)'), '(PMC text of the Arthritis Care & Research version)'),
]


def clean_fields(e):
    for x in e['evidence']:
        a = x.get('access', '')
        if a in ACCESS:
            x['access'] = ACCESS[a]
        loc = x.get('location', '')
        if loc in LOCATION:
            loc = LOCATION[loc]
        for rx, rep in LOC_RULES:
            loc = rx.sub(rep, loc)
        x['location'] = loc


def apply(e):
    clean_fields(e)
    ch = CHANGES.get(e['id'])
    if not ch:
        return e
    for field, (old, new) in ch.items():
        assert e[field] == old, (e['id'], field, e[field])
        e[field] = new
    for old, new in SUPPORTS.get(e['id'], []):
        hits = [x for x in e['evidence'] if x.get('supports', '') == old or (len(old) > 8 and old in x.get('supports', ''))]
        assert len(hits) >= 1, (e['id'], 'supports not found', old)
        for x in hits:
            x['supports'] = new if x['supports'] == old else x['supports'].replace(old, new)
    for x in ADD_EV.get(e['id'], []):
        assert any(str(s.get('pmid')) == x['pmid'] for s in e['sources']), (e['id'], 'source missing', x['pmid'])
        if not any(y['quote'] == x['quote'] for y in e['evidence']):
            e['evidence'].append(dict(x))
    return e
