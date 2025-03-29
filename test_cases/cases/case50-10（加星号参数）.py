#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/7/8 22:25
=================================================='''
'''
加了星号 * 的参数会以元组(tuple)的形式导入
'''
def greetPerson(*name):
    print('Hello', name)#Hello ('Runoob', 'Google', 'beijing')
greetPerson('Runoob', 'Google', 'beijing')

