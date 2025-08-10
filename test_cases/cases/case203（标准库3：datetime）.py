#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/2/7 23:08
=================================================='''
import time
from datetime import datetime, timedelta, date


def test1():
    time1 = datetime.now()  # 当前时间 2025-02-10 08:00:05.172923
    time1_delta = time1 + timedelta(days=1, hours=2, minutes=3, seconds=4)  # 调整时间
    time_sring = time1_delta.strftime('%Y-%m-%d %H:%M:%S')  # 转化时间格式 2025-02-11 10:03:09(将 datetime 对象格式化为字符串)

    # 从字符串创建 datetime 对象
    date_str = "2023-03-15 14:30:45"
    specific_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    print("从字符串创建的时间:", specific_time)

    time2 = datetime.now().date()  # 2025-02-10
    time3 = datetime.now().time()  # 08:18:35.804948
    time4 = datetime(2025, 1, 2, 13, 14, 15)  # 创建指定时间
    time4_1 = time4 + timedelta(days=2)  # 2025-01-04 13:14:15
    time5 = datetime(2025, 1, 2)  # 2025-01-02 00:00:00

    time6 = datetime(2025, 5, 16, 17, 23, 36)
    time7 = datetime(2025, 2, 3, 11, 24, 16)
    timedelta1 = time6 - time7  # 102 days, 5:59:20
    # 创建指定日期
    time8 = date(2025, 5, 16)  # 2025-05-16
    time9 = datetime.now()
    time9_1 = time9.timetuple()  # 返回日期对象的元组格式
    print(
        time9_1)  # time.struct_time(tm_year=2025, tm_mon=2, tm_mday=10, tm_hour=8, tm_min=53, tm_sec=38, tm_wday=0, tm_yday=41, tm_isdst=-1)
    # 创建时分秒对象
    specific_time = datetime(2025, 5, 16, 17, 23, 36)
    time10 = specific_time.strftime('%H:%M:%S')  # 17:23:36
    print("时分秒:", time10)

