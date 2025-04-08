class MyHashTable:
    def __init__(self):
        self.table = []  # Внутренний список для хранения пар ключ-значение

    def __setitem__(self, key, value):
        # Проверяем, существует ли уже ключ
        for i, (k, v) in enumerate(self.table):
            if k == key:
                self.table[i] = (key, value)  # Обновляем значение
                return
        # Если ключ не найден, добавляем новую пару
        self.table.append((key, value))

    def __getitem__(self, key):
        # Ищем ключ в таблице
        for k, v in self.table:
            if k == key:
                return v
        # Если ключ не найден, выбрасываем исключение KeyError
        raise KeyError(f"Key {key} not found.")

    def __len__(self):
        return len(self.table)  # Возвращаем количество пар ключ-значение

# Пример использования
if __name__ == "__main__":
    hash_table = MyHashTable()
    hash_table['apple'] = 1
    hash_table['banana'] = 2
    hash_table['orange'] = 3

    print(hash_table['apple'])  # Вывод: 1
    print(len(hash_table))  # Вывод: 3

    try:
        print(hash_table['grape'])  # Это вызовет KeyError
    except KeyError as e:
        print(e)  # Вывод: Key grape not found.
