'''
Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию,
и Вы должны реализовать функционал для изменения и удаления данных.
'''


from os.path import exists
from csv import DictReader, DictWriter


def get_info():
    info = []
    first_name = input('Введите имя пользователя: ')
    last_name = input('Введите фамилию пользователя: ')
    data = read_file()
    now_number_row = len(data) + 1
    info.append(now_number_row)
    info.append(first_name)
    info.append(last_name)
    phone_number = None
    flag = False
    while not flag:
        try:
            phone_number = int(input('Введите номер телефона: '))
            if len(str(phone_number)) != 11:
                print('wrong number')
            else:
                flag = True
        except ValueError:
            print('not valid number')
    info.append(phone_number)
    return info


def create_file():  # создание пустого файла с шапкой
    with open('phone.csv', 'w', encoding='utf-8') as data:
        f_n_writer = DictWriter(data, fieldnames=['№', 'Имя', 'Фамилия', 'Номер'])
        f_n_writer.writeheader()


def write_file(lst):
    with open('phone.csv', 'r', encoding='utf-8') as f_n:
        f_n_reader = DictReader(f_n)
        res = list(f_n_reader)
    with open('phone.csv', 'w', encoding='utf-8') as f_n:
        obj = {'№': lst[0], 'Имя': lst[1], 'Фамилия': lst[2], 'Номер': lst[3]}
        res.append(obj)
        f_n_writer = DictWriter(f_n, fieldnames=['№', 'Имя', 'Фамилия', 'Номер'])
        f_n_writer.writeheader()
        f_n_writer.writerows(res)
    print("Строка успешно записана!")


def read_file():
    with open('phone.csv', 'r', encoding='utf-8') as f_n:
        f_n_reader = DictReader(f_n)
        res = list(f_n_reader)
        # print(len(res))  # длина списка равна 0
        return res


def change_row():
    data = read_file()
    print(*data)
    count_rows = len(data)
    number_row = int(input(f"Введите номер строки, которую хотите изменить от 1 до {count_rows}: "))
    while number_row < 1 or number_row > count_rows:
        number_row = int(input(f"Ошибка!"
                               f"Введите номер строки, которую хотите изменить от 1 до {count_rows}: "))
    first_name = input('Введите имя пользователя: ')
    last_name = input('Введите фамилию пользователя: ')
    phone_number = None
    flag = False
    while not flag:
        try:
            phone_number = int(input('Введите номер телефона: '))
            if len(str(phone_number)) != 11:
                print('wrong number')
            else:
                flag = True
        except ValueError:
            print('not valid number')
    data[number_row - 1] = {'№': number_row, 'Имя': first_name, 'Фамилия': last_name, 'Номер': phone_number}
    with open('phone.csv', 'w', encoding='utf-8') as f_n:
        f_n_writer = DictWriter(f_n, fieldnames=['№', 'Имя', 'Фамилия', 'Номер'])
        f_n_writer.writeheader()
        f_n_writer.writerows(data)
    print("Строка успешно изменена!")


def delete_row():
    data = read_file()
    print(*data)
    count_rows = len(data)
    number_row = int(input(f"Введите номер строки, которую хотите удалить от 1 до {count_rows}: "
                           f"от 1 до {count_rows}: "))
    while number_row < 1 or number_row > count_rows:
        number_row = int(input(f"Ошибка!"
                               f"Введите номер строки, которую хотите удалить от 1 до {count_rows}: "
                               f"от 1 до {count_rows}: "))
    del data[number_row - 1]
    with open('phone.csv', 'w', encoding='utf-8') as f_n:
        f_n_writer = DictWriter(f_n, fieldnames=['№', 'Имя', 'Фамилия', 'Номер'])
        f_n_writer.writeheader()
        f_n_writer.writerows(data)
    print("Строка успешно удалена!")


def record_info():
    lst = get_info()
    write_file(lst)


def main():
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'r':
            if not exists('phone.csv'):
                print('Файл не создан')
                break
            print(*read_file())
        elif command == 'w':
            if not exists('phone.csv'):
                create_file()
                record_info()
            else:
                record_info()
        elif command == 'c':
            if not exists('phone.csv'):
                print('Файл не создан')
                break
            else:
                change_row()
        elif command == 'd':
            if not exists('phone.csv'):
                print('Файл не создан')
                break
            else:
                delete_row()


main()
