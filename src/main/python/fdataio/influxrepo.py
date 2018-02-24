'''
Created on 2018年2月22日

@author: aadebuger
'''
import arrow 
import influxResource

def zjlx(tags,position):
    


    newitem= {
        "measurement": "zjlx",
        "tags": tags ,
        "time": arrow.now().format("YYYY-MM-DD HH:mm:ss"),
        "fields": {
            "value": position,
 
        }
                    }
    retv =[]
    retv.append(newitem)
    return retv

def zjlxoutputb(listv):
    
     for item in listv:
         print(item)   
         newitem = zjlx({'code':item['code']},item['position'])

         influxResource.InfluxResourcePost(newitem)
         
if __name__ == '__main__':
    pass