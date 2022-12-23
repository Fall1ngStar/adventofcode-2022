from lib import read_input, Point, window


def parse_input(input_data):
    grid = {}
    for line in input_data.splitlines():
        coords = [Point(*map(int, coord.split(","))) for coord in line.split(" -> ")]
        for start, end in window(coords, 2):
            direction = (end - start).nor
            current = start
            grid[(*current,)] = "#"
            while current != end:
                current += direction
                grid[(*current,)] = "#"
    return grid


def print_grid(grid):
    lowest_y = max([y for _, y in grid.keys()])
    lowest_x = min([x for (x, _) in grid.keys()])
    highest_x = max([x for (x, _) in grid.keys()])
    lines = [
        [" " for _ in range((highest_x - lowest_x) + 1)] for _ in range(lowest_y + 1)
    ]

    for (x, y), value in grid.items():
        lines[y][x - lowest_x] = value
    for line in lines:
        print("".join(line))
    print("_")


def part1(input_data):
    grid = parse_input(input_data)
    print_grid(grid)
    lowest = max([y for _, y in grid.keys()]) + 1
    loop = False
    while not loop:
        sand = Point(500, 0)
        grid[(*sand,)] = "o"
        falling = True
        while falling and (*sand,)[1] < lowest:
            for direction in [Point(0, 1), Point(-1, 1), Point(1, 1)]:
                next_pos = sand + direction
                if not grid.get((*next_pos,)):
                    del grid[(*sand,)]
                    grid[(*next_pos,)] = "o"
                    sand = next_pos
                    print_grid(grid)
                    break
            else:
                falling = False
        if falling:
            loop = True

    return len([val for val in grid.values() if val == "o"]) - 1


def part2(input_data):
    grid = parse_input(input_data)
    print_grid(grid)
    lowest = max([y for _, y in grid.keys()]) + 1
    loop = True
    while loop:
        sand = Point(500, 0)
        grid[(*sand,)] = "o"
        falling = True
        while falling and (*sand,)[1] < lowest:
            for direction in [Point(0, 1), Point(-1, 1), Point(1, 1)]:
                next_pos = sand + direction
                if not grid.get((*next_pos,)):
                    del grid[(*sand,)]
                    grid[(*next_pos,)] = "o"
                    sand = next_pos
                    # print_grid(grid)
                    break
            else:
                falling = False
        if grid.get((500, 0)):
            loop = False
    return len([val for val in grid.values() if val == "o"])


if __name__ == "__main__":
    input_data = read_input("day14")
    # print(f"part1 -> {part1(input_data)}")
    print(f"part2 -> {part2(input_data)}")
