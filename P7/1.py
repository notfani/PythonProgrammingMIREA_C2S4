import numpy as np
import matplotlib.pyplot as plt

# Параметры t
t = np.linspace(0, 2 * np.pi, 1000)  # 1000 точек для гладкости графика

# Вычисление x и y
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

# Создание фигуры с двумя подграфиками
fig, axes = plt.subplots(1, 2, figsize=(12, 6))  # Две колонки, общая высота 6

# График 1: Без заливки
axes[0].plot(x, y, color='red', label='График')
axes[0].set_title('Без заливки')
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')
axes[0].grid(True)
axes[0].axis('equal')  # Сохранение пропорций осей
axes[0].legend()

# График 2: С заливкой
axes[1].plot(x, y, color='red', label='График')
axes[1].fill(x, y, color='red', alpha=0.3, label='Заливка')
axes[1].set_title('С заливкой')
axes[1].set_xlabel('x')
axes[1].set_ylabel('y')
axes[1].grid(True)
axes[1].axis('equal')  # Сохранение пропорций осей
axes[1].legend()

# Отображение графиков
plt.tight_layout()  # Автоматическая настройка межграфического пространства
plt.show()