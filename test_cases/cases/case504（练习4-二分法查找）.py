#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/11/4 14:57
=================================================='''


# 二分法
# list=[-3,4,7,10,13,21,43,77,89]#列表事先已经按照从小到达的顺序排列
def search1(target, list):
    while True:
        mid_index = len(list) // 2  # 取整除 - 往小的方向取整数
        print('取整除 - 往小的方向取整数：', str(mid_index))
        mid_val = list[mid_index]
        print('list中间的一个值是：' + str(mid_val))

        if target > mid_val:  # 说明序号在列表的右半部分去找
            list = list[mid_index + 1:]  # 列表=列表切片
            print('列表切片1' + str(list))  # 列表切片[21, 43, 77, 89]

        elif target < mid_val:
            list = list[:mid_index]
            print('列表切片2' + str(list))  # [21, 43]

        else:
            print('find it:' + str(mid_val))  # 第3次查找：find it:43
            break
search1(43, [-3, 4, 7, 10, 13, 21, 43, 77, 89])

def search2(target, list):
    while True:
        print(list)  # 第1次查找：[-3, 4, 7, 10, 13, 21, 43, 77, 89]/ 第2次查找：[21, 43, 77, 89]/第3次查找：[21, 43]
        mid_index = len(list) // 2  # 取整除 - 往小的方向取整数
        print(mid_index)  # 第2次查找：4/第3次查找：2/第3次查找：1

        mid_val = list[mid_index]
        print(mid_val)  # 第1次查找：13/第2次查找：77/第3次查找：43

        if target > mid_val:  # 说明序号在列表的右半部分去找
            list = list[mid_index + 1:]  # 列表=列表切片
            print(list)  # 第1次查找：[21, 43, 77, 89]
        elif target < mid_val:
            list = list[:mid_index]
            print(list)  # 第2次查找：[21, 43]
        else:
            print('find it:' + str(mid_val))  # 第3次查找：find it:43
            break
search2(43, [-3, 4, 7, 10, 13, 21, 43, 77, 89])

def search3(target, list):
    while True:
        mid_index = len(list) // 2  # 取整除 - 往小的方向取整数
        mid_val = list[mid_index]
        if target > mid_val:  # 说明序号在列表的右半部分去找
            list = list[mid_index + 1:]  # 列表=列表切片
        elif target < mid_val:
            list = list[:mid_index]
        else:
            print('find it:' + str(mid_val))  # 第3次查找：find it:43
            break
search3(43, [-3, 4, 7, 10, 13, 21, 43, 77, 89])

def search4(target, list):
    while True:
        mid_index = len(list) // 2
        mid_val = list[mid_index]
        if target > mid_val: list = list[mid_index + 1:]
        elif target < mid_val:
            list=list[:mid_index]
        else:
            print('find it:' + str(mid_val))
            break
search4(43, [-3, 4, 7, 10, 13, 21, 43, 77, 89])