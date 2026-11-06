# Bicycle Rental Demand Prediction

We developed this Streamlit application to estimate hourly bicycle-rental demand from the time, day of week, and forecast weather conditions. It was prepared for the IFJC4002 project by the Computer Engineering team at Walailak University in collaboration with Universiti Malaysia Perlis (UniMAP).

## Application

The application accepts seven inputs: hour, temperature, relative humidity, weather category, wind speed, working-day status, and day of week. It returns an estimated number of rentals per hour.

Run it locally with the pinned dependencies:

```powershell
python -m pip install -r requirements.txt
streamlit run app.py
```

For Streamlit Community Cloud, use `app.py` as the entry point and Python 3.12. Keep `personal_features.py` and every file in `models/` in the same release; the application verifies the hashes of its model artifact and feature module before making a prediction.

## Model and results

We selected a tuned Random Forest with time features using validation MAE. The saved pipeline uses 200 trees, `min_samples_leaf=4`, and `max_features=0.7`. It internally adds cyclical time features and working-day commuter-hour indicators while preserving the seven raw inputs used by the application.

| Evaluation measure | Result |
| --- | ---: |
| Validation MAE | 13.046351 |
| Validation RMSE | 17.335641 |
| Validation R² | 0.820696 |
| Repeated test MAE | 12.851067 |
| Repeated test RMSE | 16.501946 |
| Repeated test R² | 0.843084 |

The model was trained and evaluated with synthetic teaching data using a chronological 1,400/300/300 split. The test partition had been inspected during earlier project work, so the repeated test result is not an independent untouched holdout and does not establish real-world accuracy. The full release record is in [Model and deployment](docs/MODEL_AND_DEPLOYMENT.md); raw result files are in [results](results/README.md).

## Repository contents

| Path | Contents |
| --- | --- |
| `app.py` | Streamlit prediction interface |
| `models/` | Released pipeline, input contract, and model metadata |
| `results/` | Model-comparison, selection, evaluation, and inference-check outputs |
| `notebooks/personal/` | Completed experiment notebook for the promoted model |
| `assets/`, `logo/`, `.streamlit/` | Application styling, identity assets, and Streamlit configuration |

## Team

Nattakorn Chuaychoowong · Nidanish Niseng · Suwarot Intharawichiar · Chanon Chubuatong · Supot Bamrung
