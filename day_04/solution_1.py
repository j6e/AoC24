from itertools import product

with open("day_04/input.txt") as f:
    matrix = [[c for c in line if c != "\n"] for line in f.readlines()]

wide = len(matrix[0])
tall = len(matrix)

# For each X, check clockwise if XMAS is in any of the 8 directions
counter = 0
for i, j in product(range(tall), range(wide)):
    if matrix[i][j] != "X":
        continue

    # Check right
    if j + 3 < wide:
        if (
            matrix[i][j + 1] == "M"
            and matrix[i][j + 2] == "A"
            and matrix[i][j + 3] == "S"
        ):
            counter += 1

    # Check down-right
    if i + 3 < tall and j + 3 < wide:
        if (
            matrix[i + 1][j + 1] == "M"
            and matrix[i + 2][j + 2] == "A"
            and matrix[i + 3][j + 3] == "S"
        ):
            counter += 1

    # Check down
    if i + 3 < tall:
        if (
            matrix[i + 1][j] == "M"
            and matrix[i + 2][j] == "A"
            and matrix[i + 3][j] == "S"
        ):
            counter += 1

    # Check down-left
    if i + 3 < tall and j - 3 >= 0:
        if (
            matrix[i + 1][j - 1] == "M"
            and matrix[i + 2][j - 2] == "A"
            and matrix[i + 3][j - 3] == "S"
        ):
            counter += 1

    # Check left
    if j - 3 >= 0:
        if (
            matrix[i][j - 1] == "M"
            and matrix[i][j - 2] == "A"
            and matrix[i][j - 3] == "S"
        ):
            counter += 1

    # Check up-left
    if i - 3 >= 0 and j - 3 >= 0:
        if (
            matrix[i - 1][j - 1] == "M"
            and matrix[i - 2][j - 2] == "A"
            and matrix[i - 3][j - 3] == "S"
        ):
            counter += 1

    # Check up
    if i - 3 >= 0:
        if (
            matrix[i - 1][j] == "M"
            and matrix[i - 2][j] == "A"
            and matrix[i - 3][j] == "S"
        ):
            counter += 1

    # Check up-right
    if i - 3 >= 0 and j + 3 < wide:
        if (
            matrix[i - 1][j + 1] == "M"
            and matrix[i - 2][j + 2] == "A"
            and matrix[i - 3][j + 3] == "S"
        ):
            counter += 1

print(counter)
