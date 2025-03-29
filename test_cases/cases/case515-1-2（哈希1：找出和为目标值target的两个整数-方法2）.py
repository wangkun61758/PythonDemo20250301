#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/3/11 0:58
=================================================='''

class Solution1(object):
    def test1(self, nums, target):
        dict = {}
        for index, num in enumerate(nums):
            if target - num in dict:
                print([dict[target - num], index])#此前dict={2:0} , 打印["dict[2]对应的值0",1]，结果：[0,1]
            else:
                dict[num] = index#{2: 0}
                print('打印：' + str(dict))
slo1=Solution1()
slo1.test1([2,7,11,15],9)

class Solution2(object):
    def test2(self, nums, target):
        dict = {}
        for index, num in enumerate(nums):
            if target - num in dict:
                print([dict[target - num], index])
            else:
                dict[num] = index
slo2=Solution2()
slo2.test2([2,7,11,15],9)

class Solution3(object):
    def test3(self, nums, target):
        dict = {}
        for index,num in enumerate(nums):
            if target-num in dict:
                print(dict[target - num], index)
            else:
                dict[num]=index
slo3=Solution3()
slo3.test3([2,7,11,15],9)

class Solution4(object):
    def test4(self,nums,target):
        dict4={}
        for index,num in enumerate(nums):
            if target-num in dict4:
                print([dict4[target-num], index])
            else:dict4[num]=index
slo4=Solution4()
slo4.test4([2,7,11,15],9)