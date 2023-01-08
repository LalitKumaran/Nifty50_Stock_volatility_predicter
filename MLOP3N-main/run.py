import dask
from dask.distributed import Client
import dask.dataframe as dd
from datetime import datetime
import numpy as np
import pandas as pd
import os
import tqdm
import pandas as pd
PATH='/home/u170690/MLOP3N/d1/src/'
dB = dd.read_csv(PATH+'*_minute_data.csv',include_path_column=True)

import warnings
warnings.filterwarnings('ignore')
# dB.head()
dB = dB.drop(columns='Unnamed: 0',axis=0)

def clean_data(row):
#     global errors
    row= row[28:-16]
    return row

dB['path'] = dB['path'].map(clean_data)
dB.persist()
df = dB.compute()

m= df['date']
# y = pd.to_datetime(m,infer_datetime_format=True,utc=False,errors='ignore')
n =  2157*16 #chunk row size
list_df = [m[i:i+n] for i in range(0,df.shape[0],n)]
y = pd.Series()
for i in list_df:
    tmp = pd.to_datetime(i,infer_datetime_format=True,utc=False,errors='ignore')
    y = pd.concat([y,tmp],axis=0)
df['date'] = m

df.to_parquet('d1_minute.parquet',engine='fastparquet')
