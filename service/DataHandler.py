import csv

from model.Note import Note


class DataHandler:
    def __init__(self, path: str, record: Note):
        self.__path = path
        self.__record = record

    def write(self):
        with open(self.__path, 'a', newline='') as file:
            size = len(self.read())
            if size:
                wr = csv.writer(file, delimiter=';')
                wr.writerow([size + 1, self.__record.title, self.__record.body, self.__record.time])
            else:
                wr = csv.writer(file, delimiter=';')
                wr.writerow([1, self.__record.title, self.__record.body, self.__record.time])

    def read(self):
        with open(self.__path, 'r') as file:
            return list(csv.reader(file, delimiter=';'))
