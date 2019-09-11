#encoding=utf-8
'''
Created on 2018年2月22日

@author: aadebuger
'''

from gsrl import zjlxall,zjlxquery,zjlxquerydict
import numpy as  np
import influxrepo
import yaml
import sys
import pandas as pd
import arrow
def todf():
        pass


def topstock():
         allv= zjlxall()

         yaml.safe_dump(allv[:10], sys.stdout, allow_unicode=True, default_flow_style=False)

  
         codev=['000725','600036','600050','002594','600115','000400','600125','600876','000681'
                ,'600958','600679','601878','002038','002439','000858',"000868","600818","300017"]
         x = np.sort(codev, axis=-1, kind='mergesort')
         
         keyv={}
         for code in x:
             position= zjlxquerydict(allv,code)   
             print(code+ " positon",position)  
             keyv[code]=position

#             influxrepo.zjlxoutputb([{'code':code,'position':position}])
         newkeyv = sorted(keyv.items(), key=lambda d: d[1]) 
#         print(newkeyv)   
         for item in newkeyv:
             print(item)
#         yaml.safe_dump(newkeyv, sys.stdout, allow_unicode=True, default_flow_style=False)

         position=0    
 
         for stock in allv:
                  influxrepo.zjlxoutputext([{'code': stock['k1'],'position':position,'time':stock['k15'],'stock':stock}])
                  position+=1              
         df = pd.DataFrame(allv)
         print(df[:10])            

if __name__ == '__main__':
    topstock()