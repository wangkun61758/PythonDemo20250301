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
        mimebase = MIMEBase('application', 'octet-stream')# 实例化MIMEBase并附加内容类型
        mimebase.set_payload((file).read())  # 设置邮件正文为附件内容
        encoders.encode_base64(mimebase)  # 编码附件为base64
        mimebase.add_header('Content-Disposition', f"attachment; filename={os.path.basename('../../resources/reports/2025-02-20-23-18-36.html')}") # 添加头信息
        message.attach(mimebase)# 将附件添加到邮件中
        self.smtp.sendmail(from_addr=self.user, to_addrs=to_addrs,msg=message.as_string())  # 调用‘SMTP对象’发送邮件（from_addr：发件人地址，to_addrs：收件人地址）
email = Email(host="smtp.163.com", port=25, user="18325961727@163.com", password="HVtbqZRrxFCDwNUc")
email.send(From="发送者昵称", To="接收人昵称", Subject="邮件主题", Context="邮件正文",
             to_addrs="18210958030@163.com")
class Email2:
    def __init__(self, host, port, user, passwd):
        self.smtp = smtplib.SMTP()
        self.smtp.connect(host=host, port=port)
        self.user = user
        self.passwd = passwd
        self.smtp.login(user=self.user, password=self.passwd)
    def send2(self, From, To, Subject, Text, to_addrs):
        # message = MIMEMultipart()
        # message['From'] = Header(From)
        # message['To'] = Header(To)
        # message['Subject'] = Header(Subject)
        # message['Text'] = Header(Text)
        # message['to_addrs'] = Header(to_addrs)
        # message.attach(MIMEText("邮件正文内容", 'plain'))
        #
        # file2=open('../../resources/reports/2025-02-20-23-18-36.html', 'rb')
        # mimebase=MIMEBase('application','octet-stream')
        # mimebase.set_payload((file2).read())
        # encoders.encode_base64(mimebase)
        # mimebase.add_header('Content-Disposition', f"attachment; filename={os.path.basename('../../resources/reports/2025-02-20-23-18-36.html')}")
        # message.attach(mimebase)
        # self.smtp.sendmail(from_addr=self.user, to_addrs=to_addrs, msg=message.as_string())

        # message = MIMEMultipart()# 创建MIMEMultipart对象
        # message['From'] = Header(From)
        # message['To'] = Header(To)
        # message['Subject'] = Header(Subject)
        # message['Text'] = Header(Text)
        # message['to_addrs'] = Header(to_addrs)
        # message.attach(MIMEText(Text,'plain'))# 创建邮件正文内容（文本/HTML）
        #
        # mimebase=MIMEBase('application', 'octet-stream')#实例化MIMEBase(多用途互联网邮件扩展)并附加内容类型
        # mimebase.set_payload((open('../../resources/reports/2025-02-20-23-18-36.html', 'rb')).read())# 设置邮件正文为附件内容
        # encoders.encode_base64(mimebase)# 编码附件为base64
        #
        # mimebase.add_header('Content-Disposition', f"attachment; filename={os.path.basename('../../resources/reports/2025-02-20-23-18-36.html')}")# 添加头信息
        # message.attach(mimebase)# 将附件添加到邮件中
        # self.smtp.sendmail(from_addr=self.user, to_addrs=to_addrs, msg=message.as_string())

        # msg = MIMEMultipart()
        # msg['From'] = From
        # msg['To'] = To
        # msg['Subject'] =Subject
        # msg['Text'] = Text
        # msg['to_addrs'] = to_addrs
        # msg.attach(MIMEText(Text,'plain'))
        #
        # mimebase=MIMEBase('application', 'octet-stream')
        # mimebase.set_payload(open('../../resources/reports/2025-02-20-23-18-36.html', 'rb').read())
        # encoders.encode_base64(mimebase)
        # mimebase.add_header('Content-Disposition', f"attachment; filename={os.path.basename('../../resources/reports/2025-02-20-23-18-36.html')}")
        # msg.attach(mimebase)
        # self.smtp.sendmail(from_addr=self.user, to_addrs=to_addrs, msg=msg.as_string())

        # msg = MIMEMultipart()
        # msg['From'] = From
        # msg['To'] = To
        # msg['Subject'] = Subject
        # msg['Text'] = Text
        # msg['to_addrs'] = to_addrs
        # msg.attach(MIMEText(Text, 'plain'))
        #
        # mimebase=MIMEBase('application','octet-stream')
        # mimebase.set_payload(open('../../resources/reports/2025-02-20-23-18-36.html','rb').read())
        # encoders.encode_base64(mimebase)
        # mimebase.add_header('Content-Dispotion',f"attachment; filename={os.path.basename('../../resources/reports/2025-02-20-23-18-36.html')}")
        # msg.attach(mimebase)
        # self.smtp.sendmail(from_addr=self.user, to_addrs=to_addrs, msg=msg.as_string())

        # msg = MIMEMultipart()
        # msg['From'] = From
        # msg['To'] = To
        # msg['Subject'] = Subject
        # msg['Text'] = Text
        # msg['to_addrs'] = to_addrs
        # msg.attach(MIMEText(Text, 'plain'))
        #
        # mimebase=MIMEBase('application', 'octet-stream')
        # mimebase.set_payload(open('../../resources/reports/2025-02-20-23-18-36.html','rb').read())
        # encoders.encode_base64(mimebase)
        # mimebase.add_header('Content-Disposition', f"attachment; filename={os.path.basename('../../resources/reports/2025-02-20-23-18-36.html')}")
        # msg.attach(mimebase)
        # self.smtp.sendmail(from_addr=self.user, to_addrs=to_addrs, msg=msg.as_string())

        # msg=MIMEMultipart()
        # msg['From']=From
        # msg['To']=To
        # msg['Subject']=Subject
        # msg['Text']=Text
        # msg['to_addrs']=to_addrs
        # msg.attach(MIMEText(Text,'plain'))
        #
        # mimebase=MIMEBase('application','octet-stream')
        # mimebase.set_payload(open('../../resources/reports/2025-02-20-23-18-36.html','rb').read())
        # encoders.encode_base64(mimebase)
        #
        # mimebase.add_header('Content-Disposition', f"attachment; filename={os.path.basename('../../resources/reports/2025-02-20-23-18-36.html')}")
        # msg.attach(mimebase)
        #
        # self.smtp.sendmail(from_addr=self.user, to_addrs=to_addrs, msg=msg.as_string())

        msg = MIMEMultipart()
        msg['From'] = From
        msg['To'] = To
        msg['Subject'] = Subject
        msg['Text'] = Text
        msg['to_addrs'] = to_addrs
        msg.attach(MIMEText(Text, 'plain'))

        mimebase = MIMEBase('application', 'octet-stream')
        mimebase.set_payload(open('../../resources/reports/2025-02-20-23-18-36.html', 'rb').read())
        encoders.encode_base64(mimebase)
        mimebase.add_header('Content-Disposition',
                            f"attachment; filename={os.path.basename('../../resources/reports/2025-02-20-23-18-36.html')}")
        msg.attach(mimebase)
        self.smtp.sendmail(from_addr=self.user, to_addrs=to_addrs, msg=msg.as_string())
