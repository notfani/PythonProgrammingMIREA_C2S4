import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def draw(figure_func, bbox=(-1.3, 1.3)):
    xmin, xmax, ymin, ymax, zmin, zmax = bbox * 3
    fig = plt.figure(figsize=(10, 10))  # Создаем фигуру с размером (10, 10)
    ax = fig.add_subplot(projection='3d')  # Добавляем 3D-подграфик

    a = np.linspace(xmin, xmax, 80)  # Создаем массив значений для x
    b = np.linspace(ymin, ymax, 80)  # Создаем массив значений для y и z

    a1, a2 = np.meshgrid(a, a)  # Создаем двумерные сетки

    # Проходим по всем осям и строим контурные линии
    for x in b:
        y, z = a1, a2  # Фиксируем x, а y и z остаются переменными
        X = figure_func(x, y, z)  # Вычисляем значение функции
        cset = ax.contour(X + x, y, z, [x], zdir='x', colors=('red'))  # Рисуем контурные линии

    for y in b:
        x, z = a1, a2  # Фиксируем y, а x и z остаются переменными
        Y = figure_func(x, y, z)  # Вычисляем значение функции
        cset = ax.contour(x, Y + y, z, [y], zdir='y', colors=('red'))  # Рисуем контурные линии

    for z in b:
        x, y = a1, a2  # Фиксируем z, а x и y остаются переменными
        Z = figure_func(x, y, z)  # Вычисляем значение функции
        cset = ax.contour(x, y, Z + z, [z], zdir='z', colors=('red'))  # Рисуем контурные линии

    # Устанавливаем пределы для осей
    ax.set_xlim3d(xmin, xmax)
    ax.set_ylim3d(ymin, ymax)
    ax.set_zlim3d(zmin, zmax)

    # Отображаем график
    plt.show()

# Определяем функцию F(x, y, z)
def F(x, y, z):
    return (x**2 + (9 * y**2) / 4 + z**2 - 1)**3 - x**2 * z**3 - (9 * y**2 * z**3) / 200

# Вызываем функцию draw с передачей функции F
draw(F)