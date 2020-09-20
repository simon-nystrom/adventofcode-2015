import requests
import sys
import os.path

day = sys.argv[1]
year = sys.argv[2]
verbose = len(sys.argv) <= 3 or sys.argv[3] != '-q'
AOC_SESSION_COOKIE = os.getenv('AOC_SESSION_COOKIE')


def get_file_name(day):
    return f'{year}_{day}_input.txt'


file_name = get_file_name(day)
if os.path.isfile(file_name):
    file = open(file_name, 'r')
    if (verbose):
        print(file.read())
    file.close()
    exit(0)

response = requests.get(
    f"https://adventofcode.com/{year}/day/{day}/input",
    cookies={'session': AOC_SESSION_COOKIE})

file = open(file_name, 'w')
file.write(response.text)
file.close()
if (verbose):
    print(response.text)


# for n ({1..25}); do python3 util/util.py ; done
