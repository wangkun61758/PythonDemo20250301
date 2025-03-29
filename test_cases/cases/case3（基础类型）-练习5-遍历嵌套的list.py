#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/11/30 19:51
=================================================='''


def test1():
    list1 = ['12345678', ['bbb', 'ccc', 'ddd', 'eee'], '567', '890', '156']
    for i in range(0, len(list1)):
        for j in range(0, len(list1[i])):
            # a = 1
            if isinstance(list1[i], str):
                # if a < 2:
                print(list1[i])
                # a = a + 1
                break
            else:
                print(list1[i][j])
