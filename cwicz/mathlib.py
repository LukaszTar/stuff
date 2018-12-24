class NumErr(Exception): pass
class DivZero(NumErr): pass
class Oflow(NumErr): pass
def func():
	raise DivZero()

