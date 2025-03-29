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
    sum1=sum(score for score in scores if score>50)#求和
    print(sum1)

    print(sum(range(1,101)))
    print(sum(range(1,101),10))
    print(sum([1,2,3,4,5]))

def test2():
    sum = 0
    for i in range(1, 101):
        sum = sum + i
    print(sum)

def test3():
    print(sum(range(1, 101)))  # 5050
    print(sum(range(1, 101), 10))  # 5060
    print(sum([1, 2, 3, 4, 5]))
    print(sum((1, 2, 3, 4, 5)))
    print(sum({1, 2, 3, 4, 5}))

# sum()函数可以与列表推导式结合使用，以实现更复杂的求和操作
def test4():
    list1 = [1, 2, 3, 4, 5, 6]
    sum1 = sum(i for i in list1 if i % 2 == 0)
    print(sum1)  # 2

# 计算特定条件下的元素总和
def test5():
    scores = [55, 90, 75, 43, 80, 65, 50]
    scores.sort()
    print(scores)  # [43, 50, 55, 65, 75, 80, 90]
    passing_scores_sum = sum(score for score in scores if score >= 60)
    print(passing_scores_sum)  # 输出：310

def test6():
    print(sum(range(1,101)))#5050
    print(sum(range(1,101),10))#5060
    print(sum([1,2,3,4,5]))#15
    print(sum((1,2,3,4,5)))#15
    print(sum({1,2,3,4,5}))#15

    list1 = [1, 2, 3, 4, 5, 6]
    print(sum(i for i in list1 if i%2==0))#12
    print(sum(i for i in list1 if i>4))#11

def test7():
    print(sum(range(1,101)))
    print(sum(range(1,101),10))
    print(sum([1,2,3,4,5]))
    print(sum((1,2,3,4,5)))
    print(sum({1,2,3,4,5}))
    list1 = [1, 2, 3, 4, 5, 6]
    print(sum(i for i in  list1 if i%2==0))
    print(sum(i for i in list1 if i>5))
'''
练习：2025/3/20（1）
'''
def test8():
    print(sum(range(1,101)))
    print(sum(range(1,101),10))
    print(sum([1,2,3,4,5]))
    print(sum((1,2,3,4,5)))
    print(sum({1,2,3,4,5}))
    list1 = [1, 2, 3, 4, 5, 6]
    print(sum(i for i in list1 if i%2==0))
def test9():
    print(sum(range(1,101)))
    print(sum(range(1,101),10))
    print(sum([1,2,3,4,5]))
    list1 = [1, 2, 3, 4, 5, 6]
    print(sum(i for i in list1 if i%2==0))
