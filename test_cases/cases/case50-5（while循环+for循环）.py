#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/7/4 22:17
=================================================='''


def test1():
    a = 1
    while a < 100:
        if (a % 2 == 0):
            print('第' + str(a) + '次' + '不能整除2')
        else:
            print('第' + str(a) + '次' + '可以整除2')
        a = a + 1
test1()

def test2():
    list = [13, 3, 99, 78, 17, 66, 18]
    for i in list:
        print(i)
test2()


def test3():
    list = []
    for i in range(1, 100):
        list.append(i)
    print(list)
test3()


def test4():
    list = []
    for i in range(1, 100, 6):
        list.append(i)
    print(list)
test4()

def test5():
    for _ in range(1, 100, 6):
        print(_)