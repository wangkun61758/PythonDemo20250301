#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/3/21 19:48
=================================================='''
import json
import random
from datetime import datetime, timedelta

from faker import Faker  # 需要安装：pip install Faker


class Jsondata():
    def __init__(self, locale='en_US'):
        self.fake = Faker(locale)

    def email(self, domain='163.com'):
        return self.fake.email(domain=domain)

    def date(self, date_format='%Y-%m-%d'):
        return self.fake.date_between_dates(date_start=datetime.now() - timedelta(days=365),
                                            date_end=datetime.now()).strftime(date_format)

    def jsondata(self, count):
        list = []
        for _ in range(count):
            list.append(
                {
                    'id': self.fake.uuid4(),
                    'name': self.fake.name(),
                    'email': self.email(),
                    'birthdate': self.date(),
                    'address': {
                        'city': self.fake.city(),
                        'street': self.fake.street_address()
                    },
                    'created_time': datetime.now().strftime('%y-%m-%d %H:%M:%S'),
                    'is_active': random.choice([True, False])
                }
            )
        return list

    def create_json(self, jsondata, filepath):
        with open(filepath, 'w', encoding='utf-8') as file1:
            json.dump(jsondata, file1, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    object = Jsondata()
    jsondata = object.jsondata(1)
    object.create_json(jsondata, '../../resources/data/demo.json')
