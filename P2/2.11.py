import timeit
import random
import string

try:
    from Levenshtein import distance as levenshtein_lib
    lib_available = True
except ImportError:
    lib_available = False
    print("Библиотека python-Levenshtein не установлена. Установите её командой: pip install python-Levenshtein")


def levenshtein_recursive(a: str, b: str, memo=None) -> int:
    """Рекурсивная реализация с мемоизацией."""
    if memo is None:
        memo = {}

    if (a, b) in memo:
        return memo[(a, b)]

    if not a:
        return len(b)
    if not b:
        return len(a)

    if a[-1] == b[-1]:
        cost = 0
    else:
        cost = 1

    res = min(
        levenshtein_recursive(a[:-1], b, memo) + 1,   # Удаление
        levenshtein_recursive(a, b[:-1], memo) + 1,   # Вставка
        levenshtein_recursive(a[:-1], b[:-1], memo) + cost  # Замена
    )

    memo[(a, b)] = res
    return res


def levenshtein_iterative(a: str, b: str) -> int:
    """Итеративная реализация с динамическим программированием."""
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]


def generate_random_string(length):
    """Генерирует случайную строку заданной длины."""
    return ''.join(random.choices(string.ascii_letters, k=length))


# Тестируем на строках разной длины
lengths = [5, 10, 50]
test_cases = [(generate_random_string(n), generate_random_string(n)) for n in lengths]

print("Сравнение производительности (в секундах):\n")

for a, b in test_cases:
    print(f"Длина строк: {len(a)}")

    time_recursive = timeit.timeit(lambda: levenshtein_recursive(a, b), number=1)
    time_iterative = timeit.timeit(lambda: levenshtein_iterative(a, b), number=10) / 10
    time_lib = timeit.timeit(lambda: levenshtein_lib(a, b), number=100) / 100 if lib_available else None

    print(f"  - Рекурсивный алгоритм: {time_recursive:.6f} сек")
    print(f"  - Итеративный алгоритм: {time_iterative:.6f} сек")
    if lib_available:
        print(f"  - Библиотечный алгоритм: {time_lib:.6f} сек")
    print("-" * 40)
