from view.base_view import View
from model.note import Note
from service import notes_handler as n_h


class MainUI:
	
	def welcome_ui():
		'''меню приветствия пользователя'''
		
		print(f'{"<" * 10} Главное меню {">" * 10}')
		print('=' * 42)
		print('help - показать списка всех команд.\nexit - выход из приложения')
		print('=' * 42)

	def help_ui():
		'''список команд для работы с приложением'''
		
		print(f'''
{'*' * 11} список всех команд {'*' * 11}
		add\t\tдобавить заметку
		ed\t\tредактировать заметку
		del\t\tудалить заметку
		sh\t\tпросмотр заметок
		help\tсписок всех команд
		exit\tвыход из приложения
{'*' * 42}
					''')

class AddUI:
	
	def add_ui():
		'''добавление заметки'''		
		
		print('=' * 42)
		print(f'{" " * 10}Добавление заметки.')
		print('=' * 42)
		
		title = input('Введите название заметки: ')
		body = input('Введите текст:\n')
		note = Note(title, body)	# создаем заметку
		n_h.addNote(note)	# добавляем заметку в файл
		print(f'{">" * 10} Заметка успешно добавлена {"<" * 10}')

class EditUI:
	
	def edit_note_ui():
		'''редактировать заметку'''
		
		print('=' * 42)
		print(f'{" " * 10}Редактирование заметки.')
		print('=' * 42)
		
		notes_list = n_h.getNotesList() # получаем список всех заметок по названию
		print(notes_list)
		[print(f'{note[0]} => {note[1]}') for note in notes_list]
			
		print('=' * 42)
		
		id = input('Введите номер заметки: ')
		if n_h.editBodyOfNote(id):
			print('Заметка успешно отредактирована')
		else:
			print('Заметки с таким номером нет в списке')

class BaseUI(MainUI, AddUI, EditUI):
	pass
