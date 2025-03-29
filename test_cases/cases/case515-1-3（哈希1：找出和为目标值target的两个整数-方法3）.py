#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/3/11 0:58
=================================================='''

class Solution1(object):
    def test1(self, nums, target):
        # 遍历列表
        for i in range(len(nums)):
            # 计算需要找到的下一个目标数字
            n = target-nums[i]
                # 在剩下的元素，查找是否存在该数字
            if n in nums[i+1:]:
                # 若存在，返回答案。这里由于是两数之和，可采用.index()方法
                # 获得目标元素在nums[i+1:]这个子数组中的索引后，还需加上i+1才是该元素在nums中的索引
                res = [i, (nums[i+1:].index(n))+(i+1)]
                print(res)

slo1=Solution1()
slo1.test1([2,7,11,15],9)