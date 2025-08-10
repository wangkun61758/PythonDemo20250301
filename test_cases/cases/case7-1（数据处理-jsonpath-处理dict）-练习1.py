#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/11/4 14:40
=================================================='''
import json

import jsonpath
import yaml


def test1():
    str1 = '''
        {
        "store": {
            "book": [
                {
                    "category": "reference", 
                    "price": 8.95
                }, 
                {
                    "category": "fiction", 
                    "price": 22.99
                }
            ], 
             "car": {
                "color": "blue", 
                "price": 155
            },
            "truck": {
                "color": "white", 
                "price": 999,
                "owner": ["马云", "史玉柱", "马化腾", "王健林", "董明珠", "雷军"]
            }

        }
    }
        '''
    dict1=json.loads(str1)
    print(dict1)
    a=jsonpath.jsonpath(dict1,'$..book[*].price')
    print(a)
    b=jsonpath.jsonpath(dict1,'$..car.color')
    print(b)
