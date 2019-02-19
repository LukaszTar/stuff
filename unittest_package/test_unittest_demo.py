import pytest


@pytest.fixture()
def set_up_class():
    print('*' * 30)
    print('Setup class method')
    print('*' * 30)

class TestDemo():

    def test_method1(self, set_up_class):
        print('testing t1_method')

    def test_method2(self):
        print('testing t2_method')

