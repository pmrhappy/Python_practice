class Foo(object):
    pass


class Bar(object):
    def __init__(self, obj):
        self.obj = obj


if __name__ == '__main__':
    foo = Foo()
    bar = Bar(foo)
    print("id(foo): ", id(foo))
    print("id(bar.obj): ", id(bar.obj))
    print("foo is bar.obj:", foo is bar.obj)
    del foo, bar.obj
    print("id(bar.obj): ", id(bar.obj))
