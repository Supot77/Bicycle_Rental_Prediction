# Evaluation results

These files document the promoted tuned Random Forest with time features:

- `model_comparison.csv` compares the baseline and candidate models.
- `model_selection.json` records the validation-MAE selection decision.
- `final_test_metrics.json` records the repeated test metrics for the selected pipeline.
- `search_summary.json` and `run_manifest.json` record the parameter-search and run context.
- `inference_checks.csv` records reference input/output checks for the released model.

The reported data are synthetic teaching data. The test partition was already inspected in earlier work, so the repeated test evaluation is not an untouched holdout and does not prove real-world performance.
