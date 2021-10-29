# -*- coding: utf-8 -*-
from config import odpsCli

tables = ["sqxj_hj_biz_067_qx_qxyj_valid_old",
          "sqxj_hj_biz_067_qx_qxskfxxsxx_valid_old",
          "sqxj_hj_biz_067_qx_zdqxz5fzljjs_valid_old",
          "sqxj_hj_biz_067_qx_dmgcz_valid_old",
          "sqxj_hj_biz_067_qx_qyqxzgc_valid_old",
          "sqxj_hj_biz_067_qx_qyqxzd_valid_old",
          "sqxj_hj_biz_067_qx_skmyl_valid_old",
          "sqxj_hj_biz_067_qx_24xsljmyl_valid_old",
          "slt_hj_biz_033_fd_imp_warn_index_valid_old"]

for table in tables:
    sql = f'select * from sgzx_data_center.{table} limit 10;'
    reader = odpsCli.execute_sql(sql).open_reader()
    df = reader.to_pandas()
    df.to_csv(f'{table}.csv', index=False)
