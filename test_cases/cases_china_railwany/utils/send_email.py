#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：kw
@IDE    ：PyCharm
@Date   ：2025/4/12 18:57
=================================================='''
import os
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class SendMail:
    def __init__(self, host, port, user, passwd):
        self.smtp = smtplib.SMTP()
        self.smtp.connect(host=host, port=port)
        self.user = user
        self.passwd = passwd
        self.smtp.login(user=self.user, password=self.passwd)

    def send_email(self, From, To, Subject, Context, to_addrs):
        msg = MIMEMultipart()
        msg['From'] = Header(From)
        msg['To'] = Header(To)
        msg['Subject'] = Header(Subject)
        msg['to_addrs'] = Header(to_addrs)
        msg['Context'] = Header(Context)
        msg["Cc"] = '18210958030@163.com,13552790590@163.com,h18210958030@163.com'  # 抄送
        msg.attach(MIMEText("邮件正文内容", 'plain'))

        minebase = MIMEBase('application', 'octet-stream')
        minebase.set_payload(open('../report/reports.html', 'rb').read())
        encoders.encode_base64(minebase)

        minebase.add_header('Content-Disposition', f"attachment;filename={os.path.basename('../report/reports.html')}")
        msg.attach(minebase)
        self.smtp.sendmail(from_addr=self.user, to_addrs=to_addrs.split(','), msg=msg.as_string())
