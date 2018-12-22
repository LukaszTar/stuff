class Scene:
	def __init__(self):
		self.cus = Customer()
		self.cle = Clerk()
		self.par = Parrot()
	def action(self):
		self.cus.speak()
		self.cle.speak()
		self.par.speak()
class Action():
	def speak(self):
		print('{}:{}'.format(self.name, self.line()))
class Customer(Action):
	name = 'Customer'
	def line(self):
		return('"To juz ekspapuga"')
class Clerk(Action):
	name = 'Clerk'
	def line(self):
		return('"nie, wcale nie"')
class Parrot(Action):
	name = 'Parrot'
	def line(self):
		return(None)
