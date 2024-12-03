import numpy as np


with open("day_02/input.txt") as f:
    l_left, l_right = [], []
    rows = []
    for line in f:
        numbers = [int(x) for x in line.strip().split(" ")]
        rows.append(np.array(numbers))


def is_safe(diff):
    is_all_increasing = np.all(diff >= 1)
    is_all_decreasing = np.all(diff <= -1)
    is_max_diff_3 = np.abs(diff).max() <= 3
    return (is_all_increasing or is_all_decreasing) and is_max_diff_3


def is_safe_tolerate_one_bad(row):
    diff = np.diff(row)

    if is_safe(diff):
        return True

    for i in range(len(row)):
        new_row = np.delete(row, i)
        if is_safe(np.diff(new_row)):
            return True

    return False


safe = 0
for row in rows:
    if is_safe_tolerate_one_bad(row):
        safe += 1

print(safe)
