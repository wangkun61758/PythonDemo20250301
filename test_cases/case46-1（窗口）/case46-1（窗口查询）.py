#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/12/3 9:34
@Desc   ：
@Project -> File   ：PythonDemo20231201 -> case46-1（窗口）
=================================================='''
import tkinter as tk
from idlelib import search


def test1():
    # 1、创建主窗口
    window = tk.Tk()
    window.title("Python查询功能")

    # 2、创建输入框
    # input = tk.Entry(window)
    '''
    https://blog.csdn.net/jzwalliser/article/details/128762107
    entry = tkinter.Entry(root,cursor="crosshair") #光标放在输入框上后样式为十字准心
    entry1 = tkinter.Entry(root,width=50) #长度约为50个英文字母
    entry = tkinter.Entry(root,font=("宋体",25,"italic"))#创建一个输入框，字体为宋体，字号25，斜体
    entry = tkinter.Entry(root,fg="red",bg="blue",selectbackground="black",selectforeground="white")#创建一个输入框，正常时蓝底红字，被选中的内容黑底白字
    entry = tkinter.Entry(root,show="*") #将输入的内容显示为"*"
    entry1 = tkinter.Entry(root,justify=tkinter.RIGHT) #靠右
    entry2 = tkinter.Entry(root,justify=tkinter.LEFT) #靠左
    entry3 = tkinter.Entry(root,justify=tkinter.CENTER) #居中
    input.select_from(0) #从第1个字符开始
    input.select_to(7) #一直选择到第8个字符
    '''
    input = tk.Entry(window, show="*", fg="red", bg="white", selectbackground="black", selectforeground="white")
    # 3、把输入框放到窗口上去
    input.pack()
    # 4、获取输入框中的内容
    # get_something = input.get()
    # print(get_something)
    # # 5、运行主循环
    # window.mainloop()

    # 4、获取输入框中的内容
    result = input.get()  # 获取输入框的值
    print("查询结果：" + result)
    # 创建查询按钮
    button = tk.Button(window, text="查询", command=search)
    button.pack()
    # 运行窗口
    window.mainloop()
