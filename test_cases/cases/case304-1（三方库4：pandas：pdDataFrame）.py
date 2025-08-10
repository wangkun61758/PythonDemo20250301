#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/2/16 1:57
=================================================='''
import pandas as pd

def test1():
    #     Name   Age
    # 0    Tom   25
    # 1   John   30
    # 2  Emily   28
    data = {'Name': ['Tom', 'John', 'Emily'], 'Age': [25, 30, 28]}
    df = pd.DataFrame(data)
    print(df.head(3))  # 显示前几行数据(不输入数字显示全部数据)


