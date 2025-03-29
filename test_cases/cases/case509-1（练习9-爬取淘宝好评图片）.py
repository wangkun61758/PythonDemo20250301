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
    url = "https://h5api.m.tmall.com/h5/mtop.alibaba.review.list.for.new.pc.detail/1.0/?jsv=2.7.2&appKey=12574478&t=1720854402013&sign=90a5cef201663e158c4bddc5991794b7&api=mtop.alibaba.review.list.for.new.pc.detail&v=1.0&isSec=0&ecode=0&timeout=20000&ttid=2022%40taobao_litepc_9.17.0&AntiFlood=true&AntiCreep=true&preventFallback=true&type=jsonp&dataType=jsonp&callback=mtopjsonp7&data=%7B%22itemId%22%3A%22689137895471%22%2C%22bizCode%22%3A%22ali.china.tmall%22%2C%22channel%22%3A%22pc_detail%22%2C%22pageSize%22%3A20%2C%22pageNum%22%3A1%2C%22rateType%22%3A7%7D"

    payload = {}
    headers = {
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'cna=uCYYH5oMLVcCAW/E9mu8OKfo; xlly_s=1; lid=%E4%B9%8C%E5%B8%82%E5%9B%9E%E5%BF%86; wk_cookie2=105c4d8dfd4cf78405ebc65c25fa3f43; wk_unb=VWZ7qlhAfso0; dnk=%5Cu4E4C%5Cu5E02%5Cu56DE%5Cu5FC6; tracknick=%5Cu4E4C%5Cu5E02%5Cu56DE%5Cu5FC6; lgc=%5Cu4E4C%5Cu5E02%5Cu56DE%5Cu5FC6; cookie2=1716f1e84bb32caaef9208e473182668; t=300611ee53f706e25e0c382e00eb92a1; sn=; _tb_token_=5f073e5ebe6be; mtop_partitioned_detect=1; _m_h5_tk=e050318b6f76606cb19ab521174b4691_1720863009154; _m_h5_tk_enc=40468ccc5fb1fb771f82ed5d338adaac; uc1=pas=0&existShop=false&cookie15=V32FPkk%2Fw0dUvg%3D%3D&cookie14=UoYcA8A3pns3VQ%3D%3D&cookie21=WqG3DMC9Edo0nJdq6ehNCQ%3D%3D&cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D; uc3=vt3=F8dD3i%2FM2ptmCSdOYCc%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D&id2=VWZ7qlhAfso0&nk2=rUPBFbEsoPk%3D; _l_g_=Ug%3D%3D; uc4=nk4=0%40r7Il6uDfeekOhfD8YfzlNwn2Mg%3D%3D&id4=0%40V8exE%2Fcl8j99gxPvZ%2FhY1p9tC5g%3D; unb=695573030; cookie1=V33DIKglYYC62IzdWcUS9oujtXZ%2Bg%2BnIj5%2BR%2B3nceLc%3D; login=true; cookie17=VWZ7qlhAfso0; _nk_=%5Cu4E4C%5Cu5E02%5Cu56DE%5Cu5FC6; sgcookie=E100QZxai89CmcjSjOQdUOyf0DbsVJ0N0DxfFK%2BFF%2B34vVVzHzpVvmvOKMfvC47bIzUOw76vmHwHk%2FNHDMrAClik2ARRWcH%2BCaxbXhX8elgu3vb3JIonwimJ9tMGctP40%2FoE; cancelledSubSites=empty; sg=%E5%BF%8606; csg=09d530e4; tfstk=fS2oi9m_D7l7jCxdr-D5OaEvXQfYPUMI-ypKJv3Fgqubp73dN9jnollRVyULi244o4r-Jgw3izZZwyqCVDuU8y0LwsBTVuMILNUhBOE70aTsYWcEToSE2cK-2Ov4VuMBcnLF6SrWt601v8kU8xlqAckE4puPmxotqvJrTLR2uqiEL2zEaI-qY08E8Dke3b7Ra4wU3-7lAKXKbAsa30co-p3DKoeXBbgZ5qJF7Jmk5VrropJEPauHWoqRrdZxFRUiXzB2EPqUfWl0KE7iR-q4UWrXrwobTzHqyA5ymYe745lUQwOUSY4n_8lDYLDqn2km0RSp1qemyyyogGpi9xyt_YPAGahKEc4UFzxHLPrYX8GbKNYqR7ns3D2CbB0nTgkDgC8_2piVv-RBObojmV_IY4Q0__V-0ijD_MGrc0gOmiABObojmVIcmCWIamiSW; isg=BBERXJVFE7K4IH-lW5T_j1a2IB2rfoXwMWHgTvOnMlitmjPsO85JwN-8PG58kh0o',
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

    str2 = str1[12:max_length - 1]
    # print(str2)

    dict2 = json.loads(str2)
    # print('dict2(返回值可用的部分):' + str(dict2))

    list3 = dict2['data']['module']['reviewVOList']
    # print('list3:' + str(list3))

    '''
        3、从接口返回值中读取图片链接的集合和视频链接集合
        '''
    list4 = []  # 图片集合
    list5 = []  # 视频集合
    for i in range(len(list3)):
        list4 = list4 + list3[i]['reviewPicPathList']
        # print('每一个好评中的视频对应的集合:' + str(list3[i]['videoVOList']))

        list5 = list5 + list3[i]['videoVOList']
    print('list4（图片集合）:' + str(list4))
    # print('list5（视频集合）:' + str(list5))

    '''
        3.1、遍历得到的视频集合
        '''
    for i in range(len(list5)):
        url = str(list5[i]['url'])
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36"
        }

        response = requests.get(url, headers=headers)  # 获取图片

        if not os.path.exists('../../resources/image89/video'):
            os.makedirs('../../resources/image89/video')

        ran1 = random.randint(1000000000, 9999999999)
        image_path = '../resources/image89/video/视频' + str(ran1) + '.mp4'
        with open(image_path, "wb") as f:  # wb:写入二进制文件
            f.write(response.content)  # 写入图片
            f.close()
        print('第' + str(i) + '个视频下载完成')

    '''
    3.2、遍历得到的图片集合（此处是list4对象）：考虑list集合中的值的类型，是否有“字符串”和“list集合”混合组成list的情况
    '''
    for i in range(0, len(list4)):
        for j in range(0, len(list4[i])):
            '''
            3.2.1、若读取到的list中的值是string形式
            '''
            if isinstance(list4[i], str):
                print('这个是字符：' + str(list4[i]))

                str1_url = 'https:' + list4[i]
                print('读取的url1:' + str(str1_url))

                headers = {
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36"
                }

                response2 = requests.get(str1_url, headers=headers)  # 获取图片
                if not os.path.exists('../../resources/image89/picture'):
                    os.makedirs('../../resources/image89/picture')

                ran1 = random.randint(1000000000, 9999999999)
                image_path = '../resources/image89/picture/' + str(ran1) + '字符.jpg'
                with open(image_path, "wb") as f:  # wb:写入二进制文件
                    f.write(response2.content)  # 写入图片
                    f.close()
                print('第' + str(i) + '个图片下载完成')
                break

            # 3.2.2、若读取到的list中的值不是string形式（此处是一个list集合）
            else:
                str1_url = 'https:' + list4[i]
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
                image_path = '../resources/image89/picture' + str(ran1) + '.jpg'
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
