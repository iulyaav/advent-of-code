def ten_a():
    with open("input_10.txt", "r") as f:
        bag = sorted([int(x) for x in f.read().split('\n')])
        current = 0
        ones = 0
        threes = 1
        for item in bag:
            dif = item - current
            if dif == 1:
                ones += 1
            elif dif == 3:
                threes += 1
            else:
                print("What am i doing here")
            current = item
        return ones * threes

def reach_the_end(numbers, current, target):
    pass


def ten_b():
    with open("input_10.txt", "r") as f:
        bag = sorted([int(x) for x in f.read().split('\n')], reverse=True)
        bag.append(0)
        start = bag[0] + 3
        total = {start: 1}
        for item in bag:
            total[item] = 0
            for i in range(1, 4):
                if item + i in total:
                    total[item] += total[item+i]
        return total[0]
 
print(ten_b())