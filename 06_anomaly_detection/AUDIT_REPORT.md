# Data Science Audit Report

## Checks

- **Reproducibility:** fixed random seed is used where randomness exists.
- **Target leakage:** target values are not intentionally included in model input features.
- **Train/test discipline:** supervised models use a holdout split or cross-validation. Time-series projects use chronological splitting.
- **Metric choice:** the project reports a metric appropriate for its task instead of relying on one generic score.
- **Transparency:** offline synthetic data is clearly labeled and not presented as the original Kaggle or market dataset.
- **Generated artifacts:** metrics and plots are produced by the code in this repository.

## Limitations

This is a compact academic reproduction, not a production deployment. External datasets, AutoGluon, live APIs, GPU training, cloud MLOps, and large-scale load testing are outside the verified offline path unless explicitly added later.
