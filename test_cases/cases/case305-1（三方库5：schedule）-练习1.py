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

while True:
    schedule.run_pending()
    # time.sleep(1)  # 等待1秒再次检查是否有新的定时任务需要执行
