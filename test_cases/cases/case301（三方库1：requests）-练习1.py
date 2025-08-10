#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/2/7 23:36
=================================================='''
import requests


def test1():
    response = requests.get('https://www.baidu.com/')
    if response.status_code == 200:
        print("Success!")
    else:
        print("Failed:", response.status_code)
    print(requests.head('https://www.baidu.com/'))
