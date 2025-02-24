import math


def main(n: int) -> float:
    if n == 0:
        return -0.17
    elif n == 1:
        return -0.64
    elif n >= 2:
        return 91 * main(n - 2) - math.atan(44 * (main(n - 1) ** 2)) ** 2
    else:
        return -1


if __name__ == "__main__":
    n = int(input("Введите n: "))
    print(f"main({n}) ≈ {main(n):.2e}")
