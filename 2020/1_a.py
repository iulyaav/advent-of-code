
def one():
    with open("input_1.txt", "r") as f:
        d = {}
        data = [int(x) for x in f.read().split('\n')]
        for item in data:
            d[item] = True
            if 2020 - item in d.keys():
                return item * (2020 - item)

    
print(one())