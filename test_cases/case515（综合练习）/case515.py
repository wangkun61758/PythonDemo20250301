#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/3/1 22:19
=================================================='''
import os
from email.header import Header
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timedelta, date
import unittest
from unittestreport import TestRunner
import time
'''
1、要想执行到相关测试脚本（否则测试报告中执行到的测试脚本会为空），测试脚本要放到类中，且这个类要传入参数“unittest.TestCase”，同时调用unittest执行main函数类似于：
class c(unittest.TestCase):
    def setUp(self):
if __name__ == '__main__':
    unittest.main()
'''
class Email:
    def __init__(self, host, port, user, password):
        self.smtp = smtplib.SMTP()  # 创建 SMTP 对象
        self.smtp.connect(host=host, port=port)  # ‘SMTP对象’链接到服务器（host：邮件服务器地址，port：邮件服务器端口）
        self.user = user  # user：自己邮箱账户名
        self.password = password  # password：自己邮箱账户的密码（注意是授权码，不是邮箱官网的登录密码）
        self.smtp.login(user=self.user, password=self.password)  # ‘SMTP对象’登录自己邮箱账号
    def send(self, From, To, Subject, Context, to_addrs, path):
        message = MIMEMultipart()  # 初始化邮件对象
        message['From'] = Header(From)
        message['To'] = Header(To)
        message['Subject'] = Header(Subject)
        message['Context'] = Header(Context)
        message.attach(MIMEText("邮件正文内容", 'plain'))
        # 2、添加附件到邮件中
        attachment = open(path, "rb")  # 以二进制读取模式打开文件
        # 实例化MIMEBase并附加内容类型
        minebase = MIMEBase('application', 'octet-stream')
        minebase.set_payload((attachment).read())  # 设置邮件正文为附件内容
        encoders.encode_base64(minebase)  # 编码附件为base64
        minebase.add_header('Content-Disposition', f"attachment; filename= {path}")  # 添加头信息
        message.attach(minebase)  # 将附件添加到邮件中
        self.smtp.sendmail(from_addr=self.user, to_addrs=to_addrs,msg=message.as_string())

def suite():
    suite = unittest.TestSuite()
    cases=unittest.defaultTestLoader.discover('../case515（综合练习）', pattern='Test1.py', top_level_dir=None)
    suite.addTest(cases)
    return suite

if __name__ == '__main__':
    unit=suite()
    now = datetime.now()
    time1 = now.strftime("%Y%m%d%H%M%S")#报告的文件名中不能出现“-”和“：”
    filename1 = time1 + '.html'
    path1=os.path.join('../../resources/reports/', filename1)
    runner = TestRunner(unit, filename=filename1, report_dir='../../resources/reports', title='测试报告', tester='wk', desc='自动化测试')
    runner.run()
    time.sleep(5)

    email = Email(host="smtp.163.com", port=25, user="18325961727@163.com", password="HVtbqZRrxFCDwNUc")
    email.send(From="发送者昵称", To="接收人昵称", Subject="邮件主题", Context="邮件正文",
             to_addrs="18210958030@163.com",path=path1)
