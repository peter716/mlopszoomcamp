#!/usr/bin/env python
# coding: utf-8

# In[1]:



import pickle
import pandas as pd

import sys


# In[4]:


with open('model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)




categorical = ['PULocationID', 'DOLocationID']

def read_data(filename):
    df = pd.read_parquet(filename)
    
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    return df


# In[13]:

taxi_type = sys.argv[1]
year = int(sys.argv[2])
month = int(sys.argv[3])

input_file = f'https://d37ci6vzurychx.cloudfront.net/trip-data/{taxi_type}_tripdata_{year:04d}-{month:02d}.parquet'
output_file = f'output/{taxi_type}/{taxi_type}_tripdata_{year:04d}-{month:02d}.parquet'
df = read_data(input_file)



dicts = df[categorical].to_dict(orient='records')
X_val = dv.transform(dicts)
y_pred = model.predict(X_val)


# In[20]:


df_result = pd.DataFrame()
#df_result['ride_id'] = df['ride_id']
df_result['ride_id'] = f'{year:04d}/{month:02d}_' + df.index.astype('str')

df_result['predicted_duration'] = y_pred
#df_result['diff'] = df_result['actual_duration'] - df_result['predicted_duration']
#df_result['model_version'] = RUN_ID



print(df_result.describe())



df_result.to_parquet(
    output_file,
    engine='pyarrow',
    compression=None,
    index=False
)


# In[ ]:

#python script.py yellow 2023 4


