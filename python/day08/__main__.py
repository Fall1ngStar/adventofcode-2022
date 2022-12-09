from lib import read_input


def up(x, y, trees):
    height = trees[x][y]
    for i in range(0, x):
        if trees[i][y] >= height:
            return False
    return True


def down(x, y, trees):
    height = trees[x][y]
    for i in range(x + 1, len(trees)):
        if trees[i][y] >= height:
            return False
    return True


def left(x, y, trees):
    height = trees[x][y]
    for i in range(0, y):
        if trees[x][i] >= height:
            return False
    return True


def right(x, y, trees):
    height = trees[x][y]
    for i in range(y + 1, len(trees[x])):
        if trees[x][i] >= height:
            return False
    return True


def is_visible(x, y, trees):
    values = [
        up(x, y, trees),
        down(x, y, trees),
        left(x, y, trees),
        right(x, y, trees),
    ]
    # print(f"{x},{y}->{trees[x][y]} up={values[0]} down={values[1]} left={values[2]} right={values[3]}")
    return any(values)


def part1(input_data):
    trees = [[int(c) for c in line] for line in input_data.splitlines()]
    # print(trees)
    score = 0
    for x in range(0, len(trees)):
        for y in range(0, len(trees[x])):
            if is_visible(x, y, trees):
                score += 1
    return score


def d_up(x, y, trees):
    score = 0
    height = trees[x][y]
    for i in range(x-1, -1, -1):
        if trees[i][y] >= height:
            return score + 1
        score += 1
    return score


def d_down(x, y, trees):
    score = 0
    height = trees[x][y]
    for i in range(x + 1, len(trees)):
        if trees[i][y] >= height:
            return score + 1
        score += 1
    return score


def d_left(x, y, trees):
    score = 0
    height = trees[x][y]
    for i in range(y -1, -1, -1):
        if trees[x][i] >= height:
            return score + 1
        score += 1
    return score


def d_right(x, y, trees):
    score = 0
    height = trees[x][y]
    for i in range(y + 1, len(trees[x])):
        if trees[x][i] >= height:
            return score + 1
        score += 1
    return score


def distance(x, y, trees):
    values = [
        d_up(x, y, trees),
        d_down(x, y, trees),
        d_left(x, y, trees),
        d_right(x, y, trees),
    ]
    print(f"{x},{y}->{trees[x][y]} up={values[0]} down={values[1]} left={values[2]} right={values[3]}")
    return (
        d_up(x, y, trees)
        * d_down(x, y, trees)
        * d_left(x, y, trees)
        * d_right(x, y, trees)
    )


def part2(input_data):
    trees = [[int(c) for c in line] for line in input_data.splitlines()]
    # print(trees)
    score = []
    for x in range(1, len(trees) - 1):
        for y in range(1, len(trees[x]) -1):
            if is_visible(x, y, trees):
                score.append(distance(x, y, trees))
    return max(score)


if __name__ == "__main__":
    input_data = read_input("day08")
    print(f"part1 -> {part1(input_data)}")
    print(f"part2 -> {part2(input_data)}")
