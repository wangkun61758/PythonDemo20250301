#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/7/8 22:30
=================================================='''


# # 递归函数方式
# def recursion1(n):
#     if n == 1:  # 正确的返回添加（结束条件）
#         return 1
#     else:
#         return n * recursion1(n - 1)  # 调用自身函数的行为
#
#
# a = int(input("请输入："))
# b = recursion1(a)
# print(b)
#
# def recursion2(n):
#     if n==1:return 1
#     else:return n*recursion2(n-1)
# a=int(input())
# b=recursion2(a)
# print(b)
def recursion1(n):
    if n==1: return 1
    else:return n*recursion1(n-1)
def test1():
    print(recursion1(5))

def recursion2(n):
    if n==1:return 1
    else:return n*recursion2(n-1)
def test2():
    print(recursion2(5))

def recursion3(n):
    if n==1:return 1
    else:return n*recursion3(n-1)
def test3():
    print(recursion3(5))

def recursion4(n):
    if n==1:return 1
    else:return n*recursion4(n-1)
def test4():
    print(recursion4(5))

def recursion5(n):
    if n==1:return 1
    else:return n*recursion5(n-1)
def test5():
    print(recursion5(5))

def recursion6(n):
    if n==1:return 1
    else:return n*recursion6(n-1)
def test6():
    print(recursion6(5))
'''
练习：2025/3/20（7）
'''
def recursion7(n):
    if n==1:return 1
    else:return n*recursion7(n-1)
def test7():
    print(recursion7(5))