# JIT-VP

Just-in-time vulnerability prediction for skill file updates on ClawHub. We collect skill version histories (changelogs + diffs) and study which changes introduce security issues.

## Files

| File | What it does |
|---|---|
| `dataset.ipynb` | Collects ClawHub skill version data used to build the dataset. |
| `load_dataset.ipynb` | Loads and cleans the dataset and builds the analysis frame for RQ1 (`rq1_frame.parquet`), including the SKILL.md language filter. |
| `rq1_sampling.ipynb` | Draws the RQ1 samples in rounds for open coding of changelogs and diffs, and reports each round. |
| `dataset_provenance.json` | Records where the data came from and how it was collected. |

## Data

The raw and processed data files (`.parquet`, `.jsonl`, `clawhub_content/`) are not in this repo because they are too large.
