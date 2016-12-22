

def f1(*args):
    print(args)
    
def f2(**kwargs):
    print(kwargs)

def f3(arg1,arg2):
    print(arg1, arg2)
    
f1(1,2,3,4,5,6)
f2(a=15, b=88, c="something")
l = [100, 25]
f3(*l)
d = {"arg1":77, "arg2":88}
f3(*d)