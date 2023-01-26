from service.data_service import FileDataHandler
from model.note import Note


def run():

	nt = Note('iphone', 'this is the best phone')
	dh = FileDataHandler(nt)

	#dh.write()
	note_list = dh.read()
	dh.reWrite(note_list)

	note_list = dh.read()
	print(note_list)

