#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/3/19 18:03
=================================================='''
import csv
import os.path
from asyncore import write
def test1():
    list1=[]
    with open('../../resources/file1.csv','r',encoding='gbk') as file1:
        data1=csv.reader(file1)
        for row in data1:
            list1.append(row)
    file1.close()

    data2 = ["李白", "杜甫", "白居易", "王维"]
    if not os.path.exists('../../resources/csv'):
        os.makedirs('../../resources/csv')
    with open('../../resources/csv/file1.csv','w',encoding='gbk') as file2:
        writer2=csv.writer(file2)
        writer2.writerow(data2)


def test2():
    list1=[]
    with open('../../resources/csv/file1.csv','r',encoding='gbk') as file1:
        data1=csv.reader(file1)
        for row in data1:
            list1.append(row)
    file1.close()

    data2 = ["李白", "杜甫", "白居易", "王维"]
    if not os.path.exists('../../resources/csv'):
        os.makedirs('../../resources/csv')
    with open('../../resources/csv/file1.csv','w',encoding='gbk') as file2:
        writer2=csv.writer(file2)
        writer2.writerow(data2)


def test3():
    list1=[]
    with open('../../resources/csv/file1.csv','r',encoding='gbk') as file1:
        data1=csv.reader(file1)
        for row in data1:
            list1.append(row )
    file1.close()

    # data2 = ["李白", "杜甫", "白居易", "王维"]
    data2={'name': '韩梅梅', 'age': 19, 'car': 'jeep'}
    with open('../../resources/csv/file1.csv','w',encoding='gbk') as file2:
        write2=csv.writer(file2)
        # write2.writerow(data2.items())#"('name', '韩梅梅')","('age', 19)","('car', 'jeep')"
        # write2.writerow(data2)#name,age,car
        write2.writerow(data2.keys())#name,age,car
        # write2.writerow(data2.values())#韩梅梅,19,jeep

def test4():
    list1=[]
    with open('../../resources/csv/file1.csv','r',encoding='gbk') as file1:
        data1=csv.reader(file1)
        for row in data1:
            list1.append(row)
    file1.close()

    data2 = {'name': '韩梅梅', 'age': 19, 'car': 'jeep'}
    with open('../../resources/csv/file1.csv','w',encoding='gbk') as file2:
        writer2=csv.writer(file2)
        writer2.writerow(data2.keys())


def test5():
    list1=[]
    with open('../../resources/csv/file1.csv','r',encoding='gbk') as file1:
        data1=csv.reader(file1)
        for row in data1:
            list1.append(row)
    file1.close()
    data2 = {'name': '韩梅梅', 'age': 19, 'car': 'jeep'}
    with open('../../resources/csv/file1.csv','w',encoding='gbk') as file2:
        writer2=csv.writer(file2)
        writer2.writerow(data2.keys())

def test6():
    list1=[]
    with open(r'../../resources/csv/file1.csv','r',encoding='gbk') as file1:
        data1=csv.reader(file1)
        for row in data1:
            list1.append(row)
    file1.close()
    data2 = {'name': '韩梅梅', 'age': 19, 'car': 'jeep'}
    with open(r'../../resources/csv/file1.csv','w',encoding='gbk') as file2:
        write2=csv.writer(file2)
        write2.writerow(data2.keys())

def test7():
    list1=[]
    with open(r'../../resources/csv/file1.csv','r',encoding='gbk') as file1:
        data1=csv.reader(file1)
        for row in data1:
            list1.append(row)
    file1.close()
    data2 = {'name': '韩梅梅', 'age': 19, 'car': 'jeep'}
    with open(r'../../resources/csv/file1.csv','w',encoding='gbk') as file2:
        write2=csv.writer(file2)
        write2.writerow(data2.keys())

def test8():
    list1=[]
    with open('../../resources/csv/file1.csv','r',encoding='gbk') as fil1:
        reader1=csv.reader(fil1)
        for row in reader1:
            list1.append(row)
    fil1.close()

    dict1={'name':'雷军', 'age': 19, 'car': 'jeep'}
    with open(r'../../resources/csv/file1.csv','w',encoding='gbk') as file2:
        writer2=csv.writer(file2)
        writer2.writerow(dict1.items())

def test9():
    list1=[]
    with open('../../resources/csv/file1.csv','r',encoding='gbk') as file1:
        reader1=csv.reader(file1)
        for row in reader1:
            list1.append(row)
    file1.close()

    dict1={'name':"leijun", 'age': 19, 'car': 'jeep'}
    with open(r'../../resources/csv/file1.csv','w',encoding='gbk') as file2:
        writer2=csv.writer(file2)
        writer2.writerow(dict1.items())

def test10():
    list1=[]
    with open('../../resources/csv/file1.csv','r',encoding='gbk') as fil1:
        reader1=csv.reader(fil1)
        for row in reader1:
            list1.append(row)
    fil1.close()

    dict1={'name':'leijun', 'age': 19, 'car': 'jeep'}
    with open(r'../../resources/csv/file1.csv','w',encoding='gbk') as file2:
        writer2=csv.writer(file2)
        writer2.writerow(dict1.items())

def test11():
    list1=[]
    with open('../../resources/csv/file1.csv','r',encoding='gbk') as fil1:
        reader1=csv.reader(fil1)
        for row in reader1:
            list1.append(row)
    fil1.close()
    dict1={'name':'leijun', 'age': 19, 'car': 'jeep'}
    with open(r'../../resources/csv/file1.csv','w',encoding='gbk') as file2:
        writer2=csv.writer(file2)
        writer2.writerow(dict1.items())
def test12():
    list1=[]
    with open('../../resources/csv/file1.csv','r',encoding='gbk') as fil1:
        reader1=csv.reader(fil1)
        for row in reader1:
            list1.append(row)
    fil1.close()
    dict1={'name':'leijun', 'age': 19, 'car': 'jeep'}
    with open(r'../../resources/csv/file1.csv','w',encoding='gbk') as file2:
        writer2=csv.writer(file2)
        writer2.writerow(dict1)

def test13():
    list1=[]
    with open(r'../../resources/csv/file1.csv','r',encoding='gbk') as fil1:
        reader1=csv.reader(fil1)
        for row in reader1:
            list1.append(row)
    fil1.close()
    dict1={'name':'leijun', 'age': 19, 'car': 'jeep'}
    with open(r'../../resources/csv/file1.csv','w',encoding='gbk') as file2:
        writer2=csv.writer(file2)
        writer2.writerow(dict1)
'''
练习：2025/3/20（1）
'''
def test14():
    list1=[]
    with open('../../resources/csv/file1.csv','r',encoding='gbk') as file1:
        reader1=csv.reader(file1)
        for row in reader1:
            list1.append(row)
    file1.close()
    dict1={'name':'leijun', 'age': 19, 'car': 'jeep'}
    with open(r'../../resources/csv/file1.csv','w',encoding='gbk') as file2:
        writer2=csv.writer(file2)
        writer2.writerow(dict1)

def test15():
    list1=[]
    with open('../../resources/csv/file1.csv','r',encoding='gbk') as file1:
        reader1=csv.reader(file1)
        for row in reader1:
            list1.append(row)
    file1.close()
    dict1={'name':'leijun', 'age': 19, 'car': 'jeep'}
    with open(r'../../resources/csv/file1.csv','w',encoding='gbk') as file2:
        writer2=csv.writer(file2)
        writer2.writerow(dict1)

