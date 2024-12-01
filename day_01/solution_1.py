import numpy as np

with open("day_01/input.txt") as f:
    l_left, l_right = [], []
    for line in f:
        left, right = map(int, line.strip().split("   "))
        l_left.append(left)
        l_right.append(right)

v_left = np.array(l_left)
v_right = np.array(l_right)

v_left.sort()
v_right.sort()

res = np.abs((v_left - v_right)).sum()

print(res)
