def main(z, y) -> float:
    term1 = 14 - 48 * (y ** 3 - y ** 2 - z) ** 2
    numerator = (0.02 + z ** 2) ** 4 - (57 * z ** 2 + y + 1) ** 3
    denominator = (y ** 3 / 80 - z) ** 5
    result = term1 - numerator / denominator
    return result


if __name__ == "__main__":
    z = float(input())
    y = float(input())
    print(main(z, y))
