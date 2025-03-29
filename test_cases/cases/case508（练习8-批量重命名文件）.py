#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/2/19 21:09
=================================================='''
import os
import random

def test1():
    # 获取目标文件夹中的所有文件名
    file_list = os.listdir('../../resources/file1/')
    # 遍历文件列表
    for file_name in file_list:
        # 构建完整的文件路径
        old_file_path = os.path.join('../../resources/file1/', file_name)
        print(old_file_path)

        new_name=str(random.randint(10000,99999))+'.yaml'
        new_file_path = os.path.join('../../resources/file1/', new_name)
        print(new_file_path)
        # 重命名文件
        os.rename(old_file_path, new_file_path)

def test2():
    file_list = os.listdir('../../resources/file1/')
    for file_name in file_list:
        old_file_path = os.path.join('../../resources/file1/', file_name)
        new_name=str(random.randint(10000,99999))+'.yaml'
        new_file_path = os.path.join('../../resources/file1/', new_name)
        os.rename(old_file_path, new_file_path)

def test3():
    file_list = os.listdir('../../resources/file1/')
    for file_name in file_list:
        old_file_path = os.path.join('../../resources/file1/', file_name)
        new_name=str(random.randint(10000,99999))+'.yaml'
        new_file_path = os.path.join('../../resources/file1/', new_name)
        os.rename(old_file_path, new_file_path)
