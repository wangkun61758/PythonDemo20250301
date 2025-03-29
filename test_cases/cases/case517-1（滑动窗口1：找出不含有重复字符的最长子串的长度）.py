#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/3/13 23:13
=================================================='''

'''
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''
def test1():
    str1="pwwkew"
    left, right = 0, 0
    res = 0

    while right < len(str1):
        if str1[right] not in str1[left:right]:
            right += 1
            res = max(res, len(str1[left:right]))
        else:
            while str1[right] in str1[left:right]:
                left += 1
    print(res)