import numpy as np
FEATURES = ['hour','temperature_c','humidity_pct','weather','wind_speed_kmh','is_working_day','day_of_week']
EXTRA = ['hour_sin','hour_cos','hour_sin2','hour_cos2','weekday_sin','weekday_cos','morning_commute','evening_commute']
def add_features(frame):
    if not hasattr(frame, 'columns'):
        raise TypeError('Pass a pandas DataFrame with named raw input columns')
    missing=set(FEATURES)-set(frame.columns)
    if missing:
        raise ValueError('Missing raw inputs: '+', '.join(sorted(missing)))
    data=frame[FEATURES].copy()
    hour=data['hour']; weekday=data['day_of_week']; work=data['is_working_day']
    data['hour_sin']=np.sin(2*np.pi*hour/24)
    data['hour_cos']=np.cos(2*np.pi*hour/24)
    data['hour_sin2']=np.sin(4*np.pi*hour/24)
    data['hour_cos2']=np.cos(4*np.pi*hour/24)
    data['weekday_sin']=np.sin(2*np.pi*weekday/7)
    data['weekday_cos']=np.cos(2*np.pi*weekday/7)
    data['morning_commute']=hour.between(7,9).astype(int)*work
    data['evening_commute']=hour.between(17,19).astype(int)*work
    return data
