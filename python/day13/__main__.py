from lib import read_input


def correct_order(left, right):
    for a, b in zip(left, right):
        if isinstance(a, int) and isinstance(b, int):
            if a < b:
                return True
            if a == b:
                continue
            if a > b:
                return False
        elif isinstance(a, list) and isinstance(b, list):
            list_result = correct_order(a, b)
            if list_result is False or list_result is True:
                return list_result
        else:
            if isinstance(a, int):
                a = [a]
            else:
                b = [b]
            list_result = correct_order(a, b)
            if list_result is False or list_result is True:
                return list_result
    if len(right) < len(left):
        return False
    elif len(right) > len(left):
        return True
    else:
        return None


def part1(input_data):
    valid = []
    for i, group in enumerate(input_data.split("\n\n")):
        raw_a, raw_b = group.splitlines()
        left = eval(raw_a)
        right = eval(raw_b)
        if correct_order(left, right):
            valid.append(i + 1)
    return sum(valid)


def part2(input_data):
    packets = [
        eval(line) for group in input_data.split("\n\n") for line in group.splitlines()
    ]

    sort = [[[2]], [[6]]]
    for packet in packets:
        i = 0
        while i < len(sort) and not correct_order(packet, sort[i]):
            i += 1
        sort.insert(i, packet)
    return (sort.index([[2]]) + 1) * (sort.index([[6]]) + 1)


if __name__ == "__main__":
    input_data = read_input("day13")
    print(f"part1 -> {part1(input_data)}")
    print(f"part2 -> {part2(input_data)}")
