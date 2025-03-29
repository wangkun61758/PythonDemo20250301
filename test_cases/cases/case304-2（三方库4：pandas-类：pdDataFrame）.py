#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/3/13 0:21
=================================================='''
import numpy as np
import pandas as pd


def test1():
    # 创建水果列表
    fruits = ['苹果', '香蕉', '橙子']

    # 随机生成包含 20 行的 DataFrame
    df1 = pd.DataFrame({
        '水果': np.random.choice(fruits, 20),
        '数量': np.random.randint(1, 10, 20),  # 生成随机数量
        '价格': np.random.uniform(1.0, 10.0, 20)  # 生成随机价格
    })

    print(df1['水果'])
    print(set(df1['水果']))  # {'橙子', '苹果', '香蕉'}
    print(df1['数量'])
    print(set(df1['数量']))
    print(df1['价格'])
    print(set(df1['价格']))
    print(df1['水果'].unique())  # ['香蕉' '橙子' '苹果']