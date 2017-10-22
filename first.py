class firstClass:							# Define a class object

	def setData(self, value):				# Define class's methods
		self.data = value					# "self" is the instance

	def Display(self):						
		print(self.data)					# self.data: per instance


x = firstClass()							# Make two instances
y = firstClass()							# Each is a new namespace

x.setData("King Arthur")					# Call methods: self is x
y.setData(3.14159)							# Runs: firstClass.setData(y, 3.14159)

x.Display()									# self.data differs in each instance
# print(x)
y.Display()									# Runs: firstClass.display(y)
# print(y)

x.data = "New value"						# Can get/set attributes
x.Display()									# Outside the class too