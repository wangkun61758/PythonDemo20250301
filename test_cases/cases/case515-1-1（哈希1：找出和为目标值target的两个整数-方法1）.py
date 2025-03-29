#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/3/11 0:58
=================================================='''

# nums = [2, 7, 11, 15]
# target = 9
#
# n = len(nums)
# for i in range(n):
#     for j in range(i + 1, n):
#         if nums[i] + nums[j] == target:
#             print([i, j])


class Solution1(object):
    def test1(self, nums, target):
        list1 = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    list1.append(i)
                    list1.append(j)
        print(list1)
        return list1


slo=Solution1()
slo.test1([2,7,11,15],9)

class Solution2(object):
    def test2(self,nums,target):
        list2=[]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i]+nums[j]==target:
                    list2.append(i)
                    list2.append(j)
        print(list2)
slo2=Solution2()
slo2.test2(nums=[2,7,11,15],target=9)

class Solution3(object):
    def test3(self,nums,target):
        list3=[]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i]+nums[j]==target:
                    list3.append(i)
                    list3.append(j)
        print(list3)

slo3=Solution3()
slo3.test3([2,7,11,15],9)

def test1():
    nums=[2,7,11,15]
    target=9
    list1=[]
    for i in range(0,len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j]==target:
                list1.append(i)
                list1.append(j)
    print(list1)
