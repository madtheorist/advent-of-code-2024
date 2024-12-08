
import os
from typing import List, Any

forward = list('XMAS')
backward = list('SAMX')
window_length = 4

def count_xmas(grid: List[List[str]]) -> int:
    count = 0
    count += count_horizontal(grid)
    count += count_vertical(grid)
    count += count_diagonal(grid)
    return count

def count_horizontal(grid: List[List[str]]) -> int:
    count = 0
    width = len(grid[0])
    for row in grid:
        for i in range(width - window_length + 1):
            test = row[i:i+window_length]
            if test == forward or test == backward:
                count += 1
    return count

def count_vertical(grid: List[List[str]]) -> int:
    count = 0
    height, width = len(grid), len(grid[0])
    # grid[row num][col num]
    for j in range(width):
        for i in range(height - window_length + 1):
            test = [grid[i + k][j] for k in range(window_length)]
            if test == forward or test == backward:
                count += 1
    return count

def count_diagonal(grid: List[List[str]]) -> int:
    count = 0
    height, width = len(grid), len(grid[0])
    for i in range(height - window_length + 1):
        for j in range(width - window_length + 1):
            test = [grid[i + k][j + k] for k in range(window_length)]
            test_2 = [grid[i + k][j + window_length - 1 - k] for k in range(window_length)]
            if test == forward or test == backward:
                count += 1
            if test_2 == forward or test_2 == backward:
                count += 1
    return count

if __name__ == "__main__":
    filepath = os.path.join("src", "inputs", "day_4_input.txt")
    with open(filepath, mode="r") as f:
        grid: List[List[str]] = []
        for line in f:
            grid.append(list(line.strip())) # strip() needed to remove newline character
    print(f"xmas count: {count_xmas(grid)}")


