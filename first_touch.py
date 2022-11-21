def answer(data):
    print(data)

def export_data():  
    some_list = []
    message = {
        'Введите имя - \n',
        'Введите фамилию - \n',
        'введите отчество - \n',
        'Введите должность'
    }
    for i in range(4):
        some_list.append(input(message[i]))
    


