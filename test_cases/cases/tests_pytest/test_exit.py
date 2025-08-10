#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/2/13 0:21
=================================================='''
import unittest


class Test():
    def test_1(self):
        print("test1")
        assert 1 == 1

    def test_2(self):
        print("test2")
        assert 1 == 1
if __name__ == '__main__':
    Test().test_2()
    Test().test_1()