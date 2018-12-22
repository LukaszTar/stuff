class Set:
	def __init__(self, value = []):
		self.data = []
		self.concat(value)
	def intersect(self, other):
		res = []
		for x in self.data:
			if x in other:
				res.append(x)
		return Set(res)
	def union(self, other):
		res = self.data[:]
		for x in other:
			if not x in res:
				res.append(x)
		return Set(res)
	def concat(self, value):
		for x in value:
			if x not in self.data:
				self.data.append(x)
	def __len__(self):
		return len(self.data)
	def __getitem__(self, key):
		print('aaa')
		return self.data[key]
	def __and__(self, other):
		return self.intersect(other)
	def __or__(self, other):
		return self.union(other)
	def __repr__(self):
		return 'Zbiór:' + repr(self.data)

class MultiSet(Set):
	def intersect(self, *others):
		res = []
		for x in self.data:
			for other in others:
				if not x in other:
					break
			else:
				res.append(x)
		return Set(res)
	def union(self, *others):
		res = self.data[:]
		for other in others:
			for x in other:
				if not x in res:
					res.append(x)
		return Set(res)


x=Set([1,2,3,4,5])
y=MultiSet([4,5,6,7,8])

print(y.intersect([1,2,3,4,7], [7,8,9,0]))
print(y.union([1,2], [8,9]))





