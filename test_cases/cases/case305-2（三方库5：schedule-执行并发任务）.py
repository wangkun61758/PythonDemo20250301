#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/2/22 13:07
=================================================='''
import time

import schedule


def job1(msg):
    time.sleep(1)
    print('任务1接受参数为:{}'.format(msg))


def job2(msg):
    time.sleep(2)
    print('任务2接受参数为:{}'.format(msg))


def job3(msg):
    time.sleep(3)
    print('任务3接受参数为:{}'.format(msg))


schedule.every(1).seconds.do(job1, msg='任务1')
schedule.every(3).seconds.do(job2, msg='任务2')
schedule.every(1).seconds.do(job3, msg='任务3')
while 1:
    schedule.run_pending()
