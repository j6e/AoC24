import numpy as np


with open("day_02/input.txt") as f:
    l_left, l_right = [], []
    rows = []
    for line in f:
        numbers = [int(x) for x in line.strip().split(" ")]
        rows.append(np.array(numbers))


def is_safe(row):
    is_all_increasing = np.all(np.diff(row) >= 1)
    is_all_decreasing = np.all(np.diff(row) <= -1)
    is_max_diff_3 = np.abs(np.diff(row)).max() <= 3
    return (is_all_increasing or is_all_decreasing) and is_max_diff_3


safe = 0
for row in rows:
    if is_safe(row):
        safe += 1

print(safe)
