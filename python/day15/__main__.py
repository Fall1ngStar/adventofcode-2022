import itertools
from lib import read_input, Point
import re

DIRECTIONS = (
    (Point(-1, 0), Point(0, 1)),
    (Point(1, 0), Point(0, -1)),
    (Point(0, 1), Point(1, 0)),
    (Point(0, -1), Point(0, 1)),
)

def parse_data(input_data):
    result = []
    for line in input_data.splitlines():
        xa, ya, xb, yb = re.match(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line).groups()
        result.append((Point(int(xa), int(ya)), Point(int(xb), int(yb))))
    return result

def part1(input_data):
    target_line = 2000000
    lines = parse_data(input_data)
    impossible_posistions = set()
    for sensor, beacon in lines:
        distance_to_beacon = len(sensor - beacon)
        distance_to_target = abs(sensor[1] - target_line)
        if (delta := distance_to_beacon - distance_to_target) >= 0:
            for i in range(sensor[0] - delta, sensor[0] + delta + 1):
                impossible_posistions.add(i)
    for _, beacon in lines:
        if beacon[0] in impossible_posistions and beacon[1] == target_line:
            impossible_posistions.remove(beacon[0])
    return len(impossible_posistions)

# TODO: not working with example input
def part2(input_data):
    bounds = 4_000_000
    lines = parse_data(input_data)
    plus_x_lines = set()
    minus_x_lines = set()
    for sensor, beacon in lines:
        distance = len(sensor - beacon)
        x, y = sensor
        plus_x_lines.add(-(x-y+distance))
        plus_x_lines.add(-(x-y-distance))
        minus_x_lines.add(x+y+distance)
        minus_x_lines.add(x+y-distance)
    candidates_plus_x = set()
    for a, b in itertools.combinations(plus_x_lines, 2):
        avg = (a+b)//2
        if abs(a-b) == 2 and avg not in plus_x_lines:
            candidates_plus_x.add(avg)
    candidates_minus_x = set()
    for a, b in itertools.combinations(minus_x_lines, 2):
        avg = (a+b)//2
        if abs(a-b) == 2 and avg not in minus_x_lines:
            candidates_minus_x.add(avg)

    for a, b in itertools.product(candidates_minus_x, candidates_plus_x):
        x = (b-a)// -2
        y = -x + a
        if 0 <= x <= bounds and 0 <= y <= bounds:
            return x * 4_000_000 + y

        

if __name__ == "__main__":
    input_data = read_input("day15")
    print(f"part1 -> {part1(input_data)}")
    print(f"part2 -> {part2(input_data)}")
