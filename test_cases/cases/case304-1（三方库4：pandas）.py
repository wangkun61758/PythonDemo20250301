#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/2/16 1:57
=================================================='''
import pandas as pd
import numpy as np

def test1():
    #     Name   Age
    # 0    Tom   25
    # 1   John   30
    # 2  Emily   28
    data = {'Name': ['Tom', 'John', 'Emily'], 'Age': [25, 30, 28]}
    df = pd.DataFrame(data)
    print(df.head(3))  # 显示前几行数据(不输入数字显示全部数据)


def test2():
    # np.random.randn(a, b) 生成a*b维的随机数，且该数服从标准正太分布（np.random.randn()返回一个或一组服从“0~1”均匀分布的随机样本值）
    # 第一个参数是存放在DataFrame里的数据，第二个参数index就是之前说的行名，第三个参数columns是之前说的列名
    #           A         B         C
    # a -0.612978  0.237191  0.312969
    # b -1.281485  1.135944  0.162456
    # c  2.232905  0.200209  0.028671
    df1 = pd.DataFrame(np.random.randn(3, 3), index=list('abc'), columns=list('ABC'))
    print(df1)

    #       A         B         C         D
    # a  1.296851 -1.115277  0.303265  2.339364
    # b -1.454742 -0.026442 -0.744811 -1.472689
    # c  0.671877 -0.293015 -0.250978  1.474022
    # d -0.206824 -0.460824  0.795805 -2.971934
    # np.random.randn(a, b) 生成a*b维的随机数，且该数服从标准正太分布（可以有若干个参数）
    df2 = pd.DataFrame(np.random.randn(4, 4), index=list('abcd'), columns=list('ABCD'))
    print(df2)
    #      A          B          C
    # a 2.396999   2.396999   2.396999
    # b 2.396999   2.396999   2.396999
    # c 2.396999   2.396999   2.396999
    # d 2.396999   2.396999   2.396999
    df3 = pd.DataFrame(np.random.uniform(4), index=list('abcd'), columns=list('ABC'))
    print(df3)

    df4 = np.random.randint(5, size=(2, 4))
    print(df4)
    df5 = np.random.randn(4, 4)
    print(df5)
