#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/12/3 8:44
=================================================='''
import os.path
import shutil

def test1():
    list_dirs = os.listdir('../../resources/')
    for i in list_dirs:
        path = os.path.join('../../resources/', i)
        print(path)
        if os.path.isdir(path):
            if 'parse_qs' in path and path != '../../resources/parse_qs':
                # os.rmdir(path)#只能删除空目录
                shutil.rmtree(path, ignore_errors=False)  # 支持删除非空目录
        else:
            os.path.isfile(path)
            pass
            # print('是文件不删除')

def test2(paths):
    list_dirs = os.listdir(paths)
    for i in list_dirs:
        path= os.path.join('paths', i)
        print(path)
        if os.path.isdir(path):
            if 'o' in path:
                shutil.rmtree(path, ignore_errors=False)
        else:
            os.path.isfile(path)
            print('是文件不删除')
test2('../reso')
