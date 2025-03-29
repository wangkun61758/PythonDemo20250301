#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/12/3 10:32
@Desc   ：
@Project -> File   ：PythonDemo20231201 -> test
=================================================='''
import tkinter as tk
from test_cases.case47.TbQuery import get_evaluate


# 3.1.2 执行查询函数
def get_input():
    # 3.1.2.1 获取输入框1中的内容
    input_text1 = input1.get()
    # 3.1.2.2 获取输入框2中的内容
    input_text2 = input2.get()
    # 3.1.2.3 调取函数，同时传入参数
    get_evaluate(input_text1, input_text2)


# 1、创建主窗口
window = tk.Tk()
window.title("Python查询功能")
# 2.1.1、创建输入框1
input1 = tk.Entry(window)
# 2.1.2、把【输入框1】放到窗口上去
input1.pack()
# 2.2.1、创建输入框2
input2 = tk.Entry(window)
# 2.2.2、把【输入框2】放到窗口上去
input2.pack()

# 3.1.1、创建查询按钮（窗口、文案、执行的命令）
button = tk.Button(window, text="查询", command=get_input)
# 3.2、把【按钮】放到窗口上去
button.pack()
# 4、运行窗口
window.mainloop()
