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

