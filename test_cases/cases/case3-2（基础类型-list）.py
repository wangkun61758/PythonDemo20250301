#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/2/12 22:54
=================================================='''

def test1():
    list1 = ['hameimei', 'lilei', 'lisi', 'zhagnsan', 'zhaoer', 'wangwu']
    list1.append('wk')  # 添加元素
    print(list1)  # ['hameimei', 'lilei', 'lisi', 'zhagnsan', 'zhaoer', 'wangwu', 'wk']
    list1.extend('王五')  # extend是将可迭代对象中的每个元素逐一添加到列表尾部
    print(list1)  # ['hameimei', 'lilei', 'lisi', 'zhagnsan', 'zhaoer', 'wangwu', 'wk', '王', '五']
    list1.sort(reverse=False)  # 按照元素本身升序排列
    print(list1)  # ['hameimei', 'lilei', 'lisi', 'wangwu', 'wk', 'zhagnsan', 'zhaoer', '五', '王']
    print(sorted(list1, reverse=False))  # ['hameimei', 'lilei', 'lisi', 'wangwu', 'wk', 'zhagnsan', 'zhaoer', '五', '王']
    list1.pop(0)  # 删除索引指定的元素,并将删除元素返回
    print(list1)  # ['lilei', 'lisi', 'wangwu', 'wk', 'zhagnsan', 'zhaoer', '五', '王']
    list1.remove('lilei')  # 删除列表中第一个匹配元素，若没有找到匹配元素会报错
    list2 = [11, 3, 67, 2, -6, 18, 36]
    print(list2.sort(key=lambda x: abs(x)))  # [2, 3, -6, 11, 18, 36, 67]
    print(list2.count(11))  # 1
    list2.insert(2, '清华')  # 在指定位置插入一个元素
    print(list2)  # [2, 3, '清华', -6, 11, 18, 36, 67]
    print(list2.copy())  # list.copy() 方法没有参数，返回一个新的列表，这个新列表与原列表在内存地址上不同，但包含相同的元素 [2, 3, '清华', -6, 11, 18, 36, 67]
    list2.reverse()
    print(list2)  # [67, 36, 18, 11, -6, '清华', 3, 2]
    print(list2.index(67, 0, 6))  # [67, 36, 18, 11, -6, '清华', 3, 2]
    list2.clear()
    print(list2)  # []

    list3 = [2, 7, 11, 15]
    print(list3[1:])  # [7, 11, 15]
    print([0, (list3[1:].index(7)) + (0 + 1)])  # [0, 1]
