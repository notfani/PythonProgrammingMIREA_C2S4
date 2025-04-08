import os
import sys

def is_python_module(filename: str) -> bool:
    """
    Проверяет, является ли файл Python-модулем (оканчивается на .py).
    """
    return filename.endswith('.py')

def print_module_tree(root: str, prefix: str = "") -> None:
    """
    Рекурсивно выводит дерево модулей (файлы .py и каталоги-пакеты) начиная с заданного пути.
    """
    # Получаем список элементов в текущем каталоге, сортируя для стабильного вывода
    try:
        items = sorted(os.listdir(root))
    except PermissionError:
        return

    # Фильтруем элементы, оставляем каталоги и Python файлы
    entries = []
    for item in items:
        full_path = os.path.join(root, item)
        if os.path.isdir(full_path):
            # Также можем анализировать и обычные каталоги, если в них есть .py файлы
            if any(is_python_module(f) for f in os.listdir(full_path)):
                entries.append(item)
        elif is_python_module(item):
            entries.append(item)

    count = len(entries)
    for index, entry in enumerate(entries):
        full_path = os.path.join(root, entry)
        connector = "└── " if index == count - 1 else "├── "
        print(prefix + connector + entry)
        if os.path.isdir(full_path):
            new_prefix = prefix + ("    " if index == count - 1 else "│   ")
            print_module_tree(full_path, new_prefix)

if __name__ == '__main__':
    project_path = "C:\\Users\\prime\\PycharmProjects\\PythonProgrammingMIREA_C2S4"

    if not os.path.exists(project_path):
        print(f"Путь {project_path} не существует.")
        sys.exit(1)

    # Выводим корневой каталог проекта
    print(os.path.basename(os.path.abspath(project_path)) + "/")
    print_module_tree(project_path)
