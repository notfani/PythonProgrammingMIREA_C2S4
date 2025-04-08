from pathlib import Path
import tkinter as tk
from math import floor, ceil

# Конфигурация
SCALE_X = 6
SCALE_Y = 4
WIDTH = 160 * SCALE_X
HEIGHT = 200 * SCALE_Y

# Палитра EGA (16 цветов) в 6-битном формате
COLORS = [
    (0x00, 0x00, 0x00),  # 0: Черный
    (0x00, 0x00, 0x2A),  # 1: Синий
    (0x00, 0x2A, 0x00),  # 2: Зеленый
    (0x00, 0x2A, 0x2A),  # 3: Голубой
    (0x2A, 0x00, 0x00),  # 4: Красный
    (0x2A, 0x00, 0x2A),  # 5: Пурпурный
    (0x2A, 0x15, 0x00),  # 6: Коричневый
    (0x2A, 0x2A, 0x2A),  # 7: Светло-серый
    (0x15, 0x15, 0x15),  # 8: Темно-серый
    (0x15, 0x15, 0x3F),  # 9: Ярко-синий
    (0x15, 0x3F, 0x15),  # 10: Ярко-зеленый
    (0x15, 0x3F, 0x3F),  # 11: Ярко-голубой
    (0x3F, 0x15, 0x15),  # 12: Ярко-красный
    (0x3F, 0x15, 0x3F),  # 13: Ярко-пурпурный
    (0x3F, 0x3F, 0x15),  # 14: Желтый
    (0x3F, 0x3F, 0x3F)  # 15: Белый
]


