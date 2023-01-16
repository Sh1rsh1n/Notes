from service.DataHandler import DataHandler
from model.Note import Note


def run():

    n = Note('iphone', 'this is the best phone')
    dh = DataHandler('test2.csv', n)

    dh.write()
    note_list = dh.read()

    print(note_list)
