"""Run deployment integration checks in hosted Colab; no model training."""
import importlib.metadata
import json
import os
from pathlib import Path
import shutil
import sys
from datetime import datetime, timezone

import joblib
import pandas as pd
from streamlit.testing.v1 import AppTest

release = Path(os.environ['RELEASE_DIR'])
evidence = Path(os.environ['EVIDENCE_DIR'])
evidence.mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(release))
os.environ['M5_MODEL_DIR'] = str(release / 'models')
namespace = {'__name__': 'release_validation', '__file__': str(release / 'app.py')}
exec(compile((release / 'app.py').read_text(encoding='utf-8'), str(release / 'app.py'), 'exec'), namespace)
validate = namespace['validate_inputs']
model = joblib.load(release / 'models/final_pipeline.joblib')
base = dict(hour=12, temperature_c=25.0, humidity_pct=70.0, weather='Clear', wind_speed_kmh=10.0, is_working_day=1, day_of_week=2)
records = []

def record(case, expected, actual, passed):
    records.append(dict(case=case, expected=str(expected), actual=str(actual), passed=bool(passed)))

for name, patch in [('hour above max', {'hour': 24}), ('fractional hour', {'hour': 1.5}),
                    ('unknown weather', {'weather': 'Snow'}), ('negative wind', {'wind_speed_kmh': -1}),
                    ('nonfinite temperature', {'temperature_c': float('nan')}),
                    ('string temperature', {'temperature_c': 'hot'}), ('humidity below min', {'humidity_pct': 34}),
                    ('humidity above max', {'humidity_pct': 100}), ('weekday mismatch', {'day_of_week': 6})]:
    try:
        validate({**base, **patch})
        record(name, 'reject', 'accepted', False)
    except ValueError as error:
        record(name, 'reject', error, True)
try:
    validate({key: value for key, value in base.items() if key != 'weather'})
    record('missing input', 'reject', 'accepted', False)
except ValueError as error:
    record('missing input', 'reject', error, True)

valid_cases = [('weather ' + weather, {'weather': weather}) for weather in ['Clear', 'Cloudy', 'Light_Rain', 'Heavy_Rain']]
valid_cases += [('hour 0', {'hour': 0}), ('hour 23', {'hour': 23}),
                ('Sunday', {'day_of_week': 6, 'is_working_day': 0}),
                ('humidity 35', {'humidity_pct': 35.0}), ('humidity 99', {'humidity_pct': 99.0}),
                ('zero wind', {'wind_speed_kmh': 0.0}),
                ('personal notebook example', {'hour': 8, 'temperature_c': 26.0, 'humidity_pct': 75.0})]
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
for name, patch in valid_cases:
    values = {**base, **patch}
    at = AppTest.from_file(str(release / 'app.py')).run(timeout=30)
    at.selectbox[0].select(weekdays[values['day_of_week']])
    at.selectbox[1].select(values['weather'])
    for widget, key in zip(at.number_input, ['hour', 'temperature_c', 'humidity_pct', 'wind_speed_kmh']):
        widget.set_value(values[key])
    at.button[0].click().run(timeout=30)
    expected = float(model.predict(validate(values))[0])
    actual = float(at.session_state['last_prediction']) if 'last_prediction' in at.session_state else None
    passed = actual is not None and abs(expected - actual) <= 1e-9 and not len(at.exception) and not len(at.error)
    record(name + ' parity', expected, actual, passed)

# A separate directory holds failure fixtures; the promoted files stay intact.
bad = evidence / 'failure_fixture'
bad.mkdir(exist_ok=True)
for name in ['final_pipeline.joblib', 'input_schema.json', 'model_metadata.json']:
    shutil.copy2(release / 'models' / name, bad / name)
original_meta = json.loads((bad / 'model_metadata.json').read_text())
for case, field in [('mismatched model', 'pipeline_sha256'), ('mismatched feature helper', 'feature_module_sha256')]:
    (bad / 'model_metadata.json').write_text(json.dumps({**original_meta, field: '0' * 64}))
    os.environ['M5_MODEL_DIR'] = str(bad)
    at = AppTest.from_file(str(release / 'app.py')).run(timeout=30)
    at.button[0].click().run(timeout=30)
    record(case, 'visible integrity error', [x.value for x in at.error], len(at.error) == 1 and len(at.exception) == 0)
os.environ['M5_MODEL_DIR'] = str(evidence / 'missing_models')
at = AppTest.from_file(str(release / 'app.py')).run(timeout=30)
at.button[0].click().run(timeout=30)
record('missing artifacts', 'visible error', [x.value for x in at.error], len(at.error) == 1 and len(at.exception) == 0)
os.environ['M5_MODEL_DIR'] = str(release / 'models')
log = pd.DataFrame(records)
log.to_csv(evidence / 'app_test_log.csv', index=False)
metadata = json.loads((release / 'models/model_metadata.json').read_text())
receipt = dict(executed_at_utc=datetime.now(timezone.utc).isoformat(), environment='hosted Google Colab',
               model_sha256=metadata['pipeline_sha256'], feature_module_sha256=metadata['feature_module_sha256'],
               passed=int(log.passed.sum()), total=len(log),
               libraries={name: importlib.metadata.version(name) for name in ['streamlit', 'scikit-learn', 'joblib', 'pandas', 'numpy']})
(evidence / 'app_test_run.json').write_text(json.dumps(receipt, indent=2))
assert log.passed.all(), log.loc[~log.passed].to_string(index=False)
print('PROMOTED APP TESTS PASS:', receipt['passed'], '/', receipt['total'])
print('MODEL SHA256:', receipt['model_sha256'])
print(log.loc[log['case'].str.contains('personal notebook')].to_string(index=False))
print('Evidence:', evidence)
