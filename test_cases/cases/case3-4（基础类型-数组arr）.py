#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/7/11 21:07
=================================================='''
import numpy as np


def test1():
    arr = np.array([56, 25, 21, 12, 3, 4, 25])  # 创建数组
    print(type(arr))  # <class 'numpy.ndarray'>
    print(arr[1])  # 25

    # 1、添加新元素，参数是值
    new_arr = np.append(arr, 1000)
    print(new_arr)  # [  56   25   21   12    3    4   25 1000]

    # 2、删除指定位置的元素，参数是下标
    new_arrs = np.delete(new_arr, 1)
    print(new_arrs)  # [  56   21   12    3    4   25 1000]
