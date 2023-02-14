
from model.note import Note
from view.base_view import View
from us_in.ui import BaseUI as b_u
import os


def run():
	
	print('=' * 30)
	print(f'{'<' * 10} Приложение "Блокнот" {'>' * 10}')
	print('=' * 30)
	
	notepad_name = input('Введите название блокнота или создайте новый:\n:>>> ')
	
	while True:
		b_u.main_i()
		arg = check_input_args(input(':>>> '))
		
		if arg == 'add':
			print('добавили заметку')
			
		if arg == 'ed':
			print('изменили заметку')

		if arg == 'del':
			print('удалили заметку')

		if arg == 'sh':
			print('показали заметку')
		
		if arg == 'exit':
			print('вышли из программы')
			break


def check_input_args(value):
		cmd_list = ['add', 'ed', 'del', 'sh', 'exit']
		while True:
			if value in cmd_list:
				return value
			else:
				print('Некорректное значение, повторите ввод')
				value = input(':>>> ')

def check_csv_list(name):
	str().
	if file.match(f'{name}.csv') in os.listdir(os.getcwd()):
		return True
	return False
