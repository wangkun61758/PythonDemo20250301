import os
import time
import unittest
from unittestreport import TestRunner
'''
目标2：执行多个文件夹下的不同脚本
（1）要满足的条件1：要执行的测试用例所在的文件夹中必须包含【__init__.py】
（2）要满足的条件2：top_level_dir：如果需要调用多次，且在不同目录下的话，需要手动给top_level_dir传值，将”根目录（测试用例所在目录的上级目录）“的值给此参数
资料地址：https://blog.csdn.net/weixin_30765319/article/details/96864801
解析：　discover 第三个参数 top_level_dir 第一次运行时如果为None 会取当前传入的start_dir所在路径为 top_level_dir，而top_level_dir会作为self的参数保存下来，这样第二次运行时 top_level_dir实际取的是上一次的路径，直接影响到了下一次的运行
（3）要运行的用例文件要按照规定的格式写，不然无法运行
a、脚本中的类要继承 unittest.TestCase，比如：class TestStringMethods(unittest.TestCase)
b、类中的函数要实例化使用self —— def test_isupper(self):
'''

def creatsuite():
    testunit = unittest.TestSuite()
    list_dir = os.listdir('D:/Python/PythonDemo20240331/test_cases/case49/tests')

    for i in list_dir:
        if os.path.isdir(i):#如果遍历到的i是目录
            print('目录')
        else:#如果遍历到的i是文件
            print('遍历到的是文件:'+str(i))#test1
            file_path='D:/Python/PythonDemo20240331/test_cases/case49/tests/'
            case_path=file_path+i
            print(case_path)#D:/Python/PythonDemo20240315/test_cases/case29-2（unittest+TestRunner-执行多文件夹）/cases/test1
            discover = unittest.defaultTestLoader.discover(str(case_path), pattern='a*.py', top_level_dir='D:/Python/PythonDemo20240331/test_cases/case49/tests/')
            testunit.addTests(discover)

    return testunit


if __name__ == "__main__":
    unit = creatsuite()

    now = time.strftime("%Y%m%d-%H-%M-%S")
    filename = 'case49测试报告' + now + '.html'

    report_dir = 'D:/Python/PythonDemo20240331/resources/reports/'
    runner = TestRunner(unit,
                        filename=filename,
                        report_dir=report_dir,
                        title='测试报告',
                        tester="wk",
                        desc='自动化测试')
    runner.run()
