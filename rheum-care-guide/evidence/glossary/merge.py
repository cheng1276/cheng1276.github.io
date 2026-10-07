"""Merge the research files into the site glossary, applying the editorial review decisions (EDITS)
and the fixes from the independent verification (postfix.py).

Run from the rheum-care-guide folder:
  python3 evidence/glossary/merge.py      # writes src/glossary/glossary.json
"""
import glob
import json
import pathlib
import re

import postfix

HERE = pathlib.Path(__file__).resolve().parent
RESEARCH = HERE / 'research'
OUT = HERE.parent.parent / 'src' / 'glossary' / 'glossary.json'

DROP = {'bed-cage', 'imaging'}

CATS = [
    ('condition', '疾病與症狀'),
    ('allergy', '蕁麻疹與過敏'),
    ('drug', '藥物與疫苗'),
    ('exercise', '運動'),
    ('rehab', '復健與療法'),
    ('diet', '飲食與營養'),
    ('sun', '防曬'),
    ('tool', '評估工具'),
    ('evidence', '研究與出處用語'),
    ('org', '出處機構'),
]
CAT_FIX = {'psych': 'rehab'}
ALLERGY = {'csu-cindu', 'cold-urticaria', 'pressure-urticaria', 'solar-urticaria', 'cholinergic-urticaria',
           'wheal', 'angioedema', 'anaphylaxis', 'stridor-wheeze'}

# Terms that appear very often: link only the first occurrence on each page (default: first per card).
PAGE_SCOPE = {'guideline', 'csu-cindu', 'physical-therapy', 'occupational-therapy', 'disease-activity', 'autoimmune',
              'org-acr', 'org-eular', 'org-bsr', 'org-nice', 'org-asas', 'org-who', 'org-galen', 'org-wao', 'org-tfos',
              'org-tra', 'org-aaaai', 'org-bsaci', 'org-ects', 'org-sf'}
# Strings that are consumed by the matcher but never linked (label vocabulary explained in the legend).
STOP = ['指引說明']
EXCLUDE_PAGES = {'disease-activity': ['urticaria']}

