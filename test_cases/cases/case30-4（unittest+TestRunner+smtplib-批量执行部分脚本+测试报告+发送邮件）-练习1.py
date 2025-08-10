import os
import unittest
from unittestreport import TestRunner
from datetime import datetime
from email.header import Header
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

'''
目标1：执行指定文件夹的脚本
1、unittest.defaultTestLoader.discover(str(case_dir), pattern='a*.py', top_level_dir=None)
（1）str(case_dir)—— 读取文件的路径
（2）pattern='a*.py'—— 读取文件路径下以 a开头的python文件（比如：a*.py）
2、要运行的用例文件要按照规定的格式写，不然无法运行
（1）脚本中的类要继承 unittest.TestCase，比如：class TestStringMethods(unittest.TestCase)
（2）类中的函数要实例化使用self —— def test_isupper(self):
'''


def suite():
    unit = unittest.TestSuite()
    cases = unittest.defaultTestLoader.discover(str('../../test_cases/cases'), pattern='*.py', top_level_dir=None)
    unit.addTests(cases)
    return unit


class Email:
    def __init__(self, host, port, user, password):
        self.smtp = smtplib.SMTP()  # 创建 SMTP 对象
        self.smtp.connect(host=host, port=port)  # ‘SMTP对象’链接到服务器（host：邮件服务器地址，port：邮件服务器端口）
        self.user = user  # user：自己邮箱账户名
        # self.password = password  # password：自己邮箱账户的密码（注意是授权码，不是邮箱官网的登录密码）
        self.smtp.login(user=user, password=password)  # ‘SMTP对象’登录自己邮箱账号

    def send(self, From, To, Subject, context, to_addrs):
        msg = MIMEMultipart()
        #1、邮件正文
        msg['From'] = From
        msg['To'] = To
        msg['Subject'] = Subject
        msg['context'] = context
        msg['to_addrs'] = to_addrs
        msg.attach(MIMEText(context, 'plain'))

        #2、附件文本内容
        msg.attach(MIMEText("邮件正文内容", 'plain'))

        #3、添加本地附件
        mimebase = MIMEBase('application', 'octet-stream')  # 实例化MIMEBase并附加内容类型
        mimebase.set_payload((open("../../resources/reports/2025-02-20-23-18-36.html", "rb")).read())
        encoders.encode_base64(mimebase)  # 编码附件为base64
        mimebase.add_header('Content-Disposition',f"attachment; filename={os.path.basename('../../resources/reports/2025-02-20-23-18-36.html')}")  # 添加头信息
        msg.attach(mimebase)  # 将附件添加到邮件中
        self.smtp.sendmail(from_addr=self.user, to_addrs=to_addrs, msg=msg.as_string())  # 调用‘SMTP对象’发送邮件（from_addr：发件人地址，to_addrs：收件人地址）


if __name__ == "__main__":
    unit = suite()
    runner = TestRunner(unit, filename='3.html', report_dir='../../resources/reports', title='测试报告', tester='wk',
                        desc='自动化测试')
    runner.run()
    email = Email(host="smtp.163.com", port=25, user="18325961727@163.com", password="HVtbqZRrxFCDwNUc")
    email.send(From="18325961727@163.com", To="18210958030@163.com", Subject="邮件主题", context="邮件正文",
               to_addrs="18210958030@163.com")
