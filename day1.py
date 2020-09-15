from functools import reduce

with open("day1_input.txt") as file:
    puzzle_input = file.read()


def part1():
    return reduce(
        lambda floor, instr: floor + 1 if instr == '(' else floor - 1,
        puzzle_input,
        0
    )


def part2():
    floor = 0
    for (i, instr) in enumerate(puzzle_input, start=1):
        if (instr == '('):
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            return i


print(part1())
print(part2())
