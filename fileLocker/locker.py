from lockfile import LockFile
import io,time

f=open("test.txt",'a')
lock = LockFile("./test.txt")


with lock:
    print lock.path, 'is locked!!'
    for i in range(1000000):
        print(i)
    
    print lock.path, 'is unlocked.'