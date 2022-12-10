from lib import read_input, window

DIRECTIONS = {
    "R": (1, 0),
    "U": (0, 1),
    "D": (0, -1),
    "L": (-1, 0),
}


def part1(input_data):
    head = (0, 0)
    tail = (0, 0)
    visited = {(0, 0)}
    for line in input_data.splitlines():
        raw_direction, raw_count = line.split(" ")
        direction = DIRECTIONS[raw_direction]
        count = int(raw_count)
        for _ in range(count):
            head = (head[0] + direction[0], head[1] + direction[1])
            dx, dy = (head[0] - tail[0], head[1] - tail[1])
            if any([abs(dx) > 1, abs(dy) > 1]):
                vx, vy = dx / (abs(dx) or 1), dy / (abs(dy) or 1)
                tail = (tail[0] + vx, tail[1] + vy)
                visited.add(tail)
    return len(visited)


def part2(input_data):
    rope = [(0, 0) for _ in range(10)]

    visited = {(0, 0)}
    for line in input_data.splitlines():
        raw_direction, raw_count = line.split(" ")
        ax, ay = DIRECTIONS[raw_direction]
        count = int(raw_count)
        for _ in range(count):
            hx, hy = rope[0]
            head = (hx + ax, hy + ay)
            rope[0] = head
            for i, ((fx, fy), (tx, ty)) in enumerate(window(rope, 2)):
                dx, dy = (fx - tx, fy - ty)
                if any([abs(dx) > 1, abs(dy) > 1]):
                    vx, vy = dx / (abs(dx) or 1), dy / (abs(dy) or 1)
                    to = (tx + vx, ty + vy)
                    rope[i + 1] = to
            visited.add(rope[-1])
    return len(visited)


if __name__ == "__main__":
    input_data = read_input("day09")
    print(f"part1 -> {part1(input_data)}")
    print(f"part2 -> {part2(input_data)}")
