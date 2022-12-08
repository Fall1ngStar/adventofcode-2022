from lib import read_input


def part1(input_data):
    score = 0
    for line in input_data.splitlines():

        a, b = line.split(",")
        start_a, end_a = map(int, a.split("-"))
        start_b, end_b = map(int, b.split("-"))

        if start_a <= start_b and end_b <= end_a:
            score += 1
        elif start_b <= start_a and end_a <= end_b:
            score += 1
    return score


def part2(input_data):
    score = 0
    for line in input_data.splitlines():

        a, b = line.split(",")
        start_a, end_a = map(int, a.split("-"))
        start_b, end_b = map(int, b.split("-"))
        range_a = set(range(start_a, end_a + 1))
        range_b = set(range(start_b, end_b + 1))
        if range_a & range_b:
            score += 1
    return score


if __name__ == "__main__":
    input_data = read_input("day04")
    print(f"part1 -> {part1(input_data)}")
    print(f"part2 -> {part2(input_data)}")