email2 = Email2(host="smtp.163.com", port=25, user="18325961727@163.com", passwd="HVtbqZRrxFCDwNUc")
email2.send2(From="wk1", To="wk2", Subject="测试报告", Text="测试报告正文",
             to_addrs="18210958030@163.com")
class Email3:
    def __init__(self, host, port, user, passwd):
        self.smtp = smtplib.SMTP()
        self.smtp.connect(host=host, port=port)
        self.user = user
        self.passwd = passwd
        self.smtp.login(user=self.user, password=self.passwd)
    def send3(self,From,To,Subject,Text,to_addrs):
        msg = MIMEMultipart()
        msg['From'] = From
        msg['To'] = To
        msg['Subject'] = Subject
        msg['Text'] = Text
        msg['to_addrs'] = to_addrs
        msg.attach(MIMEText(Text, 'plain'))

        mimebase = MIMEBase('application', 'octet-stream')
        mimebase.set_payload(open('../../resources/reports/2025-02-20-23-18-36.html', 'rb').read())
        encoders.encode_base64(mimebase)
        mimebase.add_header('Content-Disposition',
                            f"attachment; filename={os.path.basename('../../resources/reports/2025-02-20-23-18-36.html')}")
        msg.attach(mimebase)
        self.smtp.sendmail(from_addr=self.user, to_addrs=to_addrs, msg=msg.as_string())
