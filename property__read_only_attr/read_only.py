'''
Runnable in Python 2.7
'''

class C1(object):
	def __init__(self, x):
		self.__x = x
	
	@property
	def x(self):
		return self.__x
		
		
if __name__=='__main__':
	c1 = C1(100)
	print("c1.x: ", c1.x)
	
	c1.x = 5 # AttributeError: can't set attribute
	