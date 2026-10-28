import json, hashlib, shutil, copy, io, contextlib, importlib.metadata, math
from pathlib import Path
from datetime import datetime, timezone
import pandas as pd
import numpy as np
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
ROOT = Path('/content/drive/MyDrive/Bicycle_Rental_Project_Team')
FEATURES = ['hour','temperature_c','humidity_pct','weather','wind_speed_kmh','is_working_day','day_of_week']
NUMERIC = [x for x in FEATURES if x != 'weather']
RUN = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
REPAIR_DIR = ROOT / '00_SHARED' / 'repair_runs' / RUN
REPAIR_DIR.mkdir(parents=True, exist_ok=True)
PATHS = {k:Path(v) for k,v in ARTIFACT_PATHS.items()}
DATA = ROOT / '00_SHARED/dataset_from_lecturer/03_Bicycle_Rental_Demand.csv'
DATA_SHA = hashlib.sha256(DATA.read_bytes()).hexdigest()
def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def save(key, obj):
    path = PATHS[key]
    path.parent.mkdir(parents=True, exist_ok=True)
    for old in (path, path.with_name(path.name+'.provenance.json')):
        if old.is_file():
            backup = REPAIR_DIR / 'backup' / old.relative_to(ROOT)
            backup.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(old, backup)
    if path.suffix == '.csv': obj.to_csv(path,index=False,encoding='utf-8-sig')
    elif path.suffix == '.joblib': joblib.dump(obj,path)
    elif path.suffix == '.json': path.write_text(json.dumps(obj,ensure_ascii=False,indent=2,default=str),encoding='utf-8')
    else: path.write_text(str(obj),encoding='utf-8')
    receipt = dict(artifact=key,path=str(path),sha256=sha(path),dataset_sha256=DATA_SHA,role='user-authorized coordinated repair',saved_utc=datetime.now(timezone.utc).isoformat(),run_directory=str(REPAIR_DIR))
    path.with_name(path.name+'.provenance.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
    return path
def load(key):
    p=PATHS[key]
    if p.suffix=='.joblib': return joblib.load(p)
    if p.suffix=='.json': return json.loads(p.read_text(encoding='utf-8'))
    if p.suffix=='.csv': return pd.read_csv(p)
    return p.read_text(encoding='utf-8')
def preprocess():
    return ColumnTransformer([('num',Pipeline([('imputer',SimpleImputer(strategy='median')),('scaler',StandardScaler())]),NUMERIC),('cat',Pipeline([('imputer',SimpleImputer(strategy='most_frequent')),('onehot',OneHotEncoder(handle_unknown='ignore',sparse_output=False))]),['weather'])],remainder='drop')
def metrics(model, frame, split):
    pred=model.predict(frame[FEATURES])
    assert np.isfinite(pred).all()
    return dict(dataset_split=split,n=len(frame),MAE=float(mean_absolute_error(frame.rental_count,pred)),RMSE=float(np.sqrt(mean_squared_error(frame.rental_count,pred))),R2=float(r2_score(frame.rental_count,pred)))
def run_role(role):
    if role=='M1':
        definitions = {'record_id':'Unique synthetic identifier; exclude from model inputs.','timestamp':'Local time at the beginning of the predicted hour.','hour':'Hour 0-23, known before prediction.','temperature_c':'Forecast temperature in degrees Celsius.','humidity_pct':'Forecast relative humidity in percent; Guide range 35-99.','weather':'Forecast: Clear, Cloudy, Light_Rain, Heavy_Rain.','wind_speed_kmh':'Forecast wind speed in km/h.','is_working_day':'1 Monday-Friday; 0 weekend; holidays not modelled.','day_of_week':'0 Monday through 6 Sunday.','rental_count':'Target: synthetic rentals per hour.'}
        raw=pd.read_csv(DATA)
        save('data_dictionary',pd.DataFrame([dict(column_name=c,data_type=str(raw[c].dtype),description=definitions[c],role='target' if c=='rental_count' else 'identifier' if c=='record_id' else 'input') for c in raw.columns]))
        print('M1 dictionary repaired: exact column meanings; synthetic data.')
    elif role=='M2':
        frame=pd.read_csv(DATA,parse_dates=['timestamp']).sort_values('timestamp').reset_index(drop=True)
        assert len(frame)==2000 and frame.timestamp.is_unique and frame.rental_count.notna().all()
        a,b=int(len(frame)*.7),int(len(frame)*.85)
        train,val,test=frame.iloc[:a].copy(),frame.iloc[a:b].copy(),frame.iloc[b:].copy()
        assert train.timestamp.max()<val.timestamp.min()<test.timestamp.min()
        for k,v in [('train',train),('validation',val),('test',test)]: save(k,v)
        save('split_manifest',dict(method='chronological',ratios=[.7,.15,.15],target='rental_count',features=FEATURES,excluded=['record_id','timestamp'],dataset_sha256=DATA_SHA,partitions={k:dict(n=len(v),start=str(v.timestamp.min()),end=str(v.timestamp.max())) for k,v in [('train',train),('validation',val),('test',test)]}))
        prep=preprocess().fit(train[FEATURES])
        save('preprocessor',prep)
        save('preprocessing_recipe',dict(features=FEATURES,numeric=NUMERIC,categorical=['weather'],numeric_imputation='training median',categorical_imputation='training most_frequent',encoding='onehot ignore unknown; app rejects unsupported categories',scaling='standard numeric',fit_partition='train',excluded=['record_id','timestamp','rental_count']))
        save('input_schema',dict(features=[dict(name=c,type='string' if c=='weather' else 'int' if c in ['hour','is_working_day','day_of_week'] else 'float') for c in FEATURES],target=dict(name='rental_count',unit='rentals/hour')))
        print('M2 PASS: 1400/300/300 chronological split; seven inputs; preprocessing fit on train only.')
    elif role=='M3':
        train,val=load('train'),load('validation')
        for key, estimator in [('baseline',DummyRegressor(strategy='mean')),('model_a',LinearRegression())]:
            pipeline=Pipeline([('preprocessor',copy.deepcopy(load('preprocessor'))),('regressor',estimator)])
            pipeline.fit(train[FEATURES],train.rental_count)
            path=save(key+'_pipeline',pipeline)
            result=metrics(pipeline,val,'validation')
            result.update(model=type(estimator).__name__,settings=estimator.get_params(),pipeline_sha256=sha(path),seed=42)
            save(key+'_metrics',result)
            print(key,json.dumps({k:result[k] for k in ['model','MAE','RMSE','R2']}))
    elif role=='M4':
        train,val=load('train'),load('validation')
        pipeline=Pipeline([('preprocessor',copy.deepcopy(load('preprocessor'))),('regressor',RandomForestRegressor(n_estimators=100,random_state=42,n_jobs=-1))])
        pipeline.fit(train[FEATURES],train.rental_count)
        p=save('model_b_pipeline',pipeline)
        result=metrics(pipeline,val,'validation')
        result.update(model='RandomForestRegressor',settings=pipeline.named_steps['regressor'].get_params(),pipeline_sha256=sha(p),seed=42)
        save('model_b_metrics',result)
        rows=[]
        for name in ['baseline','model_a','model_b']:
            m=load(name+'_metrics')
            assert m['dataset_split']=='validation' and m['pipeline_sha256']==sha(PATHS[name+'_pipeline'])
            rows.append(dict(candidate=name,algorithm=m['model'],MAE=m['MAE'],RMSE=m['RMSE'],R2=m['R2']))
        comparison=pd.DataFrame(rows).sort_values(['MAE','RMSE','candidate'])
        save('model_comparison',comparison)
        winner=comparison.iloc[0]['candidate']
        save('model_selection',dict(pipeline_key=winner+'_pipeline',selection_metric='validation MAE; RMSE then name break ties',selection_reason='Lowest validation MAE in current comparison',selected_at_utc=datetime.now(timezone.utc).isoformat(),test_used_for_selection=False,fit_partition='train; no refit'))
        selected=load(winner+'_pipeline')
        final_path=save('final_pipeline',selected)
        versions={x:importlib.metadata.version(x) for x in ['scikit-learn','joblib','pandas','numpy','scipy']}
        save('model_metadata',dict(pipeline_key=winner+'_pipeline',algorithm=type(selected.named_steps['regressor']).__name__,created_at_utc=datetime.now(timezone.utc).isoformat(),libraries=versions,features=FEATURES,dataset_sha256=DATA_SHA,pipeline_sha256=sha(final_path),repair_run=RUN,postprocessing='none; UI displays raw estimate to 2 decimals'))
        final=joblib.load(final_path)
        assert list(final.feature_names_in_)==FEATURES
        test=load('test')
        m=metrics(final,test,'test')
        m.update(pipeline_hash=sha(final_path),model_name=type(final.named_steps['regressor']).__name__,evaluation_status='REPEATED after correcting implementation; test previously inspected; not a fresh untouched holdout',test_used_for_tuning=False,settings_frozen_before_this_test=True)
        save('final_test_metrics',m)
        print(comparison.to_string(index=False))
        print('FINAL TEST',json.dumps(m))
    else:
        raise ValueError(role)
