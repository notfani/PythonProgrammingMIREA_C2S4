class Room:
    def __init__(self, title, description, actions):
        self.title = title
        self.description = description
        self.actions = actions

    def display(self):
        print(f"{self.title}\n{self.description}")
        for i, action in enumerate(self.actions, 1):
            print(f"{i}. {action['description']}")
        print("> ", end='')

def main():
    # Определение комнат
    rooms = {
        'start': Room(
            title="Начало лабиринта",
            description="Вы в начале лабиринта. Сможете ли из него выбраться?",
            actions=[
                {'description': 'Проход на запад.', 'next_room': 'room_2'},
            ]
        ),
        'room_2': Room(
            title="Комната №2",
            description="Вы находитесь в комнате №2.",
            actions=[
                {'description': 'Проход на запад.', 'next_room': 'room_3'},
                {'description': 'Проход на восток.', 'next_room': 'start'},
            ]
        ),
        'room_3': Room(
            title="Комната №3",
            description="Вы находитесь в комнате №3.",
            actions=[
                {'description': 'Проход на север.', 'next_room': 'room_4'},
                {'description': 'Проход на восток.', 'next_room': 'room_2'},
            ]
        ),
        'room_4': Room(
            title="Комната №4",
            description="Вы находитесь в комнате №4. Здесь темно и страшно.",
            actions=[
                {'description': 'Вернуться на юг.', 'next_room': 'room_3'},
                {'description': 'Исследовать темноту.', 'next_room': 'room_5'},
            ]
        ),
        'room_5': Room(
            title="Комната №5",
            description="Вы нашли светильник! Теперь вы можете видеть.",
            actions=[
                {'description': 'Проход на восток.', 'next_room': 'room_6'},
                {'description': 'Вернуться на запад.', 'next_room': 'room_4'},
            ]
        ),
        'room_6': Room(
            title="Комната №6",
            description="Вы находитесь в комнате №6. Здесь много дверей.",
            actions=[
                {'description': 'Проход на юг.', 'next_room': 'room_7'},
                {'description': 'Проход на запад.', 'next_room': 'room_5'},
                {'description': 'Проход на север.', 'next_room': 'room_8'},
            ]
        ),
        'room_7': Room(
            title="Комната №7",
            description="Вы находитесь в комнате №7. Это выход!",
            actions=[
                {'description': 'Выбраться из лабиринта.', 'next_room': 'end'},
                {'description': 'Вернуться на север.', 'next_room': 'room_6'},
            ]
        ),
        'room_8': Room(
            title="Комната №8",
            description="Вы находитесь в комнате №8. Здесь есть загадка.",
            actions=[
                {'description': 'Решить загадку.', 'next_room': 'room_9'},
                {'description': 'Вернуться на юг.', 'next_room': 'room_6'},
            ]
        ),
        'room_9': Room(
            title="Комната №9",
            description="Вы находитесь в комнате №9. Загадка решена!",
            actions=[
                {'description': 'Проход на восток.', 'next_room': 'room_10'},
                {'description': 'Вернуться на запад.', 'next_room': 'room_8'},
            ]
        ),
        'room_10': Room(
            title="Комната №10",
            description="Вы находитесь в комнате №10. Здесь много сокровищ.",
            actions=[
                {'description': 'Собрать сокровища.', 'next_room': 'end'},
                {'description': 'Вернуться на запад.', 'next_room': 'room_9'},
            ]
        ),
        'end': Room(
            title="Конец игры",
            description="Поздравляем! Вы выбрались из лабиринта.",
            actions=[]
        ),
    }

    current_room = 'start'


    while True:
        room = rooms[current_room]
        room.display()

        if not room.actions:
            break

        choice = input()
        try:
            choice_index = int(choice) - 1
            next_room = room.actions[choice_index]['next_room']
            current_room = next_room
        except (ValueError, IndexError):
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()
