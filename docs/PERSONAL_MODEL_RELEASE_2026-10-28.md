# Personal experiment promoted to the application

The user requested replacing the deployed repository's original model with the better-performing personal experiment. The promoted run is `20261028T153400574248Z`, selected in hosted Google Colab using validation MAE before its repeated test evaluation.

## Model and comparison

The selected pipeline is **Tuned Random Forest + time features**: 200 trees, `min_samples_leaf=4`, `max_features=0.7`, `max_depth=None`, and random seed 42. It adds cyclical hour/weekday features and working-day commuter-hour indicators inside the saved pipeline. The application continues to accept the same seven raw input fields.

| Measure | Original Random Forest | Promoted model |
| --- | ---: | ---: |
| Validation MAE | 13.809600 | 13.046351 |
| Validation RMSE | 18.134306 | 17.335641 |
| Validation R² | 0.803794 | 0.820696 |
| Repeated test MAE | 13.931000 | 12.851067 |
| Repeated test RMSE | 18.701039 | 16.501946 |
| Repeated test R² | 0.798475 | 0.843084 |

Validation MAE decreased by 5.53%; repeated test MAE decreased by 7.75%. The same synthetic dataset fingerprint and chronological 1,400/300/300 split were used. Parameter search used four TimeSeriesSplit folds inside training data. Preprocessing was fitted within each fold. The selected pipeline remains fitted on training data only.

The test partition was previously inspected during team work. This is a repeated comparison, not an independent untouched holdout. These results do not establish real-world accuracy.

## Files and compatibility

- `models/final_pipeline.joblib`: the exact compressed artifact from the personal run, renamed for deployment without reserialization.
- `personal_features.py`: the matching importable transformation module required to reload the artifact in a fresh Python process.
- `models/model_metadata.json`: model hash, feature-module hash, input contract, package versions and provenance.
- `app.py`: verifies both hashes and handles the feature-engineering pipeline's optional `feature_names_in_` attribute.
- `results/model_comparison.csv`, `model_selection.json`, `final_test_metrics.json`, `search_summary.json`, `run_manifest.json`, `inference_checks.csv`: current measured results and selection provenance.
- `notebooks/personal/Bicycle_Rental_Personal_Accuracy_Experiments.ipynb`: source notebook, with account metadata and execution outputs removed for publication.
- `colab/verify_personal_release.py`: fresh-process model/app validation in hosted Colab. Set `RELEASE_DIR` to a repository copy and `EVIDENCE_DIR` to a writable personal Drive output folder.

Earlier member notebooks and `colab/repair_workflow.py` remain as the historical team workflow. They reproduce the earlier model; the personal notebook reproduces the currently promoted experiment. Do not use historical metrics as current deployment scores. Earlier score records are also retained under `results/history/b1912bb/`; the original binary can be recovered from Git commit `b1912bb`.

Model SHA-256: `1de64cbede6d646d7bb86aae213732c727a81a867e82885a3bb3913a19c3ef8b`.

Feature-module SHA-256: `5c97bf8197bbba38311ccab8a9d0420156ad36d48e3eaf6414b19042f28d2bc6`.

## Deployment and evidence

Use branch `main`, entry point `app.py`, and Python 3.12 in Streamlit Community Cloud. Keep the matching model files and `personal_features.py` in the same release. Dependencies remain pinned to the compatible tested versions.

All 24 current application checks passed in a fresh Python process on hosted Colab at 2026-10-28 15:43 UTC. Results are recorded in `evidence/app_test_log.csv` and `evidence/app_test_run.json`. They include raw-input validation, predictions compared with the saved model across weather/weekday/boundary cases, missing artifacts and mismatched model/helper hashes. They run in hosted Colab without retraining.

Live deployment verified on 2026-10-28 after changing Streamlit Community Cloud's Python runtime from 3.14 to 3.12. The earlier build left `joblib` unavailable; the new build logs confirm Python 3.12.16 and successful installation of the pinned dependencies, including joblib 1.6.0 and scikit-learn 1.6.1.

The live app loaded in a fresh browser session and returned **43.84 rentals/hour** for Wednesday, hour 12, temperature 25 °C, humidity 70%, Clear weather and wind speed 10 km/h. This matches the saved model's reference prediction of 43.84184502303255 rounded to two decimal places. The Python version is configured in Streamlit Cloud settings; no dependency-version change was needed in the repository.
