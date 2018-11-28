# for Python 2.7 (Python < 3.3)
from unittest import TestCase
from mock import patch

import mock_module_1
from mock_module_2 import C1


class TestMockInner(TestCase):

    # mock for function
    def test_mock_normal_function(self):
        with patch('mock_module_1.get_99') as get_99:
            get_99.return_value = 9999

            print("get_99: {}".format(get_99()))

    # mock for class method
    def test_mock_inner(self):
        with patch.object(C1, 'get_value') as get_value:
            get_value.return_value = 'mocked'
            
            print("c1.get_value: ", mock_module_1.get_c_value())
            c1 = C1()
            print("c1.get_value (current)", c1.get_value())
            print("c1.get_500: ", c1.get_500())

