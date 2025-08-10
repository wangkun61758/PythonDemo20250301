#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/4/8 22:25
=================================================='''
import json
import os.path
from test_cases.cases_china_railwany.common.random_datas import date_time


def create_url_data(count):
    query_data = []
    dict1 = {}
    for i in range(count):
        query_data.append({
            'leftTicketDTO.train_date': date_time(),
            'leftTicketDTO.from_station': 'BJP',
            'leftTicketDTO.to_station': 'SHH',
            'purpose_codes': 'ADULT'
        })
    dict1['cases'] = query_data
    return dict1


def export():
    test_data = create_url_data(2)
    if not os.path.exists('../data/'):
        os.mkdir('../data/')
    with open('../data/url_data.json', 'w', encoding='utf-8') as f:
        json.dump(test_data, f, ensure_ascii=False, indent=4)
