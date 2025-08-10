import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class Email:
    def __init__(self, host, port, user, password):
        self.smtp = smtplib.SMTP()
        self.smtp.connect(host=host, port=port)
        self.user = user
        # self.password = password
        self.smtp.login(user=user, password=password)

    def send(self, From, To, Subject, context, to_addrs):
        msg = MIMEMultipart()
        msg['From'] = From
        msg['To'] = To
        msg['Subject'] = Subject
        msg['context'] = context
        msg['to_addrs'] = to_addrs
        msg.attach(MIMEText(context, 'plain'))

        msg.attach(MIMEText("附件文本内容", 'plain'))

        mimebase = MIMEBase('application', 'octet-stream')
        mimebase.set_payload((open("../../resources/reports/2025-02-20-23-18-36.html", "rb")).read())
        encoders.encode_base64(mimebase)
        mimebase.add_header('Content-Disposition',f"attachment; filename={os.path.basename('../../resources/reports/2025-02-20-23-18-36.html')}")
        msg.attach(mimebase)

        self.smtp.sendmail(from_addr=self.user, to_addrs=to_addrs,msg=msg.as_string())

email = Email(host="smtp.163.com", port=25, user="18325961727@163.com", password="HVtbqZRrxFCDwNUc")
email.send(From="18325961727@163.com", To="18210958030@163.com", Subject="邮件主题", context="邮件正文",
           to_addrs="18210958030@163.com")




