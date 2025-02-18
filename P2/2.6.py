import math
from typing import List

def minkowski_distance(y: List[float], z: List[float], h: int) -> float:
    return sum(abs(yi - zi) ** h for yi, zi in zip(y, z)) ** (1 / h)


if __name__ == "__main__":
    y = [1, 0.5, 1]
    z = [0.5, 2, 1]
    h = 5
    minkowski_result = minkowski_distance(y, z, h)
    print(f"Minkowski distance (h={h}): {minkowski_result}")
