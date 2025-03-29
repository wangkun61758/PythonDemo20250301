#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/3/21 19:48
=================================================='''
import random
import json
from datetime import datetime, timedelta
from faker import Faker  # 需要安装：pip install Faker

# class TestDataGenerator:
#     def __init__(self, locale='en_US', seed=None):
#         self.fake = Faker(locale)#通过设置locale参数，可以指定生成数据的语言。例如，将locale设置为'zh_CN'可以生成中文数据，而设置为'en_US'则可以生成英文数据
#     def generate_email(self, domain=None):
#         """生成随机邮箱"""
#         return self.fake.email(domain=domain)
#     def generate_date(self,  date_format='%Y-%m-%d'):
#         """生成随机日期"""
#         return self.fake.date_between_dates(#随机生成指定范围内日期
#             date_start=datetime.now() - timedelta(days=365),
#             date_end=datetime.now()
#         ).strftime(date_format)
#     def generate_user_data(self, count=10):
#         """生成用户测试数据"""
#         users = []
#         for _ in range(count):
#             users.append({
#                 "id": self.fake.uuid4(),
#                 "name": self.fake.name(),
#                 "email": self.generate_email(),
#                 "birthdate": self.generate_date(),
#                 "address": {
#                     "street": self.fake.street_address(),
#                     "city": self.fake.city(),
#                     "zipcode": self.fake.postcode()
#                 },
#                 "phone": self.fake.phone_number(),
#                 "created_at": datetime.now().isoformat(),
#                 "is_active": random.choice([True, False])
#             })
#         return users
#     def export_to_json(self, data, filename):
#         """导出JSON文件"""
#         with open(filename, 'w', encoding='utf-8') as file1:
#             json.dump(data, file1, indent=2, ensure_ascii=False)
# # 使用示例
# if __name__ == "__main__":
#     # 初始化生成器（设置seed保证可重复性）
#     generator = TestDataGenerator(seed=42)
#     # 生成用户数据
#     users = generator.generate_user_data(1)
#     print(json.dumps(users[0], indent=2, ensure_ascii=False))
#     # 导出数据
#     generator.export_to_json(users, '../../resources/data/test_users.json')

class TestData:
    def __init__(self,locale='en_US',seed=None):
        self.fake=Faker(locale)
    def email(self,domain=None):
        return self.fake.email(domain=domain)
    def date(self,date_format='%Y-%m-%d'):
        return self.fake.date_between_dates(date_start=datetime.now()-timedelta(days=365),date_end=datetime.now()).strftime(date_format)
    def user(self,count):
        users=[]
        for _ in range(count):
            users.append(
                {
                    "id": self.fake.uuid4(),
                    "name": self.fake.name(),
                    "email": self.fake.email(),
                    "birthdate":self.date(),
                    "address": {
                        "street":self.fake.street_address(),
                        "city":self.fake.city(),
                        "zipcode":self.fake.postcode()
                    },
                    'phone': self.fake.phone_number(),
                    'created_at': datetime.now().isoformat(),
                    "is_active":random.choice([True, False])
                }
            )
        return users
    def export(self,data,filename):
        with open(filename, 'w', encoding='utf-8') as file1:
            json.dump(data,file1,indent=2, ensure_ascii=False)

if __name__ == '__main__':
    testData = TestData(seed=42)
    users=testData.user(1)
    testData.export(users,'../../resources/data/test_users1.json')