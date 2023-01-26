import csv

from model.note import Note


class FileDataHandler:
	'''Класс, записывает/читает данные о заметке в файл формата .csv'''
	
	path = 'test2.csv'
	
	def __init__(self, record: Note):
		self.__record = record

	def write(self):
		with open(path, 'a', newline='') as file:
			size = len(self.read())
			if size:
				wr = csv.writer(file, delimiter=';')
				wr.writerow(
					[size + 1, self.__record.title, self.__record.body, self.__record.time])
			else:
				wr = csv.writer(file, delimiter=';')
				wr.writerow(
					[1, self.__record.title, self.__record.body, self.__record.time])
					
	def rewriteAfterRemove(self, list: list()):
		id = 1
		list = [note.title(id += 1) for note: Note in list]
		with open(path, 'w', newline='') as file:
			rwr = csv.writer(file, delimiter=';')
			for note in list:
				rwr.writerow(note)
	
	def rewriteAfterEdit(self, list: list()):
		with open(path, 'w', newline='') as file:
			rwr = csv.writer(file, delimiter=';')
			for note in list:
				rwr.writerow(note)

	def read(self):
		with open(path, 'r') as file:
			list = csv.reader(file, delimiter=';')
			note_list = []
			index = 0
			for note: Note in list:
				note_list.append(Note(note[index][1], note[index][2], note[index][3]))
			return note_list
				
				
class NotesHandler:
	'''Класс обрабатывает запросы на добавление, удаление, получения данных о заметки'''
	
	def getNoteByTitle(self, title):
		for note in FileDataHandler.read():
			if note.title() == title:
				return note
	
	def getAllTitlesOfNotes():
		return [note.title() for note in FileDataHandler.read()]
		 
	def addNote(note: Note):
		FileDataHandler(note).write()
	
	def removeNoteByTitle(title):
		list = FileDataHandler.read()
		for note in list:
			if note.title() == title:
				list.remove(note)
				FileDataHandler.rewriteAfterRemove(list)
				return

	def editBodyOfNote(title, body):
		list_notes = FileDataHandler.read()
		for note: Note in list_notes:
			if note.title() == title:
				note.body(body)
				rewriteAfterEdit(list_notes)
				return
