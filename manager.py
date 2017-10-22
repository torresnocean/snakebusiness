from personTest import *

class Manager(Person):
	def giveRaise(self, percent, bonus=.10):
		Person.giveRaise(self, percent + bonus)

# if __name__ == '__main__':
# 	bob = Person("Bob Smith")