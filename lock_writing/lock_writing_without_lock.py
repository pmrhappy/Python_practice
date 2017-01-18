from threading import Lock
from multiprocessing import Process

class File_Locker(object):
    file_lock = Lock()
    
    def write_file(self, func):
        #with type(self).file_lock:
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

def do_n_times(n, func):
    file_locker = File_Locker()
    for _n in range(n):
        file_locker.write_file(func)
    
if __name__ == '__main__':
    p1 = Process(target=do_n_times, args=(10, plus_1))
    p2 = Process(target=do_n_times, args=(10, multiply_2))
    p1.start()
    p2.start()
