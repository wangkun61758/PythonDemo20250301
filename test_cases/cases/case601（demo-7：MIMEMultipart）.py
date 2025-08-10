import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

'''
1、测试报告的标题不能出现中文，否则生成的附件格式是.bin文件类型
'''


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

email = Email(host="smtp.163.com", port=25, user="18325961727@163.com", password="HVtbqZRrxFCDwNUc")
email.send(From="18325961727@163.com", To="18210958030@163.com", Subject="邮件主题", context="邮件正文",
           to_addrs="18210958030@163.com")



