# coding=utf-8
"""
@author: Tracy
@mail: wanghongyu@ruijie.com.cn
@date: 2019.05.27
"""
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from utils.log import logger1


class Email:
    def __init__(self, server, sender, password, receiver, title, message=None, path=None, ):
        """
        初始化邮件
        :param server: smtp服务器
        :param sender: 发件人
        :param password: 发件人密码
        :param receiver: 收件人
        :param title: 邮件标题
        :param message: 邮件正文，非必填
        :param path:附件路径，可传入list，非必填
        """
        self.server = server
        self.sender = sender
        self.password = password
        self.receiver = receiver
        self.title = title
        self.msg = MIMEMultipart('related')
        self.message = message
        self.files = path

    def _attach_file(self, att_file):
        """
        将单个文件添加到附件中
        :param att_file:
        :return:
        """
        att = MIMEText(open(att_file, 'rb').read(), 'plain', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        file_name = re.split(r'[\\|/]', att_file)
        att["Content-Disposition"] = 'attachment;filename=%s' % file_name[-1]
        self.msg.attach(att)

    def send(self):
        self.msg['Subject'] = self.title
        self.msg['From'] = self.sender
        self.msg['To'] = self.receiver
        # self.msg['cc'] = self.cc

        # 邮件正文
        if self.message:
            self.msg.attach(MIMEText(self.message))

        # 添加附件(list / str)
        if self.files:
            if isinstance(self.files, list):
                for f in self.files:
                    self._attach_file(f)
            elif isinstance(self.files, str):
                self._attach_file(self.files)

        # 发送
        try:
            smtp_server = smtplib.SMTP(self.server)
        except Exception as e:
            logger1.exception('发送邮件失败，无法连接到SMTP服务器。%s',e)
        else:
            try:
                smtp_server.login(self.sender, self.password)
            except  smtplib.SMTPAuthenticationError as e:
                logger1.exception('用户名密码校验失败。%s',e)
            else:
                smtp_server.sendmail(self.sender, self.receiver.split(';'), self.msg.as_string())
            finally:
                smtp_server.quit()
                logger1.info('发送邮件{0}成功！ 收件人：{1}'.format(self.title, self.receiver))













