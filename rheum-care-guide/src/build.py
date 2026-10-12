"""Build the 風濕免疫生活照護圖解 site.

Usage:
  python3 src/build.py                 # public site -> index.html (full HTML document)
  python3 src/build.py --review --fragment --out PATH
                                       # review copy with physician notes, as an HTML fragment
  python3 src/build.py --review --drafts DIR --fragment --out PATH
                                       # review copy that also shows the draft pages in DRAFT_ORDER,
                                       # read from DIR/<slug>.json (not part of the public site)

Content lives in src/content/<slug>.json: every sentence carries the guideline quotes it rests on.
"""
import json
import os
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
CONTENT = HERE / 'content'
GLOSSARY = HERE / 'glossary' / 'glossary.json'
TEMPLATE = HERE / 'template.html'
SITE_URL = 'https://cheng1276.github.io/rheum-care-guide/'

ORDER = ['common', 'gout', 'urticaria', 'ra', 'axspa', 'sle', 'sjogren',
         'oa', 'osteoporosis', 'labs', 'infection']  # the last four went live on 2026-10-11
# Pages drafted for physician review; shown only in a review build with --drafts.
DRAFT_ORDER = ['pregnancy']  # second batch, in physician review (2026-10-11)
TABS = {'common': '共通照護', 'gout': '痛風', 'urticaria': '慢性蕁麻疹', 'ra': '類風濕性關節炎',
        'axspa': '僵直性脊椎炎', 'sle': '紅斑性狼瘡', 'sjogren': '乾燥症',
        'oa': '退化性關節炎', 'osteoporosis': '骨質疏鬆症', 'labs': '健檢報告異常', 'infection': '治療期間防感染',
        'pregnancy': '懷孕、哺乳與避孕'}

# Notes for the reviewing physician (shown only in a review build). They are kept in a private repository,
# not in this public one: set RHEUM_NOTES_DIR, or keep a copy of that repository next to this one as
# ../rheum-care-guide-notes. Without it, review builds simply show no notes.
NOTES_DIR = pathlib.Path(os.environ.get('RHEUM_NOTES_DIR') or ROOT.parent.parent / 'rheum-care-guide-notes')


def _private_notes(name):
    p = NOTES_DIR / name
    return json.load(open(p, encoding='utf-8')) if p.exists() else {}


NOTES = _private_notes('build_notes.json')
GLOSSARY_NOTES = _private_notes('glossary_reviewer_notes.json')

URL_FIX = {
    ('gout', 'S12'): 'https://mymahtas2.moh.gov.my/files/e-CPG_Management_of_Gout_(Second_Edition)%20(3).pdf',
}

DESCRIPTION = ('痛風、類風濕性關節炎、紅斑性狼瘡、退化性關節炎、骨質疏鬆症等風濕免疫科常見疾病的生活照護，'
               '以及看懂健檢報告、治療期間防感染；每則建議都附出處與建議強度，少數安全提醒標為編輯加註。')

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
            x['rn'] = GLOSSARY_NOTES.get(e['id'], '')
        entries.append(x)
    n_quotes = sum(len(e['evidence']) for e in g['entries'])
    return {'cats': g['categories'], 'stop': g.get('stop', []), 'entries': entries, 'srcs': srcs,
            'notes': NOTES.get('glossary', []) if review else [],
            'meta': {'n': len(entries), 'quotes': n_quotes}}


def build_data(review, drafts=None):
    common_src = {s['s']: s for s in json.load(open(CONTENT / 'common.json', encoding='utf-8'))['sources']}
    order = ORDER + (DRAFT_ORDER if (review and drafts) else [])
    data = {'order': order, 'diseases': {}, 'meta': {}}
    n_stmt = 0
    for slug in order:
        base = drafts if slug in DRAFT_ORDER else CONTENT
        d = json.load(open(base / f'{slug}.json', encoding='utf-8'))
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
    # Quotes checked by the independent verification (reports kept privately since 2026-10-12):
    # 95 common+gout, 98 RA+axSpA, 74 SLE, 81 urticaria+Sjogren (first seven pages) = 348;
    # 75 OA, 88 osteoporosis, 43 labs, 57 infection (pages added 2026-10-11) = 263;
    # 14 quotes newly attached in the legal and dispute-risk revision, checked on 2026-10-12.
    data['meta'] = {'statements': n_stmt, 'quotes': 348 + 263 + 14}
    data['glossary'] = glossary_data(review)
    return data, n_stmt


def main(argv):
    review = '--review' in argv
    fragment = '--fragment' in argv
    out = pathlib.Path(argv[argv.index('--out') + 1]) if '--out' in argv else ROOT / 'index.html'
    drafts = pathlib.Path(argv[argv.index('--drafts') + 1]) if '--drafts' in argv else None
    if drafts and not review:
        sys.exit('--drafts is only allowed with --review')
    data, n_stmt = build_data(review, drafts)
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
