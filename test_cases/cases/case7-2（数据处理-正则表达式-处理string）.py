#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/7/6 21:03
=================================================='''
import re

'''
1)  1、re.match(r'a(.*)b',str1,re.M|re.I) 匹配结果是对象。，且包括 a，b
    2、从字符串的起始位置开始匹配，如果匹配不到则返回NONE
2) 1、re.search(r'a(.*)b',str1,re.M|re.I) 匹配结果是对象。，且包括 a，b
    2、不需要从字符串的起始位置开始匹配
3) 1、re.findall(r'a(.*)b',str1,re.M|re.I) 匹配结果是列表，且不包括 a，b
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
    matchObj1 = re.match(r'(.*) are (.*?) ', line,re.M | re.I)  # 第一个.* 表示匹配任何单个或多个【字符】：对应Cats/ (.*?) 只保存第一个匹配到的【字符串】：对应so
    print(matchObj1)  # 'Cats are so
    matchObj2 = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
    print(matchObj2)  # Cats are so smarter than dogs
    if matchObj2:
        print("matchObj.group() : ", matchObj2.group())  # Cats are so smarter than dogs【group()匹配的整体】
        print("matchObj.group(1) : ", matchObj2.group(1))  # Cats【group(1) 列出第一个括号匹配部分】
        print("matchObj.group(2) : ", matchObj2.group(2))  # so【 group(2) 列出第二个括号匹配部分】
    else:print("No match!!")

    str1 = 'pk_Id&0&secondName&近来可好&userName&大师傅&phoneNumber&13688882277&warnSecondBalance&88&powers&101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701&transportNum&0&smsNumber&0&isSmS&1&isRelevance&1&exCompanyJson&[]&addUser&b5075cb063b941c186c6daaae08e1c2f&companyCode&c8e405c097a3463ba27ee83cadd9dce5&'
    '''
    1、r'(.*)Balance(.*)102' —— 以【Balance】进行分割：
    2）前一部分 —— pk_Id&0&secondName&近来可好&userName&大师傅&phoneNumber&13688882277&warnSecond
    3）后一部分 —— &88&powers&101,104,【解析：(.*)102 的意思是匹配102之前，Balance之后的任意字符部分】
    '''
    a = re.findall(r'(.*)Balance(.*)102', str1, re.M | re.I)
    print(a)  # [('pk_Id&0&secondName&近来可好&userName&大师傅&phoneNumber&13688882277&warnSecond', '&88&powers&101,104,')]
def test2():
    line = 'xx你好xx11111xx新世界xx22222xx哈哈xx11'
    matchObj2 = re.match(r'xx(.*)xx', line, re.M | re.I)  # 使用“.*”表达式，则表示贪婪匹配，则返回去掉头尾xx 之间的全部数据
    print(matchObj2)  # <re.Match object; span=(0, 29), match='xx你好xx11111xx新世界xx22222xx哈哈xx'>

    if matchObj2:
        print(matchObj2.group())  # xx你好xx11111xx新世界xx22222xx哈哈xx
        print(matchObj2.group(1))  # 你好xx11111xx新世界xx22222xx哈哈
    else:
        print("No match!!")
def test3():
    str = 'pk_Id0secondName近来可好userName大师傅phoneNumber13688882277warnSecondBalance88powers101,104,102,110,109,1061,201,202,203'
    stt11 = re.search(r'user(.*)', str)
    print(stt11)  # <re.Match object; span=(20, 114), match='userName大师傅phoneNumber13688882277warnSecondBalanc>

    s2 = re.search(r'user(.*)', str).span()
    print(s2)  # (20, 114)
def test4():
    pattern = r'apple'
    text = "I have an apples and a banana. apple"

    # 在文本中查找第一个匹配的子串
    match = re.search(pattern, text)

    if match:
        print("Found:", match.group())  # 获取匹配的子串#apple
        print("Start:", match.start())  # 获取匹配的起始位置#Start: 10
        print("End:", match.end())  # 获取匹配的结束位置#End: 15

    else:
        print("No match found.")

    match1 = re.findall(r'apple', text)
    print(match1)  # ['apple', 'apple']
    print(match1[0])  # apple
