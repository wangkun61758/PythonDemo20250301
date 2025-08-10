#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/4/3 23:17
=================================================='''
import json
import os


class ReadJsonFileUtils:
    def get_request_data(file_name):
        file_path = os.path.join(os.path.dirname(__file__), '..', 'data', file_name)
        with open(file_path, 'r') as f:
            return json.load(f)
