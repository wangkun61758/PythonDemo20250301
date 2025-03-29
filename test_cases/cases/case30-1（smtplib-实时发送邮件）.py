import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import schedule
'''
1、声明一个邮件类
类中的初始化函数中已经定义的参数（比如：user），类中自定义的函数中无需再次重复定义（比如：user）,但是自定义函数中可以直接使用该参数（比如：user）
'''
# class Email:
#     '''
#     1.1、定义类的初始化属性（定义类的时候，若是添加__init__方法，那么在创建类的实例的时候，实例会自动调用这个方法，对实例的属性进行初使化）
#     '''
#     def __init__(self, host, port, user, password):
#         self.smtp = smtplib.SMTP()  # 创建 SMTP 对象
#         self.smtp.connect(host=host, port=port)  # ‘SMTP对象’链接到服务器（host：邮件服务器地址，port：邮件服务器端口）
#
#         self.user = user  # user：自己邮箱账户名
#         self.password = password  # password：自己邮箱账户的密码（注意是授权码，不是邮箱官网的登录密码）
#         self.smtp.login(user=self.user, password=self.password)  # ‘SMTP对象’登录自己邮箱账号
#     '''
#     1.2定义类中的函数用以发送邮件(实例化类对象后，可用实例化的对象去调用此函数)
#     '''
#     def send(self, From, To, Subject, Context, to_addrs):
#         message = MIMEText(Context, 'plain', 'utf-8')  # Context：邮件正文
#         message['From'] = Header(From)  # From：发送者昵称（随便取）
#         message['To'] = Header(To)  # To：接收者昵称（随便取）
#         message['Subject'] = Header(Subject)  # Subject：邮件主题
#         self.smtp.sendmail(from_addr=self.user, to_addrs=to_addrs,msg=message.as_string())  # 调用‘SMTP对象’发送邮件（from_addr：发件人地址，to_addrs：收件人地址）
#
# # 2.1、实例化类的一个对象（创建类的实例的时候，实例会自动调用“__init__方法”）
# email = Email(host="smtp.163.com", port=25, user="18325961727@163.com", password="HVtbqZRrxFCDwNUc")
#
# # # 2.2实例化的对象去调用类中的方法
# # email.send(From="这是发送者昵称", To="这是接收人的昵称", Subject="这是邮件主题", Context="邮件正文",to_addrs="18210958030@163.com")
#
# def job():
#     email.send(From="这是发送者昵称1", To="这是接收人的昵称1", Subject="这是邮件主题1", Context="邮件正文1",to_addrs="18210958030@163.com")
#
# # 设定定时任务，例如每天上午10点发送邮件
# schedule.every().day.at("21:57").do(job)
# while True:
#     schedule.run_pending()
#     time.sleep(1)  # 等待1秒再次检查是否有新的定时任务需要执行

# class Email:
#     def __init__(self,host,port,user,password):
#         self.smtp = smtplib.SMTP()  # 创建 SMTP 对象
#         self.smtp.connect(host=host, port=port)  # ‘SMTP对象’链接到服务器（host：邮件服务器地址，port：邮件服务器端口）
#         self.user = user  # user：自己邮箱账户名
#         self.password = password  # password：自己邮箱账户的密码（注意是授权码，不是邮箱官网的登录密码）
#         self.smtp.login(user=self.user, password=self.password)  # ‘SMTP对象’登录自己邮箱账号
#
#     def send(self,From, To, Subject, Context, to_addrs):
#         message = MIMEMultipart()# 初始化邮件对象
#         message['From'] = Header(From)
#         message['To'] = Header(To)
#         message['Subject'] = Header(Subject)
#         message['Context']=Header(Context)
#         message.attach(MIMEText("邮件正文内容", 'plain'))
#
#         self.smtp.sendmail(from_addr=self.user, to_addrs=to_addrs,msg=message.as_string())
# email = Email(host="smtp.163.com", port=25, user="18325961727@163.com", password="HVtbqZRrxFCDwNUc")
# email.send(From="发送者昵称", To="接收人昵称", Subject="邮件主题", Context="邮件正文",
#              to_addrs="18210958030@163.com")

class Email1:
    def __init__(self,host,port,user,password):
        self.smtp=smtplib.SMTP()
        self.smtp.connect(host=host, port=port)
        self.user = user
        self.password = password
        self.smtp.login(user=self.user, password=self.password)

    def send1(self,From,To,Subject,Context,to_addrs):
        message=MIMEMultipart()
        message['From']=Header(From)
        message['To']=Header(To)
        message['Subject']=Header(Subject)
        message['Context']=Header(Context)
        message['to_addrs']=to_addrs
        message.attach(MIMEText('正文内容','plain'))

        self.smtp.sendmail(from_addr=self.user,to_addrs=to_addrs,msg=message.as_string())
email1=Email1(host="smtp.163.com", port=25, user="18325961727@163.com", password="HVtbqZRrxFCDwNUc")
email1.send1(From="发送者昵称", To="接收人昵称", Subject="邮件主题", Context="邮件正文",
             to_addrs="18210958030@163.com")

class Email2:
    def __init__(self,host,port,user,passwd):
        self.smtp=smtplib.SMTP()
        self.smtp.connect(host=host,port=port)
        self.user=user
        self.passwd=passwd
        self.smtp.login(user=self.user,password=self.passwd)
    def send2(self,From,To,Subject,Text,to_addrs):
        msg = MIMEMultipart()
        msg['From'] = Header(From)
        msg['To'] = Header(To)
        msg['Subject'] = Header(Subject)
        msg['Text'] = Header(Text)
        msg['to_addrs']=Header(to_addrs)
        msg.attach(MIMEText("邮件正文内容", 'plain'))
        self.smtp.sendmail(from_addr=self.user,to_addrs=to_addrs,msg=msg.as_string())
email2=Email2(host="smtp.163.com", port=25, user="18325961727@163.com", passwd="HVtbqZRrxFCDwNUc")
email2.send2(From="发送者昵称",To="接收人昵称",Subject="邮件主题",Text="邮件正文",to_addrs="18210958030@163.com")

class Email3:
    def __init__(self,host,port,user,passwd):
        self.smtp=smtplib.SMTP()
        self.smtp.connect(host=host,port=port)
        self.user=user
        self.passwd=passwd
        self.smtp.login(user=self.user,password=self.passwd)
    def send3(self,From,To,Subject,Text,to_addrs):
        msg=MIMEMultipart()
        msg['From']=Header(From)
        msg['To']=Header(To)
        msg['Subject'] = Header(Subject)
        msg['Text'] = Header(Text)
        msg['to_addrs']=Header(to_addrs)
        msg.attach(MIMEText("邮件正文内容", 'plain'))
        self.smtp.sendmail(from_addr=self.user,to_addrs=to_addrs,msg=msg.as_string())
email3=Email3(host="smtp.163.com", port=25, user="18325961727@163.com", passwd="HVtbqZRrxFCDwNUc")
email3.send3(From="wk1", To="wk2", Subject="测试报告", Text="测试报告正文",
             to_addrs="18210958030@163.com")