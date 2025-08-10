#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/2/7 23:01
=================================================='''
import json

'''
json.dump(dict_1, dump_f, ensure_ascii=False, indent=4)
ensure_ascii=False：输出原有的语言文字，可通过该参数实现中文写入。
indent：缩进量，一般省略(省略后的格式为整行展示，建议不省略)
'''


def test1():
    data = {"name": "Alice", "age": 30, "city": "New York"}
    data1 = json.dumps(data, ensure_ascii=False)  # # 将字典转换为JSON字符串
    print(data1, type(data1))  # {"name": "Alice", "age": 30, "city": "New York"} <class 'str'>

    # 假设有一个包含JSON类型数据的列表
    data = [{'name': 'wang', 'age': '16', 'weight': '168'}, {'name': 'liu', 'age': '26', 'weight': '170'}]
    # 使用json.dumps方法将列表转换为字符串形式
    data_str = json.dumps(data, ensure_ascii=False)
    print(data_str, type(
        data_str))  # [{"name": "wang", "age": "16", "weight": "168"}, {"name": "liu", "age": "26", "weight": "170"}] <class 'str'>

    data2 = json.loads(data1)  # # 从JSON字符串中解析数据
    print(data2, type(data2))  # {'name': 'Alice', 'age': 30, 'city': 'New York'} <class 'dict'>

    with open('../../resources/json/history.json', 'r') as f1:  # 所读取的Json文件中的键值对必须使用双引号“”
        data3 = json.load(f1)  # 从文件中读取JSON数据，并将其转换为Python对象（返回python对象，也即字典）
        print(
            data3)  # [{'success': 5, 'all': 5, 'fail': 0, 'skip': 0, 'error': 0, 'runtime': '0.00 S', 'begin_time': '2024-02-29 21:37:41', 'pass_rate': '100.00'}]

    list_data = [{'name': 'wang', 'age': '16', 'weight': '168'}, {'name': 'liu', 'age': '26', 'weight': '170'}]
    write_file = open('../../resources/json/json1.json', 'w', encoding='utf-8')
    json.dump(list_data, write_file, ensure_ascii=False)  # 将json信息写进文件