# Field edits decided in the editorial review (None = clear the field).
EDITS = {
    'aerobic': {'note': '又稱耐力運動，可提升心肺耐力。'},
    'moderate-intensity': {'example': '快走、打排球'},
    'sedentary': {'note': '睡覺不算。目前證據還不足以訂出「坐多久算太久」。'},
    'passive-therapy': {'note': '物理治療的目標之一是教您學會自己運動，所以以主動運動為主，被動治療只能輔助、不能取代。'},
    'hand-therapist': {'note': None},
    'cervical-traction': {'def': '頸椎牽引是用拉力伸展頸部的治療。例如機械牽引：把頭套套在後腦（有時也套住下巴）並接上機器，依設定的時間和重量拉。'},
    'cbt': {'note': '常由心理師或心理治療師提供，也有受過這項訓練的護理師。'},
    'hfcs': {'note': None},
    'special-diets': {'example': None},
    'saturated-fat': {'def': '飽和脂肪是脂肪的一種，在動物油脂和植物性的固態油脂中含量較多。',
                      'drop_pmids': ['29788879']},
    'bmi': {'def': 'BMI（身體質量指數）是用體重（公斤）除以身高（公尺）的平方算出的數值，常用來判斷是否過重或肥胖。',
            'note': '國際（WHO）分級：25 以上為過重、30 以上為肥胖；亞洲人在 BMI 較低時，健康風險就可能升高。'},
    'uva-uvb': {'def': 'UVA 和 UVB 是兩種波長不同的紫外線：UVA 波長較長，能穿透到皮膚較深的真皮層；UVB 波長較短。'},
    'oral-glucocorticoid': {'def': '這裡的類固醇指「糖皮質類固醇」，用來治療狼瘡等風濕病，能快速控制病情；口服類固醇就是用吃的。',
                            'note': '長期使用對健康有不良影響（例如增加骨質疏鬆風險），指引主張盡量減少用量；調整劑量請和醫師討論，不要自行停藥。'},
    'dmard': {'term': '抗風濕藥物（疾病調節型抗風濕藥物）'},
    'antimalarial': {'example': None},
    'mtx-lef': {'def': '兩者都是用來治療類風濕性關節炎的「傳統合成」抗風濕藥物（csDMARDs）。'},
    'nsaid': {'note': None},
    'antihistamine': {'term': '抗組織胺（較不會嗜睡的）',
                      'aliases': ['較不會嗜睡的抗組織胺', '不會嗜睡的抗組織胺', '抗組織胺']},
    'eye-ointment': {'example': None},
    'autoimmune': {'def': '免疫系統的重要工作，是分辨「自己」和「外來的東西」。自體免疫是指出現了針對自己身體的免疫成分（例如自體抗體）；若同時造成明顯的病變，就是自體免疫疾病。'},
    'anaphylaxis': {'term': '嚴重過敏反應', 'aliases': ['嚴重過敏反應']},
    'axspa': {'def': '一種主要影響脊椎和薦腸關節的慢性發炎性疾病；包括 X 光已看得到結構破壞的僵直性脊椎炎，以及 X 光還看不到破壞的非放射線型。',
              'example': None,
              'note': '也可能影響其他關節和肌腱附著處，或出現急性前葡萄膜炎、乾癬、發炎性腸道疾病等骨骼肌肉以外的表現。'},
    'uveitis': {'def': '葡萄膜炎是眼球內部的發炎。前葡萄膜炎是眼睛前段（虹彩等處）的發炎，虹彩炎就屬於這一類；急性型會突然發作，常只有一眼，也可能兩眼輪流復發。'},
    'cvd': {'note': None},
    'urolithiasis': {'note': None},
    'salivary-gland': {'note': '乾燥症若唾液腺出現新的腫脹，應盡早回診檢查。'},
    'night-sweats': {'def': '睡覺時出汗，嚴重時會全身濕透；很多沒有特別疾病的人也會有。',
                     'note': '乾燥症病人若持續夜間盜汗，或合併發燒、體重減輕，請盡早回診。'},
    'expert-consensus': {'note': '常用在缺乏高品質研究證據時；有些指引會把它列在較低的證據等級。'},
    'org-wao': {'def': '世界性的過敏組織；發表過「嚴重過敏反應」的處理指引，有 2011 年與 2020 年版。'},
    # 職能或物理治療師: link 職能 to occupational therapy and 物理治療師 to physical therapy.
    'occupational-therapy': {'aliases': ['職能治療師', '職能治療', '職能']},
}

