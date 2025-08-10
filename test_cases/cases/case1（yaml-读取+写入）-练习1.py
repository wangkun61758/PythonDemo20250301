#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/11/4 13:30
=================================================='''

import os.path

import jsonpath
import yaml


def test1():
    file1=open('../../resources/parse_qs/parse_qs.yaml','r',encoding='utf-8')
    data1=yaml.load(file1,Loader=yaml.FullLoader)
    list1=[]
    list2=[]
    for k,v in data1.items():
        list1.append(k)
        list2.append(v)
    dict2={list1[i]:list2[i] for i in range(len(list2))}
    if not os.path.exists('../../resources/parse_qs8'):
        os.makedirs('../../resources/parse_qs8')
    with open('../../resources/parse_qs/parse_qs.yaml','w',encoding='utf-8') as file2:
        file2.write(str(dict2))
