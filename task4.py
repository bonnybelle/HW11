'''
4. У вас несколько JSON файлов. В каждом из этих файлов есть произвольная структура данных.
Вам необходимо написать класс который будет описывать работу с этими файлами, а именно:
    a запись в файл
    b чтение из файла
    c объединение данных из файлов в новый файл
    d получить относительный путь к файлу
    e получить абсолютный путь к файлу
'''
import json
import os
import string
from random import choice, randint

path1 = 'C:/Users/bonny/PycharmProjects/FirstPrj/advanced/HW11/json_data1.json'
path2 = 'C:/Users/bonny/PycharmProjects/FirstPrj/advanced/HW11/json_data2.json'
path3 = 'C:/Users/bonny/PycharmProjects/FirstPrj/advanced/HW11/json_data_merged.json'

animals = ['bird', 'fish', 'cat', 'dog']
pet_names = ['Dorothy', 'Pinkie', 'Chan', 'Star', 'Silva', 'Vincent', 'Ken', 'Lucky']
rnd = randint


class JsonTasks:
    def __init__(self):
        self.clients_list = []

    def person_generator(self):
        name = '{}. {}.'.format(choice(string.ascii_uppercase), choice(string.ascii_uppercase))
        age = '{}'.format(rnd(19, 100))
        pets = []
        for i in range(rnd(1, 4)):
            pet_age = '{}'.format(rnd(1, 10))
            pet = {animals[rnd(0, len(animals) - 1)]: pet_names[rnd(0, len(pet_names) - 1)], 'pet age': pet_age}
            pets.append(pet)
        person = {'initials': name, 'age': age, 'pets': pets}
        return person

    def writing(self, path):
        for i in range(4):
            self.clients_list.append(self.person_generator())
        with open(path, 'w') as write_file:
            json.dump(self.clients_list, write_file, indent=2, ensure_ascii=False)

    def reading(self, path):
        with open(path, 'r') as read_file:
            data = json.load(read_file)
        return data

    def merging(self, path1, path2, path3):
        first_file_data = self.reading(path1)
        second_file_data = self.reading(path2)
        self.clients_list.extend(first_file_data)
        self.clients_list.extend(second_file_data)
        with open(path3, 'w') as merging_file:
            json.dump(self.clients_list, merging_file, indent=2, ensure_ascii=False)

    def r_path(self, file_name):
        r_path = os.path.relpath(file_name, start='')
        return r_path

    def absolute_path(self, file_name):
        abs_path = os.path.abspath(file_name)
        return abs_path


j = JsonTasks()
j.writing(path1)
# j.writing(path2)
print(j.reading(path1))
print(j.reading(path2))
# j.merging(path1, path2, path3)
# print(j.reading(path3))
# print('Абсолютный путь: ', j.absolute_path('json_data1.json'))
print('Абсолютный путь: ', j.absolute_path('json_data_merge.json'))
print('Относительный путь: ', j.r_path('json_data_merge.json'))
