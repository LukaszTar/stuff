class Lunch:
	def __init__(self):
		Cname = Customer.__init__()
		Ename = Employee.__init__()	
	def order(self, foodName):
		Customer.placeOrder(foodName, Ename)
	def result(self):
		Cname.printFood()
	
class Customer(Lunch, Employee):
	def __init__(self):
	def placeOrder(self, foodName, employee):
		employee.takeOrder(foodName)
	def printFood(self):
		

class Employee(Lunch):
	def takeOrder(self, foodName):
		Food.__init__(foodName)
class Food:
	def __init__(self, name):
		self.food = name
		
