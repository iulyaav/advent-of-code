import copy

def print_matrix(matrix, r, c):
    m = []
    for i in range(r):
        line = []
        for j in range(c):
            line.append(matrix[(i, j)])
        m.append(line)
    print("\n".join(["".join(x) for x in m]))


def lookup(matrix, point, stop_after_one=False):
    occupied = 0
    a, b = point
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    status = [0] * 8
    index = [(a, b), (a, b), (a, b), (a, b), (a, b), (a, b), (a, b), (a, b)]
    s = 0

    while sum(status) < 8:
        for i in range(8):
            if status[i] == 1:
                continue
            index[i] = (index[i][0] + directions[i][0], index[i][1] + directions[i][1])
            seat = matrix.get(index[i], "L")
            if seat == "#":
                occupied += 1
                status[i] = 1
            elif seat == "L":
                status[i] = 1
        if stop_after_one:
            break        

    return occupied

def eleven_a():
    with open("input_11.txt", "r") as f:
        rows = {}
        line = f.readline()
        r = 0
        c = None
        while line:
            tmp = list(line.strip())
            if c is None:
                c = len(tmp)
            
            for i in range(c):
                rows[(r, i)] = tmp[i]
            line = f.readline()
            r += 1

        made_change = True
        prev = copy.deepcopy(rows)
        current = {}
        
        while made_change:
            made_change = False
            for i in range(r):
                for j in range(c):
                    if prev[(i, j)] == ".":
                        current[(i, j)] = "."
                    elif prev[(i, j)] == "L":
                        if lookup(prev, (i, j), True) == 0:
                            made_change = True
                            current[(i, j)] = "#"
                        else:
                            current[(i, j)] = "L"
                    elif prev[(i, j)] == "#":
                        if lookup(prev, (i, j), True) >= 4:
                            made_change = True
                            current[(i, j)] = "L"
                        else:
                            current[(i, j)] = "#"
            prev = copy.deepcopy(current)
            current = {}
        
        cnt = 0
        # print_matrix(prev, r, c)
        for _, v in prev.items():
            if v == "#":
                cnt += 1
        return cnt

def eleven_b():
    with open("input_11.txt", "r") as f:
        rows = {}
        line = f.readline()
        r = 0
        c = None
        while line:
            tmp = list(line.strip())
            if c is None:
                c = len(tmp)
            
            for i in range(c):
                rows[(r, i)] = tmp[i].strip()
            line = f.readline()
            r += 1

        made_change = True
        prev = copy.deepcopy(rows)
        current = {}
        
        while made_change:
            made_change = False
            for i in range(r):
                for j in range(c):
                    if prev[(i, j)] == ".":
                        current[(i, j)] = "."
                    elif prev[(i, j)] == "L":
                        if lookup(prev, (i, j)) == 0:
                            made_change = True
                            current[(i, j)] = "#"
                        else:
                            current[(i, j)] = "L"
                    elif prev[(i, j)] == "#":
                        if lookup(prev, (i, j)) >= 5:
                            made_change = True
                            current[(i, j)] = "L"
                        else:
                            current[(i, j)] = "#"
            prev = copy.deepcopy(current)
            current = {}
        
        cnt = 0
        # print_matrix(prev, r, c)
        for _, v in prev.items():
            if v == "#":
                cnt += 1
        return cnt

print(eleven_a())