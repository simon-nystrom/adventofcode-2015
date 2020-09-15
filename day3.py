with open("day3_input.txt") as file:
    puzzle_input = file.read()

direction_deltas = {
    ">": (1, 0),
    "<": (-1, 0),
    "^": (0, 1),
    "v": (0, -1)
}


def part1(puzzle_input):
    pos = (0, 0)
    visited = {
        (pos[0], pos[1]): True
    }
    presents = 1
    for _, direction in enumerate(puzzle_input, start=1):
        delta = direction_deltas[direction]
        pos = (pos[0] + delta[0], pos[1] + delta[1])
        if pos not in visited:
            presents += 1
            visited[pos] = True
        # pass
    return presents


def part2(puzzle_input):
    santa_pos, robot_pos = (0, 0), (0, 0)
    visited = {
        (santa_pos[0], santa_pos[1]): True
    }
    presents = 1
    for i, direction in enumerate(puzzle_input, start=1):
        delta = direction_deltas[direction]

        if i % 2 == 0:
            santa_pos = (santa_pos[0] + delta[0], santa_pos[1] + delta[1])
            new_pos = santa_pos
        else:
            robot_pos = (robot_pos[0] + delta[0], robot_pos[1] + delta[1])
            new_pos = robot_pos

        if new_pos not in visited:
            presents += 1
            visited[new_pos] = True
        # pass
    return presents


print(part1(puzzle_input))
print(part2(puzzle_input))
