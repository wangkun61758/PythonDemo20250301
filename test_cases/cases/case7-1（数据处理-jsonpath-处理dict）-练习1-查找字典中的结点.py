#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/11/4 14:40
=================================================='''
import jsonpath
import yaml


def test1():
    file1 = open('../../resources/parse_qs/parse_qs.yaml', 'r', encoding='utf-8')
    # {'pk_Id': '0', 'secondName': '近来可好', 'userName': '大师傅', 'phoneNumber': '13688882277', 'warnSecondBalance': '88', 'powers': '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', 'transportNum': '0', 'smsNumber': '0', 'isSmS': '1', 'isRelevance': '1', 'exCompanyJson': '[]', 'addUser': 'b5075cb063b941c186c6daaae08e1c2f', 'companyCode': 'c8e405c097a3463ba27ee83cadd9dce5'}
    data1 = yaml.load(file1, Loader=yaml.FullLoader)
    str1 = jsonpath.jsonpath(data1, '$..userName')
    print(str1)
    str2 = jsonpath.jsonpath(data1, '$..userName')
    print(str2)
    str3 = jsonpath.jsonpath(data1, '$..userName')
    print(str3)


def test2():
    file = open('../../resources/parse_qs/parse_qs1.yaml', 'r', encoding='utf-8')
    dict1 = yaml.load(file, Loader=yaml.FullLoader)

    a = jsonpath.jsonpath(dict1, '$..userName')
    print(a)