email3 = Email3(host="smtp.163.com", port=25, user="18325961727@163.com", passwd="HVtbqZRrxFCDwNUc")
email3.send3(From="wk1", To="wk2", Subject="测试报告", Text="测试报告正文",to_addrs="18210958030@163.com")

class Email4:
    def __init__(self, host, port, user, passwd):
        self.smtp=smtplib.SMTP()
        self.smtp.connect(host=host, port=port)
        self.user = user
        self.passwd = passwd
        self.smtp.login(user=self.user,password=self.passwd)
    def send4(self,From,To,Subject,Text,to_addrs):
        msg=MIMEMultipart()
        msg['From']=From
        msg['To']=To
        msg['Subject']=Subject
        msg['Text']=Text
        msg['to_addrs']=to_addrs
        msg.attach(MIMEText(Text,'plain'))

        mimebase=MIMEBase('application', 'octet-stream')
        mimebase.set_payload(open('../../resources/reports/2025-02-20-23-18-36.html','rb').read())
        encoders.encode_base64(mimebase)
        mimebase.add_header('Content-Disposition',f"attachment;filename={os.path.join('../../resources/reports/2025-02-20-23-18-36.html')}")
        msg.attach(mimebase)

        self.smtp.sendmail(from_addr=self.user, to_addrs=to_addrs, msg=msg.as_string())
email4 = Email4(host="smtp.163.com", port=25, user="18325961727@163.com", passwd="HVtbqZRrxFCDwNUc")
email4.send4(From="wk1", To="wk2", Subject="测试报告", Text="测试报告正文",to_addrs="18210958030@163.com")

class Email5:
    def __init__(self, host, port, user, passwd):
        self.smtp=smtplib.SMTP()
        self.smtp.connect(host=host, port=port)
        self.user = user
        self.passwd = passwd
        self.smtp.login(user=self.user, password=self.passwd)
    def send5(self,From,To,Subject,Text,to_addrs):
        msg=MIMEMultipart()
        msg['From']=From
        msg['To']=To
        msg['Subject']=Subject
        msg['Text']=Text
        msg['to_addrs']=to_addrs
        msg.attach(MIMEText(Text,'plain'))

        mimebase=MIMEBase('application', 'octet-stream')
        mimebase.set_payload(open('../../resources/reports/2025-02-20-23-18-36.html','rb').read())
        encoders.encode_base64(mimebase)
        mimebase.add_header('Content-Disposition',
                            f"attachment;filename={os.path.join('../../resources/reports/2025-02-20-23-18-36.html')}")
        msg.attach(mimebase)
        self.smtp.sendmail(from_addr=self.user, to_addrs=to_addrs, msg=msg.as_string())
email5 = Email5(host="smtp.163.com", port=25, user="18325961727@163.com", passwd="HVtbqZRrxFCDwNUc")
email5.send5(From="wk1", To="wk2", Subject="测试报告", Text="测试报告正文",to_addrs="18210958030@163.com")

class Email6:
    def __init__(self, host, port, user, passwd):
        self.smtp=smtplib.SMTP()
        self.smtp.connect(host=host, port=port)
        self.user = user
        self.passwd = passwd
        self.smtp.login(user=self.user, password=self.passwd)
    def send6(self,From,To,Subject,Text,to_addrs):
        msg=MIMEMultipart()
        msg['From']=From
        msg['To']=To
        msg['Subject']=Subject
        msg['Text']=Text
        msg['to_addrs']=to_addrs
        msg.attach(MIMEText(Text,'plain'))

        mimebase=MIMEBase('application','octet-stream')
        mimebase.set_payload(open('../../resources/reports/2025-02-20-23-18-36.html','rb').read())
        encoders.encode_base64(mimebase)
        mimebase.add_header( 'Content-Disposition',f"attachment;filename={os.path.basename('../../resources/reports/2025-02-20-23-18-36.html')}")
        msg.attach(mimebase)
        self.smtp.sendmail(from_addr=self.user,to_addrs=to_addrs,msg=msg.as_string())
