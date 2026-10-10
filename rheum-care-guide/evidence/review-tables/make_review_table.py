"""Make a statement-by-statement review table (same layout as evidence/review-tables/*.md) from a content JSON."""
import json, sys, pathlib

def ev_cell(evs):
    out = []
    for e in evs or []:
        out.append(f"**{e.get('c','')} / {e.get('s','')}** ({e.get('confidence','')}; {e.get('strength','')}): “{e.get('quote','')}”")
    return '<br>'.join(out)

def esc(t):
    return (t or '').replace('|', '｜').replace('\n', ' ')

def main(slug, src_dir, out_dir):
    d = json.load(open(pathlib.Path(src_dir) / f'{slug}.json', encoding='utf-8'))
    L = [f"# {d['name']}（{slug}）", '', f"簡介：{d['intro']}", '',
         '| 編號 | 位置 | 網站文字 | 強度標示 | 依據（C-ID / S-ID：原文） |', '|---|---|---|---|---|']
    for c in d['cards']:
        for p in c['points']:
            L.append(f"| {p.get('sid','')} | {esc(c['title'])} | {esc(p['text'])} | {esc(p.get('strength_label',''))} | {esc(ev_cell(p.get('evidence')))} |")
        t = c.get('tip')
        if t:
            L.append(f"| {t.get('sid','')} | {esc(c['title'])}（小提醒） | {esc(t['text'])} | {esc(t.get('strength_label',''))} | {esc(ev_cell(t.get('evidence')))} |")
    for m in d.get('myths', []):
        L.append(f"| {m.get('sid','')} | 常見迷思 | 【常見說法】{esc(m['belief'])}　【說明】{esc(m['fact'])} | {esc(m.get('strength_label',''))} | {esc(ev_cell(m.get('evidence')))} |")
    for s in d.get('seek_care', []):
        L.append(f"| {s.get('sid','')} | 何時就醫 | {esc(s['text'])} | {esc(s.get('strength_label',''))} | {esc(ev_cell(s.get('evidence')))} |")
    L += ['', '## 來源']
    for s in d['sources']:
        L.append(f"- **{s['s']}** {s.get('short','')} — {s.get('citation','')} PMID: {s.get('pmid') or '—'}; DOI: {s.get('doi') or '—'}; URL: {s.get('url') or '—'}")
    if d.get('reviewer_notes'):
        L += ['', '## 審閱備註（撰寫者）'] + [f'- {n}' for n in d['reviewer_notes']]
    out = pathlib.Path(out_dir) / f'review_{slug}.md'
    out.write_text('\n'.join(L) + '\n', encoding='utf-8')
    n = sum(len(c['points']) + (1 if c.get('tip') else 0) for c in d['cards']) + len(d.get('myths', [])) + len(d.get('seek_care', []))
    print(out, n, 'statements')

if __name__ == '__main__':
    for slug in sys.argv[3:]:
        main(slug, sys.argv[1], sys.argv[2])