def test5():
    '''
    \d匹配任意数字，等价于 [0-9].
    +匹配一个及以上
    :return:
    '''
    pattern = r'\d+'  # 匹配一个或多个数字
    text = "I have 35 apples and 5 bananas. Total 8 fruits."

    # 查找所有匹配的子串
    matches = re.findall(pattern, text)

    if matches:
        print("Matches:", matches)  # 获取所有匹配的子串列表#['35', '5', '8']
    else:
        print("No matches found.")

    pattern1 = r'.*'
    matches1 = re.findall(pattern1, text)
    print(matches1)  # ['I have 35 apples and 5 bananas. Total 8 fruits.', '']

    matches2 = re.findall(r'.*?', text)
    # ['', 'I', '', ' ', '', 'h', '', 'a', '', 'v', '', 'e', '', ' ', '', '3', '', '5', '', ' ', '', 'a', '', 'p', '', 'p', '', 'l', '', 'e', '', 's', '', ' ', '', 'a', '', 'n', '', 'd', '', ' ', '', '5', '', ' ', '', 'b', '', 'a', '', 'n', '', 'a', '', 'n', '', 'a', '', 's', '', '.', '', ' ', '', 'T', '', 'o', '', 't', '', 'a', '', 'l', '', ' ', '', '8', '', ' ', '', 'f', '', 'r', '', 'u', '', 'i', '', 't', '', 's', '', '.', '']
    print(matches2)

    print(re.findall(r'I.*s', text))  # ['I have 35 apples and 5 bananas. Total 8 fruits']
    print(re.search(r'I.*s', text).group())  # I have 35 apples and 5 bananas. Total 8 fruits
    print(re.search(r'I.*s',
                    text))  # <re.Match object; span=(0, 46), match='I have 35 apples and 5 bananas. Total 8 fruits'>
def test6():
    pattern = r'\d{2}-\d{2}-\d{4}'  # 匹配日期格式：dd-mm-yyyy
    text = "Today's date is 31-08-2023."

    match = re.search(pattern, text)

    if match:
        print("Date found:", match.group())  # 31-08-2023
    else:
        print("No date found.")
def test7():
    '''
    1、\S —— 匹配任意非空字符
    2、\S+ —— 匹配多个任意非空字符（+ —— 匹配一个或多个）
    3、？—— 匹配0个或1个字符
    :return:
    '''
    pattern = r'httpsa?://\S+'  # 匹配HTTP或HTTPS链接
    text = "Here are some links: httpsa://www.example.com and https://google.com"

    links = re.findall(pattern, text)

    if links:
        print("Links found:", links)  # ['httpsa://www.example.com', 'https://google.com']
    else:
        print("No links found.")
def test8():
    '''
    1、\S —— 匹配任意非空字符
    2、\S+ —— 匹配多个任意非空字符（+ —— 匹配一个或多个）
    3、？—— 匹配0个或1个字符
    :return:
    '''
    pattern = r'hta?:\S+'
    text = "Here are some links: hta://www.example.com and ht://google.com and ht://google.com"

    links = re.findall(pattern, text)

    if links:
        print("Links found:", links)  # ['hta://www.example.com', 'ht://google.com']
    else:
        print("No links found.")
def test9():
    str1 = 'pk_Id&0&secondName&近来可好&userName&大师傅&phoneNumber&13688882277&warnSecondBalance&88&powers&101,104,102,110,109,1061,201,202,203,301,302,303,315,304,306,307,308,310,501,503,504,601,701&transportNum&0&smsNumber&0&isSmS&1&isRelevance&1&exCompanyJson&[]&addUser&b5075cb063b941c186c6daaae08e1c2f&companyCode&c8e405c097a3463ba27ee83cadd9dce5&'
    '''
    1、re.findall() —— 匹配的结果是列表
    2、r'(.*)Balance(.*)102' —— 以【Balance】进行分割：
    1）前一部分 —— pk_Id&0&secondName&近来可好&userName&大师傅&phoneNumber&13688882277&warnSecond
    2）后一部分 —— &88&powers&101,104,【解析：(.*)102 的意思是匹配102之前，Balance之后的任意字符部分】
    '''
    a = re.findall(r'(.*)Balance(.*)102', str1, re.M | re.I)
    print(a)  # [('pk_Id&0&secondName&近来可好&userName&大师傅&phoneNumber&13688882277&warnSecond', '&88&powers&101,104,')]

    a1 = re.findall(r'.*Balance', str1, re.M | re.I)
    print(a1)  # ['pk_Id&0&secondName&近来可好&userName&大师傅&phoneNumber&13688882277&warnSecondBalance']

    a2 = re.findall(r'(.*)Balance', str1, re.M | re.I)
    print(a2)  # ['pk_Id&0&secondName&近来可好&userName&大师傅&phoneNumber&13688882277&warnSecond']
