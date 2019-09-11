#encoding=utf-8
'''
Created on 2018年3月2日

@author: aadebuger
'''
import requests
import json
import re
import yaml
import sys
from functools import reduce
import pandas as pd
import matplotlib.pyplot as plt
import time
def jqk():
    s = requests.Session() 
    header = {
            "Accept":"text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",

#            "Host":"zhugeio.com",

#            "Origin":"https://zhugeio.com", 

#            "Referer":"https://zhugeio.com/index/login.jsp",

            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36X-Requested-With:XMLHttpRequest"}

    s.headers.update(header)
    url="http://data.10jqka.com.cn/funds/ggzjl/field/ddlr/order/DESC/ajax/1/"
    url="http://data.10jqka.com.cn/funds/ggzjl/"
    
    ret = s.get(url)
    text= ret.text   
    print("text=",text)
    time.sleep(5)
    url="http://data.10jqka.com.cn/funds/ggzjl/field/ddlr/order/DESC/ajax/1/" 
    ret = s.get(url)
    text= ret.text   
    print("newtext=",text)
    print("ok")
    time.sleep(5)
    url="http://data.10jqka.com.cn/funds/ggzjl/field/ddlr/order/DESC/ajax/2/" 
    ret = s.get(url)
    text= ret.text   
    print("newtext=",text)
    print("ok")
    return text

if __name__ == '__main__':
      jqk()
      