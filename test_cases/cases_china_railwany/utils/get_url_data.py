#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/4/9 21:19
=================================================='''
import json
import urllib.parse

def get_url_data():
    with open('../data/url_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        encoded_data = urllib.parse.urlencode(data['cases'][0])
        return encoded_data