def test10():
    str1 = 'a123b346b789b'
    a = re.findall(r'a(.*)b', str1, re.I)
    print(a)  # ['123b346b789']

    b = re.findall(r'a(.*?)b', str1)  # ？——最多只匹配一个
    print(b)  # ['123']

    c = re.findall(r'a(.+)b', str1)
    print(c)  # ['123b346b789']

    d = re.findall(r'\d', str1)
    print(d)  # ['1', '2', '3', '3', '4', '6', '7', '8', '9']

    e = re.findall(r'\D', str1)
    print(e)  # ['a', 'b', 'b', 'b']
def test11():
    str1 = 'a123b346b789b'
    a=re.findall(r'b(.*)b',str1,re.M|re.I)#['346b789']
    print(a)
def test12():
    str1 = 'a123b346b'
    a1=re.findall(r'a(.*)b',str1,re.M|re.I)
    a2=re.findall(r'a(.*?)b',str1,re.M|re.I)
    b1=re.findall(r'\d',str1)#['1', '2', '3', '3', '4', '6']
    print(b1)
    b2=re.findall(r'\D',str1)#['a', 'b', 'b']
    print(b2)
'''
练习：2025/3/20（1）
'''
def test13():
    '''
    1、re.findall(r'a(.*)b',str1,re.M|re.I) 匹配结果是列表，且不包括 a，b
    2、匹配整个字符串，直到字符串的末尾
    :return:
    '''
    str1 = 'a123b3467878hba123b346bhhjkla123b346b'
    a1=re.findall(r'a(.*)b',str1,re.M|re.I)
    print(a1)#['123b3467878hba123b346bhhjkla123b346']
    # a2=re.findall(r'a(.*?)b',str1,re.M|re.I)
    # print(a2)#['123', '123', '123']
    a3=re.findall(r'a(.*)b34678',str1,re.M|re.I)
    print(a3)#['123']

    '''
    1、re.match(r'a(.*)b',str1,re.M|re.I) 匹配结果是对象。，且包括 a，b
    2、从字符串的起始位置开始匹配，如果匹配不到则返回NONE
    :return:
    '''
    c1=re.match(r'a(.*)b',str1,re.M|re.I)
    print(c1)#<re.Match object; span=(0, 37), match='a123b3467878hba123b346bhhjkla123b346b'>
    # c2 = re.match(r'a(.*?)b', str1, re.M | re.I)
    # print(c2)  # <re.Match object; span=(0, 5), match='a123b'>
    c3=re.match(r'a(.*)b34678',str1,re.M|re.I)
    print(c3)#<re.Match object; span=(0, 10), match='a123b34678'>
    c4=re.match(r'46b(.*)123',str1,re.M|re.I)
    print(c4)#None

    '''
    1、re.search(r'a(.*)b',str1,re.M|re.I) 匹配结果是对象。，且包括 a，b
    2、不需要从字符串的起始位置开始匹配
    :return:
    '''
    d1=re.search(r'a(.*)b',str1,re.M|re.I)
    print(d1)#<re.Match object; span=(0, 37), match='a123b3467878hba123b346bhhjkla123b346b'>
    # d2 = re.search(r'a(.*?)b', str1, re.M | re.I)
    # print(d2)  # <re.Match object; span=(0, 5), match='a123b'>
    d3=re.search(r'a(.*)b34678',str1,re.M|re.I)
    print(d3)#<re.Match object; span=(0, 10), match='a123b34678'>
    d4=re.search(r'46b(.*)123',str1,re.M|re.I)
    print(d4)#<re.Match object; span=(20, 32), match='46bhhjkla123'>



