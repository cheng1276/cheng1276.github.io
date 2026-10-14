"""Evidence-location wording in the glossary, requested by the reviewing physician on 2026-10-14.

Applied by merge.py after postfix_2026_10_12.py. The evidence panel shows each quote's location and access
publicly; these notes now describe the source (section, table, entry, what the explanation leaves out) instead of
how a copy was read or extracted (PMC extraction, PMC or PubMed record, publisher PDF, character codes). Citation
markers that remain in quotes are described as omitted citations. Two quotes are corrected where extraction lost
text: the pneumococcal quote starts with an ellipsis where the species name was lost, and the CKD quote has the
unit "m²". Each change states the text it replaces; check_all_used() (called by merge.py) stops the merge if any
mapped text was not found.
"""

LOCATION = {
    "Table 1 ('Descriptions and examples of interventions included in the integrative management of rheumatoid arthritis guideline'); PMC page and CDC Stacks author manuscript p.19":
        "Table 1 ('Descriptions and examples of interventions included in the integrative management of rheumatoid arthritis guideline')",
    'Section "Health-Related Fitness And Associated Physiological Changes", paragraph 1. The PMC text extraction reads "Third,refers to an individual’s range of motion around a joint, or group of joints." (italic word dropped); "flexibility" restored as on the PMC page':
        'Section "Health-Related Fitness And Associated Physiological Changes", paragraph 1',
    'Section "Health-Related Fitness And Associated Physiological Changes", paragraph 1. The PMC text extraction drops the italic subject "CRF" ("components., also known as …"); restored as on the PMC page':
        'Section "Health-Related Fitness And Associated Physiological Changes", paragraph 1',
    'Plain language summary (PMC record of the Cochrane review)':
        'Plain language summary (Cochrane review)',
    'Abstract, Background (text as displayed in the PMC record, which uses the hyphen character U+2010 in low‐technology)':
        'Abstract, Background',
    'PMC full text ("kg/m²" glued in the PMC extraction, replaced by …)':
        "Full text ('…' replaces the unit kg/m²)",
    'Live attenuated vaccines section ("()" = stripped citation markers)':
        "Live attenuated vaccines section ('()' marks omitted citations)",
    'Introduction, first sentence ("[,]" = stripped citation markers)':
        "Introduction, first sentence ('[,]' marks omitted citations)",
    'Results ("()" = stripped citation markers)':
        "Results ('()' marks omitted citations)",
    'Introduction (first sentence; italic species name dropped by extraction)':
        "Introduction (first sentence; '…' replaces the species name)",
    'Key question 7 (Cochrane review; "[]" = stripped citation number)':
        "Key question 7 (Cochrane review; '[]' marks an omitted citation number)",
    "Table 6 (CSU column); quoted only up to '> 6 weeks' because the next word is glued in the PMC extraction":
        "Table 6 (CSU column); quoted up to '> 6 weeks'",
    'Plain language summary (in the PMC record)':
        'Plain language summary',
    'Section on ocular management (empty brackets are stripped citation markers)':
        'Section on ocular management (empty brackets mark omitted citations)',
    'Eye section ("[]" = stripped citation markers)':
        "Eye section ('[]' marks omitted citations)",
    'Box 1 Glossary of terms, entry "Systematic review" (the bold term label is missing from the PMC text extraction; label as on bmj.com)':
        'Box 1 Glossary of terms, entry "Systematic review"',
    'Box 1 Glossary of terms, entry "Statistical synthesis" (label missing from the PMC text; as on bmj.com)':
        'Box 1 Glossary of terms, entry "Statistical synthesis"',
    'Box 1 Glossary of terms, entry "Meta-analysis of effect estimates" (label missing from the PMC text; as on bmj.com)':
        'Box 1 Glossary of terms, entry "Meta-analysis of effect estimates"',
    'Introduction (sentence continues after an extraction-glued comma; not quoted further)':
        'Introduction (quoted in part; the sentence continues)',
    "Abstract (first of three key refinements; the dash in '50‒64' is printed as U+2012)":
        'Abstract (first of three key refinements)',
    "Plain language summary, 'What is osteoarthritis and what is transcutaneous electrostimulation?' (PMC record; 'battery‐operated' is printed with U+2010)":
        "Plain language summary, 'What is osteoarthritis and what is transcutaneous electrostimulation?'",
    'Plain language summary (PMC record)':
        'Plain language summary',
    "Results (PMC text of the Arthritis Care & Research version), text under the TENS recommendation (the heading itself is not quoted because the PMC text drops 'against')":
        'Results (Arthritis Care & Research version), text under the TENS recommendation',
    'Results (PMC text of the Arthritis Care & Research version), physical approaches (no dropped word in this heading)':
        'Results (Arthritis Care & Research version), physical approaches',
    "Plain language summary, 'Background: What is osteoarthritis and what are braces and orthoses?' (PMC record)":
        "Plain language summary, 'Background: What is osteoarthritis and what are braces and orthoses?'",
    "Commentary text (consecutive sentences; the PMC text prints 'OA.The' because a citation was removed between them)":
        "Commentary text (consecutive sentences; '…' replaces a citation)",
    "Abstract (Authors' conclusions; PMC record prints 'Moderate‐quality' with U+2010)":
        "Abstract (Authors' conclusions)",
    "Results (PMC text of the Arthritis Care & Research version), text under the wedged-insole recommendation (heading not quoted: the PMC text drops 'against')":
        'Results (Arthritis Care & Research version), text under the wedged-insole recommendation',
    "Plain language summary, 'What is osteoarthritis and glucosamine?' (PMC record)":
        "Plain language summary, 'What is osteoarthritis and glucosamine?'",
    "Results (PMC text of the Arthritis Care & Research version), pharmacologic approaches, text under the glucosamine recommendation (citation brackets follow 'US')":
        'Results (Arthritis Care & Research version), pharmacologic approaches, text under the glucosamine recommendation',
    "Results (PMC text of the Arthritis Care & Research version), text under the glucosamine recommendation (heading not quoted: the PMC text drops 'against')":
        'Results (Arthritis Care & Research version), text under the glucosamine recommendation',
    "Table 2, Recommendation 1.1, remark (the PMC text drops the list of examples that follows 'such as:')":
        'Table 2, Recommendation 1.1, remark (quoted in part)',
    'Section "Bone mineral density (BMD) measurement and classification" (sentence continues with "(g/cm)", whose superscript was lost in extraction; quote stops before it)':
        'Section "Bone mineral density (BMD) measurement and classification" (quoted in part; the sentence continues with the unit)',
    'Glossary, entry on bone mineral density (term labels are not present in the PMC extraction; entry identified by its content)':
        'Glossary, entry on bone mineral density',
    'Section "Background" (followed by a stripped citation "[]")':
        'Section "Background"',
    'Glossary, entry on risk factors (term labels are not present in the PMC extraction; entry identified by its content)':
        'Glossary, entry on risk factors',
    'Glossary, entry on fracture (term labels are not present in the PMC extraction; entry identified by its content)':
        'Glossary, entry on fracture',
    'Section "Management of symptomatic osteoporotic vertebral fractures" (followed by a stripped citation and "(Evidence level Ia)")':
        'Section "Management of symptomatic osteoporotic vertebral fractures" (in the source, the sentence is followed by "(Evidence level Ia)")',
    'Glossary, entry on remodeling (term labels are not present in the PMC extraction; the sentence names its own term)':
        'Glossary, entry on remodeling',
    'Section "Transition of bone protective agents" (followed by stripped citations ".,")':
        'Section "Transition of bone protective agents"',
    'Abstract, first sentence (identical in PubMed abstract and PMC text)':
        'Abstract, first sentence',
    "Abstract (Conclusion; quoted up to the point before the glued word 'erosivedisease')":
        'Abstract (Conclusion; quoted in part)',
    'Abstract (PubMed; the PMC copy drops the italic organism name)':
        'Abstract',
    "Introduction, first paragraph ('[]' = stripped citation)":
        "Introduction, first paragraph ('[]' marks an omitted citation)",
    'Abstract (background); the same sentence opens the PMC executive summary, where the organism name is dropped':
        'Abstract (background); the same sentence opens the executive summary',
    "Introduction ('()' = stripped citation)":
        "Introduction ('()' marks an omitted citation)",
    "Abstract (PubMed; 'They' = the TST and the IGRA; the PMC copy drops the italic organism names)":
        "Abstract ('They' = the TST and the IGRA)",
    "'Interpretation of Screening Tests' ('()' = stripped citation)":
        "'Interpretation of Screening Tests' ('()' marks an omitted citation)",
    "Table 1 'Interpretation of screening test results for hepatitis B virus infection and recommended actions'; columns: Clinical state / HBsAg / Anti-HBs / Total anti-HBc / IgM anti-HBc / Action ('/' marks cell breaks in the extracted table)":
        "Table 1 'Interpretation of screening test results for hepatitis B virus infection and recommended actions'; columns: Clinical state / HBsAg / Anti-HBs / Total anti-HBc / IgM anti-HBc / Action ('/' marks cell breaks)",
    "Section 6D.2 'Screening Recommendations in the Setting of Immunosuppressive or Cytotoxic Drugs' ('(–)' = stripped citations)":
        "Section 6D.2 'Screening Recommendations in the Setting of Immunosuppressive or Cytotoxic Drugs' ('(–)' marks omitted citations)",
    "Section 6D.1 ('(–)' = stripped citations)":
        "Section 6D.1 ('(–)' marks omitted citations)",
    "'Immunopathogenesis of hepatitis due to HBV reactivation' (sentence ends with a figure reference whose number was dropped in extraction; quoted up to 'failure')":
        "'Immunopathogenesis of hepatitis due to HBV reactivation' (quoted up to 'failure'; the sentence ends with a figure reference)",
    "Rationale for R 2.11 ('(,,)' = stripped citations)":
        "Rationale for R 2.11 ('(,,)' marks omitted citations)",
    "Table 4 (title, then two of its rows under 'Secondary immune deficiencies'; '/' marks line breaks in the extracted table)":
        "Table 4 (title, then two of its rows under 'Secondary immune deficiencies'; '/' marks line breaks)",
    'Glossary of terms (the entry heading is missing from the PMC extraction)':
        'Glossary of terms',
    'Table 1 (PA Rating System for UVA Protection); table cells read in order, whitespace normalised':
        'Table 1 (PA Rating System for UVA Protection); cells in reading order',
    'Section "Anti-resorptive drugs: denosumab" (non-breaking spaces as in source; the dose is not used in the Chinese text)':
        'Section "Anti-resorptive drugs: denosumab" (the explanation gives no dose)',
    'Table 8 (stress dosing), one cell; in the PMC extraction the cell boundaries run into the neighbouring cells, but the quoted words are intact (doses in the table are not used)':
        "Table 8 (stress dosing), one cell (the explanation gives none of the table's doses)",
    "Results, 'Pneumocystis jirovecii' ('()' = stripped citation; doses are not printed)":
        "Results, 'Pneumocystis jirovecii' ('()' marks an omitted citation; the explanation gives no doses)",
    'Abstract (PubMed)':
        'Abstract',
    'Abstract (Recommendations); the PMC \'Summary and call-to-action\' section has a reworded version ("Sarcopenia, i.e. muscle failure, is a muscle disease rooted in adverse muscle changes that accrue across a lifetime; …")':
        'Abstract (Recommendations); the \'Summary and call-to-action\' section has a reworded version ("Sarcopenia, i.e. muscle failure, is a muscle disease rooted in adverse muscle changes that accrue across a lifetime; …")',
    'Abstract (Results; PubMed version)':
        'Abstract (Results)',
    'Abstract (superscript "2" after "m" lost in the PubMed text)':
        'Abstract',
    'Author affiliation (PubMed record)':
        'Author affiliation',
    'Definition of obesity (PMC full text)':
        'Definition of obesity',
    'Introduction (PMC version)':
        'Introduction',
    'Methods (PMC full text)':
        'Methods',
    "Methods, 'Paraffin therapy' (non-breaking space in '20 minutes' written as an ordinary space; citation brackets follow 'removed' in the source)":
        "Methods, 'Paraffin therapy'",
    "Methods, 'Paraffin therapy' (non-breaking space in '8 weeks' written as an ordinary space)":
        "Methods, 'Paraffin therapy'",
    'Table 1 (Descriptions and examples of interventions), row: Activity pacing (PMC table page)':
        'Table 1 (Descriptions and examples of interventions), row: Activity pacing',
    'Table 1 (Descriptions and examples of interventions), row: Adaptive equipment (PMC table page)':
        'Table 1 (Descriptions and examples of interventions), row: Adaptive equipment',
    'Table 1 (Descriptions and examples of interventions), row: Assistive devices (PMC table page)':
        'Table 1 (Descriptions and examples of interventions), row: Assistive devices',
    'Table 1 (Descriptions and examples of interventions), row: Bracing and orthoses (PMC table page)':
        'Table 1 (Descriptions and examples of interventions), row: Bracing and orthoses',
    'Table 1 (Descriptions and examples of interventions), row: Chiropractic (PMC table page)':
        'Table 1 (Descriptions and examples of interventions), row: Chiropractic',
    'Table 1 (Descriptions and examples of interventions), row: Cognitive behavioral therapy (PMC table page)':
        'Table 1 (Descriptions and examples of interventions), row: Cognitive behavioral therapy',
    'Table 1 (Descriptions and examples of interventions), row: Comprehensive occupational therapy (PMC table page)':
        'Table 1 (Descriptions and examples of interventions), row: Comprehensive occupational therapy',
    'Table 1 (Descriptions and examples of interventions), row: Comprehensive physical therapy (PMC table page)':
        'Table 1 (Descriptions and examples of interventions), row: Comprehensive physical therapy',
    'Table 1 (Descriptions and examples of interventions), row: Environmental adaptations (PMC table page)':
        'Table 1 (Descriptions and examples of interventions), row: Environmental adaptations',
    'Table 1 (Descriptions and examples of interventions), row: Joint protection techniques (PMC table page)':
        'Table 1 (Descriptions and examples of interventions), row: Joint protection techniques',
    'Table 1 (Descriptions and examples of interventions), row: Self-management program (PMC table page)':
        'Table 1 (Descriptions and examples of interventions), row: Self-management program',
    'Table 1 (Descriptions and examples of interventions), row: Vocational rehabilitation (PMC table page)':
        'Table 1 (Descriptions and examples of interventions), row: Vocational rehabilitation',
    'Table 1 (Descriptions and examples of interventions), row: Work site evaluation and modifications (PMC table page)':
        'Table 1 (Descriptions and examples of interventions), row: Work site evaluation and modifications',
    'Table 1 (definitions of the interventions), row "Aerobic exercise" (PMC table page)':
        'Table 1 (definitions of the interventions), row "Aerobic exercise"',
    'Table 1 (definitions of the interventions), row "Resistance exercise" (PMC table page)':
        'Table 1 (definitions of the interventions), row "Resistance exercise"',
    'Title (PubMed record)':
        'Title',
    'Title (PubMed record; no abstract)':
        'Title (the article has no abstract)',
    'Title (PubMed record; capitalisation as indexed)':
        'Title',
    'Title (PubMed record; consensus paper from ESCEO, IOF and IFCC)':
        'Title (consensus paper from ESCEO, IOF and IFCC)',
    'Title (PubMed record; EASI position paper)':
        'Title (EASI position paper)',
    'Title (PubMed record; APASL consensus)':
        'Title (APASL consensus)',
    'Title (PubMed record; AASLD practice guidance)':
        'Title (AASLD practice guidance)',
    'Author affiliation (PubMed record of an Endocrine Society guideline communication)':
        'Author affiliation (Endocrine Society guideline communication)',
    'Abstract (Results; PMC author-manuscript version)':
        'Abstract (Results; author manuscript)',
}
ACCESS = {
    "PMC full text (the word 'i.e.' before 'a 12-ounce' is missing from the PMC text extraction; as on the PMC page)":
        'PMC full text',
    'PMC full text (plain language summary in the PMC record)':
        'PMC full text (plain language summary)',
}
QUOTES = {
    ('pneumococcal', '(pneumococcus) is a common bacterial cause of respiratory tract infections, bacteremia, and meningitis.'):
        '… (pneumococcus) is a common bacterial cause of respiratory tract infections, bacteremia, and meningitis.',
    ('ckd', 'The definition and classification of chronic kidney disease (CKD) have evolved over time, but current international guidelines define this condition as decreased kidney function shown by glomerular filtration rate (GFR) of less than 60 mL/min per 1·73 m, or markers of kidney damage, or both, of at least 3 months duration, regardless of the underlying cause.'):
        'The definition and classification of chronic kidney disease (CKD) have evolved over time, but current international guidelines define this condition as decreased kidney function shown by glomerular filtration rate (GFR) of less than 60 mL/min per 1·73 m², or markers of kidney damage, or both, of at least 3 months duration, regardless of the underlying cause.',
}
USED = set()


def apply(e):
    for x in e['evidence']:
        loc = x.get('location', '')
        if loc in LOCATION:
            USED.add(('location', loc))
            x['location'] = LOCATION[loc]
        acc = x.get('access', '')
        if acc in ACCESS:
            USED.add(('access', acc))
            x['access'] = ACCESS[acc]
    for (eid, old), new in QUOTES.items():
        if eid != e['id']:
            continue
        hits = [x for x in e['evidence'] if x['quote'] == old]
        assert len(hits) == 1, (eid, 'quote not found', old[:60])
        hits[0]['quote'] = new
        USED.add(('quote', eid))
    return e


def check_all_used(entries):
    """Every mapped text must have been found and replaced."""
    missing = [k for k in LOCATION if ('location', k) not in USED] + [k for k in ACCESS if ('access', k) not in USED]
    missing += [eid for (eid, _old) in QUOTES if ('quote', eid) not in USED]
    assert not missing, ('postfix_2026_10_14: mapped text not found', missing[:3])
