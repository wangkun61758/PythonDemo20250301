#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/2/7 13:49
=================================================='''


# 方法 1：使用 sort() 方法（原地排序）
def test1():
    list1 = [11, 45, 2, 68, 99]
    list1.sort()#修改原列表，无返回值
    print(list1)#[2, 11, 45, 68, 99]
    list1.sort(reverse=False)#reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）
    print(list1)#[2, 11, 45, 68, 99]
    list1.sort(reverse=True)
    print(list1)#[99, 68, 45, 11, 2]

    list2 = ['a','wk','apple', 'orange', 'banana', 'lilei', 'hanmeimei']
    list2.sort(key=len)#按长度排
    print(list2)#['a', 'wk', 'apple', 'lilei', 'orange', 'banana', 'hanmeimei']


# 方法 2：使用 sorted() 函数（返回新列表）
def test2():
    list1 = [11, 45, 2, 68, 99]
    print(sorted(list1))#不改变原列表，返回新列表
    print(sorted(list1, reverse=True))

    list2 = ['apple', 'orange', 'banana', 'lilei', 'hanmeimei']
    print(sorted(list2, key=len))


# 方法 3：使用 lambda 表达式进行自定义排序
def test3():
    # 基于元组的第二个元素排序
    data = [(1, 3), (4, 1), (2, 2), (3, 4)]
    data.sort(key=lambda x: x[1])
    print(data)#[(4, 1), (2, 2), (1, 3), (3, 4)]

    # 按字符串的最后一个字母排序
    words = ["apple", "banana", "kiwi", "cherry"]
    words.sort(key=lambda x: x[-1])  # 单词最后一个字母排序(原地排序，不生成新的)
    print(words)
    sorted_words = sorted(words, key=lambda x: x[-1])  # 按单词最后一个字母排序（不改变原列表，返回新列表）
    print(sorted_words)


# 方法 4：使用 reverse() 方法倒序排列
def test4():
    list1 = [11, 45, 2, 68, 99]
    list1.reverse()  # 修改原列表，直接反转列表顺序
    print(list1)#[99, 68, 2, 45, 11]

# 方法 5：自定义排序算法
def test5():  # 冒泡排序
    list1 = [11, 45, 2, 68, 99]
    n = len(list1)
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if list1[j] > list1[j + 1]:
                # 第1轮比较 j 0~4:[11, 45, 2, 68, 99] [11, 2, 45, 68, 99] [11, 2, 45, 68, 99] [11, 2, 45, 68, 99]
                # 第2轮比较 j 0~3:[11, 45, 2, 68, 99] [11, 2, 45, 68, 99] [11, 2, 45, 68, 99]
                # 第3轮比较 j 0~2:[2, 11, 45, 68, 99] [2, 11, 45, 68, 99]
                # 第4轮比较 j 0~1:[2, 11, 45, 68, 99]
                list1[j], list1[j + 1] = list1[j + 1], list1[j]  # 交换位置
                # list1[j + 1] = list1[j]
                # list1[j] = list1[j + 1]

    print(list1)#[2, 11, 45, 68, 99]

def test6():
    list1 = [11, 45, 2, 68, 99]
    list1.sort()
    print(list1)
    list2=sorted(list1)
    print(list2)
    list1.reverse()
    print(list1)

    data = [(1, 3), (4, 1), (2, 2), (3, 4)]
    data.sort(key=lambda x:x[1])
    print(data)

    n=len(list1)
    for i in range(0,n):
        for j in range(0,n-i-1):
            list1[j],list1[i+1]=list1[j+1],list1[j]
    print(list1)

def test7():
    list1 = [11, 45, 2, 68, 99]
    list1.sort()
    print(list1)

    print(sorted(list1, reverse=False))

    data = [(1, 3), (4, 1), (2, 2), (3, 4)]
    data.sort(key=lambda x:x[1])
    print(data)

    words = ["apple", "banana", "kiwi", "cherry"]
    words.sort(key=lambda x: x[-1])
    print(words)

def test8():
    list1 = [11, 45, 2, 68, 99]
    list1.sort(reverse=False)
    print(list1)
    print(sorted(list1,reverse=True))

    data = [(1, 3), (4, 1), (2, 2), (3, 4)]
    data.sort(key=lambda x:x[-1])
    print(data)

    words = ["apple", "banana", "kiwi", "cherry"]
    words.sort(key=lambda x:x[-1])
    print(words)