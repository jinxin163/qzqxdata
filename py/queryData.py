# -*- coding: utf-8 -*-
import datetime
import warnings
import pandas as pd
from config import mysqlCli, odpsCli

warnings.filterwarnings("ignore")


def queryOdps_HoursRain(start_time, end_time):
    sql = f'select * from sgzx_data_center.sqxj_hj_biz_067_qx_skmyl_valid_old where city = "衢州" ' \
          f'and observtimes >= {f"{start_time}"} and observtimes < {f"{end_time}"};'
    reader = odpsCli.execute_sql(sql).open_reader()
    df = reader.to_pandas()
    return df


def queryOdps_ReportRain(start_time, end_time):
    sql = f'select * from sgzx_data_center.sqxj_hj_biz_067_qx_24xsljmyl_valid_old where city = "衢州市" ' \
          f'and reporttimes >= {f"{start_time}"} and reporttimes < {f"{end_time}"};'
    reader = odpsCli.execute_sql(sql).open_reader()
    df = reader.to_pandas()
    return df


def queryMysql_HoursRain(start_time, end_time):
    df = mysqlCli.query_params(table='qz_risk_zone_rain',
                               items=['hash_unique'],
                               where={'observtimes': [start_time, end_time]})
    return df


def queryMysql_ReportRain(start_time, end_time):
    df = mysqlCli.query_params(table='qz_risk_zone_rain_report',
                               items=['hash_unique'],
                               where={'reporttimes': [start_time, end_time]})
    return df


def get_update_data_by_table(opds_table):
    start_time = str(datetime.datetime.now() - datetime.timedelta(days=1))[0:19]
    end_time = str(datetime.datetime.now())[0:19]

    if opds_table == "sqxj_hj_biz_067_qx_skmyl_valid_old":
        df1 = queryOdps_HoursRain(start_time, end_time)
        df2 = queryMysql_HoursRain(start_time, end_time)
    else:
        df1 = queryOdps_ReportRain(start_time, end_time)
        df2 = queryMysql_ReportRain(start_time, end_time)

    if df1.empty or df1 is None:
        return pd.DataFrame()

    df1 = df1.append(df2)
    df1 = df1.append(df2)
    df1 = df1.drop_duplicates(subset=['hash_unique'], keep=False)

    return df1
