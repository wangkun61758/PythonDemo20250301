#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/3/11 1:30
=================================================='''
'''
for index, num in enumerate(nums):
将一个可遍历的数据对象（如列表、元组、字典和字符串）组合成一个索引序列，同时列出数据下标和数据（索引 值），一般配合for循环使用
'''
class Solution1(object):
    def test1(self, nums, target):
        dict = {}
        for index, num in enumerate(nums):
            if target - num in dict:
                print([dict[target - num], index])#键2对应的值是0（前面遍历list时，存在“dict = {}”中的值dict={2:0}）
            else:
                dict[num] = index#{2: 0}
                # print('打印：' + str(dict))
slo1=Solution1()
slo1.test1([2,7,11,15],9)

class Solution2(object):
    def test2(self, nums, target):
        dict2={}
        for index, num in enumerate(nums):
            if target-num in dict2:
                print([dict2[target-num], index])
            else:
                dict2[num] = index
slo2=Solution2()
slo2.test2([2,7,11,15],9)

class Solution3(object):
    def test3(self,nums,target):
        dict3={}
        for index,num in  enumerate(nums):
           if target-num in dict3:
               print([dict3[target-num],index])
           else: dict3[num]=index
s3=Solution3()
s3.test3([2,7,11,15],9)

class Solution4(object):
    def test4(self,nums,target):
        dict4={}
        for index,num in enumerate(nums):
            if target-num in dict4:
                print([dict4[target-num],index])
            else:
                dict4[num]=index
s4=Solution4()
s4.test4([2,7,11,15],9)

class Solution5(object):
    def test5(self,nums,target):
        dict5={}
        for index,num in enumerate(nums):
            if target-num in dict5:
                print([dict5[target-num],index])
            else:
                dict5[num]=index
s5=Solution5()
s5.test5([2,7,11,15],9)
'''
练习：2025/3/20（3）
'''
class Solution6(object):
    def test6(self,nums,target):
        dict6={}
        for index,num in enumerate(nums):
            if target-num in dict6:
                print([dict6[target-num],index])
            else:
                dict6[num]=index
s6=Solution6()
s6.test6([2,7,11,15],9)