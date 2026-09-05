# Customer Intelligence Clustering: Reproduction Report

## 1. Introduction
The purpose of this project is to reproduce the main learning objective in the supplied coding-assistant prompt using a small implementation that can be rerun and explained.

## 2. Problem and data
The task is unsupervised clustering. The reference dataset/theme is Mall Customer Segmentation style data. For offline verification, this submission uses a deterministic built-in or synthetic equivalent when network data is not required for the concept.

## 3. Method
Customer-like synthetic data, standardization, KMeans model search over k, silhouette score selection, cluster visualization.

## 4. CRISP-DM process
The project documents business understanding, data understanding, data preparation, modeling, evaluation, and deployment/communication. The experiment entry point is `src/experiment.py`.

## 5. Evaluation
The primary reported measure is **Silhouette**. Exact generated values are kept in `artifacts/metrics.json` rather than hard-coded in this report. This prevents the written result from becoming stale after reruns.

## 6. Reproducibility and audit
Random operations use a fixed seed. Supervised evaluation keeps held-out data separate, and time-series evaluation is chronological. The project does not claim that synthetic fallback data is the original external dataset.

## 7. Limitations
This is an educational reproduction. It favors clarity and reproducibility over production scale. Heavy cloud, GPU, and external-service features from the reference project are not claimed as verified here.

## 8. Conclusion
The project demonstrates the requested concept, produces repeatable outputs, and provides a simple dashboard and documentation suitable for a code walkthrough.
