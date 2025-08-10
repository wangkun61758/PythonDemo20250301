import os
from datetime import datetime
import pandas as pd


def test1():
    os.chdir(f'../resources/')
    list_dir = os.listdir(f'../resources/')
    for file in list_dir:
        # pd.set_option('display.max_colums', 9)
        # pd.set_option('display.max_rows', 18)
        pd.set_option('display.max_rows', 18)  # 设置展示的最大行数，以免打印时展示...(设置后可以完整展示内容)
        pd.set_option('display.max_columns', 9)  # 设置展示的最大列数，以免打印时展示...(设置后可以完整展示内容)
        df_file = pd.read_excel(file, sheet_name=None, engine='openpyxl')
        sheetname_list = list(df_file.keys())[0:1]
        print(sheetname_list)

        df2 = pd.DataFrame()
        for sheetname in sheetname_list:
            df1 = pd.read_excel(file, sheet_name=sheetname, header=5, usecols=[1, 2, 3, 4, 5, 6]).fillna(
                method='backfill', axis=0)
            print(df1)
            df2 = df2._append(df1)
            print(df2)

        df2.dropna(axis=0, how='all', inplace=True)
        df2['用例名称'] = df2['测试模块'] + '-' + df2['用例名称']

        df2.drop('测试模块', axis='columns', inplace=True)

        df2['操作步骤'] = df2['操作步骤'].str.replace('.', '、', regex=False)
        df2['预期结果'] = df2['预期结果'].str.replace('.', '、', regex=False)
        df2.columns = ['优先级', '用例标题', '前置条件', '步骤', '预期']
        df2 = df2[['用例标题', '前置条件', '优先级', '步骤', '预期']]

        df2.insert(0, 'name', 'wk', allow_duplicates=True)
        df2.insert(1, '时间', '2025', allow_duplicates=True)

        time1 = datetime.now().strftime('%Y-%m %d %H-%M-%S')
        path = f'../data/' + time1 + '.xlsx'
        df2.to_excel(path, sheet_name='df测试', index=False)
