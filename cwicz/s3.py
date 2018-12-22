class Meta:
	def __getattr__(self, *args):
		return self.nazwa
	def __setattr__(self, *args):
		self.__dict__['nazwa'] = args[1]

if __name__ == '__main__':
	x=Meta()
	x.nazwa=5
	print(x.nazwa+3)
