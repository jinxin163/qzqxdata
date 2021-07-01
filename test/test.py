# -*- coding: utf-8 -*-
import datetime

now = str(datetime.datetime.now())
print(now)
hours = int(now[11:13])

if hours < 1:
    start_time = str(datetime.datetime.now() - datetime.timedelta(days=1))[0:11] + ' 00:00:00'
    end_time = str(datetime.datetime.now())[0:11] + ' 00:00:00'
else:
    start_time = str(datetime.datetime.now())[0:11] + ' 00:00:00'
    end_time = str(datetime.datetime.now() + datetime.timedelta(days=1))[0:11] + ' 00:00:00'

print(start_time)
print(end_time)

start_time = str(datetime.datetime.now() - datetime.timedelta(days=1))[0:19]
end_time = str(datetime.datetime.now())[0:19]
print(start_time)
print(end_time)

sql = f'select * from sgzx_data_center.sqxj_hj_biz_067_qx_skmyl_valid_old where city = "衢州" ' \
          f'and observtimes >= \"{start_time}\" and observtimes < \"{end_time}\";'
print(sql)

sql = f'select * from sgzx_data_center.sqxj_hj_biz_067_qx_24xsljmyl_valid_old where city = "衢州市" ' \
          f'and reporttimes >= \"{start_time}\" and reporttimes < \"{end_time}\";'
print(sql)