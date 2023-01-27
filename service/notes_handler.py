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

