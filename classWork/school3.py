# Humberto Torres
# CISW 24 LAB
# 11/9/17
# Program 4

# version 3
# basic person with first and last names
# saving all students in a shelve

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

# actually construct our student instance

	s = Student(first_name, last_name, courses)
	roster.append(s)

	print()
	print("Congradulations! you have been Enrolled... ")
	print()

	print(s)

	print()
	cont = input("Create another student? (y/n) ")


# check our roster of students
print(str(roster))

# now, we'll save all the students to the roster
# in a pickle/shelve database.
  
import shelve
db = shelve.open("schooldb")
  
for s in roster:
    db[s.getNames()] = s
  
db.close()    



