# 11/1/2017from studentAgain import Student
# 11/1/2017
#get input from userto create students
cont = input("Create a student? (y/n)")
#save student instances in this list
roster = []

while (cont == 'y'):
	first_name = input("first_name: ")
	last_name = input("last_name: ")
	courses = []
	courses.append(input("First Course: "))
	courses.append(input("Second Course: "))
	print("Creating a student...")

	#Construct a student instance

	s = Student('Harry', 'Balzanya', courses)
	print("Student enrolled")
	print(s)
	roster.append(s)


