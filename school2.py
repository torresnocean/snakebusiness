# Humberto Torres
# CISW 24 LAB
# 11/6/17
# Program 4

# version 2
# saving all students in a list

from student import Student

# saving the students instances in a list
roster = []

# getting input from the user to create students

cont = input("Create a student? (y/n) ")

while cont == "y":
	first_name = input("First Name: ")
	last_name = input("Last Name: ")
	courses = []
	courses.append(input("First course: "))
	courses.append(input("Second course: "))
	print()
	print("Creating new student... ")
	print()

# creating an actual student instance
	s = Student(first_name, last_name, courses)
	roster.append(s)

	print()
	print("Congradulations! You have been Enrolled... ")
	print(s)

	cont = input("Create another student? (y/n) ")

# check the roster of students
print(str(roster))