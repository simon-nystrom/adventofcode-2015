import requests
import sys

day = sys.argv[1]
cookies = dict(
    session='53616c7465645f5f05b035a13e6e753151381dc98240c33f50757e65d4a0e80147e04aea3c56623c748e96f918e9a0c3')
response = requests.get(
    f"https://adventofcode.com/2015/day/{day}/input", cookies=cookies)

file = open(f'day{day}_input.txt', 'w')
file.write(response.text)
