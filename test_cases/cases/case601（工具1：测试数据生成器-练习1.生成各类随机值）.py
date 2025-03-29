#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/3/21 20:00
=================================================='''
import random
import string

"""生成随机字符串"""
def test1():
    # print(string.ascii_letters)#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    # print(string.digits)#0123456789
    chars = string.ascii_letters + string.digits
    # print(chars)#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
    # print('' + ''.join(random.choice(chars) for _ in range(8)) + '')#sOwwfdso
    print(''.join(random.choice(chars) for _ in range(8)))  # sOwwfdso
    # print(random.choice(chars) )#b

"""生成随机浮点数"""
def test1():
    print(random.uniform(0, 100))#61.33547723612565
    print((random.uniform(0, 100), 2))#(81.57979868083513, 2)

"""生成随机字符串"""
def test2():
    chars = string.ascii_letters + string.digits
    print(string.ascii_letters)#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    print(chars)#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
    print(''.join(random.choice(chars) for _ in range(8)) )
    return ''.join(random.choice(chars) for _ in range(8)) # _是一个常见的占位符