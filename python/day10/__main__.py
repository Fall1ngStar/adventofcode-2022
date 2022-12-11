from lib import read_input, chunker


def part1(input_data):
    register = 1
    history = []
    for line in input_data.splitlines():
        history.append(register)
        if line == "noop":
            continue
        _, to_add = line.split(" ")
        history.append(register)
        register += int(to_add)
    result = history[19] * 20
    print(result)
    for i in range(59, 220, 40):
        result += history[i] * (i + 1)
    return result


def part2(input_data):
    register = 1
    history = []
    for line in input_data.splitlines():
        history.append(register)
        if line == "noop":
            continue
        _, to_add = line.split(" ")
        history.append(register)
        register += int(to_add)
    crt = [
        "X" if i % 40 - 1 <= value <= i % 40 + 1 else " "
        for i, value in enumerate(history)
    ]
    for chunk in chunker(crt, 40):
        print("".join(chunk))


if __name__ == "__main__":
    input_data = read_input("day10")
    print(f"part1 -> {part1(input_data)}")
    print(f"part2 -> {part2(input_data)}")
