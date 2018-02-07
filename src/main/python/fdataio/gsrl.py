#encoding=utf-8
'''
Created on 2018年1月29日

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
data1="""["0#1#2018-01-29 15:58:53#【人民币汇率攀升 多家公司回应对业务影响情况】中金公司研报显示，人民币过去12个月兑美元的累积升幅为2008年以来最高。预计人民币汇率将继续走强。英科医疗称将通过提高产品售价和对冲手段来减轻影响；光莆股份称，受汇率波动2017年公司照明出口的盈利受一定影响，正逐步与大客户洽谈汇率捆绑等；沙隆达A称，如人民币对美元升值，则会对公司人民币口径财报数据有负面影响。（新浪）#####0###20180129155853485100","0#1#2018-01-29 15:48:11#据外媒：安哥拉据称将在3月出口48船原油。#####0###20180129154811621100","0#1#2018-01-29 15:45:10#<b>香港特别行政区政府：加密货币存在高度投机性与波动性。</b>#####0###20180129154510310100","0#1#2018-01-29 15:44:04#<b>据外媒：香港特别行政区政府据称将开始对加密货币、ICO的投资者开展教育项目。</b>#####0###20180129154404489100","0#1#2018-01-29 15:35:44#<b>【报告】保监会修订发布保险资金运用管理办法新闻发布会</b>###1517211334_lite.png##0###20180129153544022100","0#1#2018-01-29 15:35:40#【股市资金流向图】今日沪深两市主力资金净流出367.69亿元，占比6.66%；小单资金净流入291.81亿元，占比5.28%。###1517211227_lite.png##0###20180129153540035100","0#1#2018-01-29 15:31:00#【交易所收盘】<br />上海黄金交易所黄金T+D 1月29日（周一）午盘收盘下跌0.58%报275.85元/克；</br >上海黄金交易所白银T+D 1月29日（周一）午盘收盘下跌0.53%报3786.00元/千克。#####0###20180129153100252100","0#1#2018-01-29 15:30:00#日本首相安倍晋三：希望听到来自美国总统特朗普对TPP的想法。#####0###20180129153000048100","0#1#2018-01-29 15:29:10#<b>日本首相安倍晋三：乐见美国总统特朗普发表对TPP的评论。</b>#####0###20180129152910378100","0#1#2018-01-29 15:28:39#印度财政部报告：商品与服务税（GST）税收收入的强劲程度高于预期。#####0###20180129152839102100","0#1#2018-01-29 15:27:09#【外媒：韩国将就扩大贸易协议与中国商谈】据凤凰新闻援引外媒报道，韩国财政部长金东兖在一个政府会议上表示，韩国将尽早与中国举行会晤，寻求扩大一项已适用两年的自由贸易协议，以扩大服务和投资领域的覆盖范围。韩国财政部在声明中公布了金东兖的评论。韩国希望旅游、文化、医疗和法律等领域的企业更积极地进入中国市场。#####0###20180129152709690100","0#0#2018-01-29 15:22:32#【行情】德国5年期国债收益率自2015年12月来首次触及0%。#####0###20180129152232445100","0#1#2018-01-29 15:20:47#【科技部：2025年国家要布局不超过30家农业高新技术产业示范区】国务院新闻办公室29日举行新闻发布会，科技部副部长徐南平表示，现在已经有两个示范区，计划到2025年，国家要布局不超过30家农业高新技术产业示范区，探索农业创新驱动发展路径，显著提高示范区土地产出率、劳动生产率和绿色和平发展。（证券时报）#####0###20180129152047647100","0#1#2018-01-29 15:18:05#<a href=\"http://app.jin10.com/\" target=\"_blank\"><img src=\"https://image.jin10.com/1516772845.gif\" width=\"754\" height=\"120\" /></a>#####0###20180129151805355100","0#1#2018-01-29 15:17:45#印度财政部报告：若通胀不与当前利率水平背离，预计通胀将会保持平稳。#####0###20180129151745537100","0#1#2018-01-29 15:16:46#印度财政部报告：预计印度2017/2018财年CPI为3.7%。#####0###20180129151646706100","0#1#2018-01-29 15:15:29#以色列总理内塔尼亚胡：将会与俄罗斯总统普京讨论伊朗导弹项目问题。#####0###20180129151529033100","0#1#2018-01-29 15:13:28#【权重股调整 指数集体下挫】周一，沪指上午盘中创阶段新高，随后放量跳水，权重股大幅回调，午后加速调整；深成指弱势调整，下跌近2%。截至收盘，沪指下跌0.99%，深成指下跌1.772%，创业板指下跌0.94%。盘面上，煤炭、钢铁微涨，保险、酿酒、半导体等大幅走低。上证成交2854.17亿，深成指成交2699.42亿，合计成交5553.59亿元人民币。#####0###20180129151328470100","0#1#2018-01-29 15:10:28#挪威国家石油公司：周一挪威天然气气田产量减少560万立方米/日。#####0###20180129151028757100","0#1#2018-01-29 15:07:10#<b>日本内阁官房长官菅义伟：观察货币市场走向是很重要的。</b>#####0###20180129150710150100","0#1#2018-01-29 15:06:43#印度财政部报告：预计印度将在明年重新成为经济增速最快的经济体。#####0###20180129150643662100","0#1#2018-01-29 15:05:23#<b>印度财政部报告：沙特阿美上市的可能性将进一步推动油价走高。</b>#####0###20180129150523856100","0#1#2018-01-29 15:03:40#印度财政部报告：周期性情况将降低2017/2018财年的税收及非税收收入。#####0###20180129150340725100","0#1#2018-01-29 15:02:00#【股市收盘】<br />中国上证综指1月29日（周一）收盘下跌35.13点，跌幅：0.99%，报3523.00点；<br />中国深证成指1月29日（周一）收盘下跌205.10点，跌幅：1.77%，报11352.72点；<br />中国沪深300指数1月29日（周一）收盘下跌79.28点，跌幅：1.81%，报4302.02点；<br />中国创业板指数1月29日（周一）收盘下跌17.03点，跌幅：0.94%，报1799.77点。#####0###20180129150200958100","0#1#2018-01-29 15:01:38#泰国财政部：预计2017年泰国GDP增速为4.0%（10月预期为3.8%）；预计2018年GDP增速为4.2%（10月预期为3.8%）。#####0###20180129150138154100","1#15:00#德国12月进口物价指数年率#2.7%#1%#1.1%#2#利多#2018-01-29 15:00:35#德国##245296#20180129150035168100#0","1#15:00#德国12月进口物价指数月率#0.8%#0.2%#0.3%#2#利多#2018-01-29 15:00:33#德国##245295#20180129150033426100#0","0#1#2018-01-29 15:00:26#印度财政部报告：经济管理将会是来年遇到的挑战。#####0###20180129150026315100","0#1#2018-01-29 14:59:56#<b>印度财政部报告：预计2017/2018财年GDP增速为6.75%。</b>#####0###20180129145956211100","0#1#2018-01-29 14:59:33#印度财政部报告：经济增速上行的最大动力来源于出口业。#####0###20180129145933553100"]"""

def getText(datestr):
#    url="""http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx?type=GSRL&sty=GSRL&stat=21&fd=2018-01-29&p=1&ps=50&js=({pages:(pc),data:[(x)]})&cb=callback&callback=callback&_=1517208500467"""
    url="""http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx?type=GSRL&sty=GSRL&stat=21&fd=%s&p=1&ps=50&js=({pages:(pc),data:[(x)]})&cb=callback&callback=callback&_=1517208500467"""%(datestr)
    
    ret = requests.get(url)
    text= ret.text
    print("text",text[9:-1])
    return text[9:-1]
def parseText(text):
#error
#        ll_patched = re.sub('([{,:])(\w+)([},:])','\\1\"\\2\"\\3',text)
# var fixedJSON = crappyJSON.replace(/(['"])?([a-zA-Z0-9_]+)(['"])?:/g, '"$2": ');

        ll_patched = re.sub(r'(?<={|,)([a-zA-Z][a-zA-Z0-9]*)(?=:)', r'"\1"', text)

        print("ll_patched",ll_patched)
        data = json.loads(ll_patched)
        print("pages",data['pages'])
        

        print("data",data)
        yaml.safe_dump(data['data'], sys.stdout, allow_unicode=True, default_flow_style=False)
        print("len",len(data['data']))
        return data['data']

def getData(begindate,enddate):
    url="""http://data.eastmoney.com/DataCenter_V3/cjrl/getData.ashx?&pagesize=50&page=1&js=var%20UTCcPXRn&param=&sortRule=1&sortType=ConferenceDate&code=&startDateTime="""+"""%s&endDateTime=2018-02-27&Type=all&rt=50573725"""%(begindate)
    ret = requests.get(url)
    text= ret.text
    print("text",text[len('var UTCcPXRn='):])
    return text[len('var UTCcPXRn='):]
def parseData(jsondata):
        data = json.loads(jsondata)
        print("data",data)
        yaml.safe_dump(data, sys.stdout, allow_unicode=True, default_flow_style=False)
          

def getJs():
    url="""https://www.jin10.com/newest_1.js?rnd=0.004516075425650912 """
    ret = requests.get(url)
    text= ret.text
    print("text",text[len("var newest = "):])
    return text[len("var newest = "):]

def getDataJs(url):
    print("getDataJs")
    url1="""http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx/JS.aspx?type=ct&st=(BalFlowMain)&sr=-1&p=1&ps=50&js=var%20QNkqerGy={pages:(pc),date:%222014-10-22%22,data:[(x)]}&token=894050c76af8597a853f5b408b759f5d&cmd=C._AB&sty=DCFFITA&rt=50576214"""
    url="http://datainterface.eastmoney.com//EM_DataCenter/js.aspx"
    req={"type":"SR",
"sty":"GGSR",
#"js":"""var GOwNelEn={"data":[(x)],"pages":"(pc)","update":"(ud)","count":"(count)"}""",
"js":"""{"data":[(x)],"pages":"(pc)","update":"(ud)","count":"(count)"}""",
"ps":50,
"p":2,
"mkt":0,
"stat":0,
"cmd":2,
"code":None,
"rt":50576413
        }
    
    ret = requests.get(url,params=req)
    text= ret.text   
    print(text)
    return text

def parseJs(jsdata):
        data = json.loads(jsdata)
        print("data",data)
  

#http://data.eastmoney.com/zjlx/detail.html
def zjlx(page):
#http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx/JS.aspx
    url="http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx/JS.aspx"
#    url="""http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx/JS.aspx?type=ct&st=(BalFlowMain)&sr=-1&p=1&ps=50&js=var%20JsYLCfbz={pages:(pc),date:%222014-10-22%22,data:[(x)]}&token=894050c76af8597a853f5b408b759f5d&cmd=C._AB&sty=DCFFITA&rt=50596597"""
    req = {
            "type":"ct",
"st":"(BalFlowMain)",
"sr":"-1",
"p":page,
"ps":"50",
#"js":"""var JsYLCfbz={pages:(pc),date:"2014-10-22",data:[(x)]}""",
"js":"""{pages:(pc),date:"2014-10-22",data:[(x)]}""",

"token":"894050c76af8597a853f5b408b759f5d",
"cmd":"C._AB",
"sty":"DCFFITA",
"rt":"50596597"
}
    ret = requests.get(url,params=req)
    print("test1")
#    ret = requests.get(url)
    print(ret)
    text= ret.text   
    print(text)
    return text

def appendItem(alldata,item):
        print("item",item)
        print("alldata",alldata)
        alldata.extend(item)
        return alldata
def f(x, y):
    return x + y
def zjlxall():
        pagev = [] 
        for page in range(1,3):
            text =zjlx(page)
            data=parseText(text)
            pagev.append(data)
        dataall=[]

        reduce(appendItem,pagev,[])
        return dataall
def zjlxsingle():
#http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd=6000501&sty=CTBFTA&st=z&sr=&p=&ps=&cb=&js=var%20tab_data=({data:[(x)]})&token=70f12f2f4f091e459a279469fe49eca5
    url='http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx'
    req = {
        "type":"CT",
"cmd":"6000501",
"sty":"CTBFTA",
"st":"z",
"sr":None,

"p":None,
"ps":None,
"cb":None,
##"js":"var tab_data=({data:[(x)]})",
"js":"""{"data":[(x)]}""",

"token":"70f12f2f4f091e459a279469fe49eca5"
}
    ret = requests.get(url,params=req)
    print("test1")
#    ret = requests.get(url)
    print(ret)
    text= ret.text   
    print(text)
    return text

def zjlxh():
#http://ff.eastmoney.com//EM_CapitalFlowInterface/api/js?type=hff&rtntype=2&js=({data:[(x)]})&cb=var%20aff_data=&check=TMLBMSPROCR&acces_token=1942f5da9b46b069953c873404aad4b5&id=6000501&_=1517911403431

    url='http://ff.eastmoney.com//EM_CapitalFlowInterface/api/js'
    req = {
        "type":"hff",
"rtntype":2,
"js":"""{"data":[(x)]}""",
#"cb":"var aff_data=",
"cb":"",

"check":"TMLBMSPROCR",
"acces_token":"1942f5da9b46b069953c873404aad4b5",
"id":"6000501",
"_":"1517911403431"
}
    ret = requests.get(url,params=req)
    print("test1")
#    ret = requests.get(url)
    print(ret)
    text= ret.text   
    print(text)
    data = json.loads(text)
    print("data",data['data'])
            
    return data['data']


def  gsrl():

#http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx?type=GSRL&sty=GSRL&stat=21&fd=2018-02-07&p=1&ps=50&js=({pages:(pc),data:[(x)]})&cb=callback&callback=callback&_=1517983109557

    url='http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx'
    req = {
        "type":"GSRL",
"sty":"GSRL",
"stat":21,
"fd":"2018-02-07",
"p":1,
"ps":50,
"cb":"",
##"js":"var tab_data=({data:[(x)]})",
##"js":"""({pages:(pc),data:[(x)]})""",
"js":"""{"pages":(pc),"data":[(x)]}""",
"callback":"callback",
"_":"1517983109557"
}
    print("gsrl")
    ret = requests.get(url,params=req)
    text= ret.text   
    print(text)
    data = json.loads(text)
    print("data",data['data'])    
    print("test2")

    return data['data']
def  gsrl2():

#http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx?type=GSRL&sty=GSRL&stat=21&fd=2018-02-07&p=1&ps=50&js=({pages:(pc),data:[(x)]})&cb=callback&callback=callback&_=1517983109557

    url='http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx'
    req = {
        "type":"GSRL",
"sty":"GSRL",
"stat":23,
"fd":"2018-02-07",
"sr":2,
"p":1,
"ps":50,
"cb":"",
##"js":"var tab_data=({data:[(x)]})",
##"js":"""({pages:(pc),data:[(x)]})""",
"js":"""{"pages":(pc),"data":[(x)]}""",
"callback":"callback",
"_":"1517983109557"
}
    print("gsrl")
    ret = requests.get(url,params=req)
    text= ret.text   
    print(text)
    data = json.loads(text)
    print("data",data['data'])    
    print("test2")
    return data['data']
     
def plot_curve1(data,title):
    plt.figure(figsize=(15,5))
    plt.title(title)
    plt.plot(data,'o-')
    plt.show()
        
if __name__ == '__main__':
     text=getText('2018-01-29')
     parseText(text)
     jsondata=getData('2018-01-29','2018-01-29')
     parseData(jsondata)
#     jsdata=getJs()
#     parseJs(data1)
     getDataJs("")  
     print("zjlx")
     text=zjlx(1) 
     parseText(text)
     zjlxall()
     zjlxsingle()
     print("zjlxh")
     datav= zjlxh()
     for item in datav[0]:
        print(item)
     newdatav = list(map(lambda item:item.split(","),datav[0]))
     print("newdata=",newdatav)
     table = newdatav
     df = pd.DataFrame(table)
     print("df",df)
     df.set_index(0)
     print("df0",df.iloc[:,1][:-20])
     print("df0",df.iloc[:,0][-10:])
     yvalues = list(map(lambda item:float(item),df.iloc[:,1][-15:]))
     print("yvalues",yvalues)
     plt.plot(df.iloc[:,0][-15:], yvalues,'ro')
     plt.show()
     