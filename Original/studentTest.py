
from personTest import *
from manager import *

class Student:
	def __init__(self, name, surname):
		self.name = name
		self.surname = surname 













obj = Person("Bob Smith", "Engineer", 150000)

obj.giveRaise(.10)

print(obj.pay)

obj2 = Manager("Gary Hernandez", "Garbage Man", 150000)

obj2.giveRaise(.10)

print(obj2.pay)

print(obj2)
