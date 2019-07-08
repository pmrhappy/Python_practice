import pdb


class Animal(object):

    def __repr__(self):
        return "This is repr"

    def __str__(self):
        return "This is str"

animal = Animal()
pdb.set_trace()
# p animal will show repr
# print animal will show str
