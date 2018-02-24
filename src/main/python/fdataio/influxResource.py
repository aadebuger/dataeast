#encoding=utf-8
'''
Created on 2018年2月22日

@author: aadebuger
'''

from influxdb import InfluxDBClient

import os

def getIp():
    return os.environ.get('influxdb',"localhost")

def InfluxResource():
    client = InfluxDBClient(getIp(), 8086, 'root', 'root', 'dataeast')
    client.create_database('dataeast')
        
def InfluxResourcePost(json_body):
    
    client = InfluxDBClient(getIp(), 8086, 'root', 'root', 'dataeast')
    
    client.write_points(json_body)
def InfluxResourceGet( sql):
    client = InfluxDBClient(getIp(), 8086, 'root', 'root', 'dataeast')
    
    result = client.query(sql)

    retv=[]
    for item in result.get_points():
        retv.append(item)
    return retv
if __name__ == '__main__':
    InfluxResource()
