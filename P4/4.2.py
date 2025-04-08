import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime


def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')


def load_csv(filename, col_names):
    return pd.read_csv(filename, delimiter=',', names=col_names, encoding='utf8')


def generate_sprite_map(rows=10, cols=20, size=5):
    fig, axes = plt.subplots(rows, cols, figsize=(cols, rows))
    for i in range(rows):
        for j in range(cols):
            sprite = np.random.randint(0, 2, (size, size // 2 + 1))
            sprite = np.hstack((sprite, np.fliplr(sprite[:, :-1])))
            axes[i, j].imshow(sprite, cmap='gray', interpolation='nearest')
            axes[i, j].axis('off')
    plt.show()


generate_sprite_map()