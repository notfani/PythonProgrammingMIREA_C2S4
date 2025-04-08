def main(hex_string):
    # Преобразуем шестнадцатеричную строку в число
    value = int(hex_string, 16)
    # Определяем маски и сдвиги для каждого поля
    fields = [
        ('R1', 0xF, 0),    
        ('R2', 0x1FF, 4),  
        ('R3', 0x7, 13),  
        ('R4', 0x7, 16),  
        ('R5', 0x1F, 19)  
    ]
    result = []
    for name, mask, shift in fields:
        # Применяем делаем сдвиг и применяем маску
        field_value = (value >> shift) & mask
        # Добавляем результат
        result.append((name, str(field_value)))
    return result
# Тесты
print(main('0x6a9f6'))    
print(main('0x2464d1'))  
print(main('0x18ba48b')) 
print(main('0xb077e5'))