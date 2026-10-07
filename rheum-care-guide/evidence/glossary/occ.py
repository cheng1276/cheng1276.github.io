"""Find where each glossary alias occurs on the site (same matching rules as the site's JavaScript).

Rules
- Longest alias wins at each position; a matched alias is consumed (no shorter alias inside it).
- Latin-script aliases need a non-alphanumeric character (or text edge) on both sides.
- Terms excluded on a page are consumed but not linked there.
- Linking: first occurrence per scope. Scope = card (or intro / myths / seek block), or the whole page for
  entries whose scope is 'page'.

Usage (from the rheum-care-guide folder): python3 evidence/glossary/occ.py [--md out.md]
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
CONTENT = HERE.parent.parent / 'src' / 'content'
GLOSSARY = HERE.parent.parent / 'src' / 'glossary' / 'glossary.json'
ORDER = ['common', 'gout', 'urticaria', 'ra', 'axspa', 'sle', 'sjogren']
LATIN = re.compile(r'[A-Za-z0-9]')


def load_glossary():
    g = json.load(open(GLOSSARY, encoding='utf-8'))
    return g


def alias_index(entries, stop=()):
    idx = {}
    for a in stop:
        idx.setdefault(a[0], []).append((a, None))
    for e in entries:
        for a in e['aliases']:
            idx.setdefault(a[0], []).append((a, e['id']))
    for k in idx:
        idx[k].sort(key=lambda x: -len(x[0]))
    return idx


def matches(text, idx):
    """Yield (start, end, alias, term_id) for the longest-match segmentation."""
    i = 0
    n = len(text)
    while i < n:
        hit = None
        for a, tid in idx.get(text[i], ()):
            if not text.startswith(a, i):
                continue
            if LATIN.match(a[0]) and i > 0 and LATIN.match(text[i - 1]):
                continue
            if LATIN.match(a[-1]) and i + len(a) < n and LATIN.match(text[i + len(a)]):
                continue
            hit = (i, i + len(a), a, tid)
            break
        if hit:
            yield hit
            i = hit[1]
        else:
            i += 1


def site_items():
    """Yield (slug, scope_key, sid, field, text) in reading order."""
    for slug in ORDER:
        d = json.load(open(CONTENT / f'{slug}.json', encoding='utf-8'))
        yield slug, 'intro', f'{slug}-intro', 'intro', d['intro']
        for c in d['cards']:
            sk = c['id']
            yield slug, sk, c['id'], 'title', c['title']
            yield slug, sk, c['id'], 'summary', c['summary']
            for p in c['points']:
                yield slug, sk, p['sid'], 'text', p['text']
                yield slug, sk, p['sid'], 'label', p.get('strength_label', '')
            if c.get('tip'):
                t = c['tip']
                yield slug, sk, t['sid'], 'text', t['text']
                yield slug, sk, t['sid'], 'label', t.get('strength_label', '')
        for m in d.get('myths', []):
            yield slug, 'myths', m['sid'], 'belief', m['belief']
            yield slug, 'myths', m['sid'], 'fact', m['fact']
            yield slug, 'myths', m['sid'], 'label', m.get('strength_label', '')
        for s in d.get('seek_care', []):
            yield slug, 'seek', s['sid'], 'text', s['text']
            yield slug, 'seek', s['sid'], 'label', s.get('strength_label', '')


def run():
    g = load_glossary()
    entries = {e['id']: e for e in g['entries']}
    idx = alias_index(g['entries'], g.get('stop', []))
    occ = {tid: [] for tid in entries}
    linked_scope = {}
    for slug, sk, sid, field, text in site_items():
        for s, t, a, tid in matches(text, idx):
            if tid is None:
                continue
            e = entries[tid]
            if slug in e['exclude_pages']:
                occ[tid].append((slug, sid, field, a, text, 'excluded'))
                continue
            key = (slug, tid) if e['scope'] == 'page' else (slug, sk, tid)
            if key in linked_scope:
                status = 'repeat'
            else:
                linked_scope[key] = sid
                status = 'LINK'
            occ[tid].append((slug, sid, field, a, text, status))
    return g, occ


def main(argv):
    g, occ = run()
    out = []
    for e in g['entries']:
        rows = occ[e['id']]
        nl = sum(1 for r in rows if r[5] == 'LINK')
        out.append(f"\n## {e['id']} — {e['term']}  (aliases: {' / '.join(e['aliases'])}; scope: {e['scope']}; links: {nl}; occurrences: {len(rows)})")
        if not rows:
            out.append('  (no occurrence on the site)')
        for slug, sid, field, a, text, status in rows:
            out.append(f"- [{status}] {sid} ({field}) 「{a}」: {text}")
    md = '\n'.join(out)
    if '--md' in argv:
        pathlib.Path(argv[argv.index('--md') + 1]).write_text(md, encoding='utf-8')
    else:
        print(md)
    none = [e['id'] for e in g['entries'] if not occ[e['id']]]
    print('entries without occurrence:', none, file=sys.stderr)
    print('total links:', sum(1 for v in occ.values() for r in v if r[5] == 'LINK'), file=sys.stderr)


if __name__ == '__main__':
    main(sys.argv[1:])
