import traceback
import pickle

if __name__ == '__main__':
    try:
        a=15
        file = open("new.txt", "ab+") # FileNotFoundError
        p = pickle.load(file) # EOFError: Ran out of input
        f2 # NameError
    except Exception as err:# FileNotFoundError as err:
        print("catch!! : ", type(err))
        print("a: ",a)
        if type(err) is EOFError:
            print("yes!!")
        else:
            print("no!!")