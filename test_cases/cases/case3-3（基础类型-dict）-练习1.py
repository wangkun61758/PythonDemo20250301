#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/7/11 21:04
=================================================='''


def test1():
    dict1={'name':'lilei','age':15,'sex':'male'}
    print(dict1['name'])
    list1=[]
    list2=[]
    for k,v in dict1.items():
        list1.append(k)
        list2.append(v)
    dict2=dict({list1[i]:list2[i] for i in range(len(list1))})
    print(dict2)

    dict2['car']='特斯拉'
    print(dict2)
    dict2.pop('car')
    print(dict2)
    dict2.popitem()
    print(dict2)
