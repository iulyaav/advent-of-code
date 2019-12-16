import sys
from math import gcd

def read_map(data):
    row = len(data)
    col = len(data[0])

    asteroids = {}
    total_a = sum([x.count('#') for x in data])

    for i in range(row):
        for j in range(col):
            if data[i][j] == "#":
                asteroids[(i, j)] = total_a - 1
    
    return asteroids


def compute_visibility(asteroids):

    for a in asteroids.keys():
        lines = set()
        for b in asteroids.keys():
            if a == b:
                continue
            x = a[0] - b[0]
            y = a[1] - b[1]
            g = gcd(x, y)
            x = x // g
            y = y // g
            if (x, y) not in lines:
                lines.add((x, y))
            else:
                asteroids[a] -= 1
    
    return max(asteroids.values())


if __name__ == "__main__":
    data_file = sys.argv[1]
    data = None
    with open(data_file) as f:
        data = f.read().split('\n')

    a = read_map(data)
    print(compute_visibility(a))
