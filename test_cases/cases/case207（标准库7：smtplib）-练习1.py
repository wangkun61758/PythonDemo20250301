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
        self.password = password  # password：自己邮箱账户的密码（注意是授权码，不是邮箱官网的登录密码）
        self.smtp.login(user=self.user, password=self.password)  # ‘SMTP对象’登录自己邮箱账号

    def send(self, From, To, Subject, Context, to_addrs):
        message = MIMEMultipart()  # 初始化邮件对象
        msg = MIMEMultipart()
        msg['From'] = From
        msg['To'] = To
        msg['Subject'] = Subject
        msg['Text'] = Context
        msg['to_addrs'] = to_addrs
        msg.attach(MIMEText(Context, 'plain'))
        message.attach(MIMEText("邮件正文内容", 'plain'))
        file = open("../../resources/reports/2025-02-20-23-18-36.html", "rb")  # # 2、添加附件到邮件中(以二进制读取模式打开文件)
        mimebase = MIMEBase('application', 'octet-stream')  # 实例化MIMEBase并附加内容类型
        mimebase.set_payload((file).read())  # 设置邮件正文为附件内容
        encoders.encode_base64(mimebase)  # 编码附件为base64
        mimebase.add_header('Content-Disposition',
                            f"attachment; filename={os.path.basename('../../resources/reports/2025-02-20-23-18-36.html')}")  # 添加头信息
        message.attach(mimebase)  # 将附件添加到邮件中
        self.smtp.sendmail(from_addr=self.user, to_addrs=to_addrs,
                           msg=message.as_string())  # 调用‘SMTP对象’发送邮件（from_addr：发件人地址，to_addrs：收件人地址）


email = Email(host="smtp.163.com", port=25, user="18325961727@163.com", password="HVtbqZRrxFCDwNUc")
email.send(From="发送者昵称", To="接收人昵称", Subject="邮件主题", Context="邮件正文",
           to_addrs="18210958030@163.com")


