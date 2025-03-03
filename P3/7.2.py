'''digraph G {
    start [label="Начало лабиринта"];
    room_2 [label="Комната №2"];
    room_3 [label="Комната №3"];
    room_4 [label="Комната №4"];
    room_5 [label="Комната №5"];
    room_6 [label="Комната №6"];
    room_7 [label="Комната №7"];
    room_8 [label="Комната №8"];
    room_9 [label="Комната №9"];
    room_10 [label="Комната №10"];
    end [label="Конец игры"];

    start -> room_2 [label="Проход на запад"];
    room_2 -> start [label="Проход на восток"];
    room_2 -> room_3 [label="Проход на запад"];
    room_3 -> room_2 [label="Проход на восток"];
    room_3 -> room_4 [label="Проход на север"];
    room_4 -> room_3 [label="Вернуться на юг"];
    room_4 -> room_5 [label="Исследовать темноту"];
    room_5 -> room_4 [label="Вернуться на запад"];
    room_5 -> room_6 [label="Проход на восток"];
    room_6 -> room_5 [label="Проход на запад"];
    room_6 -> room_7 [label="Проход на юг"];
    room_6 -> room_8 [label="Проход на север"];
    room_7 -> end [label="Выбраться из лабиринта"];
    room_7 -> room_6 [label="Вернуться на север"];
    room_8 -> room_6 [label="Вернуться на юг"];
    room_8 -> room_9 [label="Решить загадку"];
    room_9 -> room_8 [label="Вернуться на запад"];
    room_9 -> room_10 [label="Проход на восток"];
    room_10 -> end [label="Собрать сокровища"];
    room_10 -> room_9 [label="Вернуться на запад"];
}
'''