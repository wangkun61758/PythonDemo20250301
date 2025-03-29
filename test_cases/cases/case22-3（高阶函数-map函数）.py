#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/7/8 22:49
=================================================='''
# 定义一个获取数字平方的函数
# def square(n):
#     return n * n
# # 一个数字列表
# numbers = [1, 2, 3, 4, 5]
# # 使用map函数
# a1 = map(square, numbers)
# # 因为map返回的是迭代器，所以我们可以用list将其转换为列表
# b1 = list(a1)
# print(b1)


numbers2 = [1, 2, 3, 4, 5]
# 直接在map中使用lambda表达式
a2 = list(map(lambda x: x * x, numbers2))
print(a2)
a3=  list(map(lambda x: x * x ,numbers2))
print(a3)

a4=list(map(lambda x: x * x ,numbers2))
print(a4)
a5=list(map(lambda x:x*x,numbers2))
print(a5)
a6=list(map(lambda x:x*x,numbers2))
print(a6)
a7=list(map(lambda x:x*x,numbers2))
print(a7)
'''
练习：2025/3/20（7）
'''
a8=list(map(lambda x:x*x,numbers2))
print(a8)
a9=list(map(lambda x:x*x,numbers2))
print(a9)
a10=list(map(lambda x:x*x,numbers2))
print(a10)