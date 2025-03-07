### 1. Импортирование библиотек
В данном коде не используются внешние библиотеки, поэтому этот шаг пропускаем.

### 2. Определение класса Room

```python
class Room:
    def __init__(self, title, description, actions):
        self.title = title
        self.description = description
        self.actions = actions
```

- **Класс Room**: Этот класс представляет комнату в игре. Он имеет три атрибута:
  - `title`: название комнаты.
  - `description`: текстовое описание комнаты, которое будет отображаться игроку.
  - `actions`: список действий, которые игрок может выполнить в этой комнате. Каждое действие представлено как словарь с описанием и меткой следующей комнаты.

### 3. Метод display

```python
    def display(self):
        print(f"{self.title}\n{self.description}")
        for i, action in enumerate(self.actions, 1):
            print(f"{i}. {action['description']}")
        print("> ", end='')
```

- **Метод display**: Этот метод отвечает за отображение информации о комнате. Он выводит название и описание комнаты, а затем перечисляет доступные действия с их номерами. 
- `enumerate(self.actions, 1)`: Используется для перебора списка действий, начиная с 1, чтобы нумерация была удобной для игрока.

### 4. Функция main

```python
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
        ...
        'end': Room(
            title="Конец игры",
            description="Поздравляем! Вы выбрались из лабиринта.",
            actions=[]
        ),
    }
```

- **Функция main**: Это основная функция, которая запускает игру.
- **Словарь rooms**: Здесь мы создаем словарь, где ключи — это метки комнат (например, `'start'`, `'room_2'`), а значения — экземпляры класса `Room`. Каждая комната имеет свое название, описание и список действий.

### 5. Цикл игры

```python
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
```

- **Переменная current_room**: Изначально устанавливается на `'start'`, что означает, что игра начинается с первой комнаты.
- **Цикл while True**: Этот бесконечный цикл будет продолжаться, пока игрок не выйдет из игры.
  - `room = rooms[current_room]`: Получаем текущую комнату по метке.
  - `room.display()`: Вызываем метод display для отображения информации о текущей комнате.
  - `if not room.actions: break`: Если в текущей комнате нет доступных действий, игра заканчивается.
  - `choice = input()`: Запрашиваем у игрока ввод.
  - `try` блок: Пытаемся преобразовать ввод в индекс и получить следующую комнату. Если ввод некорректен (например, не число или номер действия вне диапазона), программа выдает сообщение об ошибке.

### 6. Запуск игры

```python
if __name__ == "__main__":
    main()
```

- Этот блок кода проверяет, запущен ли скрипт напрямую. Если да, то вызывается функция `main()`, и игра начинается.