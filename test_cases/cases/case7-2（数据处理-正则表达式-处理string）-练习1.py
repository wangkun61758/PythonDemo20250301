#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/11/4 14:05
=================================================='''
import re

def test():
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


def test1():
    str1 = 'pk_Id&Name&近来可好&userNamelileiisdog'
    a=re.findall(r'(.*)Name',str1,re.M|re.I)#['pk_Id&Name&近来可好&user']
    print(a)

    b=re.match(r'p(.*)Name',str1,re.M|re.I)#'pk_Id&Name&近来可好&userName'
    print(b)

    c=re.search(r'p(.*)Name',str1,re.M|re.I)#'pk_Id&Name&近来可好&userName'
    print(c)