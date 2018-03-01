# -*- coding:utf-8 -*-
#author:hanyou11
from bs4 import *
import sys,urllib2
import smtplib  
from email.mime.text import MIMEText
from email.header import Header
import re

f_bofore= open('C:\Users\\admin\\111.txt','r')
txt_before = f_bofore.read()
f_bofore.close()

urlname = 'http://pg.njupt.edu.cn/1049/list.htm'
url = urllib2.urlopen(urlname) 
context = url.read()
pattern = re.compile('>.*?<td align="left"><a href=\'(.*?)\' target=\'_blank\' title=\'(.*?)\'>.*?<td.*?><.*?>(.*?)<',re.S)
items0 = pattern.findall(context)
print items0
ftp = open('C:\Users\\admin\\111.txt','w')
for item in items0:
    ftp.write(item[1])
    ftp.write('    ') 
    ftp.write('http://pg.njupt.edu.cn')
    ftp.write(item[0])
    ftp.write('    ')
    ftp.write(item[2])
    ftp.write('\n')

ftp.close( ) 
f= open('C:\Users\\admin\\111.txt','r')
txt = f.read()
f.close()

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

def sendemail(body):
    from_addr = 'xxxx@njupt.edu.cn'
    password = 'xxxx'
    to_addr = ['xxxx@qq.com']
    smtp_server = 'em.njupt.edu.cn'

    msg = MIMEText(body.decode('utf-8'), 'plain', 'utf-8')
    msg['From'] = _format_addr(u'高季 <%s>' % from_addr)
    msg['To'] = _format_addr(u'接收人 <%s>' % to_addr)
    msg['Subject'] = Header(u'通知更新', 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()

if txt==txt_before:
    pass
else:
    sendemail(txt)
