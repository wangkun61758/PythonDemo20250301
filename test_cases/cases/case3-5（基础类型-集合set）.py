#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/3/12 23:30
=================================================='''
import numpy as np
import pandas as pd


def test1():
    list1 = [100, 4, 200, 1, 3, 2, 5, 5, 2, 1]
    set1 = set(list1)
    set1.add(111)
    a1 = set1.copy()  # {1, 2, 3, 100, 4, 5, 200, 111}
    print(2 in set1)  # True
    set1.discard(2)  # 移除(返回移除后的)# {1, 3, 100, 4, 5, 200, 111}
    set1.discard(3)  # 移除(返回移除后的)# {1, 100, 4, 5, 200, 111}
    ###################################################################
    s1 = {1, 2, 3}
    s2 = {3, 4, 5}
    a4 = s1.pop()  # 弹出并返回集合s1中的任意元素  # 1
    s1.remove(3)  # 从集合s中移除元素2，如果不存在则引发错误  # {2}

    diff1 = s1.difference(s2)  # 返回s1中存在但s2中不存在的元素
    print(diff1)  # {1, 2}

    s1.difference_update(s2)  # 从s1中移除s2中存在的元素
    print(s1)  # {1, 2}

    diff3 = s2.intersection(s2)  # 返回同时存在于s1和s2中的元素  # {3, 4, 5}
    print(diff3)  # {3, 4, 5}
    s1.intersection_update(s2)  # 保留同时存在于s1和s2中的元素到s1中  # set()

    s1.update(s2)  # 将s2中的元素添加到s1中  # {3, 4, 5}

    a1 = s1.isdisjoint(s2)  # 如果s1和s2没有共同元素则返回True
    print(a1)  # True

    a2 = s1.issubset(s2)  # 如果s1是s2的子集则返回True
    a3 = s1.issuperset(s2)  # 如果s1包含s2则返回True
    print(a2)  # True
    print(a3)  # False

    set1.clear()

def test2():
    list1 = [100, 4, 200, 1, 3, 2, 5, 5, 2, 1]
    set1 = set(list1)
    set1.add(111)
    a1 = set1.copy()
    print(a1)  # {1, 2, 3, 100, 4, 5, 200, 111}
    print(2 in set1)  # True
    set1.discard(2)  # 移除(返回移除后的)
    print(set1)  # {1, 3, 100, 4, 5, 200, 111}
    set1.discard(3)
    print(set1)  # {1, 100, 4, 5, 200, 111}
    ###################################################################
    s1 = {1, 2, 3}
    s2 = {3, 4, 5}

    a4 = s1.pop()  # 弹出并返回集合s1中的任意元素
    print(a4)  # 1
    s1.remove(3)  # 从集合s中移除元素2，如果不存在则引发错误
    print(s1)  # {2}

    diff1 = s1.difference(s2)  # 返回s1中存在但s2中不存在的元素
    print(diff1)  # {1, 2}

    s1.difference_update(s2)  # 从s1中移除s2中存在的元素
    print(s1)  # {1, 2}

    diff3 = s2.intersection(s2)  # 返回同时存在于s1和s2中的元素
    print(diff3)  # {3, 4, 5}
    s1.intersection_update(s2)  # 保留同时存在于s1和s2中的元素到s1中
    print(s1)  # set()

    s1.update(s2)  # 将s2中的元素添加到s1中
    print(s1)  # {3, 4, 5}

    a1 = s1.isdisjoint(s2)  # 如果s1和s2没有共同元素则返回True
    print(a1)  # True

    a2 = s1.issubset(s2)  # 如果s1是s2的子集则返回True
    a3 = s1.issuperset(s2)  # 如果s1包含s2则返回True
    print(a2)  # True
    print(a3)  # False

    set1.clear()
'''
练习：2025/3/20（1）
'''
def test3():
    list1 = [100, 4, 200, 1, 3, 2, 5, 5, 2, 1]
    set1 = set(list1)
    set1.add(111)
    print(2 in set1)  # True
    set1.discard(2)  # 移除(返回移除后的)# {1, 3, 100, 4, 5, 200, 111}
    print(set1)
    set1.discard(3)  # 移除(返回移除后的)# {1, 100, 4, 5, 200, 111}
    print(set1)
    set2=set1.copy()
    print(set2)
