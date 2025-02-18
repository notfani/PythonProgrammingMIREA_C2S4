from typing import List

def reverse_list_to_string(lst: List[int]) -> str:
    reversed_list = lst[::-1]
    return ' '.join(map(str, reversed_list))

if __name__ == "__main__":
    sample_list = [1, 2, 3, 4, 5]
    result = reverse_list_to_string(sample_list)
    print(result)