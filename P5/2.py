def main(fields):
    # Добавляем поля
    V1, V2, V3, V4, V5, V6 = fields
    value = ((V6 << 24) | (V5 << 23) | (V4 << 19) | (V3 << 18) | (V2 << 9) | V1)
    return value

# Тесты
print(main((376, 159, 1, 0, 1, 21)))
print(main((130, 60, 1, 11, 1, 52)))
print(main((396, 444, 0, 14, 0, 33)))
print(main((110, 199, 1, 12, 0, 27)))