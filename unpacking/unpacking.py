def fun(a=0, b='null'):
    print("a= ", a, "b= ", b)

def fun_argv(**argv):
    print("argv: ", argv)
    
def fun_tuple(*argv_tuple):
    print("argv_tuple: ", argv_tuple)
    
d = {'a': 15, 'b': 'str'}

fun(**d)

fun_argv(**d)
fun_argv(x=100, y=77)

fun_argv(35, 'game')
fun_tuple(*d)
fun_tuple(35, 'game')