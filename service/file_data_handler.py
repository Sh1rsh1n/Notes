import csv
from model.note import Note
from datetime import datetime
import os

path = 'notepad.csv'

def write(note: Note):
	'''запись в файл, с добавлением на новой строке'''

	with open(path, 'a', newline='', encoding='utf-8') as file:
		size = len(readToList())
		if size:
			wr = csv.writer(file, delimiter=';')
			wr.writerow([size + 1, note.title, note.body, note.time])
		else:
			wr = csv.writer(file, delimiter=';')
			wr.writerow([1, note.title, note.body, note.time])


def rewrite(list):
	'''Перезапись файла, после удаления или изменения заметки'''
	
	if not len(list) == len(readToList()):
		id = 1
		for note in list:
			note[0] = id
			id += 1
	
	with open(path, 'w', newline='', encoding='utf-8') as file:
		rwr = csv.writer(file, delimiter=';')
		for note in list:
			rwr.writerow(note)

'''
def rewriteAfterEdit(list):
	
	with open(path, 'w', newline='', encoding='utf-8') as file:
		rwr = csv.writer(file, delimiter=';')
		for note in list:
			rwr.writerow(note)
'''

def readToNotesList():
	with open(path, 'r', encoding='utf-8') as file:
		list = csv.reader(file, delimiter=';')
		note_list = []
		index = 0
		for note in list:
			new_note = Note(note[1], note[2], datetime.strptime(note[3], '%d %m %Y %H:%M:%S'))
			note_list.append(new_note)
			index = index + 1
		return note_list


def readToList():
	with open(path, 'r', encoding='utf-8') as file:
		return list(csv.reader(file, delimiter=';'))


