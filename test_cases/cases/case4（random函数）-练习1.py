#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/7/12 9:04
=================================================='''
import random


def test1():
    a=random.random()
    print(a)
    b=random.randint(1,10)
    print(b)
    c=random.uniform(1,2)
    print(c)

    d=random.randrange(1,100,3)
    print(d)
    list1=[1,1,3,5,66]
    random.shuffle(list1)
    print(list1)
    print(random.choice(list1))
