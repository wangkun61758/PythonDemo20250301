#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/7/12 9:04
=================================================='''
import random


def test1():
    # 1、用于生成0到1之间的浮点数
    n = random.random()
    print('1、生成0到1之间的浮点数:' + str(n))
    n1=random.random()

    # 2、生成一个指定范围内的整数，其中a是下限，b是上限
    m = random.randint(1, 100)
    print('2、生成一个指定范围内的整数：' + str(m))
    m1=random.randint(100,1000)

    # 3、从给定范围内取值
    a = random.randrange(0, 100, 3)
    print('3、从给定范围内取值：' + str(a))
    a1=random.randrange(0,100,2)

    # 4、从序列种随机取一个元素
    list = ['哈哈', 13, 9887, 'xixi', [1, 2, 3], {'品牌': '长安', '颜色': 'red'}]
    print('4、从序列种随机取一个元素：' + str(random.choice(list)))
    print(str(random.choice(list)))
    l=random.choice(list)

    '''
    5、random.shuffle(x)表示对列表x中的所有元素随机打乱顺序（若x不是列表，则报错）。
    此函数会直接对x本身进行操作，函数的返回值为None，即如果想对列表x进行洗牌，须使用random.shuffle(x)的形式，而不能使用y=random.shuffle(x)的形式
    '''
    lists = [15, 22, 13, 97, 57, 7, 28]
    random.shuffle(lists)
    print(lists)  # 正常打印

    # 6、从一个序列中随机选择指定数量的元素
    list1 = ['hameimei', 'lilei', 'lisi', 'zhagnsan', 'zhaoer', 'wangwu']
    print(random.sample(list1, 2))  # ['hameimei', 'zhagnsan']

    a = random.random()
    print(a)

    b = random.randint(1, 1000)
    print(b)

    c = random.randrange(1, 1000, 13)
    print(c)
    list = ['haha', '熙熙', '你好', '韩梅梅', 'age']
    print(random.choice(list))

def test2():
    a = random.random()
    print(a)
    b=random.randint(1,100)
    print(b)

    c=random.randrange(0,100,3)
    print(c)

    list1 = ['hameimei', 'lilei', 'lisi', 'zhagnsan', 'zhaoer', 'wangwu']
    print(random.choice(list1))
    random.shuffle(list1)
    print(str(list1))#['lilei', 'zhagnsan', 'wangwu', 'lisi', 'hameimei', 'zhaoer']

    print(random.sample(list1, 2))#(从一个列表中随机选择指定数量的元素)['hameimei', 'zhagnsan']
def test3():
    a1=random.random()
    a2=random.randint(1,100)
    a3=random.randrange(1,100)
    a4=random.uniform(0,100)

    list1 = [11,2,56,198,22]
    print(random.choice(list1))
    random.shuffle(list1)
    print(str(list1))#[56, 2, 11, 22, 198]
    print(random.sample(list1, 2))#[11, 2]

def test4():
    a1 = random.random()
    a2 = random.randint(1, 100)
    a3 = random.randrange(1, 100)
    a4 = random.uniform(0, 100)
    list1 = [1,2,3,4,5]
    random.shuffle(list1)
    print(str(list1))
    print(random.choice(list1))

    print(random.sample(list1, 2))

def test5():
    a1 = random.random()
    a2 = random.randint(1,100)
    a3 = random.randrange(1,100)
    a4 = random.uniform(0,100)
    list1 = [1,2,3,4,5]
    random.shuffle(list1)
    print(str(list1))
    print(random.sample(list1, 2))
    print(random.choice(list1))
'''
练习：2025/3/20（1）
'''
def test6():
    a1 = random.random()
    a2 = random.randint(1,100)
    a3=random.randrange(1,100)
    a4=random.uniform(0,100)
    list1 = [1,2,3,4,5]
    random.shuffle(list1)
    random.choice(list1)
    random.sample(list1, 2)

