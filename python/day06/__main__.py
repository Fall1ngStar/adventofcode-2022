from lib import read_input


def part1(input_data):
    for i in range(4, len(input_data)):
        chunk = input_data[i - 4 : i]
        if len(chunk) == len(set(chunk)):
            return i


def part2(input_data):
    for i in range(14, len(input_data)):
        chunk = input_data[i - 14 : i]
        if len(chunk) == len(set(chunk)):
            return i


if __name__ == "__main__":
    input_data = read_input("day06")
    print(f"part1 -> {part1(input_data)}")
    print(f"part2 -> {part2(input_data)}")
