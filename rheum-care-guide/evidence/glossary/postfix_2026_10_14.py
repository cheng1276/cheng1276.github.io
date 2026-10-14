"""Evidence-location wording in the glossary, requested by the reviewing physician on 2026-10-14.

Applied by merge.py after postfix_2026_10_12.py. Drafting notes about what the glossary text uses are reworded
to describe the explanation itself; where the quote sits in the source is unchanged. Each change states the text
it replaces, and apply() stops if the merged entry no longer has that text.
"""

LOCATION = {
    'denosumab': (
        'Section "Anti-resorptive drugs: denosumab" (non-breaking spaces as in source; the dose is not used in the Chinese text)',
        'Section "Anti-resorptive drugs: denosumab" (non-breaking spaces as in source; the explanation gives no dose)'),
    'adrenal': (
        'Table 8 (stress dosing), one cell; in the PMC extraction the cell boundaries run into the neighbouring cells, but the quoted words are intact (doses in the table are not used)',
        "Table 8 (stress dosing), one cell; in the PMC extraction the cell boundaries run into the neighbouring cells, but the quoted words are intact (the explanation gives none of the table's doses)"),
    'pjp': (
        "Results, 'Pneumocystis jirovecii' ('()' = stripped citation; doses are not printed)",
        "Results, 'Pneumocystis jirovecii' ('()' = stripped citation; the explanation gives no doses)"),
}


def apply(e):
    ch = LOCATION.get(e['id'])
    if not ch:
        return e
    old, new = ch
    hits = [x for x in e['evidence'] if x.get('location') == old]
    assert len(hits) == 1, (e['id'], 'location not found', old)
    hits[0]['location'] = new
    return e
