#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2024/2/20 22:24
@Desc   ：
@Project -> File   ：PythonDemo20240301 -> case89
=================================================='''
import json
import os.path
import random

import requests
from PIL import Image
from matplotlib import pyplot as plt

'''
从网页复制过来的cookie，若在脚本使用过程中退出已经登录的网页，会造成「从网页复制过来的cookie」失效，需要重新登录网页获取新的
'''


def get_cookie():
    cookie = 'cna=jGxcHhYaHAUCAXudnULPUU1G; xlly_s=1; dnk=%5Cu4E4C%5Cu5E02%5Cu56DE%5Cu5FC6; tracknick=%5Cu4E4C%5Cu5E02%5Cu56DE%5Cu5FC6; lid=%E4%B9%8C%E5%B8%82%E5%9B%9E%E5%BF%86; _l_g_=Ug%3D%3D; unb=695573030; lgc=%5Cu4E4C%5Cu5E02%5Cu56DE%5Cu5FC6; cookie1=V33DIKglYYC62IzdWcUS9oujtXZ%2Bg%2BnIj5%2BR%2B3nceLc%3D; login=true; cookie17=VWZ7qlhAfso0; cookie2=1d36e87eb4e6001b7b6adab78784685c; _nk_=%5Cu4E4C%5Cu5E02%5Cu56DE%5Cu5FC6; cancelledSubSites=empty; sg=%E5%BF%8606; t=b24f46e88fd8fd5ab368cac52fdc7ef9; _tb_token_=e6ee013f5ed66; uc1=cookie21=Vq8l%2BKCLiv0NZbsVmuOI%2Bw%3D%3D&cookie15=UtASsssmOIJ0bQ%3D%3D&existShop=false&cookie14=UoYenbiLrP8XjQ%3D%3D&cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&pas=0; uc3=vt3=F8dD3er58uu2FYFUac0%3D&nk2=rUPBFbEsoPk%3D&id2=VWZ7qlhAfso0&lg2=Vq8l%2BKCLz3%2F65A%3D%3D; uc4=nk4=0%40r7Il6uDfeekOhfD%2BtTnyP8bvtQ%3D%3D&id4=0%40V8exE%2Fcl8j99gxPvZbnxxYT7tSU%3D; sgcookie=E100L8y0yP9yfMN2lfx8S0stAFwHDNl0p%2FUyOEpu69OgA8pivVXfBndyHAISMxaJchal1a5KBfSqGHzGgMei1YfCD3nNWuXI%2F0OoiN4qLwGg5tXrpnDsw5GlE%2BY%2FvS%2FqDgCS; csg=f161d187; mtop_partitioned_detect=1; _m_h5_tk=21e8f9fc84ae0fbb73856825b56ce3f2_1708588054763; _m_h5_tk_enc=9ad72a045a47cb3a0c6609cd7e07f2ae; isg=BLCw5OOuoWW7kH1iJGlaUCOhgXgC-ZRDve95K6oAdIv5ZVUPUggN04uTvW0FdUwb; tfstk=eN2MfhtsA2TSUdp7vPH1ppgfHbCd5FMjorpxkx3VT2uQH53A1tjm-ulOfrUYtq4U-VrtkGw0tPZr6rqffmu4ur0Y66B8flMj3aHceTE6q89M1adt6uYrhx7RJBpq1TDbrQ1BfModUMP6--IiN4xkks8FACZ-zluaXleF8fO_x2Yp8JVnM4u--KJ4Kcjy5BRre1JjYieeGIGZAD0R2TzYdnpS6TjhxQsj_DityMjHGhLW3KL5xMAPVfoIfP1..'
    return cookie


def get_evaluate():
    '''
    1、请求好评对应的接口，获取返回值
    :return:
    '''
    url = "https://h5api.m.tmall.com/h5/mtop.alibaba.review.list.for.new.pc.detail/1.0/?jsv=2.7.2&appKey=12574478&t=1708762545212&sign=c3111b953d729917de309c998c13eb08&api=mtop.alibaba.review.list.for.new.pc.detail&v=1.0&isSec=0&ecode=0&timeout=10000&ttid=2022%40taobao_litepc_9.17.0&AntiFlood=true&AntiCreep=true&preventFallback=true&type=jsonp&dataType=jsonp&callback=mtopjsonp6&data=%7B%22itemId%22%3A%22683525454347%22%2C%22bizCode%22%3A%22ali.china.tmall%22%2C%22channel%22%3A%22pc_detail%22%2C%22pageSize%22%3A20%2C%22pageNum%22%3A1%7D"

    payload = {}
    headers = {
        'authority': 'h5api.m.tmall.com',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'cna=bqtfHoIyuzUBASQOAPBd7Xi9; xlly_s=1; login=true; cookie2=1837fe4e526d5803f79d0f0ace13bf84; cancelledSubSites=empty; t=f6e3dec079805db7cf5e915111d05ee6; _tb_token_=ee838b557b375; _l_g_=Ug%3D%3D; dnk=%5Cu4E4C%5Cu5E02%5Cu56DE%5Cu5FC6; uc1=cookie21=UIHiLt3xSixxby3qOiSomw%3D%3D&existShop=false&pas=0&cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&cookie15=VT5L2FSpMGV7TQ%3D%3D&cookie14=UoYenbpMyoSd3A%3D%3D; uc3=lg2=UtASsssmOIJ0bQ%3D%3D&id2=VWZ7qlhAfso0&nk2=rUPBFbEsoPk%3D&vt3=F8dD3er7mjOcKFvjCWw%3D; tracknick=%5Cu4E4C%5Cu5E02%5Cu56DE%5Cu5FC6; lid=%E4%B9%8C%E5%B8%82%E5%9B%9E%E5%BF%86; uc4=nk4=0%40r7Il6uDfeekOhfD%2BtTuPU28tjw%3D%3D&id4=0%40V8exE%2Fcl8j99gxPvZbnzipVcRzw%3D; unb=695573030; lgc=%5Cu4E4C%5Cu5E02%5Cu56DE%5Cu5FC6; cookie1=V33DIKglYYC62IzdWcUS9oujtXZ%2Bg%2BnIj5%2BR%2B3nceLc%3D; cookie17=VWZ7qlhAfso0; _nk_=%5Cu4E4C%5Cu5E02%5Cu56DE%5Cu5FC6; sgcookie=E100ulE53w7mqGKkUENBhBJBvz01efahcaVozurlQJhWUqdYU7aueKpOLaBSksl3P6lXlYFYFi8QyuLuEUku9cOk14ehKwN%2BlxMd1N2LYLhL23AaBYMOZD0xEaetF5O3oa6C; sg=%E5%BF%8606; csg=27b609c0; mtop_partitioned_detect=1; _m_h5_tk=d3a527e22ab6d66c86d9c96a9dce583b_1708771868138; _m_h5_tk_enc=219536b6c042a71a2194fde0a6f7a9dd; tfstk=eA7JfA268-2katMwmzEc8lvvO2PceaCykT5s-pvoAtBAQO33agXhDB6cpeYhO8WdJK6--gflOXdCnUtFqpvkpeCFBS2gSPfPae87IR4gIDD3NeGkZP3fa_8EgjDQji1rJ029Gi_jd-wI32QdJQZsiGxYf_ikM3p1MluIJrOSIp1Wj2nWeI--Z_9xR2_V4hQGW2BrIR2tVSFxYD-Wg9d3iG_QjbZpMdVmmDoemIRvISFxYD-WgIpgirmEYnAV.; isg=BEdHoZaN7gfA4WqKtBuYKgU-1vsRTBsuKTScSBk0oVbciGNKIRxPfhsOKkjWYPOm',
        'referer': 'https://detail.tmall.com/item.htm?_u=t2dmg8j26111&id=683525454347&spm=a1z0k.7628869.0.0.54b737dew7jRGI',
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

    #########################################
    '''
    2、将获取的返回值转成字符串，并做截取，只保留字典内的部分
    '''
    str2 = response.text
    max_length = len(str2)
    # print(str2[12:max_length - 1])

    str3 = str2[12:max_length - 1]
    # print('str3:' + str3)
    dict3 = json.loads(str3)
    print('dict3(返回值可用的部分):' + str(dict3))

    list3 = dict3['data']['module']['reviewVOList']
    # [{'allowInteract': 'true', 'buyCreditLevelPic': 'https://img.alicdn.com/imgextra/i4/O1CN01ZlCYMx1nbVriw6u0S_!!6000000005108-2-tps-92-45.png', 'headPicUrl': 'http://sns.m.taobao.com/avatar/sns/user/flag/sns_logo?type=taobao&kn=wwc_tb_11&bizCode=taobao_avatar&userFlag=RAzN84GK7wS8eNU7T4LBTdyVdokHSRg7iVSLTia1XEdmpjua4LCy5ACmm6ZEz6QNSNwgTBwHzjec27Z4ALYZkh7taxZ3xVazYCctxmmpMi95qfgwjZcFQB8hC2RR2x5yisjLx3EpqV4GXkm5m3n6cgfdaFwKLfWX2m1GHTX', 'id': '1217454492091', 'interactionVO': {'alreadyLike': 'false', 'commentCount': '0', 'likeCount': '0', 'opinionCount': '0', 'readCount': '129', 'reviewId': '1217454492091'}, 'reply': '我们卖的不只是产品，更有对您的一份关心。让您能放心购买是我们的宗旨，所以若有任何疑问，还请咨询我们为您答疑。我们想让您感受舒适的穿着体验，更想给您提供一个可以让您放心的购物环境。感谢购买我们的宝贝...mitaobei旗舰店，专注文胸，胸贴，在看不见的地方精致，才是我们对自己的态度，一套内衣，一份精美的礼物，无微不至，匠心尖货，以做奢侈品的态度做内衣，让平价体验奢侈服务，我们承诺七天内无理由退换货', 'reviewDate': '2个月前', 'reviewPicPathList': ['//img.alicdn.com/imgextra/i1/O1CN012rnLVN2Hk9veFzaQQ_!!0-tbbala.jpg', '//img.alicdn.com/imgextra/i4/O1CN01wr0PgB2Hk9vg3ZSdt_!!0-tbbala.jpg', '//img.alicdn.com/imgextra/i3/O1CN01Y5GhRQ2Hk9vhl634f_!!0-tbbala.jpg'], 'reviewWordContent': '订婚的时候买来穿的，上身很舒服，聚拢效果好，垫子还是上薄下厚的，托胸效果和显大效果真的是绝绝子呀，穿小旗袍真的好凸显身材，显得胸型都立挺不少，软钢圈的承托力对我来说简直就是yyds，头一次穿到有钢圈还不勒的，要订婚的或者要结婚的小姐妹可以直接入手！！', 'skuText': {'颜色分类': '新婚穿红 幸福一生-玫瑰红单件', '尺码': '75B'}, 'userNick': 't**4', 'videoVOList': []}, {'allowInteract': 'true', 'buyCreditLevelPic': 'https://img.alicdn.com/imgextra/i4/O1CN019QZnaG1U1LtUAPn6e_!!6000000002457-2-tps-92-45.png', 'headPicUrl': 'http://sns.m.taobao.com/avatar/sns/user/flag/sns_logo?type=taobao&kn=wwc_tb_11&bizCode=taobao_avatar&userFlag=RAzN83923zmuymBJGKH7nTUTGWti49X2k9CfCF76aMF5Myr35WEXZZrioDdNfSoCeFJBFpcFHHkiBQaXnfym1YzzA6b1a4jib4nJUVxrByq88TN5C8SqjgLNwnPa', 'id': '1218054381326', 'interactionVO': {'alreadyLike': 'false', 'commentCount': '0', 'likeCount': '0', 'opinionCount': '0', 'readCount': '171', 'reviewId': '1218054381326'}, 'reply': '我们卖的不只是产品，更有对您的一份关心。让您能放心购买是我们的宗旨，所以若有任何疑问，还请咨询我们为您答疑。我们想让您感受舒适的穿着体验，更想给您提供一个可以让您放心的购物环境。感谢购买我们的宝贝...mitaobei旗舰店，专注文胸，胸贴，在看不见的地方精致，才是我们对自己的态度，一套内衣，一份精美的礼物，无微不至，匠心尖货，以做奢侈品的态度做内衣，让平价体验奢侈服务，我们承诺七天内无理由退换货', 'reviewDate': '2个月前', 'reviewPicPathList': ['//img.alicdn.com/imgextra/i2/O1CN01WviydN1X43Bu4jjTL_!!0-rate.jpg', '//img.alicdn.com/imgextra/i4/O1CN019TYo931X43Bqh9eQ0_!!0-rate.jpg'], 'reviewWordContent': '本来应该买套装的，结果买了单件，又补钱买了内裤，备婚买的了，穿上还挺舒服的，主要是聚拢效果好，罩杯又是加厚的，可以很好的托住胸部，还能显大，内衣颜值高，上身穿着很显白，我个人还是挺满意的，老公也蛮喜欢的！', 'skuText': {'颜色分类': '性感专属 鸿运本命年-锦鲤红 套装', '尺码': '75C'}, 'userNick': '麻**2', 'videoVOList': []}, {'allowInteract': 'true', 'buyCreditLevelPic': 'https://img.alicdn.com/imgextra/i3/O1CN01QZTjHW1F4oegDvuEX_!!6000000000434-2-tps-92-45.png', 'headPicUrl': 'http://img.alicdn.com/tps/TB1l6dkOXXXXXXEXVXXXXXXXXXX-210-210.png_70x70.jpg', 'id': '1218160790172', 'interactionVO': {'alreadyLike': 'false', 'commentCount': '0', 'likeCount': '0', 'opinionCount': '0', 'readCount': '103', 'reviewId': '1218160790172'}, 'reply': '我们卖的不只是产品，更有对您的一份关心。让您能放心购买是我们的宗旨，所以若有任何疑问，还请咨询我们为您答疑。我们想让您感受舒适的穿着体验，更想给您提供一个可以让您放心的购物环境。感谢购买我们的宝贝...mitaobei旗舰店，专注文胸，胸贴，在看不见的地方精致，才是我们对自己的态度，一套内衣，一份精美的礼物，无微不至，匠心尖货，以做奢侈品的态度做内衣，让平价体验奢侈服务，我们承诺七天内无理由退换货', 'reviewDate': '2个月前', 'reviewPicPathList': ['//img.alicdn.com/imgextra/i4/O1CN01NiRnkm1jGD5ogA2iU_!!0-rate.jpg', '//img.alicdn.com/imgextra/i3/O1CN0110Z9QL1jGD5vftUjp_!!0-rate.jpg', '//img.alicdn.com/imgextra/i1/O1CN01uuSmWa1jGD5sW2kUn_!!0-rate.jpg'], 'reviewWordContent': '这个内衣真的好适合结婚的时候穿呀，超级好看，颜值很高，也很高级，上身的聚拢效果也很好，显得胸型超级圆润立挺，推荐推荐', 'skuText': {'颜色分类': '白色-单件[纯欲专属 聚拢必备]', '尺码': '75B'}, 'userNick': 'c**5', 'videoVOList': []}, {'allowInteract': 'true', 'buyCreditLevelPic': 'https://img.alicdn.com/imgextra/i4/O1CN019QZnaG1U1LtUAPn6e_!!6000000002457-2-tps-92-45.png', 'headPicUrl': 'http://sns.m.taobao.com/avatar/sns/user/flag/sns_logo?type=taobao&kn=wwc_tb_11&bizCode=taobao_avatar&userFlag=RAzN84GK7wS8eNU7T4LBTdyVdokHSRg7iVSM7BkX7fyhFoFCMFw3J8UKpffz9CAAjejRnamUKtnmFVq8S9XupFKoqeDCpVjEsYSjVGz8jZaB9PFVw7XsLrt97KDvJPegrDTy5Hf27trw7LV5bCYpHTNpbza9gkP7ufAnWgR', 'id': '1220527515604', 'interactionVO': {'alreadyLike': 'false', 'commentCount': '0', 'likeCount': '0', 'opinionCount': '0', 'readCount': '57', 'reviewId': '1220527515604'}, 'reply': '我们卖的不只是产品，更有对您的一份关心。让您能放心购买是我们的宗旨，所以若有任何疑问，还请咨询我们为您答疑。我们想让您感受舒适的穿着体验，更想给您提供一个可以让您放心的购物环境。感谢购买我们的宝贝...mitaobei旗舰店，专注文胸，胸贴，在看不见的地方精致，才是我们对自己的态度，一套内衣，一份精美的礼物，无微不至，匠心尖货，以做奢侈品的态度做内衣，让平价体验奢侈服务，我们承诺七天内无理由退换货', 'reviewDate': '1个月前', 'reviewPicPathList': ['//img.alicdn.com/imgextra/i2/O1CN01mwlSw123g7pQi7MLl_!!0-rate.jpg'], 'reviewWordContent': '订婚穿了很显瘦，颜色也很百搭，质量挺好的聚拢效果比较明显，上身穿着听挺舒服的，拍的码数刚刚好不会空杯，没有一点束缚感，料很亲肤，比较柔软而且又透气，穿一天也没有感觉', 'skuText': {'颜色分类': '性感专属 鸿运本命年-锦鲤红 套装', '尺码': '75B'}, 'userNick': 'c**3', 'videoVOList': []}, {'allowInteract': 'true', 'buyCreditLevelPic': 'https://img.alicdn.com/imgextra/i4/O1CN019QZnaG1U1LtUAPn6e_!!6000000002457-2-tps-92-45.png', 'headPicUrl': 'http://sns.m.taobao.com/avatar/sns/user/flag/sns_logo?type=taobao&kn=wwc_tb_11&bizCode=taobao_avatar&userFlag=RAzN84GK7wS8eNU7T4LBTdyVdokHSRg7iVSMFDDhBgQyfUZVRmm2EuDPAEdEi8Rby8W1xbBacATzLxZ5g5u41S4UvAkQLKFXZG2tDFZDmuxZtb39a5vCBZf8JAprsknjiyH3AKxVuvvvRLKjPjWrcTN59GjqcFfwXSuYegR', 'id': '1218034846457', 'interactionVO': {'alreadyLike': 'false', 'commentCount': '0', 'likeCount': '0', 'opinionCount': '0', 'readCount': '125', 'reviewId': '1218034846457'}, 'reply': '我们卖的不只是产品，更有对您的一份关心。让您能放心购买是我们的宗旨，所以若有任何疑问，还请咨询我们为您答疑。我们想让您感受舒适的穿着体验，更想给您提供一个可以让您放心的购物环境。感谢购买我们的宝贝...mitaobei旗舰店，专注文胸，胸贴，在看不见的地方精致，才是我们对自己的态度，一套内衣，一份精美的礼物，无微不至，匠心尖货，以做奢侈品的态度做内衣，让平价体验奢侈服务，我们承诺七天内无理由退换货', 'reviewDate': '2个月前', 'reviewPicPathList': ['//img.alicdn.com/imgextra/i4/O1CN0118Utzq2DX6AVTnZt7_!!0-rate.jpg', '//img.alicdn.com/imgextra/i3/O1CN01FjqEIP2DX6Ail6J8k_!!0-rate.jpg'], 'reviewWordContent': '真的是一款颜值超高 舒适度超棒 质感很好的内衣 真的穿上胸型很漂亮 包裹感很好 和内裤搭配在一起真的很绝，美胸带加上胸前的交叉设计 真的很有设计感 男朋友也一直夸很漂亮', 'skuText': {'颜色分类': '性感专属 鸿运本命年-锦鲤红套盒', '尺码': '70C'}, 'userNick': 'h**8', 'videoVOList': []}, {'allowInteract': 'true', 'buyCreditLevelPic': 'https://img.alicdn.com/imgextra/i4/O1CN01ZlCYMx1nbVriw6u0S_!!6000000005108-2-tps-92-45.png', 'headPicUrl': 'http://img.alicdn.com/tps/TB1l6dkOXXXXXXEXVXXXXXXXXXX-210-210.png_70x70.jpg', 'id': '1197385935201', 'interactionVO': {'alreadyLike': 'false', 'commentCount': '0', 'likeCount': '2', 'opinionCount': '0', 'readCount': '690', 'reviewId': '1197385935201'}, 'reply': '我们卖的不只是产品，更有对您的一份关心。让您能放心购买是我们的宗旨，所以若有任何疑问，还请咨询我们为您答疑。我们想让您感受舒适的穿着体验，更想给您提供一个可以让您放心的购物环境。感谢购买我们的宝贝...mitaobei旗舰店，专注文胸，胸贴，在看不见的地方精致，才是我们对自己的态度，一套内衣，一份精美的礼物，无微不至，匠心尖货，以做奢侈品的态度做内衣，让平价体验奢侈服务，我们承诺七天内无理由退换货', 'reviewDate': '11个月前', 'reviewPicPathList': ['//img.alicdn.com/imgextra/i2/O1CN01rQVbyF1HwWMyaGslG_!!0-rate.jpg', '//img.alicdn.com/imgextra/i3/O1CN01JnfmOw1HwWN0r4uQF_!!0-rate.jpg'], 'reviewWordContent': '超级好 版型很好看，特别质感，买了好几家就这家的很质感，颜色也正，分享一下我的喜悦～', 'skuText': {'颜色分类': '新婚穿红 幸福一生-玫瑰红单件', '尺码': '85B'}, 'userNick': '乍**♂', 'videoVOList': []}, {'allowInteract': 'true', 'buyCreditLevelPic': 'https://img.alicdn.com/imgextra/i4/O1CN019QZnaG1U1LtUAPn6e_!!6000000002457-2-tps-92-45.png', 'headPicUrl': 'http://img.alicdn.com/tps/TB1l6dkOXXXXXXEXVXXXXXXXXXX-210-210.png_70x70.jpg', 'id': '1196312777092', 'interactionVO': {'alreadyLike': 'false', 'commentCount': '0', 'likeCount': '2', 'opinionCount': '0', 'readCount': '679', 'reviewId': '1196312777092'}, 'reply': '我们卖的不只是产品，更有对您的一份关心。让您能放心购买是我们的宗旨，所以若有任何疑问，还请咨询我们为您答疑。我们想让您感受舒适的穿着体验，更想给您提供一个可以让您放心的购物环境。感谢购买我们的宝贝...mitaobei旗舰店，专注文胸，胸贴，在看不见的地方精致，才是我们对自己的态度，一套内衣，一份精美的礼物，无微不至，匠心尖货，以做奢侈品的态度做内衣，让平价体验奢侈服务，我们承诺七天内无理由退换货', 'reviewDate': '11个月前', 'reviewPicPathList': ['//img.alicdn.com/imgextra/i3/O1CN01ps8VoL2KNfFelAhjZ_!!0-rate.jpg', '//img.alicdn.com/imgextra/i4/O1CN01Xse56Y2KNfFlIBCgT_!!0-rate.jpg', '//img.alicdn.com/imgextra/i1/O1CN01sQ05m02KNfFlIDt0m_!!0-rate.jpg'], 'reviewWordContent': '一整个礼盒装氛围感满满呀，刺绣的也很好看，我胸很小穿上不会空杯，刚刚好能把胸聚起来，像这种礼盒装的买来送人或者自己本命年结婚啥的穿都是性价比最高的，配套内裤一套穿上更有感觉', 'skuText': {'颜色分类': '性感专属 鸿运本命年-锦鲤红', '尺码': '75B'}, 'userNick': '不**硬', 'videoVOList': []}, {'allowInteract': 'true', 'buyCreditLevelPic': 'https://img.alicdn.com/imgextra/i3/O1CN01PIYxrZ22FGrmiDphN_!!6000000007090-2-tps-92-45.png', 'headPicUrl': 'http://img.alicdn.com/tps/TB1l6dkOXXXXXXEXVXXXXXXXXXX-210-210.png_70x70.jpg', 'id': '1195364865759', 'interactionVO': {'alreadyLike': 'false', 'commentCount': '0', 'likeCount': '0', 'opinionCount': '0', 'readCount': '238', 'reviewId': '1195364865759'}, 'reply': '我们卖的不只是产品，更有对您的一份关心。让您能放心购买是我们的宗旨，所以若有任何疑问，还请咨询我们为您答疑。我们想让您感受舒适的穿着体验，更想给您提供一个可以让您放心的购物环境。感谢购买我们的宝贝...mitaobei旗舰店，专注文胸，胸贴，在看不见的地方精致，才是我们对自己的态度，一套内衣，一份精美的礼物，无微不至，匠心尖货，以做奢侈品的态度做内衣，让平价体验奢侈服务，我们承诺七天内无理由退换货', 'reviewDate': '11个月前', 'reviewPicPathList': ['//img.alicdn.com/imgextra/i4/O1CN01uSKfmg1pS0v67zf0p_!!0-rate.jpg', '//img.alicdn.com/imgextra/i4/O1CN01ERAZa625z1JdQtusa_!!0-rate.jpg'], 'reviewWordContent': '结婚穿这个红内衣真的很适合，对小熊很友好，很聚拢，显得胸型很好看，真心不错，好看中又带着性感，真的很喜欢', 'skuText': {'颜色分类': '性感专属 鸿运本命年-锦鲤红', '尺码': '70B'}, 'userNick': 'j**泳', 'videoVOList': []}, {'allowInteract': 'true', 'buyCreditLevelPic': 'https://img.alicdn.com/imgextra/i4/O1CN019QZnaG1U1LtUAPn6e_!!6000000002457-2-tps-92-45.png', 'headPicUrl': 'http://img.alicdn.com/tps/TB1l6dkOXXXXXXEXVXXXXXXXXXX-210-210.png_70x70.jpg', 'id': '1199335710039', 'interactionVO': {'alreadyLike': 'false', 'commentCount': '0', 'likeCount': '1', 'opinionCount': '0', 'readCount': '98', 'reviewId': '1199335710039'}, 'reply': '我们卖的不只是产品，更有对您的一份关心。让您能放心购买是我们的宗旨，所以若有任何疑问，还请咨询我们为您答疑。我们想让您感受舒适的穿着体验，更想给您提供一个可以让您放心的购物环境。感谢购买我们的宝贝...mitaobei旗舰店，专注文胸，胸贴，在看不见的地方精致，才是我们对自己的态度，一套内衣，一份精美的礼物，无微不至，匠心尖货，以做奢侈品的态度做内衣，让平价体验奢侈服务，我们承诺七天内无理由退换货', 'reviewDate': '10个月前', 'reviewPicPathList': ['//img.alicdn.com/imgextra/i1/O1CN01ddo5XE1cGTxA965aE_!!0-rate.jpg', '//img.alicdn.com/imgextra/i4/O1CN01GI7lcG1cGTwynfnnO_!!0-rate.jpg'], 'reviewWordContent': '和卖家描述的一样，我很喜欢，所以用心推荐给大家。首先是内衣颜色正，耐看。布料好，顺顺滑滑的。客服很好，没有多余线头， 上身很显胸型，把副乳收拾的很好，聚拢效果超棒。内衣质量非常的好 胸杯也特别好 非常适合面料柔软舒适亲肤，', 'skuText': {'颜色分类': '新婚穿红 幸福一生-玫瑰红套装[性感专属 鸿运本命年]', '尺码': '75B'}, 'userNick': '阿**的', 'videoVOList': []}, {'allowInteract': 'true', 'buyCreditLevelPic': 'https://img.alicdn.com/imgextra/i4/O1CN01ZlCYMx1nbVriw6u0S_!!6000000005108-2-tps-92-45.png', 'headPicUrl': 'http://img.alicdn.com/tps/TB1l6dkOXXXXXXEXVXXXXXXXXXX-210-210.png_70x70.jpg', 'id': '1198456619808', 'interactionVO': {'alreadyLike': 'false', 'commentCount': '0', 'likeCount': '0', 'opinionCount': '0', 'readCount': '288', 'reviewId': '1198456619808'}, 'reply': '', 'reviewDate': '10个月前', 'reviewPicPathList': ['//img.alicdn.com/imgextra/i2/O1CN01oXIFS21iRpSMYxXm5_!!0-rate.jpg', '//img.alicdn.com/imgextra/i4/O1CN01MEEy1K1iRpSCw29SM_!!0-rate.jpg'], 'reviewWordContent': '聚拢效果特别好，穿着透气舒服，买来结婚穿的，真的美美哒', 'skuText': {'颜色分类': '性感专属 鸿运本命年-锦鲤红 套装', '尺码': '75B'}, 'userNick': 't**6', 'videoVOList': []}, {'allowInteract': 'true', 'buyCreditLevelPic': 'https://img.alicdn.com/imgextra/i4/O1CN019QZnaG1U1LtUAPn6e_!!6000000002457-2-tps-92-45.png', 'headPicUrl': 'http://img.alicdn.com/tps/TB1l6dkOXXXXXXEXVXXXXXXXXXX-210-210.png_70x70.jpg', 'id': '1197454772022', 'interactionVO': {'alreadyLike': 'false', 'commentCount': '0', 'likeCount': '0', 'opinionCount': '0', 'readCount': '343', 'reviewId': '1197454772022'}, 'reply': '', 'reviewDate': '10个月前', 'reviewPicPathList': ['//img.alicdn.com/imgextra/i1/O1CN01mEENze2CRlsVk2tx6_!!0-rate.jpg', '//img.alicdn.com/imgextra/i3/O1CN01AGPpPq2CRlsa2p94R_!!0-rate.jpg'], 'reviewWordContent': '内衣质量很好，也不会往下掉，布料超级好，这个价钱买到真的是太值了!想买的姐妹快行动起来吧', 'skuText': {'颜色分类': '性感专属 鸿运本命年-锦鲤红', '尺码': '70B'}, 'userNick': 't**3', 'videoVOList': []}, {'allowInteract': 'true', 'buyCreditLevelPic': 'https://img.alicdn.com/imgextra/i4/O1CN019QZnaG1U1LtUAPn6e_!!6000000002457-2-tps-92-45.png', 'headPicUrl': 'http://img.alicdn.com/tps/TB1l6dkOXXXXXXEXVXXXXXXXXXX-210-210.png_70x70.jpg', 'id': '1197232068842', 'interactionVO': {'alreadyLike': 'false', 'commentCount': '0', 'likeCount': '1', 'opinionCount': '0', 'readCount': '473', 'reviewId': '1197232068842'}, 'reply': '', 'reviewDate': '10个月前', 'reviewPicPathList': ['//img.alicdn.com/imgextra/i2/O1CN01Ybk1AH1w3vPAzbnWX_!!0-rate.jpg', '//img.alicdn.com/imgextra/i4/O1CN01KEUaXB1w3vPFd0I9l_!!0-rate.jpg', '//img.alicdn.com/imgextra/i3/O1CN01AkS5MA1w3vPBWmBzT_!!0-rate.jpg'], 'reviewWordContent': '我是小胸的，穿上确实很聚拢，颜色是我喜欢的红，妥妥好评！', 'skuText': {'颜色分类': '性感专属 鸿运本命年-锦鲤红 套装', '尺码': '75B'}, 'userNick': 't**0', 'videoVOList': []}, {'allowInteract': 'true', 'buyCreditLevelPic': 'https://img.alicdn.com/imgextra/i4/O1CN01ZlCYMx1nbVriw6u0S_!!6000000005108-2-tps-92-45.png', 'headPicUrl': 'http://img.alicdn.com/tps/TB1l6dkOXXXXXXEXVXXXXXXXXXX-210-210.png_70x70.jpg', 'id': '1197386705668', 'interactionVO': {'alreadyLike': 'false', 'commentCount': '0', 'likeCount': '2', 'opinionCount': '0', 'readCount': '183', 'reviewId': '1197386705668'}, 'reply': '', 'reviewDate': '10个月前', 'reviewPicPathList': ['//img.alicdn.com/imgextra/i3/O1CN01HMf9wD1IbHcirh4f1_!!0-rate.jpg', '//img.alicdn.com/imgextra/i3/O1CN019HlDfI1IbHceN5qdH_!!0-rate.jpg'], 'reviewWordContent': '好漂亮的颜色。高端大气。性感迷人。我这小胸都给我聚拢了', 'skuText': {'颜色分类': '性感专属 鸿运本命年-锦鲤红 套装', '尺码': '75B'}, 'userNick': 't**4', 'videoVOList': []}, {'allowInteract': 'true', 'buyCreditLevelPic': 'https://img.alicdn.com/imgextra/i4/O1CN019QZnaG1U1LtUAPn6e_!!6000000002457-2-tps-92-45.png', 'headPicUrl': 'http://img.alicdn.com/tps/TB1l6dkOXXXXXXEXVXXXXXXXXXX-210-210.png_70x70.jpg', 'id': '1197683796210', 'interactionVO': {'alreadyLike': 'false', 'commentCount': '0', 'likeCount': '2', 'opinionCount': '0', 'readCount': '662', 'reviewId': '1197683796210'}, 'reply': '', 'reviewDate': '10个月前', 'reviewPicPathList': ['//img.alicdn.com/imgextra/i1/O1CN01J5hSzF28YrYCazG3f_!!0-rate.jpg', '//img.alicdn.com/imgextra/i4/O1CN01PMMYZE28YrYEPkVdv_!!0-rate.jpg'], 'reviewWordContent': '这款内衣真的太绝了，我的天呐~谁能相信没穿这款内衣之前，我是平胸（算是基本没胸的）但是穿上这款内衣，现在真的超自信，修身衣服也能有曲线，而且还不假，超级聚拢，胸型吼吼看！！太满意了~', 'skuText': {'颜色分类': '黑色-套装[性感专属 聚拢必备]', '尺码': '85D'}, 'userNick': 't**9', 'videoVOList': []}, {'allowInteract': 'true', 'buyCreditLevelPic': 'https://img.alicdn.com/imgextra/i3/O1CN01QZTjHW1F4oegDvuEX_!!6000000000434-2-tps-92-45.png', 'headPicUrl': 'http://sns.m.taobao.com/avatar/sns/user/flag/sns_logo?type=taobao&kn=wwc_tb_11&bizCode=taobao_avatar&userFlag=RAzN84GK7wS8eNVZ4pygCySf4JN6VZKMKqp6dDh2YnRsc97YskkRhaZkN3tTztgw3MbJNPgTqdHC5vEDi1VgBxaYuqV1MiAY9LsbvsRVAqVGmFkGdHqUEtZPawMSG5PCEbzmUHACdfoiCoYDXtS4BJid4MEM7X41FSd8xEu', 'id': '1195966991517', 'interactionVO': {'alreadyLike': 'false', 'commentCount': '0', 'likeCount': '0', 'opinionCount': '0', 'readCount': '268', 'reviewId': '1195966991517'}, 'reply': '我们卖的不只是产品，更有对您的一份关心。让您能放心购买是我们的宗旨，所以若有任何疑问，还请咨询我们为您答疑。我们想让您感受舒适的穿着体验，更想给您提供一个可以让您放心的购物环境。感谢购买我们的宝贝...mitaobei旗舰店，专注文胸，胸贴，在看不见的地方精致，才是我们对自己的态度，一套内衣，一份精美的礼物，无微不至，匠心尖货，以做奢侈品的态度做内衣，让平价体验奢侈服务，我们承诺七天内无理由退换货', 'reviewDate': '11个月前', 'reviewPicPathList': ['//img.alicdn.com/imgextra/i4/O1CN01hJVfZd1u0bIGHiVYH_!!2-rate.png', '//img.alicdn.com/imgextra/i1/O1CN01DRyWOB1u0bIDMEuqi_!!2-rate.png', '//img.alicdn.com/imgextra/i4/O1CN01CNLMBE1u0bIDME2ma_!!2-rate.png'], 'reviewWordContent': '穿了感觉hhh，小胸真的很聚拢显大，上薄下厚的罩杯好像可以调整，而且稳固性很好，抬手杯不会往上跑，同时胸前还有绑带设计，搭配小吊带也不突兀，喜欢！！', 'skuText': {'颜色分类': '性感专属 鸿运本命年-锦鲤红 套装', '尺码': '75B'}, 'userNick': '猫**瓜', 'videoVOList': []}, {'allowInteract': 'true', 'buyCreditLevelPic': 'https://img.alicdn.com/imgextra/i4/O1CN019QZnaG1U1LtUAPn6e_!!6000000002457-2-tps-92-45.png', 'headPicUrl': 'http://img.alicdn.com/tps/TB1l6dkOXXXXXXEXVXXXXXXXXXX-210-210.png_70x70.jpg', 'id': '1197878795553', 'interactionVO': {'alreadyLike': 'false', 'commentCount': '0', 'likeCount': '0', 'opinionCount': '0', 'readCount': '152', 'reviewId': '1197878795553'}, 'reply': '', 'reviewDate': '10个月前', 'reviewPicPathList': ['//img.alicdn.com/imgextra/i2/O1CN01evoBAC1D0Znkz8wu4_!!0-rate.jpg', '//img.alicdn.com/imgextra/i2/O1CN01hS10cX1D0Znk7NWXl_!!0-rate.jpg'], 'reviewWordContent': '太喜欢了，这个红色买来结婚穿到，看到款式和颜色，平时穿也是可以的，大小正好，聚拢', 'skuText': {'颜色分类': '性感专属 鸿运本命年-锦鲤红', '尺码': '75B'}, 'userNick': '爱**风', 'videoVOList': []}, {'allowInteract': 'true', 'buyCreditLevelPic': 'https://img.alicdn.com/imgextra/i4/O1CN019QZnaG1U1LtUAPn6e_!!6000000002457-2-tps-92-45.png', 'headPicUrl': 'http://img.alicdn.com/tps/TB1l6dkOXXXXXXEXVXXXXXXXXXX-210-210.png_70x70.jpg', 'id': '1195162109380', 'interactionVO': {'alreadyLike': 'false', 'commentCount': '0', 'likeCount': '0', 'opinionCount': '0', 'readCount': '415', 'reviewId': '1195162109380'}, 'reply': '', 'reviewAppendVO': {'appendedWordContent': '真的是一款颜值超高 舒适度超棒 质感很好的内衣 真的穿上胸型很漂亮 包裹感很好 美胸带加上胸前的交叉设计 真的很有设计感 男朋友也一直夸很漂亮', 'intervalDay': '0', 'reply': '我们卖的不只是产品，更有对您的一份关心。让您能放心购买是我们的宗旨，所以若有任何疑问，还请咨询我们为您答疑。我们想让您感受舒适的穿着体验，更想给您提供一个可以让您放心的购物环境。感谢购买我们的宝贝...mitaobei旗舰店，专注文胸，胸贴，在看不见的地方精致，才是我们对自己的态度，一套内衣，一份精美的礼物，无微不至，匠心尖货，以做奢侈品的态度做内衣，让平价体验奢侈服务，我们承诺七天内无理由退换货', 'reviewPicPathList': ['//img.alicdn.com/imgextra/i1/2/O1CN017EOTCn1J0vnQPnMay_!!2-rate.png', '//img.alicdn.com/imgextra/i3/2/O1CN01G8I7li1J0vnSRYh5x_!!2-rate.png'], 'videoVOList': []}, 'reviewDate': '11个月前', 'reviewWordContent': '颜色正，版型好，尺码标准，发货快。满意', 'skuText': {'颜色分类': '新婚穿红 幸福一生-玫瑰红单件', '尺码': '75C'}, 'userNick': '曹**m', 'videoVOList': []}, {'allowInteract': 'true', 'buyCreditLevelPic': 'https://img.alicdn.com/imgextra/i4/O1CN01ZlCYMx1nbVriw6u0S_!!6000000005108-2-tps-92-45.png', 'headPicUrl': 'http://img.alicdn.com/tps/TB1l6dkOXXXXXXEXVXXXXXXXXXX-210-210.png_70x70.jpg', 'id': '1217648065630', 'interactionVO': {'alreadyLike': 'false', 'commentCount': '0', 'likeCount': '0', 'opinionCount': '0', 'readCount': '28', 'reviewId': '1217648065630'}, 'reply': '我们卖的不只是产品，更有对您的一份关心。让您能放心购买是我们的宗旨，所以若有任何疑问，还请咨询我们为您答疑。我们想让您感受舒适的穿着体验，更想给您提供一个可以让您放心的购物环境。感谢购买我们的宝贝...mitaobei旗舰店，专注文胸，胸贴，在看不见的地方精致，才是我们对自己的态度，一套内衣，一份精美的礼物，无微不至，匠心尖货，以做奢侈品的态度做内衣，让平价体验奢侈服务，我们承诺七天内无理由退换货', 'reviewDate': '2个月前', 'reviewPicPathList': ['//img.alicdn.com/imgextra/i3/O1CN0198rVCQ25CTPSsOdJU_!!0-rate.jpg', '//img.alicdn.com/imgextra/i1/O1CN01v6LnmG25CTPDtAsWq_!!2-rate.png', '//img.alicdn.com/imgextra/i1/O1CN01CNoGqT25CTPDtC9Uh_!!0-rate.jpg'], 'reviewWordContent': '这款内衣 惊艳到尖叫的地步 超级高级的正红色显白的颜色真的很好看！！ 深v设计非常性感 但是聚拢效果一点也没差 后背没有勒肉 非常舒服 男友很喜欢这种高级设计感的小性感', 'skuText': {'颜色分类': '性感专属 鸿运本命年-锦鲤红套盒', '尺码': '70C'}, 'userNick': '一**呢', 'videoVOList': []}, {'allowInteract': 'true', 'buyCreditLevelPic': 'https://img.alicdn.com/imgextra/i4/O1CN01ZlCYMx1nbVriw6u0S_!!6000000005108-2-tps-92-45.png', 'headPicUrl': 'http://img.alicdn.com/tps/TB1l6dkOXXXXXXEXVXXXXXXXXXX-210-210.png_70x70.jpg', 'id': '1197686412127', 'interactionVO': {'alreadyLike': 'false', 'commentCount': '0', 'likeCount': '0', 'opinionCount': '0', 'readCount': '284', 'reviewId': '1197686412127'}, 'reply': '', 'reviewDate': '10个月前', 'reviewPicPathList': ['//img.alicdn.com/imgextra/i3/O1CN01skQy5M2CfVlJx41fe_!!0-rate.jpg', '//img.alicdn.com/imgextra/i1/O1CN01rULm2v2CfVlMe9wmW_!!0-rate.jpg'], 'reviewWordContent': '订婚咱也要美美的 里面也要穿红色的内内哦 小胸穿巨合适 内衣很轻薄透气 里杯也是那种超级舒服的棉 穿上一点也不勒胸 订婚结婚的小胸姐妹可以入手一套哦', 'skuText': {'颜色分类': '性感专属 鸿运本命年-锦鲤红 套装', '尺码': '75B'}, 'userNick': 'h**8', 'videoVOList': []}, {'allowInteract': 'true', 'buyCreditLevelPic': 'https://img.alicdn.com/imgextra/i4/O1CN019QZnaG1U1LtUAPn6e_!!6000000002457-2-tps-92-45.png', 'headPicUrl': 'http://img.alicdn.com/tps/TB1l6dkOXXXXXXEXVXXXXXXXXXX-210-210.png_70x70.jpg', 'id': '1218077934685', 'interactionVO': {'alreadyLike': 'false', 'commentCount': '0', 'likeCount': '0', 'opinionCount': '0', 'readCount': '12', 'reviewId': '1218077934685'}, 'reply': '我们卖的不只是产品，更有对您的一份关心。让您能放心购买是我们的宗旨，所以若有任何疑问，还请咨询我们为您答疑。我们想让您感受舒适的穿着体验，更想给您提供一个可以让您放心的购物环境。感谢购买我们的宝贝...mitaobei旗舰店，专注文胸，胸贴，在看不见的地方精致，才是我们对自己的态度，一套内衣，一份精美的礼物，无微不至，匠心尖货，以做奢侈品的态度做内衣，让平价体验奢侈服务，我们承诺七天内无理由退换货', 'reviewDate': '2个月前', 'reviewPicPathList': ['//img.alicdn.com/imgextra/i2/O1CN01eLqTJV1lIcPQOfVW3_!!0-rate.jpg', '//img.alicdn.com/imgextra/i2/O1CN01Vtpebt1lIcPMDAKWe_!!0-rate.jpg'], 'reviewWordContent': '1 这个内衣好绝呀，超级好看，上身很显白，聚拢效果也好，而且内衣垫子是加厚的，小胸也不用担心会空杯啦，结婚穿超级合适，没买错太好了', 'skuText': {'颜色分类': '新婚穿红 幸福一生-玫瑰红单件', '尺码': '70C'}, 'userNick': 's**1', 'videoVOList': []}]
    print('list3:' + str(list3))

    '''
    3、从接口返回值中读取图片链接的集合和视频链接集合
    '''
    list4 = []  # 图片集合
    list5 = []  # 视频集合
    for i in range(len(list3)):
        list4 = list4 + list3[i]['reviewPicPathList']
        print('每一个好评中的视频对应的集合:' + str(list3[i]['videoVOList']))
        list5 = list5 + list3[i]['videoVOList']
    print('list4（图片集合）:' + str(list4))
    print('list5（视频集合）:' + str(list5))

    '''
    3.1、遍历得到的视频集合
    '''
    for i in range(len(list5)):
        url = str(list5[i]['url'])
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36"
        }

        response = requests.get(url, headers=headers)  # 获取图片
        ran1 = random.randint(1000000000, 9999999999)
        image_path = '../resources/image2/mp4' + str(ran1) + '.mp4'
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
                # print('这个是字符：' + str(list1[i]))

                str1_url = 'https:' + list4[i]
                print('读取的url1:' + str(str1_url))

                headers = {
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36"
                }

                response = requests.get(str1_url, headers=headers)  # 获取图片
                if not os.path.exists('../../resources/image2'):
                    os.makedirs('../../resources/image2')

                ran1 = random.randint(1000000000, 9999999999)
                image_path = '../../resources/image2/bra' + str(ran1) + '字符.jpg'
                with open(image_path, "wb") as f:  # wb:写入二进制文件
                    f.write(response.content)  # 写入图片
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
                if not os.path.exists('../../resources/image2'):
                    os.makedirs('../../resources/image2')

                ran1 = random.randint(10000000000, 99999999999)
                image_path = '../../resources/image2/bra' + str(ran1) + '.jpg'
                with open(image_path, "wb") as f:  # wb:写入二进制文件
                    f.write(response.content)  # 写入图片
                    f.close()
                '''
                3.2.2.2、打开对应的图片预览
                '''
                img = Image.open(image_path)
                plt.figure(str(ran1) + '.jpg')  # 创建自定义图像
                plt.imshow(img)
                plt.show()


get_evaluate()
