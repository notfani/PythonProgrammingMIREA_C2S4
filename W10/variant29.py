import sys
from datetime import datetime


def remove_duplicate_columns(table):
    seen = []
    unique_cols = []
    for col_idx in range(len(table[0])):
        column = [row[col_idx] for row in table]
        if column not in seen:
            seen.append(column)
            unique_cols.append(column)
    return list(map(list, zip(*unique_cols)))


def get_columns(table):
    return list(zip(*table))


def remove_empty_columns(table):
    columns = get_columns(table)
    non_empty = []
    for col in columns:
        if any(cell is not None for cell in col):
            non_empty.append(col)
    if non_empty:
        return [list(col) for col in zip(*non_empty)]
    return table


def remove_duplicate_rows(table):
    seen = []
    for row in table:
        if row not in seen:
            seen.append(row)
    return seen


def split_cell(cell):
    if not cell:
        return None, None
    parts = cell.split("&")
    if len(parts) == 2:
        return parts[0], parts[1]
    return None, None


def split_first_column(table):
    new_table = []
    for row in table:
        # Получаем value и date из первого столбца.
        value, date = split_cell(row[0])
        # Берем email из второго столбца, если он есть.
        email = row[1] if len(row) > 1 else None
        new_table.append([date, email, value])
    return new_table


def is_date_format(cell):
    if not cell or len(cell) != 10 or "." not in cell:
        return False
    return all(part.isdigit() for part in cell.split("."))


def process_date(cell):
    year, month, day = cell.split(".")
    return f"{day}/{month}/{year}"


def process_cell(cell):
    if cell is None:
        return None

    if is_date_format(cell):
        return process_date(cell)

    if "@" in cell:
        return cell.replace("@", "[at]")

    try:
        num = float(cell)
        return f"{round(num * 100)}%"
    except ValueError:
        return cell


def process_cells(table):
    return [[process_cell(cell) for cell in row] for row in table]


def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%d/%m/%Y")
    except Exception:
        return datetime.min


def transform_table(table):
    table = remove_duplicate_columns(table)
    table = remove_empty_columns(table)
    table = remove_duplicate_rows(table)
    table = split_first_column(table)
    table = process_cells(table)

    # Сортировка по email (второй столбец) — от А до Я
    table = sorted(table, key=lambda row: row[1] or '')

    return table


def parse_table_data(data):
    if not data:
        return data

    if isinstance(data[0], list):
        return data
    if isinstance(data[0], str):
        return [item.split(",") for item in data]
    raise ValueError("Неверный формат входных данных")


def main(table_data=None):
    table = parse_table_data(table_data) if table_data is not None else [
        ['0.4067&2000.03.08', 'vaceslav57@yahoo.com', None, None,
         'vaceslav57@yahoo.com'],
        ['0.9690&2004.05.02', 'keganz7@rambler.ru', None, None,
         'keganz7@rambler.ru'],
        ['0.0476&2002.11.02', 'miroslav4@gmail.com', None, None,
         'miroslav4@gmail.com'],
        ['0.0476&2002.11.02', 'miroslav4@gmail.com', None, None,
         'miroslav4@gmail.com'],
        ['0.0476&2002.11.02', 'miroslav4@gmail.com', None, None,
         'miroslav4@gmail.com'],
        ['0.8717&2002.02.17', 'tosumskij82@mail.ru', None, None,
         'tosumskij82@mail.ru']
    ]
    result = transform_table(table)

    # Разделяем столбцы
    dates = [row[0] for row in result]
    emails = [row[1] for row in result]
    percents = [row[2] for row in result]

    output = [dates, emails, percents]

    return output


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        main()
