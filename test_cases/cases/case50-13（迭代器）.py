#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/7/5 8:18
=================================================='''


def test():
    # 遍历方法
    list = [12, 88, 5, 19, 339, 56]
    # it = iter(list)

    for i in list:
        print(i, end=',')#12,88,5,19,339,56,
    print('\n')

    # 打印下一个
    tup = ('下一个', 99, '函数', 76, 156)
    it = iter(tup)
    print(next(it))

def test2():
    tup1 = ('下一个', 99, '函数', 76, 156)
    it1 = iter(tup1)
    print(next(it1))
