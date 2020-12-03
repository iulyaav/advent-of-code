from functools import reduce

def three_a():
    with open("input_3.txt", "r") as f:
        slope = f.read().split('\n')
        height = len(slope)
        width = len(slope[0])

        x, y = 0, 0
        trees = 0 
        while y < height - 1:
            # move
            y += 1
            x = (x + 3) % width
            if slope[y][x] == "#":
                trees += 1
        return trees


def three_b():
    with open("input_3.txt", "r") as f:
        slope = f.read().split('\n')
        height = len(slope)
        width = len(slope[0])

        cases = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

        def move(coord_x, coord_y):
            x, y = 0, 0
            trees = 0
            while y < height - 1:
                # move
                y += coord_y
                x = (x + coord_x) % width
                if slope[y][x] == "#":
                    trees += 1
            return trees
    tree_list = [move(x[0], x[1]) for x in cases]   
    return reduce((lambda x, y: x * y), tree_list)


print(three_b())