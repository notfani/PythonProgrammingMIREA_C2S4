import math
from typing import List

def chebyshev_distance(y: List[float], z: List[float]) -> float:
    chebyshev_max = float("-inf")
    for yi, zi in zip(y, z):
        diff = abs(yi - zi)
        if diff > chebyshev_max:
            chebyshev_max = diff
    return chebyshev_max


if __name__ == "__main__":
    y = [1, 0.5, 1]
    z = [0.5, 2, 1]
    chebyshev_result = chebyshev_distance(y, z)
    print(f"Chebyshev distance: {chebyshev_result}")
