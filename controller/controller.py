
from model.note import Note
from view.base_view import View
from us_in.ui import BaseUI as b_u


def run():
	
	#load_bar()
	print('=' * 42)
	print(f'{"<" * 10} Приложение "Блокнот" {">" * 10}')
	print('=' * 42)

	
	while True:
		b_u.welcome_ui()
		
		value = input(':>>> ')
		arg = check_input_args(value)	# проверка аргумента переданого из консоли
		
		if arg == 'add':
			while True:
				b_u.add_ui()	# функция добавления заметки в файл
				print('=' * 42)
				print('> добавить еще одну заметку введите: "1" <\n> для выхода в главное меню введите любое значение <')
				arg = input(':>>> ')
				if arg.lower == 'a':
					continue
				break
			continue
									
		if arg == 'ed':
			while True:
				b_u.edit_note_ui()	# функция редактирования заметки
				print('=' * 42)
				print('> Отредактировать другую заметку, введите "1" <\n> для выхода в главное меню введите любое значение <')
				arg = input(':>>> ')
				if not arg == '1':
					break
				else:
					continue
			continue
		
		if arg == 'del':
			print('удалили заметку')

		if arg == 'sh':
			print('показали заметку')
			
		if arg == 'help':
			b_u.help_ui()
			continue
		
		if arg == 'exit':
			print('Завершение работы')
			break


def check_input_args(value):
		cmd_list = ['add', 'ed', 'del', 'sh', 'exit', 'help']
		while True:
			if value in cmd_list:
				return value
			else:
				print('Некорректное значение, повторите ввод')
				value = input(':>>> ')

def load_bar():
	'''бутофория загрузки приложения))'''
	
	import time
	import console
	
	for percent in range(100):
		s = f"[{(percent // 10) * '■'}"
		s += f"{(10 - (percent // 10)) * '○'}] "
		s += f"{percent}"
		print(s, end="\r")
		time.sleep(0.05)
		console.clear()
