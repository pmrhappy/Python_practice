import unittest
import scheduling_result_validator #in the same folder or in pythonpath


class TestFunctions(unittest.TestCase):

    def test_add(self): # test_[function_name]
        excepted_result = 5
        self.assertEqual(excepted_result, scheduling_result_validator.add(3, 2))

if __name__ == '__main__':
    unittest.main(verbosity=2)