import json


def save_file(data):
    """
    Записывает данные формата json в json файл.
    :param data: Данные типа dict
    :return: записывает в формат *.json значения (в одну строрку)
    """
    try:
        temporary_data = json.load(open('notes.json', encoding='utf-8'))
    except FileNotFoundError:
        temporary_data = []

    temporary_data.append(data)

    with open('notes.json', 'w', encoding='utf-8') as file:
        json.dump(temporary_data, file, indent=2, ensure_ascii=False)


def rewrite_file(data):
    """
    Перезаписывает данные формата json в файле.
    :param data: Данные типа dict
    :return: записывает в формат *.json значения (в одну строрку)
    """
    with open('notes.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def load_file(open_file='notes.json'):
    """
    Читает данные формата json
    :param open_file: Открывает имеющийся файл json
    :return: записывает в формат *.json значения (в одну строрку)
    """
    with open(f'{open_file}', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        result = []
        for i in data:
            result.append(i)
        return result
