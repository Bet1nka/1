from logger import input_data, print_data, put_data, delete_data,new_dict,find_in_otdel
from data_create import init_id
global dict1

def interface():
    init_id(dict1)
    print('1. Записать данные\n'
          '2. Удалить данные\n'
          '3. Изменить данные\n'
          '4. Вывести данные\n'
          '5. Найти по отделу\n')
    command = int(input("Введите номер операции: "))

    while command < 1 or command > 5:
        print('(1-5) ')
        command = int(input("Введите номер операции: "))

    if command == 1:
        print(new_dict(dict1,input_data()))
       
    elif command == 2:
        delete_data()
    elif command == 3:
        put_data()
    elif command == 4:
        print_data()
    else: find_in_otdel()


