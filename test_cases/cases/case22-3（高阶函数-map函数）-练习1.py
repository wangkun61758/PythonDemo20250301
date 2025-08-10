#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/7/8 22:49
=================================================='''

numbers2 = [1, 2, 3, 4, 5]
# 直接在map中使用lambda表达式
a2 = list(map(lambda x: x * x, numbers2))
print(a2)
