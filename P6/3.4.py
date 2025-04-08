import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

class Chaos:
    def __init__(self, mu, state):
        self.mu = mu
        self.state = state
        self.stabilize()

    def stabilize(self):
        for _ in range(1000):
            self.next()

    def next(self):
        pass

class LogisticMap(Chaos):
    def next(self):
        self.state = self.mu * self.state * (1 - self.state)
        return self.state

def bifurcation_diagram():
    mus = np.linspace(1.0, 4.0, 60)
    x0 = 0.1
    iterations = 50

    plt.figure(figsize=(8, 6))

    # Используем 10 цветов из табличной палитры
    cmap = plt.get_cmap('tab10')

    for i, mu in enumerate(mus):
        system = LogisticMap(mu, x0)
        xs = [mu] * iterations
        ys = [system.next() for _ in range(iterations)]

        # Цвет повторяется каждые 10 μ
        color = cmap(i % 10)
        plt.scatter(xs, ys, color=color, s=10)

    plt.xlabel('μ')
    plt.ylabel('State')
    plt.title('Bifurcation Diagram for Logistic Map')
    plt.grid(True)
    plt.show()


bifurcation_diagram()