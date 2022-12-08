from lib import chunker, read_input

SCORE = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def part1(input_data):
    total = 0
    for line in input_data.splitlines():
        size = len(line) // 2
        first, second = line[:size], line[size:]
        common = {*first} & {*second}
        total += SCORE.index(common.pop())
    return total


def part2(input_data):
    total = 0
    lines = [*input_data.splitlines()]
    for a, b, c in chunker(lines, 3):
        common = {*a} & {*b} & {*c}
        total += SCORE.index(common.pop())
    return total


if __name__ == "__main__":
    input_data = read_input("day03")
    print(f"part1 -> {part1(input_data)}")
    print(f"part2 -> {part2(input_data)}")
