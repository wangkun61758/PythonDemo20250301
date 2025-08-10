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

path = '../../test_cases/cases/tests_unitest'
report_name = 'unitest—' + datetime.now().strftime("%Y-%m-%d %H-%M-%S") + '.html'
report_path = '../../resources/reports'+'/'+report_name

def run():
    cases = unittest.defaultTestLoader.discover(path, pattern='*.py')

    with open(report_path, 'w', encoding='utf-8') as f:
        runner = HTMLTestRunner(stream=f, title='测试报告')
        runner.run(cases)
run()