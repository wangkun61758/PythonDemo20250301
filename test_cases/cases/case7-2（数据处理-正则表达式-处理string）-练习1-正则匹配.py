#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/11/4 14:05
=================================================='''
import re
import yaml

'''
    \S	匹配任意非空字符
    \d	匹配任意数字
    \D	匹配任意非数字
    .	匹配任意字符
    *	匹配0个或多个的表达式
    +	匹配1个或多个的表达式
'''


def test1():
    str1 = 'pk_Id&0&secondName&近来可好&userName&大师傅&phoneNumber&13688882277&warnSecondBalance&88&powers&101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701&transportNum&0&smsNumber&0&isSmS&1&isRelevance&1&exCompanyJson&[]&addUser&b5075cb063b941c186c6daaae08e1c2f&companyCode&c8e405c097a3463ba27ee83cadd9dce5&'
    '''
    1、re.findall() —— 匹配的结果是列表
    2、r'(.*)Balance(.*)102' —— 以【Balance】进行分割：
    1）前一部分 —— pk_Id&0&secondName&近来可好&userName&大师傅&phoneNumber&13688882277&warnSecond
    2）后一部分 —— &88&powers&101,104,【解析：(.*)102 的意思是匹配102之前，Balance之后的任意字符部分】
    '''
    a = re.findall(r'(.*)Balance(.*)102', str1, re.M | re.I)
    print(a)  # [('pk_Id&0&secondName&近来可好&userName&大师傅&phoneNumber&13688882277&warnSecond', '&88&powers&101,104,')]

    # re.search() 函数用于在字符串中查找匹配的第一个子串，并返回一个匹配对象
    b = re.search(r'(.*)Name', str1, re.M | re.I)
    print(b)  # pk_Id&0&secondName&近来可好&userName

    c = re.match(r'(.*)Name', str1, re.M | re.I)
    print(c)  # pk_Id&0&secondName&近来可好&userName


def test2():
    file1 = open('../../resources/parse_qs/parse_qs.yaml', 'r', encoding='utf-8')
    data1 = yaml.load(file1, Loader=yaml.FullLoader)
    str1 = ''
    for k, v in data1.items():
        str181 = str1 + k
        str181 = str1 + v
    print(
        str1)  # pk_Id0secondName近来可好userName大师傅phoneNumber13688882277warnSecondBalance88powers101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701transportNum0smsNumber0isSmS1isRelevance1exCompanyJson[]addUserb5075cb063b941c186c6daaae08e1c2fcompanyCodec8e405c097a3463ba27ee83cadd9dce5
    # match='pk_Id0secondName近来可好userName大师傅phoneNumber1368888
    match = re.match(r'(.*)userName(.*)', str181, re.M | re.I)
    print(match)

    match1 = re.search(r'user(.*)', str181, re.M | re.I)
    print(match1)  # <re.Match object; span=(20, 308), match='userName大师傅phoneNumber13688882277warnSecondBalanc>

    match2 = re.search(r'[Uu]ser', str181)
    print(match2)  # <re.Match object; span=(20, 24), match='user'>

    stri = 'pk_Id0seconuserName d Name近userName 来可好 userName 大师userName傅phoneNumbuserNameer13688882277userNauserNameme'
    ser1 = re.search(r'[Uu]ser', stri, re.M)
    print(ser1)  # <re.Match object; span=(11, 15), match='user'>

    ser2 = re.search(r'user.*?', stri)
    print(ser2)  # <re.Match object; span=(11, 15), match='user'>

    ser3 = re.search(r'user.*?$', stri)
    print(ser3)  # <re.Match object; span=(11, 106), match='userName d Name近userName 来可好 userName 大师userName傅>

    ser4 = re.search(r'user.*user', stri)
    print(ser4)  # <re.Match object; span=(11, 31), match='userName d Name近user'>

    str1 = 'pk_Id0seconuserNames d Name近userName 来可好 userName 大师userName  傅phoneNumbuserNameer  13688882277userNauserNameme'
    ser5 = re.search(r'.*user', str1)
    print(ser5)  # <re.Match object; span=(0, 100), match='pk_Id0seconuserName d Name近userName 来可好 userName >


def test3():
    file1 = open('../../resources/parse_qs/parse_qs.yaml', 'r', encoding='utf-8')
    data1 = yaml.load(file1, Loader=yaml.FullLoader)
    str1 = ''
    for k, v in data1.items():
        str1 = str1 + k
        str1 = str1 + v
    print(
        str1)  # pk_Id0secondName近来可好userName大师傅phoneNumber13688882277warnSecondBalance88powers101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701transportNum0smsNumber0isSmS1isRelevance1exCompanyJson[]addUserb5075cb063b941c186c6daaae08e1c2fcompanyCodec8e405c097a3463ba27ee83cadd9dce5
    # match='pk_Id0secondName近来可好userName大师傅phoneNumber1368888
    match = re.match(r'(.*)userName(.*)', str1, re.M | re.I)
    print(match)

    match1 = re.search(r'user(.*)', str1, re.M | re.I)
    print(match1)  # <re.Match object; span=(20, 308), match='userName大师傅phoneNumber13688882277warnSecondBalanc>

    match2 = re.search(r'[Uu]ser', str1)
    print(match2)  # <re.Match object; span=(20, 24), match='user'>

    stri = 'pk_Id0seconuserName d Name近userName 来可好 userName 大师userName傅phoneNumbuserNameer13688882277userNauserNameme'
    ser1 = re.search(r'[Uu]ser', stri, re.M)
    print(ser1)  # <re.Match object; span=(11, 15), match='user'>

    ser2 = re.search(r'user.*?', stri)
    print(ser2)  # <re.Match object; span=(11, 15), match='user'>

    ser3 = re.search(r'user.*?$', stri)
    print(ser3)  # <re.Match object; span=(11, 106), match='userName d Name近userName 来可好 userName 大师userName傅>

    ser4 = re.search(r'user.*user', stri)
    print(ser4)  # <re.Match object; span=(11, 31), match='userName d Name近user'>


def test4():
    file = open('../../resources/parse_qs/parse_qs1.yaml', 'r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)

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

    '''
     .* —— 表示匹配一个或多个任意【字符】
    '''
    a1 = re.findall(r'.*Balance', str1, re.M | re.I)
    print(a1)  # ['pk_Id&0&secondName&近来可好&userName&大师傅&phoneNumber&13688882277&warnSecondBalance']

    a2 = re.findall(r'(.*)Balance', str1, re.M | re.I)
    print(a2)  # ['pk_Id&0&secondName&近来可好&userName&大师傅&phoneNumber&13688882277&warnSecond']

    b1 = re.findall(r'(.*)师傅', str1)
    print(b1)  # ['pk_Id&0&secondName&近来可好&userName&大']

    c1 = re.findall(r'(.*?)大师傅.*', str1)
    print(c1)  # ['pk_Id&0&secondName&近来可好&userName&']


def test5():
    str1 = 'pk_Id&0&secondName&近来可好&userName&大师傅&phoneNumber&13688882277&warnSecondBalance&88&powers&101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701&transportNum&0&smsNumber&0&isSmS&1&isRelevance&1&exCompanyJson&[]&addUser&b5075cb063b941c186c6daaae08e1c2f&companyCode&c8e405c097a3463ba27ee83cadd9dce5&'
    '''
    1、re.findall() —— 匹配的结果是列表
    2、r'(.*)Balance(.*)102' —— 以【Balance】进行分割：
    1）前一部分 —— pk_Id&0&secondName&近来可好&userName&大师傅&phoneNumber&13688882277&warnSecond
    2）后一部分 —— &88&powers&101,104,【解析：(.*)102 的意思是匹配102之前，Balance之后的任意字符部分】
    '''
    a = re.findall(r'(.*)Balance(.*)102', str1, re.M | re.I)
    print(a)  # [('pk_Id&0&secondName&近来可好&userName&大师傅&phoneNumber&13688882277&warnSecond', '&88&powers&101,104,')]


def test6():
    # re.search() 函数用于在字符串中查找匹配的第一个子串，并返回一个匹配对象
    str1 = 'pk_IdsecondNameuserNamephoneNumberwarnSecondBalancepowerstransportNumsmsNumberisSmSisRelevanceexCompanyJsonaddUsercompanyCode'
    a = re.search(r'(.*)Name', str1, re.M | re.I)
    print(a)  # pk_IdsecondNameuserName
    # b=re.search(r'(.*)Name(.*)',str1,re.M | re.I)
    # print(b)#pk_IdsecondNameuserNamephoneNumberwarnSecondBalan
    # c = re.search(r'(.*)Name(.*)', str1, re.M | re.I)
    # print(c)  # pk_IdsecondNameuserNamephoneNumberwarnSecondBalan
    # re.findall()函数用于在字符串中查找所有匹配的子串，并返回一个包含所有匹配结果的列表
    d = re.findall(r'(.*)Na(.*)', str1, re.M | re.I)
    print(
        d)  # [('pk_IdsecondNameuserNamephoneNumberwarnSecondBalancepowerstransportNumsmsNumberisSmSisRelevanceexCompanyJso', 'ddUsercompanyCode')]
