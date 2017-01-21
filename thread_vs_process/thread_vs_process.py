from multiprocessing import Process
from threading import Thread
import time


def func(arg):
    time.sleep(3)
    return arg

def evoke_thread(function, **func_kwargs):
    thread = Thread(target=function, kwargs=func_kwargs)
    thread.start()

def evoke_process(function, *func_args):
    process = Process(target=function, args=func_args)
    process.start()

def test_thread(data):
    time_thread_start = time.time()
    evoke_thread(func, arg=data)
    time_thread_end = time.time()
    print("thread time:     ", time_thread_end - time_thread_start)

def test_process(data):    
    time_process_start = time.time()
    evoke_process(func, data)
    time_process_end = time.time()
    print("process time:    ", time_process_end - time_process_start)
    
if __name__ == '__main__':     
    data = [i for i in range(100)]
    test_thread(data)
    test_process(data)
    
    data = [i for i in range(10000000)]
    test_thread(data)
    test_process(data)

    