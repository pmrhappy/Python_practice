class Base(object):

    def __call__(self, *args, **kwargs):
        print("__call__")

    def __new__(self, *args, **kwargs):
        print("__new__")
        return super(Base, self).__new__(self, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        print("__init__")
        super(Base, self).__init__(self, *args, **kwargs)


if __name__ == '__main__':
    Base(1234)
    print("\n")
    Base(1234)(5678)
