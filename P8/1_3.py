from contextlib import contextmanager


@contextmanager
def raises(expected_exception):
    """
    Менеджер контекста, который проверяет, что внутри него возникает ожидаемое исключение.

    Аргументы:
    expected_exception (Exception): Ожидаемый тип исключения.

    Пример использования:
    >>> with raises(ZeroDivisionError):
    ...     1 / 0
    """
    try:
        # Передаём управление внутрь блока `with`
        yield
    except Exception as e:
        # Проверяем, что возникшее исключение соответствует ожидаемому
        if not isinstance(e, expected_exception):
            raise AssertionError(f"Expected {expected_exception}, but got {type(e)}")
    else:
        # Если исключение не возникло, вызываем ошибку
        raise AssertionError(f"{expected_exception} was not raised")


# Пример использования
if __name__ == "__main__":
    # Тест 1: Ожидается ZeroDivisionError
    try:
        with raises(ZeroDivisionError):
            1 / 0
        print("Test 1 passed")
    except AssertionError as e:
        print(f"Test 1 failed: {e}")

    # Тест 2: Ожидается ValueError, но возникает ZeroDivisionError
    try:
        with raises(ValueError):
            1 / 0
        print("Test 2 passed")
    except AssertionError as e:
        print(f"Test 2 failed: {e}")

    # Тест 3: Исключение не возникает
    try:
        with raises(ValueError):
            pass
        print("Test 3 passed")
    except AssertionError as e:
        print(f"Test 3 failed: {e}")