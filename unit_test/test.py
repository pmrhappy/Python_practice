import unittest
import testPython as tp
import numpy as np

class TestStringMethods(unittest.TestCase):

	def test_upper(self):
		self.assertEqual('foo'.upper(), 'FOO')

	def test_isupper(self):
		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper())

	def test_split(self):
		s = 'hello world'
		self.assertEqual(s.split(), ['hello', 'world'])
		# check that s.split fails when the separator is not a string
		with self.assertRaises(TypeError):
			s.split(2)
   
	def test_train_module(self):
		x=np.array([1,2,3,4])
		y=np.array([1,2,3,4])
		result=tp.train_module(0,0,x,y)
		#result.
		#self.assertEqual(result,np.array([10,20,30,40]))
		self.assertEqual(result[1]/10,x[1])

if __name__ == '__main__':
    unittest.main()
 
def add(a,b):
	return a+b+1


