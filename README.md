# Data Science Experiment Reproduction Portfolio

Fifteen small, runnable data science and ML projects, built with an AI coding assistant from the prompt catalog in [dlmastery/data_science_examples](https://github.com/dlmastery/data_science_examples). Each one is a compact, laptop-friendly version of the original prompt: same core idea, deterministic offline data, no special credentials or GPU required.

The reference repository also includes Project 00 (a todo app), which isn't a data science project and isn't reproduced here.

## Projects

| # | Project | Topic | Try it |
|---|---|---|---|
| 01 | [NYC Taxi Trip Duration Predictor](01_nyc_taxi_trip_prediction/) | Supervised regression | `python 01_nyc_taxi_trip_prediction/src/experiment.py` |
| 02 | [NanoLlama Language Model Lab](02_nano_llm_transformer/) | Language modeling | `python 02_nano_llm_transformer/src/experiment.py` |
| 03 | [Customer Intelligence Clustering](03_customer_segmentation_clustering/) | Unsupervised clustering | `python 03_customer_segmentation_clustering/src/experiment.py` |
| 04 | [Market Basket Pattern Mining](04_associative_pattern_mining/) | Association rule mining | `python 04_associative_pattern_mining/src/experiment.py` |
| 05 | [Data Science Skills Mastery Lab](05_data_science_skills_lab/) | End-to-end ML skills | `python 05_data_science_skills_lab/src/experiment.py` |
| 06 | [Anomaly Threat Intelligence](06_anomaly_detection/) | Anomaly detection | `python 06_anomaly_detection/src/experiment.py` |
| 07 | [AutoML Model Tournament](07_automl_autogluon/) | Automated model selection | `python 07_automl_autogluon/src/experiment.py` |
| 08 | [Data Science Visual Foundations](08_datascience_visual_mastery/) | ML concepts from scratch | `python 08_datascience_visual_mastery/src/experiment.py` |
| 09 | [FlowForge DAG Engine](09_flowforge_dag_engine/) | Pipeline orchestration | `python 09_flowforge_dag_engine/src/experiment.py` |
| 10 | [CRISP-DM Masters Platform](10_crispdm_masters_curriculum/) | Integrated CRISP-DM workflow | `python 10_crispdm_masters_curriculum/src/experiment.py` |
| 11 | [Enterprise Data Science Audit](11_enterprise_ds_audit/) | Repo governance/audit | `python 11_enterprise_ds_audit/src/experiment.py` |
| 12 | [TimePulse Forecasting Engine](12_timeseries_forecasting/) | Time series forecasting | `python 12_timeseries_forecasting/src/experiment.py` |
| 13 | [CRISP-DM NYC TLC Audit Platform](13_crispdm_nyc_taxi_audit_platform/) | Audited regression + explainability | `python 13_crispdm_nyc_taxi_audit_platform/src/experiment.py` |
| 14 | [Multimodal AutoML Suite](14_autogluon_multimodal_automl_suite/) | Multimodal classification | `python 14_autogluon_multimodal_automl_suite/src/experiment.py` |
| 15 | [SPY Time Series Forecasting Lab](15_spy_timeseries_sota_forecasting/) | Financial time series | `python 15_spy_timeseries_sota_forecasting/src/experiment.py` |

## What's in each project folder

- `README.md` - what it does, how to run it, and the latest results
- `prompts.md` - the exact prompt I gave the coding assistant, and how I adapted it to run offline
- `src/experiment.py` - the runnable experiment (fixed random seed, holdout/chronological evaluation where relevant)
- `dashboard.html` - a generated results dashboard (metrics, chart, CRISP-DM summary)
- `artifacts/metrics.json`, `artifacts/result.png` - generated outputs the README/dashboard are built from
- `docs/screenshots/` - rendered screenshots of the dashboard

## Setup and run

```bash
pip install -r requirements.txt

# run one project
python 01_nyc_taxi_trip_prediction/src/experiment.py
open 01_nyc_taxi_trip_prediction/dashboard.html

# run everything and regenerate all dashboards
python scripts/run_all.py

# sanity-check that every project has its required files
python scripts/verify_repo.py
```

Verified, generated results for all 15 projects are in [`RESULTS_SUMMARY.md`](RESULTS_SUMMARY.md).

## A note on reproduction vs. the original

These are lightweight reproductions of the core idea in each prompt, not feature-for-feature rebuilds of the (much larger) systems in the reference repository. Where a project would normally need an external dataset, GPU training, or a paid API, it instead uses a small deterministic built-in or synthetic dataset so anyone can clone this repo and get the same results with no credentials and no network access.

## YouTube walkthrough

**Video:** ADD_YOUTUBE_LINK_HERE

A walkthrough of the code and the dashboard UX for each of the 15 projects.
