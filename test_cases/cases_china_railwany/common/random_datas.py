#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/4/8 22:25
=================================================='''
import random
import string
from faker import Faker
from datetime import datetime, timedelta


def phone_num():
    phoneNum = '1' + ''.join(random.sample(string.digits, 10))
    return phoneNum


def uuid():
    faker = Faker()
    uuid = faker.uuid4()
    return uuid


def date_time():
    now = datetime.now().date()
    date = now + timedelta(days=3)
    return str(date)
