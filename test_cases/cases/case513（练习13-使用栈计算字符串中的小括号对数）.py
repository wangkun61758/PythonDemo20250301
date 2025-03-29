#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/2/17 23:15
=================================================='''

def test1():
    str1='h)jjk(dssd))(((aaj2450dg)(jnvds346h))'
    list = []
    count = 0
    for i in str1:
        if i == '(':
            list.append(i)
        elif i == ')':
            if list:#栈不为空
                list.pop()
                count += 1
            else:
                print('栈为空')
    print(count)