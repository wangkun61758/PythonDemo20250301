# coding=gbk
import csv
import os.path
import random

'''
���,�Ÿ�,�ŷ�,����
�ŷ�,����,����,����
����,����,����,����
'''
def test1():
    list = []
    with open('../../resources/file1.csv', 'r', encoding='gbk') as file:  # gbk' �����ȡ�������޷�����������
        csv_data = csv.reader(file)
        for row in csv_data:
            list.append(row)
    print(list)

    file.close()
    return list
def test2():
    list = []
    with open('../../resources/file1.csv', 'r', encoding='gbk') as file:
        data=csv.reader(file)
        for i in data:
            list.append(i)
    print(list)
    file.close()
def test3():
    list = []
    with open('../../resources/file1.csv', 'r', encoding='gbk') as file:
        data=csv.reader(file)
        for row in data:
            list.append(row)
    print(list)
def test4():
    list = []
    with open('../../resources/file1.csv', 'r', encoding='gbk') as file:
        data=csv.reader(file)
        for row in data:
            list.append(row)
    print(list)
    file.close()
def test5():
    list = []
    with open('../../resources/file1.csv', 'r', encoding='gbk') as file:
        data=csv.reader(file)
        for row in data:
            list.append(row)
    print(list)
    file.close()
def test6():
    list = []
    with open('../../resources/file1.csv', 'r', encoding='gbk') as file:
        data=csv.reader(file)
        for row in data:
            list.append(row)
    print(list)
    file.close()
def test7():
    list = []
    with open('../../resources/file1.csv', 'r', encoding='gbk') as file:
        data=csv.reader(file)
        for row in data:
            list.append(row)
    print(list)
    file.close()
def test8():
    list=[]
    with open('../../resources/file1.csv', 'r', encoding='gbk') as file:
        data=csv.reader(file)
        for row in data:
            list.append(row)
    print(list)
    file.close()
def test9():
    list=[]
    with open('../../resources/file1.csv', 'r', encoding='gbk') as file:
        data=csv.reader(file)
        for row in data:
            list.append(row)
    file.close()
def test10():
    list=[]
    with open('../../resources/file1.csv', 'r', encoding='gbk') as file:
        data=csv.reader(file)
        for row in data:
            list.append(row)
    file.close()
def test11():
    list=[]
    with open('../../resources/file1.csv', 'r', encoding='gbk') as file:
        data=csv.reader(file)
        for row in data:
            list.append(row)
    file.close()
def test12():
    list = []
    with open(r'../../resources/file1.csv', 'r', encoding='gbk') as file:
        data=csv.reader(file)
        for row in data:
            list.append(row)
    file.close()
'''
��ϰ��2025/3/20��2��
'''
def test13():
    list1=[]
    with open(r'../../resources/file1.csv', 'r', encoding='gbk') as file:
        data=csv.reader(file)
        for row in data:
            list1.append(row)
    file.close()
def test14():
    list1=[]
    with open('../../resources/file1.csv', 'r', encoding='gbk') as file:
        data=csv.reader(file)
        for row in data:
            list1.append(row)
    file.close()