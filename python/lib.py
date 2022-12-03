import os


def read_input(day, case="input"):
    with open(os.path.join(day, case)) as file:
        return file.read()
