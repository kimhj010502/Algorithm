import math
import sys

t = int(input())

def is_in_planet(x, y, cx, cy, r):
    distance = math.sqrt( (x-cx)**2 + (y-cy)**2 )
    if distance < r:
        return 1
    else:
        return 0

for _ in range(t):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())

    n = int(input())
    planet_list = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
    result = 0

    for i in range(n):
        start = is_in_planet(x1, y1, planet_list[i][0], planet_list[i][1], planet_list[i][2])
        end = is_in_planet(x2, y2, planet_list[i][0], planet_list[i][1], planet_list[i][2])
        #print(f'start: {start}, end: {end}')
        if start != end:
            result += 1
    print(result)