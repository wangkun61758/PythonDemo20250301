#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/2/17 22:52
=================================================='''
'''
sum()函数是一个内置的数学函数，用于计算可迭代对象（如列表或元组）中所有元素的总和
sum()函数可以接受两个参数：iterable和start。
iterable：这是一个必须参数，你可以传入任何可迭代的对象，如列表、元组或生成器。
start：这是一个可选参数，用于给定一个初始累加值。如果你的计算需要一个不同于0的起始值，这个参数将非常有用。
:return:
'''


def test1():
    scores = [55, 90, 75, 43, 80, 65, 50]
    scores.sort()
    sum1 = sum(score for score in scores if score > 50)  # 求和
    print(sum1)

    print(sum(range(1, 101)))
    print(sum(range(1, 101), 10))
    print(sum([1, 2, 3, 4, 5]))

