# YouTube Walkthrough Script

Target length: about 12 to 18 minutes. Speak naturally and show the code and dashboard for every project.

## Opening

Hi, this repository is my reproduction of fifteen data science experiments using a coding assistant. I will briefly show the repository structure, the prompt used for each project, the experiment, the result dashboard, and the audit notes.

## Project 01: NYC Taxi Trip Duration Predictor

Open `01_nyc_taxi_trip_prediction`. Show `prompts.md`, then `src/experiment.py`, then `dashboard.html`. Explain: Synthetic NYC-like trip data, train/test split, baseline linear regression, random forest regression, MAE/RMSE/R2 comparison. Point out the saved metric `RMSE` and the audit report.

## Project 02: NanoLlama Language Model Lab

Open `02_nano_llm_transformer`. Show `prompts.md`, then `src/experiment.py`, then `dashboard.html`. Explain: Small character n-gram language-model baseline with deterministic training corpus, perplexity estimate, and text generation. Kept intentionally laptop-friendly. Point out the saved metric `Perplexity` and the audit report.

## Project 03: Customer Intelligence Clustering

Open `03_customer_segmentation_clustering`. Show `prompts.md`, then `src/experiment.py`, then `dashboard.html`. Explain: Customer-like synthetic data, standardization, KMeans model search over k, silhouette score selection, cluster visualization. Point out the saved metric `Silhouette` and the audit report.

## Project 04: Market Basket Pattern Mining

Open `04_associative_pattern_mining`. Show `prompts.md`, then `src/experiment.py`, then `dashboard.html`. Explain: Deterministic basket transactions, item and pair support, confidence and lift calculation, top association rules. Point out the saved metric `Top lift` and the audit report.

## Project 05: Data Science Skills Mastery Lab

Open `05_data_science_skills_lab`. Show `prompts.md`, then `src/experiment.py`, then `dashboard.html`. Explain: EDA, scaling, PCA, classification, cross-validation, feature importance and model evaluation using the Iris dataset. Point out the saved metric `Accuracy` and the audit report.

## Project 06: Anomaly Threat Intelligence

Open `06_anomaly_detection`. Show `prompts.md`, then `src/experiment.py`, then `dashboard.html`. Explain: Synthetic normal and anomalous points, Isolation Forest scoring, ROC-AUC evaluation, visual inspection. Point out the saved metric `ROC-AUC` and the audit report.

## Project 07: AutoML Model Tournament

Open `07_automl_autogluon`. Show `prompts.md`, then `src/experiment.py`, then `dashboard.html`. Explain: Lightweight AutoML-style tournament across logistic regression, random forest, gradient boosting and KNN using cross-validation. README includes optional AutoGluon upgrade path. Point out the saved metric `CV accuracy` and the audit report.

## Project 08: Data Science Visual Foundations

Open `08_datascience_visual_mastery`. Show `prompts.md`, then `src/experiment.py`, then `dashboard.html`. Explain: Naive Bayes classifier, confusion matrix metrics, gradient descent simulation, visual learning artifacts and quiz bank. Point out the saved metric `Accuracy` and the audit report.

## Project 09: FlowForge DAG Engine

Open `09_flowforge_dag_engine`. Show `prompts.md`, then `src/experiment.py`, then `dashboard.html`. Explain: Directed acyclic graph validation, topological execution order, task status simulation and dependency visualization. Point out the saved metric `Tasks completed` and the audit report.

## Project 10: CRISP-DM Masters Platform

Open `10_crispdm_masters_curriculum`. Show `prompts.md`, then `src/experiment.py`, then `dashboard.html`. Explain: One compact workflow covering EDA, KMeans, Isolation Forest, Random Forest classification, simple association rules, approximate neighbor search and synthesis. Point out the saved metric `Accuracy` and the audit report.

## Project 11: Enterprise Data Science Audit

Open `11_enterprise_ds_audit`. Show `prompts.md`, then `src/experiment.py`, then `dashboard.html`. Explain: Static audit of sibling projects for required files, seed usage, train/test discipline markers and documentation completeness. Point out the saved metric `Audit score` and the audit report.

## Project 12: TimePulse Forecasting Engine

Open `12_timeseries_forecasting`. Show `prompts.md`, then `src/experiment.py`, then `dashboard.html`. Explain: Chronological split, lag features, linear and random-forest forecasts, MAE/RMSE comparison, no random shuffling. Point out the saved metric `RMSE` and the audit report.

## Project 13: CRISP-DM NYC TLC Audit Platform

Open `13_crispdm_nyc_taxi_audit_platform`. Show `prompts.md`, then `src/experiment.py`, then `dashboard.html`. Explain: NYC-like regression with chronological-style partitioning, model comparison, feature importance, clustering of pickup coordinates and explicit audit checks. Point out the saved metric `RMSE` and the audit report.

## Project 14: Multimodal AutoML Suite

Open `14_autogluon_multimodal_automl_suite`. Show `prompts.md`, then `src/experiment.py`, then `dashboard.html`. Explain: Combines tabular, simple text-count and image-summary features, then runs an automated classifier tournament. AutoGluon is optional when installed. Point out the saved metric `Accuracy` and the audit report.

## Project 15: SPY Time Series Forecasting Lab

Open `15_spy_timeseries_sota_forecasting`. Show `prompts.md`, then `src/experiment.py`, then `dashboard.html`. Explain: Leakage-safe lagged-return forecasting with walk-forward holdout, directional accuracy, RMSE and simple long/cash strategy diagnostics. Real SPY CSV can replace offline synthetic data. Point out the saved metric `Directional accuracy` and the audit report.

## Closing

End by showing `VERIFICATION.md` and the top-level README. Mention that the repository uses fixed seeds and lightweight offline fallbacks so the experiments can be rerun on a normal laptop.
