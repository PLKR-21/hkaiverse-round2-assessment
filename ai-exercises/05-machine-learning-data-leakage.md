# AI-assisted exercise — Machine Learning

- **Model:** ChatGPT GPT-6 (model label available in this conversation; exact backend build not exposed)
- **Date:** 2026-10-23
- **Evidence status:** Generated in this ChatGPT conversation; candidate review and source check recommended.

## Exact prompt used

> Explain a leakage-safe train/test workflow for a tabular classification problem with missing values and numeric features. Include where to fit preprocessing, why splitting matters, and what changes if records are time-dependent or grouped by person/device. Do not invent performance results.

## Output excerpt

First define the prediction target and split strategy. For independent IID records, split into train/test before fitting imputers, scalers, feature selectors or other learned transformations. Fit preprocessing only on training data and apply the fitted transforms to validation/test data, preferably in a pipeline. Keep the test set untouched until final evaluation. If records are time-dependent, use a time-aware split; if multiple rows belong to the same person/device/group, use a group-aware split so related records do not leak across partitions. Report a baseline, suitable metrics, class balance and limitations. No model performance can be stated without running an experiment.

## Verification notes

Compare the workflow with scikit-learn's documented common pitfalls and train/test splitting guidance. This is a procedural recommendation; no dataset or model was run, so no performance claim is made.

## Verification source

https://scikit-learn.org/stable/common_pitfalls.html#data-leakage

## Candidate review

Before submission, personally review the prompt/output, open the source, add any corrections you make, and do not claim a code/test was executed unless you execute it yourself. This record discloses AI assistance rather than attributing generated wording to independent candidate work.
