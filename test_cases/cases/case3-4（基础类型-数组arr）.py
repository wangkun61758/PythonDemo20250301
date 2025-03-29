#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/7/11 21:07
=================================================='''
import numpy as np


def test1():
    arr = np.array([56, 25, 21, 12, 3, 4, 25])#创建数组
    print(type(arr))#<class 'numpy.ndarray'>
    print(arr[1])#25

    # 1、添加新元素，参数是值
    new_arr = np.append(arr, 1000)
    print(new_arr)  # [  56   25   21   12    3    4   25 1000]

    # 2、删除指定位置的元素，参数是下标
    new_arrs = np.delete(new_arr, 1)
    print(new_arrs)  # [  56   21   12    3    4   25 1000]

def test2():
    list = [56, 25, 21, 12, 3, 4, 25]
    print(type(list))
    print(list)  # [56, 25, 21, 12, 3, 4, 25]
def test3():
    arr=np.array([56, 25, 21, 12, 3, 4, 25])#创建数组
    print(np.append(arr,111))#[ 56  25  21  12   3   4  25 111]
    print(np.delete(arr,1))#[56 21 12  3  4 25]
def test4():
    arr=np.array([56, 25, 21, 12, 3, 4, 25])
    new_arr1=np.append(arr,111)
    print(new_arr1)#[ 56  25  21  12   3   4  25 111]
    new_arr2=np.delete(arr,0)
    print(new_arr2)#[25 21 12  3  4 25]
def test5():
    arr=np.array([56, 25, 21, 12, 3, 4, 25])
    new_arr1=np.append(arr,111)
    new_arr2=np.delete(new_arr1,0)
def test6():
    arr=np.array([56, 25, 21, 12, 3, 4, 25])
    new_arr1=np.append(arr,111)
    new_arr2=np.delete(new_arr1,1)
def test7():
    arr=np.array([13,2,56,37,12])
    new_arr=np.append(arr,111)
    print(new_arr)
    new_arr=np.delete(new_arr,0)
    print(new_arr)
'''
练习：2025/3/20（1）
'''
def test8():
    arr1=np.array([56, 25, 21, 12, 3, 4, 25])
    arr2=np.append(arr1,111)
    arr3=np.delete(arr2,1)

    arr4=np.array([56, 25, 21, 12, 3, 4, 25])
    arr5=np.append(arr4,111)
    arr6=np.delete(arr5,0)

    arr7=np.array([1,2,3,4,5])
    arr8=np.delete(arr7,0)
    arr9=np.append(arr8,111)

    a10=np.array([1,2,3,4,5])
    a11=np.append(a10,111)
    a12=np.delete(a11,0)

    arr13=np.array([56, 25, 21, 12, 3, 4, 25])
    arr14=np.append(arr13,111)
    arr15=np.delete(arr14,0)

    arr16=np.array([56, 25, 21, 12, 3, 4, 25])
    arr17=np.append(arr16,111)
    arr18=np.delete(arr17,0)

    arr19=np.array([56, 25, 21, 12, 3, 4, 25])
    arr20=np.append(arr19,111)
    arr21=np.delete(arr20,0)

    arr22=np.array([56, 25, 21, 12, 3, 4, 25])
    arr23=np.delete(arr22,0)
    arr24=np.append(arr23,111)
def test9():
    arr1=np.array([56, 25, 21, 12, 3, 4, 25])
    arr2=np.append(arr1,111)
    arr3=np.delete(arr2,0)




