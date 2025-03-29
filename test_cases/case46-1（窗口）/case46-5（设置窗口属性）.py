#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2024/2/26 21:36
@Desc   ：
@Project -> File   ：case509-4（爬取搜索页商品主图）（爬取淘宝好评中的视频和图片）.py -> case46-1（窗口）-5
=================================================='''
import tkinter as tk
from idlelib import search


def query():
    print('111')


window = tk.Tk()
window.title('查询')
window.geometry('500x300')
window['bg'] = 'yellow'

label1 = tk.Label(window, text='输入框1')
label1.pack()

entry1 = tk.Entry(window)
entry1.pack()

label2 = tk.Label(window, text='输入框2')
label2.pack()

entry2 = tk.Entry(window)
entry2.pack()

button = tk.Button(window, text='提交', command=query)
button.pack()

window.mainloop()
