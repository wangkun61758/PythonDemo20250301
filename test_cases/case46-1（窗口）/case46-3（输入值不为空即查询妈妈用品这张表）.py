#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2024/2/25 20:03
@Desc   ：
@Project -> File   ：case509-4（爬取搜索页商品主图）（爬取淘宝好评中的视频和图片）.py -> case46-1（窗口）（查询excel文件）
=================================================='''
import tkinter as tk
from tkinter import messagebox

import openpyxl
'''
只要输入值不为空，就去查询‘妈妈用品’这张表
1、创建窗口
2、点击按钮要去执行的函数
3、查询excel
'''
'''
3、查询excel
'''


def excel(str1):
    file1 = openpyxl.load_workbook('../../resources/data1.xlsx')
    sheet = file1[str1]
    sum = 0
    for i in sheet.iter_rows():
        for cell in i:
            if i[(cell.column) - 1].value == '护理类':
                m = i[4].value
                sum = sum + m
    print(sum)  # 533.96


'''
2、点击按钮要去执行的函数
'''


def submit2():
    input1 = entry1.get()  # 获取文本框1输入框的值

    if len(input1) != 0:
        a = '妈妈用品'
        excel(a)

    else:
        result = f"输入结果：\n{input1}"
        messagebox.showinfo("提交成功", result)


'''
1、创建窗口
'''
# 1、创建主窗口
window = tk.Tk()  # 初始化
window.title("输入框示例")  # 给窗口的可视化起名字

# 2.1、在图形界面上设定标签
label1 = tk.Label(window, text="输入内容1：")
# 2.2、把标签放到窗口上去
label1.pack()
# 3.1、创建单行可输入文本框1
entry1 = tk.Entry(window)
# entry1 = tk.Entry(window,show='*')
# 3.2、把输入框放到窗口上去
entry1.pack()

'''
4.1、创建查询按钮
'''
button = tk.Button(window, text="提交", command=submit2)  # command=submit2  —— 点击按钮要去执行的函数：submit2（即要去执行的操作）
# 4.2、把提交按钮放到窗口上去
button.pack()
# 运行窗口
window.mainloop()
