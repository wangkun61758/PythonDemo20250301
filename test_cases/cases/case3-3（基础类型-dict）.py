#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/2/13 0:21
=================================================='''


def test1():
    dict1 = {'Name': '王五', 'Age': 7, 'Class': '一年级'}
    print(dict1['Name'])

    for i in dict1:  # 遍历key值
        print(i)
    for j in dict1.keys():  # 遍历key值
        print(j)
    for k in dict1.values():
        print(k)
    list1 = []
    list2 = []
    for key, value in dict1.items():  # 遍历字典
        list1.append(key)
        list2.append(value)
    dict_list1 = dict({list1[i]: list2[i] for i in range(len(list1))})
    print('列表转字典：' + str(dict_list1))  # {'Name': '王五', 'Age': 7, 'Class': '一年级'}

    print('删除字典 key（键）所对应的值，返回被删除的值:' + str(dict1.pop("Age")))  # 删除字典 key（键）所对应的值，返回被删除的值:7
    print(dict1.popitem())  # 用于返回并删除字典中的一个键值对，一般删除字典末尾的键值对

    dict2 = {}  # 创建一个空字典
    # dict2=dict()#创建一个空字典
    print(dict2)  # {}
    dict2['喜好'] = '摄影'  # 增加元素‌：可以通过键来为字典添加新的键值对
    print(dict2)  # {'喜好': '摄影'}
    dict3 = {'喜好': '摄影'}
    del (dict3['喜好'])  # 删除键值对
    print(dict3)  # {}
