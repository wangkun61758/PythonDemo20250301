#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2024/2/24 15:06
@Desc   ：
@Project -> File   ：case509-4（爬取搜索页商品主图）（爬取视频和图片）.py -> case509-4（爬取搜索页商品主图）
=================================================='''
import requests


def test():
    url = "https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/?jsv=2.6.2&appKey=12574478&t=1708762162614&sign=80fd0bfb475a99c2a9721cd67235a911&api=mtop.relationrecommend.WirelessRecommend.recommend&v=2.0&type=jsonp&dataType=jsonp&callback=mtopjsonp6&data=%7B%22appId%22%3A%2234385%22%2C%22params%22%3A%22%7B%5C%22device%5C%22%3A%5C%22HMA-AL00%5C%22%2C%5C%22isBeta%5C%22%3A%5C%22false%5C%22%2C%5C%22grayHair%5C%22%3A%5C%22false%5C%22%2C%5C%22from%5C%22%3A%5C%22nt_history%5C%22%2C%5C%22brand%5C%22%3A%5C%22HUAWEI%5C%22%2C%5C%22info%5C%22%3A%5C%22wifi%5C%22%2C%5C%22index%5C%22%3A%5C%224%5C%22%2C%5C%22rainbow%5C%22%3A%5C%22%5C%22%2C%5C%22schemaType%5C%22%3A%5C%22auction%5C%22%2C%5C%22elderHome%5C%22%3A%5C%22false%5C%22%2C%5C%22isEnterSrpSearch%5C%22%3A%5C%22true%5C%22%2C%5C%22newSearch%5C%22%3A%5C%22false%5C%22%2C%5C%22network%5C%22%3A%5C%22wifi%5C%22%2C%5C%22subtype%5C%22%3A%5C%22%5C%22%2C%5C%22hasPreposeFilter%5C%22%3A%5C%22false%5C%22%2C%5C%22prepositionVersion%5C%22%3A%5C%22v2%5C%22%2C%5C%22client_os%5C%22%3A%5C%22Android%5C%22%2C%5C%22gpsEnabled%5C%22%3A%5C%22false%5C%22%2C%5C%22searchDoorFrom%5C%22%3A%5C%22srp%5C%22%2C%5C%22debug_rerankNewOpenCard%5C%22%3A%5C%22false%5C%22%2C%5C%22homePageVersion%5C%22%3A%5C%22v7%5C%22%2C%5C%22searchElderHomeOpen%5C%22%3A%5C%22false%5C%22%2C%5C%22search_action%5C%22%3A%5C%22initiative%5C%22%2C%5C%22sugg%5C%22%3A%5C%22_4_1%5C%22%2C%5C%22sversion%5C%22%3A%5C%2213.6%5C%22%2C%5C%22style%5C%22%3A%5C%22list%5C%22%2C%5C%22ttid%5C%22%3A%5C%22600000%40taobao_pc_10.7.0%5C%22%2C%5C%22needTabs%5C%22%3A%5C%22true%5C%22%2C%5C%22areaCode%5C%22%3A%5C%22CN%5C%22%2C%5C%22vm%5C%22%3A%5C%22nw%5C%22%2C%5C%22countryNum%5C%22%3A%5C%22156%5C%22%2C%5C%22m%5C%22%3A%5C%22pc%5C%22%2C%5C%22page%5C%22%3A1%2C%5C%22n%5C%22%3A48%2C%5C%22q%5C%22%3A%5C%22%25E8%25BF%259E%25E4%25BD%2593%25E5%2586%2585%25E8%25A1%25A3%25E5%25A5%25B3%25E8%2595%25BE%25E4%25B8%259D%25E6%2580%25A7%25E6%2584%259F%5C%22%2C%5C%22tab%5C%22%3A%5C%22all%5C%22%2C%5C%22pageSize%5C%22%3A48%2C%5C%22totalPage%5C%22%3A100%2C%5C%22totalResults%5C%22%3A4800%2C%5C%22sourceS%5C%22%3A%5C%220%5C%22%2C%5C%22sort%5C%22%3A%5C%22_coefp%5C%22%2C%5C%22bcoffset%5C%22%3A%5C%22%5C%22%2C%5C%22ntoffset%5C%22%3A%5C%22%5C%22%2C%5C%22filterTag%5C%22%3A%5C%22%5C%22%2C%5C%22service%5C%22%3A%5C%22%5C%22%2C%5C%22prop%5C%22%3A%5C%22%5C%22%2C%5C%22loc%5C%22%3A%5C%22%5C%22%2C%5C%22start_price%5C%22%3Anull%2C%5C%22end_price%5C%22%3Anull%2C%5C%22startPrice%5C%22%3Anull%2C%5C%22endPrice%5C%22%3Anull%2C%5C%22itemIds%5C%22%3Anull%2C%5C%22p4pIds%5C%22%3Anull%7D%22%7D"

    payload = {}
    headers = {
        'authority': 'h5api.m.taobao.com',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 't=f6e3dec079805db7cf5e915111d05ee6; xlly_s=1; thw=cn; cookie2=1837fe4e526d5803f79d0f0ace13bf84; _tb_token_=ee838b557b375; _samesite_flag_=true; 3PcFlag=1708757028107; cna=bqtfHoIyuzUBASQOAPBd7Xi9; sgcookie=E100ulE53w7mqGKkUENBhBJBvz01efahcaVozurlQJhWUqdYU7aueKpOLaBSksl3P6lXlYFYFi8QyuLuEUku9cOk14ehKwN%2BlxMd1N2LYLhL23AaBYMOZD0xEaetF5O3oa6C; unb=695573030; uc3=lg2=UtASsssmOIJ0bQ%3D%3D&id2=VWZ7qlhAfso0&nk2=rUPBFbEsoPk%3D&vt3=F8dD3er7mjOcKFvjCWw%3D; csg=27b609c0; lgc=%5Cu4E4C%5Cu5E02%5Cu56DE%5Cu5FC6; cancelledSubSites=empty; cookie17=VWZ7qlhAfso0; dnk=%5Cu4E4C%5Cu5E02%5Cu56DE%5Cu5FC6; skt=ba3dcb68eb561244; existShop=MTcwODc1NzA0MQ%3D%3D; uc4=nk4=0%40r7Il6uDfeekOhfD%2BtTuPU28tjw%3D%3D&id4=0%40V8exE%2Fcl8j99gxPvZbnzipVcRzw%3D; publishItemObj=Ng%3D%3D; tracknick=%5Cu4E4C%5Cu5E02%5Cu56DE%5Cu5FC6; _cc_=Vq8l%2BKCLiw%3D%3D; _l_g_=Ug%3D%3D; sg=%E5%BF%8606; _nk_=%5Cu4E4C%5Cu5E02%5Cu56DE%5Cu5FC6; cookie1=V33DIKglYYC62IzdWcUS9oujtXZ%2Bg%2BnIj5%2BR%2B3nceLc%3D; mt=ci=0_1; uc1=cookie21=V32FPkk%2FhodqgY9Lqf5dEg%3D%3D&cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&cookie15=WqG3DMC9VAQiUQ%3D%3D&cookie14=UoYenbpMyoLf9g%3D%3D&pas=0&existShop=false; mtop_partitioned_detect=1; _m_h5_tk=ddb7e9e61e125297de0e0e52011ae97e_1708772190519; _m_h5_tk_enc=44b692bcf886da8aaaac69ee7e8c179d; tfstk=eT0Xn6g3ItXja6jcFKOrNM27zLz_cxTFh1NttfQV6rUYB0GnC-RMmro7CYH7HZRDmlesnrEi0Ry4CPGidQJe8elmiP4vLp8UCl9haPLXU3Wrij4GZ_W9Y0hc5iJL6idNmBYD3fv5ya_OISlCAdMx64Nb23lYe-wk_5EfPjyPoLmzG92KM8_O7grR8JiGmGG2WNN7LQO5jG0Ln77RFB7kgoFua2RWNtsgD7V7LQO5jGqYZ7reNQ6fj; isg=BL29XCJghAXPDCBoUsnOjLHHzBm3WvGsp5pWan8BkJT1ttToR6-bfMcgYOrwNglk',
        'referer': 'https://s.taobao.com/search?fromTmallRedirect=true&page=1&q=%E8%BF%9E%E4%BD%93%E5%86%85%E8%A1%A3%E5%A5%B3%E8%95%BE%E4%B8%9D%E6%80%A7%E6%84%9F&spm=pc_detail.27183998.202201.1228&tab=all',
        'sec-ch-ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'script',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.160 Safari/537.36'
    }
    response = requests.get(url, headers=headers, params=payload)
    # 访问好评的返回值
    print('访问好评的返回值:' + response.text)

