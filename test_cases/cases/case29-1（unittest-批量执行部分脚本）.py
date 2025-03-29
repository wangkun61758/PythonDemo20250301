#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/2/13 12:19
=================================================='''
import unittest

def sunit():
    sunit=unittest.TestSuite()
    cases=unittest.defaultTestLoader.discover(str('../../test_cases/cases'),pattern='*.py',top_level_dir=None)
    sunit.run(cases)
    return sunit
