#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding UTF-8

"""
author: Yong Tan
"""

import sys
from PyQt4 import QtGui,QtCore,Qt
import time
import datetime
import codecs
import os
from bs4 import BeautifulSoup
import re
import cookielib
import urllib
import urllib2
import cookielib
import random
import json


try:
    import configparser 
    from urllib import request
    from urllib.request import urlopen
except:
    import urllib as request
    import ConfigParser as configparser 
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s:s


def bs4_paraser(html):
    all_value = []
    value = {}
    soup = BeautifulSoup(html, 'html.parser')
    all_div = soup.find_all('div', attrs={'class': 'message-other sign_message'})
    #print all_div
    for row in all_div:
        teacher=''
        msg=''
        all_div_teacher = row.find_all('div', attrs={'class': 'main'},limit=1)
        if all_div_teacher:
            teacher=all_div_teacher[0].h1.string
            if teacher==u'二（4）班(杨丽)':
                pass
                #print u'数学',
            elif teacher==u'二（4）班(陈红)':
                pass
                #print u'英语',
            elif teacher==u'二（4）班(唐佳媛)':
                pass
                #print u'语文',
            #print all_div_teacher[0].h1.string
       
        all_div_date = row.find_all('div', attrs={'class': 'bottom'},limit=1)
        if all_div_date:
            pass
            #print all_div_date[0].span.string,

        all_div_msg = row.find_all('div', attrs={'class': 'content'},limit=1)
        if all_div_msg:
            if all_div_msg[0].span:
                msg=all_div_msg[0].span.string
            elif all_div_msg[0].dd:
                msg=all_div_msg[0].dd.string
            if msg:
                pass
                #print msg,
        #msg=str(msg)
        #print msg,type(msg)
        #msg=msg.decode('utf-8')
        p=re.compile(u"[1-5]{1}[\、|\.][\u4e00-\u9fa5|\w|\d|\、|\：|\（\|）|\，|\《|\》|\-|\.|\—]+")
        #if msg:
            #match_obj=re.match(u"[1-5]{1}[\、|\.][\u4e00-\u9fa5|\w|\d|\、|\：|\（\|）|\，|\《|\》|\-|\.|\—]+",msg) 
            #print msg
            #msg=msg.decode('utf-8')
        #    match_obj=re.match(u"\d+",msg.decode('utf-8')) 
        #    if match_obj:
        #        print match_obj.group()
        
            
        #print
def GetTask():
    abc=u'通知 · 英语作业：1、纳米盒。2、一起作业。3、打卡朗读课本P38--41的内容。'
    #print abc.encode('utf-8')
    p=re.compile(u'[\u4e00-\u9fa5]+')
    print p.findall(abc)
    #match_obj=re.match(u"[\u4e00-\u9fa5]+",abc) 
    #if match_obj:
    #    print match_obj.group()


if __name__=="__main__":
    GetTask()


