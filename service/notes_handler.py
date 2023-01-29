import service.file_data_handler as fdh
from model.note import Note


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

def dateChoices():
	from datetime import datetime
	# input_date = input('>>> ')
	list_notes = fdh.readToList()
	for note in list_notes:
		print(note[3])
		# if datetime.strftime(note[3][:]):
		# 	print(note)


