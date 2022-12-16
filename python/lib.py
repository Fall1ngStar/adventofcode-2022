import os
from typing import Self


def read_input(day, case="input"):
    with open(os.path.join(day, case)) as file:
        return file.read()


def chunker(seq, size):
    return (seq[pos : pos + size] for pos in range(0, len(seq), size))


def window(seq, size):
    for i in range(size, len(seq) + 1):
        yield seq[i - size : i]


def nor(num: int) -> int:
    if num == 0:
        return 0
    return num // abs(num)


class Point:
    def __init__(self, *args):
        self.dimensions = list(args)

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f"Point({', '.join(map(str, self.dimensions))})"

    def __add__(self, other: Self):
        if len(other.dimensions) != len(self.dimensions):
            raise ValueError("Points dimensions does not match")
        return Point(*[a + b for a, b in zip(self.dimensions, other.dimensions)])

    def __neg__(self):
        return Point(*[-num for num in self.dimensions])

    @property
    def nor(self):
        return Point(*[nor(num) for num in self.dimensions])

    def __sub__(self, other: Self) -> Self:
        if len(other.dimensions) != len(self.dimensions):
            raise ValueError("Points dimensions does not match")
        return self + -other

    def __eq__(self, other: Self) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return all([a == b for a, b in zip(self.dimensions, other.dimensions)])

    def __hash__(self) -> int:
        return hash(tuple(self.dimensions))

    def __iter__(self):
        return iter(self.dimensions)

    def __len__(self):
        return sum([abs(val) for val in self.dimensions])
    
    def __mul__(self, value):
        return Point(*[dim * value for dim in self.dimensions])

    def __getitem__(self, key):
        return self.dimensions[key]

def print_on_map(rows: int, cols: int, **kwargs: dict[str, tuple[int, int]]):
    result = [["." for _ in range(cols)] for _ in range(rows)]
    for key, (x, y) in kwargs.items():
        result[y][x] = key[0]
    for line in result[::-1]:
        print("".join(line))
    print()
