'''
Created on 2018年2月24日

@author: aadebuger
'''
import requests
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
    pass