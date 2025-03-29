#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/11/4 13:30
=================================================='''

import jsonpath
from test_cases.public_function.load_data.yaml_load import load
import os.path
import pytest
import yaml

def test1():
    f1 = open('../../resources/parse_qs/parse_qs1.yaml', 'r', encoding='utf-8')
    data1 = yaml.load(f1, Loader=yaml.FullLoader)
    print(data1)

    list1 = []
    for k, v in data1.items():
        list1.append(k)
        list1.append(v)
    print(
        list1)  # ['pk_Id', '0', 'secondName', '近来可好', 'userName', '大师傅', 'phoneNumber', '13688882277', 'warnSecondBalance', '88', 'powers', '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', 'transportNum', '0', 'smsNumber', '0', 'isSmS', '1', 'isRelevance', '1', 'exCompanyJson', '[]', 'addUser', 'b5075cb063b941c186c6daaae08e1c2f', 'companyCode', 'c8e405c097a3463ba27ee83cadd9dce5']

    list_one = []
    list_two = []

    for i in range(len(list1)):
        if i % 2 == 0:
            list_one.append(list1[i])
        else:
            list_two.append(list1[i])
    print(
        list_one)  # ['pk_Id', 'secondName', 'userName', 'phoneNumber', 'warnSecondBalance', 'powers', 'transportNum', 'smsNumber', 'isSmS', 'isRelevance', 'exCompanyJson', 'addUser', 'companyCode']

    print(
        list_two)  # ['0', '近来可好', '大师傅', '13688882277', '88', '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', '0', '0', '1', '1', '[]', 'b5075cb063b941c186c6daaae08e1c2f', 'c8e405c097a3463ba27ee83cadd9dce5']

    di = dict({list_one[i]: list_two[i] for i in range(len(list_one))})
    print(
        str(di))  # {'pk_Id': '0', 'secondName': '近来可好', 'userName': '大师傅', 'phoneNumber': '13688882277', 'warnSecondBalance': '88', 'powers': '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', 'transportNum': '0', 'smsNumber': '0', 'isSmS': '1', 'isRelevance': '1', 'exCompanyJson': '[]', 'addUser': 'b5075cb063b941c186c6daaae08e1c2f', 'companyCode': 'c8e405c097a3463ba27ee83cadd9dce5'}
def test2():
    f1 = open('../../resources/parse_qs/parse_qs1.yaml', 'r', encoding='utf-8')
    data1 = yaml.load(f1, Loader=yaml.FullLoader)

    list1 = []
    for k, v in data1.items():
        list1.append(k)
        list1.append(v)
    print(
        list1)  # ['pk_Id', '0', 'secondName', '近来可好', 'userName', '大师傅', 'phoneNumber', '13688882277', 'warnSecondBalance', '88', 'powers', '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', 'transportNum', '0', 'smsNumber', '0', 'isSmS', '1', 'isRelevance', '1', 'exCompanyJson', '[]', 'addUser', 'b5075cb063b941c186c6daaae08e1c2f', 'companyCode', 'c8e405c097a3463ba27ee83cadd9dce5']

    list_one = []
    list_two = []

    for i in range(len(list1)):
        if i % 2 == 0:
            list_one.append(list1[i])
        else:
            list_two.append(list1[i])
    print(
        list_one)  # ['pk_Id', 'secondName', 'userName', 'phoneNumber', 'warnSecondBalance', 'powers', 'transportNum', 'smsNumber', 'isSmS', 'isRelevance', 'exCompanyJson', 'addUser', 'companyCode']

    print(
        list_two)  # ['0', '近来可好', '大师傅', '13688882277', '88', '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', '0', '0', '1', '1', '[]', 'b5075cb063b941c186c6daaae08e1c2f', 'c8e405c097a3463ba27ee83cadd9dce5']

    # dict = {list_one[i]: list_two[i] for i in range(len(list_one))}
    # print(str(dict))
    # n=len(list_one)
    # print(n)
    di = dict({list_one[i]: list_two[i] for i in range(len(list_one))})
    print(
        str(di))  # {'pk_Id': '0', 'secondName': '近来可好', 'userName': '大师傅', 'phoneNumber': '13688882277', 'warnSecondBalance': '88', 'powers': '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', 'transportNum': '0', 'smsNumber': '0', 'isSmS': '1', 'isRelevance': '1', 'exCompanyJson': '[]', 'addUser': 'b5075cb063b941c186c6daaae08e1c2f', 'companyCode': 'c8e405c097a3463ba27ee83cadd9dce5'}
def test3():
    file1 = open('../../resources/parse_qs/parse_qs1.yaml', 'r', encoding='utf-8')
    data1 = yaml.load(file1, Loader=yaml.FullLoader)
    print(
        data1)  # {'pk_Id': '0', 'secondName': '近来可好', 'userName': '大师傅', 'phoneNumber': '13688882277', 'warnSecondBalance': '88', 'powers': '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', 'transportNum': '0', 'smsNumber': '0', 'isSmS': '1', 'isRelevance': '1', 'exCompanyJson': '[]', 'addUser': 'b5075cb063b941c186c6daaae08e1c2f', 'companyCode': 'c8e405c097a3463ba27ee83cadd9dce5'}

    list1 = []
    for k, v in data1.items():
        list1.append(k)
        list1.append(v)
    print(
        list1)  # ['pk_Id', '0', 'secondName', '近来可好', 'userName', '大师傅', 'phoneNumber', '13688882277', 'warnSecondBalance', '88', 'powers', '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', 'transportNum', '0', 'smsNumber', '0', 'isSmS', '1', 'isRelevance', '1', 'exCompanyJson', '[]', 'addUser', 'b5075cb063b941c186c6daaae08e1c2f', 'companyCode', 'c8e405c097a3463ba27ee83cadd9dce5']

    list12 = []
    list13 = []
    for i in range(len(list1)):
        if i % 2 == 0:
            list12.append(list1[i])
        else:
            list13.append(list1[i])
    print(
        list12)  # ['pk_Id', 'secondName', 'userName', 'phoneNumber', 'warnSecondBalance', 'powers', 'transportNum', 'smsNumber', 'isSmS', 'isRelevance', 'exCompanyJson', 'addUser', 'companyCode']

    print(
        list13)  # ['pk_Id', 'secondName', 'userName', 'phoneNumber', 'warnSecondBalance', 'powers', 'transportNum', 'smsNumber', 'isSmS', 'isRelevance', 'exCompanyJson', 'addUser', 'companyCode']

    dict11 = dict({list12[i]: list13[i] for i in range(len(list13))})
    print(
        dict11)  # {'pk_Id': 'pk_Id', 'secondName': 'secondName', 'userName': 'userName', 'phoneNumber': 'phoneNumber', 'warnSecondBalance': 'warnSecondBalance', 'powers': 'powers', 'transportNum': 'transportNum', 'smsNumber': 'smsNumber', 'isSmS': 'isSmS', 'isRelevance': 'isRelevance', 'exCompanyJson': 'exCompanyJson', 'addUser': 'addUser', 'companyCode': 'companyCode'}
def test4():
    f1 = open('../../resources/parse_qs/parse_qs1.yaml', 'r', encoding='utf-8')
    data2 = yaml.load(f1, Loader=yaml.FullLoader)

    list2 = []
    for k, v in data2.items():
        list2.append(k)
        list2.append(v)
    print(
        list2)  # ['pk_Id', '0', 'secondName', '近来可好', 'userName', '大师傅', 'phoneNumber', '13688882277', 'warnSecondBalance', '88', 'powers', '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', 'transportNum', '0', 'smsNumber', '0', 'isSmS', '1', 'isRelevance', '1', 'exCompanyJson', '[]', 'addUser', 'b5075cb063b941c186c6daaae08e1c2f', 'companyCode', 'c8e405c097a3463ba27ee83cadd9dce5']

    list3 = []
    list4 = []
    for i in range(len(list2)):
        if i % 2 == 0:
            list3.append(list2[i])
        else:
            list4.append(list2[i])
    print(
        list3)  # ['pk_Id', 'secondName', 'userName', 'phoneNumber', 'warnSecondBalance', 'powers', 'transportNum', 'smsNumber', 'isSmS', 'isRelevance', 'exCompanyJson', 'addUser', 'companyCode']

    print(
        list4)  # ['0', '近来可好', '大师傅', '13688882277', '88', '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', '0', '0', '1', '1', '[]', 'b5075cb063b941c186c6daaae08e1c2f', 'c8e405c097a3463ba27ee83cadd9dce5']

    dict2 = dict({list3[i]: list4[i] for i in range(len(list4))})
    print(
        dict2)  # {'pk_Id': '0', 'secondName': '近来可好', 'userName': '大师傅', 'phoneNumber': '13688882277', 'warnSecondBalance': '88', 'powers': '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', 'transportNum': '0', 'smsNumber': '0', 'isSmS': '1', 'isRelevance': '1', 'exCompanyJson': '[]', 'addUser': 'b5075cb063b941c186c6daaae08e1c2f', 'companyCode': 'c8e405c097a3463ba27ee83cadd9dce5'}

    if not os.path.exists('../../resources/parse_qs'):
        os.makedirs('../../resources/parse_qs')
    with open('../../resources/parse_qs/parse_qs1.yaml', 'w', encoding='utf-8') as file33:
        file33.write(str(dict2))
def test5():
    file131 = open('../../resources/data/order.yaml', 'r', encoding='utf-8')  # 打开文件('r':以只读的方式打开文件，编码方式：'utf-8')
    data131 = yaml.load(file131, Loader=yaml.FullLoader)  # 读取yaml文件
    return data131
@pytest.mark.parametrize('data', load('../../resources/data/order.yaml').items())
def test6(data):
    a = data
    print(str(a))  # ('pk_Id', '0')
# {'pk_Id': '0', 'secondName': '近来可好', 'userName': '大师傅', 'phoneNumber': '13688882277', 'warnSecondBalance': '88', 'powers': '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', 'transportNum': '0', 'smsNumber': '0', 'isSmS': '1', 'isRelevance': '1', 'exCompanyJson': '[]', 'addUser': 'b5075cb063b941c186c6daaae08e1c2f', 'companyCode': 'c8e405c097a3463ba27ee83cadd9dce5#'}
@pytest.mark.parametrize('data', load('../../resources/data/order.yaml').values())
def test7(data):
    print(data)  # 0
# {'pk_Id': '0', 'secondName': '近来可好', 'userName': '大师傅', 'phoneNumber': '13688882277', 'warnSecondBalance': '88', 'powers': '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', 'transportNum': '0', 'smsNumber': '0', 'isSmS': '1', 'isRelevance': '1', 'exCompanyJson': '[]', 'addUser': 'b5075cb063b941c186c6daaae08e1c2f', 'companyCode': 'c8e405c097a3463ba27ee83cadd9dce5#'}
@pytest.mark.parametrize('data', load('../../resources/data/order.yaml').values())
def test8(data):
    print(data)  # pk_Id
def test9():
    file1 = open('../../resources/parse_qs/parse_qs1.yaml', 'r', encoding='utf-8')
    data1 = yaml.load(file1, Loader=yaml.FullLoader)

    list1 = []
    for k, v in data1.items():
        list1.append(k)
        list1.append(v)

    list2 = []
    list3 = []
    for i in range(len(list1)):
        if i % 2 == 0:
            list2.append(list1[i])
        else:
            list3.append(list1[i])
    print(
        list2)  # ['pk_Id', 'secondName', 'userName', 'phoneNumber', 'warnSecondBalance', 'powers', 'transportNum', 'smsNumber', 'isSmS', 'isRelevance', 'exCompanyJson', 'addUser', 'companyCode']

    print(
        list3)  # ['0', '近来可好', '大师傅', '13688882277', '88', '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', '0', '0', '1', '1', '[]', 'b5075cb063b941c186c6daaae08e1c2f', 'c8e405c097a3463ba27ee83cadd9dce5#']

    # list144=[]
    # list144=list142+list143
    # print(list144)
    dict141 = dict({list2[i]: list3[i] for i in range(len(list3))})
    print(
        dict141)  # {'pk_Id': '0', 'secondName': '近来可好', 'userName': '大师傅', 'phoneNumber': '13688882277', 'warnSecondBalance': '88', 'powers': '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', 'transportNum': '0', 'smsNumber': '0', 'isSmS': '1', 'isRelevance': '1', 'exCompanyJson': '[]', 'addUser': 'b5075cb063b941c186c6daaae08e1c2f', 'companyCode': 'c8e405c097a3463ba27ee83cadd9dce5#'}
    if not os.path.exists('../../resources/parse_qs'):
        os.makedirs('../../resources/parse_qs')
    with open('../../resources/parse_qs/parse_qs4.yaml', 'w', encoding='utf-8') as file141:
        file141.write(str(dict141))

    # os.remove('../resources/parse_qs/parse_qs4.yaml')
def test10():
    file1 = open('../../resources/parse_qs/parse_qs.yaml', 'r', encoding='utf-8')
    data1 = yaml.load(file1, Loader=yaml.FullLoader)

    list1 = []
    for k, v in data1.items():
        list1.append(k)
        list1.append(v)

    list2 = []
    list3 = []
    for k, v in data1.items():
        list2.append(k)
        list3.append(v)

    list4 = list2 + list3
    len151 = len(list4)

    list5 = []
    list6 = []
    for i in range(len151):
        if i < 13:
            list5.append(list4[i])
        else:
            list6.append(list4[i])
    print(list5)
    print(list6)

    dict151 = dict({list5[i]: list6[i] for i in range(len(list6))})
    print(dict151)

    if not os.path.exists('../resources/parse_qs1'):
        os.makedirs('../resources/parse_qs1')

    with open('../resources/parse_qs1/parse_qs5.yaml', 'w', encoding='utf-8') as file152:
        file152.write(str(dict151))

    # os.remove('../resources/parse_qs/parse_qs5.yaml')

    # lists1 = os.listdir('../resources/parse_qs1')
    # for i in lists1:
    #     new_path = os.path.join('../resources/parse_qs1', i)
    #     if os.path.isdir(new_path):
    #         print('是目录')
    #     else:
    #         os.remove(new_path)

    # lists2=os.listdir('../resources/parse_qs1')
    # for i in lists2:
    #     paths=os.path.join('../resources/parse_qs1',i)
    #     if os.path.isdir(paths):
    #         print('是目录')
    #     else:
    #         os.remove(paths)

    # lists3 = os.listdir('../resources/parse_qs1')
    # for i in lists3:
    #     new_paths3 = os.path.join('../resources/parse_qs1', i)
    #     if os.path.isdir(new_paths3):
    #         print('目录')
    #     else:
    #         os.remove(new_paths3)

    # list4=os.listdir('../resources/parse_qs1')
    # for i in list4:
    #     new_path5=os.path.join('../resources/parse_qs1',i)
    #     if os.path.isdir(new_path5):
    #         print('目录')
    #     else:
    #         os.remove(new_path5)

    # list5 = os.listdir('../resources/parse_qs1')
    # for i in list5:
    #     new_path5 = os.path.join('../resources/parse_qs1', i)
    #     if os.path.isdir(new_path5):
    #         print('目录')
    #     else:
    #         os.remove(new_path5)

    # list6=os.listdir('../resources/parse_qs1')
    # for i in list6:
    #     new_path6=os.path.join('../resources/parse_qs1',i)
    #     if os.path.isdir(new_path6):
    #         print('1')
    #     else:
    #         os.remove(new_path6)

    # list7 = os.listdir('../resources/parse_qs1')
    # for i in list7:
    #     new_path = os.path.join('../resources/parse_qs1', i)
    #     if os.path.isdir(new_path):
    #         print('2')
    #     else:
    #         os.remove(new_path)
def test11():
    file1 = open('../../resources/parse_qs/parse_qs2.yaml', 'r', encoding='utf-8')
    data1 = yaml.load(file1, Loader=yaml.FullLoader)

    list1 = []
    for k, v in data1.items():
        list1.append(k)
        list1.append(v)

    list2 = []
    list3 = []
    for i in range(len(list1)):
        if i % 2 == 0:
            list2.append(list1[i])
        else:
            list3.append(list1[i])

    dict1 = dict({list2[i]: list3[i] for i in range(len(list3))})
    print(
        dict1)  # {'pk_Id': '0', 'secondName': '近来可好', 'userName': '大师傅', 'phoneNumber': '13688882277', 'warnSecondBalance': '88', 'powers': '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', 'transportNum': '0', 'smsNumber': '0', 'isSmS': '1', 'isRelevance': '1', 'exCompanyJson': '[]', 'addUser': 'b5075cb063b941c186c6daaae08e1c2f', 'companyCode': 'c8e405c097a3463ba27ee83cadd9dce5#'}

    list4 = []
    list5 = []
    for k, v in dict1.items():
        list4.append(k)
        list5.append(v)
    print(
        list4)  # ['pk_Id', 'secondName', 'userName', 'phoneNumber', 'warnSecondBalance', 'powers', 'transportNum', 'smsNumber', 'isSmS', 'isRelevance', 'exCompanyJson', 'addUser', 'companyCode']

    print(
        list5)  # ['0', '近来可好', '大师傅', '13688882277', '88', '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', '0', '0', '1', '1', '[]', 'b5075cb063b941c186c6daaae08e1c2f', 'c8e405c097a3463ba27ee83cadd9dce5#']

    list6 = []
    for k, v in dict1.items():
        list6.append(k)
        list6.append(v)
    print(
        list6)  # ['pk_Id', '0', 'secondName', '近来可好', 'userName', '大师傅', 'phoneNumber', '13688882277', 'warnSecondBalance', '88', 'powers', '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', 'transportNum', '0', 'smsNumber', '0', 'isSmS', '1', 'isRelevance', '1', 'exCompanyJson', '[]', 'addUser', 'b5075cb063b941c186c6daaae08e1c2f', 'companyCode', 'c8e405c097a3463ba27ee83cadd9dce5#']
    dict7 = {}
    for i in range(len(list6)):
        if i % 2 == 0:
            dict7.update(dict({list6[i]: list6[
                i + 1]}))  # {'pk_Id': '0', 'secondName': '近来可好', 'userName': '大师傅', 'phoneNumber': '13688882277', 'warnSecondBalance': '88', 'powers': '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', 'transportNum': '0', 'smsNumber': '0', 'isSmS': '1', 'isRelevance': '1', 'exCompanyJson': '[]', 'addUser': 'b5075cb063b941c186c6daaae08e1c2f', 'companyCode': 'c8e405c097a3463ba27ee83cadd9dce5#'}
        else:
            pass

    list1 = []
    for k, v in dict7.items():
        list1.append(k)
        list1.append(v)
    print(
        list1)  # ['pk_Id', '0', 'secondName', '近来可好', 'userName', '大师傅', 'phoneNumber', '13688882277', 'warnSecondBalance', '88', 'powers', '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', 'transportNum', '0', 'smsNumber', '0', 'isSmS', '1', 'isRelevance', '1', 'exCompanyJson', '[]', 'addUser', 'b5075cb063b941c186c6daaae08e1c2f', 'companyCode', 'c8e405c097a3463ba27ee83cadd9dce5#']

    list2 = []
    list3 = []
    for i in range(len(list1)):
        if i % 2 == 0:
            list2.append(list1[i])

        else:
            list3.append(list1[i])

    print(list2)
    print(list3)

    dict121 = dict({list2[i]: list3[i] for i in range(len(list2))})
    print(str(dict121))

    if not os.path.exists('../../resources/parse_qs'):
        os.makedirs('../../resources/parse_qs')
    with open('../../resources/parse_qs/parse_qs3.yaml', 'w', encoding='utf-8') as file1:
        file1.write(
            str(dict121))  # {'pk_Id': '0', 'secondName': '近来可好', 'userName': '大师傅', 'phoneNumber': '13688882277', 'warnSecondBalance': '88', 'powers': '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', 'transportNum': '0', 'smsNumber': '0', 'isSmS': '1', 'isRelevance': '1', 'exCompanyJson': '[]', 'addUser': 'b5075cb063b941c186c6daaae08e1c2f', 'companyCode': 'c8e405c097a3463ba27ee83cadd9dce5#'}
def test12():
    file = open('../../resources/parse_qs/parse_qs.yaml', 'r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)
    print(data)

    list1 = []
    list2 = []
    for k, v in data.items():
        list1.append(k)
        list2.append(v)
    print(list1)
    print(list2)

    list3 = list1 + list2
    print(list3)

    dict1 = dict({list1[i]: list2[i] for i in range(len(list2))})
    print(dict1)

    dict2 = dict({list1[i]: list2[i] for i in range(len(list2))})
    print(dict2)

    dict3 = dict({list1[i]: list2[i] for i in range(len(list2))})
    print(dict3)

    dict4 = dict({list1[i]: list2[i] for i in range(len(list2))})
    print(dict4)

    dict5 = dict({list1[i]: list2[i] for i in range(len(list1))})
    print(dict5)

    dict6 = dict({list1[i]: list2[i] for i in range(len(list2))})
    print(dict6)
    print(type(dict6))  # <class 'dict'>

    dict7 = {list1[i]: list2[i] for i in range(len(list2))}
    print(dict7)
    print(type(dict7))  # <class 'dict'>

    if not os.path.exists('../resources/parse_qs1'):
        os.makedirs('../resources/parse_qs1')
    with open('../resources/parse_qs1/parse_qs.yaml', 'w', encoding='utf-8') as file:
        file.write(str(dict7))

    list_dit = os.listdir('../resources/parse_qs1')
    for i in list_dit:
        path = os.path.join('../resources/parse_qs1', i)
        if os.path.isdir(path):
            print('目录')
        else:
            os.remove(path)
def test13():
    file1 = open('../../resources/parse_qs/parse_qs1.yaml', 'r', encoding='utf_8')
    data1 = yaml.load(file1, Loader=yaml.FullLoader)
    print(data1)

    list1 = []
    for k, v in data1.items():
        list1.append(k)
        list1.append(v)
    print(list1)

    list2 = []
    list3 = []
    for i in range(len(list1)):
        if i % 2 == 0:
            list2.append(list1[i])
        else:
            list3.append(list1[i])
    print(
        list2)  # ['pk_Id', 'secondName', 'userName', 'phoneNumber', 'warnSecondBalance', 'powers', 'transportNum', 'smsNumber', 'isSmS', 'isRelevance', 'exCompanyJson', 'addUser', 'companyCode']

    print(
        list3)  # ['0', '近来可好', '大师傅', '13688882277', '88', '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', '0', '0', '1', '1', '[]', 'b5075cb063b941c186c6daaae08e1c2f', 'c8e405c097a3463ba27ee83cadd9dce5']

    list4 = list2 + list3
    list5 = []
    list6 = []
    for i in range(len(list4)):
        if i < len(list4) / 2:
            list5.append(list4[i])
        else:
            list6.append(list4[i])
    print(
        list5)  # ['pk_Id', 'secondName', 'userName', 'phoneNumber', 'warnSecondBalance', 'powers', 'transportNum', 'smsNumber', 'isSmS', 'isRelevance', 'exCompanyJson', 'addUser', 'companyCode']

    print(
        list6)  # ['0', '近来可好', '大师傅', '13688882277', '88', '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', '0', '0', '1', '1', '[]', 'b5075cb063b941c186c6daaae08e1c2f', 'c8e405c097a3463ba27ee83cadd9dce5']

    set1 = set()  # 创建空set集合
    for i in range(len(list5)):
        set1.add(list5[i])
    print(
        set1)  # {'userName', 'phoneNumber', 'companyCode', 'pk_Id', 'powers', 'addUser', 'smsNumber', 'exCompanyJson', 'secondName', 'warnSecondBalance', 'isRelevance', 'isSmS', 'transportNum'}

    set2 = set()
    for i in range(len(list6)):
        set2.add(list6[i])
    print(
        set2)  # {'大师傅', '88', 'b5075cb063b941c186c6daaae08e1c2f', '近来可好', '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', '0', '[]', '13688882277', 'c8e405c097a3463ba27ee83cadd9dce5', '1'}

    list7 = list(set1)
    list8 = list(set2)
    print('list7:' + str(list7), '\n', 'list8:' + str(list8))

    if not os.path.exists('../resources/parse_qs2'):
        os.makedirs('../resources/parse_qs2')
    with open('../resources/parse_qs2/parse_qs1.yaml', 'w', encoding='utf-8') as file2:
        file2.write(str(list7))

    list_dir = os.listdir('../resources/parse_qs2')
    for i in list_dir:
        new_path = os.path.join('../resources/parse_qs2', i)
        if os.path.isdir(new_path):
            print('目录')
        else:
            if new_path == '../resources/parse_qs2\parse_qs1.yaml':

                os.remove(new_path)
                print('成功删除')
            else:
                print('不删除')
def test14():
    file = open('../../resources/parse_qs/parse_qs1.yaml', 'r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)
    print('22222222' + str(data))

    list1 = []
    list2 = []
    for k, v in data.items():
        # ['pk_Id', 'secondName', 'userName', 'phoneNumber', 'warnSecondBalance', 'powers', 'transportNum', 'smsNumber', 'isSmS', 'isRelevance', 'exCompanyJson', 'addUser', 'companyCode']
        list1.append(k)
        # ['0', '近来可好', '大师傅', '13688882277', '88', '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', '0', '0', '1', '1', '[]', 'b5075cb063b941c186c6daaae08e1c2f', 'c8e405c097a3463ba27ee83cadd9dce5']
        list2.append(v)
    print(list1)
    print(list2)

    list3 = list1 + list2

    list4 = []
    list5 = []
    for i in range(len(list3)):
        if i < len(list3) / 2:
            list4.append(list3[i])
        else:
            list5.append(list3[i])
    print(list4)
    print(list5)
    # {'pk_Id': '0', 'secondName': '近来可好', 'userName': '大师傅', 'phoneNumber': '13688882277', 'warnSecondBalance': '88', 'powers': '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', 'transportNum': '0', 'smsNumber': '0', 'isSmS': '1', 'isRelevance': '1', 'exCompanyJson': '[]', 'addUser': 'b5075cb063b941c186c6daaae08e1c2f', 'companyCode': 'c8e405c097a3463ba27ee83cadd9dce5'}
    dict = {list4[i]: list5[i] for i in range(len(list4))}
    print(dict)
    print(type(dict))

    if not os.path.exists('../resources/parse_qs3'):
        os.makedirs('../resources/parse_qs3')
    with open('../resources/parse_qs3/parse_qs.yaml', 'w', encoding='utf-8') as f:
        f.write(str(dict))

    list_dit = os.listdir('../resources/parse_qs3')
    for i in list_dit:
        path = os.path.join('../resources/parse_qs3', i)
        if os.path.isdir(path):
            print('目录')
        else:
            os.remove(path)
def test15():
    file1 = open('../../resources/parse_qs/parse_qs1.yaml', 'r', encoding='utf-8')
    data1 = yaml.load(file1, Loader=yaml.FullLoader)
    print(data1)

    list1 = []
    list2 = []
    for k, v in data1.items():
        list1.append(k)
        list2.append(v)
    print(list1)
    print(list2)
    list3 = list1 + list2
    # ['pk_Id', 'secondName', 'userName', 'phoneNumber', 'warnSecondBalance', 'powers', 'transportNum', 'smsNumber', 'isSmS', 'isRelevance', 'exCompanyJson', 'addUser', 'companyCode', '0', '近来可好', '大师傅', '13688882277', '88', '101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701', '0', '0', '1', '1', '[]', 'b5075cb063b941c186c6daaae08e1c2f', 'c8e405c097a3463ba27ee83cadd9dce5']
    print(list3)

    list4 = []
    list5 = []

    for i in range(len(list3)):
        if i <= len(list3) / 2:
            list4.append(list3[i])
        else:
            list5.append(list3[i])

    print(list4)
    print(list5)

    list6 = list4 + list5

    str1 = ''
    for i in range(len(list6)):
        str1 = str1 + list6[i] + '&'
    print(str1)

    list7 = str1.split('&', len(list6))
    print(list7)
    list7.pop()
    print(list7)

    list8 = []
    list9 = []
    for i in range(len(list7)):
        if i <= len(list7) / 2 - 1:
            list8.append(list7[i])
        else:
            list9.append(list7[i])

    dict1 = {list8[i]: list9[i] for i in range(len(list9))}
    print(dict1)
    print(type(dict1))

    if not os.path.exists('../resources/parse_qs4'):
        os.makedirs('../resources/parse_qs4')
    with open('../resources/parse_qs4/parse_qs1.yaml', 'w', encoding='utf-8') as f:
        f.write(str(dict1))

    # list_dirs=os.listdir('../resources/parse_qs4')
    # for i in list_dirs:
    #     path=os.path.join('../resources/parse_qs4',i)
    #
    #     if os.path.isdir(path):
    #         print('是目录')
    #     else:
    #         os.remove(path)
    list_dirs = os.listdir('../resources/parse_qs4')
    for i in list_dirs:
        path = os.path.join('../resources/parse_qs4', i)
        if os.path.isdir(path):
            print('是目录')
        else:
            os.remove(path)
def test16():
    file1 = open('../../resources/parse_qs/parse_qs1.yaml', 'r', encoding='utf-8')
    data1 = yaml.load(file1, Loader=yaml.FullLoader)

    list1 = []
    list2 = []
    for k, v in data1.items():
        list1.append(k)
        list2.append(v)

    list3 = list1 + list2
    print(list3)
    list4 = []
    list5 = []
    for i in range(len(list3)):
        if i <= len(list3) / 2 - 1:
            list4.append(list3[i])
        else:
            list5.append(list3[i])
    print(list4)
    print(list5)

    dict1 = {list4[i]: list5[i] for i in range(len(list4))}
    print(dict1)
    a = jsonpath.jsonpath(dict1, '$..userName')
    print('jsonpath获取到的值：' + str(a))
    list6 = []
    for k, v in dict1.items():
        list6.append(k)
        list6.append(v)
    print(list6)

    str1 = ''
    for i in range(len(list6)):
        str1 = str1 + list6[i] + '&'
    print(str1)

    list7 = str1.split('&', len(list6))
    print(list7)

    list8 = []

    list9 = []
    for i in range(len(list7)):
        if i % 2 == 0:
            list8.append(list7[i])
        else:
            list9.append(list7[i])
    list8.pop()
    print('list8去掉最后一个下标的值：' + str(list8))

    print(list9)

    dict2 = {list8[i]: list9[i] for i in range(len(list8))}
    print(dict2)

    if not os.path.exists('../resources/parse_qs4'):
        os.makedirs('../resources/parse_qs4')
    with open('../resources/parse_qs4/parse_qs4.yaml', 'w', encoding='utf-8') as file2:
        file2.write(str(dict2))

    list_dicts = os.listdir('../resources/parse_qs4')
    for i in list_dicts:
        path = os.path.join('../resources/parse_qs4', i)
        if os.path.isdir(path):
            print('是目录')
        else:
            os.remove(path)
def test16():
    file1 = open('../../resources/parse_qs/parse_qs1.yaml', 'r', encoding='utf-8')
    data = yaml.load(file1, Loader=yaml.FullLoader)

    list1 = []
    for k, v in data.items():
        list1.append(k)
        list1.append(v)
    print(list1)

    str1 = ''
    for i in range(len(list1)):
        str1 = str1 + list1[i] + '&'
    print(str1)

    list2 = str1.split('&', len(list1))
    print('list2：' + str(list2))
    list2.pop()
    print('list2去除末尾一个参数后的值为：' + str(list2))

    list3 = []
    list4 = []
    for i in range(len(list2)):
        if i % 2 == 0:
            list3.append(list2[i])
        else:
            list4.append(list2[i])
    print(list3)
    print(list4)
    list5 = list3 + list4
    print(list5)

    list6 = []
    list7 = []
    for i in range(len(list5)):
        if i <= len(list5) / 2 - 1:
            list6.append(list5[i])
        else:
            list7.append(list5[i])
    print(list6)
    print(list7)

    dict1 = {list6[i]: list7[i] for i in range(len(list6))}
    print(dict1)

    if not os.path.exists('../resources/parse_qs4'):
        os.makedirs('../resources/parse_qs4')
    with open('../resources/parse_qs4/parse-qs1.yaml', 'w', encoding='utf-8') as file2:
        file2.write(str(dict1))

    list_dicts = os.listdir('../resources/parse_qs4')
    for i in list_dicts:
        path = os.path.join('../resources/parse_qs4', i)
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.remove(path)
def test17():
    file = open('../../resources/parse_qs/parse_qs1.yaml', 'r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)

    list1 = []
    for k, v in data.items():
        list1.append(k)
        list1.append(v)
    print(list1)

    list2 = []
    list3 = []
    for i in range(len(list1)):
        if i % 2 == 0:
            list2.append(list1[i])
        else:
            list3.append(list1[i])

    dict1 = {list2[i]: list3[i] for i in range(len(list2))}

    list4 = []
    list5 = []
    for k, v in dict1.items():
        list4.append(k)
        list5.append(v)

    list6 = list4 + list5
    list7 = []
    list8 = []
    for i in range(len(list6)):
        if i <= len(list6) / 2 - 1:
            list7.append(list6[i])
        else:
            list8.append(list6[i])

    str1 = ''
    for i in range(len(list7)):
        str1 = str1 + list7[i] + '&'
    str2 = ''
    for i in range(len(list8)):
        str2 = str2 + '#' + list8[i]
    list9 = str1.split('&', len(list7))
    list10 = str2.split('#', len(list8))
    list9.pop()
    list10.pop(0)

    dict2 = {list9[i]: list10[i] for i in range(len(list10))}

    if os.path.exists('../resources/parse_q4'):
        os.makedirs('../resources/parse_qs4')
    with open('../resources/parse_qs4/parse_qs1.yaml', 'w', encoding='utf-8') as file1:
        file1.write(str(dict2))

    list_dits = os.listdir('../resources/parse_qs4')
    for i in list_dits:
        path = os.path.join('../resources/parse_qs4', i)
        if os.path.isdir(path):
            print('目录')
        else:
            os.remove(path)
def test18():
    file1 = open('../../resources/parse_qs/parse_qs1.yaml', 'r', encoding='utf-8')
    dict1 = yaml.load(file1, Loader=yaml.FullLoader)
    print(dict1)

    list1 = []
    for k, v in dict1.items():
        list1.append(k)
        list1.append(v)

    list2 = []
    list3 = []
    for i in range(len(list1)):
        if i % 2 == 0:
            list2.append(list1[i])
        else:
            list3.append(list1[i])

    dict2 = {list2[i]: list3[i] for i in range(len(list2))}
    print(dict2)

    if not os.path.exists('../resources/parse_qs5'):
        os.makedirs('../resources/parse_qs5')

    with open('../resources/parse_qs5/parse_qs1.yaml', 'w', encoding='utf-8') as file2:
        file2.write(str(dict2))

    list_dict = os.listdir('../resources/parse_qs5')
    for i in list_dict:
        path = os.path.join('../resources/parse_qs5', i)
        if os.path.isdir(path):
            print('是目录')
        else:
            os.remove(path)
def test19():
    file1 = open('../../resources/parse_qs/parse_qs1.yaml', 'r', encoding='utf-8')
    dict1 = yaml.load(file1, Loader=yaml.FullLoader)

    list1 = []
    list2 = []
    for k, v in dict1.items():
        list1.append(k)
        list2.append(v)

    list3 = list1 + list2

    list4 = []
    list5 = []
    for i in range(len(list3)):
        if i <= len(list3) / 2 - 1:
            list4.append(list3[i])
        else:
            list5.append(list3[i])
    print(list4)
    print(list5)

    dict2 = {list4[i]: list5[i] for i in range(len(list5))}
    print(dict2)

    str1 = jsonpath.jsonpath(dict2, '$..phoneNumber')
    print(str1)

    list6 = []
    for k, v in dict2.items():
        list6.append(k)
        list6.append(v)
    str2 = ''
    for i in range(len(list6)):
        str2 = str2 + '&' + list6[i]
    print(str2)

    list7 = str2.split('&', len(list6))
    print(list7)

    list7.remove('')
    print(list7)
    list8 = []
    list9 = []
    for i in range(len(list7)):
        if i % 2 == 0:
            list8.append(list7[i])
        else:
            list9.append(list7[i])

    dict3 = {list8[i]: list9[i] for i in range(len(list8))}
    print(dict3)

    if not os.path.exists('../resources/parse_qs6'):
        os.makedirs('../resources/parse_qs6')
    with open('../resources/parse_qs6/parse_qs1.yaml', 'w', encoding='utf-8') as file2:
        file2.write(str(dict3))

    list_dict1 = os.listdir('../resources/parse_qs6')
    for i in list_dict1:
        path = os.path.join('../resources/parse_qs6', i)
        if os.path.isdir(path):
            print('是目录')
        else:
            os.remove(path)
def test20():
    file = open('../../resources/parse_qs/parse_qs1.yaml', 'r', encoding='utf-8')
    dict = yaml.load(file, Loader=yaml.FullLoader)

    list1 = []
    for k, v in dict.items():
        list1.append(k)
        list1.append(v)
    list2 = []
    list3 = []
    for i in range(len(list1)):
        if i % 2 == 0:
            list2.append(list1[i])
        else:
            list3.append(list1[i])

    dict2 = {list2[i]: list3[i] for i in range(len(list2))}
    print(dict2)

    list4 = []
    for i in range(len(list2)):
        Cookie = "{}={}".format(list2[i], list3[i])
        list4.append(Cookie)
        print('Cookie:' + Cookie)
    print(list4)

    if not os.path.exists('../resources/parse_qs7'):
        os.makedirs('../resources/parse_qs7')
    with open('../resources/parse_qs7/parse_qs.yaml', 'w', encoding='utf-8') as file1:
        file1.write(str(dict2))

    list_dict = os.listdir('../resources/parse_qs7')
    for i in list_dict:
        path = os.path.join('../resources/parse_qs7', i)
        if os.path.isdir(path):
            print('目录')
        else:
            os.remove(path)
def test21():
    file1=open('../../resources/parse_qs/parse_qs.yaml', 'r', encoding='utf-8')
    data1=yaml.load(file1,Loader=yaml.FullLoader)
    list1=[]
    list2=[]
    for key,value in data1.items():
        list1.append(key)
        list2.append(value)

    dict1={list1[i]:list2[i] for i in range(len(list2))}
    print(dict1)
    if not os.path.exists('../resources/parse_qs9'):
        os.makedirs('../resources/parse_qs9')
    with open('../resources/parse_qs9/parse_qs.yaml', 'w', encoding='utf-8') as file2:
        file2.write(str(dict1))
    list3=os.listdir('../../resources/parse_qs')
    for i in list3:
        path1=os.path.join('../../resources/parse_qs', i)
        if os.path.isdir(path1):
            print('是目录')
            if path1.endswith('.yaml'):
                print('目录是以.yaml结尾')
                # os.remove(path1)

        elif os.path.isfile(path1):
            print('是文件')
            if path1.startswith('.yaml'):
                print('文件是以.yaml结尾')
                # shutil.rmtree(path1)
def test22():
    file1=open('../../resources/parse_qs/parse_qs.yaml','r',encoding='utf-8')
    data1=yaml.load(file1,Loader=yaml.FullLoader)
    list1=[]
    list2=[]
    for k,v in data1.items():
        list1.append(k)
        list2.append(v)
    dict1={list1[i]:list2[i] for i in range(len(list2))}
    print(dict1)
    a=jsonpath.jsonpath(dict1,'$..secondName')
    print(a)
    if not os.path.exists('../../resources/parse_qs3'):
        os.makedirs('../../resources/parse_qs3')
    with open('../../resources/parse_qs3/parse_qs3.yaml', 'w', encoding='utf-8') as file2:
        file2.write(str(dict1))

    list_dict=os.listdir('../../resources/parse_qs3')
    for i in list_dict:
        path1=os.path.join('../../resources/parse_qs3', i)
        if os.path.isdir(path1):
            print('是目录')
            if path1.startswith('.yaml'):
                print('目录是以.yaml开始')
            elif path1.endswith('.yaml'):
                print('目录是以.yaml结尾')
        else:
            if path1.endswith('.yaml'):
                os.remove(path1)
'''
练习：2025/3/20（1）
'''
def test23():
    file1=open('../../resources/parse_qs/parse_qs.yaml','r',encoding='utf-8')
    data1=yaml.load(file1,Loader=yaml.FullLoader)
    list1=[]
    list2=[]
    for k,v in data1.items():
        list1.append(k)
        list1.append(v)
    dict2={list1[i]:list2[i] for i in range(len(list2))}
    a=jsonpath.jsonpath(dict2,'$..secondName')
    print(a)
    if not os.path.exists('../../resources/parse_qs8'):
        os.makedirs('../../resources/parse_qs8')
    with open('../../resources/parse_qs8/parse_qs8.yaml', 'w', encoding='utf-8') as file2:
        file2.write(str(dict2))
    list_dict=os.listdir('../../resources/parse_qs8')
    for i in list_dict:
        path1=os.path.join('../../resources/parse_qs8', i)
        if os.path.isdir(path1):
            print('是目录')
            if path1.startswith('.yaml'):
                print('.yaml开始')
                os.remove(path1)
            else:pass
        elif os.path.isfile(path1):
            print('是文件')
            if path1.endswith('.yaml'):
                print('.yaml结尾')
def test24():
    file1=open('../../resources/parse_qs/parse_qs.yaml','r',encoding='utf-8')
    data1=yaml.load(file1,Loader=yaml.FullLoader)
    list1=[]
    list2=[]
    for k,v in data1.items():
        list1.append(k)
        list2.append(v)
    dict2=dict({list1[i]:list2[i] for i in range(len(list2))})
    a=jsonpath.jsonpath(dict2,'$..secondName')
    if not os.path.exists('../../resources/parse_qs8'):
        os.makedirs('../../resources/parse_qs')
    with open('../../resources/parse_qs8/parse_qs8.yaml', 'w', encoding='utf-8') as file2:
        file2.write(str(dict2))
    list_dict=os.listdir('../../resources/parse_qs8')
    for i in list_dict:
        path1=os.path.join('../../resources/parse_qs8', i)
        if os.path.isdir(path1):
            print('是目录')
            if path1.endswith('.yaml'):
                # os.remove(path1)
                print('.yaml结尾')
        elif os.path.isfile(path1):
            print('是文件')
            if path1.startswith('.yaml'):
                # os.remove(path1)
                print('.yaml开始')


