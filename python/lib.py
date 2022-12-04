import os


def read_input(day, case="input"):
    with open(os.path.join(day, case)) as file:
        return file.read()


def chunker(seq, size):
    return (seq[pos : pos + size] for pos in range(0, len(seq), size))
