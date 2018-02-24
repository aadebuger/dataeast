'''
Created on 2018年2月22日

@author: aadebuger
'''
import pandas as pd

import arrow
from gsrl import zjlxall,zjlxquery
def zjlx_datasets():
        allitem= zjlxall(70)
        for item in allitem:
            print(item)
            subitemv = item.split(",")
        newallitem  = map(lambda item:item.split(","),allitem)
        return pd.DataFrame.from_records(newallitem)
        
               
if __name__ == '__main__':
      datav = zjlx_datasets()
      print("zjlx",datav)
      datav.to_csv("zjlx"+ arrow.now().format("YYYYMMDD")+".csv")