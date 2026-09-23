# TimePulse Forecasting Engine

**Domain:** Time series forecasting

## What this does

A chronological train/test split, lag features, and a linear vs. random forest forecast comparison on MAE/RMSE.

Forecasts with lag features and a strictly chronological split so future data never leaks into training, unlike a random split.

## Dataset

Reference dataset/theme: **Airline-passenger style synthetic seasonal series**. This project uses a small, deterministic, offline dataset (built-in scikit-learn data or a seeded synthetic equivalent) so it runs the same way on any laptop without external credentials or network access. See `prompts.md` for how this maps to the original prompt.

## How to run

```bash
pip install -r requirements.txt      # once, from the repository root
python 12_timeseries_forecasting/src/experiment.py
```

Then open `12_timeseries_forecasting/dashboard.html` in a browser.

## Results (this run)

| Metric | Value |
|---|---|
| best_model | Linear |
| MAE | 1.9616 |
| RMSE | 2.5227 |
| chronological_split | True |

Full numbers are also saved to `artifacts/metrics.json` and `artifacts/result.png` every time the script runs, so this table never goes stale.

## Screenshots

![Dashboard results](docs/screenshots/dashboard_01.png)
![Dashboard details](docs/screenshots/dashboard_02.png)

## Prompt

See [`prompts.md`](prompts.md) for the exact prompt used to build this project.
