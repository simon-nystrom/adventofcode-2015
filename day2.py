from functools import reduce

with open("day2_input.txt") as file:
    puzzle_input = file.read().splitlines()


def surface_area(l, w, h):
    slack = min(l * w, w * h, l * h)
    return 2 * l * w + 2 * w * h + 2 * h * l + slack


def part1(puzzle_input):

    # Use a helper function rather than a lambda, way more readable!
    def helper(total_area, dimensions):
        # Parse the dimensions into their l, w and h respectively and turn them into ints
        [l, w, h] = map(int, dimensions.split('x'))
        return total_area + surface_area(l, w, h)

    return reduce(helper, puzzle_input, 0)


def shortest_bow(l, w, h):
    bow = l * w * h
    return min(l * 2 + w * 2, w * 2 + h * 2, l * 2 + h * 2) + bow


def part2(puzzle_input):
    # Use a helper function rather than a lambda, way more readable!
    def helper(total_area, dimensions):
        # Parse the dimensions into their l, w and h respectively and turn them into ints
        [l, w, h] = map(int, dimensions.split('x'))
        return total_area + shortest_bow(l, w, h)

    return reduce(helper, puzzle_input, 0)


print(part1(puzzle_input))
print(part2(puzzle_input))
