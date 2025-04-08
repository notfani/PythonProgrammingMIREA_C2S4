class A:
    pass

class B(A):
    pass

class C(B):
    pass

def get_inheritance(cls):
    return ' -> '.join(c.__name__ for c in cls.__mro__)

# Пример использования для класса OSError
import os  # Импортируем модуль os для доступа к OSError
print(get_inheritance(OSError))  # Вывод иерархии наследования для OSError

# Пример использования для ваших классов
print(get_inheritance(C))  # Вывод иерархии наследования для класса C
