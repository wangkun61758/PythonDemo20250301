#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/4/2 11:37
=================================================='''
'''
1.创建目录：创建要执行的脚本所在的目录（脚本所在的目录命名无要求）
  编写脚本：编写要执行的测试脚本（测试脚本必须以test_开头 / 测试函数必须以test_开头【测试函数无需放在以Test开头的类中，测试类也无需继承unittest.TestCase】）
  class Test:
    def test_1(self):
        print("test1")
        assert 1 == 1
    if __name__ == '__main__':
        Test().test_2()
  或
  def test_1():
    print("test1")
    assert 1==1
    

注意：ini文件只能放在根目录下，不然执行main函数会报错
2.在ini中，设置main函数要执行的测试用例的路径
#执行以 tests_unitest 开头的测试用例
testpaths =./test_cases/cases/tests_ini #测试用例的路径

3.执行main函数（main会根据ini中的设置执行指定路径下的测试用例）
if __name__ == '__main__':
    pytest.main()
    
4.在ini中，设置测试报告的存放路径及测试报告名称
#-s -v --html=路径/文件名.html（-s：输出调试信息，-v：显示更详细的信息）
addopts = -s -v --html=./resources/reports/main_ini_report.html
'''
