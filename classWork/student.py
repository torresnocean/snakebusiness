# Humberto Torres
# CISW 24 LAB
# 10/28/17
# Program 4

# from little person to big person
from person import Person

# subclassing person to make students
class Student(Person):

	def __init__(self, first_name, last_name, courses):
		Person.__init__(self, first_name, last_name)
		self.courses = courses

	#def setCourses(self, courses):
	#	self.courses = courses

	#def getCourses(self):
	#	return self.courses

	#def addCourse(self, course):
	#	self.courses.append(course)

	#def dropCourse(self, course):
	#	if course in self.courses:
	#		self.courses.remove(course)
	#		print("A changed has been made..")
	#	else:
	#		print("Nothing changed..")

	def __str__(self):
		return ("Student Name: " + Person.__str__(self) + " " + str(self.courses))		



# END OF CLASS



#student = Student()

#s1 = Person('Umber', 'T.')
#s2 = Person('Tony', 'Montana')		
#student.addCourse('cisb 11')


#if __name__ == '__main__':
															#$ python3 student.py
	#print("Student NoFirstName NoLastName")					# s1 Student NoFirstName NoLastName
	#print("courses []")										# courses []
	#print("set names and courses")							# set names and courses
	#print("Student: ", s1)									# s1 Student Umber T.
	#print("courses: ", student.getCourses())				# s1 added, courses ['cisw 24', 'cisb 11']
	#print("Student: ", s2)									# s2 student Tony Montana
	#student.addCourse('cisb 31')							
	#print("courses: ", student.getCourses())				# s2 courses ['cisw 24', 'cisb 11', 'cisb 31']			
	#student.dropCourse('cisb 11')							# s2 dropped, courses ['cisw 24', 'cisb 31']
	#print("dropped, courses: ", student.getCourses())
