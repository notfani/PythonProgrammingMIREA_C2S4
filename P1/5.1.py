def sdf_func(x, y):
    return circle( x, y, 0.45 )


def shader(x, y):
    d = sdf_func(x - 0.5, y - 0.5)
    return d > 0, abs(d) * 3, 0

def circle(x, y, r):
    """Функция SDF для круга с радиусом r."""
    return np.sqrt(x**2 + y**2) - r