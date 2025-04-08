def decode_hex(hex_str):
    # Преобразуем шестнадцатеричную строку в целое число
    value = int(hex_str, 16)

    # Определяем маски для извлечения каждого битового поля
    mask_N1 = 0b111111  # 6 бит
    mask_N2 = 0b11111  # 5 бит
    mask_N3 = 0b1111111  # 7 бит
    mask_N4 = 0b11  # 2 бита
    mask_N5 = 0b111  # 3 бит

    # Извлекаем значения полей
    N1 = (value >> 0) & mask_N1
    N2 = (value >> 6) & mask_N2
    N3 = (value >> 12) & mask_N3
    N4 = (value >> 19) & mask_N4
    N5 = (value >> 21) & mask_N5

    return {'N1': N1, 'N2': N2, 'N3': N3, 'N4': N4, 'N5': N5}


# Тесты
print(decode_hex('0xb9a562'))
print(decode_hex('0x85c1a5'))
print(decode_hex('0xe3fb96'))
print(decode_hex('0x2909e9'))