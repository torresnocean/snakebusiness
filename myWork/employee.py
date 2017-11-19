from person import *

class Employee():

	def __init__(self, first, last):
		self.fname = first
		self.lname = last
		

newObj = Person("Joe", "Montana")
print(newObj.Name())

newObj5 = Person("Cindy", "Crawford")
print(newObj5.lastname)


newObj6 = Grandpa("John", "Smith")

result = newObj6.addTheseVals(2, 5)

print(result)

newObj6.printMyName("Jackson")


