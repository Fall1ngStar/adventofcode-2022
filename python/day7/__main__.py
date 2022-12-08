from lib import read_input

def get_nested_key(key, dic):
    current = dic[key[0]]
    for part in key[1:]:
        current = current[part]
    return current

def calc_size(tree):
    score = 0
    for value in tree.values():
        if isinstance(value, dict):
            score += calc_size(value)
        else:
            score += value
    return score


def get_score(tree):
    score = 0
    for value in tree.values():
        if not isinstance(value, dict):
            continue
        if (size := calc_size(value)) <= 100000:
            score += size
        score += get_score(value)
    return score

def get_tree(input_data):
    tree = {"/": {}}
    current = []
    for line in input_data.splitlines():
        cmd_parts = line.split(" ")
        if line.startswith("$ cd .."):
            current.pop(-1)
            continue
        if line.startswith("$ cd"):
            current.append(cmd_parts[-1])
            continue
        if line.startswith("$ ls"):
            continue
        pos = get_nested_key(current, tree)
        if cmd_parts[0] == "dir":
            pos[cmd_parts[1]] = {}
        else:
            pos[cmd_parts[1]] = int(cmd_parts[0])
    return tree

def get_score_2(tree, prefix=""):
    result = []
    for key, value in tree.items():
        if not isinstance(value, dict):
            continue
        result.append((f"{prefix}/{key}", calc_size(value)))
        result += get_score_2(value, f"{prefix}/{key}")
    return result

def part1(input_data):
    tree = get_tree(input_data)
    return get_score(tree)

def part2(input_data):
    tree = get_tree(input_data)
    result = get_score_2(tree)
    sort = sorted(result, key=lambda x: x[1])
    total_size = sort[-1][1]
    for (_, size) in sort:
        if total_size - size < 40000000:
            return size

if __name__ == "__main__":
    input_data = read_input("day7")
    print(f"part1 -> {part1(input_data)}")
    print(f"part2 -> {part2(input_data)}")
