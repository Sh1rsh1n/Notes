#import service.file_data_handler as fdh
#from model.note import Note
from view.base_view import GetNoteView as gnv 
from view.base_view import RemoveNote as rn


def run():

	# note = Note("uskoda", "simply clever")
	# fdh.write(note)
	'''note_list = fdh.readAsList()
	fdh.rewriteAfterRemove(note_list)

	note_list = fdh.readAsNotesList()
	print(note_list)'''
	
	#gnv.getNote()
	gnv.getAllNotes()
	rn.remove()
	gnv.getAllNotes()
	
	

