import sys

def intcode(data):
    data = [int(x) for x in data.split(',')]
    index = 0
    data[1] = 12
    data[2] = 2

    while data[index] != 99:
        if data[index] == 1:
            data[data[index + 3]] = data[data[index + 1]] + data[data[index + 2]]
        elif data[index] == 2:
            data[data[index + 3]] = data[data[index + 1]] * data[data[index + 2]]

        index += 4
    return data[0]


if __name__ == "__main__":
    data_file = sys.argv[1]
    with open(data_file) as f:
        print(intcode(f.read()))
