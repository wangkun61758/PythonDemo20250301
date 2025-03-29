#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/10/19 20:49
=================================================='''
import pytest

#https://blog.csdn.net/weixin_48776531/article/details/135028480
def setup_module():#在当前测试模块开始执行前调用一次。通常用于设置全局测试环境
    print('开始（类外面）-模块级别-最先执行')
def teardown_module():  # 在当前测试模块执行完后调用一次。通常用于清理全局测试环境
    print('结束（类外面））-模块级别-最后执行')

def setup_function():
    print('函数级别：setup_function-不在类中的方法-类外的函数执行前执行')
def teardown_function():
    print('函数级别：teardown_function-不在类中的方法-类外的函数执行后执行')
def test1():
    print('类外的测试函数')

class Test:
    def setup_class(self):
        print('开始1（类内）-setup_class:类方法之前执行-多个setup_class仅执行最后一个')
    def teardown_class(self):
        print('结束1（类内）-teardown_class:类方法之后执行-多个teardown_class仅执行最后一个')
    def test1(self):
        print('函数1')
    # def setup_class(self):
    #     print('开始2（类内）-setup_class:类方法之前执行-多个setup_class仅执行最后一个')
    # def teardown_class(self):
    #     print('结束2（类内）-teardown_class:类方法之后执行-多个teardown_class仅执行最后一个')
    def test2(self):
        print('函数2')
    def test3(self):
        print('函数3')
    def setup_method(self):
        print('在每个测试类中的每个测试方法运行前调用一次。通常用于设置方法级别的测试环境')
    def teardown_method(self):
        print('在每个测试类中的每个测试方法运行后调用一次。通常用于清理方法级别的测试环境')


# if __name__ == '__main__':
#
#     pytest.main(['-v', '-s'])
