from lib import read_input
from collections import defaultdict


def parse_input(input_data):
    grid = [[char for char in line] for line in input_data.splitlines()]
    start = None
    end = None
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == "S":
                start = (x, y)
                grid[x][y] = "a"
            if grid[x][y] == "E":
                end = (x, y)
                grid[x][y] = "z"
            grid[x][y] = ord(grid[x][y]) - 96
    return grid, start, end


def get_neighbours(point, grid):
    x, y = point
    val = grid[x][y]
    neighbours = []
    if x < len(grid) - 1:
        neighbours.append((x + 1, y))
    if x > 0:
        neighbours.append((x - 1, y))
    if y < len(grid[x]) - 1:
        neighbours.append((x, y + 1))
    if y > 0:
        neighbours.append((x, y - 1))
    return [(xn, yn) for xn, yn in neighbours if grid[xn][yn] - val <= 1]


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path


def print_map(grid, path):
    new_grid = [[chr(val + 96) for val in line] for line in grid]
    for x, y in path:
        new_grid[x][y] = " "
    for line in new_grid:
        print("".join(line))
    print("_")


def a_star(start, end, grid):
    def heuristic(point):
        return abs(point[0] - end[0]) + abs(point[1] - end[1])

    open_set = {start}
    came_from = {}

    g_score = defaultdict(lambda: 99999999)
    g_score[start] = 0

    f_score = defaultdict(lambda: 99999999)
    f_score[start] = heuristic(start)
    while open_set:
        current, _ = sorted(
            [(val, f_score[val]) for val in open_set], key=lambda x: x[1]
        )[0]
        # print_map(grid, reconstruct_path(came_from, current))
        if current == end:
            return reconstruct_path(came_from, current)
        open_set.remove(current)
        for neighbour in get_neighbours(current, grid):
            tentative_g_score = g_score[current] + 1
            if tentative_g_score < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = tentative_g_score
                f_score[neighbour] = tentative_g_score + heuristic(neighbour)
                if neighbour not in open_set:
                    open_set.add(neighbour)
    return "failed"


def part1(input_data):
    grid, start, end = parse_input(input_data)
    path = a_star(start, end, grid)
    if path == "failed":
        return -1
    return len(path) - 1


def part2(input_data):
    grid, _, end = parse_input(input_data)
    candidates = {}
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 1:
                candidates[(x, y)] = a_star((x, y), end, grid)
    return min([len(c) for c in candidates.values() if c != "failed"]) - 1


if __name__ == "__main__":
    input_data = read_input("day12")
    print(f"part1 -> {part1(input_data)}")
    print(f"part2 -> {part2(input_data)}")
