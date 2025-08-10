#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/4/8 23:10
=================================================='''

import unittest
from unittestreport import TestRunner
from datetime import datetime

filename1 = datetime.now().strftime("%Y-%m-%d %H-%M-%S") + '.html'

def suite():
    suite = unittest.TestSuite()
    cases = unittest.defaultTestLoader.discover(str('../report/'), pattern='*.py', top_level_dir=None)
    suite.addTests(cases)
    return suite

if __name__ == "__main__":
    unit = suite()
    runner = TestRunner(unit, filename=filename1, report_dir='../report/', title='测试报告', tester="wk",
                        desc='自动化测试')
    runner.run()
