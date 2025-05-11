def find_word(text, word):
    """
    Находит все индексы вхождений слова в строку.

    Аргументы:
    text (str): Строка, в которой производится поиск.
    word (str): Слово, которое нужно найти.

    Возвращает:
    list: Список индексов каждого вхождения слова в строку. Если слово не найдено, возвращается пустой список.

    Примеры:
    >>> find_word("hello world world", "world")
    [6, 12]

    >>> find_word("hello world", "planet")
    []

    >>> find_word("the quick brown fox quick", "quick")
    [4, 20]

    >>> find_word("", "test")
    []

    >>> find_word("test", "")
    []

    >>> find_word("case sensitive", "Sensitive")
    []
    """
    if not isinstance(text, str) or not isinstance(word, str):
        raise ValueError("Оба аргумента должны быть строками.")

    if word == "":
        return []

    indices = []
    start = 0
    while True:
        index = text.find(word, start)
        if index == -1:
            break
        indices.append(index)
        start = index + 1  # Увеличиваем start только на 1

    return indices


# Тестирование функции с помощью doctest
if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)