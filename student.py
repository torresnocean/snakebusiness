# Daniel Ocean 
# CISW 24 LAB
# 10/15/17
# Program 4 

from person import *

class Student(Person):
	
	courses = []

	def __init__(self, first='NoFirstName', last='NoLastName', course= 'No Main Course'):
		Person.__init__(self, first, last)
		self.courses = [course]

	def setMainCourse(self, course):
		self.courses.insert(0, course)

	def getCourses(self):
		return self.courses

	def addCourse(self, course):
		self.courses.append(course)

	def dropCourse(self, course):
		if course in self.courses:
			self.courses.remove(course)
			print("Removed " + course)
		else:
			print("Sorry " + course + " could not be found")
		
	# def __repr__(self):
	# 	return '[Student: %s %s]' % (Person.__repr__(self), (self.courses))

	def __str__(self):
	 	return "Student: " + Person.__str__(self)





s1 = Person("Daniel", "Ocean")
print(s1)




if __name__ == '__main__':
	print("----------------------------------------name/main condition--------------------------------------")
	stu1 = Student()					# s1 Student NoFirstName NoLastName
	print(stu1)
	print("Courses", stu1.courses)		# s1 courses []

	stu1.setMainCourse("cisw 24")		# set names and courses
	stu1.addCourse("cisb 11")			# set names and courses
	stu1.setFirstName("Johnny")			#s1 Student Johnny Bravo
	stu1.setLastName("Bravo")			#s1 Student Johnny Bravo
	stu1.setMainCourse("cisw 24")		#s1 courses ['cisw 24']
	stu1.addCourse("cisb 11")			# s1 added, courses ['cisw 24', 'cisb 11']  //already added cisw 24

	stu2 = Student("James", "Holbert")	# s2 Student James Holbert

	stu2.addCourse("cisw 24")			# s2 courses ['cisw 24', 'cisb 11', 'cisb 31'] 
	stu2.addCourse("cisb 11")			# s2 courses ['cisw 24', 'cisb 11', 'cisb 31'] 
	stu2.addCourse("cisb 31")			# s2 courses ['cisw 24', 'cisb 11', 'cisb 31'] 

	stu2.dropCourse("cisw 24")			#s2 dropped, courses ['cisw 24', 'cisb 31']
	stu2.dropCourse("cisb 31")			#s2 dropped, courses ['cisw 24', 'cisb 31']

	print(stu2)
	print("Courses", stu2.courses)
	print("----------------------------------------name/main condition--------------------------------------")



















