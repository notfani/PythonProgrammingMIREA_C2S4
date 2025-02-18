import numpy as np
import matplotlib.pyplot as plt


def manhattan_distance(y, z):
    """Вычисляет манхэттенское расстояние между векторами."""
    return sum(abs(yi - zi) for yi, zi in zip(y, z))


def euclidean_distance(y, z):
    """Вычисляет евклидово расстояние между векторами."""
    return np.sqrt(sum((yi - zi) ** 2 for yi, zi in zip(y, z)))


def chebyshev_distance(y, z):
    """Вычисляет расстояние Чебышева между векторами без использования max()."""
    distances = [abs(yi - zi) for yi, zi in zip(y, z)]
    chebyshev = distances[0]
    for d in distances:
        if d > chebyshev:
            chebyshev = d
    return chebyshev


def minkowski_distance(y, z, h=5):
    """Вычисляет расстояние Минковского между векторами."""
    return sum(abs(yi - zi) ** h for yi, zi in zip(y, z)) ** (1 / h)


def cosine_distance(y, z):
    """Вычисляет косинусное расстояние между векторами."""
    dot_product = sum(yi * zi for yi, zi in zip(y, z))
    norm_y = np.sqrt(sum(yi ** 2 for yi in y))
    norm_z = np.sqrt(sum(zi ** 2 for zi in z))
    return 1 - dot_product / (norm_y * norm_z)


def visualize(distance_metrics, y, z, move=1):
    """Визуализирует изменения расстояний при сдвиге вектора z."""
    moved_z = [i + move for i in z]
    distance_differences = []

    for distance in distance_metrics:
        distance_before_move = distance(y, z)
        distance_after_move = distance(y, moved_z)
        distance_difference = distance_after_move - distance_before_move
        distance_differences.append(distance_difference)

    x = range(len(distance_differences))
    figure, axis = plt.subplots()

    # Построение гистограммы
    axis.bar(x, distance_differences)
    axis.set_xticks(x, labels=['d_{}'.format(i + 1) for i in x])

    # Для работы вне Jupyter-ноутбуков раскомментируйте строку ниже
    plt.show()


# Входные данные
y = (1, 0.5, 1)
z = (0.5, 2, 1)

# Запуск визуализации
distances = [
    euclidean_distance,
    manhattan_distance,
    chebyshev_distance,
    lambda y, z: minkowski_distance(y, z, 5),  # Минковский с h=5
    cosine_distance
]

visualize(distances, y, z, move=1)
