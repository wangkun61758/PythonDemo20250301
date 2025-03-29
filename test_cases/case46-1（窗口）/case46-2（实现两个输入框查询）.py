#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2024/2/25 19:13
@Desc   ：
@Project -> File   ：case509-4（爬取搜索页商品主图）（爬取淘宝好评中的视频和图片）.py -> case46-1（窗口）（查询）
=================================================='''
import tkinter as tk
from tkinter import messagebox


def submit2():
    input1 = entry1.get()  # 获取第一个输入框的值
    input2 = entry2.get()  # 获取第二个输入框的值

    if len(input1) == 0 or len(input2) == 0:
        messagebox.showerror("错误", "请确保所有字段都不为空！")
    else:
        result = f"输入结果：\n{input1}\n{input2}"
        messagebox.showinfo("提交成功", result)


# 1、创建主窗口
window = tk.Tk()  # 初始化
window.title("输入框示例")  # 给窗口的可视化起名字

# 2.1、在图形界面上设定标签
label1 = tk.Label(window, text="输入内容1：")
# 2.2、把标签放到窗口上去
label1.pack()
# 3.1、创建单行可输入文本框
entry1 = tk.Entry(window)
# entry1 = tk.Entry(window,show='*')
# 3.2、把输入框放到窗口上去
entry1.pack()

label2 = tk.Label(window, text="输入内容2：")
label2.pack()
entry2 = tk.Entry(window)
entry2.pack()


# 4.1、创建查询按钮
button = tk.Button(window, text="提交", command=submit2)
# 4.2、把提交按钮放到窗口上去
button.pack()
# 运行窗口
window.mainloop()
