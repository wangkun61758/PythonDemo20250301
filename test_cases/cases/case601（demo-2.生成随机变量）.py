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
    fake=Faker()
    uuid=fake.uuid4()
    print(uuid)
    return uuid
uuid()

def phone_num():
    phoneNum = '135' + ''.join(random.choice(string.digits) for _ in range(8))
    print(phoneNum)
    return phoneNum
phone_num()

def email():
    fake=Faker()
    email=fake.email(domain='163.com')
    print(email)
    return email
email()

def address():
    fake=Faker(locale='zh_CN')
    address= {
        'country': fake.country(),
        'city':fake.city(),
        'street':fake.street_address(),
        'postcode':fake.postcode()

    }
    print(address)
    return address
address()

def id_card():
    fake=Faker(locale='zh_CN')
    id_card = fake.ssn(min_age=18,max_age=80)
    print(id_card)
    return id_card
id_card()

def user():
    fake=Faker(locale='zh_CN')
    user={
        '姓名':fake.name(),
        '身份证号':fake.ssn(min_age=18,max_age=90),
        '手机号':fake.phone_number(),
        '邮箱':fake.email(),
        '地址':fake.address()

    }
    print(user)
    return user
user()