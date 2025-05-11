from hypothesis import given, strategies as st
import math

# Реализация функций
def euclidean_distance(p1, p2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(p1, p2)))

def manhattan_distance(p1, p2):
    return sum(abs(x - y) for x, y in zip(p1, p2))

# Ограничение диапазона генерируемых чисел
@given(
    st.lists(st.floats(min_value=-1e6, max_value=1e6, allow_nan=False, allow_infinity=False), min_size=2, max_size=2),
    st.lists(st.floats(min_value=-1e6, max_value=1e6, allow_nan=False, allow_infinity=False), min_size=2, max_size=2)
)
def test_euclidean_commutativity(p1, p2):
    """Тест на коммутативность для евклидова расстояния."""
    assert math.isclose(euclidean_distance(p1, p2), euclidean_distance(p2, p1), rel_tol=1e-9)

@given(
    st.lists(st.floats(min_value=-1e6, max_value=1e6, allow_nan=False, allow_infinity=False), min_size=2, max_size=2),
    st.lists(st.floats(min_value=-1e6, max_value=1e6, allow_nan=False, allow_infinity=False), min_size=2, max_size=2)
)
def test_manhattan_commutativity(p1, p2):
    """Тест на коммутативность для манхэттенского расстояния."""
    assert manhattan_distance(p1, p2) == manhattan_distance(p2, p1)