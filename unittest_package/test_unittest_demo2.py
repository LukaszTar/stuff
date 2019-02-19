import unittest
import selenium_test.logger


class UnitTestDemo2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('*' * 30)
        print('Setup class2 method')
        print('*' * 30)

    def test_method1(self):
        print('testing t1_method')

    def test_method2(self):
        print('testing t2_method')

    @classmethod
    def tearDownClass(cls):
        print('*' * 30)
        print('teardown cls method')
        print('*' * 30)


if __name__ == '__main__':
    unittest.main(verbosity=2)