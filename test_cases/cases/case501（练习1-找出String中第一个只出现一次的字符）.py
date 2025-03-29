#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/2/6 13:02
=================================================='''
def test1():
    s ="abaccdeff"
    dits = dict()  # 创建一个字典
    for i in s:
        if i not in dits:
            dits[i] = True# 如果该元素第一次出现，则设对应布尔值为True
        else:
            dits[i] = False# 如果该元素重复出现，则对应布尔值为False
    print(dits)#{'a': False, 'b': True, 'c': False, 'd': True, 'e': True, 'f': False}
    # 此时已经将所有出现过的字母种类存入了字典，只出现过一次的对应True，重复过的对应False，那么只需要再次遍历字典找到第一个值为True的键
    for i in s:
        if dits[i]:# 如果值为True，则输出
            print(i)
            break
def test2():
    a='abaccdeff'
    dict1={}
    for i in a :
        if i not in dict1:
            dict1[i] = True
        else:
            dict1[i] = False
    for i in a:
        if dict1[i]:
            print(i)
            break
def test3():
    a='abaccdeff'
    dict1={}
    for i in a:
        if i not in dict1:
            dict1[i]=True
        else:
            dict1[i]=False
    for i in a:
        if dict1[i]:
            print(i)
            break
def test4():
    str1='abaccdeff'
    dict1={}
    for i in str1:
        if i not in dict1:
            dict1[i]=True
        else:
            dict1[i]=False
    for i in str1:
        if dict1[i]:
            print(i)
            break
def test5():
    str1 = 'abaccdeff'
    dict1 = {}
    for i in str1:
        if i not in dict1:
            dict1[i] = True
        else:
            dict1[i] = False
    for i in str1:
        if dict1[i]:
            print(i)
            break
def test6():
    str1='abaccdeff'
    dict={}
    for i in str1:
        if i not in dict:
            dict[i]=True
        else:
            dict[i]=False
    for i in str1:
        if dict[i]:
            print(i)
            break
