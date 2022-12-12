import math
from lib import read_input


def parse_input(input_data):
    monkeys = {}
    for raw_monkey in input_data.split("\n\n"):
        lines = raw_monkey.splitlines()
        monkey_num = lines[0].removeprefix("Monkey ").removesuffix(":")
        items = [int(item) for item in lines[1].removeprefix("  Starting items: ").split(", ")]
        operation = lines[2].removeprefix("  Operation: new = ")
        divisible = int(lines[3].removeprefix("  Test: divisible by "))
        if_true = lines[4].removeprefix("    If true: throw to monkey ")
        if_false = lines[5].removeprefix("    If false: throw to monkey ")
        monkeys[monkey_num] = {
            "items": items,
            "operation": operation,
            "divisible": divisible,
            "if_true": if_true,
            "if_false": if_false,
            "inspect": 0
        }
    return monkeys


def part1(input_data):
    monkeys = parse_input(input_data)
    
    for _ in range(20):
        for monkey in monkeys.values():
            while monkey["items"]:
                current = monkey["items"].pop(0)
                new_value = eval(monkey["operation"], globals(), {"old": current})
                new_value //= 3
                if new_value % monkey["divisible"] == 0:
                    monkeys[monkey["if_true"]]["items"].append(new_value)
                else:
                    monkeys[monkey["if_false"]]["items"].append(new_value)
                monkey["inspect"] += 1
    *_, a, b = sorted([monkey["inspect"] for monkey in monkeys.values()])
    return a * b    

def part2(input_data):
    monkeys = parse_input(input_data)
    common_multiple = math.lcm(*[monkey["divisible"] for monkey in monkeys.values()])
    for _ in range(10_000):
        for monkey in monkeys.values():
            while monkey["items"]:
                current = monkey["items"].pop(0)
                new_value = eval(monkey["operation"], globals(), {"old": current})
                if new_value % monkey["divisible"] == 0:
                    target = monkeys[monkey["if_true"]]
                else:
                    target = monkeys[monkey["if_false"]]
                target["items"].append(new_value % common_multiple)
                monkey["inspect"] += 1
    *_, a, b = sorted([monkey["inspect"] for monkey in monkeys.values()])
    return a * b    


if __name__ == "__main__":
    input_data = read_input("day11")
    print(f"part1 -> {part1(input_data)}")
    print(f"part2 -> {part2(input_data)}")
