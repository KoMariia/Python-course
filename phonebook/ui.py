from logger import*

def userinterface():
    cmd = ''
    while cmd != '6':

        print('Выберите вариант действия: \n'\
        '1. Записать данные\n'\
        '2. Вывести данные\n'\
        '3. Поиск данных\n'\
        '4. Удаление данных\n'\
        '5. Изменение данных\n'\
        '6. Выход\n')
        cmd = input('Введите номер операции: ')
        while cmd not in ('1', '2', '3', '4', '5', '6'):
            print("Ввод неверный")
            cmd = input('Введите номер операции: ')
        if cmd == '1':
            input_data()
        elif cmd == '2':
            print_data()
        elif cmd == '3':
            search_line()
        elif cmd == '4':
            remove_line()
        elif cmd == '5':
            edit_line()   
    print('Всего доброго!')