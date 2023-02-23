from view.base_view import View
from model.note import Note
from service import notes_handler as n_h
from colorama import Fore

def draw_bord(size=0, bord='='):
	'''функция отрисовки границ меню'''
	return bord * size


class MainUI:
	
	def welcome_ui():
		'''метод, отображает меню приветствия пользователя'''
		
		print(f'''
{draw_bord(10, '<')} Главное меню {draw_bord(10, '>')}
{draw_bord(42)}
help - показать списка всех команд.\nexit - выход из приложения
{draw_bord(42)}''')

	def help_ui():
		'''метод, показывает список команд для работы с приложением'''
		
		print(f'''
{draw_bord(11, '*')} список всех команд {draw_bord(11, '*')}
		add\t\tдобавить заметку
		ed\t\tредактировать заметку
		del\t\tудалить заметку
		sh\t\tпросмотр заметок
		help\tсписок всех команд
		exit\tвыход из приложения
{draw_bord(42)}
					''')

class AddUI:
	
	def add_note_ui():
		'''метод, добавление заметки'''		
		
		print(draw_bord(42))
		print(f'{draw_bord(10, " ")}Добавление заметки.')
		print(draw_bord(42))
		
		title = input('Введите название заметки: ')
		body = input('Введите текст:\n')
		note = Note(title, body)	# создаем заметку
		n_h.addNote(note)	# добавляем заметку в файл
		print(f'{draw_bord(">", 10)} Заметка успешно добавлена {draw_bord("<", 10)}')

class EditUI:
	
	def edit_note_ui():
		'''метод, редактирование заметки'''
		
		print('=' * 42)
		print(f'{" " * 10}Редактирование заметки.')
		print('=' * 42)
		
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
		
		print('=' * 42)
		print(f'{" " * 10}Удаление заметки.')
		print('=' * 42)
		
		notes_list = n_h.getNotesList() # получаем список всех заметок по названию
		
		[print('{:2s} || {:10s}'.format(note[0], note[1])) for note in notes_list]
		
		id = input('Введите номер заметки: ')
		if n_h.removeNote(id):
			print('Заметка была успешно удалена')
		else:
			print('Заметки с таким номером нет в списке')


class ShowUI:
	
	def show_note_ui():
		
		print('=' * 42)
		print(f'{" " * 10}Просмотр заметки.')
		print('=' * 42)
		
		notes_list = n_h.getNotesList() # получаем список всех заметок по названию
		
		[print('{:2s} || {:10s}'.format(note[0], note[1])) for note in notes_list]
		
		id = input('Введите номер заметки: ')
		for note in notes_list:
			if id == note[0]:
				print(f'{"=" * 42}\nНазвание: {note[1]}\n{"=" * 42}\nТекст: {note[2]}\n{"=" * 42}\nДата изменения: {note[3]}\n{"=" * 42}')
				return 
		print('Заметки с таким номером нет в списке')
	
	def sorted_by_date():
		notes_list = n_h.notes_sorting()
		


class BaseUI(MainUI, AddUI, EditUI, DeleteUI, ShowUI):
	pass
