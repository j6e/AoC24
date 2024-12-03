import re

with open("day_03/input.txt") as f:
    text = f.read()

muls = re.compile(
    r"mul\((?P<d1>\d{1,3}),(?P<d2>\d{1,3})\)|(?P<do>do\(\))|(?P<dont>don't\(\))",
    re.MULTILINE | re.DOTALL,
)

accu = 0
activated = True
for match in muls.finditer(text):
    a, b, do, dont = match.groups()
    match (do, dont):
        # If the flags match, we make the switch and go to next iteration
        case ("do()", None):
            activated = True
            continue
        case (None, "don't()"):
            activated = False
            continue
        # If the flags don't match, we have to accumulate or not
        case (None, None):
            match activated:
                case True:
                    accu += int(a) * int(b)
                case False:
                    continue

print(accu)
