#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/11/16 8:57
=================================================='''
import datetime

import jsonpath
import pytest
import requests
import yaml

def test2():
    now_time = datetime.datetime.now().date()  # 2023-11-20

    num = int(str(now_time).split('-', )[2]) + 1

    list = str(now_time).split('-', )  # ['2023', '11', '20']
    list.pop()
    list.append(num)  # ['2023', '11', 21]

    tomorrow = str(list[0]) + '-' + str(list[1]) + '-' + str(list[2])  # 2023-11-21

    url = "https://m.ctrip.com/restapi/soa2/14666/json/GetBookingByStationV3ForPC"

    payload = {"DepartStation":"杭州","ArriveStation":"莆田","DepartDate":tomorrow,"ChannelName":"ctrip.pc"}
    headers = {

    }

    response = requests.request("POST", url, headers=headers, data=payload)

    dict1=response.json()
    list1=dict1['ResponseBody']['TrainItems']

    for i in range(len(list1)):
        while list1[i]['TrainName']=='D3111':
            print('订这张票：'+str(list1[i]['TrainName']))
            list2=list1[i]
            break
    print(list2)



