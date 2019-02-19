import unittest
from unittest_package.unittest_demo import UnitTestDemo
from unittest_package.unittest_demo2 import UnitTestDemo2

tc1 = unittest.TestLoader().loadTestsFromTestCase(UnitTestDemo)
tc2 = unittest.TestLoader().loadTestsFromTestCase(UnitTestDemo2)

test_suite = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner().run(test_suite)
