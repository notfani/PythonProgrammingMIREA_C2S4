import re


def parse_data_string(input_str):
    # Регулярное выражение для извлечения записей
    entry_pattern = r'<data>\s*set\s*@"([^"]+)"\s*=\s*(-?\d+)\s*</data>'

    # Найти все записи
    entries = re.findall(entry_pattern, input_str)

    # Преобразовать результат в словарь
    result = {name: int(value) for name, value in entries}

    return result


# Пример использования
input_str_1 = '[ <data> set @"arerre_209" =-4948 </data><data>set @"zaen" = -5816 </data> ]'
input_str_2 = '[<data>set @"este_583" = 5840 </data> <data> set @"usbear" = -2370 </data> <data>set @"arso_10" = -1480 </data><data>set @"vesobi"= 2526 </data> ]'

print(parse_data_string(input_str_1))
print(parse_data_string(input_str_2))