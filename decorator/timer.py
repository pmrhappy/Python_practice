import time

def timer(func):
    def wrapper(*args, **kwargs):
        t_start = time.time()
        result = func(*args, **kwargs)
        print(func.__name__, ": ", time.time()-t_start)
        return result
    return wrapper
    
@timer
def f1():
    time.sleep(3)
    return 0

if __name__ == '__main__':
    f1()