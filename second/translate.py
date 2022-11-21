# Написать функцию num_translate(), переводящую числительные от 0 до 10 c
# английского на русский язык. 

def num_translate():
    some_dictionary = {
        'eight': 'восемь',
        'seven': 'семь',
        'five': 'пять',
        'six': 'шесть',
        'two': 'два', 
        'one': 'один', 
        'three':'три', 
        'four': 'четыре',
        'nine': 'девять', 
        'ten': 'десять'
    }
    word = input('slovo - \n').lower()
    if word in some_dictionary:
        print(some_dictionary[word])
    else:
        print('none')

num_translate()

