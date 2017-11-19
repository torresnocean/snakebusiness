# Humberto Torres
# 11/18/2017
# CISW 24
# Program 5

# creating a class "comment"..
import time

class Comment:

	def setId(self, post_id):
		self.post_id = post_id

	def getId(self):
		return self.post_id

	def setContent(self, content):
		self.content = content

	def getContent(self):
		return self.content

	def setTime(self, time):
		self.time = time

	def getTime(self):
		return self.time

	def __str__(self):
		return self.post_id + " " + self.content + " " + self.time

# testing section
if __name__ == '__main__':

	c = Comment()
	print("Hello.. Good job so far..")

	print(c)






