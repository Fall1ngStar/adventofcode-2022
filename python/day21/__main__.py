from lib import read_input

OPERATORS = {
    "/": lambda a, b: a / b,
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
}


def parse_input(input_data):
    result = {}
    for line in input_data.splitlines():
        key, value = line.split(": ")
        try:
            result[key] = int(value)
        except ValueError:
            result[key] = value
    return result


def get_value(dic, key):
    value = dic[key]
    try:
        a, op, b = value.split(" ")
        value = OPERATORS[op](get_value(dic, a), get_value(dic, b))
        dic[key] = value
    except AttributeError:
        pass
    return value


def part1(input_data):
    data = parse_input(input_data)
    return int(get_value(data, "root"))


def part2(input_data):
    data = parse_input(input_data)
    data["humn"] = 1j
    key_a, _, key_b = data["root"].split(" ")
    a: complex = get_value(data, key_a)
    b = get_value(data, key_b)
    return int((b - a.real) / a.imag)


if __name__ == "__main__":
    input_data = read_input("day21")
    print(f"part1 -> {part1(input_data)}")
    print(f"part2 -> {part2(input_data)}")
