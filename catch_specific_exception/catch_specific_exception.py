import traceback

if __name__ == '__main__':
    try:
        file = open("123.txt", "r") # FileNotFoundError
        f2 # NameError
    except FileNotFoundError as err:
        print("catch!! : ", err.__str__)