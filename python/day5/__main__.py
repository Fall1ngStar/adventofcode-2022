import re
from lib import read_input


def parse_input(input_data):
    raw_crates, raw_instructions = input_data.split("\n\n")
    raw_crates = raw_crates.splitlines()[:-1]
    crates = [[] for _ in range(len(raw_crates[0]) // 4 + 1)]
    for line in raw_crates:
        for i in range(1, len(line), 4):
            if line[i] == " ":
                continue
            col = (i - 1) // 4
            crates[col] = [line[i]] + crates[col]

    instructions = []
    for line in raw_instructions.splitlines():
        match = re.match(r"move (\d+) from (\d+) to (\d+)", line)
        a, b, c = match.groups()
        instructions.append([*map(int, (a, b, c))])
    return crates, instructions


def part1(input_data):
    crates, instructions = parse_input(input_data)
    for num, from_, to in instructions:
        to_move = crates[from_ - 1][-num:][::-1]
        crates[from_ - 1] = crates[from_ - 1][:-num]
        crates[to - 1] += to_move
    return "".join([stack[-1] for stack in crates])


def part2(input_data):
    crates, instructions = parse_input(input_data)
    for num, from_, to in instructions:
        to_move = crates[from_ - 1][-num:]
        crates[from_ - 1] = crates[from_ - 1][:-num]
        crates[to - 1] += to_move
    return "".join([stack[-1] for stack in crates])


if __name__ == "__main__":
    input_data = read_input("day5")
    print(f"part1 -> {part1(input_data)}")
    print(f"part2 -> {part2(input_data)}")
