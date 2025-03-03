def matrix_division(A, B):
    # Получаем размеры матриц
    rows_A = len(A)
    cols_A = len(A[0]) if rows_A > 0 else 0
    rows_B = len(B)
    cols_B = len(B[0]) if rows_B > 0 else 0

    # Проверяем, можно ли перемножить матрицы
    if cols_A != rows_B:
        raise ValueError("Количество столбцов в первой матрице должно быть равно количеству строк во второй матрице.")

    # Создаем результирующую матрицу с нулями
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Выполняем умножение матриц
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result

def input_matrix(rows, cols):
    matrix = []
    print(f"Введите элементы матрицы {rows}x{cols}:")
    for i in range(rows):
        row = list(map(int, input(f"Строка {i + 1}: ").split()))
        if len(row) != cols:
            raise ValueError(f"Количество элементов в строке должно быть равно {cols}.")
        matrix.append(row)
    return matrix

def main():
    # Ввод размеров первой матрицы
    rows_A = int(input("Введите количество строк в первой матрице: "))
    cols_A = int(input("Введите количество столбцов в первой матрице: "))
    A = input_matrix(rows_A, cols_A)

    # Ввод размеров второй матрицы
    rows_B = int(input("Введите количество строк во второй матрице: "))
    cols_B = int(input("Введите количество столбцов во второй матрице: "))
    B = input_matrix(rows_B, cols_B)

    # Умножаем матрицы
    try:
        result = matrix_division(A, B)
        print("Результат произведения матриц:")
        for row in result:
            print(row)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
