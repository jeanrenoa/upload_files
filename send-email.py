#!/usr/bin/env python3  
#coding: utf-8  
import smtplib  
from email.mime.text import MIMEText  
from email.header import Header  
  
sender = 'peng.gao@autodesk.com'  
receiver = 'peng.gao@autodesk.com'  
subject = 'python email test'  
smtpserver = 'mail-relay.autodesk.com'  
# username = 'xxx'  
# password = 'xxx'  
  
msg = MIMEText('Hello world!!!')  
msg['Subject'] = Header(subject)
msg['From'] = sender
msg['To'] = receiver
  
smtp = smtplib.SMTP()
smtp.connect('mail-relay.autodesk.com')  
# smtp.login(username, password)  
smtp.sendmail(sender, receiver, msg.as_string())  
smtp.quit()
