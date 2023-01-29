from datetime import datetime as dt

class Note:
	def __init__(self, title: str, body: str, create_time=dt.now().strftime('%d %m %Y %H:%M:%S')):
		self.__create_time = create_time
		self.__title = title
		self.__body = body
	
	@property
	def title(self):
		return self.__title
	
	@property
	def body(self):
		return self.__body
	
	@property
	def time(self):
		return self.__create_time
	
	@title.setter
	def title(self, title):
		self.__title = title
	
	@body.setter
	def body(self, body):
		self.__body = body
	
	@time.setter
	def time(self, create_time):
		self.__create_time = create_time.strftime('%d %m %Y %H:%M:%S')
	
	def __repr__(self):
		return f'Название заметки: {self.__title}\nДата последнего изменения: {self.__create_time}\nТекст:\n{self.__body}\n'
