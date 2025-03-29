#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/10/13 8:34
=================================================='''
import yaml


def test():
    f = open('../../resources/parse_qs/parse_qs.yaml', 'r', encoding='utf-8')
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(
        data)  # {'pk_Id': '0', 'secondName': '近来可好', 'userName': '大师傅', 'phoneNumber': '13688882277', 'warnSecondBalance': '88', 'powers': '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', 'transportNum': '0', 'smsNumber': '0', 'isSmS': '1', 'isRelevance': '1', 'exCompanyJson': '[]', 'addUser': 'b5075cb063b941c186c6daaae08e1c2f', 'companyCode': 'c8e405c097a3463ba27ee83cadd9dce5'}

    list = []
    for k, v in data.items():
        list.append(k)
        list.append(v)

    print(
        list)  # ['pk_Id', '0', 'secondName', '近来可好', 'userName', '大师傅', 'phoneNumber', '13688882277', 'warnSecondBalance', '88', 'powers', '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', 'transportNum', '0', 'smsNumber', '0', 'isSmS', '1', 'isRelevance', '1', 'exCompanyJson', '[]', 'addUser', 'b5075cb063b941c186c6daaae08e1c2f', 'companyCode', 'c8e405c097a3463ba27ee83cadd9dce5']

    list1 = []
    list2 = []
    for i in range(len(list)):
        if i % 2 == 0:
            list1.append(list[i])
        else:
            list2.append(list[i])

    print(
        list1)  # ['pk_Id', 'secondName', 'userName', 'phoneNumber', 'warnSecondBalance', 'powers', 'transportNum', 'smsNumber', 'isSmS', 'isRelevance', 'exCompanyJson', 'addUser', 'companyCode']
    print(
        list2)  # ['0', '近来可好', '大师傅', '13688882277', '88', '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', '0', '0', '1', '1', '[]', 'b5075cb063b941c186c6daaae08e1c2f', 'c8e405c097a3463ba27ee83cadd9dce5']

    dict1 = dict({list1[i]: list2[i] for i in range(len(list1))})
    print(
        dict1)  # {'pk_Id': '0', 'secondName': '近来可好', 'userName': '大师傅', 'phoneNumber': '13688882277', 'warnSecondBalance': '88', 'powers': '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', 'transportNum': '0', 'smsNumber': '0', 'isSmS': '1', 'isRelevance': '1', 'exCompanyJson': '[]', 'addUser': 'b5075cb063b941c186c6daaae08e1c2f', 'companyCode': 'c8e405c097a3463ba27ee83cadd9dce5'}
