# -*- coding: utf-8 -*-
"""
Created on Thu May 14 09:55:08 2015

@author: A30294

"""
from operator import add
import time

def fun(x,y):
    a=x[0]+y[0]
    b=x[1]+y[1]
    
    return a,b

time_start=time.time()

list=[(1,"a"),(2,"b"),(3,"c"),(5,"j")]

#p=map(lambda x : x*x,list)
r=reduce(fun ,list)
print list
for each in range(0,10000):
    i=50


       
         
time_finish=time.time()
time_execution=time_finish-time_start
print('All finish, time=%f' % time_execution )
