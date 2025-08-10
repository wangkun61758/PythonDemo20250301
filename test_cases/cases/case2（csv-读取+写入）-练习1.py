#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/3/19 18:03
=================================================='''
import csv
import os.path


def test1():
    list=[]
    with open('../../resources/file1.csv','r',encoding='gbk') as file1:
        reader=csv.reader(file1)
        for row in reader:
            list.append(row)
    dict2=["李白", "杜甫", "白居易", "王维"]
    if not os.path.exists('../../resources/csv'):
        os.makedirs('../../resources/csv')
    with open('../../resources/csv/file1.csv','w',encoding='gbk') as file2:
        writer=csv.writer(file2)
        writer.writerow(dict2)