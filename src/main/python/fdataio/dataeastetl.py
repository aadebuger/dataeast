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
scheduler = BackgroundScheduler()

def myfunc():
        print("hello ")
def my_job():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    topstock()
if __name__ == '__main__':
     
     scheduler.add_job(myfunc, 'interval', minutes=2, id='my_job_id')
     scheduler.add_job(my_job, 'interval', seconds=300)
     
     scheduler.start()
     sleep(500000)