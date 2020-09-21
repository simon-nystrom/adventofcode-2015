import sys
import re
from collections import namedtuple

puzzle_input = sys.stdin.read().rstrip().splitlines()

Point = namedtuple('Point', ['x', 'y'])
Instruction = namedtuple('Instruction', ['op', 'start', 'end'])


def get_instruction(line):
    match = re.match(
        r'(turn on|toggle|turn off)\s(\d{1,3}),(\d{1,3})\sthrough\s(\d{1,3}),(\d{1,3})', line)
    return Instruction(
        match.group(1),
        start=Point(int(match.group(2)), int(match.group(3))),
        end=Point(int(match.group(4)), int(match.group(5))))


def a(puzzle_input):
    lights = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in puzzle_input:
        [op, start, end] = get_instruction(line)
        for x in range(start.x, end.x + 1):
            for y in range(start.y, end.y + 1):
                if op == 'turn on':
                    lights[y][x] = 1
                elif op == 'toggle':
                    lights[y][x] = 1 if lights[y][x] == 0 else 0
                else:
                    lights[y][x] = 0
    num_lights_on = 0
    for row in lights:
        for x in row:
            num_lights_on += x
    return num_lights_on


def b(puzzle_input):
    lights = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in puzzle_input:
        [op, start, end] = get_instruction(line)
        for x in range(start.x, end.x + 1):
            for y in range(start.y, end.y + 1):
                if op == 'turn on':
                    lights[y][x] += 1
                elif op == 'toggle':
                    lights[y][x] += 2
                else:
                    lights[y][x] = max(0, lights[y][x] - 1)
    num_lights_on = 0
    for row in lights:
        for x in row:
            num_lights_on += x
    return num_lights_on


print(a(puzzle_input))
print(b(puzzle_input))