# Clean English names shown in the popup (the research "aka" field is kept as metadata).
EN = {
    'aerobic': 'aerobic activity / aerobic exercise', 'moderate-intensity': 'moderate-intensity physical activity',
    'vigorous-intensity': 'vigorous-intensity physical activity', 'light-intensity': 'light-intensity physical activity',
    'muscle-strengthening': 'muscle-strengthening activity; resistance training', 'major-muscle-groups': 'major muscle groups',
    'weight-bearing': 'weight-bearing exercise', 'multicomponent': 'multicomponent physical activity',
    'sedentary': 'sedentary behaviour', 'mind-body': 'mind-body exercise; mind-body approaches',
    'aquatic': 'aquatic exercise', 'range-of-motion': 'range of motion exercises',
    'passive-therapy': 'passive / active physical therapy', 'aerobic-capacity': 'cardiorespiratory fitness (aerobic capacity)',
    'perceived-exertion': 'rating of perceived exertion', 'physical-therapy': 'physical therapy (physiotherapy)',
    'occupational-therapy': 'occupational therapy', 'hand-therapist': 'hand therapist', 'joint-protection': 'joint protection',
    'orthoses': 'splints, braces and orthoses', 'assistive-devices': 'assistive devices',
    'activity-pacing': 'activity pacing; energy conservation', 'self-management': 'self-management',
    'vocational-rehab': 'vocational rehabilitation', 'spinal-manipulation': 'spinal manipulation',
    'cervical-traction': 'cervical traction', 'contact-sports': 'contact sports', 'flare-plan': 'flare management plan',
    'cbt': 'cognitive behavioural therapy (CBT)', 'psychosocial': 'psychosocial interventions',
    'complementary': 'complementary therapies', 'purine': 'purine; purine-rich foods',
    'uric-acid': 'uric acid (urate); hyperuricaemia', 'hfcs': 'high-fructose corn syrup (HFCS)',
    'alcohol-serving': 'alcohol serving', 'mediterranean': 'Mediterranean-style diet',
    'special-diets': 'ketogenic, gluten-free and vegan diets; intermittent fasting',
    'refined-carbs': 'refined carbohydrates (refined grains)', 'saturated-fat': 'saturated fat',
    'processed-food': 'highly processed foods', 'elemental-calcium': 'elemental calcium', 'iu': 'International Unit (IU)',
    'bmi': 'body mass index (BMI)', 'xylitol': 'xylitol', 'diagnostic-diet': 'diagnostic diet',
    'spf': 'sun protection factor (SPF)', 'uva-uvb': 'ultraviolet A / ultraviolet B', 'broad-spectrum': 'broad-spectrum sunscreen',
    'uv-index': 'UV Index', 'photosensitivity': 'photosensitivity', 'oral-glucocorticoid': 'oral glucocorticoids',
    'dmard': 'disease-modifying antirheumatic drugs (DMARDs)', 'immunosuppressant': 'immunosuppressive medications',
    'biologic': 'biologics (biological DMARDs)', 'antimalarial': 'antimalarials; hydroxychloroquine',
    'mtx-lef': 'methotrexate; leflunomide', 'nsaid': 'non-steroidal anti-inflammatory drugs (NSAIDs)',
    'low-dose-aspirin': 'low-dose aspirin (acetylsalicylic acid)', 'antihistamine': 'second-generation H1-antihistamines',
    'ult': 'urate-lowering therapy (ULT)', 'flare-medicine': 'gout flare treatment',
    'non-live-vaccine': 'non-live (inactivated) vaccines', 'live-vaccine': 'live attenuated vaccines',
    'rzv': 'recombinant zoster vaccine (RZV)', 'pneumococcal': 'pneumococcal vaccines',
    'artificial-tears': 'preservative-free artificial tears', 'eye-ointment': 'ophthalmic ointment',
    'saliva-substitute': 'saliva substitutes', 'fluoride': 'topical fluoride', 'dhea': 'dehydroepiandrosterone (DHEA)',
    'autoimmune': 'autoimmunity; autoimmune disease', 'csu-cindu': 'chronic spontaneous / inducible urticaria',
    'cold-urticaria': 'cold urticaria', 'pressure-urticaria': 'delayed pressure urticaria', 'solar-urticaria': 'solar urticaria',
    'cholinergic-urticaria': 'cholinergic urticaria', 'wheal': 'wheal (hive)', 'angioedema': 'angioedema',
    'anaphylaxis': 'anaphylaxis', 'stridor-wheeze': 'stridor; wheeze',
    'uas7': 'Urticaria Activity Score over 7 days (UAS7)', 'uct': 'Urticaria Control Test (UCT)',
    'aas': 'Angioedema Activity Score (AAS)', 'axspa': 'axial spondyloarthritis (axSpA)',
    'uveitis': 'acute anterior uveitis; iritis', 'spinal-fusion': 'spinal fusion (ankylosis)', 'osteoporosis': 'osteoporosis',
    'raynaud': "Raynaud's phenomenon", 'lupus-nephritis': 'lupus nephritis', 'cutaneous-lupus': 'cutaneous lupus erythematosus',
    'neonatal-lupus': 'neonatal lupus', 'disease-activity': 'disease activity', 'comorbidity': 'comorbidity',
    'cvd': 'cardiovascular disease', 'ckd': 'chronic kidney disease', 'urolithiasis': 'urolithiasis (urinary stones)',
    'mgd': 'meibomian gland dysfunction', 'blepharitis': 'blepharitis', 'salivary-gland': 'salivary glands',
    'night-sweats': 'night sweats', 'guideline': 'clinical practice guideline', 'systematic-review': 'systematic review',
    'meta-analysis': 'meta-analysis', 'rct': 'randomised controlled trial (RCT)', 'observational': 'observational study',
    'placebo': 'placebo', 'certainty': 'certainty of evidence', 'clinical-significance': 'clinical significance',
    'expert-consensus': 'expert consensus', 'org-acr': 'American College of Rheumatology',
    'org-eular': 'European Alliance of Associations for Rheumatology', 'org-bsr': 'British Society for Rheumatology',
    'org-nice': 'National Institute for Health and Care Excellence',
    'org-asas': 'Assessment of SpondyloArthritis international Society', 'org-who': 'World Health Organization',
    'org-galen': 'Global Allergy and Asthma Excellence Network (GA²LEN)', 'org-wao': 'World Allergy Organization',
    'org-tfos': 'Tear Film & Ocular Surface Society', 'org-tra': 'Taiwan Rheumatology Association',
    'org-aaaai': 'American Academy of Allergy, Asthma & Immunology; American College of Allergy, Asthma & Immunology',
    'org-bsaci': 'British Society for Allergy and Clinical Immunology', 'org-ects': 'European Calcified Tissue Society',
    'org-sf': "Sjögren's Foundation",
}


