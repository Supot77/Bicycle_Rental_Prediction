import streamlit as st
import pandas as pd
import math
import os, json, hashlib
from pathlib import Path
import joblib
import personal_features

WEATHER = ['Clear', 'Cloudy', 'Light_Rain', 'Heavy_Rain']
FEATURES = ['hour', 'temperature_c', 'humidity_pct', 'weather', 'wind_speed_kmh', 'is_working_day', 'day_of_week']
LOGO_DIR = Path(__file__).resolve().parent / 'logo'
DEVELOPERS = [
    ('M1', 'Nattakorn Chuaychoowong'),
    ('M2', 'Nidanish Niseng'),
    ('M3', 'Suwarot Intharawichiar'),
    ('M4', 'Chanon Chubuatong'),
    ('M5', 'Supot Bamrung'),
]

def validate_inputs(values):
    missing = set(FEATURES) - set(values)
    if missing:
        raise ValueError('Missing inputs: ' + ', '.join(sorted(missing)))
    for key in FEATURES:
        if key == 'weather':
            if values[key] not in WEATHER:
                raise ValueError('Unsupported weather category')
        else:
            value = values[key]
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
                raise ValueError(key + ' must be a finite number')
    for key, low, high in [('hour', 0, 23), ('day_of_week', 0, 6), ('is_working_day', 0, 1)]:
        if values[key] != int(values[key]) or not low <= values[key] <= high:
            raise ValueError(key + ' is outside its allowed integer range')
    if not 35 <= values['humidity_pct'] <= 99:
        raise ValueError('Humidity must be between 35 and 99 percent')
    if values['wind_speed_kmh'] < 0:
        raise ValueError('Wind speed must be non-negative')
    expected = int(values['day_of_week'] < 5)
    if values['is_working_day'] != expected:
        raise ValueError('Working-day status must match the selected weekday')
    return pd.DataFrame([{name: values[name] for name in FEATURES}], columns=FEATURES)

def main():
    st.set_page_config(page_title='Bicycle Rental Demand', page_icon='🚲')
    university, department = st.columns([3, 2], vertical_alignment='center')
    with university:
        st.image(str(LOGO_DIR / 'walailak-university.png'), width=260)
    with department:
        st.image(str(LOGO_DIR / 'computer-engineering.jpg'), width=96)
    st.caption('Walailak University | Computer Engineering')
    st.title('Bicycle Rental Demand Prediction')
    st.caption('IFJC4002 | Synthetic teaching data | Hourly demand')
    st.write('Choose the hour and forecast weather for the hour you want to estimate.')
    st.info('Estimates use synthetic teaching data. Real-world accuracy has not been established.')
    hour = st.number_input('Hour (0–23)', min_value=0, max_value=23, value=12, step=1)
    day = st.selectbox('Day of week', ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    day_index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'].index(day)
    working = int(day_index < 5)
    st.caption('Working day: ' + ('Yes' if working else 'No') + '. Public holidays are not modelled.')
    temp = st.number_input('Forecast temperature (°C)', value=25.0, step=0.1)
    humidity = st.number_input('Forecast relative humidity (%)', min_value=35.0, max_value=99.0, value=70.0, step=0.1)
    weather = st.selectbox('Forecast weather', WEATHER)
    wind = st.number_input('Forecast wind speed (km/h)', min_value=0.0, value=10.0, step=0.1)
    values = dict(hour=hour, temperature_c=temp, humidity_pct=humidity, weather=weather, wind_speed_kmh=wind, is_working_day=working, day_of_week=day_index)
    try:
        validate_inputs(values)
    except ValueError as error:
        st.error(str(error))
    if st.button('Predict rentals/hour'):
        try:
            model_dir = Path(os.environ.get('M5_MODEL_DIR', str(Path(__file__).parent / 'models')))
            metadata = json.loads((model_dir / 'model_metadata.json').read_text(encoding='utf-8'))
            model_path = model_dir / 'final_pipeline.joblib'
            if hashlib.sha256(model_path.read_bytes()).hexdigest() != metadata['pipeline_sha256']:
                raise ValueError('Model integrity check failed. Restore the matching deployment files.')
            feature_path = Path(personal_features.__file__)
            if hashlib.sha256(feature_path.read_bytes()).hexdigest() != metadata['feature_module_sha256']:
                raise ValueError('Feature module integrity check failed. Restore personal_features.py from the same release.')
            model = joblib.load(model_path)
            schema = json.loads((model_dir / 'input_schema.json').read_text(encoding='utf-8'))
            model_features = getattr(model, 'feature_names_in_', None)
            if ([x['name'] for x in schema['features']] != FEATURES
                    or metadata['features'] != FEATURES
                    or personal_features.FEATURES != FEATURES
                    or (model_features is not None and list(model_features) != FEATURES)):
                raise ValueError('Model input contract mismatch.')
            frame = validate_inputs(values)
            prediction = float(model.predict(frame)[0])
            if not math.isfinite(prediction):
                raise ValueError('The model produced an invalid estimate.')
            st.session_state['last_prediction'] = prediction
            st.metric('Predicted rentals/hour', f'{prediction:.2f}')
        except (ValueError, FileNotFoundError, KeyError, OSError) as error:
            st.error(str(error))
    st.caption('Predictions are continuous estimates in rentals/hour, displayed to 2 decimal places. Public holidays are not modelled.')
    st.divider()
    st.subheader('Developers / ผู้พัฒนา')
    st.caption('Computer Engineering, Walailak University')
    for member_id, name in DEVELOPERS:
        st.write(f'**{name}** · Developer ({member_id})')

if __name__ == '__main__':
    main()
