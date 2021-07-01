# -*- coding: utf-8 -*-
import pandas as pd
import time
from config import mysqlCli

df = pd.read_csv(r"skmyl.csv", sep='\t', header=None)

df1 = mysqlCli.query_params(table='sqxj_hj_biz_067_qx_skmyl_valid_old', items=["*"])
print(df1)
cols = list(df1.columns)
cols.remove("id")
df.columns = cols

df = df[df['city'] == "衢州"]


code_list = df['hash_unique'].drop_duplicates().to_list()
print(code_list)
for code in code_list:
    dfi = df[df['hash_unique'] == code]
    dfi = dfi.reset_index(drop=True)
    dfi = dfi.head(1)
    print(dfi)
    mysqlCli.insert_df(table='sqxj_hj_biz_067_qx_skmyl_valid_old', df=dfi)
    time.sleep(5)
