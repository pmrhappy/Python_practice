from multiprocessing import Pool
import multiprocessing
import time

def f((x,y)):
    #t=[0]
    
    t=[x]*30000
    
    return t

if __name__ == '__main__':
    t1=time.time()
    
    l2=range(150)
    l1=range(1,300,2)
    l3=zip(l1,l2)
    result=[]
    l4=[]
    # using multiprocessing #############
#    for j in range(0,3000):
#        l4=l4+l3
#    p = Pool(8)
#    result=p.map(f, l3)
#    p.close()
#    p.join()
    #------------------------------
    # for data divided into 4 parts
    
    
    
    ###############################
    
    # not use multiprocessing
    for j in range(0,300):
        for i in range(0,150,1):
            result.append([l1[i]]*3000)
    ###############################
        
    #print(result)
    f=open("result.txt","a")
    
    f.write(result.__str__())
    f.close()
    t2=time.time()
    print("time = %.3f" % (t2-t1))
    k=[range(1,5)]
    del result
    del l4
    #l3=l3+l3
    #print(l3)