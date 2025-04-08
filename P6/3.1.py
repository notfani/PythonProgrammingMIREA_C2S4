from graphviz import Digraph

def draw(vertices, edges):
    # Создаем новый граф
    dot = Digraph()

    # Добавляем вершины в граф
    for vertex in vertices:
        id, label = vertex
        dot.node(str(id), label)  # Добавляем вершину с заданным id и label

    # Добавляем рёбра в граф
    for edge in edges:
        start, end = edge
        dot.edge(str(start), str(end))  # Добавляем ребро между вершинами

    # Визуализируем граф
    dot.render('graph', format='png', cleanup=True)  # Сохраняем граф в файл graph.png
    dot.view()  # Открываем граф в стандартном просмотрщике изображений

# Пример использования
draw([(1, 'v1'), (2, 'v2'), (3, 'v3')], [(1, 2), (2, 3), (2, 2)])
