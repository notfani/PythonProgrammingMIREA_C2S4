import matplotlib.pyplot as plt
import math
from decimal import Decimal

# Заданный список коэффициентов
k = [6, 0, -4 - 3, 5, 6, -6, -13, 7, 44, 64, 44, 7, -13, -6, 6, 5, -3, -4, 0, 6]

# Функция для создания диапазона чисел с шагом Decimal
def float_range(start, stop, step):
    while start < stop:
        yield start
        start += step

# Создаем список значений omega
omega_list = list(float_range(Decimal('0.1'), Decimal('2.1'), Decimal('0.1')))

# Список для хранения результатов
ex_list = []

# Основной цикл для вычисления значений
for omega in omega_list:
    for t in range(1, 100):  # Цикл по времени
        result_sum = 0  # Переменная для накопления суммы
        for b in range(0, 20):  # Цикл по смещению
            x = round(1000 * math.sin(omega * (t + b)))  # Вычисляем значение синусоиды
            result_sum += x * k[b]  # Умножаем на соответствующий коэффициент из списка k
        ex_list.append(result_sum)  # Добавляем результат в общий список

# Визуализация результатов
plt.figure(figsize=(12, 6))
plt.plot(ex_list, label="Сигнал ускорителя")
plt.title("Моделирование работы аппаратного ускорителя")
plt.xlabel("Время / Итерация")
plt.ylabel("Значение сигнала")
plt.legend()
plt.grid(True)
plt.show()