import sys, w3, traceback
def safe(func, *args):
	try:
		func()
	except:
		print(sys.exc_info()[0], traceback.print_exc())
safe(w3.oops)
	
