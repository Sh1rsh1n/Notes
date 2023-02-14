import service.file_data_handler as s_f

class MainUI:
	
	def welcome_i():
		s_f.note_name = input('Введите название блокнота: ')

	def main_i():
		print(f'''{'<' * 10} Главное меню {'>' * 10}
	добавить заметку введите: add
	редактировать заметку введите: ed
	удалить заметку введите: del
	просмотр заметок введите: sh
	для выхода введите: exit''')


class AddUI:
	
	def add():
		pass
		



class BaseUI(MainUI, AddUI):
	pass
