from multiprocessing import Process
from threading import Thread
import time


def func(arg):
    time.sleep(3)
    return arg

def evoke_procedure(Procedure, function, **func_kwargs):
    procedure = Procedure(target=function, kwargs=func_kwargs)
    procedure.start()

def test(data, Procedure, type):
    time_start = time.time()
    evoke_procedure(Procedure, func, arg=data)
    time_end = time.time()
    print(type, " time:     ", time_end - time_start)
    
if __name__ == '__main__':     
    data = [i for i in range(100)]
    test(data, Thread, 'Thread')
    test(data, Process, 'Process')

    data = [i for i in range(100000)]
    test(data, Thread, 'Thread')
    test(data, Process, 'Process')

    