email6 = Email6(host="smtp.163.com", port=25, user="18325961727@163.com", passwd="HVtbqZRrxFCDwNUc")
email6.send6(From="wk1", To="wk2", Subject="测试报告", Text="测试报告正文",to_addrs="18210958030@163.com")

class Email7:
    def __init__(self, host, port, user, passwd):
        self.smtp=smtplib.SMTP()
        self.smtp.connect(host=host, port=port)
        self.user = user
        self.passwd = passwd
        self.smtp.login(user=self.user,password=self.passwd)
    def send7(self,From,To,Subject,context,to_addrs):
        msg=MIMEMultipart()
        msg['From']=From
        msg['To']=To
        msg['Subject']=Subject
        msg['to_addrs']=to_addrs
        msg['context']=context
        msg.attach(MIMEText(context,'plain'))
        minebase=MIMEBase('application','octet-stream')
        minebase.set_payload(open('../../resources/reports/2025-02-20-23-18-36.html','rb').read())
        encoders.encode_base64(minebase)
        minebase.add_header('Content-Disposition',f"attachment;filename={os.path.basename('../../resources/reports/2025-02-20-23-18-36.html')}")
        msg.attach(minebase)
        self.smtp.sendmail(from_addr=self.user,to_addrs=to_addrs,msg=msg.as_string())
email7 = Email7(host="smtp.163.com", port=25, user="18325961727@163.com", passwd="HVtbqZRrxFCDwNUc")
email7.send7(From="wk1", To="wk2", Subject="测试报告", context="测试报告正文",to_addrs="18210958030@163.com")

class Email8:
    def __init__(self, host, port, user, passwd):
        self.smtp=smtplib.SMTP()
        self.smtp.connect(host=host, port=port)
        self.user = user
        self.passwd = passwd
        self.smtp.login(user=self.user,password=self.passwd)
    def send8(self,From,To,Subject,context,to_addrs):
        msg=MIMEMultipart()
        msg['From']=From
        msg['To']=To
        msg['Subject']=Subject
        msg['to_addrs']=to_addrs
        msg['context']=context
        msg.attach(MIMEText('context','plain'))

        minebase=MIMEBase('application','octet-stream')
        minebase.set_payload(open('../../resources/reports/2025-02-20-23-18-36.html','rb').read())
        encoders.encode_base64(minebase)

        minebase.add_header('Content-Disposition',f"attachment;filename={os.path.basename('../../resources/reports/2025-02-20-23-18-36.html')}")
        msg.attach(minebase)

        self.smtp.sendmail(from_addr=self.user,to_addrs=to_addrs,msg=msg.as_string())

class Email9:
    def __init__(self, host, port, user, passwd):
        self.smtp=smtplib.SMTP()
        self.smtp.connect(host=host, port=port)
        self.user = user
        self.passwd = passwd
        self.smtp.login(user=self.user,password=self.passwd)
    def send9(self,From,To,Subject,context,to_addrs):
        msg=MIMEMultipart()
        msg['From']=From
        msg['To']=To
        msg['Subject']=Subject
        msg['to_addrs']=to_addrs
        msg['context']=context
        msg.attach(MIMEText('context','palin'))

        minebase=MIMEBase('application','octet-stream')
        minebase.set_payload(open('../../resources/reports/2025-02-20-23-18-36.html','rb').read())
        encoders.encode_base64(minebase)

        minebase.add_header('Content-Dispotion',f"attachment;filename={os.path.basename('../../resources/reports/2025-02-20-23-18-36.html')}")
        msg.attach(minebase)
        self.smtp.sendmail(from_addr=self.user,to_addrs=to_addrs,msg=msg.as_string())