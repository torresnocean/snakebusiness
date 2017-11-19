# Humberto Torres
# CISW 24
# 10/20/17
# Program 4

from person import *

class Student(Person):

	def __init__(self, first_name = 'NoFirstName', last_name = 'NoLastName', courses = 'cisw 24'):
		Person.__init__(self, first_name, last_name)
		self.courses = [courses]

	def setCourses(self, courses):
		self.courses = courses

	def getCourses(self):
		return self.courses

	def addCourse(self, course):
		self.courses.append(course)

	def dropCourse(self, course):
		if course in self.courses:
			self.courses.remove(course)
			print("The course has been removed..")
		else:
			print("Nothing changed..")


	def __str__(self):
		return "Student: " + Person.__str__(self)

	courses = []



student = Student()


s1 = Person('Umber', 'T.')
s2 = Person('Tony', 'Montana')		
student.addCourse('cisb 11')


if __name__ == '__main__':
															#$ python3 student.py
	print("Student NoFirstName NoLastName")					# s1 Student NoFirstName NoLastName
	print("courses []")										# courses []
	print("set names and courses")							# set names and courses
	print("Student: ", s1)									# s1 Student Umber T.
	# student.addCourse('cisw 18')
	print("courses: ", student.getCourses())				# s1 added, courses ['cisw 24', 'cisb 11']
	print("Student: ", s2)									# s2 student Tony Montana
	student.addCourse('cisw 31')							
	print("courses: ", student.getCourses())				# s2 courses ['cisw 24', 'cisb 11', 'cisb 31']			
	print("Dropped: ", student.dropCourse('cisb 11'))