#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/11/4 13:33
=================================================='''
from urllib.parse import parse_qs

'''
parse_qs函数来将 "经过URL编码的字符串" 转成 "dict字典"
unquote() 函数将其解码回原始字符串
例如："pk_Id=0&secondName=%E8%BF%91%E6%9D%A5%E5%8F%AF%E5%A5%BD&userName=%E5%A4%A7%E5%B8%88%E5%82%85"  转为 'pk_Id'=0&secondName=近来可好&userName=大师傅
'''


def test1():
    payload1 = "pk_Id=0&secondName=%E8%BF%91%E6%9D%A5%E5%8F%AF%E5%A5%BD&userName=%E5%A4%A7%E5%B8%88%E5%82%85&phoneNumber=13688882277&warnSecondBalance=88&powers=101%2C104%2C102%2C110%2C109%2C1061%2C201%2C202%2C203%2C301%2C302%2C303%2C315%2C304%2C306%2C307%2C308%2C310%2C501%2C503%2C504%2C601%2C701&logoPhoto=&secondSysName=&transportNum=0&smsNumber=0&isSmS=1&isRelevance=1&exCompanyJson=%5B%5D&addUser=b5075cb063b941c186c6daaae08e1c2f&companyCode=c8e405c097a3463ba27ee83cadd9dce5"
    dict1 = parse_qs(payload1)  # 将查询字符串转换成字典
    # {'pk_Id': ['0'], 'secondName': ['近来可好'], 'userName': ['大师傅'], 'phoneNumber': ['13688882277'], 'warnSecondBalance': ['88'], 'powers': ['101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701'], 'transportNum': ['0'], 'smsNumber': ['0'], 'isSmS': ['1'], 'isRelevance': ['1'], 'exCompanyJson': ['[]'], 'addUser': ['b5075cb063b941c186c6daaae08e1c2f'], 'companyCode': ['c8e405c097a3463ba27ee83cadd9dce5']}
    print(dict1)
    dict1_style = dict([key, value[0]] for key, value in dict1.items())
    # {'pk_Id': '0', 'secondName': '近来可好', 'userName': '大师傅', 'phoneNumber': '13688882277', 'warnSecondBalance': '88', 'powers': '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', 'transportNum': '0', 'smsNumber': '0', 'isSmS': '1', 'isRelevance': '1', 'exCompanyJson': '[]', 'addUser': 'b5075cb063b941c186c6daaae08e1c2f', 'companyCode': 'c8e405c097a3463ba27ee83cadd9dce5'}
    print(dict1_style)