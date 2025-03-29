#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/3/14 0:19
=================================================='''
def test1():
    nums = [1, 3, 5, 6]
    target =5.5
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2#1
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    print(left)
