
from pathlib import Path
import sys
repo=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(repo))
from shared.experiments import run_project
from shared.dashboard import build_dashboard
meta={
'01':('01_nyc_taxi_trip_prediction','NYC Taxi Trip Duration Predictor','Supervised regression','Synthetic NYC-like trip data, train/test split, baseline linear regression, random forest regression, MAE/RMSE/R2 comparison.'),
'02':('02_nano_llm_transformer','NanoLlama Language Model Lab','Language modeling','Small character n-gram language-model baseline with deterministic training corpus, perplexity estimate, and text generation.'),
'03':('03_customer_segmentation_clustering','Customer Intelligence Clustering','Unsupervised clustering','Customer-like synthetic data, standardization, KMeans search over k, silhouette selection and cluster visualization.'),
'04':('04_associative_pattern_mining','Market Basket Pattern Mining','Association rule mining','Deterministic basket transactions with support, confidence and lift.'),
'05':('05_data_science_skills_lab','Data Science Skills Mastery Lab','End-to-end data science skills','EDA, scaling, PCA, classification and evaluation using Iris.'),
'06':('06_anomaly_detection','Anomaly Threat Intelligence','Anomaly detection','Synthetic normal/anomalous observations scored with Isolation Forest and ROC-AUC.'),
'07':('07_automl_autogluon','AutoML Model Tournament','Automated model selection','Lightweight AutoML-style model tournament using cross-validation.'),
'08':('08_datascience_visual_mastery','Data Science Visual Foundations','Data science education','Naive Bayes, confusion matrix metrics, gradient descent visualization and quizzes.'),
'09':('09_flowforge_dag_engine','FlowForge DAG Engine','Data pipeline orchestration','DAG validation, topological execution and dependency visualization.'),
'10':('10_crispdm_masters_curriculum','CRISP-DM Masters Platform','Integrated CRISP-DM workflow','Compact EDA, clustering, anomaly detection, classification, association proxy and neighbor search workflow.'),
'11':('11_enterprise_ds_audit','Enterprise Data Science Audit','Governance and reproducibility','Static repository audit for required artifacts and reproducible implementation markers.'),
'12':('12_timeseries_forecasting','TimePulse Forecasting Engine','Time series forecasting','Chronological lag-feature forecasting with linear and random-forest models.'),
'13':('13_crispdm_nyc_taxi_audit_platform','CRISP-DM NYC TLC Audit Platform','Audited regression and explainability','NYC-like regression with model audit, feature importance and pickup clustering.'),
'14':('14_autogluon_multimodal_automl_suite','Multimodal AutoML Suite','Multimodal classification','Tabular, text-summary and image-summary features in an automated classifier tournament.'),
'15':('15_spy_timeseries_sota_forecasting','SPY Time Series Forecasting Lab','Financial time series','Leakage-safe lagged-return forecasting with chronological holdout and direction diagnostics.'),
}
for pid,(folder,title,domain,method) in meta.items():
    p=repo/folder
    metrics=run_project(pid,p)
    build_dashboard(p,title,domain,method)
    print(pid, metrics)
