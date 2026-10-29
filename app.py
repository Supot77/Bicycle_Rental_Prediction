import streamlit as st
import pandas as pd
import math
import base64
from html import escape
import os, json, hashlib
from pathlib import Path
import joblib
import personal_features

WEATHER = ['Clear', 'Cloudy', 'Light_Rain', 'Heavy_Rain']
FEATURES = ['hour', 'temperature_c', 'humidity_pct', 'weather', 'wind_speed_kmh', 'is_working_day', 'day_of_week']
LOGO_DIR = Path(__file__).resolve().parent / 'logo'
ASSET_DIR = Path(__file__).resolve().parent / 'assets'
DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
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

def render_branding():
    logos = []
    for filename, label in [
        ('walailak-university.png', 'Walailak University'),
        ('computer-engineering.jpg', 'Computer Engineering, Walailak University'),
        ('unimap.png', 'Universiti Malaysia Perlis (UniMAP)'),
    ]:
        mime = 'image/jpeg' if filename.endswith('.jpg') else 'image/png'
        encoded = base64.b64encode((LOGO_DIR / filename).read_bytes()).decode('ascii')
        logos.append(f'<img src="data:{mime};base64,{encoded}" alt="{escape(label)}" title="{escape(label)}">')
    st.html('<header class="bicycle-brand"><span class="bicycle-wordmark">'
            'Bicycle Lab<span class="bicycle-course">IFJC4002</span></span>'
            '<div class="bicycle-logos" aria-label="University and department logos">'
            + ''.join(logos) + '</div></header>')


def predict_rentals(values):
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
    return prediction

def main():
    st.set_page_config(page_title='Bicycle Lab | Rental Demand', page_icon='🚲', layout='wide')
    st.html(ASSET_DIR / 'app.css')
    render_branding()
    st.title('Bicycle rental demand')
    st.write('Estimate hourly rentals from the day, time and forecast weather.')

    controls, forecast = st.columns([1.15, 1], gap='large')
    with controls, st.container(border=True, key='scenario-panel'):
        st.header('Set your scenario')
        time_col, day_col = st.columns(2)
        with time_col:
            hour = st.number_input('Hour (0–23)', min_value=0, max_value=23, value=12, step=1)
        with day_col:
            day = st.selectbox('Day of week', DAYS)
        day_index = DAYS.index(day)
        working = int(day_index < 5)
        temperature_col, humidity_col = st.columns(2)
        with temperature_col:
            temp = st.number_input('Forecast temperature (°C)', value=25.0, step=0.1)
        with humidity_col:
            humidity = st.number_input('Forecast relative humidity (%)', min_value=35.0, max_value=99.0, value=70.0, step=0.1)
        weather_col, wind_col = st.columns(2)
        with weather_col:
            weather = st.selectbox('Forecast weather', WEATHER, format_func=lambda value: value.replace('_', ' '))
        with wind_col:
            wind = st.number_input('Forecast wind speed (km/h)', min_value=0.0, value=10.0, step=0.1)
        st.caption('Working day: ' + ('Yes' if working else 'No') + '. Public holidays are not modelled.')
        values = dict(hour=hour, temperature_c=temp, humidity_pct=humidity, weather=weather, wind_speed_kmh=wind, is_working_day=working, day_of_week=day_index)
        submitted = st.button('Predict rentals/hour', type='primary', width='stretch')

    if submitted:
        try:
            prediction = predict_rentals(values)
            st.session_state['last_prediction'] = prediction
            st.session_state['last_prediction_inputs'] = values.copy()
        except (ValueError, FileNotFoundError, KeyError, OSError) as error:
            st.session_state.pop('last_prediction', None)
            st.session_state.pop('last_prediction_inputs', None)
            with forecast:
                st.error(str(error))

    with forecast, st.container(border=True, key='forecast-panel'):
        st.header('Hourly forecast')
        previous = st.session_state.get('last_prediction_inputs')
        has_prediction = previous is not None and 'last_prediction' in st.session_state
        stale = has_prediction and previous != values
        if has_prediction:
            st.metric('Predicted rentals/hour', f"{st.session_state['last_prediction']:.2f}")
            st.write(f"{DAYS[previous['day_of_week']]} at {previous['hour']:02d}:00")
            st.caption(f"{previous['weather'].replace('_', ' ')} · {previous['temperature_c']:g} °C · "
                       f"{previous['humidity_pct']:g}% humidity · {previous['wind_speed_kmh']:g} km/h wind")
            if stale:
                st.info('Inputs changed. Select Predict rentals/hour to update this previous estimate.')
            else:
                st.caption('This estimate matches your current inputs.')
        else:
            st.metric('Predicted rentals/hour', '—')
            st.write('Your estimate will appear here.')
            st.caption('Choose a scenario, then select Predict rentals/hour.')
        st.divider()
        st.caption('Based on synthetic teaching data. Real-world accuracy has not been established. '
                   'Estimates are shown to two decimal places.')

    st.divider()
    st.header('Developers / ผู้พัฒนา')
    st.caption('Computer Engineering, Walailak University')
    st.html('<div class="bicycle-developers">' + ''.join(
        f'<div class="bicycle-developer"><span class="bicycle-member">{escape(member_id)}</span>'
        f'<span class="bicycle-name">{escape(name)}</span><span class="bicycle-role">Developer</span></div>'
        for member_id, name in DEVELOPERS
    ) + '</div>')

if __name__ == '__main__':
    main()
