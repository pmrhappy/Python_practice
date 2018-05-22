'''
Runnable in Python 2.7
'''

import copy

class C2(object): 
	data = None
	
	def get_value(self, value):
		return value

class C1(object):

	def __init__(self, data={'a':99, 'b':110}):
		
		C2.data = data
		for key in C2.data:
			print("key: ", key, " v:", C2.data[key])
			setattr(C2, key, property(lambda self: self))
		self.obj = C2()
	'''@property
	def obj(self):
		return copy.deepcopy(self.__obj)'''
		
		
if __name__=='__main__':
	c1 = C1()
	#print("c1.obj: ", c1.obj)
	
	#c1.obj['a'] = 5 # AttributeError: can't set attribute
	print("c1.obj.a: ", c1.obj.a)