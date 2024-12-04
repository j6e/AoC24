from itertools import product

with open("day_04/input.txt") as f:
    matrix = [[c for c in line if c != "\n"] for line in f.readlines()]

wide = len(matrix[0])
tall = len(matrix)

# For each X, check clockwise if X-MAS is in any of the 8 directions


def check_for_patterns(matrix, i, j) -> int:
    if matrix[i][j] == "X":
        return 0

    if not (j + 2 < wide and i + 2 < tall):
        return 0

    # M.S
    # .A.
    # M.S
    if (
        matrix[i][j] == "M"
        and matrix[i][j + 2] == "S"
        and matrix[i + 1][j + 1] == "A"
        and matrix[i + 2][j] == "M"
        and matrix[i + 2][j + 2] == "S"
    ):
        return 1

    # M.M
    # .A.
    # S.S
    if (
        matrix[i][j] == "M"
        and matrix[i][j + 2] == "M"
        and matrix[i + 1][j + 1] == "A"
        and matrix[i + 2][j] == "S"
        and matrix[i + 2][j + 2] == "S"
    ):
        return 1

    # S.M
    # .A.
    # S.M
    if (
        matrix[i][j] == "S"
        and matrix[i][j + 2] == "M"
        and matrix[i + 1][j + 1] == "A"
        and matrix[i + 2][j] == "S"
        and matrix[i + 2][j + 2] == "M"
    ):
        return 1

    # S.S
    # .A.
    # M.M
    if (
        matrix[i][j] == "S"
        and matrix[i][j + 2] == "S"
        and matrix[i + 1][j + 1] == "A"
        and matrix[i + 2][j] == "M"
        and matrix[i + 2][j + 2] == "M"
    ):
        return 1

    return 0


counter = 0
for i, j in product(range(tall), range(wide)):
    counter += check_for_patterns(matrix, i, j)

print(counter)
