# Cultural Bias in Dementia Assessment

Reproducible experiments using synthetic research data.

**Package status:** runnable portfolio starter. Only the ADAS-Cog repository also contains supplied original web source in `legacy/`. Other project production code was not supplied. Newly generated code must not be represented as the original implementation.

## What works in this starter

- Thirty-six deterministic synthetic datasets and twelve illustrative analysis plans.
- Paired comparisons, explicit missingness, and seeded percentile-bootstrap examples.
- Dependency-free Python analysis CLI plus a browser explorer; no patient data is included.

## Run

```bash
python3 scripts/serve.py
```

Open http://127.0.0.1:8000. Use the bundled example content. No dependency install or account is required.

## Verify

```bash
node --test
node scripts/verify.mjs
```

## Python analysis

```bash
python3 -m analysis.cli data/scenarios/balanced-en.csv --format markdown
python3 -m unittest discover -s tests_py
```

## Contents

- `src/`: functioning browser application and reusable helpers.
- `data/`: indexed demonstration resources.
- `tests/`: behavior and data-integrity tests.
- `docs/`: architecture, provenance, integration limits, and workflow guides.
- `schemas/` and `examples/`: documented export formats.

Every project is packaged with exactly **160 files**, including code, resources, tests, and documentation; file count is not a measure of research quality.

## Topics

`data-science` `healthcare` `dementia` `cognitive-science` `research`

Set these through GitHub's About settings.

## Attribution and rights

Project identity and background come from the uploaded Aahana Gupta descriptions. Starter code and new example content were generated for this bundle. No new open-source license is assigned. Review `NOTICE.md` and `docs/PROVENANCE.md` before public distribution.
