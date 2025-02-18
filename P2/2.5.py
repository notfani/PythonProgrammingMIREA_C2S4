from typing import List
import math

def euclidean_distance(y: List[float], z: List[float]) -> float:
    return sum((yi - zi) ** 2 for yi, zi in zip(y, z))

if __name__ == "__main__":
    y = [1, 0.5, 1]
    z = [0.5, 2, 1]
    result = euclidean_distance(y, z)
    print(f"quad Euclidean distance: {result}")
