from copy import deepcopy
from tqdm import tqdm


def find_guard(map: list[list[str]]) -> tuple[int, int]:
    for i, row in enumerate(map):
        for j, elem in enumerate(row):
            if elem in ("^", "v", "<", ">"):
                return i, j


def get_direction(guard: str) -> tuple[int, int]:
    if guard == "^":
        return -1, 0
    if guard == "v":
        return 1, 0
    if guard == "<":
        return 0, -1
    if guard == ">":
        return 0, 1
    raise ValueError(f"Invalid guard token: {guard}")


def is_blocked(map: list[list[str]], x: int, y: int) -> bool:
    if not is_inside_map(map, x, y):
        return False
    return map[x][y] == "#"


def rotate_right(guard: str) -> str:
    if guard == "^":
        return ">"
    if guard == "v":
        return "<"
    if guard == "<":
        return "^"
    if guard == ">":
        return "v"


def mark_visited(map: list[list[str]], x: int, y: int) -> None:
    map[x][y] = "X"


def move_guard(map, guard, new_x, new_y):
    if is_inside_map(map, new_x, new_y):
        map[new_x][new_y] = guard


def is_inside_map(map: list[list[str]], x: int, y: int) -> bool:
    return 0 <= x < len(map) and 0 <= y < len(map[0])


def prety_print_map(map: list[list[str]]) -> None:
    for row in map:
        print("".join(row))


def count_visited(map: list[list[str]]) -> int:
    return sum(row.count("X") for row in map)


def solve(map):
    x, y = find_guard(map)
    count = 0
    while is_inside_map(map, x, y) and count < 1_000_000:
        guard_token = map[x][y]
        step_x, step_y = get_direction(guard_token)

        # If the next step is blocked, rotate the guard and go to the next iteration
        if is_blocked(map, x + step_x, y + step_y):
            map[x][y] = rotate_right(map[x][y])
            continue

        mark_visited(map, x, y)
        x += step_x
        y += step_y
        move_guard(map, guard_token, x, y)
        count += 1

    if count == 1_000_000:
        raise ValueError("Infinite loop detected")


def yield_obstacle_map(map: list[list[str]], original_map: list[list[str]]):
    for i, row in enumerate(map):
        for j, elem in enumerate(row):
            if elem == "X" and original_map[i][j] != "^":
                new_map = deepcopy(original_map)
                new_map[i][j] = "#"
                yield new_map


with open("day_06/input.txt") as f:
    map = [list(line) for line in f.read().splitlines()]

original_map = deepcopy(map)
solve(map)
visited = count_visited(map)
print(visited)

loop_count = 0
for obstacle_map in tqdm(yield_obstacle_map(map, original_map), total=visited - 1):
    try:
        solve(obstacle_map)
    except ValueError:
        loop_count += 1
        continue

print(loop_count)
