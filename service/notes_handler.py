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


def notes_sorting():
	list_notes = fdh.readToNotesList()
	arg = input(':>>> ')
	while True:
		if arg == 'asc':
			list_notes.sort(key=lambda note: note.time, reverse=True)
			break
		elif arg == 'desc':
			list_notes.sort(key=lambda note: note.time, reverse=False)
			break
		else:
			print('Некорректное значение, повторите ввод.')
			arg = input(':>>> ')
			
	return list_notes


def dateFilter(date1, date2=None):
	list_notes = fdh.readToNotesList()

	date_start = datetime.strptime(date1[:10], '%d %m %Y')
	op = lambda d: datetime.strptime(d[:10], '%d %m %Y')
	
	if date2 == None:
		for note in list_notes:
			if date_start == op(note[3]):
				print(note)
	else:
		date_finish = datetime.strptime(date2[:10], '%d %m %Y')
		for note in list_notes:
			if date_start < op(note[3]) < date_finish:
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

