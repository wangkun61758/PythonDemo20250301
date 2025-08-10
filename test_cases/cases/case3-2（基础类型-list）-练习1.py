#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/7/11 21:04
=================================================='''
def test1():
    list1 = [1, 2, 3]
    list1.append(11)
    list1.insert(1, 12)
    list1.sort()
    print(list1)
    list1.reverse()
    print(list1)
    list1.sort(key=lambda x: abs(x))
    print(list1)
    list1.pop()
    print(list1)
    list1.remove(1)
    print(list1)
    print(list1[1:3])
    list1.extend('你好啊')
    print(list1)
