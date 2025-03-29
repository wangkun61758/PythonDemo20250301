#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/3/28 13:18
=================================================='''
import pymysql
def test1():
    # 连接到MySQL数据库
    connect1 = pymysql.connect(host='你的localhost', user='name', password='123', database='your_database')
    # 创建一个Cursor对象并使用它执行SQL语句
    cur1 = connect1.cursor()
    cur1.execute('此处是sql语句')
    # 提交事务
    connect1.commit()
    # 关闭Cursor和Connection
    cur1.close()
    connect1.close()

def test2():
    connect1 = pymysql.connect(host='你的localhost', user='name', password='123', database='your_database')
    cursor1 = connect1.cursor()
    cursor1.execute('12')
    connect1.commit()
    cursor1.close()
    connect1.close()

def test3():
    connect1=pymysql.connect(host='你的localhost', user='name', password='123', database='your_database', charset='utf8')
    cursor1 = connect1.cursor()
    cursor1.execute('12')
    connect1.commit()
    cursor1.close()
    connect1.close()
