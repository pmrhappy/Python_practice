import copy
def funA(num):
    num=5

def funA_1(list):
        list[0]=11


x=10
funA(x)
print("x= ",x)

#shallow copy
list=[0,1,2]
list2=list
funA_1(list)
#reassign => new list
list2=[7,7,7,7,7]
print("list", list)
print("list2", list2)

#deep copy
list3=copy.deepcopy(list)
list[1]=77
print("\nafter deepcopy in list3")
print("list", list)
print("list2", list2)
print("list3", list3)

#global variable
def funG():
        global g
        print("in funG: g=", g)
        g=100
g=1
funG()
print("g= ",g)

#copy with range operator
list4=[9,8,7,6,5]
#will copy with the 1st layer: [1,2,3,[4,5]] =>1,2,3 are copied and [4,5] is ref
list5=list4[:]
list5[2]=9999
print("list4=",list4)
print("list5=",list5)

