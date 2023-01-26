from abc import abstractmethod, ABCMeta
from service.data_service import NotesHandler

class BaseView():
	
	def __init__(self, handle: NotesHandler):
		self.__handle = handle
	
	@property
	def handler(self):
		return self.__handler


class GetNoteView(BaseMenu):
	'''класс, получает и выводит данные о заметках'''
	
	def __init__(self):
		super()
	
	def getNote():
		title = input('Введите название заметки: ')
		note = handle.getNoteByTitle(title)
		print(note)
	
	def getAllNotes():
		note_list = handler.getAllTitlesOfNotes()
		print(note_list)

class AddNote(BaseView):
	
	def __init__(self):
		super()
	
