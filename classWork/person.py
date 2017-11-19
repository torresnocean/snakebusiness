# Humberto Torres
# CISW 24 LAB
# 10/22/17
# Program 4

# basic Person with first name, last name

class Person:

	def __init__(self, first_name, last_name):		# Creating a constructor
		self.first_name = first_name         		# Creating attributes
		self.last_name = last_name

	def __str__(self):       						#Return a string
		return self.first_name + " " + self.last_name + "\nCourses:"

	def setFirstName(self, first_name):
		self.first_name = first_name

	def setLastName(self, last_name):
		self.last_name = last_name

	def getFirstName(self):
		return self.first_name

	def getLastName(self):
		return self.last_name

	def setNames(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

	def getNames(self):
		return self.first_name
		return self.last_name





# END OF CLASS





#fname = Person()
#lname = Person()

#if __name__ == '__main__':
															# $ python3 person.py
	#print("Constructed Person with defaults")				# constructed Person with defaults
	#print("NoFirstName NoLastName")							# NoFirstName NoLastName
	#print("first_name", fname.getFirstName())				# first_name NoFirstName
	#print("last_name", lname.getLastName())					# last_name NoLastName
	#print("set first name and last names")					# set first and last names
	#s1 = Person('Umber', 'T.')
	#print(s1)
	#print("constructed Person with explicit arguments")		# constructed Person with explicit arguments
	#s2 = Person('Tony', 'Montana')
	#print(s2)												# Tony Montana


#CLASS SOLUTIONS

	#p = Person()
	#print('constructed instance with defaults')
	#print(p)

	#print('first_name', p.getFirstName())
	#print('last_name', p.getLastName())

	#p.setFirstName('Vic')
	#p.setLastName('Zamora')
	#print(p)
	#print(p.getFirstName())

	#Explicit Arguments
	#p = Person('Santa', 'Claus')
	#print(p)



