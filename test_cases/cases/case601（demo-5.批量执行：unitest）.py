#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/4/2 11:37
=================================================='''
import datetime
import os
import unittest
from datetime import datetime

from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner

'''
测试类必须以Test开头，且必须继承unittest.TestCase，只有继承unittest.TestCase的类才会被识别为测试类（否则会被忽略执行）
测试函数必须以test_开头（即测试类中的测试函数必须以test_前缀命名，否则会被忽略执行）
class Test(unittest.TestCase):
    def test_1(self):
        print("test1")
        assert 1 == 1
if __name__ == '__main__':
    Test().test_1()

'''
path = '../../test_cases/cases/tests_unitest'
report_name = 'unitest—' + datetime.now().strftime("%Y-%m-%d %H-%M-%S") + '.html'
report_path = '../../resources/reports'+'/'+report_name

def run():
    cases = unittest.defaultTestLoader.discover(path, pattern='*.py')

    with open(report_path, 'w', encoding='utf-8') as f:
        runner = HTMLTestRunner(stream=f, title='测试报告')
        runner.run(cases)
run()