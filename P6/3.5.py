import matplotlib.pyplot as plt
import seaborn as sns  # для красивой плотности KDE

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

def chaotic_distribution():
    o = LogisticMap(mu=4.0, state=0.1)
    values = [o.next() for _ in range(100_000)]  # достаточно точек

    # Гистограмма + оценка плотности KDE
    sns.histplot(values, bins=50, kde=True, stat='count', color='skyblue')
    plt.xlabel('Value')
    plt.ylabel('Count')
    plt.title('Distribution of values from LogisticMap (μ = 4.0)')
    plt.show()

chaotic_distribution()
