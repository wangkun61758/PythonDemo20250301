#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/3/21 19:48
=================================================='''
ENV = "demo"
BASE_URL = {
    "demo": "https://kyfw.12306.cn",
    "prod": "https://kyfw.12306.cn"
}[ENV]

def test():
    url=BASE_URL
    print(url)