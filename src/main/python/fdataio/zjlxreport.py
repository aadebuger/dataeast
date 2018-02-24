#encoding=utf-8
'''
Created on 2018年2月22日

@author: aadebuger
'''

import arrow
import influxResource
def zjlx(sql,begin,end):
      sql1 = sql 
      print("sql1",sql1)
      retv = influxResource.InfluxResourceGet(sql1)   
      
      return retv
if __name__ == '__main__':
        retv = zjlx("select * from zjlx",arrow.now(),arrow.now())
        print(retv)
        retv = zjlx("select * from zjlx where code='600050' ",arrow.now(),arrow.now())
        print(retv)
        retv = zjlx("select * from zjlx where code='002594' ",arrow.now(),arrow.now())
        print(retv)        