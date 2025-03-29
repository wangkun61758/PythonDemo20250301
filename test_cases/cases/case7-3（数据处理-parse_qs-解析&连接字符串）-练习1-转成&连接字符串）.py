#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/11/4 13:41
=================================================='''
import yaml
'''
1、dict转成特殊符号（#)连接的字符串
2、list转成特殊符号（#)连接的字符串
'''
def test1():
    file1 = open('../../resources/parse_qs/parse_qs1.yaml', 'r', encoding='utf-8')
    data1 = yaml.load(file1, Loader=yaml.FullLoader)
    print(data1)

    list1 = []
    for k, v in data1.items():
        list1.append(k)
        list1.append(v)
    print(
        list1)  # ['pk_Id', '0', 'secondName', '近来可好', 'userName', '大师傅', 'phoneNumber', '13688882277', 'warnSecondBalance', '88', 'powers', '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', 'transportNum', '0', 'smsNumber', '0', 'isSmS', '1', 'isRelevance', '1', 'exCompanyJson', '[]', 'addUser', 'b5075cb063b941c186c6daaae08e1c2f', 'companyCode', 'c8e405c097a3463ba27ee83cadd9dce5']

    str = ''
    for i in range(len(list1)):
        str1 = list1[i]
        str = str + str1 + '&'

    print(
        str)  # pk_Id#0#secondName#近来可好#userName#大师傅#phoneNumber#13688882277#warnSecondBalance#88#powers#101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701#transportNum#0#smsNumber#0#isSmS#1#isRelevance#1#exCompanyJson#[]#addUser#b5075cb063b941c186c6daaae08e1c2f#companyCode#c8e405c097a3463ba27ee83cadd9dce5#

    m = len(list1)
    list2 = str.split('#', m - 1)
    print(
        list2)  # ['pk_Id', '0', 'secondName', '近来可好', 'userName', '大师傅', 'phoneNumber', '13688882277', 'warnSecondBalance', '88', 'powers', '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', 'transportNum', '0', 'smsNumber', '0', 'isSmS', '1', 'isRelevance', '1', 'exCompanyJson', '[]', 'addUser', 'b5075cb063b941c186c6daaae08e1c2f', 'companyCode', 'c8e405c097a3463ba27ee83cadd9dce5#']
def test2():
    file = open('../../resources/parse_qs/parse_qs1.yaml', 'r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)
    print(data)

    list1 = []
    for k, v in data.items():
        list1.append(k)
        list1.append(v)

    str1 = ''
    for i in range(len(list1)):
        str2 = list1[i]
        str1 = str1 + str2 + '&'
    # pk_Id&0&secondName&近来可好&userName&大师傅&phoneNumber&13688882277&warnSecondBalance&88&powers&101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701&transportNum&0&smsNumber&0&isSmS&1&isRelevance&1&exCompanyJson&[]&addUser&b5075cb063b941c186c6daaae08e1c2f&companyCode&c8e405c097a3463ba27ee83cadd9dce5&
    print(str1)

    list2 = str1.split('&', len(list1))
    # ['pk_Id', '0', 'secondName', '近来可好', 'userName', '大师傅', 'phoneNumber', '13688882277', 'warnSecondBalance', '88', 'powers', '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', 'transportNum', '0', 'smsNumber', '0', 'isSmS', '1', 'isRelevance', '1', 'exCompanyJson', '[]', 'addUser', 'b5075cb063b941c186c6daaae08e1c2f', 'companyCode', 'c8e405c097a3463ba27ee83cadd9dce5', '']
    print(list2)
