def button():
    inp = input('1 - внесение, 2 - поиск, для выхода нажмите q\n')
    return inp

import os 
import csv
def import_data(data):
    if not os.path.exists('data.scv'):
        with open('data.scv', 'w', encoding = 'utf-8') as dt:
            writer = csv.writer(dt, delimiter = ';', lineterminator="\r")
            writer.writerows('Фамилия', 'имя', 'отчество', 'работа')
        exit = ' '
        while exit !='q':
            data = [
                [input('Фамилия - \n'), input('Имя - \n'), input('Отчество - \n'), input('работа - \n')]
            ]
            with open('data.scv', 'a', 'a', encoding = 'utd-8') as dt:
                writer.writerows(data)
           
