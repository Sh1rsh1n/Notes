import service.file_data_handler as fdh
from model.note import Note


def run():

	# note = Note("skoda", "simply clever")
	# fdh.write(note)
	note_list = fdh.readAsList()
	fdh.rewriteAfterRemove(note_list)

	note_list = fdh.readAsNotesList()
	print(note_list)

