from multiprocessing import Pool
import time

def f((x,y)):
    #t=[0]
    
    t=[x]*1000
    
    return t

if __name__ == '__main__':
    t1=time.time()
    
    l2=range(150)
    l1=range(1,300,2)
    l3=zip(l1,l2)
    result=[]
    # using multiprocessing
    #p = Pool(8)
    #result=p.map(f, l3)
    ###############################
    
    # not use multiprocessing
    for i in range(0,150,1):
        result.append([l1[i]]*1000)
    ###############################
        
    print(result)
    t2=time.time()
    print("time = %.3f" % (t2-t1))
    k=[range(1,5)]
    #l3=l3+l3
    #print(l3)