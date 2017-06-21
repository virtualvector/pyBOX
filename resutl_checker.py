#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 22:07:11 2017

@author: vector
"""

import urllib2
import sys
import re
import os
import time
import smtplib
from bs4 import BeautifulSoup
import urllib2
import time


def mail(value):
    fromaddr = 'jforjilla@gmail.com'
    toaddrs  = 'rohithrajreganti@gmail.com'
    msg = "\r\n".join([
      "From: rohithrajreganti@gmail.com",
      "To: jforjilla@gmail.com",
      "Subject: {}".format(value),
      "","announced" ])
    username = 'jforjilla@gmail.com'
    password = '$rupee123'
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
    
urlstring="http://result.vtu.ac.in/cbcs_results2017.aspx?usn=1pe15cs127&sem=3"   
strings = ['All','Regions','regions','Bangalooru','bangalore']
resstring="could not find result url"
while 1:
    try:
        html_content = urllib2.urlopen('http://result.vtu.ac.in').read()
        print "trying"
        
        for i in strings:
            matches = re.findall(i, html_content)
            
         
         
            if len(matches) != 0:
                try:
                    file1=urllib2.urlopen(urlstring)
                    soup=BeautifulSoup(file1,'lxml')
                    tag3=soup.select("#lblSGPA")
                    for i in tag3 :
                        p=i.string
                        resstring=i.string
                except:
                    pass
                    
                mail(resstring)
                print "mail sent"
                sys.exit(0)
                print "did not exit"
                quit()
                print "did not quit"
                #os.system("notify-send 'Yeah' 'Result is not declared yet'")
               
         
        
               
        time.sleep(30)
        
    except Exception as e:
        print e
        
        continue
       
       
       
       
       
       
       