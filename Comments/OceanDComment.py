# Daniel Ocean
# 11/18/2017
# CISW 24
# This is a comment class used to generate a timestamp, content and ID

import os
import time

class Comment:

	def setId(self,  id):
		self.commentId = id

	def setContent(self, content):
		self.content = content

	def setTimeStamp(self):
		os.environ['TZ'] = 'US/Pacific'
		time.tzset()
		self.timeStamp =  time.strftime('%a %b %d %Y %H:%M:%S %Z')

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
