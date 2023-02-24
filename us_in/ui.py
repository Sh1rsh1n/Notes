from model.note import Note
from service import notes_handler as n_h
from re import compile

def draw_bord(size=0, bord='='):
	'''функция отрисовки границ меню'''
	return bord * size

def console_clear():
	'''очистка консоли'''

	print("\033[H\033[J")

# def check_date(date):
# 	'''метод, проверка корректности ввода даты'''
#
# 	if compile(r"(?<!\d)(?:0?[1-9]|[12][0-9]|3[01]) (?:0?[1-9]|1[0-2]) (?:19[0-9][0-9]|20[01][0-9])(?!\d)").search(date):
# 		return True
# 	return False

check_date = lambda date: compile(r"(?<!\d)(?:0?[1-9]|[12][0-9]|3[01]) (?:0?[1-9]|1[0-2]) (?:19[0-9][0-9]|20[0-9][0-9])(?!\d)").search(date)


class MainUI:
	
	def welcome_ui():
		'''метод, отображает меню приветствия пользователя'''

		print("\t\tГлавное меню")
		print(draw_bord(42))
		print("help - показать список всех команд.\nexit - выход из приложения")
		print(draw_bord(42))

	def help_ui():
		'''метод, показывает список команд для работы с приложением'''

		console_clear()
		print(f"{draw_bord(11, '*')} список всех команд {draw_bord(11, '*')}")
		print('add\tдобавить заметку (add/create)')
		print('ed\tредактировать заметку (edit)')
		print('del\tудалить заметку (delete/remove)')
		print('sh\tпросмотр заметок (show/get)')
		print(draw_bord(42))
		print("Список команд аргумента 'sh'")
		print('\tgo\t(get one) просмотр содержимого заметки')
		print('\tсортировка заметок по дате последнего изменения:')
		print('\tsa\t(sorting by ascending) по возрастанию')
		print('\tsd\t(sorting by descending) по убыванию')
		print('\tflt\t(filtering by date) фильтр по дате')
		print('\tmain\tвыход в основное меню')
		print(draw_bord(42))
		print('help\tсписок всех команд')
		print('exit\tвыход из приложения')
		print(draw_bord(42))

class AddUI:
	
	def add_note_ui():
		'''метод, добавление заметки'''

		console_clear()
		print(draw_bord(42))
		print('\t\tДобавление заметки.')
		print(draw_bord(42))

		title = input('Введите название заметки: ')
		body = input('Введите текст:\n')
		note = Note(title, body)	# создаем заметку
		n_h.addNote(note)	# добавляем заметку в файл
		print(f'{draw_bord(10, ">")} Заметка успешно добавлена {draw_bord(10, "<")}')

class EditUI:
	
	def edit_note_ui():
		'''метод, редактирование заметки'''

		console_clear()
		print(draw_bord(42))
		print('\t\tРедактирование заметки.')
		print(draw_bord(42))

		notes_list = n_h.getNotesList() # получаем список всех заметок по названию
		
		[print('{:2s} || {:10s}'.format(note[0], note[1])) for note in notes_list]
		
		id = input('Введите номер заметки: ')
		if n_h.editNote(id):
			print('Заметка успешно отредактирована')
		else:
			print('Заметки с таким номером нет в списке')

class DeleteUI:
	
	def delete_note_ui():
		'''метод удаление заметки'''

		console_clear()
		print(draw_bord(42))
		print('\t\tУдаление заметки.')
		print(draw_bord(42))
		
		notes_list = n_h.getNotesList() # получаем список всех заметок по названию
		
		[print('{:2s} || {:10s}'.format(note[0], note[1])) for note in notes_list]
		
		id = input('Введите номер заметки: ')
		if n_h.removeNote(id):
			print('Заметка была успешно удалена')
		else:
			print('Заметки с таким номером нет в списке')


class ShowUI:
	
	def show_note_ui():
		'''метод, отображает название выбранной заметки, текст, дата последнего изменения'''

		console_clear()
		print(draw_bord(42))
		print('\t\tПросмотр заметки.')
		print(draw_bord(42))
		
		notes_list = n_h.getNotesList() # получаем список всех заметок по названию
		
		[print('{:2s} || {:10s}'.format(note[0], note[1])) for note in notes_list]
		
		id = input('Введите номер заметки: ')
		for note in notes_list:
			if id == note[0]:
				console_clear()
				print(f'{draw_bord(42)}\nНазвание: {note[1]}\n{draw_bord(42)}\nТекст: {note[2]}\n{draw_bord(42)}\nДата изменения: {note[3]}\n{draw_bord(42)}')
				return 
		print('Заметки с таким номером нет в списке')
	
	def sorted_by_date(value=False):
		'''метод, сортировки списка всех заметок по дате изменения, по-умолчанию в порядке возрастания(от самой старой заметки)'''

		console_clear()
		notes_list = n_h.notes_sorting(value)
		print(draw_bord(42))
		[print('{:25s} || {}'.format(note.title, note.time)) for note in notes_list]
		print(draw_bord(42))

	def filter_by_dates():
		'''метод, выборки данных по указаной дате(-ам)'''
		while True:
			console_clear()

			print("Введите даты в формате: 12 12 2012")
			date1 = input('первая дата :>>> ')
			while not check_date(date1):
				print("некорректное значение, повоторите ввод.")
				print("перая дата является обязательным параметром")
				print("Введите дату в формате: 12 12 2012")
				date1 = input(':>>> ')

			print('Введите пустую строку, если вторая дата не нужна.')
			date2 = input('вторая дата :>>> ')
			if date2:
				while not check_date(date2):
					print("некорректное значение, повоторите ввод.")
					print("Введите дату в формате: 12 12 2012")
					date2 = input(':>>> ')

			list_after_sort = n_h.dateFilter(date1, date2)
			print(draw_bord(42))
			[print('{:25s} || {}'.format(note[1], note[3])) for note in list_after_sort]
			print(draw_bord(42))
			arg = input('Выбрать другие даты, введите "1", для выхода введите любое значение\n:>>> ')
			if arg == '1':
				continue
			break

class BaseUI(MainUI, AddUI, EditUI, DeleteUI, ShowUI):
	pass
