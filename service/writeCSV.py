import csv
import os
from model.note import Note

def write(path: str, note: Note):
	with open(path, 'a', newline='') as file:
		if os.path.exists(path):
			rec = csv.writer(file, delimiter=';')
			rec.writerow(id, note.title, note.body, note.time)
		else:
			rec = csv.writer(file, delimiter=';')
			rec.writerows('id', 'title', 'body', 'time')
			rec.writerows(id, note.title, note.body, note.time)

n = Note('adbc', 'gyhmjmbfrf')
write('test1', n)
