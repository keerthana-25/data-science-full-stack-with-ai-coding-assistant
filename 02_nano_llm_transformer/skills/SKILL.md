# Reproduce NanoLlama Language Model Lab

## Goal
Recreate the experiment from a clean checkout and verify the result.

## Steps
1. Install dependencies from the top-level `requirements.txt`.
2. Read `prompts.md` and `DATASET.md`.
3. Run `python src/experiment.py` from this project directory.
4. Confirm `artifacts/metrics.json`, `artifacts/result.png`, and `dashboard.html` were generated.
5. Open the dashboard and compare the displayed metrics with the JSON file.
6. Review `AUDIT_REPORT.md`.
7. If code changes, rerun the experiment and replace the screenshot.
