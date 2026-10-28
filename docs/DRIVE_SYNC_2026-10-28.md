# Google Drive synchronization — 28 October 2026

The user authorized publishing the corrected team files and deployment package from Google Drive to this repository.

Source run: `20261028T143243642997Z` in the shared team's `00_SHARED/repair_runs` folder. Training, model evaluation and Streamlit AppTest ran in hosted Google Colab. Local checks for this synchronization only validate source syntax, file integrity and repository checks.

## Published files

- `app.py` and `requirements.txt`: tested Streamlit application and pinned dependencies.
- `models/final_pipeline.joblib`, `models/input_schema.json`, `models/model_metadata.json`: matching deployment artifacts.
- `notebooks/team/M1_data_eda.ipynb` through `M5_app_deploy.ipynb`: corrected Drive notebook sources. Execution outputs and account metadata are removed for publication. Verified run summaries retained in markdown describe the earlier Colab execution; they are not fabricated notebook execution outputs.
- `colab/repair_workflow.py` and `colab/artifact_paths.json`: shared Colab workflow and its Drive handoff paths. Member notebooks currently reference the shared Drive script. Keep that folder accessible when reproducing them.
- `results/model_comparison.csv`, `results/model_selection.json`, `results/final_test_metrics.json`: measured comparison and final evaluation.
- `evidence/app_test_log.csv`: 16 passing validation and notebook-to-app agreement checks from Colab.

Raw teaching data, previous-version backups, credentials and private account metadata are excluded. This release explicitly includes the verified model binary so Streamlit can load it.

## Verified behavior and limits

The model uses `hour`, `temperature_c`, `humidity_pct`, `weather`, `wind_speed_kmh`, `is_working_day`, and `day_of_week`. Identifiers and the target are excluded. Preprocessing fits training data only. The chronological split contains 1,400 training, 300 validation and 300 test rows.

A training-mean baseline, Linear Regression and Random Forest were compared on validation data. Random Forest was selected using validation MAE. The saved final model was evaluated without refitting. Final metrics are MAE 13.931, RMSE 18.7010393651 and R² 0.7984750934.

This was a repeated test evaluation after implementation repair: the test set had previously been inspected. The data are synthetic teaching examples. Neither these scores nor prediction logs establish real-world accuracy.

Model SHA-256: `c9319046e9eee0b7e3a4310033c1a02ceea88ef00350eb073366a24522d5dff5`. The binary, model metadata and final test record agree on this value.

## Deployment

In Streamlit Community Cloud select repository `Supot77/Bicycle_Rental_Prediction`, branch `main`, main file `app.py`, and Python 3.12. The application checks the model hash and input schema before predicting. It displays a useful error if deployment files are missing or inconsistent.

GitHub publication does not confirm a live Streamlit deployment. Open and test the deployed URL before recording deployment success or monitoring observations.
