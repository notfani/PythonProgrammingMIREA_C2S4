import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime


def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')


def load_csv(filename, col_names):
    return pd.read_csv(filename, delimiter=',', names=col_names, encoding='utf8')


# 4.1. Генератор случайных спрайтов 5x5 пикселей
def generate_sprite(size=5):
    sprite = np.random.randint(0, 2, (size, size // 2 + 1))
    sprite = np.hstack((sprite, np.fliplr(sprite[:, :-1])))
    plt.imshow(sprite, cmap='gray', interpolation='nearest')
    plt.show()


generate_sprite()