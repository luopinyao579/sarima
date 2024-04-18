import sys
import pandas as pd
import numpy as np
from scipy.stats import norm
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.statespace.sarimax import SARIMAX
import warnings
warnings.filterwarnings('ignore')

q_pos = 0.7
q_nag = 0.3

def data_preprocessing(df):
    df = df.fillna(0)
    df_sta = pd.DataFrame()
    diff = pd.DataFrame(np.zeros((df.shape[1],1)),index=df.columns)
    for i in range(df.shape[1]):
        df_stat,ADF = ADF_DIFF(df.iloc[:,i])
        df_sta= df_sta.append(df_stat)
        diff.loc[df.columns[i],:]=ADF[0]
    df_sta = df_sta.T
    df_sta = df_sta.dropna()
    transfrom = pd.concat([diff],axis=1)
    transfrom.columns=['差分阶数']
    return df_sta,transfrom


def ADF_DIFF(data_ts):
    diff = 0
    dftest = adfuller(data_ts)[1]
    data_ts_diff = data_ts

    while dftest > 0.05:
        data_ts_diff = data_ts_diff.diff().dropna()
        diff += 1
        dftest = adfuller(data_ts_diff)[1]

    ADF = [diff, dftest]
    return data_ts_diff, ADF


def sarima_predict(macro_list):
    macro_list = macro_list.fillna(0)
    maxLag = 3
    season = 4
    idx = pd.date_range(macro_list.index[-1],periods=8,freq='Q-DEC').shift(1)
    macro_predict = pd.DataFrame(index=idx)
    params_sarima = {}
    for i in macro_list.columns:
        diff,adf = ADF_DIFF(macro_list[i])
        d = adf[0]
        a,p,q,model,pp,qq = proper_model(macro_list[i],maxLag,d,season)
        predict = ts_predict(macro_list[i],model,8)
        macro_predict = pd.concat([macro_predict,predict],axis=1,ignore_index=True)
        params_sarima[i] = [p,q,pp,qq,d]
    return macro_predict,params_sarima

def proper_model(data_ts,maxLag,diff,season):
    init_bic = sys.maxsize
    init_p = 0
    init_q = 0
    init_pp = 0
    init_qq = 0
    init_properModel=None
    d = diff
    for p in np.arange(maxLag):
        for q in np.arange(maxLag):
            for pp in np.arange(maxLag):
                for qq in np.arange(maxLag):
                    model =SARIMAX(data_ts,order=(p,d,q),seasonal_order=(pp,0,qq,season),trend='c')
                    try:
                        result_sarima = model.fit(disp=-1)
                    except:
                        continue
                    bic = result_sarima.bic
                    if bic <init_bic:
                        init_p =p
                        init_q =q
                        init_pp = pp
                        init_qq =qq
                        init_properModel = result_sarima
                        init_bic =bic
    return init_bic,init_p,init_q,init_properModel,init_pp,init_qq

def ts_predict(data_ts,ts_model,n_steps):
    idx = pd.date_range(data_ts.index[-1],periods=n_steps,freq='Q-DEC').shift(1)
    f= ts_model.forecast(steps=n_steps)
    result=pd.DataFrame(np.column_stack([f]),index=idx)
    return result

data_path = r"C:\Users\tjhn\Desktop\前瞻模型验证\债券等其他\input_sarima.xlsx"
output_path = r"C:\Users\tjhn\Desktop\前瞻模型验证\债券等其他\predict_macro2.xlsx"

macro_list = pd.read_excel(data_path, sheet_name='Macro_Data', index_col=0)
macro_predict, params_ts = sarima_predict(macro_list)
macro_predict.columns = macro_list.columns
macro_predict_pos = pd.DataFrame(index=macro_predict.index, columns=macro_predict.columns)
macro_predict_nag = pd.DataFrame(index=macro_predict.index, columns=macro_predict.columns)
std = macro_list.std()
print(std)

for i in macro_list.columns:
    for j in range(len(macro_predict)):
        macro_predict_pos[i][j] = norm.ppf(q=q_pos, loc=macro_predict[i][j], scale=std[i])
        macro_predict_nag[i][j] = norm.ppf(q=q_nag, loc=macro_predict[i][j], scale=std[i])

macro_predict = macro_predict.reset_index(drop=False)
print(macro_predict)
print(params_ts)

# 写入 Excel 文件
with pd.ExcelWriter(output_path) as writer:
    macro_predict.to_excel(excel_writer=writer, sheet_name='基准', index=False)
    macro_predict_nag.to_excel(excel_writer=writer, sheet_name='悲观', index=False)
    macro_predict_pos.to_excel(excel_writer=writer, sheet_name='乐观', index=False)
