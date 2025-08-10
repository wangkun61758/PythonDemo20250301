import os
import unittest

from fontTools.misc.cython import returns
from unittestreport import TestRunner
from datetime import datetime

'''
目标1：执行指定文件夹的脚本
1、unittest.defaultTestLoader.discover(str(case_dir), pattern='a*.py', top_level_dir=None)
（1）str(case_dir)—— 读取文件的路径
（2）pattern='a*.py'—— 读取文件路径下以 a开头的python文件（比如：a*.py）
 (3) top_level_dir=None：测试模块的顶层目录，如果没有顶层目录，默认为None；

2、要运行的用例文件要按照规定的格式写，不然无法运行
（1）脚本中的类要继承 unittest.TestCase，比如：class TestStringMethods(unittest.TestCase)
（2）类中的函数要实例化使用self —— def test_isupper(self):
'''
now = datetime.now()
time1 = now.strftime("%Y-%m-%d %H-%M-%S")
filename1 = time1 + '.html'


def suite():
    suite = unittest.TestSuite()
    cases = unittest.defaultTestLoader.discover(str('../../test_cases/cases'), pattern='*.py', top_level_dir=None)
    suite.addTests(cases)
    return suite


if __name__ == "__main__":
    unit = suite()
    runner = TestRunner(unit, filename=filename1, report_dir='../../resources/reports/', title='测试报告', tester="wk",
                        desc='自动化测试')
    runner.run()


