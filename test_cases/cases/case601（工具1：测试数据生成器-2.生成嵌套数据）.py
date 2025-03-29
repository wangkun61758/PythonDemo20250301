#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/3/21 19:48
=================================================='''
import random
import csv
import json
import string
from datetime import datetime, timedelta
from faker import Faker  # 需要安装：pip install Faker

class TestDataGenerator:
    def __init__(self, locale='en_US', seed=None):
        self.fake = Faker(locale)#通过设置locale参数，可以指定生成数据的语言。例如，将locale设置为'zh_CN'可以生成中文数据，而设置为'en_US'则可以生成英文数据

    def generate_random_string(self, length=8, prefix='', suffix=''):
        """生成随机字符串"""
        chars = string.ascii_letters + string.digits
        return prefix + ''.join(random.choice(chars) for _ in range(length)) + suffix#_是一个常见的占位符

    def generate_float(self, min_val=0, max_val=100, decimal_digits=2):
        """生成随机浮点数"""
        return round(random.uniform(min_val, max_val), decimal_digits)

    def generate_nested_data(self, num_children=2):#
        """生成嵌套数据结构"""
        return {
            "parent_id": self.generate_random_string(6, 'PAR_'),
            "children": [{
                "child_id": self.generate_random_string(4, 'CH_'),
                "value": self.generate_float()
            } for _ in range(num_children)]
        }

    def export_to_json(self, data, filename):
        """导出JSON文件"""
        with open(filename, 'w', encoding='utf-8') as file1:
            json.dump(data, file1, indent=2, ensure_ascii=False)


# 使用示例
if __name__ == "__main__":
    # 初始化生成器（设置seed保证可重复性）
    generator = TestDataGenerator(seed=42)

    # 生成嵌套数据
    data = [generator.generate_nested_data() for _ in range(1)]
    print(json.dumps(data, indent=2, ensure_ascii=False))

    # 导出数据
    generator.export_to_json(data, '../../resources/data/test_users2.json')