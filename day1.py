import sys
from functools import reduce

puzzle_input = sys.stdin.read()


def a(puzzle_input):
    return reduce(
        lambda floor, instr: floor + 1 if instr == '(' else floor - 1,
        puzzle_input,
        0
    )


def b(puzzle_input):
    floor = 0
    for i, instr in enumerate(puzzle_input, start=1):
        if (instr == '('):
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            return i


print(a(puzzle_input))
print(b(puzzle_input))
