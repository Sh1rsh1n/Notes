import re

import service.file_data_handler as fdh
from model.note import Note
from datetime import datetime


def getNotesList():
	list = fdh.readToList()
	return list


def addNote(note: Note):
	fdh.write(note)


def removeNote(id):
	list = fdh.readToList()
	for note in list:
		if note[0] == id:
			list.remove(note)
			fdh.rewrite(list)
			return True
	return False


def editNote(id):
	
	list_notes = fdh.readToList()
	for note in list_notes:
		if note[0] == id:
			print(f'Название: {note[1]}\nТекст заметки: {note[2]}\n')
			title = input('Введите название заметки:\n')
			if title:	# если пользователь не ввел значение, оставить поле без изменений
				note[1] = title
				note[3] = datetime.now().strftime('%d %m %Y %H:%M:%S')
				print('изменение названия успешно завершено')
			body = input('Введите текст заметки:\n')
			if body:	# если пользователь не ввел значение, оставить поле без изменений
				note[2] = body
				note[3] = datetime.now().strftime('%d %m %Y %H:%M:%S')
				print('изменение текста заметки успешно завершено')
			fdh.rewrite(list_notes)
			return True
	return False


def notes_sorting(value=False):
	list_notes = fdh.readToNotesList()	# получаем список всех заметок
	list_notes.sort(key=lambda note: note.time, reverse=value) # сортируем заметки в зависимости от переданного параметра
	return list_notes


def dateFilter(date1, date2):

	list_notes = fdh.readToList()
	list_after_sort = []

	op = lambda d: datetime.strptime(d[:10], '%d %m %Y')
	
	if date2 is None or date2 is "":
		for note in list_notes:
			if op(date1) == op(note[3]):
				list_after_sort.append(note)
	else:
		date_start = op(date1)
		date_finish = op(date2)
		for note in list_notes:
			if date_start < op(note[3]) < date_finish:
				list_after_sort.append(note)

	return list_after_sort