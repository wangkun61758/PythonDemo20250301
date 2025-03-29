#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/2/6 12:37
=================================================='''

def intersect1(nums1, nums2):
    # 排序是基础
    nums1.sort()
    nums2.sort()

    # res = list()#使用list()函数
    lists = []
    index1 = 0
    index2 = 0

    while index1 < len(nums1) and index2 < len(nums2):

        if nums1[index1] > nums2[index2]:  # [1, 1, 2, 2, 3] 和 [2, 2, 5]
            index2 += 1
        elif nums1[index1] < nums2[index2]:
            index1 += 1
        else:
            lists.append(nums1[index1])
            index1 += 1
            index2 += 1

    print(lists)
    return lists
intersect1(nums1=[1, 2, 2, 1, 3], nums2=[2, 2, 5])

def intersect2(nums1, nums2):
    nums1.sort()
    nums2.sort()
    list1 = []
    index1 = 0
    index2 = 0
    while index1 < len(nums1) and index2 < len(nums2):
        if nums1[index1] > nums2[index2]:
            index2 += 1
        elif nums1[index1] < nums2[index2]:
            index1 += 1
        else:
            list1.append(nums1[index1])
            index1 += 1
            index2 += 1
    print(list1)
intersect2(nums1=[1, 2, 2, 1, 3], nums2=[2, 2, 5])

def intersect3(nums1, nums2):
    nums1.sort()
    nums2.sort()
    list1 = []
    index1 = 0
    index2 = 0
    while index1 < len(nums1) and index2 < len(nums2):
        if nums1[index1] > nums2[index2]: index2 += 1
        elif nums1[index1] < nums2[index2]:index1 += 1
        else:
            list1.append(nums1[index1])
            index1 += 1
            index2 += 1
    print(list1)
intersect3(nums1=[1, 2, 2, 1, 3], nums2=[2, 2, 5])

def intersect4(nums1, nums2):
    nums1.sort()
    nums2.sort()
    list1 = []
    index1 = 0
    index2 = 0
    while index1 < len(nums1) and index2 < len(nums2):
        if nums1[index1] > nums2[index2]:
            index2 += 1
        elif nums1[index1] < nums2[index2]:
            index1 += 1
        else:
            list1.append(nums1[index1])
            index1 += 1
            index2 += 1
    print(list1)
intersect4(nums1=[1, 2, 2, 1, 3], nums2=[2, 2, 5])