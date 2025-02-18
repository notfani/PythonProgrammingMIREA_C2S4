def compute_function(n: int, m: int, a: int) -> float:
    result = 1
    for c in range(1, a + 1):
        product_m = 1
        for j in range(1, m + 1):
            summation_n = 0
            for i in range(1, n + 1):
                term1 = ((28 * c ** 2) ** 6 / 5)
                term2 = 16 * ((j ** 3 / 44) + i ** 2) ** 5
                summation_n += term1 + term2
            product_m *= summation_n
        result *= product_m
    return result


if __name__ == "__main__":
    n, m, a = 4, 2, 8
    result = compute_function(n, m, a)
    print(f"Result: {result}")