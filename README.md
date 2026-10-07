# Cultural Bias in Dementia Assessment

**Reproducible experiments for asking whether a cognitive score changes when language and cultural context change.**

This repository accompanies my research into cultural and linguistic assumptions in dementia assessment, particularly ADAS-Cog.

## Research question

A standardised score looks objective. But if a patient recognises a concept in one language or cultural frame and not another, is the score measuring memory alone?

I use reproducible synthetic experiments here to explore that problem without exposing patient data.

## Project chronology

- The underlying dementia-assessment work **predates this repository**.
- **2026:** the research expanded into follow-up questions about language, culture, and what a standardised score is actually measuring.
- **October 2026:** this public reproducibility layer was consolidated on GitHub using synthetic data so the analysis logic could be inspected without exposing participant data.

## What is included

- Deterministic synthetic datasets
- Illustrative analysis plans
- Paired-comparison workflows
- Explicit missing-data handling
- Seeded percentile-bootstrap examples
- Dependency-free Python analysis CLI
- Browser-based data explorer

## Example analysis

```bash
python3 -m analysis.cli data/scenarios/balanced-en.csv --format markdown
python3 -m unittest discover -s tests_py
```

## Why synthetic data?

The aim of this public repository is to make the *analysis logic* inspectable while protecting research participants. No patient-identifiable clinical data is included.

## Repository structure

- `analysis/` — analysis code
- `data/` — synthetic scenarios
- `src/` — browser explorer
- `tests/`, `tests_py/` — reproducibility and integrity checks
- `docs/` — research, architecture, and provenance notes

## Provenance

The research question and project direction come from my dementia-assessment work. The public reproducibility/demo layer was created later with AI-assisted development tools and uses synthetic data; it is not represented as recovered clinical production code. See `docs/PROVENANCE.md` and `NOTICE.md`.

[See the broader project timeline →](https://github.com/aahana-gupta-ai/aahana-gupta-ai/blob/main/PROJECT_TIMELINE.md)

**Themes:** cognitive science · dementia · cultural bias · data analysis · reproducible research
