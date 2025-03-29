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
        self.password = password  # password：自己邮箱账户的密码（注意是授权码，不是邮箱官网的登录密码）
        self.smtp.login(user=self.user, password=self.password)  # ‘SMTP对象’登录自己邮箱账号
    def send(self, From, To, Subject, Context, to_addrs,path):
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
        minebase.add_header('Content-Disposition',f"attachment; filename= {path}")  # 添加头信息
        message.attach(minebase)  # 将附件添加到邮件中
        self.smtp.sendmail(from_addr=self.user, to_addrs=to_addrs,msg=message.as_string())  # 调用‘SMTP对象’发送邮件（from_addr：发件人地址，to_addrs：收件人地址）
if __name__ == "__main__":
    unit = suite()
    runner = TestRunner(unit, filename='3.html', report_dir='../../resources/reports', title='测试报告', tester='wk',desc='自动化测试')
    runner.run()
    email = Email(host="smtp.163.com", port=25, user="18325961727@163.com", password="HVtbqZRrxFCDwNUc")
    email.send(From="这是发送者昵称", To="这是接收人的昵称", Subject="这是邮件主题", Context="邮件正文",to_addrs="18210958030@163.com",path='../../resources/reports/3.html')
'''
练习：2025/3/20（3）
'''
class Email2:
    def __init__(self, host, port, user, password):
        self.smtp=smtplib.SMTP()
        self.smtp.connect(host=host, port=port)
        self.user = user
        self.password = password
        self.smtp.login(user=self.user,password=self.password)
    def send(self, From, To, Subject, Context, to_addrs,path):
        message=MIMEMultipart()
        message["From"]=Header(From)
        message["To"]=Header(To)
        message["Subject"]=Header(Subject)
        message["Context"]=Header(Context)
        message.attach(MIMEText('邮件正文','plain'))
        attachment = open(path, "rb")
        minebase=MIMEBase('application', 'octet-stream')
        minebase.set_payload(attachment.read())
        encoders.encode_base64(minebase)
        minebase.add_header(('Content-Disposition',f"attachment; filename= {path}"))
        minebase.attach(minebase)

        self.smtp.sendmail(from_addr=self.user, to_addrs=to_addrs,msg=message.as_string())
if __name__ == '__main__':
    unit = suite()
    runner=TestRunner(unit, filename='3.html', report_dir='../../resources/reports', title='测试报告', tester='wk',desc='自动化测试')
    runner.run()
    email = Email(host="smtp.163.com", port=25, user="18325961727@163.com", password="HVtbqZRrxFCDwNUc")
    email.send(From="这是发送者昵称", To="这是接收人的昵称", Subject="这是邮件主题", Context="邮件正文",to_addrs="18210958030@163.com",path='../../resources/reports/3.html')

