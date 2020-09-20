import sys

puzzle_input = sys.stdin.read().rstrip()
print(puzzle_input)

direction_deltas = {
    ">": (1, 0),
    "<": (-1, 0),
    "^": (0, 1),
    "v": (0, -1)
}


def update_position(pos, delta):
    return (pos[0] + delta[0], pos[1] + delta[1])


def a(puzzle_input):
    pos = (0, 0)
    visited = set((pos[0], pos[1]))
    presents = 0
    for direction in puzzle_input:
        delta = direction_deltas[direction]
        pos = update_position(pos, delta)
        if pos not in visited:
            presents += 1
            visited.add(pos)
    return presents


def b(puzzle_input):
    santa_pos, robot_pos = (0, 0), (0, 0)
    visited = set((santa_pos[0], santa_pos[1]))
    presents = 0
    for i, direction in enumerate(puzzle_input):
        delta = direction_deltas[direction]

        if i % 2 == 0:
            santa_pos = update_position(santa_pos, delta)
            new_pos = santa_pos
        else:
            robot_pos = update_position(robot_pos, delta)
            new_pos = robot_pos

        if new_pos not in visited:
            presents += 1
            visited.add(new_pos)
    return presents


print(a(puzzle_input))
print(b(puzzle_input))
