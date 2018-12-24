def action2():
	print(1+[])
def action1():
	try:
		action2()
	except TypeError:
		print('wewnwtrz')

try:
	action1()
except TypeError:
	print('zewn')
finally:
	print('koniec')
