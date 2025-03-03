import sys

def my_print(*args, sep=' ', end='\n', file=sys.stdout):
    # Преобразуем все аргументы в строки
    output = sep.join(map(str, args))
    # Используем sys.stdout.write для вывода
    file.write(output + end)

# Пример использования
my_print("Hello", "world!", 123)
my_print("This", "is", "a", "test", sep='-', end='!\n')
