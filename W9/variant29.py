import re
import sys


def parse_string(data: str):
    # Убираем лишние пробелы и нормализуем конец строки
    data = data.replace('\n', ' ')

    # Гибкое регулярное выражение:
    pattern = r"do\s+equ\s*'([^']+)'\s*<-\s*#\s*(-?\d+);"

    matches = re.findall(pattern, data)
    return [(name, int(number)) for name, number in matches]


def main(input_string: str):
    return parse_string(input_string)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py \"input_string\"")
    else:
        result = main(sys.argv[1])
        print(result)
