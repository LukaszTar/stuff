class Animal:
	def reply(self):
		self.speak()
	def speak(self):
		print('Animal')
class Mammal(Animal):
	def speak(self):
		print('Mammal')
class Cat(Mammal):
	def speak(self):
		print('Miau')
class Dog(Mammal):
	def speak(self):
		print('Hau')
class Primate(Mammal):
	def speak(self):
		print('Primate')
class Hacker(Primate):
	pass
#	def speak(self):
#		print('Witaj swiecie')
