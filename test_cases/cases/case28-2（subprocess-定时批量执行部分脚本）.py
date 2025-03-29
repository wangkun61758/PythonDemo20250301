#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/2/13 12:19
=================================================='''
import os
import subprocess
import time
import schedule
'''
./：代表目前所在目录
../"：代表上一级目录
../../：代表上上级目录
'''
def batch_run():
    # print(os.getcwd())#查看当前文件的工作路径 D:\Python\PythonDemo20250101\test_cases
    directory = '../../test_cases/cases'#../表示以'case28-1（subprocess-批量执行部分脚本）.py'为原点回到'case28-1（subprocess-批量执行部分脚本）.py'的上一级目录test_cases
    # 遍历目录中的所有文件
    for filename in os.listdir(directory):#遍历test_cases
        # 构造完整的文件路径
        file_path1 = os.path.join(directory, filename)
        # 检查是否是文件以及是否可执行（对于Python脚本通常不需要检查）
        if os.path.isfile(file_path1):
            try:
                subprocess.run(['python', file_path1], check=True)# 使用subprocess运行脚本
            except subprocess.CalledProcessError as e:
                print(f"Error running {file_path1}: {e}")
        else:
            for file2 in os.listdir(file_path1):#遍历test_cases下的文件夹
                file_path2 = os.path.join(file_path1, file2)
                if os.path.isfile(file_path2):
                    try:
                        subprocess.run(['python', file_path2], check=True)# 使用subprocess运行脚本
                    except subprocess.CalledProcessError as e:
                        print(f"Error running {file_path2}: {e}")

schedule.every(5).seconds.do(batch_run)
while True:
    schedule.run_pending()
    time.sleep(1)

schedule.every().day.do(batch_run)
while True:
    schedule.run_pending()
    time.sleep(1)
schedule.every(5).seconds.do(batch_run)
while True:
    schedule.run_pending()
    time.sleep(1)

schedule.every(5).seconds.do(batch_run)
while True:
    schedule.run_pending()
    time.sleep(1)
schedule.every(5).seconds.do(batch_run)
while True:
    schedule.run_pending()
    time.sleep(1)
'''
练习：2025/3/20（5）
'''
schedule.every(5).days.do(batch_run)
while True:
    schedule.run_pending()
    time.sleep(1)
schedule.every(5).days.do(batch_run)
while True:
    schedule.run_pending()
    time.sleep(1)

schedule.every(5).days.do(batch_run)
while True:
    schedule.run_pending()
    time.sleep(1)