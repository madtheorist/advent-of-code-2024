
import os
from typing import List, Any

def distance_between_lists(list_1: List[int], list_2: List[int]) -> int:
    """
    O(nlogn) due to sorting
    """
    dist = 0
    list_1.sort()
    list_2.sort()
    for x, y in zip(list_1, list_2):
        dist += abs(x - y)
    return dist

def similarity_score(list_1: List[int], list_2: List[int]) -> int:
    """
    Can also use collections.Counter object 
    Here we code it from scratch
    """
    score = 0
    counter_1 = get_counter(list_1)
    counter_2 = get_counter(list_2)
    for k1, v1 in counter_1.items():
        v2 = counter_2.get(k1, 0)
        score += k1 * v1 * v2
    return score

def get_counter(list: List[Any]):
    counter = {}
    for i in list:
        counter[i] = counter.get(i, 0) + 1
    return counter

if __name__ == "__main__":
    filepath = os.path.join("inputs", "day_1_input.txt")
    with open(filepath, mode="r") as f:
        list_1, list_2 = [], []
        for line in f:
            numbers = line.split()
            list_1.append(int(numbers[0]))
            list_2.append(int(numbers[1]))
    print(distance_between_lists(list_1, list_2))
    print(similarity_score(list_1, list_2))
