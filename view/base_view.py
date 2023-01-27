from abc import abstractmethod, ABCMeta
from service import notes_handler as nh

class BaseView():
	pass


class GetNoteView(BaseView):
	'''класс, получает и выводит данные о заметках'''
	
	def getNote():
		title = input('Введите название заметки: ')
		note = nh.getNoteByTitle(title)
		print(note)
	
	def getAllNotes():
		note_list = nh.getAllTitlesOfNotes()
		print('Названия всех заметок:\n')
		for note in note_list:
			print(f'\t{note.title()}')

class AddNote(BaseView):
	pass


class RemoveNote(BaseView):
	
	def remove():
		title = input('Введите заголовок заметки, которую нужно удалить: ')
		nh.removeNoteByTitle(title)
		print(f'Заметка {title}, была успешно удалена.')
