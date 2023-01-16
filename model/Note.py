from datetime import datetime as dt

class Note:
	def __init__(self, title: str, body: str, time = dt.now().strftime('%d %b %Y %H:%M:%S')):
		self.__title = title
		self.__body = body
		self.__time = time
	
	@property
	def title(self):
		return self.__title
	
	@property
	def body(self):
		return self.__body
	
	@property
	def time(self):
		return self.__time
	
	@title.setter
	def title(self, title):
		self.__title = title
	
	@body.setter
	def body(self, body):
		self.__body = body
	
	@time.setter
	def time(self, time):
		self.__time = time.strftime('%d %b %Y %H:%M:%S')
	
	def __repr__(self):
		return f'Note: {self.title}, {self.body}, {self.time}'
