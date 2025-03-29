#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/2/13 0:21
=================================================='''
def test1():
    dict1 = {'Name': '王五', 'Age': 7, 'Class': '一年级'}
    print(dict1['Name'])

    for i in dict1:# 遍历key值
        print(i)
    for j in dict1.keys():# 遍历key值
        print(j)
    for k in dict1.values():
        print(k)
    list1=[]
    list2=[]
    for key,value in dict1.items():#遍历字典
        list1.append(key)
        list2.append(value)
    dict_list1 = dict({list1[i]: list2[i] for i in range(len(list1))})
    print('列表转字典：'+str(dict_list1))#{'Name': '王五', 'Age': 7, 'Class': '一年级'}

    print('删除字典 key（键）所对应的值，返回被删除的值:'+str(dict1.pop("Age")))#删除字典 key（键）所对应的值，返回被删除的值:7
    print(dict1.popitem())  # 用于返回并删除字典中的一个键值对，一般删除字典末尾的键值对

    dict2={}#创建一个空字典
    #dict2=dict()#创建一个空字典
    print(dict2)#{}
    dict2['喜好']='摄影'#增加元素‌：可以通过键来为字典添加新的键值对
    print(dict2)#{'喜好': '摄影'}
    dict3={'喜好': '摄影'}
    del(dict3['喜好'])#删除键值对
    print(dict3)#{}

    ####################################################################
    list_datas = ["eat", "tea"]
    list1 = []
    dict1 = {}
    for i in list_datas:
        a1 = list(i)
        a2 = sorted(a1)
        a3 = ''.join(a2)
        if a3 not in dict1:
            dict1[a3] = [i]
            print('【如果a3不在dict1中】：' + str(dict1))  # {'aet': ['eat']}
        else:
            dict1[a3].append(i)
            print('【否则a3在dict1中】：' + str(dict1))  # {'aet': ['eat', 'tea']}
    for i in dict1:  # {'aet': ['eat', 'tea']}
        list1.append(dict1[i])
        print('【打印list1】:' + str(list1))  # [['eat', 'tea']]
    print(list1)

    ####################################################################
    dict1 = {'aet': ['eat']}
    dict1['aet'].append('王帅')
    print(dict1)  # {'aet': ['eat', '王帅']}

def test2():
    dict1 = {'Name': '王五', 'Age': 7, 'Class': '一年级'}
    print(dict1['Name'])
    for i in dict1:print(i)
    for j in dict1.keys():print(j)
    for k in dict1.values():print(k)
    list1=[]
    list2=[]
    for key,value in dict1.items():
        list1.append(key)
        list2.append(value)
    dict2=dict({list1[i]:list2[i] for i in range(len(list1))})
    print(dict2)
    print(dict2.popitem())#用于返回并删除字典中的一个键值对，一般删除字典末尾的键值对
def test3():
    dict1 = {'Name': '王五', 'Age': 7, 'Class': '一年级'}
    print(dict1['Age'])#7
    dict1['性别']='mail'
    print(dict1)#{'Name': '王五', 'Age': 7, 'Class': '一年级', '性别': 'mail'}

    dict1.pop('Class')#删除指定键的键值对
    print(dict1)#{'Name': '王五', 'Age': 7, '性别': 'mail'}

    print(dict1.popitem())#用于返回并删除字典中的一个键值对，一般删除字典末尾的键值对
    print(dict1)#{'Name': '王五', 'Age': 7}

    list1=[]
    list2=[]
    for k,v in dict1.items():
        list1.append(k)
        list2.append(v)
    dict2=dict({list1[i]:list2[i] for i in range(len(list1))})
    print(dict2)
def test4():
    dict1 = {'Name': '王五', 'Age': 7, 'Class': '一年级'}
    print(dict1['Name'])
    for i in dict1:
        print(i)
    for j in dict1.items():
        print(j)
    for k in dict1.values():
        print(k)
    dict1['键']='值'
    print(dict1)#{'Name': '王五', 'Age': 7, 'Class': '一年级', '键': '值'}
    dict1.pop('Name')
    dict1.popitem()
def test5():
    list_datas = ["eat", "tea"]
    list1 = []
    dict1 = {}
    for i in list_datas:
        a1 = list(i)
        a2 = sorted(a1)
        a3 = ''.join(a2)
        if a3 not in dict1:
            dict1[a3] = [i]
            print('【如果a3不在dict1中】：' + str(dict1))  # {'aet': ['eat']}
        else:
            dict1[a3].append(i)
            print('【否则a3在dict1中】：' + str(dict1))  # {'aet': ['eat', 'tea']}
    for i in dict1:  # {'aet': ['eat', 'tea']}
        list1.append(dict1[i])
        print('【打印list1】:' + str(list1))  # [['eat', 'tea']]
    print(list1)
def test6():
    dict1 = {'aet': ['eat']}
    dict1['aet'].append('王帅')
    print(dict1)#{'aet': ['eat', '王帅']}
def test7():
    dict1 = {'Name': '王五', 'Age': 7, 'Class': '一年级'}
    print(dict1['Name'])
    for i in dict1:print(i)
    for j in dict1.keys():print(j)
    for k in dict1.values():print(k)
    list1=[]
    list2=[]
    for key,value in dict1.items():
        list1.append(key)
        list2.append(value)
    dict2=dict({list1[i]:list2[i] for i in range(len(list1))})
    print(dict2)
    dict3={list1[i]:list2[i] for i in range(len(list1))}
    print(dict3)
    dict4={}
    dict4.update(dict1)
    dict5={'喜好':'摄影'}
    del (dict5['喜好'])#{'Name': '王五', 'Age': 7, 'Class': '一年级'}
    print(dict1)
    dict1.pop('Name')#{'Age': 7, 'Class': '一年级'}
    print(dict1)
def test8():
    dict1 = {'Name': '王五', 'Age': 7, 'Class': '一年级'}
    print(dict1['Name'])
    for i in dict1:print(i)
    for j in dict1.keys():print(j)
    for k in dict1.values():print(k)
    list1=[]
    list2=[]
    for key,value in dict1.items():
        list1.append(key)
        list2.append(value)
    dict2=dict({list1[i]:list2[i] for i in range(len(list1))})
    print(dict2)#{'Name': '王五', 'Age': 7, 'Class': '一年级'}
    dict3={list1[i]:list2[i] for i in range(len(list1))}
    print(dict3)#{'Name': '王五', 'Age': 7, 'Class': '一年级'}
    dict4={}
    dict4.update(dict1)
    dict1['性别']='男'
    print(dict1)#{'Name': '王五', 'Age': 7, 'Class': '一年级', '性别': '男'}
    del (dict1['性别'])
    print(dict1)#{'Name': '王五', 'Age': 7, 'Class': '一年级'}
    dict1.pop('Name')#删除指定的键值对
    print(dict1)#{'Age': 7, 'Class': '一年级'}
    dict1.popitem()# 删除字典末尾的键值对（无参数）
    print(dict1)#{'Age': 7}

    d = {'a': 1, 'b': 2}
    d.update({'c': 3, 'd': 4})
    print(d)#{'a': 1, 'b': 2, 'c': 3, 'd': 4}
'''
练习：2025/3/20（3）
'''
def test9():
    dict1 = {'Name': '王五', 'Age': 7, 'Class': '一年级'}
    print(dict1['Name'])
    for i in dict1:print(i)
    for j in dict1.keys():print(j)
    for k in dict1.values():print(k)
    list1=[]
    list2=[]
    for key,value in dict1.items():
        list1.append(key)
        list2.append(value)
    dict2={list1[i]:list2[i] for i in range(len(list1))}
    print(dict2)
    dict3=dict({list1[i]:list2[i] for i in range(len(list1))})
    print(dict3)
    dict4={}
    dict4.update(dict1)
    dict1['性别']='mail'
    print(dict1)#{'Name': '王五', 'Age': 7, 'Class': '一年级', '性别': 'mail'}
    del (dict1['性别'])#删除指定的键值对
    dict1.pop('Name')#删除指定的键值对
    dict1.popitem()# 删除字典末尾的键值对（无参数）
def test10():
    dict1 = {'Name': '王五', 'Age': 7, 'Class': '一年级'}
    print(dict1['Name'])
    for i in dict1:print(i)
    for j in dict1.keys():print(j)
    for v in dict1.values():print(v)
    list1=[]
    list2=[]
    for key,value in dict1.items():
        list1.append(key)
        list2.append(value)
    dict2={list1[i]:list2[i] for i in range(len(list1))}
    dict4={}
    dict4.update(dict1)
    dict1['性别']='mail'
    dict1.pop('Name')
    dict1.popitem()

