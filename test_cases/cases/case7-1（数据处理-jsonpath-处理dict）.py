#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/10/12 13:16
=================================================='''
import json
import jsonpath
'''
1、$ ——根节点
2、@  ——当前节点
3、*  ——匹配所有节点
4、?()  ——支持过滤操作
5、.. ——不管在任何位置，选取符合条件的节点
'''
def test1():
    # 假设我们有以下JSON数据
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
    # 转成键值对
    data = json.loads(json_data)
    author = jsonpath.jsonpath(data, '$.store.book[*].author')
    print(author)  # ['Nigel Rees', 'Evelyn Waugh', 'Herman Melville', 'J. R. R. Tolkien']
    '''
    ?(@.author) ——筛选book（book的值为列表）中，包含author的所有的对象（?()  ——支持过滤操作/@  ——当前节点/.. ——不管在任何位置，选取符合条件的节点）
    '''
    isbn_book = jsonpath.jsonpath(data, '$..book[?(@.author)]')
    print(isbn_book)  # [{'category': 'fiction', 'author': 'Herman Melville', 'title': 'Moby Dick', 'isbn': '0-553-21311-3', 'price': 8.99}, {'category': 'fiction', 'author': 'J. R. R. Tolkien', 'title': 'The Lord of the Rings', 'isbn': '0-395-19395-8', 'price': 22.99}]
    '''
    3.1、$..price ——筛选跟节点下所有的“键名price”
    '''
    category_name = jsonpath.jsonpath(data, '$..price')
    print(category_name)  # [8.95, 12.99, 8.99, 22.99, 19.95]

    color = jsonpath.jsonpath(data, '$..color')
    print(color)  # ['red']
    owner = jsonpath.jsonpath(data, '$..owner')
    print(owner)  # [['马云', '史玉柱', '马化腾', '王健林', '董明珠', '雷军']]
    owner2 = jsonpath.jsonpath(data, '$..owner[1]')
    print(owner2)  # ['史玉柱']
def test2():
    dit1={
	"store": {
		"book": [{
			"category": "reference",
			"author": "Nigel",
			"title": "Sayings of the Century",
			"price": 8.95
		}, {
			"category": "fiction",
			"author": "Tolkien",
			"title": "The Lord of the Rings",
			"isbn": "0-395-19395-8",
			"price": 22.99
		}],
		"bicycle": {
			"color": "red",
			"price": 19.95
		}
	}
}
    # dit2=json.loads(dit1)
    print(jsonpath.jsonpath(dit1,'$..book[*].author'))#['Nigel', 'Tolkien']
    print(jsonpath.jsonpath(dit1,'$..author'))#['Nigel', 'Tolkien']
    #?(@.author) ——筛选包含author的所有的对象
    print(jsonpath.jsonpath(dit1,'$..?(@.author)'))#[{'category': 'reference', 'author': 'Nigel', 'title': 'Sayings of the Century', 'price': 8.95}, {'category': 'fiction', 'author': 'Tolkien', 'title': 'The Lord of the Rings', 'isbn': '0-395-19395-8', 'price': 22.99}]
def test3():
    dit1 = {
        "store": {
            "book": [{
                "category": "reference",
                "author": "Nigel",
                "title": "Sayings of the Century",
                "price": 8.95
            }, {
                "category": "fiction",
                "author": "Tolkien",
                "title": "The Lord of the Rings",
                "isbn": "0-395-19395-8",
                "price": 22.99
            }],
            "bicycle": {
                "color": "red",
                "price": 19.95
            }
        }
    }
    print(jsonpath.jsonpath(dit1,'$..book[*].author'))
    print(jsonpath.jsonpath(dit1,'$..author'))
    print(jsonpath.jsonpath(dit1,'$..?(@.author)'))
'''
练习：2025/3/20（1）
'''
def test4():
    dit1 = {
        "store": {
            "book": [{
                "author": "张三",
                "title": "红书",
                "price": 8.95
            },{
                "author": "李四",
                "title": "战争",
                "price": 17
            }],
            "bicycle": {
                "color": "red",
                "price": 19.95
            }
        }
    }
    print(jsonpath.jsonpath(dit1,'$..book[*].author'))
    print(jsonpath.jsonpath(dit1,'$..author'))
    print(jsonpath.jsonpath(dit1,'$..?(@.author)'))#[{'author': '张三', 'title': '红书', 'price': 8.95}, {'author': '李四', 'title': '战争', 'price': 17}]
    print(jsonpath.jsonpath(dit1,'$..?(@.color)'))#[{'color': 'red', 'price': 19.95}]
    print(jsonpath.jsonpath(dit1,'$..?(@.book)'))#[{'book': [{'author': '张三', 'title': '红书', 'price': 8.95}, {'author': '李四', 'title': '战争', 'price': 17}], 'bicycle': {'color': 'red', 'price': 19.95}}]
def test5():
    dit1 = {
        "store": {
            "book": [{
                "author": "张三",
                "title": "红书",
                "price": 8.95
            }, {
                "author": "李四",
                "title": "战争",
                "price": 17
            }],
            "bicycle": {
                "color": "red",
                "price": 19.95
            }
        }
    }
    print(jsonpath.jsonpath(dit1,'$..book[*].author'))
    print(jsonpath.jsonpath(dit1,'$..author'))
    print(jsonpath.jsonpath(dit1,'$..?(@.color)'))
    print(jsonpath.jsonpath(dit1,'$..?(@.book)'))
    print(jsonpath.jsonpath(dit1,'$..?(@.author)'))
def test6():
    dit1 = {
        "store": {
            "book": [{
                "author": "张三",
                "title": "红书",
                "price": 8.95
            }, {
                "author": "李四",
                "title": "战争",
                "price": 17
            }],
            "bicycle": {
                "color": "red",
                "price": 19.95
            }
        }
    }
    print(jsonpath.jsonpath(dit1,'$..book[*].author'))
    print(jsonpath.jsonpath(dit1,'$..author'))
    print(jsonpath.jsonpath(dit1,'$..?(@.author)'))
    print(jsonpath.jsonpath(dit1,'$..?(@.price)'))
    print(jsonpath.jsonpath(dit1,'$..?(@.color)'))