import pickle

with open("123.txt", "ab+") as file:
    #a=5555
    #pickle.dump(a, file)
    file.seek(0)
    li = pickle.load(file)
    print("li: ", li)
    #file.truncate(0)
    #file.write("999")
    #file.write("77")
    
