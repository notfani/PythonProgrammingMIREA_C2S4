def compute_nu(k_values):
    """
    Вычисляет значение ν на основе заданного множества k_values.
    """

    def compute_i_set(values):
        return {abs(k) + 4 * k for k in values if k <= 65}

    def compute_delta_set(values):
        return {4 * k + k % 3 for k in values if (k <= -16) ^ (k >= -95)}

    def compute_z_set(i_set, delta_set):
        return {delta * i for i in i_set for delta in delta_set if delta >= i}

    i_set = compute_i_set(k_values)
    print(f"I: {i_set}")

    delta_set = compute_delta_set(k_values)
    print(f"Delta: {delta_set}")

    z_set = compute_z_set(i_set, delta_set)
    print(f"Z: {z_set}")

    sum_i = sum(abs(i) for i in i_set)
    pairs = [(i, z, i + z) for i in i_set for z in z_set]

    for i, z, sum_val in pairs[:10]:  # Выводим только первые 10 пар
        print(f"Пара: ({i}, {z}) -> {sum_val}")

    sum_z = sum(sum_val for _, _, sum_val in pairs) if z_set else 0
    return sum_i - sum_z


if __name__ == "__main__":
    try:
        def read_input():
            return set(
                map(int, input("Введите множество чисел через пробел: ").split())
            )


        k_values = read_input()
        print("Результат вычислений:", compute_nu(k_values))
    except ValueError:
        print("Ошибка: введите только целые числа через пробел.")
