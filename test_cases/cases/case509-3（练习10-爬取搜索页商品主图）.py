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
    url = 'https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/?jsv=2.7.2&appKey=12574478&t=1742560089728&sign=94a552124ebda0c3ca04db8fcb80025e&api=mtop.relationrecommend.wirelessrecommend.recommend&v=2.0&type=jsonp&dataType=jsonp&callback=mtopjsonp9&data=%7B%22appId%22%3A%2243356%22%2C%22params%22%3A%22%7B%5C%22device%5C%22%3A%5C%22HMA-AL00%5C%22%2C%5C%22isBeta%5C%22%3A%5C%22false%5C%22%2C%5C%22grayHair%5C%22%3A%5C%22false%5C%22%2C%5C%22from%5C%22%3A%5C%22nt_history%5C%22%2C%5C%22brand%5C%22%3A%5C%22HUAWEI%5C%22%2C%5C%22info%5C%22%3A%5C%22wifi%5C%22%2C%5C%22index%5C%22%3A%5C%224%5C%22%2C%5C%22rainbow%5C%22%3A%5C%22%5C%22%2C%5C%22schemaType%5C%22%3A%5C%22auction%5C%22%2C%5C%22elderHome%5C%22%3A%5C%22false%5C%22%2C%5C%22isEnterSrpSearch%5C%22%3A%5C%22true%5C%22%2C%5C%22newSearch%5C%22%3A%5C%22false%5C%22%2C%5C%22network%5C%22%3A%5C%22wifi%5C%22%2C%5C%22subtype%5C%22%3A%5C%22%5C%22%2C%5C%22hasPreposeFilter%5C%22%3A%5C%22false%5C%22%2C%5C%22prepositionVersion%5C%22%3A%5C%22v2%5C%22%2C%5C%22client_os%5C%22%3A%5C%22Android%5C%22%2C%5C%22gpsEnabled%5C%22%3A%5C%22false%5C%22%2C%5C%22searchDoorFrom%5C%22%3A%5C%22srp%5C%22%2C%5C%22debug_rerankNewOpenCard%5C%22%3A%5C%22false%5C%22%2C%5C%22homePageVersion%5C%22%3A%5C%22v7%5C%22%2C%5C%22searchElderHomeOpen%5C%22%3A%5C%22false%5C%22%2C%5C%22search_action%5C%22%3A%5C%22initiative%5C%22%2C%5C%22sugg%5C%22%3A%5C%22_4_1%5C%22%2C%5C%22sversion%5C%22%3A%5C%2213.6%5C%22%2C%5C%22style%5C%22%3A%5C%22list%5C%22%2C%5C%22ttid%5C%22%3A%5C%22600000%40taobao_pc_10.7.0%5C%22%2C%5C%22needTabs%5C%22%3A%5C%22true%5C%22%2C%5C%22areaCode%5C%22%3A%5C%22CN%5C%22%2C%5C%22vm%5C%22%3A%5C%22nw%5C%22%2C%5C%22countryNum%5C%22%3A%5C%22156%5C%22%2C%5C%22m%5C%22%3A%5C%22pc_sem%5C%22%2C%5C%22page%5C%22%3A1%2C%5C%22n%5C%22%3A48%2C%5C%22q%5C%22%3A%5C%22%25E5%25A5%25B3%25E8%25A3%2585%5C%22%2C%5C%22qSource%5C%22%3A%5C%22url%5C%22%2C%5C%22pageSource%5C%22%3A%5C%22%5C%22%2C%5C%22tab%5C%22%3A%5C%22all%5C%22%2C%5C%22pageSize%5C%22%3A48%2C%5C%22totalPage%5C%22%3A100%2C%5C%22totalResults%5C%22%3A4800%2C%5C%22sourceS%5C%22%3A%5C%220%5C%22%2C%5C%22sort%5C%22%3A%5C%22_coefp%5C%22%2C%5C%22bcoffset%5C%22%3A%5C%22%5C%22%2C%5C%22ntoffset%5C%22%3A%5C%22%5C%22%2C%5C%22filterTag%5C%22%3A%5C%22%5C%22%2C%5C%22service%5C%22%3A%5C%22%5C%22%2C%5C%22prop%5C%22%3A%5C%22%5C%22%2C%5C%22loc%5C%22%3A%5C%22%5C%22%2C%5C%22start_price%5C%22%3Anull%2C%5C%22end_price%5C%22%3Anull%2C%5C%22startPrice%5C%22%3Anull%2C%5C%22endPrice%5C%22%3Anull%2C%5C%22itemIds%5C%22%3Anull%2C%5C%22p4pIds%5C%22%3Anull%2C%5C%22categoryp%5C%22%3A%5C%22%5C%22%2C%5C%22myCNA%5C%22%3A%5C%22yThkIL1zozcCAXAgzZxBFsWS%5C%22%2C%5C%22clk1%5C%22%3A%5C%222aff72a72c4aaefa2f344429457796c5%5C%22%2C%5C%22refpid%5C%22%3A%5C%22mm_26632258_3504122_32538762%5C%22%7D%22%7D'

    payload = {}
    headers = {
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'cookie2=180e2a5ca4e04700cb47e146703e980f; t=9e8a9cec2f55ca2f7c9ab69731d84d28; _tb_token_=e951373d8e8bb; mtop_partitioned_detect=1; _m_h5_tk=b2c9b14238ade9c9a7157e2fa198df51_1742565568877; _m_h5_tk_enc=de63572c766fb207d934f8d7b7ae8907; thw=cn; xlly_s=1; _samesite_flag_=true; env_bak=FM%2BgyPYhUSgJmwtm2BMtPYMlAQN%2FaAwN0gFsR%2FuMr%2B8M; wk_cookie2=1e0105f875065a3aea9a6e1ba926bb3d; wk_unb=VWZ7qlhAfso0; havana_sdkSilent=1742642289757; sdkSilent=1742642307428; mt=ci=0_0; cna=yThkIL1zozcCAXAgzZxBFsWS; 3PcFlag=1742559600097; unb=695573030; lgc=%5Cu4E4C%5Cu5E02%5Cu56DE%5Cu5FC6; cancelledSubSites=empty; cookie17=VWZ7qlhAfso0; dnk=%5Cu4E4C%5Cu5E02%5Cu56DE%5Cu5FC6; publishItemObj=Ng%3D%3D; tracknick=%5Cu4E4C%5Cu5E02%5Cu56DE%5Cu5FC6; _cc_=UtASsssmfA%3D%3D; _l_g_=Ug%3D%3D; sg=%E5%BF%8606; _nk_=%5Cu4E4C%5Cu5E02%5Cu56DE%5Cu5FC6; cookie1=V33DIKglYYC62IzdWcUS9oujtXZ%2Bg%2BnIj5%2BR%2B3nceLc%3D; sgcookie=E100H8NibDSkOoZG8TIgR00iIg2OTq2hT3ikTzbDDvH0kze1V7E8Q2fl%2Fub1qzbrh%2B08aTSZjgUWW%2FfKSc8DLSM4FjYc9J3ypWY4ZN659tbAIZo30r9x4FV133n9E7Qe%2FS5%2B; havana_lgc2_0=eyJoaWQiOjY5NTU3MzAzMCwic2ciOiI4NmM5NzRkMmJkMWM2YWZkODkxOWZhMGE3MzEyNGQyNyIsInNpdGUiOjAsInRva2VuIjoiMUpMN3VvZ0VfYTFaQnc3MS13aFF4N2cifQ; _hvn_lgc_=0; havana_lgc_exp=1773663623994; cookie3_bak=180e2a5ca4e04700cb47e146703e980f; cookie3_bak_exp=1742818823994; uc1=cookie14=UoYaibVMcQgjiA%3D%3D&pas=0&cookie21=URm48syIZJfn8EkPLXu2wg%3D%3D&cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&existShop=false&cookie15=W5iHLLyFOGW7aA%3D%3D; sn=; uc3=lg2=VT5L2FSpMGV7TQ%3D%3D&id2=VWZ7qlhAfso0&vt3=F8dD2EnsvTXDJP7Omh8%3D&nk2=rUPBFbEsoPk%3D; csg=9649ab1b; skt=b3aed31bb790ee76; existShop=MTc0MjU1OTYyMw%3D%3D; uc4=id4=0%40V8exE%2Fcl8j99gxPvYQv0v0KkjfQ%3D&nk4=0%40r7Il6uDfeekOhfD6p8epherh1g%3D%3D; tfstk=gxciFn4SJAys3DtLpXN6eFkUAvvpC5NbqmCYDSE2LkrCBSpskrDnPmq9ldNtKomExl595Vn3um0jBFwvfZbst0fA6h9susVYg3KJwQ315SN22iMKstj_krqV_iC4L5aAWLrEhQ3s5w7G0UHewic-QA2V3oo4TWz_ySzNQ-83Trz4g1yV_9SUAkP47s54YJzuzrzaQmue-rZU7SyZ0W83lAcyQlGqTX-emIYW4yYqnP2g4VrZWVhFIR6sWk0oPXNs-u0Nhs5qtP2sG3m7T52t34wS6qdcO53oLWzmGUW0m8Dq6WlwYQyQ3xk8nvIwW0om8mNtTEWa4AnTTfklusu3soooT8SMxuls8bNUpQ8o8Xit5X0AuIzK2kus_SAyP5VabW4IMH1amvkq6RNfbnqjt2lZngScLTSSWs6AoW6fhRzQ-un3_3SahQLNYeYhUEwaRPZJ-eXfhRzQ-uLH-TRbQya_2; isg=BDQ0b9pU77oReHt2NElNTTb1BfKmDVj3SlS_PM6Uob9COdaD9hlnh7i_uXHhwZBP',
        'referer': 'https://s.taobao.com/search?localImgKey=&page=1&q=%E6%B5%81%E8%8B%8F%E6%96%87%E8%83%B8&spm=pc_detail.29232929%2Fevo365560b447259.top_search.search_product&tab=all',
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
    # print('str2:'+str2)

    dict2 = json.loads(str2)
    # print('dict2(返回值可用的部分):' + str(dict2))
    length = len(dict2['data']['itemsArray'])
    print(length)

    list4 = []
    for i in range(0, length - 1):
        paras = dict2['data']['itemsArray'][i]['pic_path']
        # print('list'+str(i)+':' + str(paras))
        list4.append(paras)

        '''
        1、请求图片地址
        
        '''
    for k in range(0, len(list4) - 1):
        str1_url = list4[k]
        print('读取的第' + str(k + 1) + '个url1:' + str(str1_url))

        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36"
        }

        response2 = requests.get(str1_url, headers=headers)  # 获取图片
        if not os.path.exists('D:/Image'):
            os.makedirs('D:/Image')

        ran1 = random.randint(1000000000, 9999999999)
        image_path = 'D:/Image/' + '第' + str(k + 1) + '个图片：' + str(ran1) + '字符.jpg'
        with open(image_path, "wb") as f:  # wb:写入二进制文件
            f.write(response2.content)  # 写入图片
            f.close()
        print('第' + str(k + 1) + '个图片下载完成')
