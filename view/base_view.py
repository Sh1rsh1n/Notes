from model.note import Note
from service import notes_handler as n_h


class GetNoteView:
	'''класс, запрашивает название заметки и выводит данные об одной или всех заметках'''
	
	def getNote(self):
		'''вывод одной заметки'''
		
		title = input('Введите заголовок заметки: ')
		note = n_h.getNoteByTitle(title)
		print(note)
	
	def getAllNotes(self):
		'''вывод заголовков всех заметок'''
		
		note_list = n_h.getAllTitlesOfNotes()
		print('Названия всех заметок:\n')
		for note in note_list:
			print(f'{note}')

	def notes_sort(self):
		'''отсортированный по дате список всех заметок'''
		
		sorted_notes_list = n_h.notesSorting()
		for	note in sorted_notes_list:
			print(note)

	def getNotesByDate(self):
		'''отсортированный по заданой дате или диапозоне дат, список'''
		from datetime import datetime
		d1 = "1 1 2023"
		d2 = '3 3 2023'
		n_h.dateBeetwinFilter(d1, d2)

class AddNote:
	'''Класс, добавляет заметку'''
	
	def add(self):
		'''добавить заметку'''
		
		title = input('Введите название заметки: ')
		body = input('Введите текст:\n')
		note = Note(title, body)
		n_h.addNote(note)

class RemoveNote:
	'''Класс, удаление заметок по заголовку.'''
	
	def remove(self):
		'''удаление заметк '''
		
		title = input('Введите заголовок заметки, которую нужно удалить: ')
		n_h.removeNoteByTitle(title)
		print(f'Заметка {title}, была успешно удалена.')


class View(GetNoteView, AddNote, RemoveNote):
	pass
