#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/4/2 11:37
=================================================='''
import unittest
from datetime import datetime

from unittestreport import TestRunner

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
report_name = 'pytest—' + datetime.now().strftime('%Y-%m-%d %H-%M-%S') + '.html'


def suite():
    suite = unittest.TestSuite()
    cases = unittest.defaultTestLoader.discover('../../test_cases/cases/tests_pytest', pattern='*.py')
    suite.addTests(cases)
    return suite


if __name__ == '__main__':
    suite = suite()
    runner = TestRunner(suite, filename=report_name, report_dir='../../resources/reports/', title='测试报告', tester='wk')
    runner.run()
