import six


class Meta(type):

    def __call__(cls, *args, **kwargs):
        print("__call__")
        return super(Meta, cls).__call__(cls, *args, **kwargs)

    def __new__(cls, clsname, supercls, attrdict):
        print("Meta __new__")
        attrdict['magic'] = attrdict['func']
        attrdict.pop('func')
        obj = super(Meta, cls).__new__(cls, clsname, supercls, attrdict)
        return obj


class Base(six.with_metaclass(Meta, object)):

    def __new__(self, *args, **kwargs):
        print("__new__")
        return super(Base, self).__new__(self, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        print("__init__")
        super(Base, self).__init__(self, *args, **kwargs)

    def func(self, words='normal'):
        print("func: ", words)


if __name__ == '__main__':
    base = Base(1234)
    base.magic('magic')  # callable
    base.func()  # not found because it's been remove by Meta.__new__
