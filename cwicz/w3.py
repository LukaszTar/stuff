class MyError(Exception): pass

def oops():
	raise IndexError

def fun():
	try:
		oops()
	except (MyError, Exception) as E:
		print('indexError',E.__class__)

if __name__=='__main__':
	fun()
