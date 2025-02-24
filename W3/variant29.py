import math


def main(n: int, a: int, p: float) -> float:
    result = 0
    for j in range(1, a + 1):
        for k in range(1, n + 1):
            term = (10 * (80 * k**2 - j**3 - p) ** 6) - (91 * math.cos(k) ** 7)
            result += term
    return result


if __name__ == "__main__":
    n = int(input("Введите n: "))
    a = int(input("Введите a: "))
    p = float(input("Введите p: "))
    print(f"main({n}, {a}, {p}) = {main(n, a, p):.2e}")
