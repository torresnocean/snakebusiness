from person import Person
# 11/1/2017
#student class inherits from the person class to make students

class Student(Person):

	courses = []

	def __init__(self, first_name="NoFirstName", last_name="NoLastName", courses = []):
		Person.__init__(self, first_name, last_name)
		self.courses = courses

	def __str__(self):
		return "Student: " + Person.__str__(self) + " " + str(self.courses)