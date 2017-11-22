# Humberto Torres
# 11/18/2017
# CISW 24
# Program 5

# Creating a class Comment to print out an ID, content, and timestamp.. 
from time import strftime

class Comment:

# The setter..
	def setId(self, set_id):
		self.set_id = set_id

	def setContent(self, content):
		self.content = content

# I used 1 argument (time_stamp) and it worked..
	def setTimeStamp(self, time_stamp):
		self.time_stamp =  strftime('%A, %b. %d %Y   %H:%M:%S %Z')
	
# The getter..
	def getId(self):
		return self.set_id
	
	def getContent(self):
		return self.content

	def getTimeStamp(self):
		return self.time_stamp

# Testing section..
if __name__ == '__main__':
	obj = Comment()

# Testing the unique 'id'
	obj.setId(10)
	print('Unique Id:', obj.getId())
	print()

# Testing the 'content'
	obj.setContent('[This test content] is the content.')
	print(obj.getContent())
	print()

# Testing the 'time stamp'
# On the obj.setTimeStamp, i gave it an empty space ('')
	obj.setTimeStamp('')
	print('What time is it? -> ' + obj.getTimeStamp())





