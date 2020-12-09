from collections import defaultdict

def eight_a():
    program = defaultdict(list)
    accumulator = 0
    with open("input_8.txt", "r") as f:
        cnt = 0
        line = f.readline()
        while line:
            a, b = line.strip().split(" ")
            program[cnt] = {"cmd": a, "val": b}
            line = f.readline()
            cnt += 1
    index = 0
    visited = set()
    while True:
        if index in visited:
            print(f"I reached a loop, whoops -- {accumulator}")
            break
        command = program[index]
        visited.add(index)
        if command["cmd"] == "nop":
            index += 1
        elif command["cmd"] == "jmp":
            val = int(command["val"][1:])
            if command["val"][0] == "-":
                val = -val
            index += val
        elif command["cmd"] == "acc":
            val = int(command["val"][1:])
            if command["val"][0] == "-":
                val = -val
            accumulator += val
            index += 1


def eight_b():
    with open("input_8.txt", "r") as f:
        pass


print(eight_a())