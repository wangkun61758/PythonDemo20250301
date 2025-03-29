#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/11/24 21:22
=================================================='''
from PIL import Image
import  matplotlib.pyplot as plt

def test1():
    image=Image.open('../../resources/image/2013-07-04 (1).jpg')
    image.show()

# def test2():
#     x = [0, 1, 2, 3, 4, 5,6]
#     y = [0, 2, 4, 6, 8, 10,12]
#     plt.plot(x, y)  # 绘制图片
#     plt.savefig('../../resources/image/2013-07-04 (7).jpg')  # 将图片存储在resources文件夹下并命名为2013-07-04 (7).jpg  ，注意该行代码要放在plt.show()前
#     # plt.show()
