#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/2/14 23:46
=================================================='''
def test1():  # 冒泡排序
    list1 = [11, 45, 2, 68, 99]
    n = len(list1)
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if list1[j] > list1[j + 1]:
                # 第1轮比较 j 0~4:[11, 45, 2, 68, 99] [11, 2, 45, 68, 99] [11, 2, 45, 68, 99] [11, 2, 45, 68, 99]
                # 第2轮比较 j 0~3:[11, 45, 2, 68, 99] [11, 2, 45, 68, 99] [11, 2, 45, 68, 99]
                # 第3轮比较 j 0~2:[2, 11, 45, 68, 99] [2, 11, 45, 68, 99]
                # 第4轮比较 j 0~1:[2, 11, 45, 68, 99]
                list1[j], list1[j + 1] = list1[j + 1], list1[j]  # 交换位置
                # list1[j + 1] = list1[j]
                # list1[j] = list1[j + 1]

    print(list1)#[2, 11, 45, 68, 99]

def test2():
    list1 = [11, 45, 2, 68, 99]
    print(sorted(list1))#[2, 11, 45, 68, 99]

    for i in range(0, len(list1)):
        for j in range(0, len(list1) - i - 1):
            if list1[j] > list1[j + 1]:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
    print(list1)