def clean_example(t):
    t = (t or '').strip()
    t = re.sub(r'^例如[，、:：\s]*', '', t)
    return t


def main():
    terms = {t['id']: t for t in json.load(open(RESEARCH / 'terms.json', encoding='utf-8'))}
    order = [t['id'] for t in json.load(open(RESEARCH / 'terms.json', encoding='utf-8'))]
    research = {}
    for f in sorted(glob.glob(str(RESEARCH / 'research_*.json'))):
        g = json.load(open(f, encoding='utf-8'))
        for e in g['entries']:
            e['_group'] = g['group']
            research[e['id']] = e
    extra = sorted(glob.glob(str(RESEARCH / 'new_*.json')))
    for f in extra:
        e = json.load(open(f, encoding='utf-8'))
        research[e['id']] = e
        if e['id'] not in order:
            order.append(e['id'])
    src_lookup = {}
    for e0 in research.values():
        for s0 in e0.get('sources', []):
            if s0.get('pmid'):
                src_lookup.setdefault(str(s0['pmid']), s0)
    out = []
    for tid in order:
        if tid in DROP:
            continue
        e = dict(research[tid])
        ed = EDITS.get(tid, {})
        for k, v in ed.items():
            if k == 'drop_pmids':
                continue
            e[k] = v if v is not None else ''
        if ed.get('drop_pmids'):
            e['evidence'] = [x for x in e['evidence'] if str(x.get('pmid')) not in ed['drop_pmids']]
            e['sources'] = [x for x in e['sources'] if str(x.get('pmid')) not in ed['drop_pmids']]
        cat = e.get('cat') or terms.get(tid, {}).get('cat')
        cat = CAT_FIX.get(cat, cat)
        if tid in ALLERGY:
            cat = 'allergy'
        entry = {
            'id': tid,
            'cat': cat,
            'term': e['term'],
            'en': e.get('en') or EN.get(tid, e.get('aka', '')),
            'aliases': e['aliases'],
            'def': e['def'],
            'example': clean_example(e.get('example')),
            'note': (e.get('note') or '').strip(),
            'label': e.get('label', ''),
            'scope': 'page' if tid in PAGE_SCOPE else 'card',
            'exclude_pages': EXCLUDE_PAGES.get(tid, []),
            'sources': e.get('sources', []),
            'evidence': e.get('evidence', []),
            'aka': e.get('aka', ''),
            'confidence': e.get('confidence', ''),
            'reviewer_notes': e.get('reviewer_notes', ''),
            'group': e.get('_group', e.get('group', '')),
        }
        postfix.apply(entry, src_lookup)
        entry['example'] = clean_example(entry['example'])
        assert entry['def'], tid
        assert entry['cat'] in dict(CATS), (tid, entry['cat'])
        pm_src = {str(x.get('pmid')) for x in entry['sources']}
        for x in entry['evidence']:
            assert not x.get('pmid') or str(x['pmid']) in pm_src, (tid, 'evidence PMID without source', x.get('pmid'))
        out.append(entry)
    # alias collisions
    seen = {}
    for e in out:
        for a in e['aliases']:
            assert a not in seen, (a, seen.get(a), e['id'])
            seen[a] = e['id']
    data = {'version': '2026-10-07', 'categories': [{'id': c, 'name': n} for c, n in CATS], 'stop': STOP,
            'entries': out}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    json.dump(data, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(len(out), 'entries ->', OUT)
    for e in out:
        n = len(e['def'])
        if n > 90:
            print('  long def', e['id'], n)
        if len(e['note']) > 60:
            print('  long note', e['id'], len(e['note']))


if __name__ == '__main__':
    main()
