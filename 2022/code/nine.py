def move_row(point_a, point_b):
    if point_b[0] < point_a[0]:
        return point_b[0] + 1
    return point_b[0] - 1

def move_col(point_a, point_b):
    if point_a[1] > point_b[1]:
        return point_b[1] + 1
    return point_b[1] - 1

def move_tail(point_a, point_b):
    if abs(point_a[0] - point_b[0]) <= 1 and abs(point_a[1] - point_b[1]) <= 1:
        return point_b
    if point_a[0] == point_b[0] and abs(point_a[1] - point_b[1]) > 1:
        point_b[1] = move_col(point_a, point_b)
    elif point_a[1] == point_b[1] and  abs(point_a[0] - point_b[0]) > 1:
        point_b[0] = move_row(point_a, point_b)
    else:
        point_b[0] = move_row(point_a, point_b)
        point_b[1] = move_col(point_a, point_b)
    
    return point_b

def main(arg: str, data: str):
    head = [0, 0]
    rope = []
    size = 1 if arg == "a" else 9
    for _ in range(size):
        rope.append([0,0])

    locations = set()
    locations.add((0, 0))
    moves_head = {"R": [1, 0], "L": [-1, 0], "U": [0, 1], "D": [0, -1]}
    for line in data.split('\n'):
        direction, steps = line.split(' ')
        steps = int(steps)

        for _ in range(steps):
            head[0] += moves_head[direction][0] 
            head[1] += moves_head[direction][1] 

            for i in range(size):
                prev = head if i == 0 else rope[i-1]
                rope[i] = move_tail(prev, rope[i])
            locations.add((rope[-1][0], rope[-1][1]))

    print(len(locations))