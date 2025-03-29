#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/10/9 18:50
=================================================='''
import pytest
from numpy.ma.testutils import assert_equal
'''
总结：多个断言，有一个失败，后面的程序不再执行
'''
@pytest.mark.parametrize(('x', 'y'), [(1, 1), (2, 2), (3, 3), (4, 4)])
def test_simple(x, y):
    print("测试数据x:{},y:{}".format(x, y))  # 测试数据x:1,y:1
    assert x == y
    assert x + y > 1
    assert x > 0
    print('结束')

def test1():
    #1、判断 “预期值” 和 “实际值” 是否相等
    list1 = [100, 200]
    assert_equal(list1[0], 100)  # first‌：第一个值，是被比较的值/second‌：第二个值，是用来比较的值/msg‌：可选参数，用于在断言失败时显示的自定义错误消息

    #2、 判断 “预期值” 的类型
    assert isinstance(list1, list)

    #3、比较两个值的大小
    assert 3 > 2

    #4、判断值不为空
    assert  list1 !=[]

