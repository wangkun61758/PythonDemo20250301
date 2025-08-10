#!/usr/bin/python
# *-* encoding:utf-8 *-*

import os
from datetime import datetime
import pandas as pd

os.chdir('../resources/')  # 更新工作目录到excel文件路径

list_dir = os.listdir('../resources/')  # 遍历目录下的文件
for file in list_dir:
    pd.set_option('display.max_rows', 18)  # 设置展示的最大行数，以免打印时展示...(设置后可以完整展示内容)
    pd.set_option('display.max_columns', 9)  # 设置展示的最大列数，以免打印时展示...(设置后可以完整展示内容)
    df_file = pd.read_excel(file, sheet_name=None, engine='openpyxl')
    sheetname_list = list(df_file.keys())[0:1]

    df2 = pd.DataFrame()  # 创建DataFrame对象
    for sheetname in sheetname_list:
        df1 = pd.read_excel(file, sheet_name=sheetname, header=5, usecols=[1, 2, 3, 4, 5, 6]).fillna(method='backfill',
                                                                                                     axis=0)
        df2 = df2._append(df1)

    df2.dropna(axis=0, how='all', inplace=True)
    df2 = df2.drop_duplicates(keep='first')  # 删除重复行（'first'：保留第一次出现的重复项（默认值））

    df2['用例名称'] = df2['测试模块'] + '-' + df2['用例名称']

    df2.drop('测试模块', axis='columns', inplace=True)  # axis='columns' 按列删除 / inplace=True：直接修改原数据，不返回新的 DataFrame

    df2['用例名称'] = df2['用例名称'].str.replace('-0', '', regex=False)
    df2['操作步骤'] = df2['操作步骤'].str.replace('.', '、', regex=False)
    df2['预期结果'] = df2['预期结果'].str.replace('.', '、', regex=False)
    df2['操作步骤'] = '1. ' + df2['操作步骤']
    df2['预期结果'] = '1. ' + df2['预期结果']
    df2['优先级'] = df2['优先级'].str.replace('冒烟', '1', regex=False)
    df2['优先级'] = df2['优先级'].str.replace('高', '2', regex=False)
    df2['优先级'] = df2['优先级'].str.replace('中', '3', regex=False)
    df2['优先级'] = df2['优先级'].str.replace('低', '4', regex=False)
    df2['优先级'] = df2['优先级'].fillna('3')

    df2.columns = ['优先级', '用例标题', '前置条件', '步骤', '预期']
    df2 = df2[['用例标题', '前置条件', '优先级', '步骤', '预期']]

    df2.insert(0, '所属产品', '类脑光伏新能源智慧管控平台', allow_duplicates=False)
    df2.insert(1, '所属模块', '/巡视任务(#117)', allow_duplicates=False)
    df2.insert(2, '相关研发需求', '巡视任务页面功能开发(#19)', allow_duplicates=False)
    df2.insert(5, '关键词', '', allow_duplicates=False)
    df2.insert(7, '用例类型', '功能测试', allow_duplicates=False)
    df2.insert(8, '适用阶段', '功能测试阶段', allow_duplicates=False)
    df2.insert(9, '用例状态', '正常', allow_duplicates=False)
    print('\n3.17、插入固定的列：\n' + str(df2.to_string()))

    time1 = datetime.now().strftime('%Y-%m %d %H-%M-%S')
    filepath = f'../data/' + time1 + '.xlsx'

    df2.to_excel(filepath, sheet_name='用例', index=False)
