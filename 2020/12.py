directions = {
    "N": (-1, 0),
    "W": (0, -1),
    "S": (1, 0),
    "E": (0, 1)
}

def compute_direction(origin, direc, val):
    order = {
        "L": {
            "N": ["W", "S", "E"],
            "W": ["S", "E", "N"],
            "S": ["E", "N", "W"],
            "E": ["N", "W", "S"]
        },
        "R": {
            "N": ["E", "S", "W"],
            "W": ["N", "E", "S"],
            "S": ["W", "N", "E"],
            "E": ["S", "W", "N"]
        }
    }
    return order[direc][origin][val // 90 - 1]


def rotate(origin, direc, val):
    a, b = origin
    a, b = b, a
    if direc == "L":
        a = -a
    elif direc == "R":
        b = -b
    return (a, b)


def manhattan_distance(point):
    return abs(point[0]) + abs(point[1])


def twelve_a():
    start = (0, 0)
    direction = "E"

    with open("input_12.txt", "r") as f:
        
        line = f.readline()
        while line:
            command = line[0]
            value = int(line[1:])
            if command in directions:
                start = (start[0] + (directions[command][0]*value), start[1] + (directions[command][1]*value))
            elif command == "F":
                start = (start[0] + (directions[direction][0]*value), start[1] + (directions[direction][1]*value))
            elif command in ["R", "L"]:
                direction = compute_direction(direction, command, value)
            line = f.readline()
    return manhattan_distance(start)

def twelve_b():
    start = (0, 0)
    direction = "E"
    waypoint = (-1, 10)

    with open("input_12.txt", "r") as f:
        line = f.readline().strip()
        while line:
            command = line[0]
            value = int(line[1:])
            if command in directions:
                waypoint = (waypoint[0] + (directions[command][0]*value), waypoint[1] + (directions[command][1]*value))
            elif command == "F":
                start = (start[0] + (waypoint[0] * value), start[1] + (waypoint[1] * value))
            elif command in ["R", "L"]:
                for i in range(value // 90):
                    waypoint = rotate(waypoint, command, value)
            line = f.readline().strip()
    
    return manhattan_distance(start)

print(twelve_b())