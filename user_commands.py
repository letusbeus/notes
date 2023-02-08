from user_interface import Notes
from datetime import datetime
from save_read_file import load_file, rewrite_file


def create_new_note():
    """
    Коннектор, принимает input данных title, msg от пользователя,
    подставляет автоматом id, date.
    :return:
    """
    title = create_tittle()
    msg = create_msg()
    new_notes = Notes(title, msg)
    ready_note = save_note_to_data(new_notes.get_id(), title, msg, new_notes.get_change_date())
    return ready_note


def create_tittle():
    """
    Создает название заметки
    :return: Название заметки
    """
    title = input('Введите название Заметки: ')
    # title = 'Новая заметка'
    return title


def create_msg():
    msg = input('Введите заметку: ')
    # msg = 'Вот нужная информация'
    return msg


def save_note_to_data(id, title, msg, date):
    """
    Принимает значения атрибутов класса, переводит их в словарь.
    :param id:  Атрибут
    :param title: Атрибу
    :param msg: Атрибут
    :param date: Атрибут
    :return: Возвращает словарем значения атрибута класса
    """
    date_list = {
        'id': id,
        'title': title,
        'msg': msg,
        'date': date
    }
    return date_list


def show_all_notice():
    """
    Показывает все заметки, на вход ничего не принимает
    :return: Все заметки
    """
    try:
        data = load_file()
        for val in data:
            print(val)
    except FileNotFoundError:
        print(f'{"-" * 15}\nЗаметок еще нет\n{"-" * 15}')


def search_notice(data_list, search_data, choice):
    """
    Ищет заметки в файле
    :param data_list: Указываются данные в виде списка словарей
    :param search_data: Указывается текст для поиска
    :param choice: switch case выбора типа поиска(1, 2, 3, 4)
    :return: Возвращает список словарей заметок
    """
    if choice == 1:
        data = list(filter(lambda x: x['id'] == search_data, data_list))
        if not data:
            print(f'\n\nДанных с таким id нет.\n\n')
        else:
            print(f'\n\nПо вашему запросу найдены следующие заметки: \n\n{data}\n')
    elif choice == 2:
        data = list(filter(lambda x: x['title'] == search_data, data_list))
        if not data:
            print(f'\n\nДанных с таким id нет.\n\n')
        else:
            print(f'\n\nПо вашему запросу найдены следующие заметки: \n\n{data}\n')
    elif choice == 3:
        data = list(filter(lambda x: x['msg'] == search_data, data_list))
        if not data:
            print(f'\n\nДанных с таким id нет.\n\n')
        else:
            print(f'\n\nПо вашему запросу найдены следующие заметки: \n\n{data}\n')
    elif choice == 4:
        data = list(filter(lambda x: x['date'] == search_data, data_list))
        if not data:
            print(f'\n\nДанных с таким id нет.\n\n')
        else:
            print(f'\n\nПо вашему запросу найдены следующие заметки: \n\n{data}\n')


def delete_notice(data_list: list, key, value):
    """
    Удаляет заметку по id
    :param data_list: принимает список словарей автоматом
    :param key: автоматом подсовывает id
    :param value: принимает на вход int номер id
    :return:
    """
    for index, dict_ in enumerate(data_list):
        if key in dict_ and dict_[key] == value:
            data_list.remove(dict_)
            print(f'Произведено удаление записи: {dict_}')
        rewrite_file(data_list)


def edit_notice(data_list: list, key, value):
    """
    Изменяет заметку по номеру id
    :param data_list: принимает список словарей автоматом
    :param key: автоматом подсовывает id
    :param value: принимает на вход int номер id
    :return:
    """
    for index, dict_ in enumerate(data_list):
        if key in dict_ and dict_[key] == value:
            new_title = ''
            new_msg = ''
            change_title = input(f'Хотите оставить название заметки: "{dict_.get("title")}" или поменять?\n'
                                 f'1 - Поменять\n'
                                 f'2 - Оставить\n')
            if change_title == '1':
                new_title = input(f'Введите новое название заметки: ')
            elif change_title == '2':
                new_title = dict_.get('title')
            else:
                print('\nВведено неверное значение!\n')
            change_msg = input(f'Хотите оставить текст заметки: "{dict_.get("msg")}" или поменять?\n'
                               f'1 - Поменять\n'
                               f'2 - Оставить\n')
            if change_msg == '1':
                new_msg = input(f'Введите новое название заметки: ')
            elif change_msg == '2':
                new_msg = dict_.get('msg')
            else:
                print('\nВведено неверное значение!\n')
            data_list[index] = {
                'id': value,
                'title': new_title,
                'msg': new_msg,
                'date': datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            }
            print(f'Произведено изменение заметки с {dict_} на {data_list[index]}')
    rewrite_file(data_list)
