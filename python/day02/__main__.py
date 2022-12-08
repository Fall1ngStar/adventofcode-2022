from lib import read_input

ROCK = "ROCK"
PAPER = "PAPER"
SCISOR = "SCISOR"
MAP = {"A": ROCK, "B": PAPER, "C": SCISOR, "X": ROCK, "Y": PAPER, "Z": SCISOR}

WIN = {
    ROCK: {
        ROCK: 3,
        PAPER: 0,
        SCISOR: 6,
    },
    PAPER: {
        ROCK: 6,
        PAPER: 3,
        SCISOR: 0,
    },
    SCISOR: {
        ROCK: 0,
        PAPER: 6,
        SCISOR: 3,
    },
}
FLIPPED = {key: {b: a for a, b in value.items()} for key, value in WIN.items()}

END = {"X": 6, "Y": 3, "Z": 0}
SCORE = {
    ROCK: 1,
    PAPER: 2,
    SCISOR: 3,
}


def part1(input_data):
    score = 0
    for he, me in input_data:
        me = MAP[me]
        he = MAP[he]
        score += SCORE[me]
        score += WIN[me][he]
    return score


def part2(input_data):
    score = 0
    for he, end in input_data:
        he = MAP[he]
        me = FLIPPED[he][END[end]]
        score += SCORE[me]
        score += WIN[me][he]
    return score


if __name__ == "__main__":
    input_data = read_input("day02")
    input_data = [line.split(" ") for line in input_data.splitlines()]
    print(f"{part1(input_data)=}")
    print(f"{part2(input_data)=}")
