
def one_a():
    with open("input_1.txt", "r") as f:
        d = {}
        data = [int(x) for x in f.read().split('\n')]
        for item in data:
            d[item] = True
            if 2020 - item in d.keys():
                return item * (2020 - item)

def one_b():
    with open("input_1.txt", "r") as f:
        d = {}
        data = [int(x) for x in f.read().split('\n')]
        n = len(data)
        
        for i in range(n):
            for j in range(i+1, n):
                d[data[i] + data[j]] = (i, j)
        for k in range(n):
            if 2020 - data[k] in d.keys() and k not in d[2020 - data[k]]:
                i, j = d[2020 - data[k]]
                return data[k] * data[i] * data[j]
