#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/3/14 0:02
=================================================='''
def test1():
    nums = [1,2,3]
    k = 3
    total = 0
    res = 0
    count = {}
    for num in nums:
        total += num
        if total == k:
            res += 1
        if total - k in count:
            res += count[total - k]
        count[total] = count.get(total, 0) + 1
    print(res)