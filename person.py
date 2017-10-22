# Daniel Ocean 
# CISW 24 LAB
# 10/15/17
# Program 4 

class Person:

	first_name = None
	last_name = None

	def __init__(self, first='NoFirstName', last='NoLastName'):
		self.first_name = first
		self.last_name = last

	def setFirstName(self, first):
		self.first_name = first

	def setLastName(self, last):
		self.last_name = last

	def getFirstName(self):
		return self.first_name

	def getLastName(self):
		return self.last_name

	# def __repr__(self):
	# 	return '[Person: %s %s]' % (self.first_name, self.last_name)

	def __str__(self):
		return "[Person: " + self.first_name + " " + self.last_name + "]"


#INSTRUCTIONS WERE NOT CLEAR

# constructed Person with defaults NoFirstName NoLastName
# first_name NoFirstName
# last_name NoLastName
# set first and last names
# James Holbert
# constructed Person with explicit arguments Johnny Bravo


if __name__ == '__main__':
	obj = Person()						# constructed Person with defaults NoFirstName NoLastName
	print(obj)
	print(obj.getFirstName())			# first_name NoFirstName
	print(obj.getLastName())			# last_name NoLastName
	obj2 = Person("Johnny", "Bravo")	# constructed Person with explicit arguments Johnny Bravo
	print(obj2)

print("----------------------------------PERSON CLASS ABOVE THIS LINE--------------------------------")




	



	