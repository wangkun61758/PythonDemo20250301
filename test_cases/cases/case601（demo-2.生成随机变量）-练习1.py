#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/3/21 19:48
=================================================='''
import random
import string

from faker.proxy import Faker


def uuid():
    fake=Faker(locale='zh_CN')
    uuid=fake.uuid4()
    return uuid
uuid()
def phone():
    faker=Faker(locale='zh_CN')
    phone=faker.phone_number()
    return phone
phone()
def email():
    faker=Faker(locale='zh_CN')
    email=faker.email()
    return email
email()
def id_card():
    faker=Faker('zh_CN')
    id_card=faker.ssn(min_age=18,max_age=80)
    return id_card
id_card()
def address():
    fake=Faker(locale='zh_CN')
    address={
        '国家':fake.country(),
        '城市':fake.city(),
        '街道':fake.street_address()
    }
    return address
address()
def user():
    faker=Faker(locale='zh_CN')
    user={
        'name':faker.name(),
        'email':faker.email(),
        'phone':'135'+''.join(random.choice(string.digits) for _ in range(8)),
        'birthday':faker.date(pattern='%Y-%m-%d')
    }
    return user
user()

