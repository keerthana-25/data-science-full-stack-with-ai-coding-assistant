# Portfolio Audit Report

This report summarizes the checks applied to the 15-project reproduction portfolio.

## Verified design rules

- Fixed seed is defined in the shared experiment module.
- Supervised projects use holdout evaluation or cross-validation.
- Time-series projects use chronological splitting.
- Synthetic/offline fallback data is labeled as such.
- Generated metrics are stored in JSON instead of being manually typed into reports.
- Every project has an implementation plan, prompt file, audit report, abstract, paper, article, skill file, dashboard, result image and screenshot.

## Limitation

The current execution environment blocks browser automation. HTML dashboards are rendered to screenshots with WeasyPrint for visual verification. The final YouTube walkthrough should open every dashboard in a normal browser.

