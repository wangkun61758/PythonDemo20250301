#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/3/13 22:43
=================================================='''
'''
方法1
'''
def test1():
    nums = [0, 1, 0, 3, 12]
    list1=[]
    list2=[]
    for i in nums:
        if i == 0:
            list1.append(i)
        else:
            list2.append(i)
        list3=list2+list1
    print(list3)
'''
方法2
'''
def test2():
    nums = [0, 1, 0, 3, 12]
    n = len(nums)
    print(n)
    left = right = 0
    while right < n:
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1
    print(nums)

def test3():
    nums = [0, 1, 0, 3, 12]
    n = len(nums)
    right=0
    left=0
    while right < n:
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        else:
            right+=1
    print(nums)