import service.file_data_handler as fdh
from model.note import Note
from datetime import datetime


def getNoteByTitle(title: str):
	list = fdh.readToNotesList()
	for note in list:
		if note.title == title:
			return note


def getAllTitlesOfNotes():
	list = [note.title for note in fdh.readToNotesList()]
	return list


def addNote(note: Note):
	fdh.write(note)


def removeNoteByTitle(title):
	list = fdh.readToList()
	for note in list:
		if note[1] == title:
			list.remove(note)
			fdh.rewriteAfterRemove(list)
			return


def editBodyOfNote(title, body):
	list_notes = fdh.readToNotesList()
	for note in list_notes:
		if note.title() == title:
			note.body(body)
			fdh.rewriteAfterEdit(list_notes)
			return

def notesSorting():
	list_notes = fdh.readToNotesList()
	list_notes.sort(key=lambda note: note.time, reverse=True)
	return list_notes

def dateBeetwinFilter(date1, date2):
	
	list_notes = fdh.readToList()

	date_start = datetime.strptime(date1[:10], '%d %m %Y')
	date_finish = datetime.strptime(date2[:10], '%d %m %Y')
	
	for note in list_notes:
		if date_start < op_date(note[3]) < date_finish:
			print(note)


	
'''	# поиск по возрастанию(от наименьшего)
if date1 < datetime.now():
	for note in list_notes:
		if date1 < datetime.striptime(note[3][:10], '%d %m %Y'):
			print(note)

# поиск по убыванию(от наибольшего)
if date1:
	for note in list_notes:
		if date1 > datetime.striptime(note[3][:10], '%d %m %Y'):
			print(note)'''

