import numpy as np
import matplotlib.pyplot as plt
import psutil

# Размер изображения
image_size = 1000


# Функция для получения данных процессора
def get_cpu_and_memory_usage():
    cpu_usage = psutil.cpu_percent(interval=0.1)  # Загрузка CPU в процентах
    memory_info = psutil.virtual_memory()  # Информация о памяти
    memory_usage = memory_info.percent  # Использование памяти в процентах
    return cpu_usage, memory_usage


# Генерация псевдо-белого шума
def generate_noise(size):
    # Получаем данные процессора
    cpu_usage, memory_usage = get_cpu_and_memory_usage()

    # Создаем массив координат
    x = np.linspace(0, size - 1, size)
    y = np.linspace(0, size - 1, size)
    xx, yy = np.meshgrid(x, y)

    # Генерация шума на основе данных процессора
    noise = (
            np.sin(cpu_usage * xx + memory_usage * yy) +
            np.cos(memory_usage * xx - cpu_usage * yy)
    )
    return noise


# Генерация массива белого шума
noise_image = generate_noise(image_size)

# Выбор средней строки для построения графика
middle_row = noise_image[image_size // 2]

# Построение линейного графика
plt.figure(figsize=(18, 6))  # Размер фигуры
plt.plot(middle_row, color='black')  # Построение графика
plt.title('Линейный график псевдо-белого шума (средняя строка)')
plt.xlabel('Индекс пикселя')
plt.ylabel('Значение шума')
plt.grid(True)  # Добавляем сетку
plt.show()