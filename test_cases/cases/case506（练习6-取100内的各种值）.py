#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2024/2/20 21:43
=================================================='''
'''
打印100以内包含7和可以整除7的数字
'''


def test1():
    list1 = []
    for i in range(1, 101):
        if i % 7 == 0 or '7' in str(i):
            print(i)
            list1.append(i)
    print(list1)
    # list1=[]
    # for i in range(1, 101):
    #     if i%7==0 or '7' in str(i):
    #         print(i)
    #         list1.append(i)


'''
打印100以内的质数
'''


def test2():
    list1 = []
    for i in range(2, 100):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            # print(i)
            list1.append(i)
    print(list1)

def test3():
    list1 = []
    for i in range(2, 100):
        for j in range(2, i):
            if i % j == 0:
                break
            else:
                list1.append(i)