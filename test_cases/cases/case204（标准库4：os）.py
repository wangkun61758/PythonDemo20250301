#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/2/7 23:15
=================================================='''
import os
import shutil
def test1():
    if not os.path.exists('../../resources/os/'):  # 函数用于检查指定路径是否存在，无论是文件还是目录。如果路径存在，函数返回True；如果路径不存在，返回False
        os.makedirs('../../resources/os/')  # 创建目录

    dirs = os.listdir('../../resources/os')  # 返回指定路径下的所有文件和目录名称的列表
    print(dirs)  # ['history.json', 'json1.json', 'test']
    for i in dirs:
        path = os.path.join('../../resources/os', i)  # 用于拼接路径，可以传入多个参数
        if os.path.isdir(path):  # 判断对象是否为一个目录
            print('是目录')
            # os.rmdir(path1)#删除指定路径的目录。仅当这文件夹是空的才可以, 否则, 抛出OSError
            shutil.rmtree(path)  ## 递归删除文件夹下的所有子文件夹(目录)和子文件(目录为空也不会报错)
        if os.path.isfile(path):  # 判断对象是否为一个文件
            if path.endswith('.json'):
                print("该文件为json文件")  # 该文件为json文件
            # os.remove(path)

    print(os.path.join('111', '222', '333'))  # 111/222/333

    '''
    os.walk(path, topdown=True, onerror=None, followlinks=False)
    path：必需参数，表示要遍历的目录的路径
    topdown：可选参数，布尔值。如果为 True（默认），则先遍历顶层目录，再遍历子目录。如果为 False，则先遍历子目录，再遍历顶层目录。
    onerror：可选参数，如果指定(默认None)，遇到错误时会调用该函数（通常是权限错误）。
    followlinks：可选参数，布尔值。如果为 True，会跟随目录中的符号链接（软链接）。
    '''
    for dirpath, dirnames, filenames in os.walk('../../resources/data'):#遍历目录树
        print(dirpath)
        for dirname in dirnames:
            print(f'{dirname}')
        for filename in filenames:
            print(f'{filename}')

    if not os.path.exists('../resources/rmtree/'):
        os.makedirs('../resources/rmtree/')
    shutil.rmtree('../resources/rmtree/')  # 递归删除文件夹下的所有子文件夹(目录)和子文件

    directory = os.path.dirname('../../resources/data/order.yaml')  # 获取文件路径的目录部分
    print(directory)  # ../resources/data

    m = os.path.basename('../../resources/data/order.yaml')  # 获取文件路径的文件部分
    print(m)  # order.yaml

    # 获取指定路径的绝对路径
    filename = "2013-07-04 (1).jpg"
    absolute_path = os.path.abspath(filename)  # D:\Python\PythonDemo20250101\test_cases\2013-07-04 (1).jpg
    print(absolute_path)

    file_name, file_extension = os.path.splitext(filename)#将文件名分割成两部分：文件名和扩展名
    print(file_name,file_extension)#2013-07-04 (1) .jpg
    print(os.path.splitext(filename))  # ('2013-07-04 (1)', '.jpg')

def test2():
    if not os.path.exists('../../resources/os/'):
        os.makedirs('../../resources/os')
    list1=os.listdir('../../resources/os')
    for i in list1:
        path1=os.path.join('../../resources/os/', i)
        if os.path.isdir(path1):
            print('是目录')
            a=os.path.dirname(path1)
            print(a)
            # os.rmdir(path1)#删除指定路径的目录。仅当这文件夹是空的才可以, 否则, 抛出OSError
            shutil.rmtree(path1)## 递归删除文件夹下的所有子文件夹(目录)和子文件(目录不为空也不会报错)
        if os.path.isfile(path1):
            print('是文件')
            b=os.path.basename(path1)
            print(b)
            if path1.endswith('.json'):
                print('是json文件')
                os.remove(path1)

    for path2,dir2,file2 in os.walk('../../resources/'):
        for a in dir2:
            print(f'{a}')
        for b in file2:
            print(f'{b}')

def test3():
    if not os.path.exists('../../resources/os/'):
        os.makedirs('../../resources/os')
        list1=os.listdir('../../resources/os')
        for i in list1:
            path1=os.path.join('../../resources/os/', i)
            if os.path.isdir(path1):
                print('是目录')
                print(os.path.dirname(path1))
                shutil.rmtree(path1)
            if os.path.isfile(path1):
                os.remove(path1)
                print(os.path.basename())

