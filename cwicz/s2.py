class Mylist():
	def __init__(self, lista):
		self.lista = lista[:]
	def __add__(self, other):
		return Mylist(self.lista + other)
	def sort(self):
		self.lista.sort()
		return Mylist(self.lista)
	def __getitem__(self, index):
		return self.lista[index]
	def __mul__(self, other):
		return (self.lista * other)
	def __slice__(self, low, high):
		return (self.lista[low:high])
	def __getattr__(self, name):
		print('tutaj')
	def __str__(self):
		return (str(self.lista))
if __name__ == '__main__':
	listajakas = [1,2,3,4]
	x = Mylist(listajakas)
	print(x)
	x.sort()
	x.list
	y = x + ['ua']
	z = x * 2
	x.lista
	listajakas[1] = 'a'
	print(x)
	print(y, z, x[1], x[1:3])
