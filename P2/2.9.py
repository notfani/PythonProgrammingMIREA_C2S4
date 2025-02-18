from typing import List, Dict

def reverse_list_to_string(lst: List[int]) -> str:
    """Переворачивает список и возвращает строку из элементов, разделенных пробелом."""
    reversed_list = lst[::-1]
    return ' '.join(map(str, reversed_list))


def char_count(s: str, char: str) -> int:
    """Подсчитывает количество вхождений символа в строке, игнорируя регистр."""
    return s.lower().count(char.lower())


def count_characters(s: str) -> Dict[str, int]:
    """Возвращает словарь с частотами символов в строке, игнорируя регистр и пробелы."""
    s = s.replace(" ", "").lower()  # Убираем пробелы и приводим к нижнему регистру
    unique_chars = set(s)  # Находим уникальные символы
    return {char: char_count(s, char) for char in unique_chars}


if __name__ == "__main__":
    # 8-е задание: переворот списка в строку
    sample_list = [1, 2, 3, 4, 5]
    reversed_string = reverse_list_to_string(sample_list)
    print("Перевернутая строка:", reversed_string)

    # 9-е задание: подсчет символов
    char_freq = count_characters(reversed_string)
    print("Частота символов:", char_freq)
