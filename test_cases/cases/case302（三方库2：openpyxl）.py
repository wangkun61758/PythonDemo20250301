#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/2/7 15:57
=================================================='''
import openpyxl  # 导入对应的库 —— openpyxl
def test():
    file1 = openpyxl.load_workbook('../../resources/data1.xlsx')  # 打开指定的.xlsx文件
    sheet1 = file1['妈妈用品']  # 打开.xlsx文件中指定的表
    list1 = []
    '''
    openpyxl 库并不支持直接复制单元格对象从一个工作表到另一个工作表。当你尝试将一个工作表中的单元格对象直接添加到另一个工作表时，openpyxl 会抛出“cells cannot be copied from other worksheets”的错误。
    这是因为 openpyxl 的设计不允许跨工作表复制单元格对象，需要设置values_only=True参数用于仅返回单元格的值而不包括其他信息
    '''
    for row in sheet1.iter_rows(values_only=True):  # 按行遍历.xlsx文件（values_only=True参数用于仅返回单元格的值而不包括其他信息）
        list1.append(row)  # 将遍历到的每一行作为一个数据添加到list列表
    print(f'读取的文件内容是{list1}:类型是{type(list1)}')

    workbook2 = openpyxl.Workbook()  # 创建一个新的工作簿对象
    worksheet2 = workbook2.active  # 激活当前sheet工作簿对象
    for row in list1:
        worksheet2.append(row)  # 将list列表中的数据加入到sheet工作簿对象
    workbook2.save('../resources/abc/file1.xlsx')  # 保存工作簿到文件
'''
1、读取指定行列的数据
'''
def test1():
    file1 = openpyxl.load_workbook('../../resources/data1.xlsx')
    sheet1 = file1['妈妈用品']
    cell1 = sheet1.cell(row=2, column=3)
    print(cell1.value)
'''
2、遍历所有行（根据筛选条件）
'''
def test2():
    file1 = openpyxl.load_workbook('../../resources/data1.xlsx')
    sheet1 = file1['妈妈用品']
    for row in sheet1.iter_rows(min_row=1, max_row=3, values_only=True):
        print(row)
    print("\n11111111111111111111111111111\n")
    '''
    iter_rows()函数用于遍历所有行;
    通过设置min_row参数来指定从哪一行开始读取数据;
    values_only=True参数用于仅返回单元格的值而不包括其他信息;
    '''
    for row in sheet1.iter_rows(min_row=2, values_only=True):  #
        print(row)
'''
3、遍历所有列（根据筛选条件）
'''
def test3():
    file3 = openpyxl.load_workbook('../../resources/data1.xlsx')
    sheet3 = file3['妈妈用品']
    for column in sheet3.iter_cols(min_col=2, max_col=5, values_only=True):
        print(column)
'''
4、读取符合条件的某一列的值
'''
def test4():
    file = openpyxl.load_workbook('../../resources/data1.xlsx')
    sheet = file['妈妈用品']

    sum = 0
    for i in sheet.iter_rows():#遍历每一行
        for cell in i:#遍历每一行中的每个单元格
            if i[(cell.column) - 1].value == '护理类':#第一个单元格的下标为0
                m = i[4].value#取列的值为'护理类'的这一行的下标为4对应的值
                sum = sum + m
    print(sum)
def test5():
    file1=openpyxl.load_workbook('../../resources/data1.xlsx')
    sheet1=file1['妈妈用品']
    list1=[]
    for row in sheet1.iter_rows(values_only=True):
        list1.append(row)
    print(list1)
    book1=openpyxl.Workbook()
    sheet1=book1.active

    for row in list1:
        sheet1.append(row)  # 将list列表中的数据加入到sheet工作簿对象
    book1.save('../resources/abc/file1.xlsx')  # 保存工作簿到文件

    file2=openpyxl.load_workbook('../../resources/data1.xlsx')
    sheet2=file2['妈妈用品']
    sum=0
    for i in sheet2.iter_rows():
        for cell in i:
            if i[cell.column-1].value=='护理类':
                m=i[4].value
                sum=sum+m
    print(sum)
def test6():
    file1=openpyxl.load_workbook('../../resources/data1.xlsx')
    sheet1=file1['妈妈用品']
    list1=[]
    sum=0
    for row1 in sheet1.iter_rows(values_only=True):
        list1.append(row1)
    for row2 in sheet1.iter_rows():
        for cell in row2:
            if row2[cell.column-1].value=='护理类':
                m=row2[4].value
                sum=sum+m

    print(sum)

    workbook2 = openpyxl.Workbook()  # 创建一个新的工作簿对象
    worksheet2 = workbook2.active  # 激活当前sheet工作簿对象
    for row in list1:
        worksheet2.append(row)  # 将list列表中的数据加入到sheet工作簿对象
    workbook2.save('../resources/abc/file1.xlsx')  # 保存工作簿到文件