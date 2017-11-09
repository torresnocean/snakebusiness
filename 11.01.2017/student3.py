from studentAgain import Student
#Version 3
#Save all students in a shelve

roster = []

cont = input("Create student? (y/n)")

while (cont == 'y'):
	first_name = input("first_name: ")
	last_name = input("last_name: ")
	courses = []
	courses.append(input("First Course: "))
	courses.append(input("Second Course: "))
	print("Creating a student...")

	#Construct a student instance

	s = Student('Harry', 'Balzanya')
	print("Student enrolled")
	roster.append(s)

	cont = input("create another student? (y/n)")

#save all students in a roster in shevle database
import shelve
db = shelve.open('studentdb')

for s in roster:
	db[s.getLastName()] = s

db.close()





