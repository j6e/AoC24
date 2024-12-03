import re

with open("day_03/input.txt") as f:
    text = f.read()

muls = re.compile(r"mul\((?P<d1>\d{1,3}),(?P<d2>\d{1,3})\)", re.MULTILINE | re.DOTALL)

accu = 0
for match in muls.finditer(text):
    a, b = match.groups()
    accu += int(a) * int(b)

print(accu)
