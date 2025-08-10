#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/2/12 22:35
=================================================='''
import random
import string


def test1():
    str1 = 'lilei hameimei wangwu zhagnsan lisi zhaoer'
    count1 = str1.count(' ')  # 计算字符串中某个值出现的次数
    list1 = str1.split(' ', count1)  # 使用' '分割字符串，count1为分割的次数，并且返回分割后字符串组成的列表
    list1.sort()  # 列表重新排序
    list1.sort(key=lambda x: x[-1])  # 按单词最后一个字母排序（原地排序，不生成新的）

    print(str1[1:7])  # 打印指定位置的值：ilei h
    print(str1[0:-1])  # 输出第一个到倒数第二个的所有字符（左闭右开，-1为最后一个数字的位置，由于是右开，所以截取不到最后一个数字）

    str2 = ' lilei hameimei wangwu zhagnsan lisi zhaoer '
    print(str2, str2.strip())  # 返回移除字符串两端空白字符的副本(不能处理字符串中间的空格)
    print(str1.replace('h', 'H'))  # 返回字符串中所有h子串被H替换后的字符串
    print(str1.upper())  # 返回大写形式的字符串
    print(str1.lower())  # 返回小写形式的字符串

    print(str1.find('e'))  # 位置是3
    print(str1.find('ha', 0, len(str1) - 1))  # 查询字符串中是否含有目标字符或子串，如果含有则返回第一个查询到的位置序号，否则返回-1(位置是2)
    print(str1.startswith('li', 0, len(str1) - 1))  # 检查字符串是否以指定前缀开始(True)
    print(str1.endswith('er', 0, len(str1)))  # 检查字符串是否以指定后缀结束(True)

    str3 = 'lilei hameimei wangwu zhagnsan lisi zhaoer'
    str4 = str3.replace(' ', '')
    if str4.isdigit():  # 如果字符串只包含数字则返回True
        print('都是数字')
    elif str4.isalpha():  # 如果字符串至少有一个字符并且所有字符都是字母则返回True
        print('字符串至少有一个字符并且所有字符都是字母')
    else:
        print('上面两种情况都不是')

    s = 'hello world'
    print(s[::-1])  # 按照从右到左，每次步长为1地截取（-1代表按步长1反向截取）

    '''
    [:]截取全部的字符
    [1：4]截取下标1到3的字符
    [1:16:-3]截取下标1到15的字符，按步长3截取，且是反向输出
    '''
    l = 'hello world'
    print(l[::1])  # 按照从左到右，每次步长为1地截取（1代表按步长1正向截取）

    phoneNum = '135' + ''.join(random.choice(string.digits) for _ in range(8))
    print(phoneNum)
