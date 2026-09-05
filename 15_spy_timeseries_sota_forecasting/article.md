# Reproducing SPY Time Series Forecasting Lab on a Normal Laptop

The goal of this project was not to build the largest possible system. I wanted a version I could run, inspect, and explain clearly.

The main idea is financial time series. I started from the supplied prompt, identified the core experiment, and used a small offline dataset so that another student or grader can reproduce it without special credentials.

The workflow is simple: prepare the data, run the experiment, save the metrics, create one useful visualization, and generate an HTML dashboard. I also added an audit note that checks the most important risks such as target leakage, incorrect train/test handling, and unrepeatable random results.

The most useful part of this reproduction is that the numbers in the README are not manually typed. The code saves the current run in `artifacts/metrics.json`, which makes it easy to verify what happened.
