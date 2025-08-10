#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/7/11 21:07
=================================================='''
import numpy as np


def test1():
    arr1=np.array([1,2,3,4,5])
    arr2=np.append(arr1,111)
    print(arr2)
    arr3=np.insert(arr2,2,222)
    print(arr3)

    arr4=np.delete(arr3,2)
    print(arr4)