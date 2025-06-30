import json
from core.monitor import get_system_stats
import os

def write_file_from_dict(dictionary, file_name):
    """Записывает словарь в JSON-файл."""
    if not isinstance(dictionary, list):
        dictionary = [dictionary]
    file_path = os.path.join('data', file_name)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(dictionary, file, ensure_ascii=False, indent=4)

def read_json_file(file_name):
    """Читает JSON-файл. Если файла нет или он пустой, возвращает пустой список."""
    file_path = os.path.join('data', file_name)
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        return []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []  # Если файл повреждён, возвращаем пустой список


if __name__ == '__main__':
    write_file_from_dict(get_system_stats(), 'data.json')
    r = read_json_file('data.json')
    print(r)