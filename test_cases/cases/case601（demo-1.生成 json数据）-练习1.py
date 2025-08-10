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

class Jsondata:
    def  __init__(self,local='zh_CN'):
        self.fake=Faker(local)
    def sendemail(self,domain='163.com'):
        return self.fake.email(domain=domain)

    def date(self, date_format='%Y-%m-%d'):
        return (self.fake.date_between_dates(date_start=datetime.now() - timedelta(days=365),date_end=datetime.now())
                .strftime(date_format))

    def jsonData(self,count):
        list=[]
        for i in range(count):
            list.append({
                'name':self.fake.name(),
                'age':random.randint(20,80),
                'id_card':self.fake.ssn(),
                'email':self.sendemail(),
                'phone':self.fake.phone_number(),
                'brithday':self.fake.date(),
                'adress':{
                    'city':self.fake.city(),
                    'street':self.fake.street_address()
                },
                'active':random.choice(['true','false']),
                'time':self.date()
            })
        return list
    def createJson(self,data,path):
        with open(path,'w',encoding='utf-8') as f:
            json.dump(data,f,ensure_ascii=False,indent=4)
if __name__ == '__main__':
    object = Jsondata()
    data=object.jsonData(2)
    object.createJson(data,'../../resources/data/demo.json')


