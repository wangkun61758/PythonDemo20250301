#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/11/30 19:53
=================================================='''
import random

import requests
from PIL import Image
from matplotlib import pyplot as plt


def test1():
    list1 = ['https://img.alicdn.com/imgextra/i2/O1CN016zDZ712JUFPEIIDvb_!!0-rate.jpg',
             ['https://img.alicdn.com/imgextra/i2/O1CN016zDZ712JUFPEIIDvb_!!0-rate.jpg',
              'https://img.alicdn.com/imgextra/i1/O1CN01MmclKY2JUFPGxj5x9_!!0-rate.jpg',
              'https://img.alicdn.com/imgextra/i3/O1CN01tl2Wfu1sBvwDL7TTI_!!0-rate.jpg',
              'https://img.alicdn.com/imgextra/i4/O1CN01PC6igB1OXyWdK2TpU_!!0-rate.jpg'],
             'https://img.alicdn.com/imgextra/i1/O1CN01MmclKY2JUFPGxj5x9_!!0-rate.jpg',
             'https://img.alicdn.com/imgextra/i1/O1CN01QfUSIX2JUFPEbNCdm_!!0-rate.jpg']

    '''
    1、遍历获取到的list集合（此处是list4对象）,考虑list集合中的值的类型，是否有“字符串”和“list集合”混合组成list的情况
    '''
    for i in range(0, len(list1)):
        for j in range(0, len(list1[i])):
            # 1.1、若读取到的list中的值是string形式
            if isinstance(list1[i], str):
                # print('这个是字符：' + str(list1[i]))

                str1_url = list1[i]
                # print('读取的url1:' + str(str1_url))

                headers = {
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36"
                }

                response = requests.get(str1_url, headers=headers)  # 获取图片

                ran1 = random.randint(1000000000, 9999999999)
                image_path = '../../resources/image/image' + str(ran1) + '字符.jpg'
                with open(image_path, "wb") as f:  # wb:写入二进制文件
                    f.write(response.content)  # 写入图片
                    f.close()
                break
            # 1.2、若读取到的list中的值不是string形式（此处是一个list集合）
            else:
                str1_url = list1[i][j]

                print('读取的url2:' + str(str1_url))

                headers = {
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36"
                }

                response = requests.get(str1_url, headers=headers)  # 获取图片

                ran1 = random.randint(10000000000, 99999999999)
                image_path = '../../resources/image/image' + str(ran1) + '.jpg'
                with open(image_path, "wb") as f:  # wb:写入二进制文件
                    f.write(response.content)  # 写入图片
                    f.close()

                img = Image.open(image_path)
                plt.figure(str(ran1) + '.jpg')
                plt.imshow(img)
                plt.show()

                print("图片下载完成2")
