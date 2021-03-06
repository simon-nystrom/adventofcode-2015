import sys
from functools import reduce

puzzle_input = sys.stdin.read().rstrip().splitlines()


def surface_area(l, w, h):
    slack = min(l * w, w * h, l * h)
    return 2 * (l * w + w * h + h * l) + slack


def a(puzzle_input):

    # Use a helper function rather than a lambda, way more readable!
    def helper(total_area, dimensions):
        # Parse the dimensions into their l, w and h respectively and turn them into ints
        [l, w, h] = map(int, dimensions.split('x'))
        return total_area + surface_area(l, w, h)

    return reduce(helper, puzzle_input, 0)


def shortest_ribbon(l, w, h):
    bow = l * w * h
    return min(2 * (l + w), 2 * (w + h), 2 * (l + h)) + bow


def b(puzzle_input):
    # Use a helper function rather than a lambda, way more readable!
    def helper(total_area, dimensions):
        # Parse the dimensions into their l, w and h respectively and turn them into ints
        [l, w, h] = map(int, dimensions.split('x'))
        return total_area + shortest_ribbon(l, w, h)

    return reduce(helper, puzzle_input, 0)


print(a(puzzle_input))
print(b(puzzle_input))
