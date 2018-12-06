import os
import hello


def hi():
    h = hello.Hello()
    print("hello.hi: ", h.hi())


if __name__ == '__main__':
    hi()
    os.rename('_hello.py', 'tmp')
    os.rename('hello.py', '_hello.py')
    os.rename('tmp', 'hello.py')
    
    
    print("------ reloading module")
    reload(hello)
    hi()
