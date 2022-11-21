import csv
import os
import first_touch

def find_surname(surname):
    if os.path.exists('data.scv'):
        with open('data.scv', 'r', encoding = 'utf-8') as dt:
            reader = csv.reader(dt)
            some_list = []
            for row in reader:
                if len(row) != 0:
                    some_list.append(row[1].split(';'))
            count = 0
            for item in some_list:
                if surname == item[0]:
                    first_touch.answer(item)
                    count +=1
            if count ==0:
                first_touch.answer(f'{surname} nope')
    else:
        first_touch.answer('hz bro')

def find_name(name):
    if os.path.exists('data.scv'):
        with open('data.scv', 'r', encoding = 'utf-8') as dt:
            reader = csv.writer(dt)
            sum_list = []
        for row in reader:
            if len(row)!=0:
                sum_list.append(row[0].split(';'))
        count = 0
        for item in sum_list:
            if name == item[2]:
                first_touch.answer(item)
                count+=1
        if count == 0:
            first_touch.answer(f'Человек с таким {name} не найден!')
    else:
        first_touch.answer('Файл не найден')

def occup(occup):
    if os.path.exists('data.scv'):
        with open('data.scv', 'r', encoding = 'utf-8') as dt:
            reader = csv.writer(dt)
            sum_list = []
        for row in reader:
            if len(row)!=0:
                sum_list.append(row[0].split(';'))
        count = 0
        for item in sum_list:
            if occup == item[2]:
                first_touch.answer(item)
                count+=1
        if count == 0:
            first_touch.answer(f'Человек с таким {occup} не найден!')
    else:
        first_touch.answer('Файл не найден')