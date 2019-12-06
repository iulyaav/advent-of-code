import sys

def orbits(data):
    orbits_map = {}
    for line in data:
        ob1, ob2 = line.split(')')
        # total_orbits = orbits_map[ob1][1] if orbits_map.get(ob1, None) is not None else 0
        orbits_map[ob2] = [ob1, 0]

    for node in orbits_map.keys():
        start = 1
        current_node = orbits_map[node][0]
        while True:
            if orbits_map.get(current_node, None) is None:
                break
            if orbits_map[current_node][1] != 0:
                start += orbits_map[current_node][1]
                break
            current_node = orbits_map[current_node][0]
            start += 1
        orbits_map[node][1] = start

    print(sum([x[1] for x in orbits_map.values()]))
    

if __name__ == "__main__":
    data = None
    with open(sys.argv[1]) as f:
        data = [x for x in f.read().split('\n') if x != '']
    orbits(data)
