#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/2/12 22:54
=================================================='''
from locale import windows_locale


def test1():
    list1 = ['hameimei', 'lilei', 'lisi', 'zhagnsan', 'zhaoer', 'wangwu']
    list1.append('wk')#添加元素
    print(list1)#['hameimei', 'lilei', 'lisi', 'zhagnsan', 'zhaoer', 'wangwu', 'wk']
    list1.extend('王五')#extend是将可迭代对象中的每个元素逐一添加到列表尾部
    print(list1)#['hameimei', 'lilei', 'lisi', 'zhagnsan', 'zhaoer', 'wangwu', 'wk', '王', '五']
    list1.sort(reverse=False)#按照元素本身升序排列
    print(list1)#['hameimei', 'lilei', 'lisi', 'wangwu', 'wk', 'zhagnsan', 'zhaoer', '五', '王']
    print(sorted(list1,reverse=False))#['hameimei', 'lilei', 'lisi', 'wangwu', 'wk', 'zhagnsan', 'zhaoer', '五', '王']
    list1.pop(0)#删除索引指定的元素,并将删除元素返回
    print(list1)#['lilei', 'lisi', 'wangwu', 'wk', 'zhagnsan', 'zhaoer', '五', '王']
    list1.remove('lilei')#删除列表中第一个匹配元素，若没有找到匹配元素会报错
    list2= [11, 3, 67, 2, -6, 18, 36]
    print(list2.sort(key=lambda x:abs(x)))#[2, 3, -6, 11, 18, 36, 67]
    print(list2.count(11))#1
    list2.insert(2,'清华')#在指定位置插入一个元素
    print(list2)#[2, 3, '清华', -6, 11, 18, 36, 67]
    print(list2.copy())#list.copy() 方法没有参数，返回一个新的列表，这个新列表与原列表在内存地址上不同，但包含相同的元素 [2, 3, '清华', -6, 11, 18, 36, 67]
    list2.reverse()
    print(list2)#[67, 36, 18, 11, -6, '清华', 3, 2]
    print(list2.index(67,0,6))#[67, 36, 18, 11, -6, '清华', 3, 2]
    list2.clear()
    print(list2)#[]

    list3 = [2, 7, 11, 15]
    print(list3[1:])  # [7, 11, 15]
    print([0, (list3[1:].index(7)) + (0 + 1)])  # [0, 1]

    list4 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    for i in list4:
        a1 = list(i)  # ['e', 'a', 't']
        print(a1)
        a2 = sorted(a1)
        print(a2)
        str1 = ''.join(a2)
        print(str1)

    list_datas = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
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
            print('【否则a3在dict1中】：' + str(dict1))

    for i in dict1:  # {'aet': ['eat']}
        list1.append(dict1[i])
        print('【打印list1】:' + str(list1))
    print(list1)

    list2 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    for i in list2:
        a1 = list(i)
        print(a1)#['e', 'a', 't']
        a2 = sorted(a1)
        print(a2)#['a', 'e', 't']
        str1 = ''.join(a2)
        print(str1)#aet
def test2():
    list1=['hameimei', 'lilei', 'lisi', 'zhagnsan', 'zhaoer', 'wangwu']
    print(list1[1])#lilei
    print(list1[1:3])#['lilei', 'lisi']

    list1.append('末尾添加:王梅')#在列表末尾添加一个元素['hameimei', 'lilei', 'lisi', 'zhagnsan', 'zhaoer', 'wangwu', '末尾添加:王梅']
    list1.extend('建国')#append函数把可迭代对象视作一个整体添加到列表尾部而extend是将可迭代对象中的每个元素逐一添加到列表尾部
    print(list1)#['hameimei', 'lisi', 'zhagnsan', 'zhaoer', 'wangwu', '末尾添加:王梅', '建', '国']
    list1.insert(2,'指定位置插入：卫华')#在指定位置插入一个元素

    list1.remove('lilei')#删除列表中第一个匹配元素，若没有找到匹配元素会报错
    list2=list1.pop(1)#删除索引指定的元素(此处是”指定位置插入：卫华“)并将删除元素返回
    print(list1,list2)#['hameimei', 'lisi', 'zhagnsan', 'zhaoer', 'wangwu', '末尾添加:王梅'] 指定位置插入：卫华

    list3=[11,3,67,2,-6,18,36]
    list3.sort()#按照元素本身升序排列
    list3.sort(reverse=True)#按照元素本身降序排列
    list3.sort(key=lambda x:abs(x))#按照元素绝对值排序([2, 3, -6, 11, 18, 36, 67])
    print(list3.count(11))#统计列表[2, 3, -6, 11, 18, 36, 67]中某元素出现次数
    print(list3.index(11))#查找列表[2, 3, -6, 11, 18, 36, 67]中第一个匹配元素并返回索引位置，若指定元素不在列表中会抛出ValueError异常

    #列表去重
    my_list = [1, 2, 2, 3, 4, 4, 5]
    unique_list = []
    for i in my_list:
        if i not in unique_list:
            unique_list.append(i)
    print(unique_list)#[1, 2, 3, 4, 5]

    list4=list(set(my_list))#会改变元素的原始顺序，并且如果列表中包含不可哈希类型（如列表或字典）的元素，这种方法就不能使用
    print(list4)#[1, 2, 3, 4, 5]
def test3():
    list1 = ['hameimei', 'lilei', 'lisi', 'zhagnsan', 'zhaoer', 'wangwu']
    list1.append('张三')
    print(list1)
    list1.remove('lilei')
    print(list1)
    list1.extend('李白')
    print(list1)
    list1.sort(reverse=False)
    list1.insert(3,'杜甫')
    print(list1)
    list1.pop(0)
    print(list1)

    list3 = [11, 3, 67, 2, -6, 18, 36]
    list3.sort(key=lambda x:abs(x))
    print(list3)
def test4():
    list1 = ['hameimei', 'lilei', 'lisi', 'zhagnsan', 'zhaoer', 'wangwu']
    list1.append('wk')#添加元素
    print(list1)#['hameimei', 'lilei', 'lisi', 'zhagnsan', 'zhaoer', 'wangwu', 'wk']
    list1.extend('王五')#extend是将可迭代对象中的每个元素逐一添加到列表尾部
    print(list1)#['hameimei', 'lilei', 'lisi', 'zhagnsan', 'zhaoer', 'wangwu', 'wk', '王', '五']
    list1.sort(reverse=False)##按照元素本身升序排列
    print(list1)#['hameimei', 'lilei', 'lisi', 'wangwu', 'wk', 'zhagnsan', 'zhaoer', '五', '王']
    print(sorted(list1,reverse=False))#['hameimei', 'lilei', 'lisi', 'wangwu', 'wk', 'zhagnsan', 'zhaoer', '五', '王']
    list1.pop(0)#删除索引指定的元素,并将删除元素返回
    print(list1)#['lilei', 'lisi', 'wangwu', 'wk', 'zhagnsan', 'zhaoer', '五', '王']
    list1.remove('lilei')#删除列表中第一个匹配元素，若没有找到匹配元素会报错
    list2= [11, 3, 67, 2, -6, 18, 36]
    print(list2.sort(key=lambda x:abs(x)))#[2, 3, -6, 11, 18, 36, 67]
    list2.count(11)
    print( list2.count(11))#1
    list2.insert(2,'清华')#在指定位置插入一个元素
    print(list2)#[2, 3, '清华', -6, 11, 18, 36, 67]
    print( list2.copy())#list.copy() 方法没有参数，返回一个新的列表，这个新列表与原列表在内存地址上不同，但包含相同的元素 [2, 3, '清华', -6, 11, 18, 36, 67]
    list2.reverse()
    print(list2)#[67, 36, 18, 11, -6, '清华', 3, 2]
    print(list2.index(67,0,6))#[67, 36, 18, 11, -6, '清华', 3, 2]
    list2.clear()
    print(list2)#[]
def test5():
    list1 = [11, 3, 67, 2, -6, 18, 36]
    print(list1.copy())#[11, 3, 67, 2, -6, 18, 36]
    print(list1.index(3, 0, 6))#1
    print(list1.count(2))#1

    list1.append('wk')
    print(list1)#[11, 3, 67, 2, -6, 18, 36, 'wk']
    list1.extend('王五')
    print(list1)#[11, 3, 67, 2, -6, 18, 36, 'wk', '王', '五']
    list1.reverse()
    print(list1)#['五', '王', 'wk', 36, 18, -6, 2, 67, 3, 11]
    list1.pop(0)
    print(list1)
    list1.remove('wk')
    print(list1)
def test6():
    list1 = ['hameimei', 'lilei', 'lisi', 'zhagnsan', 'zhaoer', 'wangwu']
    list1.append('张三')
    list1.extend('赵六')
    list1.insert(2,'玛丽亚')
    list1.sort(reverse=False)
    list1.pop(0)
    list1.remove('lilei')

    list2= [11, 3, 67, 2, -6, 18, 36]
    list2.sort(key=lambda x:abs(x))

    list2.insert(2,'北大')#[2, 3, '北大', -6, 11, 18, 36, 67]
    print(list2.index(2,0,6))
    print(list2.copy())
    list2.clear()
def test7():
    list1 =[2,7,11,15]
    print(list1[1:])#[7, 11, 15]
    print( [0, (list1[1:].index(7))+(0+1)])#[0, 1]
def test8():
    list1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    for i in list1:
        a1 = list(i)#['e', 'a', 't']
        print(a1)
        a2=sorted(a1)
        print(a2)
        str1=''.join(a2)
        print(str1)
def test9():
    list_datas = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    list1 = []
    dict1 = {}
    for i in list_datas:
        a1 = list(i)## ['e', 'a', 't']
        a2 = sorted(a1)# ['a', 'e', 't']
        a3 = ''.join(a2)# aet
        if a3 not in dict1:
            dict1[a3] = [i]# {'aet': ['eat']}
            print('【如果a3不在dict1中】：' + str(dict1))  # {'aet': ['eat']}
        else:
            dict1[a3].append(i)
            print('【否则a3在dict1中】：' + str(dict1))#【否则a3在dict1中】：{'aet': ['eat', 'tea']}
    print(dict1)#{'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}
    '''
    【打印list1】:[['eat', 'tea', 'ate']]
    【打印list1】:[['eat', 'tea', 'ate'], ['tan', 'nat']]
    【打印list1】:[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    '''
    for i in dict1.keys():  # [['eat', 'tea', 'ate']]
        list1.append(dict1[i])
        print('【打印list1】:' + str(list1))
    print(list1)
def test10():
    list_datas = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    list1=[]
    dict1={}
    for i in list_datas:
        a1=list(i)
        a2=sorted(a1)
        a3=''.join(a2)
        if a3 not in dict1:
            dict1[a3]=[i]
        else:
            dict1[a3].append(i)
    print(dict1)#{'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}
    for i in dict1.keys():
        list1.append(dict1[i])
    print(list1)#[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
def test11():
    list_datas = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    list1=[]
    dict1={}
    for i in list_datas:
        a1=list(i)
        a2=sorted(a1)
        a3=''.join(a2)
        if a3 not in dict1:
            dict1[a3]=[i]
        else:dict1[a3].append(i)

    for i in dict1.keys():
        list1.append(dict1[i])
def test12():
    list1 = ['zhangsan', 'lishi','zhanglong']
    print(list(list1))#['zhangsan', 'lishi', 'zhanglong']
    for i in list1:
        a1=list(i)
        print(a1)#['z', 'h', 'a', 'n', 'g', 's', 'a', 'n']
def test13():
    list_datas = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    list1=[]
    dict1={}
    for i in list_datas:
        a1=list(i)
        a2=sorted(a1)
        a3=''.join(a2)
        if a3 not in dict1:
            dict1[a3]=[i]
        else:dict1[a3].append(i)
    for key in dict1.keys():list1.append(dict1[key])
def test14():
    list1 = ['hameimei', 'lilei', 'lisi', 'zhagnsan', 'zhaoer', 'wangwu']
    list1.append('wk')
    list1.extend('lixiang')
    list1.insert(2,'linfeng')
    list1.remove('lilei')
    list1.pop(0)
    list1.sort()
    list1.sort(reverse=False)
    print(list1.sort(key=lambda x:x[-1]))
    list2=[11, 3, 67, 2, -6, 18, 36]
    list2.sort(key=lambda x:abs(x))
    print(list2.copy())#[2, 3, -6, 11, 18, 36, 67]
    list2.reverse()#[67, 36, 18, 11, -6, 3, 2]

    list_datas = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    list1=[]
    dict1={}
    for i in list_datas:
        a1=list(i)
        a2=sorted(a1)
        a3=''.join(a2)
        if a3 not in dict1:
            dict1[a3]=[i]
        else:dict1[a3].append(i)
    for k in dict1.keys():list1.append(dict1[k])
'''
练习：2025/3/20（3）
'''
def test15():
    list1 = ['hameimei', 'lilei', 'lisi', 'zhagnsan', 'zhaoer', 'wangwu']
    list1.append('wk')
    list1.insert(2,'hanmeimei')
    list1.remove('wk')
    list1.pop(0)
    list1.sort(reverse=False)
    list1.sort()
    list1.sort(key=lambda x:x[-1])
    li=list1.copy()
    print(li)
    list2 = [11, 3, 67, 2, -6, 18, 36]
    list2.sort(key=lambda x:abs(x))
    print(list2)
    list_datas = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    list1=[]
    dict1={}
    for i in list_datas:
        a1=list(i)
        a2=sorted(a1)
        a3=''.join(a2)
        if a3 not  in dict1:
            dict1[a3]=[i]
        else:dict1[a3].append(i)
    for k in dict1.keys():list1.append(dict1[k])
    print(list1)#[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

def test16():
    list_datas = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    list1=[]
    dict1={}
    for i in list_datas:
        a1=list(i)
        a2=sorted(a1)
        a3=''.join(a2)
        if a3 not in dict1:
            dict1[a3]=[i]
        else:dict1[a3].append(i)
    for k in dict1.keys():list1.append(dict1[k])
    print(list1)
    list1 = ['hameimei', 'lilei', 'lisi', 'zhagnsan', 'zhaoer', 'wangwu']
    list1.append('wk')
    list1.insert(2,'hanmeimei')
    list1.remove('wk')
    list1.pop(0)
    list1.extend('lixiang')
    list1.copy()
    list1.sort(key=lambda x:x[-1])
    list1.count('lisi')