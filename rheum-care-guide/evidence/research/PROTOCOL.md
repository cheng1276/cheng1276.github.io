# Evidence-gathering protocol (read fully before starting)

## Purpose
A Taiwanese rheumatologist is building a PUBLIC, patient-facing website of illustrated
lifestyle-care guides (生活照護圖解) for: gout, chronic urticaria, rheumatoid arthritis,
axial spondyloarthritis / ankylosing spondylitis, systemic lupus erythematosus, Sjögren's.
Every sentence on the site must trace to an authoritative source. Errors are unacceptable.
Your job is ONLY to build an evidence file. Do not write patient-facing Chinese text.

## Scope of claims to collect
Non-pharmacological self-care and lifestyle: diet, drinks, alcohol, weight, exercise /
physical activity, smoking, sun protection, triggers to avoid, eye / mouth / skin care,
home care during flares, sleep / stress / fatigue, work, infection-prevention behaviours,
and "seek care promptly / urgently if ..." statements (only when a source states them).
Medication-related items ONLY when they are a patient behaviour message stated by a
guideline (e.g. "continue urate-lowering therapy during a flare", "take antihistamines
regularly rather than on demand", "avoid NSAIDs if they aggravate urticaria").
Label these "medication-adjacent". Never record dosing of prescription drugs.

## Source hierarchy
- Tier 1: current clinical practice guidelines / recommendations from major bodies
  (ACR, EULAR, ASAS, EAACI/GA2LEN/WAO, AAAAI/ACAAI, BSR, NICE, Sjögren's Foundation,
  TFOS, WHO, APLAR, national societies incl. Taiwan). Use the most recent version and
  say whether an older one is superseded.
- Tier 2: systematic reviews / meta-analyses (incl. Cochrane).
- Tier 3: individual RCTs or large cohort studies, only when a Tier-1 guideline relies on
  them for the point, or for a landmark numeric fact.
- Exclude: narrative opinion pieces, non-peer-reviewed web pages, commercial or
  industry patient material, case reports, predatory journals.

## Tools
- PubMed MCP tools. Load them first with ToolSearch, query:
  "select:mcp__PubMed__search_articles,mcp__PubMed__get_article_metadata,mcp__PubMed__get_full_text_article,mcp__PubMed__convert_article_ids,mcp__PubMed__lookup_article_by_citation,mcp__PubMed__find_related_articles"
  search_articles returns PMIDs only; get_article_metadata returns title/abstract/DOI/PMCID;
  get_full_text_article returns PMC full text (only if a PMCID exists).
- Large tool outputs are saved to a JSON file whose path is shown; search it with
  python (json.load(...)['articles'][0]['full_text']) or Grep instead of reading it whole.
- WebSearch / WebFetch for guideline pages and publisher sites. Note: pmc.ncbi.nlm.nih.gov
  blocks WebFetch (reCAPTCHA); the shell cannot reach NCBI. Some publishers block too.

## CRITICAL extraction pitfall (confirmed in this project)
get_full_text_article DROPS words that were formatted in the original (bold/italic),
most dangerously the word "against". Real example from the 2020 ACR gout guideline
(PMC10563586): the text reads "Adding vitamin C supplementation is conditionally
recommendedfor patients with gout" — the real recommendation is "conditionally recommended
AGAINST". The same happens there for low-dose aspirin, fenofibrate, urine alkalinisation.
Telltale sign: two words glued together with no space ("recommendedfor", "recommendedin",
"recommendfor"). Rules:
- Before relying on any quote, check it for glued words or odd grammar. If present,
  assume a word is missing and confirm the true meaning from an independent source
  (the abstract, a co-published version, a summary table, the publisher page via
  WebFetch, or a reliable later paper that restates the recommendation). Write in Notes
  how you confirmed it. Never record a direction (for / against) you have not confirmed.
- Tables and figures are often missing from the extracted text. Recommendation strength
  may live in tables. If you cannot find the strength in accessible text, write
  "strength not found in accessible text" rather than guessing.

## Rules for every claim
1. Record only what you have actually read in THIS session. Never fill facts, numbers,
   strengths, years or PMIDs from memory.
2. Paste the exact supporting quote (verbatim, English) and its location (section,
   recommendation number, or table).
3. Mark access level: full text / abstract only / secondary source.
4. Keep numbers and units exactly as stated. Record population restrictions
   (e.g. "overweight/obese patients only", "cutaneous lupus patients").
5. If sources conflict, record both and flag the conflict.
6. Common beliefs that are NOT supported, recommended against, or have insufficient
   evidence go in the "Myths / not recommended / insufficient evidence" section, with
   the source.
7. Get PMID, DOI and PMCID for every source via get_article_metadata.

## Output file (write with the Write tool) at the path given in your task
Markdown with these sections:

### A. Sources
Table: S-ID | Citation (first author et al., title, journal, year;vol:pages) | Organisation
| Type/tier | PMID | DOI | PMCID | Access (full text / abstract) | Superseded? / notes

### B. Claims
One row per atomic claim:
C-ID | Topic | Claim (precise English) | Plain-language takeaway (English) | S-ID |
Verbatim quote | Location | Strength / level as stated | Confidence | Notes
Confidence: High = explicit in Tier-1 full text you read; Medium = Tier-2, or Tier-1
abstract only; Low = secondary source or indirect.

### C. Myths / not recommended / insufficient evidence

### D. Taiwan-specific sources (or "none found" + the queries you ran)

### E. Could not verify / open questions

### F. Search log (queries run, one line each)

When finished, reply with a summary of at most 300 words: the main sources, the
strongest takeaways, anything you could not verify, and the output file path.
