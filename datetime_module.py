'''
Created on Apr 12, 2016

@author: echglig
'''

import calendar

print(calendar.isleap(2000))

from datetime import date,time,datetime
one_day=date(2016,4,12)
print(one_day.isoformat())
print(one_day.day)
print(one_day.year)
print(one_day.month)

now=date.today()
print('today is: '+str(now))

noon=time(12,0,0)
print(noon)

print(noon.hour)
print(noon.minute)
print(noon.second)

someday=datetime(2016,4,12,14,46,15,6)
print(someday)

now=datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

noon=time(12,0,0)
today=date.today()
noon_today=datetime.combine(today,noon)
print(noon_today)

print(noon_today.date())
print(noon_today.time())



import time 
now=time.time()
print(now)
print(time.ctime(now))



now_str=str(date.today())
print(now)

import os
#if not os.path.exists('today.txt'):
#    fout=open('today.txt','wt')
#    fout.write(now)
#    fout.close()
if not os.path.exists('today.txt'):
    with open('today.txt','wt') as fout:
        print(now_str,file=fout)


if  os.path.exists('today.txt'):
    fin=open('today.txt','rt')
    today_string=fin.read()
    fin.close()
    
print(today_string)



print(os.listdir('.'))
print(os.listdir('..'))


import multiprocessing

def now(seconds):
    from datetime import datetime
    from time import sleep
    sleep(seconds)
    print('wait',seconds,'seconds, time is ',datetime.utcnow())
    
if __name__=='__main__':
        import random
        for n in range(3):
            seconds=random.random()
            proc=multiprocessing.process(target=now,args=(seconds,))
            proc.start
            
my_day=date(1988,12,26)
print(my_day)

print(my_day.weekday())
print(my_day.isoweekday())

from datetime import timedelta
part_day=my_day+timedelta(days=1000)
print(part_day)














