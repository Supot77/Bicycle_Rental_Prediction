# Model and deployment

## Our selected model

We promoted the tuned Random Forest with time features after selecting it by validation MAE. The pipeline uses 200 trees, `min_samples_leaf=4`, `max_features=0.7`, no maximum depth, and random seed 42. It accepts the same seven raw fields used in the Streamlit application and derives cyclical hour/weekday features plus working-day commuter-hour indicators inside the saved pipeline.

Our validation MAE was 13.046351, compared with 13.809600 for the original Random Forest. On the repeated test evaluation, the promoted model produced MAE 12.851067, RMSE 16.501946, and R² 0.843084.

We used a chronological 1,400/300/300 split and four `TimeSeriesSplit` folds within the training data for parameter search. Preprocessing was fitted within each fold, and the selected pipeline remained fitted on training data only. The synthetic test partition had been inspected in earlier team work. We therefore report this as a repeated evaluation rather than an untouched final holdout; it does not establish real-world accuracy.

## Released artifacts

The deployed release consists of `models/final_pipeline.joblib`, `models/input_schema.json`, `models/model_metadata.json`, and `personal_features.py`. The pipeline SHA-256 is `1de64cbede6d646d7bb86aae213732c727a81a867e82885a3bb3913a19c3ef8b`; the feature-module SHA-256 is `5c97bf8197bbba38311ccab8a9d0420156ad36d48e3eaf6414b19042f28d2bc6`.

The checked reference scenario—Wednesday at 12:00, 25 °C, 70% humidity, Clear weather, and 10 km/h wind—returns 43.84 rentals/hour after rounding to two decimals.

## Deployment

We deploy `app.py` to Streamlit Community Cloud with Python 3.12 and the pinned dependencies in `requirements.txt`. The application is self-contained: it does not require the source dataset or credentials at run time. It validates the released model and feature-module hashes before calculating an estimate.
