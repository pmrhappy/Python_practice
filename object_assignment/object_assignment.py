import copy
from copy import deepcopy

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def fun(x):
    print("This is in fun(), id(x):", id(x))

def fun2(x):
    x=-1
    
a = ListNode(15)
print(id(a))
b = deepcopy(a)
print(id(b))
fun(b)
c = a
d = c
d.val = 99
print("a.val: ", a.val)
i=15
j=deepcopy(i)
j=12
print("id(i): ",id(i))
print("id(j): ",id(j))
i=j
i=20
print("j: ", j, "id(j): ", id(j))