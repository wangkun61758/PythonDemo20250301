#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/2/7 23:01
=================================================='''
import json


def test1():
    data = {"name": "Alice", "age": 30, "city": "New York"}
    data1 = json.dumps(data,ensure_ascii=False)  # # 将字典转换为JSON字符串
    print(data1, type(data1))  # {"name": "Alice", "age": 30, "city": "New York"} <class 'str'>

    # 假设有一个包含JSON类型数据的列表
    data = [{'name': 'wang', 'age': '16', 'weight': '168'}, {'name': 'liu', 'age': '26', 'weight': '170'}]
    # 使用json.dumps方法将列表转换为字符串形式
    data_str = json.dumps(data,ensure_ascii=False)
    print(data_str,type(data_str))#[{"name": "wang", "age": "16", "weight": "168"}, {"name": "liu", "age": "26", "weight": "170"}] <class 'str'>


    data2 = json.loads(data1)  # # 从JSON字符串中解析数据
    print(data2, type(data2))  # {'name': 'Alice', 'age': 30, 'city': 'New York'} <class 'dict'>

    with open('../../resources/json/history.json', 'r') as f1:#所读取的Json文件中的键值对必须使用双引号“”
        data3=json.load(f1)#从文件中读取JSON数据，并将其转换为Python对象（返回python对象，也即字典）
        print(data3)#[{'success': 5, 'all': 5, 'fail': 0, 'skip': 0, 'error': 0, 'runtime': '0.00 S', 'begin_time': '2024-02-29 21:37:41', 'pass_rate': '100.00'}]

    list_data = [{'name': 'wang', 'age': '16', 'weight': '168'}, {'name': 'liu', 'age': '26', 'weight': '170'}]
    write_file=open('../../resources/json/json1.json', 'w', encoding='utf-8')
    json.dump(list_data,write_file,ensure_ascii=False)#将json信息写进文件


def test2():
    # 将字典转换为JSON字符串
    data = {"name": "Alice", "age": 30, "city": "New York"}
    json_data = json.dumps(data)  # 将字典转换为JSON字符串
    print(f"JSON string: {json_data}")

    json_data2 = json.dumps(data)
    print(f'Json string:{json_data2}')

    json_data3 = json.dumps(data)
    print(f"JSON string: {json_data3}")

    json_data4 = json.dumps(data)
    print(f'Json string:{json_data4}')
    json_data5 = json.dumps(data)
    print(f'{json_data5}')

    parsed_data = json.loads(json_data)  # 从JSON字符串中解析数据
    print(f'Parsed Data:{parsed_data} ')

    parsed_data2 = json.loads(json_data)
    print(f'{parsed_data2}')

    parsed_data3 = json.loads(json_data)
    print(f'{parsed_data3}')

    parsed_data4 = json.loads(json_data)
    print(f'{parsed_data4}')

    parsed_data5 = json.loads(json_data)
    print(f'{parsed_data5}')

def test3():
    dit1={'name':'lilei','age':22,'city':'阜阳'}
    a=json.dumps(dit1)
    print(a,type(a))

    b=json.loads(a)
    print(b,type(b))

    with open('../../resources/history.json', 'r', encoding='utf-8') as file1:
        c=json.load(file1)
        print(c)
    file2=open('../../resources/history.json', 'w', encoding='utf-8')
    json.dump(dit1,file2)

def test4():
    dit1 = {'name': 'lilei', 'age': 22, 'city': '阜阳'}
    a=json.dumps(dit1, ensure_ascii=False)
    print(a)#{"name": "lilei", "age": 22, "city": "阜阳"}
    b=json.loads(a)
    print(b)#{'name': 'lilei', 'age': 22, 'city': '阜阳'}

    with open('../../resources/history.json', 'r', encoding='utf-8') as file1:
        c=json.load(file1)##从文件中读取JSON数据，并将其转换为Python对象

    json.dump(dit1,open('../../resources/history.json', 'w', encoding='utf-8'),ensure_ascii=False)


