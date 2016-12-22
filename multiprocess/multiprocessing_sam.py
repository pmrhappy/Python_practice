# -*- coding: utf-8 -*-
#import multiprocessing
from multiprocessing import Pool
from multiprocessing import freeze_support
import time,sys

def f(s):
    for i in range(1,86400,1):
        i=i+1
    
    return len(s) 

def mypool(myf, l,num_processors):
    pool = Pool(num_processors)
    #print(l)
    a = pool.map(f, l)
    pool.close()
    pool.join()
    return a

if __name__ == '__main__':
    tstart = time.time()
    #pool = Pool(8)
    
    freeze_support()
    l = [[i, i+1] for i in range(10000)]
    a = mypool(f, l,int(sys.argv[1]))
    #print(a)
    #print(l)            
    print('costs %.5f sec' %(time.time()-tstart))
