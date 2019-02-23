# 电子邮件
# MUA = mail User Agent = foxmail,outlook等电子邮箱软件
# MTA = mail tranfer agent = 服务提供商 = 网易，新浪
# MDA = mail delivery agent = 邮件投递代理 = 电子邮箱 = 电子邮件长期存储的位置
# 发件人 -> MUA -> MTA -> MTA -> 若干个 MTA -> MDA <- MUA <- 收件人

# 发送邮件的协议：MUA和MTA使用的 SMTP：Simple Mail Transfer Protocol
# 收邮件协议：POP和IMAP
#
# Python 对 SMTP 支持有 smtplib 和 email 两个模块，email 负责构造邮件，
# smtplib 负责发送邮件。


# 构造mime数据
from email.mime.text import MIMEText

mime_text = MIMEText('你好，这是来自python smtp协议的邮件！', 'plain', 'utf-8')

# 发件人
from_addr = input('输入邮箱：')
password = input('输入密码：')
# 输入收件人地址
to_addr = input('输入收件人邮箱：')
smtp_addr = input('输入smtp服务器地址')

import smtplib

server = smtplib.SMTP(smtp_addr, 25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],mime_text.as_string())
server.quit()
