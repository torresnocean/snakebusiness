# Humberto Torres
# CISW 24 LAB
# 10/22/17
# Program 4

class Person:

	def __init__(self, first_name = 'NoFirstName', last_name = 'NoLastName'):
		self.first_name = first_name
		self.last_name = last_name

	def setFirstName(self, first_name):
		self.first_name = first_name

	def setLastName(self, last_name):
		self.last_name = last_name

	def getFirstName(self):
		return self.first_name

	def getLastName(self):
		return self.last_name

	def __str__(self):
		return self.first_name + " " + self.last_name

fname = Person()
lname = Person()


if __name__ == '__main__':
															# $ python3 person.py
	print("Constructed Person with defaults")				# constructed Person with defaults
	print("NoFirstName NoLastName")							# NoFirstName NoLastName
	print("first_name", fname.getFirstName())				# first_name NoFirstName
	print("last_name", lname.getLastName())					# last_name NoLastName
	print("set first name and last names")					# set first and last names
	s1 = Person('Umber', 'T.')
	print(s1)
	print("constructed Person with explicit arguments")		# constructed Person with explicit arguments
	s2 = Person('Tony', 'Montana')
	print(s2)												# Tony Montana

