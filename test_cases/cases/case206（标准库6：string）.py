#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/2/11 13:24
=================================================='''
import random
import string

def test1():
    str1=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    print(str1)

    str2=''.join(random.choice(string.digits+string.ascii_uppercase) for _ in range(10))
    print(str2)
