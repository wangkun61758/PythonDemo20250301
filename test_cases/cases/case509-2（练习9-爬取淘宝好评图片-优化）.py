#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2024/7/12 22:15
=================================================='''
import json
import os
import random

import requests
from PIL import Image
from matplotlib import pyplot as plt


def test1():
    url = "https://h5api.m.tmall.com/h5/mtop.alibaba.review.list.for.new.pc.detail/1.0/?jsv=2.7.2&appKey=12574478&t=1720873395360&sign=5eb12d10241b3a21f511515eef85b73d&api=mtop.alibaba.review.list.for.new.pc.detail&v=1.0&isSec=0&ecode=0&timeout=20000&ttid=2022%40taobao_litepc_9.17.0&AntiFlood=true&AntiCreep=true&preventFallback=true&type=jsonp&dataType=jsonp&callback=mtopjsonp14&data=%7B%22itemId%22%3A%22758204209094%22%2C%22bizCode%22%3A%22ali.china.tmall%22%2C%22channel%22%3A%22pc_detail%22%2C%22pageSize%22%3A20%2C%22pageNum%22%3A1%2C%22rateType%22%3A7%7D"

    payload = {}
    headers = {
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'cna=uCYYH5oMLVcCAW/E9mu8OKfo; xlly_s=1; lid=%E4%B9%8C%E5%B8%82%E5%9B%9E%E5%BF%86; wk_cookie2=105c4d8dfd4cf78405ebc65c25fa3f43; wk_unb=VWZ7qlhAfso0; dnk=%5Cu4E4C%5Cu5E02%5Cu56DE%5Cu5FC6; tracknick=%5Cu4E4C%5Cu5E02%5Cu56DE%5Cu5FC6; lgc=%5Cu4E4C%5Cu5E02%5Cu56DE%5Cu5FC6; cookie2=1557680b4d10c6c946feffdc92341577; t=300611ee53f706e25e0c382e00eb92a1; sn=; _tb_token_=5e73d15e40801; mtop_partitioned_detect=1; _m_h5_tk=6a4e9c3b61a1b4303b17abcfe3c8f431_1720880442400; _m_h5_tk_enc=afa91b609c3aefbca15c0d160a3b7b22; uc1=cookie21=Vq8l%2BKCLiv0NZbsVmuOI%2Bw%3D%3D&cookie15=URm48syIIVrSKA%3D%3D&cookie14=UoYcA8A1%2BE9Kgg%3D%3D&existShop=false&cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&pas=0; uc3=nk2=rUPBFbEsoPk%3D&lg2=UtASsssmOIJ0bQ%3D%3D&id2=VWZ7qlhAfso0&vt3=F8dD3i%2FM2FXbpwTIHqI%3D; _l_g_=Ug%3D%3D; uc4=id4=0%40V8exE%2Fcl8j99gxPvZ%2FhY1EscXfs%3D&nk4=0%40r7Il6uDfeekOhfD8YfznqcViQQ%3D%3D; unb=695573030; cookie1=V33DIKglYYC62IzdWcUS9oujtXZ%2Bg%2BnIj5%2BR%2B3nceLc%3D; login=true; cookie17=VWZ7qlhAfso0; _nk_=%5Cu4E4C%5Cu5E02%5Cu56DE%5Cu5FC6; sgcookie=E100%2BM7VXhc%2F%2BWxmF9wcSYc95hiK%2B7k9iglF14lSdITXfw4u3MpbOjUlH2MV9kOlFqae6Mu6o4h3A6rlNw2mlL3FEY2O2mtder6q5nbzSGeA0VOb7tPrBon7kvWk8y0euEhb; cancelledSubSites=empty; sg=%E5%BF%8606; csg=3fefb230; tfstk=fcmsGdiui1f_2nHQiPpUVbLGthrflfty5twxExINHlEThiMoGArqHSobcXcLkcrZQXtjEbaakmPqcOmINiSwsFDAcorvaQ-y4AXgmodr5QtPfN243OKVW5KYDIvkaQ-yYFBLcCOruzaawkw09ReYDGpQJR2_D-eTDpNLh8bA6jEvdvF3F-FYDGFdv-D9ABwH55H6dXhzbKKD8vVCDg6uCPIZLZ7AkheT77UdLiS2oRa_wAFBa8D5IyH0lmXccrktrj2-61dbiDMKX4hJTNPtP-MrlbpVSJzjjkNxX3X79cMjAP0F6Ne7f5a-XzKXFYUxRDZZXIboLvNTPkue-Cz4ffguZPLHtjMQ_jn_J1OUg4kEXyGJTMG0lqnavcdpVgyV47i4qZ6QriwQap9CoZry9Thdh4mOdPe3L0JBd1_0WJ2Qap9CoZ4TKJzydp11o; isg=BAYG--YqnIM9qEjkGF2gHgWfV_yIZ0ohAji3z_AsnC2_87YNWPcbMbHFyy8_20I5',
        'referer': 'https://detail.tmall.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'script',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    # print('访问好评的返回值:' + response.text)

    str1 = response.text
    max_length = len(str1)

    str2 = str1[13:max_length - 1]
    print('str2: ' + str2)

    dict2 = json.loads(str2)
    print('dict2(返回值可用的部分):' + str(dict2))

    list3 = dict2['data']['module']['reviewVOList']
    print('list3:' + str(list3))

    for i in range(len(list3)):
        print('i:' + str(i))

        '''
        3.1、遍历得到的视频集合
        '''
        for j in range(len(list3[i]['videoVOList'])):
            url = str(list3[i]['videoVOList'][j]['url'])
            print('url:' + str(url))
            headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36"
            }

            response = requests.get(url, headers=headers)  # 获取图片

            if not os.path.exists('../../resources/image89/video'):
                os.makedirs('../../resources/image89/video')

            ran1 = random.randint(1000000000, 9999999999)
            image_path = '../resources/image89/video/第' + str(i + 1) + '组的第' + str(j + 1) + '个视频' + str(
                ran1) + '.mp4'
            with open(image_path, "wb") as f:  # wb:写入二进制文件
                f.write(response.content)  # 写入图片
                f.close()
            print('第' + str(j) + '个视频下载完成')

        '''
        3.2、遍历得到的图片集合（此处是list4对象）：考虑list集合中的值的类型，是否有“字符串”和“list集合”混合组成list的情况
        '''
        for k in range(0, len(list3[i]['reviewPicPathList'])):
            for l in range(0, len(list3[i]['reviewPicPathList'][k])):
                '''
                3.2.1、若读取到的list中的值是string形式
                '''
                if isinstance(list3[i]['reviewPicPathList'][k], str):
                    print('这个是字符：' + str(list3[i]['reviewPicPathList'][k]))

                    str1_url = 'https:' + list3[i]['reviewPicPathList'][k]
                    print('读取的url1:' + str(str1_url))

                    headers = {
                        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36"
                    }

                    response2 = requests.get(str1_url, headers=headers)  # 获取图片
                    if not os.path.exists('../../resources/image89/picture'):
                        os.makedirs('../../resources/image89/picture')

                    ran1 = random.randint(1000000000, 9999999999)
                    image_path = '../resources/image89/picture/第' + str(i + 1) + '组的第' + str(
                        k + 1) + '个图片' + str(ran1) + '字符.jpg'
                    with open(image_path, "wb") as f:  # wb:写入二进制文件
                        f.write(response2.content)  # 写入图片
                        f.close()
                    print('第' + str(i + 1) + '组的第' + str(k + 1) + '个图片下载完成')
                    break

                # 3.2.2、若读取到的list中的值不是string形式（此处是一个list集合）
                else:

                    str1_url = 'https:' + list3[i]['reviewPicPathList'][k]
                    # print('读取的url2:' + str(str1_url))
                    '''
                    3.2.2.1、添加信息头，防止下载的图片裂开（为了避免被认为是爬取数据的）
                    '''
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36"
                    }

                    response = requests.get(str1_url, headers=headers)  # 获取图片
                    if not os.path.exists('../../resources/image89/picture'):
                        os.makedirs('../../resources/image89/picture')

                    ran1 = random.randint(10000000000, 99999999999)
                    image_path = '../resources/image89/picture/第' + str(i + 1) + '组的第' + str(
                        k + 1) + '个图片' + str(ran1) + '字符.jpg'

                    with open(image_path, "wb") as f:  # wb:写入二进制文件
                        f.write(response.content)  # 写入图片
                        f.close()
                    # '''
                    # 3.2.2.2、打开对应的图片预览
                    # '''
                    # img = Image.open(image_path)
                    # plt.figure(str(ran1) + '.jpg')  # 创建自定义图像
                    # plt.imshow(img)
                    # plt.show()
