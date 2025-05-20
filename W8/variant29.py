def validate_and_pack(field_name, value, bit_length, shift):
    max_value = (1 << bit_length) - 1
    value &= max_value
    return value << shift


def process_fields(fields):
    result = 0

    for name, value in fields:
        if name == 'D1':
            result |= validate_and_pack('D1', value, bit_length=7, shift=0)
        elif name == 'D2':
            result |= validate_and_pack('D2', value, bit_length=4, shift=7)
        elif name == 'D3':
            result |= validate_and_pack('D3', value, bit_length=6, shift=11)
        elif name == 'D4':
            result |= validate_and_pack('D4', value, bit_length=10, shift=17)
        else:
            raise ValueError(f"Неизвестное имя поля: {name}")

    return result


def main(*args):

    for fields in args:
        try:
            packed_value = process_fields(fields)
            results = hex(packed_value)
        except ValueError as e:
            print(f"Ошибка при обработке данных {fields}: {e}")
            results = None

    return results


# Тестирование программы
if __name__ == "__main__":
    # Тестовые данные
    test_data_1 = [
        ('D1', 36),
        ('D2', 13),
        ('D3', 56),
        ('D4', 302)
    ]
    test_data_2 = [
        ('D1', 111),
        ('D2', 11),
        ('D3', 43),
        ('D4', 225)
    ]
    test_data_3 = [
        ('D1', 79),
        ('D2', 11),
        ('D3', 51),
        ('D4', 5)
    ]
    test_data_4 = [
        ('D1', 123),
        ('D2', 0),
        ('D3', 11),
        ('D4', 165)
    ]
    test_data_5 = [
        ('D1', 0),
        ('D2', 0),
        ('D3', 0),
        ('D4', 0)
    ]

    # Вызов функции с несколькими массивами
    output = main(
        test_data_1,
        test_data_2,
        test_data_3,
        test_data_4,
        test_data_5
    )

    print("Результаты:")
    for i, result in enumerate(output, start=1):
        print(f"Массив {i}: {result}")
