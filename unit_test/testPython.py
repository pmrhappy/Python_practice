import numpy as np
import os

def helloWorld(data): 
    print "test 2: print in py module " + data
    return 1.0
	
	
def add_test(x,y):
    print "test3: add operation in python try2:" ,  x+y
    import numpy as np
    array = np.array({1,2,3})
    print array
    return x+y


def avm_interface(mode,route,x,y):
    print "\n\n input in python================"
    print "route = " , route
    print x.shape
    print y.shape
    print type(x)
    print "x input = \n ",x
    print "y input = \n ",y
    
    data_size=x.shape[0]
    print data_size
    print np.ones(data_size,dtype='float64') #fail
    #print test1   
   
    ack=int(1)
    return 0.5*y ,ack


def train_module(mode, route,x,y):
    #import numpy test
    try:
        np
        print "\n numpy import scucess \n"
    except:
        print "\n numpy import fail \n"
    print "\n input in python training module: \n"
    print "Mode = " , mode
    print "route = " , route
    #print x.shape
    #print y.shape
    #print type(x)
    print "x input = \n ",x
    print "y input = \n ",y
    ack=int(1)
    result=np.array(x*10,dtype='float64')
    print "train_result= \n",result
    print "\n output in python training module: \n"
    print "ACK=",ack
    return result
    
def test_module(route,x):
    try:
        np
        print "\n numpy import scucess \n"
    except:
        print "\n numpy import fail \n"
    print "\n input in python testing module: \n"
    print "route = " , route
    print "x input = \n ",x
    #data_size=x.shape[0] #[each*10 for each in x]
    result=[]
    for i in range(0,len(x)):
			result.append(x[i][0])
    print "test_result= \n",result
    y = np.array(result,dtype='float64')
    #y = np.ones(data_size,dtype='float64')
    print "\n output in python testing module: \n"
    print "y output = \n ",y
    return y   
