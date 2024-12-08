
import os
from typing import List, Any

def report_safe(report: List[int]) -> bool:
    diffs = []
    for cur, next in zip(report[:-1], report[1:]):
        diff = next - cur
        if diff == 0 or abs(diff) > 3:
            return False
        diffs.append(diff)
    ascending = [diff > 0 for diff in diffs]
    if len(set(ascending)) == 1:
        return True
    return False

def report_safe_with_dampener(report: List[int]) -> bool:
    """Brute force approach. Its really not great.."""
    if report_safe(report):
        return True
    for i in range(len(report)):
        if i == len(report) - 1:
            shortened_report = report[:-1]
        else:
            shortened_report = report[:i] + report[i+1:]
        if report_safe(shortened_report):
            return True
    return False

if __name__ == "__main__":
    filepath = os.path.join("src", "inputs", "day_2_input.txt")
    with open(filepath, mode="r") as f:
        reports: List[List[int]] = []
        for line in f:
            r = [int(val) for val in line.split()]
            reports.append(r)

    safe = [report_safe(r) for r in reports]
    safe_with_dampener = [report_safe_with_dampener(r) for r in reports]
    print(f"Number of safe reports: {sum(safe)}")
    print(f"Number of safe reports: {sum(safe_with_dampener)}")