import sys
from math import gcd, atan2, pi

def read_map(data):
    row = len(data)
    col = len(data[0])

    asteroids = {}
    total_a = sum([x.count('#') for x in data])

    for i in range(row):
        for j in range(col):
            if data[i][j] == "#":
                asteroids[(j, i)] = [total_a - 1]
    
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
                asteroids[a].append((compute_angle(a, b), (x, y), b))
            else:
                asteroids[a][0] -= 1
    
    max_value = max([x [0] for x in asteroids.values()])
    max_point = [x for x in asteroids.keys() if asteroids[x][0] == max_value][0]
    return max_value, max_point


def compute_angle(a, b):
    return atan2(b[0] - a[0], a[1] - b[1]) % (2 * pi)

def rotation(asteroids, focus):
    lines = asteroids[focus][1:]
    sorted_list = sorted(lines, key=lambda x: (x[0]))
    the_200th = sorted_list[199]
    print(the_200th[2][0] * 100 + the_200th[2][1])


if __name__ == "__main__":
    data_file = sys.argv[1]
    data = None
    with open(data_file) as f:
        data = f.read().split('\n')

    a = read_map(data)
    v, p = compute_visibility(a)
    print(v, p)
    rotation(a, p)