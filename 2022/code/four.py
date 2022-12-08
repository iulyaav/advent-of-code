def main(arg: str, data: str):
    overlapping = 0
    if arg == "a":
        rule = lambda x, y: (x[0] >= y[0] and x[1] <= y[1]) or (y[0] >= x[0] and y[1] <= x[1])
    else:
        rule = lambda x, y: list(set(range(x[0], x[1]+1)) & set(range(y[0], y[1]+1)))
    
    for line in data.split('\n'):
        elf1, elf2 = line.split(',')
        elf1 = [int(x) for x in elf1.split('-')]
        elf2 = [int(x) for x in elf2.split('-')]
        if rule(elf1, elf2):
            overlapping += 1
    
    print(overlapping)