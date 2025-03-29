#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/2/13 12:19
=================================================='''
import os
import subprocess

'''
./：代表目前所在目录
../"：代表上一级目录
../../：代表上上级目录
subprocess.run(['python', path1], check=True, text=True, capture_output=True)
['python', path1]：要执行的命令
check=True：布尔值，默认是 False。如果设为 True，命令返回非零退出状态码时会引发 CalledProcessError 异常
text：如果设为 True，会将输出解码为字符串，否则返回字节类型
capture_output：如果设为 True，则同时捕获标准输出和标准错误
'''
def test1():
    # print(os.getcwd())#查看当前文件的工作路径 D:\Python\PythonDemo20250101\test_cases
    directory = '../../test_cases/cases'#../表示以'case28-1（subprocess-批量执行部分脚本）.py'为原点回到'case28-1（subprocess-批量执行部分脚本）.py'的上一级目录test_cases
    # 遍历目录中的所有文件
    for filename in os.listdir(directory):#遍历test_cases
        # 构造完整的文件路径
        file_path1 = os.path.join(directory, filename)
        print('file_path:' + str(file_path1))
        # 检查是否是文件以及是否可执行（对于Python脚本通常不需要检查）
        if os.path.isfile(file_path1):
            try:
                subprocess.run(['python', file_path1], check=True)# 使用subprocess运行脚本
            except subprocess.CalledProcessError as e:
                print(f"Error running {file_path1}: {e}")
        else:
            os.path.isdir(file_path1)
            print('是目录')
            for file2 in os.listdir(file_path1):#遍历test_cases下的文件夹
                file_path2 = os.path.join(file_path1, file2)
                print('file_path2:' + str(file_path2))
                # 检查是否是文件以及是否可执行（对于Python脚本通常不需要检查）
                if os.path.isfile(file_path2):
                    try:
                        subprocess.run(['python', file_path2], check=True)# 使用subprocess运行脚本
                    except subprocess.CalledProcessError as e:
                        print(f"Error running {file_path2}: {e}")
def test2():
    directory = '../../test_cases/cases'
    for filename in os.listdir(directory):
        file_path1 = os.path.join(directory, filename)
        if os.path.isfile(file_path1):
            try:
                subprocess.run(['python',file_path1],check=True)
            except subprocess.CalledProcessError as e:
                print(f'Error running {file_path1}: {e}')
        else:
            os.path.isdir(file_path1)
            print('目录')
def test3():
    directory = '../../test_cases/cases'
    for filename in os.listdir(directory):
        path1 = os.path.join(directory, filename)
        if os.path.isfile(path1):
            if os.path.basename(path1).endswith('.py'):  ## 获取文件路径的文件部分
                print('path1:' + str(path1))
                try:
                    subprocess.run(['python',path1],check=True)#check=True 表示如果命令执行失败，函数将抛出一个 subprocess.CalledProcessError 异常
                except subprocess.CalledProcessError as e:
                    print(f"Error running {path1}: {e}")
def test4():
   directory = '../../test_cases/cases'
   for filename in os.listdir(directory):
       path1=os.path.join(directory,filename)
       if os.path.isfile(path1):
           try:
               subprocess.run(['python',path1],check=True)
           except subprocess.CalledProcessError as e:
               print(f'Error running {path1}: {e}')
def test5():
    directory = '../../test_cases/cases'
    for filename in os.listdir(directory):
        path1=os.path.join(directory,filename)
        if os.path.isfile(path1):
            try:
                subprocess.run(['python', path1], check=True)
            except subprocess.CalledProcessError as e:
                print(f'Error running {path1}:{e}')
def test6():
    directory = '../../test_cases/cases'
    for filename in os.listdir(directory):
        path1=os.path.join(directory,filename)
        if os.path.isfile(path1):
            try:
                subprocess.run(['python',path1], check=True)
            except subprocess.CalledProcessError as e:
                print(f'Error running {path1}:{e}')
def test7():
    directory = '../../test_cases/cases'
    for filename in os.listdir(directory):
        path1=os.path.join(directory,filename)
        if os.path.isfile(path1):
            try:
                subprocess.run(['python',path1],check=True)
            except subprocess.CalledProcessError as e:
                print(f'Error running {path1}:{e}')
def test8():
    directory = '../../test_cases/cases'
    for filename in os.listdir(directory):
        path1=os.path.join(directory,filename)
        if os.path.isfile(path1):
            try:
                subprocess.run(['python',path1],check=True)
            except subprocess.CalledProcessError as e:
                print(f'Error running {path1}:{e}')
def test9():
    directory = '../../test_cases/cases'
    for filename in os.listdir(directory):
        path1=os.path.join(directory,filename)
        if os.path.isfile(path1):
            try:
                subprocess.run(['python',path1],check=True)
            except subprocess.CalledProcessError as e:
                print(f'Error running {path1}:{e}')
def test10():
    directory = '../../test_cases/cases'
    for filename in os.listdir(directory):
        path1=os.path.join(directory,filename)
        if os.path.isfile(path1):
            try:
                subprocess.run(['python',path1],check=True)
            except subprocess.CalledProcessError as e:
                print(f'Error running {path1}:{e}')
def test11():
    directory = '../../test_cases/cases'
    for filename in os.listdir(directory):
        path1=os.path.join(directory,filename)
        if os.path.isfile(path1):
            try:
                subprocess.run(['python',path1],check=True)
            except subprocess.CalledProcessError as e:
                print(f'Error running {path1}:{e}')
def test12():
    directory = '../../test_cases/cases'
    for filename in os.listdir(directory):
        path1=os.path.join(directory,filename)
        if os.path.isfile(path1):
            try:
                subprocess.run(['python',path1],check=True)
            except subprocess.CalledProcessError as e:
                print(f'Error running {path1}:{e}')
def test13():
    directory = '../../test_cases/cases'
    for filename in os.listdir(directory):
        path1=os.path.join(directory,filename)
        if os.path.isfile(path1):
            try:
                subprocess.run(['python',path1],check=True)
            except subprocess.CalledProcessError as e:
                print(f'Error running {path1}:{e}')
def test14():
    directory = '../../test_cases/cases'
    for i in os.listdir(directory):
        path=os.path.join(directory,i)
        if os.path.isfile(path):
            try:
                subprocess.run(['python',path],check=True)
            except subprocess.CalledProcessError as e:
                print(f'Error running {path}:{e}')
def test15():
    directory = '../../test_cases/cases'
    list_dir=os.listdir(directory)
    for i in list_dir:
        path=os.path.join(directory,i)
        if os.path.isfile(path):
            try:
                subprocess.run(['python',path],check=True)
            except subprocess.CalledProcessError as e:
                print(f'Error running {path}:{e}')
def test16():
    directory = '../../test_cases/cases'
    list_dir=os.listdir(directory)
    for i in list_dir:
        path=os.path.join(directory,i)
        if os.path.isfile(path):
            try:
                subprocess.run(['python',path],check=True)
            except subprocess.CalledProcessError as e:
                print(f'Error running {path}:{e}')
def test17():
    directory = '../../test_cases/cases'
    list_dir=os.listdir(directory)
    for i in list_dir:
        path=os.path.join(directory,i)
        if os.path.isfile(path):
            try:
                subprocess.run(['python',path],check=True)
            except subprocess.CalledProcessError as e:
                print(f'Error running {path}:{e}')
'''
练习：2025/3/20（3）
'''
def test18():
    directory = '../../test_cases/cases'
    list_dir=os.listdir(directory)
    for i in list_dir:
        path=os.path.join(directory,i)
        if os.path.isfile(path):
            try:
                subprocess.run(['python',path],check=True)
            except subprocess.CalledProcessError as e:
                print(f'Error running {path}:{e}')
def test19():
    list_dir=os.listdir('../../test_cases/cases')
    for i in list_dir:
        path=os.path.join('../../test_cases/cases',i)
        if os.path.isfile(path):
            try:
                subprocess.run(['python', path], check=True)
            except subprocess.CalledProcessError as e:
                print(f'Error running {path}:{e}')
def test20():
    directory = '../../test_cases/cases'
    list_dir=os.listdir(directory)
    for i in list_dir:
        path=os.path.join('../../test_cases/cases',i)
        if os.path.isfile(path):
            try:
                subprocess.run(['python', path], check=True)
            except subprocess.CalledProcessError as e:
                print(f'{path}:{e}')
def test21():
    directory = '../../test_cases/cases'
    list_dir=os.listdir(directory)
    for i in list_dir:
        path=os.path.join('../../test_cases/cases',i)
        if os.path.isfile(path):
            try:
                subprocess.run(['python', path])
            except subprocess.CalledProcessError as e:
                print(f'Error running {path}:{e}')
