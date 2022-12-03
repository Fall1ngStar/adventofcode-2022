from lib import read_input


def part1(input_data):
    processed = [
        sum(int(line) for line in group.splitlines())
        for group in input_data.split("\n\n")
    ]
    return max(processed)


def part2(input_data):
    processed = [
        sum(int(line) for line in group.splitlines())
        for group in input_data.split("\n\n")
    ]
    return sum(sorted(processed)[-3:])


if __name__ == "__main__":
    input_data = read_input("day1")
    print(f"{part1(input_data)=}")
    print(f"{part2(input_data)=}")
