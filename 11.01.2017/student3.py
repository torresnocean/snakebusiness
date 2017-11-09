from studentAgain import Student

import shelve
#Version 3
#Save all students in a shelve

roster = []
courses = []

cont = input("Create student? (y/n)")

while (cont == 'y'):
	first_name = input("first_name: ")
	last_name = input("last_name: ")
	# courses.append(input("First Course: "))
	# courses.append(input("Second Course: "))
	print("Creating a student...")
	s = Student(first_name, last_name)
	print("Student enrolled")
	roster.append(s)
	cont = input("create another student? (y/n)")

#save all students in a roster in shevle database

db = shelve.open('testData')

for s in roster:
	db[s.getLastName()] = s

db.close()





