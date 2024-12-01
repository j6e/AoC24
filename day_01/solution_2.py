from collections import Counter

with open("day_01/input.txt") as f:
    l_left, l_right = [], []
    for line in f:
        left, right = map(int, line.strip().split("   "))
        l_left.append(left)
        l_right.append(right)

c_right = Counter(l_right)
similarity = [c_right[n] * n if n in c_right else 0 for n in l_left]
res = sum(similarity)

print(res)
