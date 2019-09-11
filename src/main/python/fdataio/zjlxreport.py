#encoding=utf-8
'''
Created on 2018年2月22日

@author: aadebuger
'''

import arrow
import influxResource
import yaml
import sys
import pandas as pd
def zjlxbycode(stockcode):
      nowdate = arrow.now().format("YYYY-MM-DD")
      sql1 = """select first(value),min(value),mean(value),last(value) from zjlx where code='%s' and time >'%s 09:30:00' and time <= '%s 15:00:00' """%(stockcode,nowdate,nowdate)
      
#      print("sql",sql1)
      retv = influxResource.InfluxResourceGet(sql1)   

      
      return retv
def zjlxbycode300s(stockcode,dategroup='300s'):
      nowdate = arrow.now().format("YYYY-MM-DD")
      nowtime = arrow.now().format("YYYY-MM-DD HH:mm:ss" )
      
      sql1 = """select first(value),min(value),mean(value),last(value) from zjlx where code='%s' and time >'%s 09:30:00' and time <= '%s' group by time(%s)"""%(stockcode,nowdate,nowtime,dategroup)
      
      print("sql",sql1)
      retv = influxResource.InfluxResourceGet(sql1)   
      return retv

def zjlxbycodeday(stockcode,dategroup='1d'):

     
      nowdate = arrow.now().replace(days=-21).format("YYYY-MM-DD")
      nowtime = arrow.now().format("YYYY-MM-DD HH:mm:ss" )
      
      sql1 = """select first(value),min(value),mean(value),last(value) from zjlx where code='%s' and time >'%s 09:30:00' and time <= '%s' group by time(%s)"""%(stockcode,nowdate,nowtime,dategroup)
      
      print("sql",sql1)
      retv = influxResource.InfluxResourceGet(sql1)   
      return retv
def zjlx(sql1,begin,end):

      print("sql",sql1)
      retv = influxResource.InfluxResourceGet(sql1)   
      
      return retv
   
if __name__ == '__main__':
#        retv = zjlx("select * from zjlx",arrow.now(),arrow.now())
#        print(retv)
#        retv = zjlx("select countx(value) from zjlx where code='600050' and time >'2018-03-12 09:30:00' group by time(1d) ",arrow.now(),arrow.now())

         sql ="""select * from zjlx where code='600050' and time >'2018-03-13 09:30:00'  """
         retv = zjlx(sql,arrow.now(),arrow.now())

#         yaml.safe_dump(retv, sys.stdout, allow_unicode=True, default_flow_style=False)

         
         sql ="""select count(value) from zjlx where code='600050' and time >'2018-03-13 09:30:00'  """
         retv = zjlx(sql,arrow.now(),arrow.now())

#         yaml.safe_dump(retv, sys.stdout, allow_unicode=True, default_flow_style=False)


         sql1 ="""select mean(value) from zjlx where code='600050' and time >'2018-03-13' group by time(1h)"""
         retv = zjlx(sql1,arrow.now(),arrow.now())

#         yaml.safe_dump(retv, sys.stdout, allow_unicode=True, default_flow_style=False)



         sql1 ="""select mean(value) from zjlx where code='600050' and time >'2018-03-13 09:30:00'  group by time(1h) """
         retv = zjlx(sql1,arrow.now(),arrow.now())

#         yaml.safe_dump(retv, sys.stdout, allow_unicode=True, default_flow_style=False)

         sql1 ="""select mean(value) from zjlx where code='600050' and  time >'2018-03-03 09:30:00' and time < '2018-03-13 16:00:00' group by time(1h) """
         retv = zjlx(sql1,arrow.now(),arrow.now())

#         yaml.safe_dump(retv, sys.stdout, allow_unicode=True, default_flow_style=False)

#        retv = zjlx("select * from zjlx where code='002594' ",arrow.now(),arrow.now())
#        print(retv)        
#        retv = zjlx("select * from zjlx where code='002439' ",arrow.now(),arrow.now())
#        print(retv) 
         retv = zjlxbycode("600050")     
         yaml.safe_dump(retv, sys.stdout, allow_unicode=True, default_flow_style=False)
         retv = zjlxbycode("002594")     
 #        yaml.safe_dump(retv, sys.stdout, allow_unicode=True, default_flow_style=False)
         codev=['600050','002594','600115','000400','600125','600876','000681'
                ,'600958','600679','601878','002038','002439','000858',"000868","600818","300017"]

         resultv=[]
         for code in codev:
             retv = zjlxbycode(code)     
#             yaml.safe_dump(retv, sys.stdout, allow_unicode=True, default_flow_style=False)
             result = retv[0]
             result['code']=code
             resultv.append(result)
         print(resultv)
         dv= pd.DataFrame.from_records(resultv)
         print(dv)
         print(dv.sort_values(by=['last']))
         codev=[sys.argv[1]]
         resultv=[]
         for code in codev:
             if sys.argv[2]=='1d':
                 retv = zjlxbycodeday(code,sys.argv[2]) 
             else:
                 retv = zjlxbycode300s(code,sys.argv[2])     
#             yaml.safe_dump(retv, sys.stdout, allow_unicode=True, default_flow_style=False)
             resultv.extend(retv)
         dv= pd.DataFrame.from_records(resultv)
         print(dv)
         
             
        