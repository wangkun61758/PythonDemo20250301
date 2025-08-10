#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/4/13 11:15
=================================================='''
import urllib


def test1():
    dict = {
        "leftTicketDTO.train_date": "2025-04-15",
        "leftTicketDTO.from_station": "BJP",
        "leftTicketDTO.to_station": "SHH",
        "purpose_codes": "ADULT"
    }
    str1 = urllib.parse.urlencode(dict)
    print(str1)

