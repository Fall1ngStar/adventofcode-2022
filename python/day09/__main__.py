from lib import read_input, window, Point

DIRECTIONS = {
    "R": Point(1, 0),
    "U": Point(0, 1),
    "D": Point(0, -1),
    "L": Point(-1, 0),
}


def simulation(input_data, rope_length):
    rope = [Point(0, 0) for _ in range(rope_length)]

    visited = {Point(0, 0)}
    for line in input_data.splitlines():
        raw_direction, raw_count = line.split(" ")
        target = DIRECTIONS[raw_direction]
        count = int(raw_count)
        for _ in range(count):
            head = rope[0]
            head = head + target
            rope[0] = head
            for i, (from_, to) in enumerate(window(rope, 2)):
                dx, dy = delta = from_ - to
                if any([abs(dx) > 1, abs(dy) > 1]):
                    move = delta.nor
                    to = to + move
                    rope[i + 1] = to
            visited.add(rope[-1])
    return len(visited)


def part1(input_data):
    return simulation(input_data, 2)


def part2(input_data):
    return simulation(input_data, 10)


if __name__ == "__main__":
    input_data = read_input("day09")
    print(f"part1 -> {part1(input_data)}")
    print(f"part2 -> {part2(input_data)}")
