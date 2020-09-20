import sys
import hashlib

puzzle_input = sys.stdin.read().rstrip()


def mine_advent_coins_until(puzzle_input, starts_with):
    result = ""
    idx = 0
    while not result.startswith(starts_with):
        idx += 1
        current_string = puzzle_input + str(idx)
        result = hashlib.md5(current_string.encode("utf-8")).hexdigest()
    return idx


def a(puzzle_input):
    return mine_advent_coins_until(puzzle_input, "00000")


def b(puzzle_input):
    return mine_advent_coins_until(puzzle_input, "000000")


print(a(puzzle_input))
print(b(puzzle_input))
