#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/3/12 22:21
=================================================='''
'''
【遍历到的值】：1
【i - 1后的值】：0
【i+k的值】：2
【i+k的值】：3
【内部的len】3

【遍历到的值】：2
【遍历到的值】：3

【遍历到的值】：100
【i - 1后的值】：99
【内部的len】3

【遍历到的值】：5
【i - 1后的值】：4
【内部的len】3
'''


def test1():
    nums = [100, 1, 3, 2, 5, 101, 102, 103, 104, 105, 106, 107]
    set1 = set(nums)  # {1, 2, 3, 100, 5}
    print(set1)

    len = 0
    for i in set1:
        if i - 1 not in set1:  # 前一个值不在里边
            k = 1
            while i + k in set1:  # 后一个值在里边(不断循环计算 101+k 后的值是否在set中)
                k += 1
            len = max(len, k)
    print(len)

    # for i in set1:
    #     print('【遍历到的值】：' + str(i))
    #     if i - 1 not in set1:
    #         print('【i - 1后的值】：' + str(i - 1))
    #         k = 1
    #         while i + k in set1:
    #             print('【i+k的值】：' + str(i + k))
    #             k += 1
    #         len = max(len, k)
    #         print('【内部的len】' + str(len))
    # print(len)


'''
【遍历到的值】：0
【i - 1后的值】：-1
【i + k的值】：1
【i + k的值】：2
【i + k的值】：3
【i + k的值】：4
【i + k的值】：5
【i + k的值】：6
【i + k的值】：7
【i + k的值】：8
【内部的len】9

【遍历到的值】：1
【遍历到的值】：2
【遍历到的值】：3
【遍历到的值】：4
【遍历到的值】：5
【遍历到的值】：6
【遍历到的值】：7
【遍历到的值】：8
'''


def test2():
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    set1 = set(nums)  # {1, 2, 3, 100, 4, 5, 200}
    print(set1)

    len = 0
    for i in set1:
        print('【遍历到的值】：' + str(i))
        if i - 1 not in set1:
            print('【i - 1后的值】：' + str(i - 1))
            k = 1
            while i + k in set1:
                print('【i + k的值】：' + str(i + k))
                k += 1
            len = max(len, k)
            print('【内部的len】' + str(len))
    print(len)

def test3():
    nums = [100, 1, 3, 2, 5, 101, 102, 103, 104, 105, 106, 107]
    set1 = set(nums)
    print(set1)
    len=0
    for i in set1:
        if i-1 not in set1:
            k=1
            while i+k in set1:
                k=k+1
            len=max(len,k)
    print(len)

def test4():
    nums = [100, 1, 3, 2, 5, 101, 102, 103, 104, 105, 106, 107]
    set1=set(nums)
    len=0
    for i in set1:
        if i-1 not in set1:
            k=1
            while i+k in set1:
                k=k+1
            len=max(len,k)
    print(len)