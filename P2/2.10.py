def levenshtein_distance(a: str, b: str, memo=None) -> int:
    """Вычисляет расстояние Левенштейна между двумя строками рекурсивно."""
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
        levenshtein_distance(a[:-1], b, memo) + 1,    # Удаление
        levenshtein_distance(a, b[:-1], memo) + 1,    # Вставка
        levenshtein_distance(a[:-1], b[:-1], memo) + cost  # Замена
    )

    memo[(a, b)] = res
    return res

# Тестируем на примерах из задания
pairs = [
    ("Hello, world!", "Goodbye, world!"),
    ("Hello, world!", "Bye, world!"),
    ("I love Python", "I like Python"),
    ("100101", "100011")
]

for s1, s2 in pairs:
    print(f"Левенштейново расстояние между '{s1}' и '{s2}': {levenshtein_distance(s1, s2)}")