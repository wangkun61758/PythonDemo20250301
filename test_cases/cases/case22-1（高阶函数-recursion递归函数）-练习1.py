#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/7/8 22:30
=================================================='''

def recursion1(n):
    if n == 1:
        return 1
    else:
        return n * recursion1(n - 1)

def test1():
    print(recursion1(5))


