#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/2/11 21:59
=================================================='''
import random

import pymysql


def test1():
    # 连接到MySQL数据库
    connect1 = pymysql.connect(host='localhost', user='root', password='360buyer', database='wk')
    # 创建一个Cursor对象并使用它执行SQL语句
    cur1 = connect1.cursor()
    sql = 'SELECT * FROM users'
    cur1.execute(sql)
    # 获取所有记录列表
    result = cur1.fetchall()
    for row in result:
        print(row)
    # 关闭Cursor和Connection
    cur1.close()
    connect1.close()


def test2():
    # 连接到MySQL数据库
    connect1 = pymysql.connect(host='localhost', user='root', password='360buyer', database='wk')
    # 创建一个Cursor对象并使用它执行SQL语句
    cur1 = connect1.cursor()
    random1 = random.randint(1000000, 9999999)
    sql = "INSERT INTO orders (orderNo, createtime, product, count, price) VALUES (random1, '2023-04-03 14:15:00', 'Product C', 2, 99.99);"
    cur1.execute(sql)
    connect1.commit()

    cur1.close()
    connect1.close()
