#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/3/28 17:59
=================================================='''
import pandas as pd

def query_excel(file_path, sheet_name=0, **conditions):
    """
    查询 Excel 文件中的数据。
    :param file_path: Excel 文件的路径
    :param sheet_name: 要查询的工作表名称或索引，默认为 0（第一个工作表）
    :param conditions: 查询条件，键为列名，值为要匹配的值
    :return: 符合条件的数据
    """
    try:
        # 读取 Excel 文件
        datafile = pd.read_excel(file_path, sheet_name=sheet_name)
        # 构建查询条件
        query_str = " and ".join([f"`{col}` == {repr(val)}" for col, val in conditions.items()])
        # print(query_str)#`类别` == '护理类' and `品牌` == 'babycare皇室狮子王 - 纸尿裤'
        if query_str:
            # 根据条件筛选数据
            result = datafile.query(query_str)
        else:
            # 如果没有提供条件，则返回全量数据
            result = datafile
        return result
    except Exception as e:
        print(f"查询过程中出现错误: {e}")
        return None

# 示例用法
if __name__ == "__main__":
    file_path = "../../resources/data1.xlsx"
    # 查询条件，这里表示查询 类别 列值为 '护理类' 且 品牌 列值为 babycare皇室狮子王 - 纸尿裤 的数据
    conditions = {
        "类别": "护理类",
        "品牌": "babycare皇室狮子王 - 纸尿裤"
    }
    result = query_excel(file_path, conditions)
    if result is not None:
        if not result.empty:
            print("查询结果:")
            print(result)
        else:
            print("未找到符合条件的数据。")