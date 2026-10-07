"""Build the 風濕免疫生活照護圖解 site.

Usage:
  python3 src/build.py                 # public site -> index.html (full HTML document)
  python3 src/build.py --review --fragment --out PATH
                                       # review copy with physician notes, as an HTML fragment

Content lives in src/content/<slug>.json: every sentence carries the guideline quotes it rests on.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
CONTENT = HERE / 'content'
GLOSSARY = HERE / 'glossary' / 'glossary.json'
TEMPLATE = HERE / 'template.html'
SITE_URL = 'https://cheng1276.github.io/rheum-care-guide/'

ORDER = ['common', 'gout', 'urticaria', 'ra', 'axspa', 'sle', 'sjogren']
TABS = {'common': '共通照護', 'gout': '痛風', 'urticaria': '慢性蕁麻疹', 'ra': '類風濕性關節炎',
        'axspa': '僵直性脊椎炎', 'sle': '紅斑性狼瘡', 'sjogren': '乾燥症'}

# Items the physician still has to decide (shown only in the review copy).
NOTES = {
    'common': [
        '酒精：共通頁沒有放「少量飲酒不太可能影響病情」（EULAR 2021 中專家同意度最低的一條，也和痛風、蕁麻疹的建議衝突）；類風濕頁保留這句並附上限制條件。',
        '疫苗時機：EULAR 2019 偏好在病情穩定時接種，ACR 2022 則不論疾病活動度；網站只寫「和醫師一起決定」。',
        '類固醇骨骼保健：未寫 ACR 的劑量門檻（每天 2.5 毫克以上、超過 3 個月），也未寫「每天不超過 2 份酒」，因為原文沒有定義一份的量。',
        '體重：未列 BMI 數字，因為 WHO 與國健署的切點不同。',
    ],
    'gout': [
        '台灣痛風與高尿酸血症多專科共識（2018）只讀到摘要；「黃豆與植物性蛋白」一點只依據英國 BSR 2017，請確認是否符合您的立場。',
        '「發作期間繼續吃原本的降尿酸藥」只有 BSR 2017 與馬來西亞指引明寫，ACR、NICE、EULAR 沒有提到。',
        '「每天喝超過 2 公升水」只適用於曾有尿路結石的人，BSR 專家同意度 57%。',
        '「高果糖糖漿」是編輯加註的台灣食品標示用語，請確認。',
        'GT-4.2 刪去「可用支被架撐起棉被」：找不到 PubMed 收錄的支被架說明，病友也可能看不懂；如要保留，可改成白話（例如用支架把棉被撐高）。',
    ],
    'urticaria': [
        '「119」「請勿自行停藥」為在地化或安全加註；依查核意見，119 的條件已加入「舌頭或喉嚨腫脹」。',
        '熱、緊身衣物、喝酒只見於 2014 年美國與 2015 年英國指引，2026 國際指引沒有列出，網站以「可能」表述。',
        '未列出較安全止痛藥的名稱（國際指引提到 paracetamol、COX-2 抑制劑）；如需列出請告知。',
        'UAS7、UCT、AAS 有版權（GALEN、MOXIE），網站只說明計分方式；門診準備單裡的蕁麻疹日記也需要確認授權。',
        '配合名詞解釋的查核而修改：UR-2.3「全身性反應」改為「全身性的過敏反應」；「不會嗜睡的抗組織胺」改為「較不會嗜睡」（指引原文 minimally or nonsedating）；UAS7 改稱「蕁麻疹活動分數」，與「血管性水腫活動分數（AAS）」一致。',
        'UR-S1 改為「呼吸有咻咻聲、吸氣時有尖銳高音（喘鳴）」：網站依 WAO 用法以咻咻聲指 wheeze、喘鳴指 stridor，但台灣也常用「喘鳴」指 wheezing，請確認。',
    ],
    'ra': [
        '是否保留藥名 methotrexate、leflunomide（EULAR 原文所列）請決定。',
        '補充品一點加上「醫師開的葉酸、鈣片或維生素 D 請照醫囑使用」（編輯加註；ACR 註明葉酸另見藥物治療指引）。',
        'ACR 2022 的「不建議」項目（其他特定飲食法、整脊）在 PMC 文字檔漏掉 against，已由作者稿與其他版本確認方向。',
    ],
    'axspa': [
        'ACR/SAA/SPARTAN 2026 更新尚未正式出版；出版後需複查整脊、跌倒評估、水中運動等建議。',
        '「出現手腳麻木或無力請立即就醫」與「告知醫師您有僵直性脊椎炎」為編輯加註。',
        '「脊椎扳動手法／整脊」「推拿」的用詞請確認是否符合病友習慣。',
        'AS-3.3 的「磁振造影」後加註「（核磁共振）」，方便病友對照常用說法（編輯加註）。',
    ],
    'sle': [
        '維生素 D：英國 BSR 2026 強烈建議所有狼瘡患者全年每天補充（1B），EULAR 只建議視需要評估；網站採「和醫師討論」，請決定是否採用 BSR 立場。',
        'EULAR 2024 非藥物建議的強度字母（防曬 C、運動 C、有氧運動 B、心理社會介入 B）經兩次讀取一致，但還沒有人在 PDF 上確認。',
        '台灣 2026 紅斑性狼瘡共識只讀到摘要，懷孕計畫一卡請對照原文。',
        '「症狀很嚴重或突然惡化請立即就醫」為編輯加註。',
    ],
    'sjogren': [
        '「可能讓口乾的藥」依據一般族群的系統性回顧，不是乾燥症指引；「不要自行停藥」為編輯加註。',
        '油漱口（油拔法）的迷思已刪除，因為原指引呈現的證據有正有負。',
        '熱敷「溫熱不燙」為編輯加註。',
        'SJ-M1（針灸）已改寫：BSR 2025 引用的 Cochrane 回顧中，5 個針灸試驗的對象都是放射治療後口乾；乾燥症本身的假針灸對照試驗結果不一致（2022 年無差異；2025、2026 年報告有改善），所以改為「目前證據不足」，標示加上「研究顯示」。請確認是否同意。',
    ],
    'glossary': [
        '喘鳴與咻咻聲：依 WAO 用法，咻咻聲＝wheeze、喘鳴＝stridor（吸氣時的尖銳高音）；台灣也常用「喘鳴」指 wheezing，請確認。',
        'BMI：補充寫 WHO 國際分級（25 以上過重、30 以上肥胖），並註明亞洲人在 BMI 較低時風險就可能升高；國健署切點（24、27）沒有 PubMed 收錄的出處，是否另加請決定。',
        'UVA 防護等級：PA 等級的說明只找到一篇 Cureus 評論（證據力弱）；「PA+++ 代表高」取自該文表格，和英國狼瘡指引的「高」（UVA 標誌或 4–5 星）沒有正式對照。',
        '一份酒：毫升數（355、148、30–44 毫升）是由研究的盎司換算，屬編輯換算。',
        '良好實務建議：WHO 2020 把「有動總比沒動好」列為 good practice statement 的說法見於 WHO 指引全書（非 PubMed 收錄），請確認；詞條定義依 GRADE 方法學論文。',
        '物理治療：刪去「有助改善脊椎活動、體能與疼痛」的補充（出自 2008 年 Cochrane 回顧的背景句；2019 年回顧對脊椎活動度的效果仍不確定）。',
        '負重運動：此詞只連結在「類固醇與骨骼保健」卡片，例子刪去慢跑和網球（BHOF 指引列為骨質疏鬆者可能受傷的活動），補充加上「開始跑步、舉重等新運動前先請醫師評估」。',
        '夜間盜汗、唾液腺：補充不提淋巴瘤，和網站就醫提醒的語氣一致；但打開「英文原文依據」時，會看到含 lymphoma 的指引原文。',
        '消炎止痛藥：補充提醒「醫師為預防血栓開的低劑量阿斯匹靈，不一定要停用」；仍未列出較安全止痛藥的名稱。',
        'ACR 2022 類風濕性關節炎整合指引的表 1（運動、復健、飲食多個詞條的定義）在 PMC 文字檔中缺漏，只能以 WebFetch 讀取 PMC 表格頁與 CDC 收藏的作者稿兩份文件，內容一致，但無法機器比對。',
    ],
}

URL_FIX = {
    ('gout', 'S12'): 'https://mymahtas2.moh.gov.my/files/e-CPG_Management_of_Gout_(Second_Edition)%20(3).pdf',
}

DESCRIPTION = ('痛風、慢性蕁麻疹、類風濕性關節炎、僵直性脊椎炎、紅斑性狼瘡、乾燥症與共通照護的生活照護建議，'
               '每則都附臨床指引出處與建議強度。')

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
           "%3Crect width='64' height='64' rx='14' fill='%230c6a5e'/%3E"
           "%3Crect x='16' y='13' width='32' height='38' rx='5' fill='white'/%3E"
           "%3Cpath d='M22 25h20M22 32h20M22 39h12' stroke='%230c6a5e' stroke-width='4' stroke-linecap='round'/%3E%3C/svg%3E")

BASE_RESET = ('<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);'
              'padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}'
              '[hidden]{display:none!important}</style>')


def ev(items):
    return [{'c': e.get('c', ''), 's': e.get('s', ''), 'q': e.get('quote', ''),
             'st': e.get('strength', ''), 'cf': e.get('confidence', '')} for e in items or []]


def item(p):
    return {'t': p['text'], 'l': p.get('strength_label', ''), 'sid': p.get('sid', ''), 'ev': ev(p.get('evidence'))}


def glossary_data(review):
    g = json.load(open(GLOSSARY, encoding='utf-8'))
    entries = []
    srcs, src_index = [], {}

    def src_id(s):
        key = (s.get('pmid') or '', s.get('short') or '')
        if key not in src_index:
            src_index[key] = len(srcs)
            srcs.append({k: s.get(k) for k in ('short', 'citation', 'pmid', 'doi')})
        return src_index[key]

    for e in g['entries']:
        x = {'id': e['id'], 'cat': e['cat'], 'term': e['term'], 'en': e['en'], 'al': e['aliases'], 'def': e['def'],
             'ex': e['example'], 'note': e['note'], 'lab': e['label'], 'sc': e['scope'], 'xp': e['exclude_pages'],
             'src': [src_id(s) for s in e['sources']],
             'ev': [{'q': v['quote'], 'loc': v.get('location', ''), 'acc': v.get('access', ''), 'pmid': v.get('pmid', '')}
                    for v in e['evidence']]}
        if review:
            x['rn'] = e.get('reviewer_notes', '')
        entries.append(x)
    n_quotes = sum(len(e['evidence']) for e in g['entries'])
    return {'cats': g['categories'], 'stop': g.get('stop', []), 'entries': entries, 'srcs': srcs,
            'notes': NOTES.get('glossary', []) if review else [],
            'meta': {'n': len(entries), 'quotes': n_quotes}}


def build_data(review):
    common_src = {s['s']: s for s in json.load(open(CONTENT / 'common.json', encoding='utf-8'))['sources']}
    data = {'order': ORDER, 'diseases': {}, 'meta': {}}
    n_stmt = 0
    for slug in ORDER:
        d = json.load(open(CONTENT / f'{slug}.json', encoding='utf-8'))
        cards = []
        for c in d['cards']:
            cards.append({'id': c['id'], 'title': c['title'], 'summary': c['summary'],
                          'points': [item(p) for p in c['points']],
                          'tip': item(c['tip']) if c.get('tip') else None})
            n_stmt += len(c['points']) + (1 if c.get('tip') else 0)
        myths = [{'b': m['belief'], 'f': m['fact'], 'l': m.get('strength_label', ''), 'sid': m.get('sid', ''),
                  'ev': ev(m.get('evidence'))} for m in d.get('myths', [])]
        seek = [item(s) for s in d.get('seek_care', [])]
        n_stmt += len(myths) + len(seek)
        sources = []
        for s in d['sources']:
            s = dict(s)
            if (slug, s['s']) in URL_FIX:
                s['url'] = URL_FIX[(slug, s['s'])]
            if s['s'].startswith('common:') and not s.get('url'):
                base = common_src.get(s['s'].split(':', 1)[1])
                if base and base.get('url'):
                    s['url'] = base['url']
            if slug == 'sle' and s['s'] == 'S11':
                s['citation'] = re.sub(r'Lupus Sci Med 2026;13\(1\).*$', 'Lupus Sci Med 2026;13(1):e002027.', s['citation'])
            sources.append({k: s.get(k) for k in ('s', 'short', 'citation', 'pmid', 'doi', 'url')})
        data['diseases'][slug] = {'name': d['name'], 'tab': TABS[slug], 'intro': d['intro'], 'cards': cards,
                                  'myths': myths, 'seek': seek, 'sources': sources,
                                  'notes': NOTES.get(slug, []) if review else []}
    data['meta'] = {'statements': n_stmt, 'quotes': 348}
    data['glossary'] = glossary_data(review)
    return data, n_stmt


def main(argv):
    review = '--review' in argv
    fragment = '--fragment' in argv
    out = pathlib.Path(argv[argv.index('--out') + 1]) if '--out' in argv else ROOT / 'index.html'
    data, n_stmt = build_data(review)
    blob = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    page = TEMPLATE.read_text(encoding='utf-8').replace('/*__DATA__*/', blob)
    if not review:
        page = page.replace('審閱模式：顯示每則建議與名詞解釋的英文原文依據', '顯示每則建議與名詞解釋的英文原文依據')
    if not fragment:
        cut = page.index('</style>') + len('</style>')
        head, body = page[:cut], page[cut:]
        meta = '\n'.join([
            '<meta charset="utf-8">',
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">',
            BASE_RESET,
            head,
            f'<meta name="description" content="{DESCRIPTION}">',
            '<meta property="og:type" content="website">',
            '<meta property="og:locale" content="zh_TW">',
            '<meta property="og:title" content="風濕免疫生活照護圖解">',
            f'<meta property="og:description" content="{DESCRIPTION}">',
            f'<meta property="og:url" content="{SITE_URL}">',
            f'<meta property="og:image" content="{SITE_URL}og.png">',
            '<meta property="og:image:width" content="1200">',
            '<meta property="og:image:height" content="630">',
            '<meta name="twitter:card" content="summary_large_image">',
            '<meta name="theme-color" content="#0c6a5e">',
            f'<link rel="icon" href="{FAVICON}">',
        ])
        page = f'<!doctype html>\n<html lang="zh-Hant">\n<head>\n{meta}\n</head>\n<body>\n{body}\n</body>\n</html>\n'
    out.write_text(page, encoding='utf-8')
    print(f'{"review" if review else "public"} build: {n_stmt} statements, {len(page.encode("utf-8"))} bytes -> {out}')


if __name__ == '__main__':
    main(sys.argv[1:])
