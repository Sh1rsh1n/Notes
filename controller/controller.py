from us_in.ui import BaseUI, draw_bord, console_clear
import time

def run():

	start()
	BaseUI.welcome_ui()

	while True:

		value = input(':>>> ')
		arg = check_input_args(value)	# проверка аргумента переданого из консоли
		
		if arg == 'add':
			while True:
				BaseUI.add_note_ui()	# функция добавления заметки в файл
				print(draw_bord(42))
				print('> добавить еще одну заметку введите: "1" <\n> для выхода в главное меню введите любое значение <')
				arg = input(':>>> ')
				if arg == '1':
					continue
				break
			BaseUI.welcome_ui()
			continue
									
		if arg == 'ed':
			while True:
				BaseUI.edit_note_ui()	# функция редактирования заметки
				print(draw_bord(42))
				print('> Отредактировать другую заметку, введите "1" <\n> для выхода в главное меню введите любое значение <')
				arg = input(':>>> ')
				if not arg == '1':
					break
				else:
					continue
			BaseUI.welcome_ui()
			continue
		
		if arg == 'del':
			while True:
				BaseUI.delete_note_ui()	# функция удаления заметки
				print(draw_bord(42))
				print('> Удалить еще одну заметку, введите "1" <\n> для выхода в главное меню введите любое значение <')
				arg = input(':>>> ')
				if not arg == '1':
					break
				else:
					continue
			BaseUI.welcome_ui()
			continue
			
		if arg == 'sh':

			while True:
				console_clear()
				print('\tМеню просмотра заметок.')
				print(draw_bord(42))
				arg = input(':>>> ')

				if arg == 'go':
					while True:
						BaseUI.show_note_ui()
						print(draw_bord(42))
						print('Просмотр еще одной заметки, введите "1"\nдля выхода в меню просмотра введите любое значение\nдля выхода в главное меню введите "main"')
						arg = input(':>>> ')
						if arg == '1':
							continue
						else:
							break
				
				if arg == 'sa':
					BaseUI.sorted_by_date(True)
					break

				if arg == 'sd':
					BaseUI.sorted_by_date(False)
					break

				if arg == 'flt':
					BaseUI.filter_by_dates()
					break

				if arg == 'help':
					BaseUI.help_ui()
					continue

				if arg == 'main':
					break
				else:
					print("Некорректное значение. Повторите ввод.")
					continue
			BaseUI.welcome_ui()

		if arg == 'help':
			BaseUI.help_ui()
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

def start():

	for percent in range(100):
		print(draw_bord(42))
		print(f'{draw_bord("<", 10)} Приложение "Блокнот" {draw_bord(">", 10)}')
		print(draw_bord(42))
		s = f"[{(percent // 10) * '■'}"
		s += f"{(10 - (percent // 10)) * '_'}] "
		s += f"{percent}%"
		print(s, end="\r")
		time.sleep(0.01)
		console_clear()