#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2023/11/16 8:57
=================================================='''
import datetime

import pytest
import requests
import yaml


def get_host():
    host = 'https://kyfw.12306.cn'
    return host


def get_yaml(path):
    file = open(path, 'r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)
    return data


@pytest.mark.parametrize('data', get_yaml('../../resources/yaml/station.yaml').values())
def test1(data):
    now_time = datetime.datetime.now().date()

    num = int(str(now_time).split('-', )[2]) + 1
    list = str(now_time).split('-', )
    list.pop()
    list.append(num)

    tomorrow = str(list[0]) + '-' + str(list[1]) + '-' + str(list[2])

    url = get_host() + "/otn/leftTicket/query?leftTicketDTO.train_date=" + tomorrow + "&leftTicketDTO.from_station=HZH&leftTicketDTO.to_station=PTS&purpose_codes=ADULT"

    payload = {}
    headers = {
        'Cookie': '_uab_collina=170096299263873668123651; JSESSIONID=4521C6C861D445DBCA5846ACCED5D7DF; tk=vBNYT5hZhWXEh6lQM6RjfrChQ-O2uaD1EukqsA45l1l0; route=495c805987d0f5c8c84b14f60212447d; BIGipServerotn=1574502666.50210.0000; BIGipServerpassport=971505930.50215.0000; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; fo=3b461jvd2ph9pd8cr7aqFSELc3WgFKAWZ02diwgjNDh2VfyyFipJpnQOt39itvKJd9FtL4i8FjVquyNAm8F3CEep6yp2yt0QVItyzdPFP4x8tTXKEjRVpbmOJESgxNoiIGw447g-go_ta4omLzYdjqyAAFYJQIKxSynIW6GDz2zZEQVGXX2r0XwvYW8; uKey=b89d58fcea7e6a8e1dd30d745969503053f0c52a2846ab566f931fb81f4aee6d; _jc_save_fromStation=%u676D%u5DDE%2CHZH; _jc_save_toStation=%u8386%u7530%2CPTS; _jc_save_fromDate=2023-11-27; _jc_save_toDate=2023-11-26; _jc_save_wfdc_flag=dc'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
