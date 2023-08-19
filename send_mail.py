# -*- coding: utf-8 -*-

import os
import getpass
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


# mail_server = smtplib.SMTP('smtp.gmail.com', 587)
# mail_server.starttls()
# pwd = 'toahvxoflsqmtrwm'
# mail_server.login('example@gmail.com', pwd)

mail_server = smtplib.SMTP('smtp.naver.com', 587)
mail_server.ehlo()
mail_server.starttls()
mail_server.ehlo()
# mail_server.starttls()
pwd = getpass.getpass('pwd> ')
# pwd = ''
mail_server.login('login@naver.com', pwd)

for i in range(26, 51):
    # target_filename = 'pycharm-community-2021.3.zip.0%.2d' % (i+1)
    target_filename = 'Anaconda3-2021.11-Windows-x86_64.zip.%.3d' % (i+1)
    print(target_filename)

    # 제목, 본문 작성
    msg = MIMEMultipart()
    msg['From'] = 'login@naver.com'
    msg['To'] = 'target1@gmail.com, target2@gmail.com'
    msg['Subject'] = target_filename
    msg.attach(MIMEText('test', 'plain'))

    # 파일첨부 (파일 미첨부시 생략가능)
    attachment = open('./data/%s' % target_filename, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    filename = os.path.basename('./data/%s' % target_filename)
    part.add_header('Content-Disposition', "attachment; filename= " + filename)
    msg.attach(part)

    # 메일 전송
    # mail_server.sendmail("ggtt7@naver.com", "example@gmail.com", msg.as_string())
    mail_server.sendmail("login@naver.com", msg['To'].split(','), msg.as_string())

mail_server.quit()
