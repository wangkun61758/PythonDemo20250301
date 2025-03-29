#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2024/2/26 22:00
@Desc   ：
@Project -> File   ：case509-4（爬取搜索页商品主图）（爬取淘宝好评中的视频和图片）.py -> case46-1（窗口）-6
=================================================='''
import tkinter as tk


def show():
    '''
    作品：《1》
    作者：2
    :return:
    '''
    print("作品：《%s》" % e1.get())
    print("作者：%s" % e2.get())

    e1.delete(0, "end")
    e2.delete(0, "end")


def quit():
    window.destroy()


window = tk.Tk()

# 生成两个 Label，显示作品和作者
tk.Label(window, text="作品：").grid(row=0, column=0)  # grid是把组件按照表格来安排，row是行，column是列
tk.Label(window, text="作者：").grid(row=1, column=0)  # ipadx/ipady 填充表格框，让表格框在X/Y方向上变胖,决定组件跟邻近表格线或窗体边界的距离
e1 = tk.Entry(window)
e2 = tk.Entry(window)

e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)

tk.Button(window, text="获取信息", width=10, command=show).grid(row=3, column=0, sticky="w", padx=10, pady=5)
tk.Button(window, text="退出", width=10, command=quit).grid(row=3, column=1, sticky="e", padx=10,
                                                            pady=5)  # 退出就直接调用窗口的 quit() 方法

window.mainloop()
