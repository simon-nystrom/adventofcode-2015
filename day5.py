import sys
from functools import reduce
import re

puzzle_input = sys.stdin.read().rstrip().splitlines()


def is_nice(string):
    has_sequential_letters = re.match(r'.*(ab|cd|pq|xy).*', string) is not None
    has_3_vowels = re.match(r'(.*[aeiou].*){3}', string) is not None
    has_two_in_a_row = re.match(r'.*([a-z])\1.*', string) is not None
    return has_3_vowels and has_two_in_a_row and not has_sequential_letters


def is_nice_2(string):
    has_pair = re.match(r'.*([a-z]{2}).*\1.*', string) is not None
    has_repeat = re.match(r'.*([a-z]).\1.*', string) is not None
    return has_pair and has_repeat


def a(puzzle_input):
    return reduce(lambda acc, s: acc + 1 if is_nice(s) else acc, puzzle_input, 0)


def b(puzzle_input):
    return reduce(lambda acc, s: acc + 1 if is_nice_2(s) else acc, puzzle_input, 0)


print(a(puzzle_input))
print(b(puzzle_input))
