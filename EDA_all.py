#%%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#%% reduce_mem_usage
def reduce_mem_usage(df, verbose=True):
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    start_mem = df.memory_usage().sum() / 1024**2    
    for col in df.columns:
        col_type = df[col].dtypes
        if col_type in numerics:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == 'int':
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)  
            else:
                if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                    df[col] = df[col].astype(np.float16)
                elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)    
    end_mem = df.memory_usage().sum() / 1024**2
    if verbose: print('Mem. usage decreased to {:5.2f} Mb ({:.1f}% reduction)'.format(end_mem, 100 * (start_mem - end_mem) / start_mem))
    return df
#%% df processing
df_113_Filter = df_113.loc[(df_113['stop'] == 1)&(df_113['composition'] != 0)]
df_all_Filter = df_all_Filter.sort_values(by=["訴訟編號", "EY_PK", "證交日期", "成交價"], 
                            ascending=[True, True, False, True])
df1 = df_DTCC.copy()
df1 = df1.drop(["備註"], axis=1)
df1 = df1[~df1["訴訟編號"].isin(except_Acc)]

#%% 時間處理
df['date'] = pd.to_datetime(df['date'])
start_date = '2022-01-02'
end_date = '2022-01-04'
filtered_df = df.loc[(df['date'] >= start_date) & (df['date'] <= end_date)]