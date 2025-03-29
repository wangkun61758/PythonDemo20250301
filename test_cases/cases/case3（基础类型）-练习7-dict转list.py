#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/10/12 16:11
=================================================='''
import json


def test1():
    js = '''
        {
        "store": {
            "book": [
                {
                    "category": "reference", 
                    "author": "Nigel Rees", 
                    "title": "Sayings of the Century", 
                    "price": 8.95
                }, 
                {
                    "category": "fiction", 
                    "author": "Evelyn Waugh", 
                    "title": "Sword of Honour", 
                    "price": 12.99
                }, 
                {
                    "category": "fiction", 
                    "author": "Herman Melville", 
                    "title": "Moby Dick", 
                    "isbn": "0-553-21311-3", 
                    "price": 8.99
                }, 
                {
                    "category": "fiction", 
                    "author": "J. R. R. Tolkien", 
                    "title": "The Lord of the Rings", 
                    "isbn": "0-395-19395-8", 
                    "price": 22.99
                }
            ], 
            "bicycle": {
                "color": "red", 
                "price": 19.95
            },
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
    js_data = json.loads(js)
    a = dict((k, v) for k, v in js_data.items())
    print(a)


def test2():
    dit2 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
    result = []
    for k, v in dit2.items():
        result.append(k)
        result.append(v)
    print(result)  # ['Name', 'Runoob', 'Age', 7, 'Class', 'First']


def test3():
    dit3 = {'Name': 'Runoob', 'Age': 7, 'Class': {'name': '韩梅梅', 'age': 55, 'sex': 'male'}}
    result = []
    for k, v in dit3.items():
        result.append(k)
        result.append(v)
    print(result)  # ['Name', 'Runoob', 'Age', 7, 'Class', {'name': '韩梅梅', 'age': 55, 'sex': 'male'}]


def test4():
    dit4 = {'Name': 'Runoob', 'Age': 7,
            'Class': [{'name': '韩梅梅', 'age': 55, 'sex': 'male'}, {'name': '李磊', 'age': 885, 'sex': 'male'}]}
    result = []
    for k, v in dit4.items():
        result.append(k)
        result.append(v)
    print(
        result)  # ['Name', 'Runoob', 'Age', 7, 'Class', [{'name': '韩梅梅', 'age': 55, 'sex': 'male'}, {'name': '李磊', 'age': 885, 'sex': 'male'}]]
