#! /usr/bin/env python

import fnmatch
import os
import smtplib  
from email.mime.text import MIMEText  
from email.header import Header  

def find_file_and_update_baseline(baseline):
    """ Go through the specified path and find the files
        compare them with the baseline that contains the existing files
        update the baseline at the end """

    rootPath = '//panda.autodesk.com/BRE_MASTERS_PSEB/ADSK_Materials/Longbow/px86x64'
    pattern = '*.zip'

    file_write = open('logfile.txt', 'a')
  
    for root, dirs, files in os.walk(rootPath):
        for filename in fnmatch.filter(files, pattern):
            if filename not in baseline:
                print(filename)
                baseline.append(filename)
                file_write.write(filename + "\n")
                send_email(filename)

            # print(os.path.join(root, filename))

    file_write.close()

def read_logfile():
    """ read all lines from the log file and strip return charater
        export the result to a list """
    
    file_read = open('logfile.txt', 'r')

    filedata = []
    for filename in file_read:
        filedata.append(filename.strip('\n'))

    file_read.close()
    return filedata

def print_logfile(filedata):
    for filename in filedata:
        print (filename)

def send_email(ILM_library):
    """ Send email through STMP email server """

    sender = 'peng.gao@autodesk.com'  
    receiver = 'peng.gao@autodesk.com'  
    subject = 'ILM: There is new medium material library in AIRMax BB'  
    smtpserver = 'mail-relay.autodesk.com'  
    # username = 'xxx'  
    # password = 'xxx'  
  
    msg = MIMEText(ILM_library)  
    msg['Subject'] = Header(subject)
    msg['From'] = sender
    msg['To'] = receiver
  
    smtp = smtplib.SMTP()
    smtp.connect('mail-relay.autodesk.com')  
    # smtp.login(username, password)  
    smtp.sendmail(sender, receiver, msg.as_string())  
    smtp.quit()

# Read the logfile as baseline
baseline = read_logfile()
# print_logfile(baseline)

# Find all files in the specified server path
find_file_and_update_baseline(baseline)
