#basic person with first and last name
# 11/1/2017
class Person:
	
	def __init__(self, first, last):
		self.first_name = first
		self.last_name = last
		
	def __str__(self):
		return self.first_name + " " + self.last_name

		
	def getLastName(self):
		return self.last_name

	def setFn(self, fn):
		self.fn = fn

	def setLn(self, ln):
		self.ln = ln

	def setName(self, fn, ln):
		self.fn = fn
		self.ln = ln