

def printA(element):
    print(element)
    return element*2

a=[7,8,9,10]


# result of map() is a iterator
for i in map(printA,a):
    pass
    
b=[printA(i*2) for i in a]
print(b)