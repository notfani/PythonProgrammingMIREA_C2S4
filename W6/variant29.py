def compute_set_I(input_set):
    """Формирует множество set_I."""
    return {abs(k) + 4 * k for k in input_set if k <= 65}


def compute_set_Delta(input_set):
    """Формирует множество set_Delta с использованием XOR (^)."""
    return {
        4 * k + k % 3
        for k in input_set
        if (k <= -16) ^ (k >= -95)
    }


def compute_set_Z(set_I, set_Delta):
    """Формирует множество set_Z."""
    return {
        delta * i
        for i in set_I
        for delta in set_Delta
        if delta >= i
    }


def compute_sum_I(set_I):
    """Вычисляет сумму элементов множества set_I."""
    return sum(abs(i) for i in set_I)


def compute_sum_Z(pairs):
    """Вычисляет сумму элементов (i + ζ) для всех пар (i, ζ)."""
    return sum(prod for _, _, prod in pairs) if pairs else 0


def compute_pairs(set_I, set_Z):
    """Генерирует пары (i, z) и их произведения (i + z)."""
    return [
        (i, z, i + z)
        for i in set_I
        for z in set_Z
    ]


def compute_nu(input_set):
    # Формирование множеств
    set_I = compute_set_I(input_set)
    print(f"Set I: {set_I}")

    set_Delta = compute_set_Delta(input_set)
    print(f"Set Delta: {set_Delta}")

    set_Z = compute_set_Z(set_I, set_Delta)
    print(f"Set Z: {set_Z}")

    # Вычисление сумм
    sum_I = compute_sum_I(set_I)

    pairs = compute_pairs(set_I, set_Z)
    for i, z, prod in pairs[:10]:  # Выводим только первые 10 пар
        print(f"Pair: ({i}, {z}) -> {prod}")

    sum_Z = compute_sum_Z(pairs)

    # Вычисление ν
    return sum_I - sum_Z


def main():
    try:
        # Чтение данных с клавиатуры
        input_data = input("Введите множество чисел через пробел: ")
        input_set = set(map(int, input_data.split()))
        result = compute_nu(input_set)
        print("Результат вычислений:", result)
    except ValueError:
        print("Ошибка: введите только целые числа через пробел.")


# Точка входа для выполнения
if __name__ == "__main__":
    main()