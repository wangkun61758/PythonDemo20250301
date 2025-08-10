#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/11/24 21:22
=================================================='''
from PIL import Image
import matplotlib.pyplot as plt


def test1():
    image = Image.open('../../resources/image/2013-07-04 (1).jpg')
    image.show()

