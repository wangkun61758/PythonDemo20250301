#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/3/1 23:10
=================================================='''
import json
import os.path
import re
import unittest

import yaml
import jsonpath
class c(unittest.TestCase):
    def test1(self):
        json_data = '''
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
        if not os.path.exists('../../resources/test/'):
            os.makedirs('../../resources/test/')
        with open(os.path.join('../../resources/test/test1.yaml'), 'w', encoding='utf-8') as f:
            f.write(str(json_data))

        file1 = open('../../resources/test/test1.yaml', 'r', encoding='utf-8')
        data = yaml.load(file1, Loader=yaml.FullLoader)
        print(data)

        list1 = []
        list2 = []
        for key, value in data.items():
            list1.append(key)
            list2.append(value)

        dict1 = dict({list1[i]: list2[i] for i in range(len(list1))})
        print(dict1)

        a = jsonpath.jsonpath(dict1, '$..book[*].author')
        print(a)  # ['Nigel Rees', 'Evelyn Waugh', 'Herman Melville', 'J. R. R. Tolkien']
        b = json.dumps(dict1, ensure_ascii=False)
        c = re.findall(r'(.*)author(.*?)', b, re.M | re.I)
        print('c' + str(c))

if __name__ == '__main__':
    unittest.main()