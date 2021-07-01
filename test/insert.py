# -*- coding: utf-8 -*-
from py.config import odpsCli


def queryOdps(sql):
    reader = odpsCli.execute_sql(sql).open_reader()
    df = reader.to_pandas()
    return df


if __name__ == '__main__':
    sql = 'select * from sgzx_data_center.sqxj_hj_biz_067_qx_24xsljmyl_valid_old where city="衢州市";'
    df = queryOdps(sql=sql)
    df.to_csv('24xsljmyl.csv', index=False)

