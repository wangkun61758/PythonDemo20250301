#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/2/22 13:07
=================================================='''
import schedule

def job1(msg):
    print("执行任务1".format(msg))
schedule.every().day.at("22:47").do(job1, msg='10s')


def job2():
    print('执行任务2')
# schedule.every(2).seconds.do(job2)
schedule.every().second.do(job2)
# schedule.every().minutes.do(job2)  # 每隔 10 分钟运行一次 job 函数
# schedule.every().hour.do(job2)  # 每隔 1 小时运行一次 job 函数
# schedule.every().day.at("22:38").do(job2)  # 每天在 10:30 时间点运行 job 函数
# schedule.every().monday.do(job2)  # 每周一 运行一次 job 函数
# schedule.every().sunday.at("22:38").do(job2)  # 每周三 13：15 时间点运行 job 函数
# schedule.every().minute.at(":38").do(job2)  # 每分钟的 17 秒时间点运行 job 函数


# 定义你要周期运行的函数
def job3(msg):
    print("I'm working...")
    print('接受参数为:{}'.format(msg))
schedule.every(10).seconds.do(job3, msg='10s')

while True:
    schedule.run_pending()
    # time.sleep(1)  # 等待1秒再次检查是否有新的定时任务需要执行
