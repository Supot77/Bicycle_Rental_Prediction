# Working on this learning scaffold

This repository is a Thai-language guided group project for IFJC4002.

- All student development and training uses hosted Google Colab only. Do not add local Python/venv/Jupyter setup instructions. GitHub stores submitted code and Streamlit Community Cloud remains the lecturer-required deployment destination. Use AppTest inside Colab for development checks; do not introduce tunnels or use Colab as a persistent app host.

- The lecturer supplies the dataset. Do not choose or download a replacement without the user's request.
- Preserve opportunities for members to do the analysis and implementation themselves. By default provide scaffolding, explanations, review and small examples; do not silently complete the ML exercises or choose a final model.
- There is no real dataset, trained model, measured performance or completed deployment in the initial scaffold. Do not fabricate results, contributions, prompt records or monitoring observations.
- Never infer the target, feature names, time granularity or units before inspecting the lecturer's actual data and confirming its meaning.
- Keep target and outcome-revealing components out of inputs; fit learned preprocessing only on training data. Preserve time order for forward prediction.
- Explain Thai learning instructions plainly. Keep task requirements distinct from optional suggestions.
- Update relevant documentation with changed files, behavior and verification after code changes.
- Run affected checks: `python scripts/check_setup.py` and `python -m unittest discover -s tests -v`. After UI changes check Streamlit with AppTest when available. These verify the scaffold, not ML competence.
- Keep data and credentials out of commits unless their publication is explicitly authorized. Do not upload notebook output containing restricted records.
