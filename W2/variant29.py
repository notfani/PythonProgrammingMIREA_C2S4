import math


def main(x: float) -> float:
    if x < 135:
        return math.log2(90 * x**3) ** 3 + 10
    elif 135 <= x < 225:
        return (abs(x) ** 6) / 62
    else:
        return x**2 + 73 * (abs(x) ** 6) + x


if __name__ == "__main__":
    x = float(input("Введите x: "))
    print(f"main({x}) = {main(x):.2e}")
