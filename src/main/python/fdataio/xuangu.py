'''
Created on 2018年2月24日

@author: aadebuger
'''
import requests
import arrow
import time
import json
import yaml
import sys
import pandas as pd
import os
def PositionChanges():
    url='http://nuyd.eastmoney.com/EM_UBG_PositionChangesInterface/api/js'
    req  = {
        "style":"top",
#"js":"([(x)])",
"js":"[(x)]",

"ac":"normal",
"check":"itntcd",
"dtformat":"HH:mm:ss",
#"cb":"jQuery183031706676890241337_%s"%(arrow.now().timestamp*1000),
"cb":"",

"num":5,
"_":"1521006655062"
}
    ret = requests.get(url,params=req)
    print("test1")
    text= ret.text   
    print(text)
    data = json.loads(text)
    print(data)
    yaml.safe_dump(data, sys.stdout, allow_unicode=True, default_flow_style=False)
    return data
      
def xuangudashi():
    url='http://xuanguapi.eastmoney.com/Stock/JS.aspx'
    req  = {
        "type":"xgq",
"sty":"xgq",
"token":"eastmoney",
"c":"""[cz_gz01(1|1)][ggxg04]""",
"p":1,
"jn":"VHcgNRCt",
"ps":40,
"s":"ggxg04",
"st":-1,
"r":"1519439717494"
}
    ret = requests.get(url,params=req)
    print("test1")
#    ret = requests.get(url)
    print(ret)
    text= ret.text   
    print(text)
    data = json.loads(text)
    print("data",data['data'])    
    print("len",len(data['data']))
    
    return data['data']

if __name__ == '__main__':
     for i in range(1,1000):
         time.sleep(5)
         try:
             datav = PositionChanges()
             valuev = map(lambda item:item.split(","),datav)
             df= pd.DataFrame.from_records(valuev)
             print(df)
             if not os.path.isfile('alert.csv'):
                 df.to_csv('alert.csv',header ='code,dattime,name,acton,amount,status')
             else: # else it exists so append without writing the header
                 df.to_csv('alert.csv',mode = 'a',header=False)
         except Exception:
             pass