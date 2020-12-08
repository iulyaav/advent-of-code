import sys
import copy

def intcode(data, noun, verb):
    index = 0
    data[1] = noun
    data[2] = verb

    while data[index] != 99:
        if data[index] == 1:
            data[data[index + 3]] = data[data[index + 1]] + data[data[index + 2]]
        elif data[index] == 2:
            data[data[index + 3]] = data[data[index + 1]] * data[data[index + 2]]

        index += 4
    print(data)

    return data[0]


if __name__ == "__main__":
    data_file = sys.argv[1]
    with open(data_file) as f:
        data = [int(x) for x in f.read().split(',')]
        n = min(100, len(data))
        found = None
        results = []
        for i in range(n):
            for j in range(n):
                # print("Trying {} and {}".format(i, j)) 
                data_copy = copy.deepcopy(data)
                try:
                    result = intcode(data_copy, i, j)
                    if result == 19690720:
                        print("Evrika! Result is {}".format(i * 1000 + j))
                        break
                except IndexError:
                    pass

        

