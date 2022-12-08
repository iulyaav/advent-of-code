from collections import deque

def main(arg: str, data: str):
    rules = []
    stack_data = []
    for line in data.split('\n'):
        if line.startswith("move"):
            rules.append(line)
        elif line == "":
            # breakline
            continue
        else:
            stack_data.append(line)

    num_stacks = int(stack_data.pop().strip().split(' ')[-1])
    stacks = []
    for i in range(num_stacks):
        if arg == "a":
            stacks.append(deque())
        else:
            stacks.append([])
    
    for line in stack_data:
        split_line = list(line)
        index = 0
        for i in range(1, len(split_line), 4):
            if split_line[i].isupper():
                stacks[index].append(split_line[i])
            index += 1
    for rule in rules:
        rule = rule.split(' ')
        how_many, source, dest = [int(rule[1]), int(rule[3]) - 1, int(rule[5]) - 1]
        if arg == "a":
            for i in range(how_many):
                current = stacks[source].popleft()
                stacks[dest].appendleft(current)
        else:
            current = stacks[source][:how_many]
            stacks[source] = stacks[source][how_many:]
            stacks[dest] = current + stacks[dest]
    
    print("".join([x[0] for x in stacks]))
        