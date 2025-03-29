#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/7/8 22:30
=================================================='''
# 递归函数方式
def recursion1(n):
    if n == 1:  return 1
    else:return n * recursion1(n - 1)  # 调用自身函数的行为
a = int(input("请输入："))
b = recursion1(a)

'''
练习：2025/3/20（1）
'''
def recursion2(n):
    if n == 1: return 1
    else:return n*recursion2(n-1)
a=int(input('输入'))
b=recursion2(a)

def recursion3(n):
    if n==1:return 1
    else:return n*recursion3(n-1)
a=int(input('输入'))
b=recursion3(a)
