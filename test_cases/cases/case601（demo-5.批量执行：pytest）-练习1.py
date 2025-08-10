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

report_name='pytest—'+datetime.now().strftime('%Y-%m-%d %H-%M-%S')+'.html'
def suite():
    suite=unittest.TestSuite()
    cases=unittest.defaultTestLoader.discover('../../test_cases/cases/tests_pytest',pattern='*.py')
    suite.addTests(cases)
    return suite
if __name__ == '__main__':
    suite=suite()
    runner=TestRunner(suite,filename=report_name,report_dir='../../resources/reports/',title='测试报告',tester='wk')
    runner.run()