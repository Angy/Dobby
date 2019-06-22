#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import datetime
import smtplib
import os

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
logger.addHandler(handler)

path = '/path/to/files/to/be/used'

for file in os.listdir(path):
    filepath = os.path.join(path, file)
    with open(filepath, 'r') as f:

        SENDER = 'YourEmail'
        SENDER_PWD = 'YourPassword'
        RECIPIENT = 'RecipientEmail'
        SUBJECT = 'That pretty one!'

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER, SENDER_PWD)

        msg = MIMEMultipart()
        msg['Subject'] = SUBJECT
        msg['From'] = 'Dobby <{}>'.format('SENDER')
        msg['TO'] = RECIEVER

        body = f.read()
        html = open('mail.html', 'r').read()
        html=html.replace('{{ content }}', body)
        msg.attach(MIMEText(html,'html'))

        server.sendmail(SENDER, RECIEVER, msg.as_string())

        logger.warning('mail sent at %s' %datetime.datetime.now())
        server.quit()
