#encoding=utf-8
'''
Created on 2018年2月22日

@author: aadebuger
'''

from gsrl import zjlxall,zjlxquery
import numpy as  np
import influxrepo
def topstock():
         allv= zjlxall()

         codev=['600050','002594','600115','000400','600125','600876','000681'
                ,'600958','600679','601878','002038','002439','000858',"000868"]
         x = np.sort(codev, axis=-1, kind='mergesort')
         
         for code in x:
             position= zjlxquery(allv,code)   
             print(code+ " positon",position)  
             influxrepo.zjlxoutputb([{'code':code,'position':position}])
                         
                              

if __name__ == '__main__':
    topstock()