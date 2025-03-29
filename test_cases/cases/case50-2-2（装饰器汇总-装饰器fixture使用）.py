#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/12/6 21:31
=================================================='''
import random

import pytest


@pytest.fixture()  # 装饰器
def test1():
    test3()  # case执行前执行
    yield  # 隔离的关键字
    print('结束')  # case执行后执行


def test3():
    print('开始')


'''
test1函数作为参数，传入测试用例test2中
'''


def test2(test1):
    char0 = '京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽赣粤青藏川宁琼'
    char1 = 'ABCDEFGHJKLMNPQRSTUVWXYZ'
    char2 = '1234567890ABCDEFGHJKLMNPQRSTUVWXYZ'
    len0 = len(char0) - 1
    len1 = len(char1) - 1

    code = ''
    index0 = random.randint(1, len0)
    index1 = random.randint(1, len1)
    code = code + char0[index0]
    code = code + char1[index1]

    for i in range(1, 6):
        code = code + char2[i]
    print(code)
