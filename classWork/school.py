# Humberto Torres
# CISW 24 LAB
# 11/2/17
# Program 4

# getting input from the user to create new students
# from little student to big Student
from student import Student

# get input from the user to create a new student
cont = input("Create a student? (y/n) ")

while cont == 'y':
	first_name = input("First Name: ")
	last_name = input("Last Name: ")
	courses = []
	courses.append(input("First course: "))
	courses.append(input("Second course: "))
	print()
	print('Creating new Student... ')
	print()

# create and actual student instance

	s = Student(first_name, last_name, courses)
	print(s)

	print()
	print("Student enrolled successfully...")
	print()

	cont = input("Create another Student? (y/n) ")
	print()

