# Data Science Visual Foundations

**Domain:** Data science education

## What this does

A Naive Bayes classifier, a confusion matrix breakdown, a gradient descent simulation, and a small quiz bank.

Builds classic ML concepts (Naive Bayes, confusion matrix, gradient descent) from first principles instead of only calling a library function.

## Dataset

Reference dataset/theme: **Iris + generated mathematical examples**. This project uses a small, deterministic, offline dataset (built-in scikit-learn data or a seeded synthetic equivalent) so it runs the same way on any laptop without external credentials or network access. See `prompts.md` for how this maps to the original prompt.

## How to run

```bash
pip install -r requirements.txt      # once, from the repository root
python 08_datascience_visual_mastery/src/experiment.py
```

Then open `08_datascience_visual_mastery/dashboard.html` in a browser.

## Results (this run)

| Metric | Value |
|---|---|
| accuracy | 0.9211 |
| gradient_steps | 18 |

Full numbers are also saved to `artifacts/metrics.json` and `artifacts/result.png` every time the script runs, so this table never goes stale.

## Screenshots

![Dashboard results](docs/screenshots/dashboard_01.png)
![Dashboard details](docs/screenshots/dashboard_02.png)

## Prompt

See [`prompts.md`](prompts.md) for the exact prompt used to build this project.
