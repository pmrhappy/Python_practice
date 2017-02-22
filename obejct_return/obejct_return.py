
def append_arr(obj):
    print("id(arr) in func:", id(arr))
    obj.append(10)
    return obj

if __name__ == '__main__':
    arr = [1,2,3,4,5,6]
    print("arr before: \t", arr)
    print("id(arr): \t", id(arr))
    
    append_arr(arr)
    print("arr after: \t", arr)
    print("id(arr): \t", id(arr))
    
    arr = append_arr(arr)
    print("arr after: \t", arr)
    print("id(arr): \t", id(arr))