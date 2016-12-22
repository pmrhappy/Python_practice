import unittest
from feature_selection.test_feature_select_filter import FeatureSelectFilterTestCase

suite=unittest.TestSuite()
tc=FeatureSelectFilterTestCase("test_transform_1")
#suite.addTest(tc)
for method_name in dir(tc) :
    if callable(getattr(tc, method_name)) and "test_trans" in method_name:
        print(method_name)
        specified_case=FeatureSelectFilterTestCase(method_name)
        suite.addTest(specified_case)

unittest.TextTestRunner().run(suite)