#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/2/12 22:10
=================================================='''
import random

import pytest
import yaml
def load(path):
    try:
        file = open(path, 'r', encoding='utf-8')
        data = yaml.load(file, Loader=yaml.FullLoader)
        return data
    except UnicodeDecodeError:
        print("解码错误，尝试使用其他编码")
@pytest.mark.parametrize('datas', load('../../resources/yaml/station.yaml').values())
def test1(datas):
    print(datas)

@pytest.mark.run(order=1)
def test2():
    print('111111111111')

@pytest.mark.skipif(1==2,reason='没有原因的跳过')
def test1():
    print('打印没有原因的跳过')

@pytest.mark.skip(reason='没有原因的跳过')
def test2():
    print('打印没有原因的跳过')

@pytest.mark.skipif(1==2,reason='没有原因的跳过')
class Test():
    @pytest.mark.skipif(1 == 2, reason='没有原因的跳过')
    def test1(self):
        print('test1打印没有原因的跳过')

    @pytest.mark.skip(reason='没有原因的跳过')
    def test2(self):
        print('test2打印没有原因的跳过')

