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
TEMPLATE = HERE / 'template.html'
SITE_URL = 'https://cheng1276.github.io/rheum-care-guide/'

ORDER = ['common', 'gout', 'urticaria', 'ra', 'axspa', 'sle', 'sjogren']
TABS = {'common': '共通照護', 'gout': '痛風', 'urticaria': '慢性蕁麻疹', 'ra': '類風濕性關節炎',
        'axspa': '僵直性脊椎炎', 'sle': '紅斑性狼瘡', 'sjogren': '乾燥症'}

# Items the physician still has to decide (shown only in the review copy).
NOTES = {}  # notes for the reviewing physician are kept privately

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
    return data, n_stmt


def main(argv):
    review = '--review' in argv
    fragment = '--fragment' in argv
    out = pathlib.Path(argv[argv.index('--out') + 1]) if '--out' in argv else ROOT / 'index.html'
    data, n_stmt = build_data(review)
    blob = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    page = TEMPLATE.read_text(encoding='utf-8').replace('/*__DATA__*/', blob)
    if not review:
        page = page.replace('審閱模式：在每則建議下方顯示英文原文依據', '顯示每則建議的英文原文依據')
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
