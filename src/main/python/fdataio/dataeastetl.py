#encoding=utf-8
'''
Created on 2018年2月22日

@author: aadebuger
'''
from apscheduler.schedulers.background import BackgroundScheduler
import sched
from time import ctime,sleep 
import time
from zjlxtop import topstock
import arrow
def isBusiness():
        nowtime  = arrow.now()
        nowm = nowtime.hour*60+nowtime.minute
        m930 = 9*60+30
        m1130 = 11*60+30
        m1300 = 13*60+0;
        m1500  = 15*60;
        
        if  nowm<m1130 and nowm>=m930:
            return True
        if  nowm<m1500 and nowm>=m1300:
            return True        
        return False
    
scheduler = BackgroundScheduler()

def myfunc():
        print("hello ")
def my_job():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
#    if isBusiness():
    topstock()
if __name__ == '__main__':
     
     scheduler.add_job(myfunc, 'interval', minutes=2, id='my_job_id')
     scheduler.add_job(my_job, 'interval', seconds=60)
     
     scheduler.start()
     sleep(500000)