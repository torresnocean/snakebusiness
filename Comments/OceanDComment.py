# Daniel Ocean
# 11/18/2017
# CISW 24
# This is a comment class used to generate a timestamp, content and ID

from time import strftime, gmtime

class Comment:

	def setId(self,  id):
		self.commentId = id

	def setContent(self, content):
		self.content = content

	def setTimeStamp(self):
		self.timeStamp = strftime("%a %b %d %Y %H:%M:%S %Z", gmtime())

	def getId(self):
		return self.commentId

	def getContent(self):
		return self.content

	def getTimeStamp(self):
		return self.timeStamp

if __name__ == '__main__':
	obj = Comment()
	obj.setId(1)
	obj.setContent('This is a test string')
	obj.setTimeStamp()
	print(obj.getId())
	print(obj.getContent())
	print(obj.getTimeStamp())
