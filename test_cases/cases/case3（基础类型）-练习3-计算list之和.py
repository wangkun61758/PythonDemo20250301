#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/7/11 21:04
=================================================='''


def test():
    list = [15, 8, 27, 988, 176, 28]

    total = 0
    for i in range(0, len(list)):
        total = total + list[i]
    print(total)