class AGIVisualizer:
    def __init__(self, canvas):
        self.canvas = canvas
        self.picture_draw = False
        self.priority_draw = False
        self.current_pic_color = 15  # Начинаем с белого (фон)
        self.current_pri_color = 4  # Приоритетный экран начинается с красного
        self.pen_position = (0, 0)

    def set_pic_color(self, color_index):
        """Установка цвета для picture screen (0xF0)"""
        self.current_pic_color = color_index & 0x0F
        self.picture_draw = True

    def disable_pic_draw(self):
        """Отключение рисования на picture screen (0xF1)"""
        self.picture_draw = False

    def set_pri_color(self, color_index):
        """Установка цвета для priority screen (0xF2)"""
        self.current_pri_color = color_index & 0x0F
        self.priority_draw = True

    def disable_pri_draw(self):
        """Отключение рисования на priority screen (0xF3)"""
        self.priority_draw = False

    def draw_line(self, coords):
        """Рисование линии между точками с учетом масштабирования"""
        if not (self.picture_draw or self.priority_draw):
            return

        scaled_coords = []
        for x, y in coords:
            # Масштабирование координат
            scaled_x = x * SCALE_X
            scaled_y = y * SCALE_Y
            scaled_coords.extend([scaled_x, scaled_y])

        # Рисование на picture screen
        if self.picture_draw:
            color = '#%02x%02x%02x' % COLORS[self.current_pic_color]
            self.canvas.create_line(*scaled_coords, fill=color, width=2)

        # Рисование на priority screen (пунктиром)
        if self.priority_draw:
            color = '#%02x%02x%02x' % COLORS[self.current_pri_color]
            self.canvas.create_line(*scaled_coords, fill=color, width=1,
                                    dash=(2, 2))

    def draw_relative_line(self, dx, dy):
        """Рисование линии относительно текущей позиции"""
        x, y = self.pen_position
        new_x = x + dx
        new_y = y + dy
        self.draw_line([(x, y), (new_x, new_y)])
        self.pen_position = (new_x, new_y)

    def draw_y_corner(self, coords):
        """Рисование Y-углов (0xF4) - сначала изменяется Y"""
        if len(coords) < 2:
            return

        x, y = coords[0], coords[1]
        self.pen_position = (x, y)
        points = [(x, y)]

        i = 2
        while i < len(coords):
            if i % 2 == 0:  # Четный индекс - изменение Y
                y = coords[i]
            else:  # Нечетный индекс - изменение X
                x = coords[i]
            points.append((x, y))
            self.pen_position = (x, y)
            i += 1

        self.draw_line(points)

    def draw_x_corner(self, coords):
        """Рисование X-углов (0xF5) - сначала изменяется X"""
        if len(coords) < 2:
            return

        x, y = coords[0], coords[1]
        self.pen_position = (x, y)
        points = [(x, y)]

        i = 2
        while i < len(coords):
            if i % 2 == 0:  # Четный индекс - изменение X
                x = coords[i]
            else:  # Нечетный индекс - изменение Y
                y = coords[i]
            points.append((x, y))
            self.pen_position = (x, y)
            i += 1

        self.draw_line(points)

    def draw_absolute_line(self, coords):
        """Рисование абсолютных линий (0xF6)"""
        if len(coords) < 2:
            return

        x, y = coords[0], coords[1]
        self.pen_position = (x, y)
        points = [(x, y)]

        i = 2
        while i < len(coords):
            if i % 2 == 0:  # Четный индекс - X координата
                x = coords[i]
            else:  # Нечетный индекс - Y координата
                y = coords[i]
                points.append((x, y))
                self.pen_position = (x, y)
            i += 1

        self.draw_line(points)

    def draw_relative_line_command(self, bytes_list):
        """Обработка команды относительных линий (0xF7)"""
        if len(bytes_list) < 2:
            return

        x, y = bytes_list[0], bytes_list[1]
        self.pen_position = (x, y)

        for byte in bytes_list[2:]:
            if byte >= 0xF0:  # Конец команды
                break

            # Разбор относительного смещения
            dx = (byte >> 4) & 0x07
            dy = byte & 0x07
            if byte & 0x08: dx = -dx
            if byte & 0x80: dy = -dy

            self.draw_relative_line(dx, dy)

    def parse_pic_file(self, pic_data):
        """Разбор файла PIC и выполнение команд"""
        i = 0
        while i < len(pic_data):
            byte = pic_data[i]

            if byte == 0xFF:  # Конец данных
                break

            # Команда изменения цвета picture и включение рисования
            elif byte == 0xF0:
                if i + 1 >= len(pic_data): break
                self.set_pic_color(pic_data[i + 1])
                i += 2

            # Команда отключения рисования picture
            elif byte == 0xF1:
                self.disable_pic_draw()
                i += 1

            # Команда изменения цвета priority и включение рисования
            elif byte == 0xF2:
                if i + 1 >= len(pic_data): break
                self.set_pri_color(pic_data[i + 1])
                i += 2

            # Команда отключения рисования priority
            elif byte == 0xF3:
                self.disable_pri_draw()
                i += 1

            # Команда Y-углов
            elif byte == 0xF4:
                args = []
                i += 1
                while i < len(pic_data) and pic_data[i] < 0xF0:
                    args.append(pic_data[i])
                    i += 1
                self.draw_y_corner(args)

            # Команда X-углов
            elif byte == 0xF5:
                args = []
                i += 1
                while i < len(pic_data) and pic_data[i] < 0xF0:
                    args.append(pic_data[i])
                    i += 1
                self.draw_x_corner(args)

            # Команда абсолютных линий
            elif byte == 0xF6:
                args = []
                i += 1
                while i < len(pic_data) and pic_data[i] < 0xF0:
                    args.append(pic_data[i])
                    i += 1
                self.draw_absolute_line(args)

            # Команда относительных линий
            elif byte == 0xF7:
                args = []
                i += 1
                while i < len(pic_data) and pic_data[i] < 0xF0:
                    args.append(pic_data[i])
                    i += 1
                self.draw_relative_line_command(args)

            # Остальные команды пропускаем
            else:
                i += 1


def draw(pic_data):
    visualizer = AGIVisualizer(canvas)
    visualizer.parse_pic_file(pic_data)


pic = Path('PIC.44').read_bytes()
canvas = tk.Canvas(width=160 * SCALE_X, height=170 * SCALE_Y)
canvas.pack()
draw(pic)
tk.mainloop()