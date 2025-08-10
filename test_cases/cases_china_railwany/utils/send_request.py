#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/4/3 23:15
=================================================='''

import requests
from test_cases.cases_china_railwany.config import global_config
from test_cases.cases_china_railwany.utils.get_url_data import get_url_data

'''
1、类外的叫函数，由def()关键字定义
2、类内的叫方法
（2.1）静态方法不需要实例化，直接类名.方法名()调用，静态方法对类一无所知，只处理参数
（2.2）类方法：不需要实例化，直接类名.方法名()调用，类方法适用于类
（2.3）实例方法：由def()定义，定义的方法默认在括号里面加一个self参数，self 是类本身的实例对象。在调用的时候，需要先进行实例化
'''

class HttpUtils:
    def send_request(interface, method, headers, data):
        payload = get_url_data()
        url = str(global_config.BASE_URL) + interface + '?' + str(payload)
        headers = headers or global_config.HEADERS
        try:
            res = requests.request(method=method, url=url, headers=headers, data=data)
            return res.json(), res.status_code
        except Exception as e:
            return {'error': str(e)}, 500
