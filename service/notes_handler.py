import file_data_handler as fdh
from model.note import Note


def getNoteByTitle(title: str):
    for note in fdh.readAsNotesList():
        if note.title() == title:
            return note


def getAllTitlesOfNotes():
    return [note.title() for note in fdh.readAsNotesList()]


def addNote(note: Note):
    fdh.write(note)


def removeNoteByTitle(title):
    list = fdh.readAsNotesList()
    for note in list:
        if note.title() == title:
            list.remove(note)
            fdh.rewriteAfterRemove(list)
            return


def editBodyOfNote(title, body):
    list_notes = fdh.readAsNotesList()
    for note in list_notes:
        if note.title() == title:
            note.body(body)
            fdh.rewriteAfterEdit(list_notes)
            return