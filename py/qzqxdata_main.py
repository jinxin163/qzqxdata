# -*- coding: utf-8 -*-
import time
import warnings

from config import mysqlCli
from logger import logger
from queryData import get_update_data_by_table

warnings.filterwarnings("ignore")

table_mapping = {
    "sqxj_hj_biz_067_qx_skmyl_valid_old": "qz_risk_zone_rain",
    "sqxj_hj_biz_067_qx_24xsljmyl_valid_old": "qz_risk_zone_rain_report",
}


def start():
    opds_table_list = table_mapping.keys()
    while True:
        try:
            for opds_table in opds_table_list:
                print(opds_table)
                mysql_table = table_mapping.get(opds_table)
                try:
                    df = get_update_data_by_table(opds_table)

                    if df.empty:
                        continue

                    print(df)
                    mysqlCli.insert_df(mysql_table, df)
                except:
                    logger.exception(msg=mysql_table)

            time.sleep(60)

        except:
            logger.exception(msg='')


if __name__ == "__main__":
    start()
