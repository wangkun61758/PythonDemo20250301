#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/3/21 19:48
=================================================='''
import requests


def send_request(method, url, headers, data):
    try:
        # requests.request(method=method, url=url, headers=headers, data=data)返回的值只能赋予一个对象，也就是说左边只能有一个值
        res = requests.request(method=method, url=url, headers=headers, data=data)
        print('\n获取到的返回值：' + str(res.json()))
        return res, res.status_code  # return的返回值可以有多个
    except Exception as e:
        return {'error': str(e)}, 500


class HttpUtils:
    def send_request(self, method, url, headers, payload):
        res, status_code = send_request(method, url, headers, payload)
        return res, status_code


if __name__ == '__main__':
    url = 'https://kyfw.12306.cn/otn/leftTicket/queryU?leftTicketDTO.train_date=2025-08-12&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=SHH&purpose_codes=ADULT'
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': '_uab_collina=175471261322738160538672; JSESSIONID=7D3D1481568A31777B554E395FF1F7E3; BIGipServerotn=1306067210.24610.0000; BIGipServerpassport=921174282.50215.0000; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; route=c5c62a339e7744272a54643b3be5bf64; _jc_save_fromStation=%u5317%u4EAC%2CBJP; _jc_save_toStation=%u4E0A%u6D77%2CSHH; _jc_save_fromDate=2025-08-09; _jc_save_toDate=2025-08-09; _jc_save_wfdc_flag=dc',
        'If-Modified-Since': '0',
        'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E5%8C%97%E4%BA%AC,BJP&ts=%E5%90%88%E8%82%A5,HFH&date=2025-04-12&flag=N,N,Y',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.95 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }
    payload = {}
    sendObject = HttpUtils()
    sendObject.send_request('GET', url, headers, payload)
