import os
from threading import Lock
from multiprocessing import Process

class File_Locker(object):    
    def write_file(self, func, lock):
        with lock:
            with open('01.txt', 'a+') as file:
                file.seek(0)
                try:
                    line = file.readlines()[-1]
                    num = int(line)
                except:
                    num = 1
                
                result = func(num)
                file.write(str(result)+"\n")

def plus_1(num):
    return num+1
    
def multiply_2(num):
    return num*2

def do_n_times(n, func, lock):
    file_locker = File_Locker()
    for _n in range(n):
        file_locker.write_file(func, lock)
    
if __name__ == '__main__':
    file_lock = Lock()
    p1 = Process(target=do_n_times, args=(10, plus_1, file_lock))
    p2 = Process(target=do_n_times, args=(10, multiply_2, file_lock))
    p1.start()
    p2.start()
