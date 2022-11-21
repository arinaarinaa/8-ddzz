
import view 
import first_touch
import find
def button_click():
    choice = view.button()
    while choice != 'q':
        if choice =='1':
           first_touch.export_data()
        elif choice =='2':
            what_find = input('1 - фамилия, 2 - имя, 3 - работа')
            if what_find == '1': find.find_surname(input('Введите фамилию - \n'))
            if what_find =='2': find.find_name(input('имя  - \n'))
            if what_find =='3': find.occup(input('работа -  - \n'))
        choice = view.button()

