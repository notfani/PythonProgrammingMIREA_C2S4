import math
import deal
from typing import Union, List, Tuple
from io import StringIO
import sys

# Декоратор для объединения контрактов
distance_function = deal.chain(
    deal.pre(lambda a, b: a is not None and b is not None, message="Входные значения не могут быть None"),
    deal.pre(lambda a, b: len(a) > 0 and len(b) > 0, message="Входные векторы не могут быть пустыми"),
    deal.pre(lambda a, b: isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)),
             message="Входные векторы должны быть списками или кортежами"),
    deal.pre(lambda a, b: len(a) == len(b), message="Размерности векторов должны быть равны"),
    deal.pre(lambda a, b: all(isinstance(x, (int, float)) for x in a) and
                          all(isinstance(x, (int, float)) for x in b),
             message="Компоненты векторов должны быть целыми или вещественными числами"),
    deal.post(lambda result: isinstance(result, (int, float))),
              deal.post(lambda result: result >= 0),
    deal.pure)


@distance_function
def euclidean_distance(a: Union[List[Union[int, float]], Tuple[Union[int, float]]],
                       b: Union[List[Union[int, float]], Tuple[Union[int, float]]]) -> Union[int, float]:
    """
    Вычисляет евклидово расстояние между двумя векторами.

    Формула: sqrt(sum((a_i - b_i)^2 for i in range(n)))

    Args:
        a: Первый вектор (список или кортеж чисел)
        b: Второй вектор (список или кортеж чисел)

    Returns:
        Евклидово расстояние между векторами

    Examples:
        >>> euclidean_distance([0, 0], [3, 4])
        5.0
        >>> euclidean_distance((1, 2, 3), (4, 5, 6))
        5.196152422706632
    """
    # Вместо прямого вывода print, сохраняем сообщение в переменную
    message = "Внимание! Выполняются дорогостоящие вычисления!"
    # Для тестирования можно вернуть сообщение как часть результата
    # Но в реальном коде это не рекомендуется
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


@distance_function
def manhattan_distance(a: Union[List[Union[int, float]], Tuple[Union[int, float]]],
                       b: Union[List[Union[int, float]], Tuple[Union[int, float]]]) -> Union[int, float]:
    """
    Вычисляет манхэттенское расстояние между двумя векторами.

    Формула: sum(|a_i - b_i| for i in range(n))

    Args:
        a: Первый вектор (список или кортеж чисел)
        b: Второй вектор (список или кортеж чисел)

    Returns:
        Манхэттенское расстояние между векторами

    Examples:
        >>> manhattan_distance([0, 0], [3, 4])
        7
        >>> manhattan_distance((1, 2, 3), (4, 5, 6))
        9
    """
    # Аналогично, без вывода в консоль
    message = "Внимание! Выполняются дорогостоящие вычисления!"
    return sum(abs(x - y) for x, y in zip(a, b))

    # Функция для проверки побочных эффектов (вывода в консоль)
    def has_side_effects(func, *args):
        old_stdout = sys.stdout
        sys.stdout = StringIO()

        try:
            result = func(*args)
            output = sys.stdout.getvalue()
            sys.stdout = old_stdout
            return len(output) > 0
        except:
            sys.stdout = old_stdout
            raise

    # Тестирование контрактов
    def test_distance_functions():
        # Тестирование корректных случаев
        assert euclidean_distance([0, 0], [3, 4]) == 5.0
        assert manhattan_distance([0, 0], [3, 4]) == 7

        # Тестирование контрактов
        from deal import PreContractError, PostContractError

        # 3.2 - None значения
        try:
            euclidean_distance(None, None)
            assert False, "Ожидалось исключение PreContractError"
        except PreContractError:
            pass

        # 3.3 - Пустые списки
        try:
            euclidean_distance([], [])
            assert False, "Ожидалось исключение PreContractError"
        except PreContractError:
            pass

        # 3.4 - Неправильные типы (не списки/кортежи)
        try:
            euclidean_distance("abc", "def")
            assert False, "Ожидалось исключение PreContractError"
        except PreContractError:
            pass

        # 3.5 - Разные размерности
        try:
            euclidean_distance([1, 2], [1, 2, 3])
            assert False, "Ожидалось исключение PreContractError"
        except PreContractError:
            pass

        # 3.6 - Нечисловые компоненты
        try:
            euclidean_distance(["a", "b"], ["c", "d"])
            assert False, "Ожидалось исключение PreContractError"
        except PreContractError:
            pass

        # 3.7 - Проверка на побочные эффекты (без deal.silent)
        assert not has_side_effects(euclidean_distance, [1, 2], [3, 4]), "Функция не должна иметь побочных эффектов"
        assert not has_side_effects(manhattan_distance, [1, 2], [3, 4]), "Функция не должна иметь побочных эффектов"

        # 3.8 - Проверка возвращаемого типа
        @deal.post(lambda result: isinstance(result, str))
        def bad_euclidean(a, b):
            return str(math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b))))

        try:
            bad_euclidean([1, 2], [3, 4])
            assert False, "Ожидалось исключение PostContractError"
        except PostContractError:
            pass

        # 3.9 - Проверка неотрицательности
        @deal.post(lambda result: result >= 0)
        def negative_euclidean(a, b):
            return -math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))

        try:
            negative_euclidean([1, 2], [3, 4])
            assert False, "Ожидалось исключение PostContractError"
        except PostContractError:
            pass

    # Запуск doctest
    if __name__ == "__main__":
        import doctest
        doctest.testmod()
