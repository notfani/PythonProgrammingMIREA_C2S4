from decimal import Decimal, getcontext

getcontext().prec = 10


def main(z, y):

    n = len(z)
    result = Decimal(0)

    for i in range(1, n + 1):
        index_z = n - 1 - ((i - 1) // 2)
        index_y = min((i - 1) // 4, len(y) - 1)

        term = (Decimal(83) * Decimal(z[index_z]) ** 3
                + Decimal(54) + Decimal(y[index_y])) ** 3
        result += term

    return float(result)


if __name__ == "__main__":
    z_values = [0.98, -0.26, 0.4, -0.33, 0.87]
    y_values = [0.43, 0.9, -0.05, -0.58, -0.82]

    result = main(z_values, y_values)
    print(f"Результат: {result:.2e}")
