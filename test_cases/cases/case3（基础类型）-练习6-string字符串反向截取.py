#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/10/10 18:59
=================================================='''
import random
import string

def test():
    s = 'hello world'
    print(s[::-1])  # 按照从右到左，每次步长为1地截取（-1代表按步长1反向截取）

    '''
    [:]截取全部的字符
    [1：4]截取下标1到3的字符
    [1:16:-3]截取下标1到15的字符，按步长3截取，且是反向输出
    '''
    l = 'hello world'
    print(l[::1])  # 按照从左到右，每次步长为1地截取（1代表按步长1正向截取）
def test2():
    s = 'hello world'

    '''
    1、reversed(s) 是Python中内置的一个函数，作用是反转一个序列。它返回的是一个反向迭代器
    2、list(n)  将迭代器强制转换成list形式
    '''
    n = list(reversed(s))  # ['d', 'l', 'r', 'o', 'w', ' ', 'o', 'l', 'l', 'e', 'h']
    print(n)

    str = ""
    for i in n:  # 遍历list
        str = str + i
    print(str)  # dlrow olleh
def test3():
    s = 'hello world'
    '''
    1、reversed(s) 是Python中内置的一个函数，作用是反转一个序列。它返回的是一个反向迭代器
    2、.join()函数将反转后的字符序列拼接为一个字符串(此处拼接时，字符与字符之间不用隔开【因为需要用''之间的字符隔开，此处''之间没有任何字符】)
    '''
    n = reversed(s)
    print(''.join(n))  # dlrow olleh
def test4():
    s = 'hello world'
    print(s[::-1])  # dlrow olleh
def test5():
    s = 'hello world'
    print(''.join(reversed(s)))  # dlrow olleh
def test6():
    s = 'hello world'
    print(s[::-1])
def test7():
    s = 'hello world'
    print(''.join(reversed(s)))
def test8():
    s = 'hello world'
    li = list(s)
    print(li[::-1])  # ['d', 'l', 'r', 'o', 'w', ' ', 'o', 'l', 'l', 'e', 'h']
    str = ''
    for i in li:
        str = str + i
    print(str)
def test9():
    s = 'hello world'
    li = list(s)
    print(li[::-1])
    str = ''
    for i in li:
        str = str + i
    print(str)
def test10():
    s = 'hello world'
    tup = tuple(s)
    print(tup)
    str = ''
    for i in tup:
        str = str + i
    print(str)
def test11():
    li = ['d', 'l', 'r', 'o', 'w', ' ', 'o', 'l', 'l', 'e', 'h']
    str = ''
    for i in li:
        str = str + i
    print(str)  # dlrow olleh
def test12():
    num_phone=str(1)+''.join(random.choice("0123456789") for i in range(10))
    print(num_phone)

    str1=''.join(random.choice(string.ascii_letters+string.digits) for i in range(10))
    print(str1)


