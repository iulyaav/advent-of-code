
def main(arg: str, data: str):
    trees = []
    for line in data.split('\n'):
        trees.append([int(x) for x in line])

    def look_up(x, y):
        result = []
        for i in range(x-1, -1, -1):
            result.append(trees[i][y])
        return result
    
    def look_down(x, y):
        result = []
        for i in range(x+1, len(trees)):
            result.append(trees[i][y])
        return result

    def look_left(x, y):
        result = []
        for i in range(y-1, -1, -1):
            result.append(trees[x][i])
        return result
    
    def look_right(x, y):
        result = []
        for i in range(y+1, len(trees[0])):
            result.append(trees[x][i])
        return result
    
    def how_many_trees(list_of_trees, val):
        idx = 0
        for tree in list_of_trees:
            idx += 1
            if tree >= val:
                break
        return idx
    
    result = 0

    for i in range(len(trees)):
        for j in range(len(trees[0])):
            up = look_up(i, j)
            left = look_left(i, j)
            down = look_down(i, j)
            right = look_right(i, j)
            if arg == "a":
                if trees[i][j] > max(up or [-1]) or \
                    trees[i][j] > max(left or [-1]) or \
                        trees[i][j] > max(down or [-1]) or \
                            trees[i][j] > max(right or [-1]):
                    result += 1
            else:
                score = how_many_trees(up, trees[i][j]) * \
                        how_many_trees(down, trees[i][j]) * \
                        how_many_trees(right, trees[i][j]) * \
                        how_many_trees(left, trees[i][j])
                result = max(result, score)

    

    print(result)

        
    

    

    