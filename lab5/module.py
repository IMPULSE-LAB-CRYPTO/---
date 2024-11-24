import os
import csv


class ImageIterator():
    """
    Класс Итератора для картинок
    """
    def __init__(self, annotation_file=None, folder_path=None):
        '''
        Конструктор, инициализирующий массив строчек в зависимости от передаваемых аргументов
        (файла аннотации или папки картинок)
        :param annotation_file: файл аннотации
        :param folder_path: Папка картинок
        '''
        self.images = []
        if annotation_file:
            with open(annotation_file, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.images.append(row['absolute_path'])
        elif folder_path:
            for root, _, files in os.walk(folder_path):
                for file in files:
                    if file.endswith(('jpg', 'jpeg', 'png')):
                        self.images.append(os.path.join(root, file))
        if not folder_path and not annotation_file:
            raise Exception("Необходимо указать либо файл аннотации, либо папку картинок")
        self.index = 0


    def __iter__(self):
        '''
        Метод возвращения самого объекта итератора
        '''
        return self


    def __next__(self):
        '''
        Метод прохода по всем элементам массива класса через индекс и вывода их на экран
        '''
        if self.index < len(self.images):
            image_path = self.images[self.index]
            self.index += 1
            return image_path
        else:
            raise StopIteration


    #Тест обратки
    def prev(self):
        '''
        Метод обратный next
        '''
        self.index -= 1
        if self.index < 0:
            raise StopIteration
        return self.images[self.index]
