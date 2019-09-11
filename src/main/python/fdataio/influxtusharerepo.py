'''
Created on 2018年3月16日

@author: aadebuger
'''

import influxResource
def zjlxext(item):
    

    tags = {}
    valuev = item
    newitem= {
        "measurement": "stock",
        "tags": tags ,
        "time": item.index,
        "fields":  valuev
                    }



def zjlxoutputext(listv):
    
         pointv =map(lambda item: stockext(item),listv)
         
         influxResource.InfluxResourcePost(point) 
         
if __name__ == '__main__':
    pass