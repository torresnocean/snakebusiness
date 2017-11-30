# Humberto Torres
# 11/19/2017
# CISW 24
# Program 5

# Creating a class Comment to print out the unique ID, content, and timestamp.. 
import os
import time

class Comment:

# The setter..
	def setId(self, set_id):
		self.set_id = set_id

	def setContent(self, content):
		self.content = content

	def setTimeStamp(self):
		os.environ['TZ'] = 'US/Pacific'
		time.tzset()
		self.time_stamp =  time.strftime('%a %b %d %Y %H:%M:%S %Z')
	
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
	print()		# New line..

# Testing the 'content'
	obj.setContent('[This test content] is the content.')
	print(obj.getContent())
	print()		# New line..

# Testing the 'time stamp'
	obj.setTimeStamp()
	print('What time is it? -> ' + obj.getTimeStamp())





