#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/2/7 22:56
=================================================='''
import random

def test1():
    m=random.randint(1,1111)#生成指定范围内的整数
    print(m)

    n=random.random()#返回随机生成的一个浮点数，范围在[0,1)之间
    print(n)

    list=['吉利', '阿里巴巴','小米', '腾讯', '谷歌', '特斯拉']
    random_list=random.choice(list)#从指定的序列(列表)中获取一个随机元素
    print(random_list)

    a=random.uniform(10,20)#19.660945339910906(随机生成的一个浮点数，范围在[a, b)之间)
    print(a)

    b=random.randrange(100,200,3)#下限值、上限值和宽度。在这三个参数中，两个参数 start 和 width 是可选的
    print(b)
    b2=random.randrange(200)#只有上限值
    b3=random.randrange(1,200)#只有上限值和下限值
    print(b2,b3)

    list2 = ['吉利', '阿里巴巴', '小米', '腾讯', '谷歌', '特斯拉']
    random.shuffle(list2)#将一个可变序列（通常是列表）中的元素随机排列，属于原地操作，不会返回新的序列
    print(list2)
    print(random.sample(list2,2))#['吉利', '特斯拉'](从一个序列中随机选择指定数量的元素)
    print(random.sample('hjkkjlfsd',3))#['h', 'k', 'k']

def test2():
    a=random.random()
    print(a)
    b=random.randint(12,33)
    print(b)
    list1=['11',"22",'36','8']
    c=random.choice(list1)
    print(c)
    d=random.uniform(11,22)
    print(d)
    e=random.randrange(33,55,2)
    print(e)

def test3():
    a=random.random()
    print(a)
    b=random.randint(1,100)
    print(b)
    c=random.uniform(22,33)
    print(c)
    list1=['11',"22",'36','8']
    d=random.choice(list1)
    print(d)
    e=random.randrange(33,55,2)
    print(e)
    list2 = ['吉利', '阿里巴巴', '小米', '腾讯', '谷歌', '特斯拉']
    random.shuffle(list2)
    print(random.sample(list2,3))
    print(random.sample('adsjkhg',2))
