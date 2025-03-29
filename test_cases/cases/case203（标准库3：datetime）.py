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
    #创建指定日期
    time8 = date(2025, 5, 16)  # 2025-05-16
    time9 = datetime.now()
    time9_1 = time9.timetuple()  # 返回日期对象的元组格式
    print(time9_1)  # time.struct_time(tm_year=2025, tm_mon=2, tm_mday=10, tm_hour=8, tm_min=53, tm_sec=38, tm_wday=0, tm_yday=41, tm_isdst=-1)
    # 创建时分秒对象
    specific_time = datetime(2025, 5, 16, 17, 23, 36)
    time10 = specific_time.strftime('%H:%M:%S')  # 17:23:36
    print("时分秒:", time10)
def test2():
    '''
    days：天数
    hours：小时数（等于 seconds 的 3600 分之
    minutes：分钟数（等于 seconds 的 60 分之一）
    seconds：秒数
    milliseconds：毫秒数（等于 seconds 的 1000 分之一）
    microseconds：微秒数
    :return:
    '''
    now = datetime.now()  # 2025-02-07 23:09:50.199752
    print(now)

    time2 = now + timedelta(7)  # 2025-02-15 13:43:25.701707
    print(time2)

    time3 = datetime(2025, 2, 8, 15, 12, 00)  # 2025-02-08 15:12:00
    print(time3)
    time4 = time3 + timedelta(3)  # 2025-02-08 15:12:00
    print(time4)

    time5 = time3 + timedelta(3, 2, 3)  # 2025-02-11 15:12:02.000003
    print(time5)

    time6 = time3 + timedelta(3333, 2, 3)  # 2034-03-26 15:12:02.000003
    print(time6)

    now1 = datetime.now()  # 2025-02-09 01:03:13.095257
    print(now1)
    time7 = now1 + timedelta(days=13, hours=2, minutes=1, seconds=22)  # 2025-02-22 03:04:35.095257
    print(time7)

    now2 = datetime.now()  # 2025-02-09 01:07:20.276588
    print(now2)
    time8 = now2 + timedelta(days=13, hours=2, minutes=1, seconds=22, microseconds=13,
                             milliseconds=5)  # 2025-02-22 03:08:42.281601
    print(time8)

    time9 = datetime(2025, 5, 16, 17, 23, 36)
    time10 = datetime(2025, 2, 3, 11, 24, 16)
    timedelta1 = time9 - time10  # 102 days, 5:59:20
    print(timedelta1)
    timedelta2 = time10 - time9  # -103 days, 18:00:40
    print(timedelta2)

    time10 = datetime.now()
    time10_1 = time10 + timedelta(days=2, hours=3, minutes=4, seconds=12)
    time_Style = time10_1.strftime('%Y-%m-%d %H:%M:%S')  # 2025-02-11 17:13:17
    print(time_Style)
    time11 = datetime(2025, 1, 1, 12, 13, 13)
    time11_1 = time11 + timedelta(days=1, hours=2, minutes=3, seconds=4)
    time_style11 = time11_1.strftime('%Y-%m-%d %H:%M:%S')
    print(time_style11)

    time12 = datetime.now()
    time12_2 = time12 + timedelta(days=1, hours=2, minutes=3, seconds=4)
    time_style12 = time12_2.strftime('%Y-%m-%d %H:%M:%S')
    print(time_style12)

    time13 = datetime(2025, 1, 1, 2, 3, 4)
    time13_1 = time13 + timedelta(days=12)
    time_Style13 = time13_1.strftime('%Y-%m-%d %H:%M:%S')
    print(time_Style13)
def test3():
    now = time.time()
    print(now)  # 1738993405.7026286
    time_arraw = time.localtime(now)
    print(
        time_arraw)  # time.struct_time(tm_year=2025, tm_mon=2, tm_mday=8, tm_hour=13, tm_min=43, tm_sec=25, tm_wday=5, tm_yday=39, tm_isdst=0)

    time_Style = time.strftime('%Y-%m-%d %H:%M:%S', time_arraw)
    print(time_Style)  # 2025-02-08 13:43:25
def test4():
    time1 = datetime.now()
    time1_1 = time1 + timedelta(days=2)
    time_style = time1_1.strftime('%Y-%m-%d %H:%M:%S')
def test5():
    time1=datetime.now()
    print(time1)
    time2=time1+timedelta(days=1,hours=2,minutes=3,seconds=4)
    print(time2)
    time3=time2.strftime('%Y-%m-%d %H:%M:%S')
    print(time3)

    time4=datetime.now().date()
    print(time4)
    time5=time1.strftime('%H:%M:%S')
    print(time5)
    str1='2025-1-2 13:14:55'
    time6=datetime.strptime(str1,'%Y-%m-%d %H:%M:%S')
    print(time6)

    time7=datetime(2025,1,2,3,4,5)
    time8=datetime(2024,2,3,1,2,3)
    time9=time7-time8
    print(time9)
    time10=date(2025,1,5)
    print(time10)
def test6():
    a=datetime.now()
    print(a)
    b=a+timedelta(days=2,hours=3,minutes=5,seconds=22)
    print(b)
    c=b.strftime('%Y-%m-%d %H:%M:%S')
    print(c)

    d1=datetime(2025,1,2,3,4,55)
    d2=datetime(2026,5,2,6,22,55)
    e=d2-d1
    print(e)

    f=a.strftime('%H:%M:%S')
    print(f)
    str1 = '2025-1-2 13:14:55'
    g=datetime.strptime(str1,'%Y-%m-%d %H:%M:%S')
    print(g)
def test7():
    datetime1=datetime.now()
    datetime1_1 = datetime1 + timedelta(days=1)
    datetime1_2=datetime1_1.strftime('%Y-%m-%d %H:%M:%S')
    print(datetime1_2)
    datetime2=datetime(2025,2,3,4,5,6)
    a=datetime2.strftime('%Y-%m-%d %H:%M:%S')
    str1='2025-1-2 13:14:55'
    b=datetime.strptime(str1,'%Y-%m-%d %H:%M:%S')
    print(b)