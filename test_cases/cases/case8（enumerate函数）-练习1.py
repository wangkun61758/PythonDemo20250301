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
                print([dict[target - num], index])  # 键2对应的值是0（前面遍历list时，存在“dict = {}”中的值dict={2:0}）
            else:
                dict[num] = index  # {2: 0}
                # print('打印：' + str(dict))


slo1 = Solution1()
slo1.test1([2, 7, 11, 15], 9)

