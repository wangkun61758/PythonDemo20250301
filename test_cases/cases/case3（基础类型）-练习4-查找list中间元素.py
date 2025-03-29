#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/7/11 21:07
=================================================='''

from collections import OrderedDict
def test1():
    list = [56, 25, 21, 12, 3, 4, 25, 12]
    new_list = sorted(list)  # 列表排序
    print(new_list)
    lenth = len(list)
    if lenth % 2 == 0:
        n = int(lenth / 2)
        print(str(new_list[n - 1]) + '   ' + str(new_list[n]))
    else:
        m = int(lenth / 2)
        print(new_list[m])
def test2():
    # 创建一个有序字典并去重
    keys = [1, 2, 3, 2, 1, 3]
    ordered_dict = OrderedDict.fromkeys(keys)
    print(ordered_dict)#OrderedDict([(1, None), (2, None), (3, None)])


