class A():
    def __init__(self, var):
        print("This is a, var=", var)

class B(A):
    def __init__(self, var):
        super().__init__(var)
        print("This is b, var=", var)

if __name__=='__main__':
    b=B(100)