import sys

INSTRUCTIONS = {
        'R': lambda x, y: (x+1, y),
        'L': lambda x, y: (x-1, y),
        'U': lambda x, y: (x, y+1), 
        'D': lambda x, y: (x, y-1)
}

def compute_location(path, also_check=None):
    locations = {}
    prev_step = (0, 0)
    total_steps = 0
    for step in path:
        for i in range(int(step[1:])):
            total_steps += 1
            new_step = INSTRUCTIONS[step[0]](prev_step[0], prev_step[1])
            if locations.get(new_step, None) is None:
                locations[new_step] = total_steps
            prev_step = new_step
    
    if also_check is not None:
        meeting_points = set(locations.keys()).intersection(set(also_check.keys()))
        result = {}
        for point in meeting_points:
            result[point] = locations[point] + also_check[point]
        return result

    return locations

def crossed_wires(first, second):
    first = first.split(',')
    second = second.split(',')
    starting_point = (0, 0)

    first_result = compute_location(first)
    shared_locations = compute_location(second, also_check=first_result)
    
    return min(shared_locations.values())

if __name__ == "__main__":
    data = None
    with open(sys.argv[1]) as f:
        first, second, _ = f.read().split('\n')
    print(crossed_wires(first, second))
