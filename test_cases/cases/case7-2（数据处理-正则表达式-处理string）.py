#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/7/6 21:03
=================================================='''
import re

'''
1)  1、re.match(r'a(.*)b',str1,re.M|re.I) 匹配结果是对象。且包括 a，b
    2、从字符串的起始位置开始匹配，如果匹配不到则返回NONE
2) 1、re.search(r'a(.*)b',str1,re.M|re.I) 匹配结果是对象。且包括 a，b
    2、不需要从字符串的起始位置开始匹配
3) 1、re.findall(r'a(.*)b',str1,re.M|re.I) 匹配结果是列表。且不包括 a，b
    2、匹配整个字符串，直到字符串的末尾
4) .* —— 表示匹配多个任意【字符串】
5) .*? 
re.match/re.search —— 匹配第一个符合条件的
re.findall —— 匹配多个对象放入list
6) \d+ —— 匹配多个任意数字【\d匹配任意数字，等价于 [0-9]】
\d{2} —— 匹配2个数字
7) re.M：多行匹配 / re.I：使匹配对大小写不敏感
'''


def test1():
    line = "Cats are so smarter than dogs"
    matchObj1 = re.match(r'(.*) are (.*?) ', line,
                         re.M | re.I)  # 第一个.* 表示匹配任何单个或多个【字符】：对应Cats/ (.*?) 只保存第一个匹配到的【字符串】：对应so
    print(matchObj1)  # 'Cats are so
    matchObj2 = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
    print(matchObj2)  # Cats are so smarter than dogs
    if matchObj2:
        print("matchObj.group() : ", matchObj2.group())  # Cats are so smarter than dogs【group()匹配的整体】
        print("matchObj.group(1) : ", matchObj2.group(1))  # Cats【group(1) 列出第一个括号匹配部分】
        print("matchObj.group(2) : ", matchObj2.group(2))  # so【 group(2) 列出第二个括号匹配部分】
    else:
        print("No match!!")

    str1 = 'pk_Id&0&secondName&近来可好&userName&大师傅&phoneNumber&13688882277&warnSecondBalance&88&powers&101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701&transportNum&0&smsNumber&0&isSmS&1&isRelevance&1&exCompanyJson&[]&addUser&b5075cb063b941c186c6daaae08e1c2f&companyCode&c8e405c097a3463ba27ee83cadd9dce5&'
    '''
    1、r'(.*)Balance(.*)102' —— 以【Balance】进行分割：
    2）前一部分 —— pk_Id&0&secondName&近来可好&userName&大师傅&phoneNumber&13688882277&warnSecond
    3）后一部分 —— &88&powers&101,104,【解析：(.*)102 的意思是匹配102之前，Balance之后的任意字符部分】
    '''
    a = re.findall(r'(.*)Balance(.*)102', str1, re.M | re.I)
    print(a)  # [('pk_Id&0&secondName&近来可好&userName&大师傅&phoneNumber&13688882277&warnSecond', '&88&powers&101,104,')]


