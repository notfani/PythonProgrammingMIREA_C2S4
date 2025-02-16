import tkinter as tk


class MalеvichSquareApp :
    def __init__( self, root ) :
        self.root = root
        self.root.title( "Черный квадрат Малевича" )

        # Создаем холст
        self.canvas = tk.Canvas( root, bg='white' )
        self.canvas.pack( expand=True, fill=tk.BOTH )

        # Привязываем события изменения размера окна
        self.root.bind( "<Configure>", self.draw_square )

        # Инициализируем переменную для хранения ID прямоугольника
        self.square_id = None

    def draw_square( self, event=None ) :
        # Очищаем холст
        if self.square_id :
            self.canvas.delete( self.square_id )

        # Получаем текущие размеры окна
        width = self.canvas.winfo_width( )
        height = self.canvas.winfo_height( )

        # Вычисляем размер квадрата (минимальная сторона)
        side_length = min( width, height )

        # Вычисляем координаты центра холста
        center_x = width // 2
        center_y = height // 2

        # Вычисляем координаты углов квадрата
        x1 = center_x - side_length // 2
        y1 = center_y - side_length // 2
        x2 = center_x + side_length // 2
        y2 = center_y + side_length // 2

        # Рисуем черный квадрат
        self.square_id = self.canvas.create_rectangle( x1, y1, x2, y2, fill='black', outline='black' )


if __name__ == "__main__" :
    root = tk.Tk( )
    app = MalеvichSquareApp( root )
    root.mainloop( )
