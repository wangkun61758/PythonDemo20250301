#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/11/29 22:25
=================================================='''
import os.path
import random

import requests
from PIL import Image
from matplotlib import pyplot as plt


def test():
    # 定义要获取的PNG图像文件的URL
    url = "https://img.alicdn.com/imgextra/i2/O1CN01WviydN1X43Bu4jjTL_!!0-rate.jpg"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    if not os.path.exists('../../resources/image3'):
        os.makedirs('../../resources/image3')

    ran1 = random.randint(10000000000, 99999999999)
    image_path = '../../resources/image3/P' + str(ran1) + '.jpg'
    with open(image_path, "wb") as f:  # wb:写入二进制文件
        f.write(response.content)  # 写入图片
        f.close()

    img = Image.open(image_path)
    '''
    在使用 `plt.show()` 函数显示图像后，还需要调用 `plt.show()` 函数将图像显示在屏幕上
    '''
    plt.imshow(img)  # 显示图像
    plt.show()  # 将图像显示在屏幕上
