from graphviz import Digraph


class Chaos:
    def __init__(self, mu, state):
        self.mu = mu
        self.state = state
        self.stabilize()

    def stabilize(self):
        for _ in range(1000):
            self.next()

    def next(self):
        pass  # Заглушка, будет переопределено в подклассе


class LogisticMap(Chaos):
    def next(self):
        self.state = self.mu * self.state * (1 - self.state)
        return self.state

o = LogisticMap(2, 0.1)
print(o.next(), o.next(), o.next())  # → (0.5, 0.5, 0.5)


def visualize(system):
    dot = Digraph()
    visited = set()

    prev = round(system.next(), 15)
    dot.node(str(prev))

    for _ in range(9):  # 9 шагов после первого
        curr = round(system.next(), 15)
        dot.node(str(curr))

        edge = (str(prev), str(curr))
        if edge not in visited:
            dot.edge(*edge)
            visited.add(edge)

        prev = curr

    dot.render('logistic_graph', format='png', view=True)


visualize(LogisticMap(3.5, 0.1))



