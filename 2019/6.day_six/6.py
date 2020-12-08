import sys

def orbits(data):
    orbits_map = {}
    for line in data:
        ob1, ob2 = line.split(')')
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

    # print(sum([x[1] for x in orbits_map.values()]))
    return orbits_map

def create_path(nodes, start, end=""):
    path = []
    current_node = start
    while True:
        if current_node == end or nodes.get(current_node, None) is None:
            break
        next_node = nodes[current_node][0]
        path.append(next_node)
        current_node = next_node
    return path[::-1]

def get_to_santa(orbits):
    my_path = create_path(orbits, "YOU")
    if "SAN" in my_path:
        print(len(my_path) - my_path.index("SAN"))
    else:
        santa_path = create_path(orbits, "SAN")
        # Find first step that is different
        not_found = True
        i = 0
        while not_found:
            if santa_path[i] != my_path[i]:
                break
            i += 1
        print(len(santa_path) + len(my_path) - 2 * i)


if __name__ == "__main__":
    data = None
    with open(sys.argv[1]) as f:
        data = [x for x in f.read().split('\n') if x != '']
    orbits_data = orbits(data)
    get_to_santa(orbits_data)
