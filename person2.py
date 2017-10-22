class Persons:													# Start a class

# Add defaults for constructor arguments
# Allow this file to be imported as well as run/tested
# Process embedded built-in types: strings, mutability
# Add methods to encapsulate operations for maintainability
# Add __repr__ overload method for printing objects

	def __init__(self, fname, lname, job = None, pay = 0):		# Constructor takes 4 arguments 
		self.fname = fname										# Fill out fields when created
		self.lname = lname
		self.job = job
		self.pay = pay											# "self" is the new instance object

	def lastName(self):											# Behavior methods
		return self.lname.split()[-1]							# self is implied subject

	def giveRaise(self, percent):
		self.pay = int(self.pay * (1 + percent))				# Must change here only

	def __repr__(self):											# Added method
		return '[Persons: %s, %s]' % (self.fname, self.pay)		# String to print


# Add incremental self-test code
if __name__ == '__main__':										# When run for testing only
# self-test code
	bob = Persons('Bob', 'Smith', job = 'dev.', pay = 50)		# Test the class
	sue = Persons('Sue', 'Jones', job = 'Tech', pay = 100)		# Runs __init__ automatically
	#print("Hello, my name is", bob.fname, bob.lname + ",", "I work as a Web", bob.job, "and i'm at", bob.pay, "$hr.")	# Fetch attached attributes
	#print("Hello, my name is", sue.fname, sue.lname + ",", "I work as a Web", sue.job, "and i'm at", sue.pay, "$hr.")	# sue's and bob's attributes differ
	print(bob)
	print(sue)
	print(bob.lastName() + ", " + sue.lastName())				# Use the new methods
	sue.giveRaise(.10)											# Instead of hardcoding
	print(bob)
	print(sue)
	#print(sue.pay)


	#print(bob.fname.split()[-1])								# Extract object's name
	#sue.pay *= 1.10											# Give this object a raise
	#print('%.2f' % sue.pay)






# End of class