import random

first_names = [
    "Алексей", "Иван", "Дмитрий", "Максим", "Роман", "Тимур", "Тамерлан", "Святослав", "Герман", "Николай",
    "Данила", "Лев", "Ильдар", "Самир", "Назар", "Степан", "Леонид", "Семен"
]

last_name_prefixes = ["Фу", "Феца", "Шоло", "Тача", "Муго", "Таб", "Чере", "Тифом", "Гуз", "Наб", "Семи", "Баш", "Куна", "Гид", "Саб"]
last_name_suffixes = ["ций", "чли", "дяк", "сяк", "дич", "ян", "в", "ский", "ц", "янц", "ин", "ий"]

initials = "АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЭЮЯ"

def generate_fio():
    first_name = random.choice(first_names)
    initial = random.choice(initials) + "."
    last_name = random.choice(last_name_prefixes) + random.choice(last_name_suffixes)
    return f"{first_name} {initial} {last_name}"

def generate_fio_list(count=10):
    return [generate_fio() for _ in range(count)]

if __name__ == "__main__":
    for fio in generate_fio_list(10):
        print(fio)
