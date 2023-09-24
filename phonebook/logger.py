from date_create import*
import os

def input_data():
    name = input_name()
    surname = input_surname()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    with open("Tasks Python\phonebook\phone_book.txt", 'a', encoding='utf-8') as data:
        data.write(f'{surname} {name} {patronymic}\n{phone}\n{address}\n\n')


def print_data():
    os.system('cls')
    with open("Tasks Python\phonebook\phone_book.txt", 'r', encoding='utf-8') as data:
        print(data.read())


# def search_line():
#     search = input('Введите значение для поиска: ')
#     with open("Tasks Python\phonebook\phone_book.txt", 'r', encoding='utf-8') as data:
#         text = data.read().split('\n\n')[:-1]        
#         for line in text:
#             if search in line:
#                 print(line)
#                 print()


def search_line():   
    print('Выберите вариант действия: \n'\
        '1. Поиск по фамилии\n'\
        '2. Поиск по имени\n'\
        '3. Поиск по отчеству\n'\
        '4. Поиск по номеру\n'\
        '5. Поиск по адресу\n')
    cmd = input('Введите номер операции: ')
    while cmd not in ('1', '2', '3', '4', '5'):
        print("Ввод неверный")
        cmd = input('Введите номер операции: ')
        
    search = input('Введите значение для поиска: ').title()
    with open("Tasks Python\phonebook\phone_book.txt", 'r', encoding='utf-8') as data:
        text = data.read().strip().split('\n\n')      
        for line in text:            
            new_line = line.replace(' ','\n').strip().split('\n')
            if search in new_line[int(cmd)-1]:
                print(line)



def remove_line():
    del_str = input('Введите значение для удаления: ')
    with open("Tasks Python\phonebook\phone_book.txt", 'r', encoding='utf-8') as data:
        text = data.read()
        text_lines = text.strip().split('\n\n')
        for i, line in enumerate(text_lines):
            if del_str in line:
              text_lines.pop(i)   
              print('Запись удалена')
    with open("Tasks Python\phonebook\phone_book.txt", 'w', encoding='utf-8') as data:
        data.write('\n\n'.join(text_lines))



def edit_line():
    rep_str = input('Введите значение для замены: ')
    with open("Tasks Python\phonebook\phone_book.txt", 'r', encoding='utf-8') as data:
        text = data.read()
        text_lines = text.strip().split('\n\n')
        for i, line in enumerate(text_lines):
            if rep_str in line:
              rep_line = line   
              print(f'Будет изменена запить: \n{rep_line}')

              name = input_name()
              surname = input_surname()
              patronymic = input_patronymic()
              phone = input_phone()
              address = input_address()
              rep = (f'{surname} {name} {patronymic}\n{phone}\n{address}')
              
              text_lines[i] = rep
              print('Запись изменена')
    with open("Tasks Python\phonebook\phone_book.txt", 'w', newline='', encoding='utf-8') as data:
        data.write('\n\n'.join(text_lines))

