from data_create import name_data, secondname_data, phone_data, address_data ,post_data,init_id
dict1={0:['name','family','address','post']}
init_id(dict1)
def input_data():
    name = name_data()
    secondname = secondname_data()
    phone = phone_data()
    address = address_data()
    post = post_data()
    element = [name,secondname,phone,address,post]
    return element
def save(stroka):
      with open('book.csv', 'a', encoding='utf-8') as file:
        file.write({stroka},'\n')

def new_dict(dict1,data):
    if len(dict1)==0:id=1
    else:id=max(dict1.keys())+1
    dict1[id]=data
    return dict1

def print_data():
    print('>>')
    with open('book.csv', 'r', encoding='utf-8') as file:
        data = list(file.readlines())
        print(*data)
    return data
def print_dataotdel():
    print('>>')
    with open('otdel.csv', 'r', encoding='utf-8') as file:
        data = list(file.readlines())
        print(*data)
    return data



def put_data():
    data_book = print_data()
    print("Какую запись по счету Вы хотите изменить?")
    number_journal = int(input('Введите номер записи: '))
    number_journal -= 1
    print(f'Изменить данную запись\n{data_book[number_journal]}')
    name = name_data()
    secondname = secondname_data()
    phone = phone_data()
    address = address_data()
    post = post_data()
    data_book = data_book[:number_journal] + [f'{name};{secondname};{phone};{address};{post}\n'] + \
        data_book[number_journal + 1:]
    with open('book.csv', 'w', encoding='utf-8') as file:
        file.write(''.join(data_book))
    print('Изменения успешно сохранены')


def delete_data():
    data_book = print_data()
    print("Какую именно запись по счету Вы хотите удалить?")
    number_journal = int(input('Введите номер записи: '))
    print(f'Удалить данную запись\n{data_book[number_journal - 1]}')
    data_book = data_book[:number_journal] + data_book[number_journal + 1:]
    with open('book.csv', 'w', encoding='utf-8') as file:
        file.write(''.join(data_book))

    print('Изменения успешно сохранены')

def find_in_otdel():
    data_book=print_data()
    data_otdel=print_dataotdel()
    a=input('введите должность ')
    for i in range(len(data_book)):
        for i in range(len(data_otdel)):
            if a==data_book[i,4]==data_otdel[i]:
                print(data_book[i])