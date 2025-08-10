#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/3/21 19:48
=================================================='''
import json

class ReadJsonFileUtils:
    def get_request_data(self,filepath):
        with open(filepath,'r',encoding='gbk') as f:
            return json.load(f)

if __name__ == '__main__':
    readJsonObjest=ReadJsonFileUtils()
    result = readJsonObjest.get_request_data('../../resources/data/request_data.json')
    print(result['cases'][0])

