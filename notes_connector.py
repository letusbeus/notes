from save_read_file import save_file
from user_commands import create_new_note, show_all_notice, search_notice, delete_notice, edit_notice
import json


def start_note():
    """
    Исполнительный метод - коннектор модулей,
    реализует функционал:
    1) Создание заметки
    2) Выход из программы
    3) Показывает все заметки
    4) Поиск по заметкам
    5) Удаление заметки по id
    6) Изменение заметки по id
    :return:
    """
    print('*** Добро пожаловать в програму заметки! *** \n')
    while True:
        program = input(str(f'{"-" * 10} Что вы хотите сделать? {"-" * 10}\n'
                            '1 - Создать новую заметку\n'
                            '2 - Выйти\n'
                            '3 - Показать все заметки\n'
                            '4 - Найти заметку\n'
                            '5 - Удалить заметку\n'
                            '6 - Изменить заметку\n'))
        menu = {
            '1': 'start',
            '2': 'quit',
            '3': 'show_all',
            '4': 'search',
            '5': 'delete',
            '6': 'edit'
        }
        try:
            program = menu[program]
            if program == 'quit':
                exit(0)
            elif program == 'start':
                start = create_new_note()
                save_file(start)
                print('Заметка успешно сохранена!')
            elif program == 'show_all':
                show_all_notice()
            elif program == 'search':
                choice = input(f'{"-" * 15}Выберите поле для поиска:{"-" * 15}\n'
                               f'1 - Поиск по id\n'
                               f'2 - Поиск по Теме\n'
                               f'3 - Поиск по сообщению в заметке\n'
                               f'4 - Поиск по дате и времени\n'
                               f'Вводите сюда --->: ')

                search_type = {
                    '1': 'id',
                    '2': 'title',
                    '3': 'msg',
                    '4': 'data'
                }
                try:
                    choice = search_type[choice]
                    temp_list = json.load(open('notes.json', encoding='utf-8'))
                    if choice == 'id':
                        search = int(input('Введите id для поиска заметки (Например: 1):'))
                        search_notice(temp_list, search, 1)
                    elif choice == 'title':
                        search = str(input('Введите "Тему заметки" для поиска (Например: Понедельник):'))
                        search_notice(temp_list, search, 2)
                    elif choice == 'msg':
                        search = str(input('Введите "Текст заметки" для поиска (Например: Сегодня солнечно):'))
                        search_notice(temp_list, search, 3)
                    elif choice == 'data':
                        search = str(input('Введите "Полную дату" для поиска (Например: 06-02-2023 18:23:59):'))
                        search_notice(temp_list, search, 4)
                except FileNotFoundError:
                    print(f'Вы еще не создали ни одной заметки!')
            elif program == 'delete':
                temp_list = json.load(open('notes.json', encoding='utf-8'))
                print('Заметки которые вы создали:')
                show_all_notice()
                notice_val = int(input(f'\nВведите id заметки, которую хотите удалить: '))
                delete_notice(temp_list, 'id', notice_val)
            elif program == 'edit':
                temp_list = json.load(open('notes.json', encoding='utf-8'))
                print('Заметки которые вы создали:')
                show_all_notice()
                notice_val = int(input(f'\nВведите id заметки, которую хотите изменить: '))
                edit_notice(temp_list, 'id', notice_val)
        except KeyError:
            print('Введено неверное значение, возврат в меню!')
