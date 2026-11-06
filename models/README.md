# Released model files

We deploy these files together:

- `final_pipeline.joblib` — the selected tuned Random Forest pipeline, including preprocessing and feature engineering.
- `input_schema.json` — the seven raw inputs and the prediction target contract.
- `model_metadata.json` — model provenance, compatible library versions, and SHA-256 hashes.

`app.py` checks the pipeline hash and the matching `personal_features.py` hash before loading the model. The model should only be loaded from this verified release.
