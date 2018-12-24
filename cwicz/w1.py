class TraceBlock:
	def message(self,arg):
		print('wykonmanie', arg)
	def __enter__(self):
		print('rozpoczecie bloku with')
		return self
	def __exit__(self, exc_type, exc_value, exc_tb):
		if exc_type is None:
			print('normalen wyjscie\n')
		else:
			print('zgloszenie wyjatku', exc_type)
		#	return False

with TraceBlock() as action:
	action.message('test 1')
	print ('osiagniety')
with TraceBlock() as action:
	action.message('test 2')
	raise TypeError
	print('nie zostal osiagniety')
