# Data Science Experiment Reproduction Portfolio

This repository contains my reproduction of 15 data science and machine learning projects, Projects 01 through 15, based on the prompt catalog provided in the reference repository. The goal is to show that I can use a coding assistant to recreate the experiments, understand the data science workflow, verify the output, and explain the work clearly.

I kept the implementations intentionally simple enough to run on a normal laptop and explain in a class walkthrough. Heavy external tools are optional. Every project includes a reproducible offline path.

## Reference

Reference repository: https://github.com/dlmastery/data_science_examples

The reference repository also contains Project 00, a dynamic todo application. I have not counted it among the 15 data science projects in this submission.

## Projects

| # | Project | Main topic |
|---|---|---|
| 01 | [NYC Taxi Trip Duration Predictor](01_nyc_taxi_trip_prediction/) | Supervised regression |
| 02 | [NanoLlama Language Model Lab](02_nano_llm_transformer/) | Language modeling |
| 03 | [Customer Intelligence Clustering](03_customer_segmentation_clustering/) | Unsupervised clustering |
| 04 | [Market Basket Pattern Mining](04_associative_pattern_mining/) | Association rule mining |
| 05 | [Data Science Skills Mastery Lab](05_data_science_skills_lab/) | End-to-end data science skills |
| 06 | [Anomaly Threat Intelligence](06_anomaly_detection/) | Anomaly detection |
| 07 | [AutoML Model Tournament](07_automl_autogluon/) | Automated model selection |
| 08 | [Data Science Visual Foundations](08_datascience_visual_mastery/) | Data science education |
| 09 | [FlowForge DAG Engine](09_flowforge_dag_engine/) | Data pipeline orchestration |
| 10 | [CRISP-DM Masters Platform](10_crispdm_masters_curriculum/) | Integrated CRISP-DM workflow |
| 11 | [Enterprise Data Science Audit](11_enterprise_ds_audit/) | Governance and reproducibility |
| 12 | [TimePulse Forecasting Engine](12_timeseries_forecasting/) | Time series forecasting |
| 13 | [CRISP-DM NYC TLC Audit Platform](13_crispdm_nyc_taxi_audit_platform/) | Audited regression and explainability |
| 14 | [Multimodal AutoML Suite](14_autogluon_multimodal_automl_suite/) | Multimodal classification |
| 15 | [SPY Time Series Forecasting Lab](15_spy_timeseries_sota_forecasting/) | Financial time series |

## Common project structure

Each project contains:

- `README.md` - simple explanation and run steps
- `prompts.md` - prompt used for reproduction
- `src/experiment.py` - runnable experiment
- `dashboard.html` - generated results dashboard
- `docs/screenshots/` - verified screenshot of the dashboard
- `abstract.md`, `paper.md`, `article.md` - writing artifacts requested in the assignment
- `IMPLEMENTATION_PLAN.md` - implementation steps
- `AUDIT_REPORT.md` - data science/reproducibility checks
- `skills/SKILL.md` - reproduction workflow
- `artifacts/metrics.json` and `artifacts/result.png` - generated experiment outputs

## Run all projects

```bash
python scripts/run_all.py
```

This uses Python, NumPy, pandas, scikit-learn, matplotlib and NetworkX. See `requirements.txt`.

## Submission documents

- [Verified results](RESULTS_SUMMARY.md)
- [Verification report](VERIFICATION.md)
- [Compliance matrix](COMPLIANCE_MATRIX.md)
- [Portfolio audit](AUDIT_REPORT.md)
- [Walkthrough script](VIDEO_SCRIPT.md)
- [GitHub push instructions](PUSH_TO_GITHUB.md)

## YouTube walkthrough

**Walkthrough video:** ADD_YOUTUBE_LINK_HERE

Before submission, record the walkthrough using `VIDEO_SCRIPT.md`, upload it to YouTube, and replace `ADD_YOUTUBE_LINK_HERE` in this README and in each project README.

## Verification

The repository includes `VERIFICATION.md`, produced after running every project and generating browser screenshots. I only mark checks as passed when they were actually run in this environment.
