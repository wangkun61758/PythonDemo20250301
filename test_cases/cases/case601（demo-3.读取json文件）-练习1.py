#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/3/21 19:48
=================================================='''
import json


class ReadJsonFile:
    def get_data(self,path):
        with open(path,'r',encoding='gbk') as f:
            return json.load(f)
if __name__ == '__main__':
    object=ReadJsonFile()
    data=object.get_data('../../resources/data/request_data.json')
    print(data['cases'][0])