#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/11/4 13:33
=================================================='''
import os
from urllib.parse import parse_qs
import jsonpath
import yaml
'''
parse_qs函数来将查询字符串转换成字典
'''
def test1():
    payload1 = "pk_Id=0&secondName=%E8%BF%91%E6%9D%A5%E5%8F%AF%E5%A5%BD&userName=%E5%A4%A7%E5%B8%88%E5%82%85&phoneNumber=13688882277&warnSecondBalance=88&powers=101%2C104%2C102%2C110%2C109%2C1061%2C201%2C202%2C203%2C301%2C302%2C303%2C315%2C304%2C306%2C307%2C308%2C310%2C501%2C503%2C504%2C601%2C701&logoPhoto=&secondSysName=&transportNum=0&smsNumber=0&isSmS=1&isRelevance=1&exCompanyJson=%5B%5D&addUser=b5075cb063b941c186c6daaae08e1c2f&companyCode=c8e405c097a3463ba27ee83cadd9dce5"
    dict1 = parse_qs(payload1)  # 将查询字符串转换成字典
    print(
        dict1)  # {'pk_Id': ['0'], 'secondName': ['近来可好'], 'userName': ['大师傅'], 'phoneNumber': ['13688882277'], 'warnSecondBalance': ['88'], 'powers': ['101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701'], 'transportNum': ['0'], 'smsNumber': ['0'], 'isSmS': ['1'], 'isRelevance': ['1'], 'exCompanyJson': ['[]'], 'addUser': ['b5075cb063b941c186c6daaae08e1c2f'], 'companyCode': ['c8e405c097a3463ba27ee83cadd9dce5']}

    dict1_style = dict([key, value[0]] for key, value in dict1.items())
    print(
        dict1_style)  # {'pk_Id': '0', 'secondName': '近来可好', 'userName': '大师傅', 'phoneNumber': '13688882277', 'warnSecondBalance': '88', 'powers': '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', 'transportNum': '0', 'smsNumber': '0', 'isSmS': '1', 'isRelevance': '1', 'exCompanyJson': '[]', 'addUser': 'b5075cb063b941c186c6daaae08e1c2f', 'companyCode': 'c8e405c097a3463ba27ee83cadd9dce5'}
def test2():
    file = open('../../resources/parse_qs/parse_qs1.yaml', 'r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)

    list = []
    for k, v in data.items():
        list.append(k)
        list.append(v)

    str = ''
    for i in range(len(list)):
        str = str + list[i] + '#'
    # pk_Id#0#secondName#近来可好#userName#大师傅#phoneNumber#13688882277#warnSecondBalance#88#powers#101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701#transportNum#0#smsNumber#0#isSmS#1#isRelevance#1#exCompanyJson#[]#addUser#b5075cb063b941c186c6daaae08e1c2f#companyCode#c8e405c097a3463ba27ee83cadd9dce5#
    print(str)
def test3():
    f = open('../../resources/parse_qs/parse_qs1.yaml', 'r', encoding='utf-8')
    s = yaml.load(f, Loader=yaml.FullLoader)

    list = []
    for k, v in s.items():
        list.append(k)
        list.append(v)

    str1 = ''
    for i in list:
        str1 = str1 + i
        str1 = str1 + '#'
    print(str1)

    m = str1.split('#', len(list) - 1)
    print(m)
def test4():
    payload = "pk_Id=0&secondName=%E8%BF%91%E6%9D%A5%E5%8F%AF%E5%A5%BD&userName=%E5%A4%A7%E5%B8%88%E5%82%85&phoneNumber=13688882277&warnSecondBalance=88&powers=101%2C104%2C102%2C110%2C109%2C1061%2C201%2C202%2C203%2C301%2C302%2C303%2C315%2C304%2C306%2C307%2C308%2C310%2C501%2C503%2C504%2C601%2C701&logoPhoto=&secondSysName=&transportNum=0&smsNumber=0&isSmS=1&isRelevance=1&exCompanyJson=%5B%5D&addUser=b5075cb063b941c186c6daaae08e1c2f&companyCode=c8e405c097a3463ba27ee83cadd9dce5"
    a = dict([(k, v[0]) for k, v in parse_qs(payload).items()])
    print(a)

    b = dict([(k, v[0]) for k, v in parse_qs(payload).items()])
    print(b)

    c = dict([(k, v[0]) for k, v in parse_qs(payload).items()])
    print(
        c)  # {'pk_Id': '0', 'secondName': '近来可好', 'userName': '大师傅', 'phoneNumber': '13688882277', 'warnSecondBalance': '88', 'powers': '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', 'transportNum': '0', 'smsNumber': '0', 'isSmS': '1', 'isRelevance': '1', 'exCompanyJson': '[]', 'addUser': 'b5075cb063b941c186c6daaae08e1c2f', 'companyCode': 'c8e405c097a3463ba27ee83cadd9dce5'}

    s = jsonpath.jsonpath(c, '$..companyCode')
    print(s)  # ['c8e405c097a3463ba27ee83cadd9dce5']

    if not os.path.exists('../../resources/parse_qs'):
        os.makedirs('../../resources/parse_qs')
    with open('../../resources/parse_qs/parse_qs.yaml', 'w', encoding='utf-8') as file:
        file.write(str(c))
def test5():
    payload = "pk_Id=0&secondName=%E8%BF%91%E6%9D%A5%E5%8F%AF%E5%A5%BD&userName=%E5%A4%A7%E5%B8%88%E5%82%85&phoneNumber=13688882277&warnSecondBalance=88&powers=101%2C104%2C102%2C110%2C109%2C1061%2C201%2C202%2C203%2C301%2C302%2C303%2C315%2C304%2C306%2C307%2C308%2C310%2C501%2C503%2C504%2C601%2C701&logoPhoto=&secondSysName=&transportNum=0&smsNumber=0&isSmS=1&isRelevance=1&exCompanyJson=%5B%5D&addUser=b5075cb063b941c186c6daaae08e1c2f&companyCode=c8e405c097a3463ba27ee83cadd9dce5"
    a = dict([(k, v[0]) for k, v in parse_qs(payload).items()])
    # {'pk_Id': '0', 'secondName': '近来可好', 'userName': '大师傅', 'phoneNumber': '13688882277', 'warnSecondBalance': '88', 'powers': '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', 'transportNum': '0', 'smsNumber': '0', 'isSmS': '1', 'isRelevance': '1', 'exCompanyJson': '[]', 'addUser': 'b5075cb063b941c186c6daaae08e1c2f', 'companyCode': 'c8e405c097a3463ba27ee83cadd9dce5'}
    print(a)

    # [('pk_Id', '0'), ('secondName', '近来可好'), ('userName', '大师傅'), ('phoneNumber', '13688882277'), ('warnSecondBalance', '88'), ('powers', '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701'), ('transportNum', '0'), ('smsNumber', '0'), ('isSmS', '1'), ('isRelevance', '1'), ('exCompanyJson', '[]'), ('addUser', 'b5075cb063b941c186c6daaae08e1c2f'), ('companyCode', 'c8e405c097a3463ba27ee83cadd9dce5')]
    b = [(k, v[0]) for k, v in parse_qs(payload).items()]
    print(b)

    c = dict([(k, v[0]) for k, v in parse_qs(payload).items()])
    print(c)

    d = dict([(k, v[0]) for k, v in parse_qs(payload).items()])
    print(d)

    e = dict([(k, v[0]) for k, v in parse_qs(payload).items()])
    f = dict([(k, v[0]) for k, v in parse_qs(payload).items()])
    g = dict([(k, v[0]) for k, v in parse_qs(payload).items()])
    # {'pk_Id': '0', 'secondName': '近来可好', 'userName': '大师傅', 'phoneNumber': '13688882277', 'warnSecondBalance': '88', 'powers': '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', 'transportNum': '0', 'smsNumber': '0', 'isSmS': '1', 'isRelevance': '1', 'exCompanyJson': '[]', 'addUser': 'b5075cb063b941c186c6daaae08e1c2f', 'companyCode': 'c8e405c097a3463ba27ee83cadd9dce5'}
    print(g)

    r = jsonpath.jsonpath(g, '$..phoneNumber')
    print(r)

    s = jsonpath.jsonpath(g, '$..phoneNumber')

    t = jsonpath.jsonpath(g, '$..phoneNumber')

    u = jsonpath.jsonpath(g, '$..userName')
    print(u)

    v = jsonpath.jsonpath(g, '$..userName')
    w = jsonpath.jsonpath(g, '$..userName')
    x = jsonpath.jsonpath(g, '$..userName')
    y = jsonpath.jsonpath(g, '$..userName')
    z = jsonpath.jsonpath(g, '$..userName')

    dict1 = dict([(k, v[0]) for k, v in parse_qs(payload).items()])
    print(dict1)

    list1 = []
    for k, v in dict1.items():
        list1.append(k)
        list1.append(v)
    # ['pk_Id', '0', 'secondName', '近来可好', 'userName', '大师傅', 'phoneNumber', '13688882277', 'warnSecondBalance', '88', 'powers', '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', 'transportNum', '0', 'smsNumber', '0', 'isSmS', '1', 'isRelevance', '1', 'exCompanyJson', '[]', 'addUser', 'b5075cb063b941c186c6daaae08e1c2f', 'companyCode', 'c8e405c097a3463ba27ee83cadd9dce5']
    print(list1)

    list2 = []
    list3 = []
    for i in range(len(list1)):
        if i % 2 == 0:
            list2.append(list1[i])
        else:
            list3.append(list1[i])
    # ['pk_Id', 'secondName', 'userName', 'phoneNumber', 'warnSecondBalance', 'powers', 'transportNum', 'smsNumber', 'isSmS', 'isRelevance', 'exCompanyJson', 'addUser', 'companyCode']
    print(list2)
    # ['0', '近来可好', '大师傅', '13688882277', '88', '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,
    print(list3)

    dict2 = {list2[i]: list3[i] for i in range(len(list2))}
    print(dict2)
    dict3 = {list2[i]: list3[i] for i in range(len(list2))}

    dict4 = {list2[i]: list3[i] for i in range(len(list2))}
    dict5 = {list2[i]: list3[i] for i in range(len(list2))}
    dict6 = {list2[i]: list3[i] for i in range(len(list2))}
    print(dict6)
    dict7 = {list2[i]: list3[i] for i in range(len(list2))}

    list5 = []
    list6 = []
    for k, v in dict7.items():
        list5.append(k)
        list6.append(v)
    print(list5)
    print(list6)

    dict8 = {list5[i]: list6[i] for i in range(len(list5))}

    if not os.path.exists('../resources/parse_qs3'):
        os.makedirs('../resources/parse_qs3')
    with open('../resources/parse_qs3/parse_qs.yaml', 'w', encoding='utf-8') as f:
        f.write(str(dict8))
def test6():
    payload = "pk_Id=0&secondName=%E8%BF%91%E6%9D%A5%E5%8F%AF%E5%A5%BD&userName=%E5%A4%A7%E5%B8%88%E5%82%85&phoneNumber=13688882277&warnSecondBalance=88&powers=101%2C104%2C102%2C110%2C109%2C1061%2C201%2C202%2C203%2C301%2C302%2C303%2C315%2C304%2C306%2C307%2C308%2C310%2C501%2C503%2C504%2C601%2C701&logoPhoto=&secondSysName=&transportNum=0&smsNumber=0&isSmS=1&isRelevance=1&exCompanyJson=%5B%5D&addUser=b5075cb063b941c186c6daaae08e1c2f&companyCode=c8e405c097a3463ba27ee83cadd9dce5"
    a = dict([(k, v[0]) for k, v in parse_qs(payload).items()])
    print(a)

    b = dict([(k, v[0]) for k, v in parse_qs(payload).items()])
    c = dict([(k, v[0]) for k, v in parse_qs(payload).items()])
    d = dict([(k, v[0]) for k, v in parse_qs(payload).items()])
    e = dict([(k, v[0]) for k, v in parse_qs(payload).items()])
    f = dict([(k, v[0]) for k, v in parse_qs(payload).items()])
    g = dict([(k, v[0]) for k, v in parse_qs(payload).items()])
    h = dict([(k, v[0]) for k, v in parse_qs(payload).items()])
    i = dict([(k, v[0]) for k, v in parse_qs(payload).items()])

    if not os.path.exists('../resources/parse_qs4'):
        os.makedirs('../resources/parse_qs4')
    with open('../resources/parse_qs4/parse_qs1.yaml', 'w', encoding='utf-8') as file1:
        file1.write(str(a))

    list_dirs = os.listdir('../resources/parse_qs4')
    for i in list_dirs:
        path = os.path.join('../resources/parse_qs4', i)
        if os.path.isdir(path):
            print('目录')
        else:
            os.remove(path)

    print(i)
    a1 = jsonpath.jsonpath(a, '$..companyCode')
    print(a1)
    b1 = jsonpath.jsonpath(b, '$..companyCode')
    c1 = jsonpath.jsonpath(c, '$..companyCode')
    d1 = jsonpath.jsonpath(d, '$..companyCode')
    e1 = jsonpath.jsonpath(e, '$..companyCode')
    f1 = jsonpath.jsonpath(f, '$..companyCode')
    g1 = jsonpath.jsonpath(g, '$..companyCode')
    h1 = jsonpath.jsonpath(h, '$..companyCode')
    i1 = jsonpath.jsonpath(i, '$..companyCode')

    if not os.path.exists('../resources/parse_qs5'):
        os.makedirs('../resources/parse_qs5')

    path = '../resources/parse_qs5'
    if os.path.isdir(path):
        os.rmdir(path)
    else:
        print('是文件')
def test7():
    payload1 = "pk_Id=0&secondName=%E8%BF%91%E6%9D%A5%E5%8F%AF%E5%A5%BD&userName=%E5%A4%A7%E5%B8%88%E5%82%85&phoneNumber=13688882277&warnSecondBalance=88&powers=101%2C104%2C102%2C110%2C109%2C1061%2C201%2C202%2C203%2C301%2C302%2C303%2C315%2C304%2C306%2C307%2C308%2C310%2C501%2C503%2C504%2C601%2C701&logoPhoto=&secondSysName=&transportNum=0&smsNumber=0&isSmS=1&isRelevance=1&exCompanyJson=%5B%5D&addUser=b5075cb063b941c186c6daaae08e1c2f&companyCode=c8e405c097a3463ba27ee83cadd9dce5"
    dict1=parse_qs(payload1)#将查询字符串转换成字典
    print(dict1)#{'pk_Id': ['0'], 'secondName': ['近来可好'], 'userName': ['大师傅'], 'phoneNumber': ['13688882277'], 'warnSecondBalance': ['88'], 'powers': ['101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701'], 'transportNum': ['0'], 'smsNumber': ['0'], 'isSmS': ['1'], 'isRelevance': ['1'], 'exCompanyJson': ['[]'], 'addUser': ['b5075cb063b941c186c6daaae08e1c2f'], 'companyCode': ['c8e405c097a3463ba27ee83cadd9dce5']}

    dict1_style=dict([key,value[0]] for key,value in dict1.items())
    print(dict1_style)#{'pk_Id': '0', 'secondName': '近来可好', 'userName': '大师傅', 'phoneNumber': '13688882277', 'warnSecondBalance': '88', 'powers': '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', 'transportNum': '0', 'smsNumber': '0', 'isSmS': '1', 'isRelevance': '1', 'exCompanyJson': '[]', 'addUser': 'b5075cb063b941c186c6daaae08e1c2f', 'companyCode': 'c8e405c097a3463ba27ee83cadd9dce5'}
def test8():
    payload1 = "pk_Id=0&secondName=%E8%BF%91%E6%9D%A5%E5%8F%AF%E5%A5%BD&userName=%E5%A4%A7%E5%B8%88%E5%82%85&phoneNumber=13688882277&warnSecondBalance=88&powers=101%2C104%2C102%2C110%2C109%2C1061%2C201%2C202%2C203%2C301%2C302%2C303%2C315%2C304%2C306%2C307%2C308%2C310%2C501%2C503%2C504%2C601%2C701&logoPhoto=&secondSysName=&transportNum=0&smsNumber=0&isSmS=1&isRelevance=1&exCompanyJson=%5B%5D&addUser=b5075cb063b941c186c6daaae08e1c2f&companyCode=c8e405c097a3463ba27ee83cadd9dce5"
    dict2=dict([k,v[0]] for k,v in parse_qs(payload1).items() )
    print(dict2)
def test9():
    payload1 = "pk_Id=0&secondName=%E8%BF%91%E6%9D%A5%E5%8F%AF%E5%A5%BD&userName=%E5%A4%A7%E5%B8%88%E5%82%85"
    dict1=dict(
        [k,v[0]]
        for k,v in parse_qs(payload1).items()
    )
    print(dict1)#{'pk_Id': '0', 'secondName': '近来可好', 'userName': '大师傅'}
def test10():
    payload1 = "pk_Id=0&secondName=%E8%BF%91%E6%9D%A5%E5%8F%AF%E5%A5%BD&userName=%E5%A4%A7%E5%B8%88%E5%82%85"
    dict1=dict([k,v[0]] for k,v in parse_qs(payload1).items())
    print(dict1)
def test11():
    payload1 = "pk_Id=0&secondName=%E8%BF%91%E6%9D%A5%E5%8F%AF%E5%A5%BD&userName=%E5%A4%A7%E5%B8%88%E5%82%85"
    dict1 = dict(
        [k, v[0]]
        for k, v in parse_qs(payload1).items()
    )
    print(dict1)