from typing import List
import math

def manhattan_distance(y: List[float], z: List[float]) -> float:
    return sum(abs(yi - zi) for yi, zi in zip(y, z))

if __name__ == "__main__":
    y = [1, 0.5, 1]
    z = [0.5, 2, 1]
    result = manhattan_distance(y, z)
    print(f"Manhattan distance: {result}")